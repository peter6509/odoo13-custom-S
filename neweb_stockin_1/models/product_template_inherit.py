# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class producttemplateinherit(models.Model):
    _inherit = "product.template"


    serial_no = fields.Text(string="產品序號")
    specification = fields.Text(string='規格說明')