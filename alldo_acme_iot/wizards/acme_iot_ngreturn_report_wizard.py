# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotngreturnreportwizard(models.TransientModel):
    _name = "alldo_acme_iot.ngreturn_report_wizard"
    _description = "退料單印表精靈"

    partner_id = fields.Many2one('res.partner',string="客戶")
    report_type = fields.Selection([('1','新單'),('2','舊單')],string="列印模式",default='1')
    report_date = fields.Date(string="製表日期",default=fields.Date.today())
    report_no = fields.Char(string="退料單號")

    def run_ngreturn_report(self):
        if self.report_type=='1' and not self.partner_id:
            raise UserError("新單列印要輸入客戶")
        if self.report_type=='2' and not self.report_no:
            raise UserError("舊單列印必需輸入退料單號")
        self.env.cr.execute("""delete from alldo_acme_iot_ngreturn_report""")
        self.env.cr.execute("""commit""")
        if self.report_type=='1':     # 新單
            self.env.cr.execute("""select ckngreturn(%d)""" % self.partner_id.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
                myrec = self.env['alldo_acme_iot.ngreturn_report']
                if not self.report_date:
                    myrec.create({'partner_id': self.partner_id.id})
                else:
                    myrec.create({'partner_id': self.partner_id.id,'report_date': self.report_date})
                self.env.cr.execute("""select gennewngreturn(%d)""" % self.partner_id.id)
                self.env.cr.execute("""commit""")
            else:
                raise UserError("目前沒有新單可供列印！")
        else:                         # 舊單
            self.env.cr.execute("""select genoldngreturn('%s')""" % (self.report_no))
            self.env.cr.execute("""commit""")

        myrec = self.env['alldo_acme_iot.ngreturn_report'].search([])
        for rec in myrec:
            myid = rec.id

        myviewid = self.env.ref('alldo_acme_iot.ngreturn_report_action')
        return {'view_name': 'ngreturn_report_action',
                'name': (u'NG return Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_acme_iot.ngreturn_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form',
                }