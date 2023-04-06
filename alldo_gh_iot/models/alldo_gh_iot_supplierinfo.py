# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class AlldoGHIOTsupplierinfo(models.Model):
    _name = "alldo_gh_iot.supplierinfo"
    _description = "供應商供料明細查詢"
    _order = "product_id"

    supplier_id = fields.Many2one('res.partner',string="廠商")
    product_id = fields.Many2one('product.product',string="料號")
    min_qty = fields.Float(digits=(10,0),string="最小量")
    price = fields.Float(digits=(10,0),string="單價")


