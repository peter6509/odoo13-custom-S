# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class CloudRentTrigger(models.Model):
    _name = "cloudrent.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_cloudrent_linelog() cascade""")
        self._cr.execute("""create  or replace function insert_cloudrent_linelog() returns trigger as $BODY$
          DECLARE
            ncount int ;
            mymemberid int ;
            mymembertype char ;
          BEGIN
            select count(*) into ncount from cloudrent_member_line_user where line_user_id=NEW.line_id ;
            if ncount > 0 then
               select max(member_id) into mymemberid from cloudrent_member_line_user where line_user_id=NEW.line_id ;
               select max(member_type) into mymembertype from cloudrent_household_member where id = mymemberid ;
               NEW.member_id = mymemberid ;
               NEW.member_type = mymembertype ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 cloudrent_linelog 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_cloudrent_linelog on cloudrent_linelog ;""")
        self._cr.execute("""create trigger insert_cloudrent_linelog before insert on cloudrent_linelog
                                 for each row execute procedure insert_cloudrent_linelog();""")

        self._cr.execute("""drop function if exists insert_cloudrent_paymentlog() cascade""")
        self._cr.execute("""create  or replace function insert_cloudrent_paymentlog() returns trigger as $BODY$
          DECLARE
            ncount int ;
            mymemberid int ;
            mymembertype char ;
          BEGIN
            select count(*) into ncount from cloudrent_member_line_user where line_user_id=NEW.line_id ;
            if ncount > 0 then
               select max(member_id) into mymemberid from cloudrent_member_line_user where line_user_id=NEW.line_id ;
               select max(member_type) into mymembertype from cloudrent_household_member where id = mymemberid ;
               NEW.member_id = mymemberid ;
               NEW.member_type = mymembertype ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 cloudrent_paymentlog 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_cloudrent_paymentlog on cloudrent_paymentylog ;""")
        self._cr.execute("""create trigger insert_cloudrent_paymentlog before insert on cloudrent_paymentlog
                                         for each row execute procedure insert_cloudrent_paymentlog();""")

        self._cr.execute("""drop function if exists insert_cloudrent_maintenancelog() cascade""")
        self._cr.execute("""create  or replace function insert_cloudrent_maintenancelog() returns trigger as $BODY$
          DECLARE
            ncount int ;
            mymemberid int ;
            mymembertype char ;
          BEGIN
            select count(*) into ncount from cloudrent_member_line_user where line_user_id=NEW.line_id ;
            if ncount > 0 then
               select max(member_id) into mymemberid from cloudrent_member_line_user where line_user_id=NEW.line_id ;
               select max(member_type) into mymembertype from cloudrent_household_member where id = mymemberid ;
               NEW.member_id = mymemberid ;
               NEW.member_type = mymembertype ;
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 cloudrent_maintenancelog 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_cloudrent_maintenancelog on cloudrent_maintenancelog ;""")
        self._cr.execute("""create trigger insert_cloudrent_maintenancelog before insert on cloudrent_maintenancelog
                                         for each row execute procedure insert_cloudrent_maintenancelog();""")
