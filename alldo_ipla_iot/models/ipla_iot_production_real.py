# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotproductionreal(models.Model):
    _name = "alldo_ipla_iot.production_real"

    prod_id = fields.Many2one('product.template',string="產品")
    eng_type = fields.Char(string="工程別名稱")
    prod_num = fields.Integer(string="數量")
    prod_time = fields.Float(digits=(10,0), string="工時(秒)")
