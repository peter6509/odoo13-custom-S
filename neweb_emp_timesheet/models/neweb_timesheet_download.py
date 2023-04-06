# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from io import BytesIO
import base64,xlsxwriter
from odoo.exceptions import UserError


class timesheetdownload(models.Model):
    _name = "neweb_emp_timesheet.timesheet_download"
    _description = "工時記錄EXCEL匯出資料夾"
    _order = "create_date desc"

    xls_file = fields.Binary(string="下載",attachment=False)
    xls_file_name = fields.Char(string="檔案")
    run_desc = fields.Char(string="匯出檔案說明")