# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentContractVersion(models.Model):
    _name = "cloudrent.contract_version"
    _description = "合約書版次記錄"

    name = fields.Char(string="版本期數")
    contract_type = fields.Selection([('1','契約書'),('2','申請書')],string="類型")
    active = fields.Boolean(string="ACTIVE",default=True)
