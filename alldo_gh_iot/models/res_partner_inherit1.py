# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class respartnerinherit3(models.Model):
    _inherit = "res.partner"

    semi_loc = fields.Many2one('stock.location', string="半成品倉")
    prod_loc = fields.Many2one('stock.location', string="成品倉")
    blank_loc = fields.Many2one('stock.location', string="毛胚倉")
    sales1 = fields.Many2one('res.users',string="業務1")
    sales2 = fields.Many2one('res.users',string="業務2")
    pdf_preview = fields.Binary(string="PDF文件",attachment=True)

    

