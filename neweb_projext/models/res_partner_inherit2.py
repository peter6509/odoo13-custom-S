# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class respartnerinherit2(models.Model):
    _inherit = "res.partner"

    partner_type = fields.Selection([('1', '客戶'), ('2', '供應商'), ('3', '兩者皆是')], string="伙伴型態", default='1')

    @api.model
    def create(self, vals):
        if 'partner_type' in vals and vals['partner_type'] == '1':
            vals['customer_rank'] = 1
            vals['supplier_rank'] = 0
        if 'partner_type' in vals and vals['partner_type'] == '2':
            vals['customer_rank'] = 0
            vals['supplier_rank'] = 1
        if 'partner_type' in vals and vals['partner_type'] == '3':
            vals['customer_rank'] = 1
            vals['supplier_rank'] = 1
        res = super(respartnerinherit2, self).create(vals)
        return res

    def write(self, vals):
        if 'partner_type' in vals and vals['partner_type'] == '1':
            vals['customer_rank'] = 1
            vals['supplier_rank'] = 0
        if 'partner_type' in vals and vals['partner_type'] == '2':
            vals['customer_rank'] = 0
            vals['supplier_rank'] = 1
        if 'partner_type' in vals and vals['partner_type'] == '3':
            vals['customer_rank'] = 1
            vals['supplier_rank'] = 1
        res = super(respartnerinherit2, self).write(vals)
        return res
