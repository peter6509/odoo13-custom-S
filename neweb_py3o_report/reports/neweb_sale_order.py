# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api


class py30newebsaleorder(models.Model):
    _inherit = "sale.order"

    @api.depends('open_account_day')
    def _get_open_acc_day(self):
        mycaccday='30天'
        for rec in self:
            if rec.open_account_day == '1':
                mycaccday = '30天'
            elif rec._get_open_acc_day == '2':
                mycaccday = '45天'
            elif rec._get_open_acc_day == '3':
                mycaccday = '60天'
            elif rec._get_open_acc_day == '4':
                mycaccday = '90天'
            elif rec._get_open_acc_day == '5':
                mycaccday = '120天'
            rec.copenaccountday = mycaccday
            return mycaccday

    @api.depends('delivery_term')
    def _get_delivery_term(self):
        mycdeliveryterm='30天'
        for rec in self:
            if rec.delivery_term == '1':
                mycdeliveryterm='30天'
            elif rec.delivery_term == '2':
                mycdeliveryterm='45天'
            elif rec.delivery_term == '3':
                mycdeliveryterm='60天'
            rec.cdeliveryterm = mycdeliveryterm
            return mycdeliveryterm


    copenaccountday = fields.Char(string="月結條件py3o",compute=_get_open_acc_day)
    cdeliveryterm = fields.Char(string="交貨期限py3o",compute=_get_delivery_term)