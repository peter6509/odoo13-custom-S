# -*- coding: utf-8 -*-
# Author : Peter Wu


import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class partnerwizard(models.TransientModel):
    _name = "alldo_acme_iot.partner_wizard"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    partner_type = fields.Selection([('1',u'客戶'),('2',u'供應商'),('3',u'兩者皆是')],string=u"合作伙伴類別",default='1')
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=2)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=2)


    def respartner_import(self):
        if self.start_row == 1 :
            raise UserError(u"數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 2 or self.end_row < 2:
            raise UserError(u"數值錯誤,ROW數值不能小於2")
        if self.start_row > self.end_row:
            raise UserError(u"數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError(u"檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        if self.start_row > 1 or self.end_row > 1:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 2
            nendrow = sheet.nrows
            # print "%s" % nendrow
        # reload(sys)

        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        myrec = self.env['res.partner'].search([])

        for row in range(nstartrow -1, nendrow):
            mypartnertype='1'
            if self.partner_type:
               mypartnertype=self.partner_type
            if mypartnertype=='1':
                mycustomerrank = 1
                mysupplierrank = 0
            elif mypartnertype=='2':
                mycustomerrank = 0
                mysupplierrank = 1
            else :
                mycustomerrank = 1
                mysupplierrank = 1

            cell = sheet.cell(row, 0)  # 客戶編號
            mypartnercode = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mypartnercode =str(cell.value)     # partner code
            print(mypartnercode)

            cell = sheet.cell(row, 1)  # 客戶名稱
            mypartnername = ' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mypartnername =  str(cell.value)     # partner name
            print(mypartnername)


            cell = sheet.cell(row, 2)  # 客戶類別
            mycategoryname = ' '
            mycategoryid = 0
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycategoryname = str(cell.value)        # partner category
               self.env.cr.execute("""select getpartnertype('%s')""" % mycategoryname)
               mycategoryid = self.env.cr.fetchone()[0]
            print(mycategoryname)
            print(mycategoryid)

            cell = sheet.cell(row, 3)  # 統一編號
            myvat = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myvat =  str(cell.value)       # 統一編號
            print(myvat)


            cell = sheet.cell(row, 4)    # 地址
            myaddress = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myaddress = str(cell.value)         # 地址
            print(myaddress)


            cell = sheet.cell(row, 5)     # 聯絡電話
            mypartnerphone = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mypartnerphone = str(cell.value)    # 聯絡電話
            print(mypartnerphone)


            cell = sheet.cell(row, 6)    # 傳真
            myfax = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                myfax = str(cell.value)           # 傳真
            print(myfax)

            cell = sheet.cell(row, 7)    # 負責人
            myboss = ' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myboss = str(cell.value)        # 負責人
            print(myboss)

            if len(myboss)>0 and myboss != ' ':
                myid = myrec.create({'company_type': 'company', 'partner_code': mypartnercode, 'name':mypartnername,'street': myaddress,'vat': myvat, 'phone': mypartnerphone,'customer_rank': mycustomerrank,'supplier_rank':mysupplierrank})
                self.env.cr.execute("""insert into res_partner_res_partner_category_rel(category_id,partner_id) values (%d,%d)""" % (mycategoryid,myid.id))
                self.env.cr.execute("""commit""")
                myrec.create({'company_type':'person','name':myboss,'parent_id':myid.id})
            else:
                myid = myrec.create({'company_type':'company','partner_code':mypartnercode, 'name':mypartnername,'street':myaddress,'vat':myvat,'phone':mypartnerphone,'customer_rank': mycustomerrank,'supplier_rank':mysupplierrank})
                self.env.cr.execute("""insert into res_partner_res_partner_category_rel(category_id,partner_id) values (%d,%d)""" % (mycategoryid, myid.id))
                self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '客戶資料匯入完成！'
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }