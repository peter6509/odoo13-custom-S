# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api


class ACMEGhIotTrigger(models.Model):
    _name = "alldo_acme_iot.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_outsuborder() cascade""")
        self._cr.execute("""create  or replace function insert_outsuborder() returns trigger as $BODY$
          DECLARE
             mynowdate date ;
          BEGIN
             if NEW.prod_date is null then
                select current_timestamp::DATE into NEW.prod_date ;
             end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 alldo_acme_iot_outsuborder 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_outsuborder on alldo_acme_iot_outsuborder;""")
        self._cr.execute("""create trigger insert_outsuborder before insert on alldo_acme_iot_outsuborder
                                 for each row execute procedure insert_outsuborder();""")

        self._cr.execute("""drop function if exists insert_electronic_scale() cascade""")
        self._cr.execute("""create  or replace function insert_electronic_scale() returns trigger as $BODY$
         DECLARE
            mynowdate date ;
         BEGIN
           execute gendayscale(NEW.id) ;
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 針對每次新增 alldo_acme_iot_electronic_scale 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_electronic_scale on alldo_acme_iot_electronic_scale;""")
        self._cr.execute("""create trigger insert_electronic_scale after insert on alldo_acme_iot_electronic_scale
                                         for each row execute procedure insert_electronic_scale();""")

        self._cr.execute("""drop function if exists upqty_sale_order_line() cascade""")
        self._cr.execute("""create  or replace function upqty_sale_order_line() returns trigger as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           if coalesce(NEW.qty_delivered,0) >= coalesce(NEW.product_uom_qty,0) then
              NEW.is_completed=TRUE ;
           else
              NEW.is_completed=FALSE ;  
           end if ;
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 針對每次新增 sale_order_line 作動一次 trigger
        self._cr.execute("""drop trigger if exists upqty_sale_order_line on sale_order_line;""")
        self._cr.execute("""create trigger upqty_sale_order_line before update of qty_delivered on sale_order_line
                                                 for each row execute procedure upqty_sale_order_line();""")

