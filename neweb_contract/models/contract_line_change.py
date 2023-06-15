# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError, ValidationError

class ContractLineChange(models.Model):
    _name = "neweb_contract.contract_line_change"
    _description = "Contract Line Change"
    _order = "change_date desc"

    contract_id = fields.Integer(string="Contract ID")
    contract_line_id = fields.Integer(string="Contract Line ID")
    change_date = fields.Date(string="Change Date")
