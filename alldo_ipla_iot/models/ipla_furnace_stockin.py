# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplafurnacestockin(models.Model):
    _name = 'alldo_ipla_iot.furnace_stockin'
    _description = "原材料投料記錄"
    _order = "stockin_date desc"

    product_id = fields.Many2one('product.product',string="料號",required=True)
    equipment_no = fields.Many2one('maintenance.equipment',string="設備")
    lot_id = fields.Many2one('stock.production.lot',string="批次號")
    quantity = fields.Float(digits=(10,2),string="數量")
    product_uom_id = fields.Many2one('uom.uom',string="單位")
    stockin_owner = fields.Many2one('res.users',string="投料人員")
    stockin_date = fields.Date(string="投料日期")
