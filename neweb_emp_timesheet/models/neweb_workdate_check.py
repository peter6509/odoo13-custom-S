# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebworkdatecheck(models.Model):
    _name = "neweb_emp_timesheet.workdate_check"
    _description = "工程師工時報工檢核暫存檔"


    timesheet_date = fields.Date(string="日期")
    emp_id = fields.Many2one('hr.employee', string="人員")
    dept_id = fields.Many2one('hr.department', string="部門")
    has_gen = fields.Char(string="異動否？")
    timesheet_hours = fields.Float(string="")


