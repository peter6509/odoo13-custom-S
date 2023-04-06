# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotstockmovelist(models.Model):
    _name = "alldo_ipla_iot.stock_move_list"
    _description = "產品出貨複合式查詢表"


    date = fields.Date(string="出貨日期")
    product_id = fields.Many2one('product.product',string="產品料號")
    product_qty = fields.Float(digits=(10,0),string="數量")
    product_uom = fields.Many2one('uom.uom',string="單位")
    location_id = fields.Many2one('stock.location',string="From")
    location_dest_id = fields.Many2one('stock.location',string="To")
    partner_id = fields.Many2one('res.partner',string="客戶")
    origin = fields.Char(string="來源")