# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotngreturnlist(models.Model):
    _name = "alldo_ipla_iot.ngreturn_list"

    name = fields.Char(string="單據")
    report_no = fields.Char(string="NG單號")
    # location_id = fields.Many2one('stock.location',string="位置")
    partner_id = fields.Many2one('res.partner',string="廠商名稱")
    ngreturn_date = fields.Date(string="NG退料日期")
    ngreturn_date1 = fields.Char(string="NG退料日期")
    product_id = fields.Many2one('product.product',string="產品名稱")
    return_good_num = fields.Float(digits=(13, 2), string="良品數量", default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="材料不良數量", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="加工不良數量", default=0)
    loss_num = fields.Float(digits=(13, 2), string="毛胚短少數量", default=0)
    origin = fields.Char(string="來源單據")
    ngreturn_type = fields.Selection([('1','生產NG'),('2','託工NG')],string="類別")
