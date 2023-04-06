# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghpacjagemowizard(models.TransientModel):
    _name = "alldo_gh_iot.package_mo_wizard"
    _description = "雜項工作建立精靈"

    package_owner = fields.Many2one('res.users',string="作業人員",default=lambda self:self.env.uid)
    package_event = fields.Char(string="雜項工作說明",default=' ')
    package_prod = fields.Many2one('product.product',string="工作產品",required=True)
    package_start = fields.Datetime(string="工作開始時間",required=True)
    package_end = fields.Datetime(string="工作結束時間",required=True)
    package_num = fields.Float(digits=(10,0),string="數量",default=0)


    @api.onchange('package_owner')
    def onchangeowner(self):
        self.env.cr.execute("""select getpackageprod()""")
        myprodid = self.env.cr.fetchone()[0]
        self.package_prod = myprodid

    def run_package_mo(self):
        if self.package_num <= 0:
            raise UserError("未輸入數量")
        if self.package_end < self.package_start:
            raise UserError("起訖時間有問題")
        myworkorderrec = self.env['alldo_gh_iot.workorder'].search([])
        myid = myworkorderrec.create({'product_no': self.package_prod.id,
                                      'blank_no': self.package_prod.id,
                                      'eng_type': self.package_event,
                                      'eng_order': '4',
                                      'eng_seq': 1,
                                      'state': '4',
                                      'order_num': self.package_num,
                                      'blank_num': self.package_num,
                                      'workorder_memo': self.package_event
                                      })

        self.env.cr.execute("""select genpackagemodata(%d,%d,'%s','%s',%s,%s)""" % (self.package_owner.id,myid.id,self.package_start,self.package_end,self.package_num,True))
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '雜項工作工單資訊輸入完成！'
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