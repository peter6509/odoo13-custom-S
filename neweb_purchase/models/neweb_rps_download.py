# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebRPSDwonload(models.Model):
    _name = "neweb.rps_download"
    _description = "申購-採購-收貨 記錄下載檔"

    rps_no = fields.Char(string="下載申購編號")
    rps_sedate = fields.Char(string="下載區間")
    xls_file = fields.Binary(string="檔案下載", attachment=False)
    xls_file_name = fields.Char(string="檔名")



