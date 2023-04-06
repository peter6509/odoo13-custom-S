# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotbookingrelease(models.Model):
    _name ="alldo_gh_iot.prod_booking_release"

    po_id = fields.Many2one('alldo_gh_iot.po_wkorder', string="訂單", ondelete='cascade')
    booking_prod = fields.Many2one('product.product', string="預留產品")
    release_num = fields.Float(digits=(10, 0), string="解除數量")
    release_owner = fields.Many2one('res.users', string="解除人員")
    release_date = fields.Date(string="解除日期", default=fields.Date.today())
    release_desc = fields.Char(string="解除說明")
    release_p_picking = fields.Many2one('stock.picking', string="產品解除調撥單號")
    release_b_picking = fields.Many2one('stock.picking', string="毛胚解除調撥單號")
