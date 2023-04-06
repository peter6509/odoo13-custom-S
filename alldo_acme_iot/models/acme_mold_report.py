# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmemoldreport(models.Model):
    _name = "alldo_acme_iot.mold_report"
    _description = "模具條碼列印主檔"

    report_owner = fields.Many2one('res.users',string="製表人",default=lambda self:self.env.uid)
    mold_line = fields.One2many('alldo_acme_iot.mold_report_line','mold_id',string="條碼列印檔",copy=False)


class acmemoldreportline(models.Model):
    _name = "alldo_acme_iot.mold_report_line"
    _description = "模具條碼列印檔"

    mold_id = fields.Many2one('alldo_acme_iot.mold_report',ondelete='cascade')
    mold_code1 = fields.Char(string="模具條碼1")
    mold_code2 = fields.Char(string="模具條碼2")
    mold_code3 = fields.Char(string="模具條碼3")
    mold_code4 = fields.Char(string="模具條碼4")
    mold_code5 = fields.Char(string="模具條碼5")
    mold_code6 = fields.Char(string="模具條碼6")
    mold_code7 = fields.Char(string="模具條碼7")
    mold_code8 = fields.Char(string="模具條碼8")
    mold_code9 = fields.Char(string="模具條碼9")
    mold_code10 = fields.Char(string="模具條碼10")
    mold_code11 = fields.Char(string="模具條碼11")
    mold_code12 = fields.Char(string="模具條碼12")
    mold_code13 = fields.Char(string="模具條碼13")
    mold_code14 = fields.Char(string="模具條碼14")
    mold_code15 = fields.Char(string="模具條碼15")
    mold_code16 = fields.Char(string="模具條碼16")
    mold_code17 = fields.Char(string="模具條碼17")
    mold_code18 = fields.Char(string="模具條碼18")
    mold_code19 = fields.Char(string="模具條碼19")
    mold_code20 = fields.Char(string="模具條碼20")