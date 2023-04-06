# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class cloudrentcontractwizard(models.TransientModel):
    _name = "cloudrent.contract_wizard"
    _description = "合約啟始及押金設定"

    member_id = fields.Many2one('cloudrent.household_member',string="租戶",required=True)
    emeter_220v_start = fields.Float(digits=(10,2),string="220V啟始度數",default=0.0)
    emeter_110v_start = fields.Float(digits=(10,2),string="110V啟始度數",default=0.0)
    member_deposit = fields.Float(digits=(10,0),string="租戶押金",default=0)

    def gen_contract_start(self):
        self.env.cr.execute("""select gencontractstart(%d,%s,%s,%s)""" % (self.member_id.id,self.emeter_220v_start,self.emeter_110v_start,self.member_deposit))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '租戶：[%s]%s 啟始數據設定完成 ！' % (self.member_id.member_no,self.member_id.member_name)
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }
