# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentEscaletotLine(models.Model):
    _name = "cloudrent.escaletot_line"
    _order = "house_id,emeter_id"

    house_id = fields.Many2one('cloudrent.household_house',string="案名")
    house_no = fields.Char(string="房號")
    member_id = fields.Many2one('cloudrent.household_member', string="住戶")
    emeter_id = fields.Many2one('cloudrent.household_electric_meter',string="電錶")
    start_date = fields.Date(string="啟始日")
    end_date = fields.Date(string="截止日")
    start_scale = fields.Float(digits=(10,2),string="啟始度數")
    end_scale = fields.Float(digits=(10, 2), string="截止度數")
    duration_scale = fields.Float(digits=(10, 2), string="區間用電度數")