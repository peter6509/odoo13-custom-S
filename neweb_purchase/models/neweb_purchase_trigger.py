# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebpurchaseTrigger(models.Model):
    _name = "neweb.purchase_trigger"

    @api.model
    def init(self):
        # self._cr.execute("""update purchase_order set purchase_reciver='Annie.Lee_李玉菁' ;""")
        self._cr.execute("""drop function if exists genpitemlitem() cascade""")
        self._cr.execute("""create  or replace function genpitemlitem() returns trigger as $BODY$
          DECLARE
             maxid float ;
             ncount int ;
             paydate date ;
             empid int ;
             preciver varchar ;
          BEGIN
             maxid = 1.0 ;
             select count(*) into ncount from neweb_pitem_list where pitem_id = NEW.pitem_id ;
             if ncount > 0 then
               /* select max(coalesce(pitem_litem,0.0)) + 1 into maxid from neweb_pitem_list where pitem_id = NEW.pitem_id ; */
               update neweb_pitem_list set pitem_litem = ncount where id = NEW.id ;
             end if ;
             
             select max(name) into empid from neweb_purchase_purchase_manager ;
             select name into preciver from hr_employee where id = empid ;
             update purchase_order set purchase_reciver=preciver where id = NEW.pitem_id and purchase_reciver is null ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists insert_on_pitemlitem on neweb_pitem_list ;""")
        self._cr.execute("""create trigger insert_on_pitemlitem after insert on neweb_pitem_list
                                 for each row execute procedure genpitemlitem();""")

        self._cr.execute("""drop function if exists genallpitemlitem() cascade""")
        self._cr.execute("""create or replace function genallpitemlitem() returns void as $BODY$
          DECLARE
            p_cur refcursor ;
            p_rec record ;
            pl_cur refcursor ;
            pl_rec record ;
            maxitem float ;
            ncount int ;
          BEGIN
            open p_cur for select id from purchase_order ;
            loop
              fetch p_cur into p_rec ;
              exit when not found ;
              maxitem = 1.0 ;
              open pl_cur for select id,sequence,pitem_litem from neweb_pitem_list where pitem_id=p_rec.id order by sequence,id ;
              loop
                fetch pl_cur into pl_rec ;
                exit when not found ;
                update neweb_pitem_list set pitem_litem = maxitem where id = pl_rec.id ;
                maxitem = maxitem + 1 ;
              end loop ;
              close pl_cur ;
            end loop ;
            close p_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpitemlitem1(purid int) cascade""")
        self._cr.execute("""create or replace function genpitemlitem1(purid int) returns void as $BODY$
         DECLARE
           maxitem float ;
           maxid int ;
           ncount int ;
           pl_cur refcursor ;
           pl_rec record ;
         BEGIN
           maxitem = 1.0 ;
           maxid = 1 ;
           open pl_cur for select id,pitem_litem from neweb_pitem_list where pitem_id=purid order by pitem_litem,id ;
           loop
             fetch pl_cur into pl_rec ;
             exit when not found ;
             update neweb_pitem_list set pitem_item=maxid,pitem_litem=maxitem where id = pl_rec.id ;
             maxid = maxid + 1 ;
             maxitem = maxitem + 1 ;
           end loop ;
           close pl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delpitemlist() cascade""")
        self._cr.execute("""create  or replace function delpitemlist() returns trigger as $BODY$
          DECLARE
             maxid float ;
             ncount int ;
             paydate date ;
          BEGIN
             execute purchaseitemunlink(OLD.pitem_id) ; 
             return OLD ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists delete_on_pitemlist on neweb_pitem_list ;""")
        self._cr.execute("""create trigger delete_on_pitemlist before delete on neweb_pitem_list
                                        for each row execute procedure delpitemlist();""")

        self._cr.execute("""drop function if exists genpurchaselineid() cascade""")
        self._cr.execute("""create or replace function genpurchaselineid() returns trigger as $BODY$
          DECLARE
            po varchar ;
            poid int ;
            plineid int ;
            ptypeid int ;
          BEGIN
            select picking_type_id into ptypeid from stock_picking where id = NEW.picking_id ;
            if NEW.product_id not in (1,2) and ptypeid=1 and NEW.purchase_line_id is null then
               select origin into po from stock_picking where id = NEW.picking_id ;
               select id into poid from purchase_order where name=po ;
               select id into plineid from purchase_order_line where product_id=NEW.product_id and order_id=poid ;
               update stock_move set purchase_line_id=plineid where id = NEW.id ; 
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_on_stockmove on stock_move ;""")
        self._cr.execute("""create trigger insert_on_stockmove after insert on stock_move
                                         for each row execute procedure genpurchaselineid();""")

        self._cr.execute("""drop function if exists cal_pitembudget() cascade""")
        self._cr.execute("""create or replace function cal_pitembudget() returns trigger as $BODY$
        DECLARE
          ncount int ;
        BEGIN
          NEW.pitem_budget=coalesce(NEW.pitem_num,0) * coalesce(NEW.pitem_price,0) ;
          return NEW;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_require_purchase_price on neweb_require_purchase_item ;""")
        self._cr.execute("""create trigger update_require_purchase_price before update of pitem_price on neweb_require_purchase_item
                                                for each row execute procedure cal_pitembudget();""")

        self._cr.execute("""drop trigger if exists update_require_purchase_num on neweb_require_purchase_item ;""")
        self._cr.execute("""create trigger update_require_purchase_num before update of pitem_num on neweb_require_purchase_item
                                                        for each row execute procedure cal_pitembudget();""")

        self._cr.execute("""drop function if exists cancel_purchase() cascade""")
        self._cr.execute("""create or replace function cancel_purchase() returns trigger as $BODY$
            DECLARE
              ncount int ;
              originid int ;
              p_cur refcursor ;
              p_rec record ;
            BEGIN
              if NEW.state='cancel' then
                 open p_cur for select id,pitem_origin_id,pitem_origin_type from neweb_pitem_list where pitem_id=NEW.id and pitem_origin_type='P' ;
                 loop
                   fetch p_cur into p_rec ;
                   exit when not found ;
                   update neweb_projsaleitem set purchase_no=null where id = p_rec.pitem_origin_id ;
                   update neweb_pitem_list set pitem_origin_id=null,pitem_origin_no=null where id=p_rec.id ;
                 end loop ;
                 close p_cur ;
              end if ;
              return NEW;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_purchase_state on purchase_order ;""")
        self._cr.execute("""create trigger update_purchase_state after update of state on purchase_order
                                                        for each row execute procedure cancel_purchase();""")
