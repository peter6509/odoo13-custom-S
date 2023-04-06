# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotshippinglist(models.Model):
    _name = "alldo_gh_iot.shipping_list"

    name = fields.Char(string="單據")
    report_no = fields.Char(string="出貨單號")
    location_id = fields.Many2one('stock.location',string="來源位置")
    partner_id = fields.Many2one('res.partner',string="客戶名稱")
    shipping_date = fields.Date(string="出貨日期")
    shipping_date1 = fields.Char(string="出貨日期")
    product_id = fields.Many2one('product.product',string="產品名稱")
    qty_done = fields.Float(string="出貨數量")
    origin = fields.Char(string="來源單據")


class ghiotprocessingview(models.Model):
    _name = "alldo_gh_iot.processing_view"
    _description = "工單生產良品查詢主檔"
    _rec_name = "mo_no"

    mo_no = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼")
    product_no = fields.Many2one('product.product',string="產品")
    good_num = fields.Float(digits=(10,0),string="生產良品數")
    material_ng_num = fields.Float(digits=(10,0),string="累計材料不良數")
    processing_ng_num = fields.Float(digits=(10,0),string="累計加工不良數")
    loss_num = fields.Float(digits=(10,0),string="累計來料短少數")
    shipping_num = fields.Float(digits=(10,0),string="出貨累計數")
    processing_line = fields.One2many('alldo_gh_iot.processing_view_line','processing_id')


class ghiotprocessingviewline(models.Model):
    _name = "alldo_gh_iot.processing_view_line"
    _description = "工單生產良品查詢明細檔"

    processing_id = fields.Many2one('alldo_gh_iot.processing_view',ondelete='cascade')
    qc_date = fields.Date(string="承製日期")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    qc_good_num = fields.Float(digits=(13, 2), string="良品數量", default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="材料不良數量", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="加工不良數量", default=0)
    loss_num = fields.Float(digits=(13, 2), string="毛胚短少數量", default=0)
    iot_owner1 = fields.Many2one('hr.employee', string="擔當者")
