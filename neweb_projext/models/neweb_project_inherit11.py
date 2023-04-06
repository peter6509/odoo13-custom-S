# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojectinherit11(models.Model):
    _inherit = "neweb.ass_service_type"

    service_manager = fields.Many2one('hr.employee',string="派工主管")