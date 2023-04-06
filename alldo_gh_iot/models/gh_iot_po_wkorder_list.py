# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotpowkorderlist(models.Model):
    _name = "alldo_gh_iot.powkorder_list"
    _description = "訂單狀態查詢"
    _order = "order_date"

    po_no = fields.Char(string="訂單號碼")
    cus_name = fields.Many2one('res.partner',string="客户")
    product_no = fields.Many2one('product.product',string="產品")
    order_date = fields.Date(string="訂單日期")
    shipping_date = fields.Date(string="出貨日期")
    response_shipping_date = fields.Date(string="回覆交期")
    custom_system = fields.Boolean(string="平台",default=False)
    open_wkorder = fields.Boolean(string="工單",default=False)
    booking_blank = fields.Boolean(string="訂貨",default=False)
    stockin_blank = fields.Boolean(string="進貨",default=False)
    po_id = fields.Many2one('purchase.order',string="採購單號")
    po_num = fields.Float(digits=(10, 0), string="訂單數量")
    unstockin_num = fields.Float(digits=(10, 0), string="已採購未到量")
    stock_pquant_line = fields.One2many('alldo_gh_iot.powkorder_line','line_id',string="產品庫存狀態")
    stock_bquant_line = fields.One2many('alldo_gh_iot.powkorder_line1','line_id',string="毛胚庫存狀態")


class ghiotwkorderlistline(models.Model):
    _name = "alldo_gh_iot.powkorder_line"

    line_id = fields.Many2one('alldo_gh_iot.powkorder_list',ondelete='cascade')
    product_no = fields.Many2one('product.product',string="料號")
    location_id = fields.Many2one('stock.location',string="位置")
    qty = fields.Float(digits=(10,0),string="數量")


class ghiotwkorderlistline1(models.Model):
    _name = "alldo_gh_iot.powkorder_line1"

    line_id = fields.Many2one('alldo_gh_iot.powkorder_list', ondelete='cascade')
    product_no = fields.Many2one('product.product', string="料號")
    location_id = fields.Many2one('stock.location', string="位置")
    qty = fields.Float(digits=(10, 0), string="數量")


