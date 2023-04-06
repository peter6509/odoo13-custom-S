# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentAgentApplyforList(models.Model):
    _name = "cloudrent.agent_applyfor_report"
    _description = "業者服務補助費用申請書"

    @api.depends('notarial_fee','develop_fee','guarantee_fee','match_fee','escrow_fee')
    def _get_amounttot(self):
        for rec in self:
            rec.applyfor_amount = rec.notarial_fee + rec.develop_fee + rec.guarantee_fee + rec.match_fee + rec.escrow_fee

    tw_y = fields.Char(string="title民國年")
    tw_m = fields.Char(string="title民國月")
    tw_period = fields.Char(string="title期")
    escrow_no = fields.Many2one('cloudrent.escrow',string="業者")
    applyfor_amount = fields.Float(digits=(10,0),string="申請總金額",compute=_get_amounttot)
    notarial_fee = fields.Float(digits=(10,0),string="公證費")
    develop_fee = fields.Float(digits=(10,0),string="開發費")
    guarantee_fee = fields.Float(digits=(10,0),string="包管費")
    match_fee = fields.Float(digits=(10,0),string="媒合費")
    escrow_fee = fields.Float(digits=(10,0),string="代管費")
    report_y = fields.Char(string="製表年")
    report_m = fields.Char(string="製表月")
    report_d = fields.Char(string="製表日")