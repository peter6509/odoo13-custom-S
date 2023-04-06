# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoiplaiotexceldownload(models.Model):
    _name = "alldo_ipla_iot.excel_download"
    _description = u"EXCEL匯出資料夾"
    _order = "create_date desc"

    emp_no = fields.Many2one('hr.employee',string=u"人員")
    download_name = fields.Char(string=u"報表名稱")
    xls_file = fields.Binary(string=u"檔案下載")
    xls_file_name = fields.Char(string=u"檔名")
    run_desc = fields.Char(string=u"匯出說明")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.download_name,myrec.emp_no.name)
            result.append((myrec.id, myname))
        return result
