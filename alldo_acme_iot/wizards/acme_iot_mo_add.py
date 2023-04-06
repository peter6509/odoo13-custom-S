# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class acmeiotmoadd(models.TransientModel):
    _name = "alldo_acme_iot.mo_add_wizard"
    _description = "製造生產單數量追加精靈"

    mo_no = fields.Many2one('mrp.production', string="製造生產單")
    product_no = fields.Many2one('product.product',string="生產產品",required=True)
    prod_origin_num = fields.Float(digits=(10,2),string="原製造單數量")
    prod_num = fields.Float(digits=(10,2),string="追加加數",default=0.00,required=True)
    addin_owner = fields.Many2one('res.users',string="入帳人員",default=lambda self:self.env.uid)

    @api.onchange('mo_no')
    def onclientchangepo(self):
        self.env.cr.execute("""select getmooriginnum(%d)""" % self.mo_no.id)
        self.prod_origin_num = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getmoprod(%d)""" % self.mo_no.id)
        myprodid = self.env.cr.fetchone()[0]
        self.product_no =myprodid
        return {'domain': {'product_no': [('id', '=', myprodid)]}}

    def run_mo_add(self):
        if self.prod_num > 0:
            self.env.cr.execute("""select runmoadd(%d,%f)""" % (self.mo_no.id,self.prod_num))
            self.env.cr.execute("""commit""")
        else:
            raise UserError("沒有輸入追加數量 ！")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '製造生產單數量追加輸入完成！'
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
