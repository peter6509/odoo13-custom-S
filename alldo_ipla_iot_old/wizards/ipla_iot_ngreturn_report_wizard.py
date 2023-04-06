# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotngreturnreportwizard(models.TransientModel):
    _name = "alldo_ipla_iot.ngreturn_report_wizard"

    partner_id = fields.Many2one('res.partner',string="客戶",required=True)
    report_type = fields.Selection([('1','新單'),('2','舊單')],string="列印模式",default='1')
    report_start_date = fields.Date(string="起始日期",default=fields.Date.today(),required=True)
    report_end_date = fields.Date(string="截止日期",default=fields.Date.today(),required=True)
    report_date = fields.Date(string="製表日期",default=fields.Date.today())
    # report_no = fields.Char(string="退料單號")

    def run_ngreturn_report(self):
        mytype = self.report_type
        self.env.cr.execute("""select genngreturnselectitem('%s',%d,'%s','%s')""" % (mytype,self.partner_id.id,self.report_start_date,self.report_end_date))
        self.env.cr.execute("""commit""")


        myrec = self.env['alldo_ipla_iot.ngreturn_select'].search([])
        for rec in myrec:
            myid = rec.id

        myviewid = self.env.ref('alldo_ipla_iot.iplaiot_ngreturn_select_form')

        return {'view_name': 'ngreturn_report_action',
                'name': (u'NG return Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.ngreturn_select',
                'type': 'ir.actions.act_window',
                'context': self._context,
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form',
                }