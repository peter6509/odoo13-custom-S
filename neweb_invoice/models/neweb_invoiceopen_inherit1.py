# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebInvoiceOpenInherit1(models.Model):
    _inherit = "neweb_invoice.invoiceopen"

    salesp1 = fields.Integer(string="sale1")
    salesp2 = fields.Integer(string="sale2")
    salesp3 = fields.Integer(string="sale3")
    salesp4 = fields.Integer(string="sale4")
    salesp5 = fields.Integer(string="sale5")
