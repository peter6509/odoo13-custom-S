# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class acmecastingfurnacestockmove(models.Model):
    _name = "alldo_acme_iot.furnace_stock_move"
    _description = "熔爐投料/耗料 明細檔"
    _order = "move_datetime desc"


    product_no = fields.Many2one('product.product',string="原始料件")
    mixprod_no = fields.Many2one('product.product',string="混合料件")
    lot_id = fields.Many2one('stock.production.lot', string="批次號")
    mo_no = fields.Many2one('mrp.production',string="生產製造單")
    move_type = fields.Selection([('1','投料'),('2','耗料')],string="屬性")
    move_datetime = fields.Datetime(string="投料/耗料時間")
    stock_owner = fields.Many2one('res.users', string="投料人員")
    equipment_no = fields.Many2one('maintenance.equipment',string="設備(爐號)")
    quantity = fields.Float(digits=(10, 3), string="數量")
    product_uom_id = fields.Many2one('uom.uom', string="單位")

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, '%s-批次號(%s)數量[%s]' % (record.product_no.default_code, record.lot_id.name, record.quantity)))
        return result



