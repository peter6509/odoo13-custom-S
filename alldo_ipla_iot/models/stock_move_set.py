# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class stockmoveset(models.Model):
    _name = "alldo_acme_iot.stock_move_set"

    material_loc = fields.Many2one('stock.location',string="原物料位置",required=True)
    good_loc = fields.Many2one('stock.location',string="成品位置",required=True)
    manufacture_loc = fields.Many2one('stock.location',string="生產耗料位置",required=True)

