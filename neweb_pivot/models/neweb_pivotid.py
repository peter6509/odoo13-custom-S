# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class pivotid(models.Model):
    _name = "neweb_pivot.pivotid"

    num = fields.Integer(string="NUM",default=0)