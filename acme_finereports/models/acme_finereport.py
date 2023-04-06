# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmefinereportpara(models.Model):
    _name = "alldo_acme_iot.finereport_para"
    _description = "FineReport 參數檔"

    finereport_key = fields.Char(string="KEY")
    finereport_cvalue = fields.Char(string="Cvalue")
    finereport_ivalue = fields.Integer(string="Ivalue")
