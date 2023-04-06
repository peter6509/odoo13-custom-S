# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class workordermanperformance(models.Model):
    _name = "alldo_acme_iot.man_performance"

    order_id = fields.Many2one('alldo_acme_iot.workorder',string="工單號碼")
    prod_date = fields.Date(string="入庫日期")
    prod_duration = fields.Float(digits=(7, 1), string="實際總工時")
    std_duration = fields.Float(digits=(7, 1), string="標準總工時")
    prod_performance = fields.Float(digits=(4,2),string="生產效率%")
    prod_owner = fields.Many2one('hr.employee', string="擔當者")
    prod_num = fields.Float(digits=(13, 2), string="總數量")
