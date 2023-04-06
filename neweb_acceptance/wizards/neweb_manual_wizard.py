# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebManualWizard(models.TransientModel):
    _name = "neweb_acceptance.manual_wizard"

    passcode = fields.Char(string="PASSCODE")

    def run_manual_work(self):
        if self.passcode != '!99999ibm':
            raise UserError("PASSCODE Error!")
        self.env.cr.execute("""select genprojacceptance()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_purno_supp()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genprojinvcomplete()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genaccsecurity()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genacceptancedate()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genacceptanceemail()""")
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='手動產生專案貨品狀態清單完成'
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
