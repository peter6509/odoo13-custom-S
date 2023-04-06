# -*- coding: utf-8 -*-
# Author : Peter Wu



from odoo import models,fields,api
from odoo.exceptions import UserError


class timesheetnocomplete(models.TransientModel):
    _name = "neweb_emp_timesheet.timesheet_nocomplete"
    _order = "id"


    timesheet_date = fields.Date(string="日期")
    emp_id = fields.Many2one('hr.employee', string="人員")
    dept_id = fields.Many2one('hr.department', string="部門")
    timesheet_hours = fields.Float(string="工時時數(分)")
    no_complete = fields.Boolean(string="未達基本時數")
    illegal_num = fields.Integer(string="不符標準筆數")
