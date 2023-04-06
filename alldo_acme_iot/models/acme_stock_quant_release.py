# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmestockquantrelease(models.Model):
    _name = "alldo_acme_iot.quant_release"

    release_owner = fields.Many2one('res.users',string="批號歸檔人員")
    release_picking = fields.Many2one('stock.picking',string="調撥單號")
    release_lot = fields.Many2one('stock.quant',string="批號")
    release_prod = fields.Many2one('product.product',string="料號")
    release_num = fields.Float(digits=(13,2),string="數值")
    release_date = fields.Date(string="歸檔日期")
