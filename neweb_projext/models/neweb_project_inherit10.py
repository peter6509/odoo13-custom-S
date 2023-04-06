# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojectinherit10(models.Model):
    _inherit = "res.partner"
    _order = "create_date desc"

    birthday_month = fields.Many2one('neweb.partner_birthday_month',string="生日(月份)")
    birthday_day = fields.Many2one('neweb.partner_birthday_day',string="生日(日期)")


class newebpartnerbirthdaymonth(models.Model):
    _name = "neweb.partner_birthday_month"
    _order = "month_code"

    name = fields.Char(string="月份")
    month_code = fields.Char(string="Code")


class newebpartnerbirthdayday(models.Model):
    _name = "neweb.partner_birthday_day"
    _order = "day_code"

    name = fields.Char(string="日期")
    day_code = fields.Char(string="Code")