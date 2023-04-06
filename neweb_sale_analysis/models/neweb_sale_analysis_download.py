# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class saleanalysisdownload(models.Model):
    _name = "neweb_sale_analysis.saleanalysis_excel_download"
    _order = "create_date desc"
    _description = "成本分析-業務業績Excel Download"

    xls_file = fields.Binary(string='下載檔案',attachment=False)
    xls_file_name = fields.Char(string='檔案說明')
