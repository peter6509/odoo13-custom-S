# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class erainvno(models.Model):
    _name = "era.inv_no_seq"

    inv_ym = fields.Char(string="年月")
    inv_prefixcode = fields.Char(string="專案前綴碼")
    inv_seq = fields.Integer(string="流水號")
