# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotmintimesearch(models.Model):
    _name = "alldo_gh_iot.mintime_list"
    _description = "產品各工序生產最低時間"
    _order = "eng_order"

    product_id = fields.Many2one('product.product',string="產品")
    mo_no = fields.Many2one('alldo_gh_iot.workorder',string="工單")
    equip_id = fields.Many2one('maintenance.equipment',string="機台")
    eng_order = fields.Integer(string="工序INT")
    eng_type = fields.Char(string="工序")
    duration = fields.Float(digits=(10,1),string="工時秒數")
    display_duration = fields.Char(string="工時")
    mold_cavity = fields.Integer(string="模穴數", default=1)

