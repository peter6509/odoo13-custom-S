# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class acmedayscale(models.Model):
    _name = "alldo_acme_iot.day_scale"
    _order = "item_seq,product_gpid"

    product_no = fields.Many2one('product.product', string="料號")
    scale_weight = fields.Float(digits=(10, 3), string="重量")
    scale_total = fields.Float(digits=(10, 3), string="群組總重")
    product_gpid = fields.Integer(string="群組編號")
    item_seq = fields.Integer(string="順序")
    scale_ratio = fields.Float(digits=(6, 2), string="比例%", group_operator="avg")
    uom_id = fields.Many2one('uom.uom', string="單位")
    scale_date = fields.Date(string="投料日期")
    scale_complete = fields.Boolean(string="運算完成",default=False)
    equipment_no = fields.Many2one('maintenance.equipment', string="設備(爐號)")

    def run_day_noncomplete(self):
        self.env.cr.execute("""select genscalenoncomplete1()""")
        self.env.cr.execute("""commit""")
