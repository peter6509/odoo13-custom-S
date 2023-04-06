# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    customer = fields.Boolean(string="客戶")
    supplier = fields.Boolean(string="供應商")
