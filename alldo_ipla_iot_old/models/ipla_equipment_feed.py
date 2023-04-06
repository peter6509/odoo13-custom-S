# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaequipmentfeed(models.Model):
    _name = "alldo_ipla_iot.equipment_feed"
    _description = "機台投料 明細檔"
    _order = "move_datetime desc"


    product_no = fields.Many2one('product.product',string="原始料件")
    mixprod_no = fields.Many2one('product.product',string="混合料件")
    lot_id = fields.Many2one('stock.production.lot', string="批次號")
    mo_no = fields.Many2one('mrp.production',string="生產製造單")
    move_datetime = fields.Datetime(string="投料時間")
    stock_owner = fields.Many2one('res.users', string="投料人員")
    equipment_no = fields.Many2one('maintenance.equipment',string="設備")
    quantity = fields.Float(digits=(10, 3), string="數量")
    product_uom_id = fields.Many2one('uom.uom', string="單位")

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, '%s-批次號(%s)數量[%s]' % (record.product_no.default_code, record.lot_id.name, record.quantity)))
        return result



