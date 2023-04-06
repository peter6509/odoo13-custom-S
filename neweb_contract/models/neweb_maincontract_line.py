# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebMainContractLine(models.Model):
    _name = "neweb_contract.mainline"

    project_no = fields.Char(string="專案編號")
    contract_no = fields.Char(string="合約編號")
    customer_name = fields.Many2one('res.partner',string="客戶名稱")
    prod_set = fields.Many2one('neweb.prodset',string="產品組別")
    prod_brand = fields.Many2one('neweb.prodbrand',string="品牌")
    prod_modeltype = fields.Char(string="機型-機種/料號")
    prod_modeltype1 = fields.Many2one('neweb.sitem_modeltype1',string="機型名稱")
    machine_serial_no = fields.Char(string="序號")
    machine_loc = fields.Char(string="設備位址")
    prod_sla = fields.Many2one('neweb_base.sla', string="SLA Name", domain=[('disabled', '=', False)])
    memo = fields.Text(string="說明")
    contract_start_date = fields.Date(string="合約起始日")
    contract_end_date = fields.Date(string="合約截止日")
    sales = fields.Many2one('hr.employee',string="業務")
    ae1 = fields.Char(string="工程師")
    main_service_rule_new = fields.Many2one('neweb.main_service_rule', string="維護服務時段")
    vat = fields.Char(string="客戶統編")

