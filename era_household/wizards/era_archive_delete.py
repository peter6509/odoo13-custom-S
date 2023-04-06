# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class EraArchiveDelete(models.TransientModel):
    _name = "era.archive_delete"

    passcode = fields.Char(string="PASSCODE")

    def run_archive_delete(self):
        if self.passcode != '!99999ibm':
            raise UserError("PASSCODE Error!")

        self.env.cr.execute("""delete from era_member_line_user where active=FALSE ;""")
        self.env.cr.execute("""delete from era_household_member where active=FALSE ;""")
        # self.env.cr.execute("""delete from res_users where active=FALSE ;""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='歸檔數據刪除完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }