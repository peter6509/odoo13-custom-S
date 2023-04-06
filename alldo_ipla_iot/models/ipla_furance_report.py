# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api

class alldoiplafurancereport(models.Model):
    _name = "alldo_ipla_iot.furance_report"


    name = fields.Char(string="設備名稱")
    code = fields.Char(string="編碼")