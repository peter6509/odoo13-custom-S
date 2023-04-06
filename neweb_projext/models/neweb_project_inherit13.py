# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class NewebProjectIherit13(models.Model):
    _inherit = "neweb.projsaleitem"

    prod_origin_price = fields.Float(digits=(13,2), string="原業務單價",default=0)
