# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmemixsearchscalemovelist(models.Model):
    _name = "alldo_acme_iot.mixsearch_scalemovelist"

    scale_type = fields.Selection([('1', '熔爐投料'), ('2', '回收料入庫')], string="類別", default='1')
    product_no = fields.Many2one('product.product', string="料號")
    need_lotno = fields.Boolean(string="是否需批次號", default=False)
    lot_no = fields.Many2one('stock.quant', string="批號")
    scale_weight = fields.Float(digits=(10, 3), string="重量")
    equipment_no = fields.Many2one('maintenance.equipment', string="設備(爐號)")
    uom_id = fields.Many2one('uom.uom', string="單位")
    scale_owner = fields.Many2one('res.users', string="作業人員", default=lambda self: self.env.uid)
    picking_no = fields.Many2one('stock.picking', string="調撥單號", readonly=True)
    is_posting = fields.Selection([('1', '未過帳'), ('2', '已過帳'), ('3', '記錄缺批次號')], string="資料狀態", default='1')
    scale_datetime = fields.Datetime(string="日期時間")
