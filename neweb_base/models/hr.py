# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = '員工主檔'

    residnet_ship = fields.Char(string='Resident Ship')
    educational_level = fields.Char(string='Educational Level')
    employee_num = fields.Char(string='Employee No.')


