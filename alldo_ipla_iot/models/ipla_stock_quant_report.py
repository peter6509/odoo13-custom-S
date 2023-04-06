# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class quantreport(models.Model):
    _name = "alldo_ipla_iot.quant_report"
    _description = "批次號主檔"

    report_owner = fields.Many2one('res.users',string="製表人",default=lambda self:self.env.uid)
    quant_line = fields.One2many('alldo_ipla_iot.quant_report_line','quant_id',string="條碼列印檔",copy=False)


class quantreportline(models.Model):
    _name = "alldo_ipla_iot.quant_report_line"
    _description = "批次號條碼列印檔"

    quant_id = fields.Many2one('alldo_ipla_iot.quant_report',ondelete='cascade')
    lot_code1 = fields.Char(string="批號條碼1")
    lot_code2 = fields.Char(string="批號條碼2")
    lot_code3 = fields.Char(string="批號條碼3")
    lot_code4 = fields.Char(string="批號條碼4")
    lot_code5 = fields.Char(string="批號條碼5")
    lot_code6 = fields.Char(string="批號條碼6")
    lot_code7 = fields.Char(string="批號條碼7")
    lot_code8 = fields.Char(string="批號條碼8")
    lot_code9 = fields.Char(string="批號條碼9")
    lot_code10 = fields.Char(string="批號條碼10")
    lot_code11 = fields.Char(string="批號條碼11")
    lot_code12 = fields.Char(string="批號條碼12")
    lot_code13 = fields.Char(string="批號條碼13")
    lot_code14 = fields.Char(string="批號條碼14")
    lot_code15 = fields.Char(string="批號條碼15")
    lot_code16 = fields.Char(string="批號條碼16")
    lot_code17 = fields.Char(string="批號條碼17")
    lot_code18 = fields.Char(string="批號條碼18")
    lot_code19 = fields.Char(string="批號條碼19")
    lot_code20 = fields.Char(string="批號條碼20")