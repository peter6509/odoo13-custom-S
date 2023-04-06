# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebemppostype(models.Model):
    _name = "hr.employee_postype"

    emp_id = fields.Many2one('hr.employee')
    flow_man1 = fields.Many2one('hr.employee', string="一線主管")
    flow_man2 = fields.Many2one('hr.employee', string="二線主管")
    flow_man3 = fields.Many2one('hr.employee', string="副總")
    flow_man4 = fields.Many2one('hr.employee', string="總經理")
    flow_man5 = fields.Many2one('hr.employee', string="助理")

    def run_emp_postype(self):
        self.env.cr.execute("""select genemppostype()""")
        self.env.cr.execute("""commit""")
