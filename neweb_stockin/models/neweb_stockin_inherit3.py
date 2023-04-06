# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebstockininherit3(models.Model):
    _inherit = "neweb.stockship_list"

    stockout_sequence_id = fields.Integer(string="Sitem ID")
    prod_serial = fields.Text(string="序號")
