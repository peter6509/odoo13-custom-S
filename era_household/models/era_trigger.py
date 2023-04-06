# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class EraTrigger(models.Model):
    _name = "era.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_eraemeter() cascade""")
        # self._cr.execute("""create  or replace function insert_eraemeter() returns trigger as $BODY$
        #   DECLARE
        #     ncount int ;
        #     emetername varchar ;
        #     emeterhubid int ;
        #   BEGIN
        #     select count(*) into ncount from era_household_electric_meter where id=NEW.emeter_id ;
        #     if ncount > 0 then
        #        select substring(emeter_name,1,8) into emetername from era_household_electric_meter where id=NEW.emeter_id ;
        #        select id into emeterhubid from era_emeterhub_status where pi_id=emetername ;
        #        if emeterhubid is not null then
        #           NEW.emeter_id1=emeterhubid ;
        #        end if ;
        #     end if ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        # 針對每次新增 era_emeter_status  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_emeter_status on era_emeter_status ;""")
        # self._cr.execute("""create trigger insert_emeter_status before insert on era_emeter_status
        #                          for each row execute procedure insert_eraemeter();""")

        self._cr.execute("""drop function if exists update_member_pid() cascade""")
        self._cr.execute("""create  or replace function update_member_pid() returns trigger as $BODY$
          DECLARE
            ncount int ;
            emetername varchar ;
            emeterhubid int ;
          BEGIN
            select count(*) into ncount from res_users where id = NEW.user_id ;
            if ncount > 0 then
               update res_users set password=NEW.member_pid where id = NEW.user_id ;
            end if ;   
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次變更身分字號 異動 res.user password
        self._cr.execute("""drop trigger if exists update_member_pid on era_household_member ;""")
        self._cr.execute("""create trigger update_member_pid after update of member_pid on era_household_member
                                        for each row execute procedure update_member_pid();""")

        self._cr.execute("""drop function if exists insert_member_income_emeter() cascade""")
        self._cr.execute("""create  or replace function insert_member_income_emeter() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            if NEW.in_used=null  then
               NEW.in_used = True ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 era_member_income_emeter  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_member_income_emeter on era_member_income_emeter ;""")
        self._cr.execute("""create trigger insert_member_income_emeter before insert on era_member_income_emeter
                                         for each row execute procedure insert_member_income_emeter();""")

