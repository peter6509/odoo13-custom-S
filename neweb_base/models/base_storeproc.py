# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class BaseStoreproc(models.Model):
    _name = "base.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists ckcustomcredit(mycompname varchar,mycapital varchar,myvat varchar,mycredit varchar) cascade""")
        self._cr.execute("""create or replace function ckcustomcredit(mycompname varchar,mycapital varchar,myvat varchar,mycredit varchar) returns void as $BODY$
         DECLARE
           ncount int ;
           maxid int ;
           cusid int ;
           ncapital float ;
           ncreditlimit float ;
         BEGIN
           if trim(mycapital) !='' then
              ncapital = mycapital::numeric ;
           else
              ncapital = 0 ;   
           end if ;
           if mycredit != '-' then 
               ncreditlimit = mycredit::numeric ;
               select count(*),max(id) into ncount,maxid from res_partner where name=mycompname and is_company=True ;
               if ncount = 0 then
                  select count(*),max(id) into ncount,maxid from res_partner where vat=myvat  and is_company=True ;
                  if ncount > 0 then
                     update res_partner set credit_limit=ncreditlimit,paidup_capital=ncapital where id=maxid ;
                  end if ;
               else   
                  update res_partner set credit_limit=ncreditlimit,paidup_capital=ncapital where id=maxid ;
               end if ;
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")
