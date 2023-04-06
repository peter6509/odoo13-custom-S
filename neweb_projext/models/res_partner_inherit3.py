# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class ResPartnerInherit3(models.Model):
    _inherit = "res.partner"

    customer = fields.Boolean(string="客戶")
    supplier = fields.Boolean(string="供應商")
    open_account_day = fields.Selection([('1', '30天'), ('2', '45天'), ('3', '60天'), ('4', '90天'), ('5', '120天')],
                                        string="付款天數")
    proj_pay1 = fields.Many2one('neweb.payment_term_rule',string="付款條件")
