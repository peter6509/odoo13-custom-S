# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class GhiotCusStocklist(models.Model):
    _name = "alldo_gh_iot.cus_stocklist"
    _description = "客戶別庫存表"

    cus_no = fields.Many2one('res.partner',string="客戶")
    prod_no = fields.Many2one('product.product',string="料號")
    stock_loc = fields.Many2one('stock.location',string="倉別")
    stock_num = fields.Integer(string="數量")
    rack_loc = fields.Char(string="儲位")
    last_update = fields.Date(string="最後異動日")
    memo = fields.Char(string="備註")
