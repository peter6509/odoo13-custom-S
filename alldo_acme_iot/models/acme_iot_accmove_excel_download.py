# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class alldoaccmoveexceldownload(models.Model):
    _name = "alldo_acme_iot.accmove_excel_download"
    _description = u"應收帳款 EXCEL匯出資料夾"
    _order = "create_date desc"

    emp_no = fields.Many2one('hr.employee',string=u"人員")
    download_name = fields.Char(string=u"報表名稱")
    xls_file = fields.Binary(string=u"檔案下載",attachment=False)
    xls_file_name = fields.Char(string=u"檔名")
    run_desc = fields.Char(string=u"匯出說明")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.download_name,myrec.emp_no.name)
            result.append((myrec.id, myname))
        return result
