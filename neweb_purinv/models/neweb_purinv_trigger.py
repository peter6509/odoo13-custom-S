# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class PurinvTrigger(models.Model):
    _name = "neweb_purinv.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists geninvlineitem() cascade""")
        self._cr.execute("""create  or replace function geninvlineitem() returns trigger as $BODY$
          DECLARE
            maxid int ;
            ncount int ;
            paydate date ;
          BEGIN
            maxid = 1 ;
            select count(*) into ncount from neweb_purinv_invoiceline where invline_id = NEW.invline_id ;
            if ncount > 0 then
               select max(coalesce(invline_item,0)) + 1 into NEW.invline_item from neweb_purinv_invoiceline where invline_id = NEW.invline_id ;
            else
               NEW.invline_item = 1 ;   
            end if ;
            if NEW.invoice_date is not null and NEW.inv_paymentterm is null then
               select get_invoicedate1(NEW.id) into paydate ;
            end if ;
            update neweb_purinv_invoiceline set inv_paymentterm=paydate where id=NEW.id and inv_paymentterm is null ;
            /* update neweb_purinv_invoiceline set invline_item = maxid where id=NEW.id ; */
           return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_on_invoiceline on neweb_purinv_invoiceline ;""")
        self._cr.execute("""create trigger insert_on_invoiceline before insert on neweb_purinv_invoiceline
                                 for each row execute procedure geninvlineitem();""")

        self._cr.execute("""drop function if exists cal_suppayterm1() cascade""")
        self._cr.execute("""create or replace function cal_suppayterm1() returns trigger as $BODY$
         DECLARE
           paydate date ;
         BEGIN
           select get_invoicedate1(NEW.id) into paydate ;
           update neweb_purinv_invoiceline set inv_paymentterm=paydate where id=NEW.id and inv_paymentterm is null  ;
           return NEW;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_invoicedate_invoiceline on neweb_purinv_invoiceline ;""")
        self._cr.execute("""create trigger update_invoicedate_invoiceline after update of invoice_date on neweb_purinv_invoiceline
                                         for each row execute procedure cal_suppayterm1();""")

