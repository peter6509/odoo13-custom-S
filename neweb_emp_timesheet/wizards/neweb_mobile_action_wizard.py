# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebmobileactionwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.mobile_action_wizard"


    repair_no = fields.Many2one('neweb_repair.repair',string="報修單號")
