# -*- coding: utf-8 -*-
# Author: Mikuroda

from odoo import api, fields, models


class EraHouseholdMemberHistory(models.Model):
    _name = 'era.household_member.history'
    _description = 'ERA住戶通知繳費歷史紀錄'
    _order = "notify_datetime desc"

    household_member_id = fields.Many2one('era.household_member', string='住戶')
    bank_last_5_digit = fields.Char('銀行後五碼')
    amount = fields.Integer('金額')
    notify_datetime = fields.Datetime('通知時間')
