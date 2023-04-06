# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class PurchaseLast10List(models.Model):
    _name = "alldo_gh_iot.purchase_last10_list"
    _order = "date_order desc"
    _description = "最近10次採購單價清單"

    date_order = fields.Date(string="訂購日期")
    partner_id = fields.Many2one('res.partner',string="供應商")
    product_id = fields.Many2one('product.product',string="料號")
    product_qty = fields.Float(digits=(10,0),string="需求數量")
    qty_received = fields.Float(digits=(10,0),string="收貨數量")
    price_unit = fields.Float(digits=(13,2),string="單價")
    prod_material = fields.Char(string="材質")
    prod_spec = fields.Char(string="規格")
    last_date = fields.Date(string="最後進貨日")
