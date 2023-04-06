# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotshippingreportwizard(models.TransientModel):
    _name = "alldo_ipla_iot.shipping_report_wizard"
    _description = "列印出貨單精靈"

    partner_id = fields.Many2one('res.partner',string="客戶")
    report_type = fields.Selection([('1','新單'),('2','舊單')],string="列印模式",default='1')
    report_date = fields.Date(string="出貨日期",default=fields.Date.today())
    report_no = fields.Char(string="出貨單號")

    def run_shipping_report(self):
        if self.report_type=='1' and not self.partner_id:
            raise UserError("新單列印要輸入客戶")
        if self.report_type=='2' and not self.report_no:
            raise UserError("舊單列印必需輸入出貨單號")
        self.env.cr.execute("""delete from alldo_ipla_iot_stockpicking_report""")
        self.env.cr.execute("""commit""")
        if self.report_type=='1':     # 新單
            self.env.cr.execute("""select ckshipping(%d)""" % self.partner_id.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
                myrec = self.env['alldo_ipla_iot.stockpicking_report']
                if not self.report_date:
                    myrec.create({'partner_id': self.partner_id.id})
                else:
                    myrec.create({'partner_id': self.partner_id.id,'report_date': self.report_date})
                self.env.cr.execute("""select gennewshipping(%d)""" % self.partner_id.id)
                self.env.cr.execute("""commit""")
            else:
                raise UserError("目前沒有新單可供列印！")
        else:                         # 舊單
            self.env.cr.execute("""select genoldshipping('%s')""" % (self.report_no))
            self.env.cr.execute("""commit""")

        myrec = self.env['alldo_ipla_iot.stockpicking_report'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_ipla_iot.ipla_iot_shipping_report_action')
        return {'view_name': 'ipla_iot_shipping_report_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_ipla_iot.stockpicking_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form'
                }