# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class acmesaleorderinherit1(models.Model):
    _inherit = "sale.order"

    so_pi = fields.Char(string="PI單號",required=True)
