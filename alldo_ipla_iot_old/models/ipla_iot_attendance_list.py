# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoiplaiotempattendancelist(models.Model):
    _name = "alldo_ipla_iot.emp_attendance_list"
    _order = "attend_date"

    attend_date = fields.Date(string="刷卡日期")
    attend_date1 = fields.Char(string="刷卡日期")
    emp_no = fields.Many2one('hr.employee',string="人員姓名")
    att_start_date = fields.Datetime(string="正常上班時間")
    attendance_start = fields.Char(string="正常上班時間")
    att_end_date = fields.Datetime(string="正常下班時間")
    attendance_end = fields.Char(string="正常下班時間")
    att_duration = fields.Float(digits=(5, 2), string="正常時數(hr)",default=0.00)
    otatt_start_date = fields.Datetime(string="加班上班時間")
    otattendance_start = fields.Char(string="加班上班時間")
    otatt_end_date = fields.Datetime(string="加班下班時間")
    otattendance_end = fields.Char(string="加班下班時間")
    otatt_duration = fields.Float(digits=(5,2),string="加班時數(hr)",default=0.00)
    att_start_date1 = fields.Datetime(string="正常上班時間1")
    attendance_start1 = fields.Char(string="正常上班時間1")
    att_end_date1 = fields.Datetime(string="正常下班時間1")
    attendance_end1 = fields.Char(string="正常下班時間1")
    att1_duration = fields.Float(digits=(5, 2), string="正常時數1(hr)", default=0.00)
    att_start_date2 = fields.Datetime(string="正常上班時間2")
    attendance_start2 = fields.Char(string="正常上班時間2")
    att_end_date2 = fields.Datetime(string="正常下班時間2")
    attendance_end2 = fields.Char(string="正常下班時間2")
    att2_duration = fields.Float(digits=(5, 2), string="正常時數2(hr)", default=0.00)
    otatt_start_date1 = fields.Datetime(string="加班上班時間1")
    otattendance_start1 = fields.Char(string="加班上班時間1")
    otatt_end_date1 = fields.Datetime(string="加班下班時間1")
    otattendance_end1 = fields.Char(string="加班下班時間1")
    otatt1_duration = fields.Float(digits=(5, 2), string="加班時數(hr)", default=0.00)