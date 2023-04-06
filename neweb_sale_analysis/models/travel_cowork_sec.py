# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class TravelCoWorkSec(models.Model):
    _inherit = "neweb_sale_analysis.travel_report"

    co_man1 = fields.Many2one('hr.employee',string="COMAN1")
    co_man2 = fields.Many2one('hr.employee', string="COMAN2")
    co_man3 = fields.Many2one('hr.employee', string="COMAN3")
    co_man4 = fields.Many2one('hr.employee', string="COMAN4")
    co_man5 = fields.Many2one('hr.employee', string="COMAN5")