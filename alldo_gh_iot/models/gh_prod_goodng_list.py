# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghprodgoodnglist(models.Model):
    _name = "alldo_gh_iot.prod_goodng_list"
    _order = "mo_no"

    product_id = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    mo_no = fields.Many2one('alldo_gh_iot.workorder',string="工單")
    blank_num = fields.Float(digits=(8,0),string="毛胚數量")
    prod_num = fields.Float(digits=(8,0),string="成品入庫數量")
    m_ng = fields.Float(digits=(8,0),string="料不良數量")
    p_ng = fields.Float(digits=(8, 0), string="加工不良數量")
    good_ratio = fields.Float(digits=(5,1),string="生產良率")
    ng_ratio = fields.Float(digits=(5,1),string="生產不良率(%)")
    mng_ratio = fields.Float(digits=(5,1),string="材料不良率(%)")
    png_ratio = fields.Float(digits=(5,1),string="加工不良率(%)")

