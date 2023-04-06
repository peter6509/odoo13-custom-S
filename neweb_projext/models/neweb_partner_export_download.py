# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api



class partnerexportdownload(models.Model):
    _name = "neweb.export_excel_download"
    _order = "id desc"

    xls_file = fields.Binary(string='EXCEL樣版檔',attachment=False)
    xls_file_name = fields.Char(string='檔案名稱')
    xls_file_memo = fields.Text(string="檔案說明")

