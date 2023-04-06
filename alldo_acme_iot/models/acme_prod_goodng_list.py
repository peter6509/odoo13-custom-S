# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeprodgoodnglist(models.Model):
    _name = "alldo_acme_iot.prod_goodng_list"

    product_id = fields.Many2one('product.product', string="產品")
    good_ratio = fields.Float(digits=(5,1),string="生產良率")
    ng_ratio = fields.Float(digits=(5,1),string="生產不良率")

