# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotmaterialline(models.Model):
    _name = "alldo_acme_iot.materialline"

    mrp_prod_id = fields.Many2one('mrp.production', string="製造命令", required=True, ondelete='cascade')
    product_no = fields.Many2one('product.product', string="產品料號")
    product_qty = fields.Float(digits=(12,3),string="生產需求量")
    onhand_qty = fields.Float(digits=(12,3),string="目前在手量")
    need_qty = fields.Float(digits=(12,3),string="不足數量")
    prod_uom_id = fields.Many2one('uom.uom', string="單位")