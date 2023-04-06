# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebtolerancesetting(models.Model):
    _name = "neweb_emp_timesheet.tolerance_setting"
    _description = "正常日工時彈性容忍時間設定"


    tolerance_time = fields.Float(string="每日彈性容忍值(分鐘)",required=True)


    # @api.model
    # def create(self, vals):
    #     myres = self.env['neweb_emp_timesheet.tolerance_setting'].search_count([])
    #     if myres > 0 :
    #         raise UserError("只能設定一筆容忍值")
    #     res = super(newebtolerancesetting, self).create(vals)
    #     return res