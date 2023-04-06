# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class newebpurchaseinherit2(models.Model):
    _inherit = "purchase.order"


    @api.onchange('partner_id')
    def onchangepartner(self):
        myrec = self.env['res.partner'].search([('id','=',self.partner_id.id)])
        mypayterm = myrec.payment_days
        self.pay_term = mypayterm