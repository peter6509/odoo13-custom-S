# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmequantreleasewizard(models.TransientModel):
    _name = "alldo_acme_iot.quant_release_wizard"

    release_owner = fields.Many2one('res.users',string="批號歸檔人員",default=lambda self:self.env.uid)

    release_lot = fields.Many2one('stock.quant',string="批號")
    release_num = fields.Float(digits=(13, 2), string="餘額")
    release_date = fields.Date(string="執行日期",default=fields.Date.today())

    @api.onchange('release_owner')
    def onchangedate(self):
        self.env.cr.execute("""select getlotdata()""")
        myres = self.env.cr.fetchall()
        ids=[]
        for item in myres:
            ids.append(item[0])
        return {'domain': {'release_lot': [('id', 'in', ids)]}}


    @api.onchange('release_lot')
    def onchangereleaselot(self):
        self.env.cr.execute("""select getquantlotnum(%d)""" % self.release_lot.id)
        self.release_num = self.env.cr.fetchone()[0]

    def run_quant_release(self):
        if self.release_num != 0 :
            myrec=self.env['alldo_acme_iot.quant_release']
            myrec.create({'release_owner':self.release_owner.id,'release_lot':self.release_lot.id,'release_num':self.release_num,'release_date':self.release_date,'release_prod':self.release_lot.product_id.id})
            self.env.cr.execute("""update stock_quant set quantity=0 where id=%d""" % self.release_lot.id)
            self.env.cr.execute("""commit""")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = '批號歸檔輸入完成！'
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


