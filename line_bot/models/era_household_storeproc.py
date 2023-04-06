# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ERAHouseholdStoreproc(models.Model):
    _name = "era.line_storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genoverdue(memberid int) cascade""")
        self._cr.execute("""create or replace function genoverdue(memberid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            acc_cur refcursor ;
            acc_rec record ;
            pay_cur refcursor ;
            pay_rec record ;
            ncount int ;
            ardate date ;
            mindate date ;
            nowtoday date ;
            nowday int ;
            arday int ;
          BEGIN
            select date_part('day',ar_date)::INT into arday from era_household_member where id=memberid ; 
            select current_timestamp::DATE into nowtoday ;
            select date_part('day',nowtoday)::INT into nowday ;
            select count(*) into ncount from era_member_account where id not in (select distinct acc_id from era_member_account_payment_rel) and account_active=True and member_id=memberid ;
            if ncount >= 2 and nowday >= arday then
               myres = True ;
            else
               myres = False ;
            end if ; 
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")
