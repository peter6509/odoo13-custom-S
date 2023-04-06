# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotprodstock(models.Model):
    _name = "alldo_ipla_iot.prod_stock_list"
    _order = "product_no,stock_location"

    product_no = fields.Many2one('product.product',string="產品")
    cus_name = fields.Many2one('res.partner',string="所屬客戶")
    prod_num = fields.Integer(string="成品庫存數")
    stock_location = fields.Many2one('stock.location',string="庫存位置")
    stock_desc = fields.Char(string="庫存位置")
    blank_num = fields.Integer(string="毛胚庫存數")
