# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebAcceptanceDownload(models.Model):
    _name = "neweb_acceptance.excel_download"
    _description = "貨品出貨狀態匯出EXCEL"
    _order = "create_date desc"

    xls_file = fields.Binary(string=u'EXCEL檔案', attachment=False)
    xls_file_name = fields.Char(string=u'檔案名稱')
    xls_file_memo = fields.Text(string=u"檔案說明")
