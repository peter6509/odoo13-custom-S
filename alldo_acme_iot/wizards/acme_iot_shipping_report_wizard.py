# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotshippingreportwizard(models.TransientModel):
    _name = "alldo_acme_iot.shipping_report_wizard"
    _description = "列印出貨單精靈"

    partner_id = fields.Many2one('res.partner',string="客戶")
    report_type = fields.Selection([('1','新單'),('2','舊單'),('3','最後單號')],string="列印模式",default='1')
    report_date = fields.Date(string="出貨日期",default=fields.Date.today())
    report_no = fields.Char(string="出貨單號")
    report_type1 = fields.Selection([('1','出貨單'),('2','銷貨單')],string="類型",default='1')

    @api.onchange('report_type')
    def onchangereporttype(self):
        if not self.partner_id:
            mypartnerid = 0
        else:
            mypartnerid = self.partner_id.id
        self.env.cr.execute("""select shippingreport(%d)""" % mypartnerid)
        self.report_no = self.env.cr.fetchone()[0]

    def run_shipping_report(self):
        if self.report_type=='1' and not self.partner_id:
            raise UserError("新單列印要輸入客戶")
        if self.report_type=='2' and not self.report_no:
            raise UserError("舊單列印必需輸入出貨單號")
        self.env.cr.execute("""delete from alldo_acme_iot_stockpicking_report""")
        self.env.cr.execute("""commit""")
        if self.report_type=='1':     # 新單
            self.env.cr.execute("""select ckshipping(%d)""" % self.partner_id.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
                myrec = self.env['alldo_acme_iot.stockpicking_report']
                if not self.report_date:
                    myrec.create({'partner_id': self.partner_id.id,'report_type':self.report_type1})
                else:
                    myrec.create({'partner_id': self.partner_id.id,'report_type':self.report_type1,'report_date': self.report_date})
                self.env.cr.execute("""select gennewshipping(%d)""" % self.partner_id.id)
                self.env.cr.execute("""commit""")
            else:
                raise UserError("目前沒有新單可供列印！")
        elif self.report_type=='2' or self.report_type=='3' :                         # 舊單
            self.env.cr.execute("""select genoldshipping('%s','%s')""" % (self.report_no,self.report_type1))
            self.env.cr.execute("""commit""")
        # elif self.report_type=='3':
        #     A=1


        myrec = self.env['alldo_acme_iot.stockpicking_report'].search([])
        myid = myrec[0].id
        myviewid = self.env.ref('alldo_acme_iot.acme_iot_shipping_report_action')
        return {'view_name': 'acme_iot_shipping_report_action',
                'name': (u'employee info  item Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_acme_iot.stockpicking_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form'
                }