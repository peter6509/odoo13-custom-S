# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api

class cloudrentcarecallTrigger(models.Model):
    _name = "cloudrent.carecall_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_cloudrent_member_carecall() cascade""")
        self._cr.execute("""create  or replace function insert_cloudrent_member_carecall() returns trigger as $BODY$
          DECLARE
            cdate varchar ;
          BEGIN
            select NEW.care_date::TEXT into cdate ;
            NEW.care_date1=cdate ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 cloudrent_member_carecall  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_cloudrent_member_carecall on cloudrent_member_care ;""")
        self._cr.execute("""create trigger insert_cloudrent_member_carecall before insert on cloudrent_member_care
                                 for each row execute procedure insert_cloudrent_member_carecall();""")
