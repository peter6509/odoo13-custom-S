# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentmemberlinewizard(models.TransientModel):
    _name = "cloudrent_household.member_line_wizard"

    @api.depends()
    def _get_billym(self):
        myrec = self.env['cloudrent.household_config'].search([])
        if myrec:
            mybillym = myrec.bill_ym
            self.bill_ym = myrec.bill_ym
            return mybillym


    project_no = fields.Many2one('cloudrent.household_house',string="專案名稱",required=True)
    bill_ym = fields.Char(size=7,string="年-月(YYYY-MM)",required=True,default=_get_billym)

    def run_member_line(self):
        myrec = self.env['cloudrent.household_config'].search([])
        if myrec:
            mybillym = myrec.bill_ym
        if self.bill_ym > mybillym:
            raise UserError("輸入的年-月 %s 超過目前待結帳年月 %s ,請確認" % (self.bill_ym,mybillym))
        # mybillm = self.bill_ym[5:7]
        # mybilly = self.bill_ym[0:4]
        # if mybillm == '01':
        #     mybillym = str(int(mybilly) - 1) + '-12'
        # else:
        #     mybillym = mybilly + '-' + (str(int(mybillm) - 1)).zfill(2)

        self.env.cr.execute("""select genmemberline(%d,'%s')""" % (self.project_no.id,mybillym))
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '住戶費用 LINE 通知帳務產生成功,準備發送 LINE MESSAGE！'
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



