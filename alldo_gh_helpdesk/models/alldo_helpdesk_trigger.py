# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class AlldoHelpDeskMgmtTrigger(models.Model):
    _name = "alldo.helpdesk.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_helpdesk_cdate() cascade;""")
        self._cr.execute("""create or replace function insert_helpdesk_cdate() returns trigger as $$
            begin
                update helpdesk_ticket set cdate = NEW.create_date::DATE where id = NEW.id;
                return NEW;
            end;
            $$ language plpgsql;""")


        # 針對每次新增 helpdesk.ticket wk_id/po_id 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_helpdesk_cdate on helpdesk_ticket ;""")
        self._cr.execute("""create trigger insert_helpdesk_cdate after insert on helpdesk_ticket
                                         for each row execute procedure insert_helpdesk_cdate();""")
