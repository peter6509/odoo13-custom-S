# -*- coding: utf-8 -*-
# Author: Mikuroda

from odoo import api, fields, models


class EraHouseholdMember(models.Model):
    _inherit = "era.household_member"

    @api.depends('ar_date')
    def _get_overdue(self):
        for rec in self:
            self.env.cr.execute("""selet genoverdue(%d)""" % rec.id)
            rec.is_overdue = self.env.cr.fetchone()[0]


    line_user_id = fields.Char(string='Line User ID')
    line_request_status = fields.Selection(
        selection=[('', '無'), ('notify', '繳費通知')]
    )
    line_rich_menu_id = fields.Char(string='Line Rich menu ID')
    line_binding = fields.Boolean(string='line已綁定', compute='_status_of_line_binding')

    history_ids = fields.One2many('era.household_member.history', 'household_member_id')
    previous_arrears = fields.Integer(string='上期欠款')
    period_addition = fields.Integer(string='本期增加')
    period_electric = fields.Integer(string='本期電費')
    period_house_rent = fields.Integer(string='本期房屋租金')
    period_house_manage = fields.Integer(string='本期房屋管理費')
    period_park_rent = fields.Integer(string='本期車位租金')
    period_park_manage = fields.Integer(string='本期車位管理費')
    period_moto_park_manage = fields.Integer(string='本期機車位管理費')
    period_water_fee = fields.Integer(string="本期水費")
    period_total = fields.Integer(string='本期應繳總金額')
    period_complete_total = fields.Integer(string="本期已核銷金額")

    period_start = fields.Char(string="起租日")
    period_end = fields.Char(string="退租日")
    now_ym = fields.Char(string="目前應結帳年月")
    period_subtot = fields.Integer(string="每月固定應繳租金/管理費")
    period_totrent = fields.Integer(string="合計應繳房租/管理費總金額")
    period_totrentpay = fields.Integer(string="合計已繳房租/管理費總金額")
    now_totrent_balance = fields.Integer(string="結算房租/管理費應繳餘額")
    period_totscale = fields.Integer(string="合計應繳總電費")
    period_totscalepay = fields.Integer(string="合計已繳總電費")
    now_totscalebalance = fields.Integer(string="結算電費應繳餘額")
    now_totbalance = fields.Integer(string="結算總應繳餘額")
    ar_date = fields.Date(string="應繳租金日期")
    is_overdue = fields.Boolean(string="已逾期",compute=_get_overdue)

    @api.depends('line_user_id')
    def _status_of_line_binding(self):
        for r in self:
            r.line_binding = True if r.line_user_id else False
        return True

    def unlink_line_user_id(self):
        for r in self:
            r.line_user_id = False
        return True
