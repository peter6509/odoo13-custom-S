# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentAgentGrantFee(models.Model):
    _name = "cloudrent.agent_grant_fee_list"
    _description = "業者服務/補助費用申請書"

    @api.depends('notarial_fee','develop_fee','guarantee_fee','match_fee','escrow_fee')
    def _get_totamount(self):
        for rec in self:
            mynotarialfee = 0
            if rec.notarial_fee:
                mynotarialfee = rec.notarial_fee
            mydevelopfee = 0
            if rec.develop_fee:
                mydevelopfee = rec.develop_fee
            myguaranteefee = 0
            if rec.guarantee_fee:
                myguaranteefee = rec.guarantee_fee
            mymatchfee = 0
            if rec.match_fee:
                mymatchfee = rec.match_fee
            myescrowfee = 0
            if rec.escrow_fee:
                myescrowfee = rec.escrow_fee
            rec.tot_amount = mynotarialfee + mydevelopfee + myguaranteefee + mymatchfee + myescrowfee

    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者")
    grant_year = fields.Char(string="年")
    grant_month = fields.Char(string="月")
    grant_period = fields.Char(string="期")
    notarial_fee = fields.Integer(string="公證費")
    develop_fee = fields.Integer(string="開發費")
    guarantee_fee = fields.Integer(string="包管費")
    match_fee = fields.Integer(string="媒合費")
    escrow_fee = fields.Integer(string="代管費")
    tot_amount = fields.Integer(string="合計金額",compute=_get_totamount)
