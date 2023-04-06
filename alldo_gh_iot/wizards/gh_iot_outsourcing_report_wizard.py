# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotoutsourcingreportwizard(models.TransientModel):
    _name = "alldo_gh_iot.outsourcing_report_wizard"

    partner_id = fields.Many2one('res.partner',string="主要委外廠商")
    partner_ids = fields.Many2many('res.partner',string="其他委外廠商")
    report_type = fields.Selection([('1','新單'),('2','舊單')],string="列印模式",default='2')
    report_date = fields.Date(string="製表日期",default=fields.Date.today())
    report_no = fields.Char(string="委外加工單號")

    def run_outsourcing_report(self):
        if self.report_type=='1' and not self.partner_id:
            raise UserError("新單列印要輸入委外加工廠商")
        if self.report_type=='2' and not self.report_no:
            raise UserError("舊單列印必需輸入委外加工單號")
        self.env.cr.execute("""delete from alldo_gh_iot_outsourcing_report""")
        self.env.cr.execute("""commit""")
        if self.report_type=='1':     # 新單
            self.env.cr.execute("""select ckoutsourcing(%d)""" % self.partner_id.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
                myrec = self.env['alldo_gh_iot.outsourcing_report']
                if not self.report_date:
                    myrec.create({'partner_id': self.partner_id.id})
                else:
                    myrec.create({'partner_id': self.partner_id.id,'report_date': self.report_date})
                self.env.cr.commit()
                self.env.cr.execute("""select gennewoutsourcing(%d,%d)""" % (self.partner_id.id,self.id))
                self.env.cr.execute("""commit""")

            else:
                raise UserError("目前沒有新單可供列印！")
        else:    # 舊單

            self.env.cr.execute("""select genoldoutsourcing('%s',%d)""" % (self.report_no,self.id))
            self.env.cr.execute("""commit""")

        myrec = self.env['alldo_gh_iot.outsourcing_report'].search([])
        for rec in myrec:
            myid = rec.id

        myviewid = self.env.ref('alldo_gh_iot.outsourcing_report_action')
        return {'view_name': 'outsourcing_report_action',
                'name': (u'Outsourcing Data'),
                'views': [[False, 'form']],
                'res_model': 'alldo_gh_iot.outsourcing_report',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'res_id': myid,
                'target': 'current',
                'view_id': myviewid.id,
                'view_mode': 'form',
                'view_type': 'form',
                }