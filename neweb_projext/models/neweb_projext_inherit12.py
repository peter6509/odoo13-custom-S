# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api

class newebprojextinherit12(models.Model):
    _inherit = "neweb.prodbrand"

    active = fields.Boolean('生效',default=True)
