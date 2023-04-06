# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotstockmovelist(models.Model):
    _name = "alldo_gh_iot.stock_move_list"
    _description = "產品出貨複合式查詢表"
    _order = "product_id"



    date = fields.Date(string="出貨日期")
    product_id = fields.Many2one('product.product',string="產品料號")
    product_qty = fields.Float(digits=(10,0),string="數量")
    product_uom = fields.Many2one('uom.uom',string="單位")
    location_id = fields.Many2one('stock.location',string="From")
    location_dest_id = fields.Many2one('stock.location',string="To")
    partner_id = fields.Many2one('res.partner',string="客戶")
    origin = fields.Char(string="來源")
    po_no = fields.Char(string="客戶訂單編號")
    report_no = fields.Char(string="出貨單號")
    po_location = fields.Char(string="庫別")
    custom_system = fields.Boolean(string="平台")
    mo_group_id = fields.Integer(string="mogroupid")
    mo_no = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼")