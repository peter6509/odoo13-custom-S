# -*- coding: utf-8 -*-
# Author : Peter Wu


import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import sys
import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class ContractModelType1importwizard(models.TransientModel):
    _name = "neweb_contract.modeltyp1_import_wizard"

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
    start_row = fields.Integer(size=3, string="啟始ROW", default=3)
    end_row = fields.Integer(size=3, string="結止ROW", default=3)


    def modeltype1_import(self):
        if self.start_row == 1 :
            raise UserError("數值錯誤,ROW啟始數值從 3 開始")
        if self.start_row < 3 or self.end_row < 3:
            raise UserError("數值錯誤,ROW數值不能小於3")
        if self.start_row > self.end_row:
            raise UserError("數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        if self.start_row > 3 or self.end_row > 3:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 3
            nendrow = sheet.nrows
            # print "%s" % nendrow
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        self.ensure_one()
        #contract_rec = self.env['neweb_contract.contract'].search([('id', '=', self.env.context.get('contract_id'))])
        #print "%s" % contract_rec.id
        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        for row in range(nstartrow -1, nendrow):
            cell = sheet.cell(row, 3)  # 產品組別
            if cell.ctype == (XL_CELL_EMPTY):
                myprodset = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myprodset = '' + str(cell.value)  # 產品組別
                myprodset = myprodset.replace(' ', '').replace('/', '').replace(' ', '').upper()
            # if myprodset == '':
            #     myprodset = ' '

            cell = sheet.cell(row, 4)  # 品牌
            if cell.ctype == (XL_CELL_EMPTY):
                mybrand = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mybrand = '' + str(cell.value)  # 品牌
            # if mybrand == False:
            #     mybrand = ' '

            cell = sheet.cell(row, 5)  # 機種-機型/料號
            if cell.ctype == (XL_CELL_EMPTY):
                mymodeltype = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymodeltype = str(cell.value)  # 機種-機型/料號
            # print(len(mymodeltype))
            # if len(mymodeltype) == 1:
            #     mymodeltype = ' '

            cell = sheet.cell(row, 6)  # 機型名稱
            if cell.ctype == (XL_CELL_EMPTY):
                mymodeltype1 = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymodeltype1 = str(cell.value)  # 機型名稱
            # print(mymodeltype1)
            # if len(mymodeltype1) == 1:
            #     mymodeltype1 = ' '

            cell = sheet.cell(row, 7)  # 序號
            if cell.ctype == (XL_CELL_EMPTY):
                myserialno = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myserialno = str(cell.value)  # 序號

            cell = sheet.cell(row, 8)  # 說明
            if cell.ctype == (XL_CELL_EMPTY):
                mydesc = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mydesc = str(cell.value)
                mydesc = mydesc.replace('(',' ').replace(')',' ').replace("'",' ')

            cell = sheet.cell(row, 9)  # 設備位址
            if cell.ctype == (XL_CELL_EMPTY):
                mymachineloc = ' '
            elif cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymachineloc = str(cell.value)
                mymachineloc = mymachineloc.replace('(', ' ').replace(')', ' ').replace("'", ' ')

            cell = sheet,cell(row, 17)   # ID
            if cell.type == (XL_CELL_EMPTY):
                myid = 0
            else:
                myid = int(str(cell.value))

            if myserialno != ' ' :
                self.env.cr.execute("""select update_contract_modeltype1('%s','%s','%s','%s','%s','%s','%s',%d)""" % (myserialno,mymodeltype1,myprodset,mybrand,mymodeltype,mydesc,mymachineloc,myid))
                self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='合約更新完成'
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