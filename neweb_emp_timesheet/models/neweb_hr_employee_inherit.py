# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError,Warning


class newebtimesheetemployeeinherit(models.Model):
    _inherit = "hr.employee"

    timesheet_expense = fields.Float(digits=(8,1),string=u"工時費用/Hr",default=0)
    timesheet_cost = fields.Float(digits=(8,1),string=u"工時成本/Hr",default=0)

