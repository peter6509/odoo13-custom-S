# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime

class acmeaccountmovewizard(models.TransientModel):
    _name = "alldo_acme_iot.accountmove_wizard"

    partner_id = fields.Many2one('res.partner',string="客戶",required=True)
    report_type = fields.Selection([('1','新單'),('2','舊單')],string="印表類型",default='1')
    report_no = fields.Char(string="單號")
    start_date = fields.Date(string="啟始日期",default=datetime.today())
    end_date = fields.Date(string="截止日期",default=datetime.today())

    def run_accountmove(self):
        if self.report_type=='1':
            if not self.start_date or not self.end_date:
                raise UserError("印新對帳單必須輸入對帳銷貨起訖日期！")
            self.env.cr.execute("""select gen_accountmove(%d,'%s','%s')""" % (self.partner_id.id,self.start_date,self.end_date))
            self.env.cr.execute("""commit""")
        else:
            if not self.report_no:
                raise UserError("印舊單必須輸入要列印的對帳單號！")
            self.env.cr.execute("""select gen_accountmove1(%d,'%s')""" % (self.partner_id.id, self.report_no))
            self.env.cr.execute("""commit""")

        myrec = self.env['alldo_acme_iot.accountmove_selectitem'].search([])
        myid = myrec[0].id
        return {'view_name': 'views_accountmove_selectitem_action',
                'name': (u'Account Move Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_acme_iot.accountmove_selectitem',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'self',
                'view_mode': 'form',
                'view_type': 'form'
                }