# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoiplaiotempattendancelist(models.Model):
    _name = "alldo_ipla_iot.emp_attendance_list"

    attend_date = fields.Date(string="刷卡日期")
    attend_date1 = fields.Char(string="C刷卡日期")
    emp_no = fields.Many2one('hr.employee',string="人員姓名")
    att_start_date = fields.Datetime(string="上班時間")
    attendance_start = fields.Char(string="C上班時間")
    att_end_date = fields.Datetime(string="下班時間")
    attendance_end = fields.Char(string="C下班時間")
    att_duration = fields.Float(digits=(5,2),string="時數(hr)")