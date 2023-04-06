# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class eraexceldownload(models.Model):
    _name = "era.excel_download"
    _description = u"EXCEL匯出資料夾"
    _order = "create_date desc"

    download_name = fields.Char(string=u"報表名稱")
    xls_file = fields.Binary(string=u"檔案下載")
    xls_file_name = fields.Char(string=u"檔名")


    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.download_name,myrec.create_uid.login)
            result.append((myrec.id, myname))
        return result

