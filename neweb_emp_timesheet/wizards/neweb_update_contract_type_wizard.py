# -*- coding: utf-8 -*-
# Author : Peter Wu


import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import sys
from datetime import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6



class newebimporttimesheetwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.update_contract"

    passcode = fields.Char(string="執行碼")
    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)

    #
    # def _getemp(self):
    #     myemp = self.env['hr.employee'].search([('user_id','=', self.env.uid)])
    #     return myemp.id

    def action_import(self):

        if self.passcode != '!99999ibm':
            raise UserError("執行碼錯誤！")

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        nstartrow = 2
        nendrow = sheet.nrows

        # print "NEDROW:%s" % nendrow
        # print "EMPID:%s" % self.emp_id.id

        # reload(sys)
        sys.setdefaultencoding('utf-8')
        self.ensure_one()

        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        # myworkdate1 = ''
        for row in range(nstartrow - 1, nendrow - 1):
            cell = sheet.cell(row, 0)     # 合約編號

            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycontractno = '' + str(cell.value).strip().decode('utf-8')

            cell = sheet.cell(row, 1)   # 專案編號

            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER) :
                myprojectno = '' + str(cell.value).strip().decode('utf-8')

            self.env.cr.execute("""select update_contract_type('%s')""" % mycontractno)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select update_contract_type1('%s')""" % myprojectno)
            self.env.cr.execute("""commit""")


        print("OK")