# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojexport(models.Model):
    _name = "neweb.projwarrantyinfo_export"

    proj_no = fields.Char(string="專案編號")
    cus_name = fields.Char(string="客戶名稱")
    prod_modeltype = fields.Char(string="機種-機型")
    prod_serial = fields.Char(string="序號")
    shipping_date = fields.Date(string="實際出貨日")
    invoice_date = fields.Date(string="發票日")
    invoice_no = fields.Char(string="發票號碼")
    neweb_start_date = fields.Date(string="藍新保固起日")
    neweb_end_date = fields.Date(string="藍新保固迄日")
    sale_id = fields.Many2one('hr.employee',string="業務")
    supplier_id = fields.Many2one('res.partner',string="廠商")