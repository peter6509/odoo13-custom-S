# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewenUncompleteList(models.Model):
    _name = "neweb_acceptance.uncomplete_list"
    _description = "未結案發票開立清單"

    project_no = fields.Many2one('neweb.project', string="專案編號")
    contract_no = fields.Many2one('neweb_contract.contract', string="合約編號")
    cus_name = fields.Many2one('res.partner', string="專案客戶")
    main_cus_name = fields.Many2one('res.partner', string="終端客戶")
    project_amount_total = fields.Float(digits=(12, 0), string="合計金額(含税)")
    open_complete_total = fields.Float(digits=(12, 0), string="已開金額(含税)")
    proj_sale = fields.Many2one('hr.employee', string="專案業務")
