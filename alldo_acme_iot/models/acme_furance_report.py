# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api

class alldoacmefurancereport(models.Model):
    _name = "alldo_acme_iot.furance_report"


    name = fields.Char(string="熔爐名稱")
    code = fields.Char(string="編碼")