# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class cloudrentstoreproc1(models.Model):
    _name = "cloudrent.storeproc1"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists chkrepairgrant(grantid int,startdt date,enddt date,grantamount float) cascade""")
        self._cr.execute("""create or replace function chkrepairgrant(grantid int,startdt date,enddt date,grantamount float) returns Boolean as $BODY$
          DECLARE
            mytoday date ;
            ncount int ;
            myres Boolean ;
          BEGIN
            select current_timestamp::DATE + interval '1 day' into mytoday ;
            update cloudrent_repair_grant_line set grant_active=FALSE where grant_end::DATE < mytoday::DATE and grant_id=grantid and grant_active=True ;
            select count(*) into ncount from cloudrent_repair_grant_line where grant_id=grantid and grant_start::DATE = startdt::DATE and 
               grant_end::DATE=enddt::DATE and grant_amount=grantamount ;
            if ncount = 0 then
               myres = False ;    /* 不存在相同補助款 */
            else
               myres = True ;     /* 補助款已建檔 */
            end if ;  
            return myres ;  
          END;$BODY$
          LANGUAGE plpgsql;""")


