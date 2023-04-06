# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotshippinglist(models.Model):
    _name = "alldo_ipla_iot.shipping_list"

    name = fields.Char(string="單據")
    report_no = fields.Char(string="出貨單號")
    location_id = fields.Many2one('stock.location',string="來源位置")
    partner_id = fields.Many2one('res.partner',string="客戶名稱")
    shipping_date = fields.Date(string="出貨日期")
    shipping_date1 = fields.Char(string="出貨日期")
    product_id = fields.Many2one('product.product',string="產品名稱")
    qty_done = fields.Float(string="出貨數量")
    origin = fields.Char(string="來源單據")
