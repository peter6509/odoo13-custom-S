# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class eraemetermixsearchline(models.Model):
    _name = "era_household.emeter_mixsearch_line"

    house_no = fields.Char(string="房號")
    start_date = fields.Date(string="啟始日期")
    end_date = fields.Date(string="截止日期")
    emeter_id = fields.Many2one('era.household_electric_meter', string="電錶")
    emeter_start_scale = fields.Float(digits=(13, 2), string="期初累計度數")
    emeter_end_scale = fields.Float(digits=(13, 2), string="期末累計度數")
    emeter_used_scale = fields.Float(digits=(10, 1), string="使用度數")
    emeter_price_unit = fields.Float(digits=(6, 2), string="單價(度)")
    emeter_amount = fields.Float(digits=(8, 0), string="電費小計")