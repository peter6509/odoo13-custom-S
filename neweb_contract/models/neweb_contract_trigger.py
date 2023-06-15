# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebContractTrigger(models.Model):
    _name = "neweb.contract_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_contract_change() cascade""")
        self._cr.execute("""create  or replace function insert_contract_change() returns trigger as $BODY$
          DECLARE
             mynowdate date;
          BEGIN
             select now()::DATE into mynowdate;
             if NEW.contract_line_id is not null then
                 insert into neweb_contract_contract_line_change(contract_id,contract_line_id,change_date) values(NEW.contract_id,NEW.contract_line_id,mynowdate);
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists insert_contract_change on neweb_contract_contract_line1 ;""")
        self._cr.execute("""create trigger insert_contract_change after update on neweb_contract_contract_line1
                                 for each row execute procedure insert_contract_change();""")

