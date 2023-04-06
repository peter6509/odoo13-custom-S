# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebpitemlist1(models.Model):
    _inherit = "neweb.pitem_list"


    pitem_spec = fields.Text(string="規格說明")
