# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
CONTRACTTYPE=[('1','契約書'),
              ('2','申請書'),
              ('3','月報'),
              ('4','週報')]

class CloudRentDocFilename(models.Model):
    _name = "cloudrent.doc_filename"
    _description = "雲房相關文件名稱檔名"

    name = fields.Char(string="表單名稱")
    name1 = fields.Many2one('cloudrent.contract_data',string="契約書/申請書")
    contract_type = fields.Selection(CONTRACTTYPE,select=True,string="文檔類型")
    contract_version = fields.Many2one('cloudrent.contract_version', string="版本期數")
    doc_type = fields.Selection([('1','代管'),('2','房東'),('3','房客')],string="用途分類")
    doc_filename = fields.Char(string="文件檔名")
    doc_filename1 = fields.Char(string="文件檔名顯示用途")
    doc_filename2 = fields.Char(string="文件檔名顯示用途")
    doc_binfile = fields.Binary(string="上傳(電腦套印)模板",attachment=False)
    doc_binfile1 = fields.Binary(string="上傳(空白)模板",attachment=False)
    doc_active = fields.Selection([('1','啟用'),('2','停用')],string="文檔狀態",default='1')


    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.contract_version.name, myrec.name1.name)
            result.append((myrec.id, myname))
        return result



