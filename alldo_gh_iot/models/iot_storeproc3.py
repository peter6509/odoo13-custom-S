# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iotstoreproc3(models.Model):
    _name = "alldo_gh_iot.storeproc3"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getprodrealnum(prodid int,engtype varchar) cascade""")
        self._cr.execute("""create or replace function getprodrealnum(prodid int,engtype varchar) returns INT as $BODY$
        DECLARE
           myres int ;
        BEGIN 
           select coalesce(prod_real_num,0) into myres from alldo_gh_iot_eng_order where prod_id=prodid and eng_type=engtype ;
           if myres is null then
               myres = 0 ;
           end if ;
            return myres ;
        END;$BODY$  
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getreprealtime(prodid int,engtype varchar) cascade""")
        self._cr.execute("""create or replace function getreprealtime(prodid int,engtype varchar) returns INT as $BODY$
        DECLARE
           myres int ;
        BEGIN 
           select coalesce(replace_real_time,0) into myres from alldo_gh_iot_eng_order where prod_id=prodid and eng_type=engtype ;
           if myres is null then
               myres = 0 ;
           end if ;
            return myres ;
        END;$BODY$  
        LANGUAGE plpgsql;""")
