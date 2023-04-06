# -*- coding: utf-8 -*-
# Author : Peter Wu

import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError,Warning
import sys
from datetime import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class CustomCreditImportWzard(models.TransientModel):
    _name = "base.custom_credit_import_wizard"
    _description = "客戶授信EXCEL匯入系統"

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
    start_row = fields.Integer(size=3, string="啟始ROW", default=0)
    end_row = fields.Integer(size=3, string="結止ROW", default=0)


    def action_import(self):
        if self.start_row == 1 :
            raise UserError("數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 0 or self.end_row < 0:
            raise UserError("數值錯誤,ROW數值不能小於0")
        if self.start_row > self.end_row:
            raise UserError("數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        if self.start_row > 0 or self.end_row > 0:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 2
            nendrow = sheet.nrows


        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        # nstartrow = 2
        # nendrow = sheet.nrows

        myamounttot = 0
        mytestamounttot = 0
        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 1)  #公司名稱
            mycompname = ' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycompname = str(sheet.cell(row, 1).value)  #公司名稱


            cell = sheet.cell(row, 2)   # 資本額
            mycapital = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycapital = str(sheet.cell(row, 2).value)  # 資本額

            cell = sheet.cell(row, 3)  # 統一編號
            myvat = ' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myvat = str(sheet.cell(row, 3).value)  # 統一編號

            cell = sheet.cell(row, 4)  # 授信額度
            mycreditlmit = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycreditlmit = str(sheet.cell(row, 4).value)  # 授信額度

            self.env.cr.execute("""select ckcustomcredit('%s','%s','%s','%s')""" % (mycompname,mycapital,myvat,mycreditlmit))
            self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='客戶授信匯入完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }

