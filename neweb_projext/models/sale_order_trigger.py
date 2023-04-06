# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class SaleOrderTrigger(models.Model):
    _name = "sale.order.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists check_discountamount() cascade""")
        self._cr.execute("""create  or replace function check_discountamount() returns trigger as $BODY$
          DECLARE
            saleno varchar ;
            disamount float ;
            totamount float ;
            ncount int ;
            projid int ;
            status1 varchar ;
            saledesc varchar ;
            projdesc varchar ;
            saleid int ;
          BEGIN
            if NEW.discount_amount != OLD.discount_amount then
                saleid = OLD.id ;
                select name,discount_amount into saleno,disamount from sale_order where id=saleid ;
                select count(*) into ncount from neweb_project  where sale_no=saleno ;
                if ncount > 0 then
                   select id into projid from neweb_project  where sale_no=saleno ;
                   select sum(analysis_revenue) into totamount from neweb_projanalysis where analysis_id=projid ; 
                   if abs(round(disamount::numeric/1.05::numeric) - totamount) > 5 then
                      saledesc = concat('NT$',round((disamount::numeric/1.05::numeric),0)::TEXT,';') ;
                      projdesc = concat('NT$',totamount::TEXT) ;
                      status1 = concat('收入不平,報價單優惠總價(未稅)',saledesc,'成本分析收入總價(未稅)',projdesc) ;
                      update neweb_project set proj_status1=status1 where id = projid ;
                   else
                      update neweb_project set proj_status1='Balance' where id = projid ;   
                   end if ;
                end if ;  
            end if ;    
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists insert_stockpicking() cascade""")

        # 針對每次更新 sale.order discount_amount優惠總價 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_on_sale_discount on sale_order ;""")
        self._cr.execute("""create trigger update_on_sale_discount after update on sale_order
                                 for each row execute procedure check_discountamount();""")

        self._cr.execute("""drop trigger if exists insert_on_stock_picking on stock_picking""")

        # self._cr.execute("""drop function if exists chk_dup_so() cascade""")
        # self._cr.execute("""create  or replace function chk_dup_so() returns trigger as $BODY$
        #   DECLARE
        #     ncount int ;
        #     preso varchar ;
        #     maxso varchar ;
        #     prenew varchar ;
        #     newnum int ;
        #     newname varchar ;
        #   BEGIN
        #     select count(*) into ncount from sale_order where name=NEW.name ;
        #     if ncount >= 1 then
        #        select max(name) into maxso from sale_order ;
        #        select substring(maxso,9,2) into prenew ;
        #        select substring(NEW.name,1,8) into preso ;
        #        newnum = prenew::integer + 1 ;
        #        newname = concat(preso,lpad(newnum::TEXT,2,'0')::TEXT) ;
        #        NEW.name = newname ;
        #        update ir_sequence set number_next=newnum + 1 where code='sale.order' ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists chk_dup_so_name on sale_order ;""")
        # self._cr.execute("""create trigger chk_dup_so_name before update of name on sale_order
        #                                  for each row execute procedure chk_dup_so();""")

        self._cr.execute("""drop function if exists update_on_openaccountday1() cascade""")
        self._cr.execute("""create  or replace function update_on_openaccountday1() returns trigger as $BODY$
          DECLARE
            rday1 int ;
            sday1 int ;
            pday1 int ;
          BEGIN
            select open_account_day1 into rday1 from res_partner where id=NEW.partner_id ;
            if NEW.open_account_day1 != rday1 then
               update res_partner set open_account_day1=NEW.open_account_day1 where id = NEW.partner_id ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次更新 sale.order open_account_day1 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_on_openaccountday1 on sale_order ;""")
        self._cr.execute("""create trigger update_on_openaccountday1 after update of open_account_day1 on sale_order
                                         for each row execute procedure update_on_openaccountday1();""")


