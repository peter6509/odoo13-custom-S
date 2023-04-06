# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class saleorderlineinherit(models.Model):
    _inherit = "sale.order.line"

    mold_id = fields.Many2one('alldo_acme_iot.acme_mold',string="模具")
    is_completed = fields.Boolean(string="結案否",default=False)

    @api.onchange('product_id')
    def onchangeprod(self):
        if self.product_id.default_code=='mold':
            mypartnerid = self.order_id.partner_id.id
            myrec = self.env['alldo_acme_iot.acme_mold'].search([('partner_id','=',mypartnerid)])
            ids=[]
            for rec in myrec:
                ids.append(rec.id)
            return {'domain': {'mold_id': [('id','in',ids)]}}
        else:
            ids=[]
            self.mold_id=False
            return {'domain': {'mold_id': [('id','in',ids)]}}

    @api.onchange('mold_id')
    def onchangemold(self):
        if self.mold_id :
            self.name = "[Mold]%s" % self.mold_id.name

    def run_completed(self):
        self.is_completed=True



