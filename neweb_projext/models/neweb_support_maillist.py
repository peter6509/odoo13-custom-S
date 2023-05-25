# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class neweb_support_maillist(models.Model):
    _name = "neweb.support_maillist"
    _description ="支援單特定通知人員名單"

    emp_no = fields.Many2one('hr.employee',string="員工編號")