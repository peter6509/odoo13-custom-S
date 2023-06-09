# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebContractIhheritWizard(models.TransientModel):
    _name = "neweb_contract.contract_inherit_wizard"
    _description = "續約帶入第四頁籤有序號之數據"

    origin_contract_id = fields.Many2one('neweb_contract.contract',string="COPY來源合約",required=True)

    def run_inherit_copy(self):
        newconid = self.env.context.get('newcontractid')
        if self.origin_contract_id.id == newconid :
            raise UserError("來源合約與目標合約相同,請重新選擇")
        if newconid:
            self.env.cr.execute("""select gencontractinherit4(%d,%d)""" % (self.origin_contract_id.id,newconid))
            self.env.cr.execute("""commit""")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message']='序號資料已帶入'
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