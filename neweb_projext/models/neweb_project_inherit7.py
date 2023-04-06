# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectinherit71(models.Model):
    _inherit = "neweb.sitem_list"


    dept_id = fields.Many2one('hr.department',string="部門別")





class newebprojectinherit72(models.Model):
    _inherit = "neweb.projsaleitem"

    dept_id = fields.Many2one('hr.department',string="部門別")