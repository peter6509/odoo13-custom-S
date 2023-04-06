# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebstockintrigger(models.Model):
    _name = "neweb.stockin_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genproddefault() cascade""")
        self._cr.execute("""create  or replace function genproddefault() returns trigger as $BODY$
          DECLARE
             ncount int ;
          BEGIN
             if NEW.default_code is null then
                update product_template set default_code=coalesce(name,' ') where id = NEW.id ;
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_on_proddefault on product_template ;""")
        self._cr.execute("""create trigger insert_on_proddefault after insert on product_template
                                     for each row execute procedure genproddefault();""")


        self._cr.execute("""drop function if exists gendelstockoutlist() cascade""")
        self._cr.execute("""create  or replace function gendelstockoutlist() returns trigger as $BODY$
          DECLARE
             ncount int ;
          BEGIN
             execute unlinkstockoutlist2(OLD.id) ;
             return OLD ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists delete_on_stockoutlist on neweb_stockout_list ;""")
        self._cr.execute("""create trigger delete_on_stockoutlist before delete on neweb_stockout_list
                                             for each row execute procedure gendelstockoutlist();""")

        self._cr.execute("""drop function if exists gendelstockshippinglist() cascade""")
        self._cr.execute("""create  or replace function gendelstockshippinglist() returns trigger as $BODY$
         DECLARE
            ncount int ;
         BEGIN
           /* execute unlinkstockoutlist1(OLD.id) ; */
           return OLD ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists delete_on_stockshippinglist on neweb_stockship_list ;""")
        #self._cr.execute("""create trigger delete_on_stockshipinglist before delete on neweb_stockship_list
        #                                           for each row execute procedure gendelstockshippinglist();""")

        self._cr.execute("""drop function if exists insert_on_stockout_list() cascade""")
        self._cr.execute("""create  or replace function insert_on_stockout_list() returns trigger as $BODY$
          DECLARE
             ncount int ;
             cdate date ;
          BEGIN
             if NEW.stockout_num > 0 then
                if NEW.create_date is not null then
                   select (NEW.create_date + interval'8 hour')::DATE into cdate ;
                   update neweb_projsaleitem set stockout_date=cdate where id = NEW.stockout_sequence_id ;
                end if ;   
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_on_stockout_list on neweb_stockout_list ;""")
        self._cr.execute("""create trigger insert_on_stockout_list after insert on neweb_stockout_list
                                             for each row execute procedure insert_on_stockout_list();""")

        self._cr.execute("""drop function if exists delete_on_stockout_list() cascade""")
        self._cr.execute("""create  or replace function delete_on_stockout_list() returns trigger as $BODY$
          DECLARE
             ncount int ;
             ncount1 int ;
             cdate date ;
             saleitemid int ;
             accid int ;
          BEGIN
             update neweb_projsaleitem set stockout_date=null where id = OLD.stockout_sequence_id ;
             select count(*) into ncount from neweb_acceptance_line where projsaleitem_id = OLD.stockout_sequence_id and active=TRUE ;
             if ncount > 0 then
                select acceptance_id into accid from neweb_acceptance_line where projsaleitem_id = OLD.stockout_sequence_id and active=TRUE ;
                delete from neweb_acceptance_line where projsaleitem_id = OLD.stockout_sequence_id and active=TRUE ;
             end if ;
             select count(*) into ncount1 from neweb_acceptance_line where acceptance_id = accid and active=TRUE ;
             if ncount1 = 0 then
                delete from neweb_acceptance where id = accid and active=TRUE ;
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists delete_on_stockout_list on neweb_stockout_list ;""")
        self._cr.execute("""create trigger delete_on_stockout_list after delete on neweb_stockout_list
                                                     for each row execute procedure delete_on_stockout_list();""")

        self._cr.execute("""drop function if exists insert_on_stockin_list() cascade""")
        self._cr.execute("""create  or replace function insert_on_stockin_list() returns trigger as $BODY$
          DECLARE
             ncount int ;
             cdate date ;
             psaleitemid int ;
          BEGIN
             if NEW.stockin_num > 0 then
                if NEW.create_date is not null then
                   select (NEW.create_date + interval'8 hour')::DATE into cdate ;
                   select pitem_origin_id into psaleitemid from neweb_pitem_list where id = NEW.stockin_sequence_id ;
                   update neweb_projsaleitem set stockin_date=cdate where id = psaleitemid ;
                end if ;   
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_on_stockin_list on neweb_stockin_list ;""")
        self._cr.execute("""create trigger insert_on_stockin_list after insert on neweb_stockin_list
                                                     for each row execute procedure insert_on_stockin_list();""")

        self._cr.execute("""drop function if exists delete_on_stockin_list() cascade""")
        self._cr.execute("""create  or replace function delete_on_stockin_list() returns trigger as $BODY$
          DECLARE
             psaleitemid int ;
          BEGIN
             select pitem_origin_id into psaleitemid from neweb_pitem_list where id = OLD.stockin_sequence_id ;
             update neweb_projsaleitem set stockin_date=null where id = psaleitemid ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists delete_on_stockin_list on neweb_stockint_list ;""")
        self._cr.execute("""create trigger delete_on_stockin_list after delete on neweb_stockin_list
                                                             for each row execute procedure delete_on_stockin_list();""")



