# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotoutsourcinginout(models.Model):
    _name = "alldo_acme_iot.inout_prod_list"
    _order = "inout_date"

    inout_date = fields.Date(string="日期")
    inout_date1 = fields.Char(string="進出日期")
    product_id = fields.Many2one('product.product',string="產品")
    out_num = fields.Float(digits=(7,1),string="出料量")
    out_owner = fields.Many2one('hr.employee',string="出料承辦人")
    in_good_num = fields.Float(digits=(7,1),string="回廠良品量")
    in_ng_num = fields.Float(digits=(7,1),string="回廠NG量")
    in_owner = fields.Many2one('hr.employee', string="回廠承辦人")
    balance_num = fields.Float(digits=(7, 1), string="餘額")