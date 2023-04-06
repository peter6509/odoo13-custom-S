# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ResUsersInherit(models.Model):
    _inherit = "res.users"

    escrow_no = fields.Many2one('cloudrent.escrow', string="歸屬代管業者")
    escrow_member = fields.Many2one('cloudrent.escrow_member',string="人員主檔")
