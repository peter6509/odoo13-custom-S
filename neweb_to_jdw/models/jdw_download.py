# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ForJDWdownload(models.Model):
    _name = "neweb_to_jdw.excel_download"
    _description = "匯出給觔斗雲的EXCEL檔案"
    _order = "id desc"


    download_type = fields.Selection([('1','客戶資料'),('2','設備資料'),('3','合約列表'),('4','合約明細')],string="類型")
    xls_file = fields.Binary(string="專案下載",attachment=False)
    xls_file_name = fields.Char(string="專案檔名")
    run_desc = fields.Char(string="匯出說明")
    export_date = fields.Datetime(string="EXCEL匯出時間")
    export_owner = fields.Many2one('res.users',string="EXCEL匯出人")

