# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import datetime


class newebexportdownload(models.Model):
    _name = "neweb.export_excel_download"
    _order = "xls_file_name desc"

    xls_file = fields.Binary(string=u'EXCEL樣版檔',attachment=False)
    xls_file_name = fields.Char(string=u'檔案名稱')
    xls_file_memo = fields.Text(string=u"檔案說明",required=True)

    # @api.model
    # def create(self, vals):
    #     mydate = datetime.datetime.now()
    #     vals['xls_file_name']="Quotation_%s.xlsx" % mydate
    #     res = super(newebimportdownload,self).create(vals)
    #     return res