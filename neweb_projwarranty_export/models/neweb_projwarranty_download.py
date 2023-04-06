# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojwarrantyexportdownload(models.Model):
    _name = "neweb.projwarranty_excel_download"
    _description = "專案保固資訊匯出資料夾"
    _order = "create_date desc"
    _rec_name = "proj_no"


    proj_no = fields.Char(string="匯出專案號碼")
    xls_file = fields.Binary(string="專案保固資訊下載",attachment=False)
    xls_file_name = fields.Char(string="專案保固資訊檔名")
    run_desc = fields.Char(string="匯出說明")
    export_date = fields.Date(string="匯出日")
    export_owner = fields.Many2one('res.users', string="匯出人")


