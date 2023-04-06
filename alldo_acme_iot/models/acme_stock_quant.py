# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmestockquant(models.Model):
    _inherit = "stock.quant"

    temp_qty = fields.Float(digits=(13,2),string="template qty")
    temp_change = fields.Boolean(string="temp change",default=False)

    def run_return_quant(self):
        self.env.cr.execute("""select returnquant()""")
        self.env.cr.execute("""commit""")
