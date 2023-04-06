# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class contractexceldownload(models.Model):
    _name = "neweb_contract.custom_excel_download"
    _order = "create_date desc"
    _description = "合約客戶 Excel Download"

    xls_file = fields.Binary(string='下載檔案',attachment=False)
    xls_file_name = fields.Char(string='檔案說明')

class customexceldata(models.Model):
    _name = "neweb_contract.custom_excel_data"

    contact1 = fields.Char(string="合約編號")
    contact2 = fields.Date(string="維護到期日")
    contact3 = fields.Many2one('res.partner',string="客戶名稱")
    contact4 = fields.Many2one('hr.employee',string="業務")
    contact5 = fields.Char(string="客戶聯絡人")
    contact6 = fields.Char(string="客戶聯絡人電郵")
    contact7 = fields.Char(string="客戶聯絡人電話")
    contact8 = fields.Many2one('res.partner',string="終端客戶名稱")
    contact9 = fields.Char(string="終端客戶聯絡人")
    contact10 = fields.Char(string="終端客戶電郵")
    contact11 = fields.Char(string="終端客戶電話")
    contact12 = fields.Char(string="客戶聯絡人滿意度勾選")
    contact13 = fields.Char(string="終端客戶聯絡人滿意度勾選")
