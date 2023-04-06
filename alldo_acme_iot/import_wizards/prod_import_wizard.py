# -*- coding: utf-8 -*-
# Author : Peter Wu


import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class prodwizard(models.TransientModel):
    _name = "alldo_acme_iot.prod_wizard"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    excel_sheet_num = fields.Integer(string=u"工作底稿序號", default=0)
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=2)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=2)

    def prod_import(self):
        if self.start_row == 1 :
            raise UserError(u"數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 2 or self.end_row < 2:
            raise UserError(u"數值錯誤,ROW數值不能小於2")
        if self.start_row > self.end_row:
            raise UserError(u"數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError(u"檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(self.excel_sheet_num)
        if self.start_row > 1 or self.end_row > 1:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 2
            nendrow = sheet.nrows

        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(self.excel_sheet_num)

        myrec = self.env['product.template'].search([])
        for row in range(nstartrow -1, nendrow):

            cell = sheet.cell(row, 0)   # 客戶
            mycusname = ' '
            mycusno = 0
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycusname = str(cell.value)
            if mycusname != ' ' :
                mycusrec = self.env['res.partner'].search([('name','like',mycusname)])
                # self.env.cr.execute("""select getpartnerid('%s')""" % mycusname)
                mycusno = mycusrec.id
            print('客戶：%d' % mycusno)

            cell = sheet.cell(row, 1)   # 料號
            myproductno = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myproductno = str(cell.value)
            print('料號:%s' % myproductno)


            cell = sheet.cell(row, 2)   # 品名規格
            myprodspec = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodspec = str(cell.value)
            print('品名規格：%s' % myprodspec)

            cell = sheet.cell(row, 5)   # 版次
            myversion = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myversion = str(cell.value)
            print('版次:%s' % myversion)

            cell = sheet.cell(row, 6)   # 粗胚重量
            myblankweight = ' '
            myblankweight1 = 0.00
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myblankweight = str(cell.value)
            if myblankweight == ' ' :
                myblankweight1 = 0.00
            else:
                if myblankweight[-2:].upper()=='KG':
                    myblankweight1=float(myblankweight[:-2])
                else:
                    myblankweight1=float(myblankweight)
            print('粗胚:%s' % myblankweight)
            print('粗胚:%s' % myblankweight1)


            cell = sheet.cell(row, 7)  # 鑄件重量
            mycasting = ' '
            mycasting1 = 0.00
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mycasting = str(cell.value)
            if mycasting == ' ' :
                mycasting1 = 0.00
            else:
                if mycasting[-2:].upper()=='KG':
                    mycasting1=float(mycasting[:-2])
                else:
                    mycasting1=float(mycasting)
            print('鑄件:%s' % mycasting)
            print('鑄件:%s' % mycasting1)

            cell = sheet.cell(row, 8)  # 成品重量
            myprodweight = ' '
            myprodweight1 = 0.00
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodweight = str(cell.value)
            if myprodweight == ' ' :
                myprodweight1 = 0.00
            else:
                if myprodweight[-2:].upper()=='KG':
                    myprodweight1=float(myprodweight[:-2])
                else:
                    myprodweight1=float(myprodweight)
            print('成品:%s' % myprodweight)
            print('成品:%s' % myprodweight1)

            cell = sheet.cell(row, 9)  # 用於銷售
            mysaleok = 'N'
            mysaleok1 = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mysaleok = str(cell.value)
                if mysaleok.upper()=='Y':
                    mysaleok1 = True
                else:
                    mysaleok1 = False
            print('銷售:%s' % mysaleok1)

            cell = sheet.cell(row, 10)  # 用於採購
            mypurchaseok = 'N'
            mypurchaseok1 = False
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mypurchaseok = str(cell.value)
                if mypurchaseok.upper()=='Y':
                    mypurchaseok1=True
                else:
                    mypurchaseok1=False
            print('採購:%s' % mypurchaseok1)

            if mycusno > 0 :
                myrec.create({'default_code':myproductno,'barcode':myproductno,'type':'product','name':myprodspec,
                              'sale_ok':mysaleok1,'purchase_ok':mypurchaseok1,'blank_weight':myblankweight1,'casting_weight':mycasting1,
                              'prod_weight':myprodweight1,'cus_no':mycusno})
            else:
                myrec.create({'default_code': myproductno, 'barcode': myproductno, 'type': 'product', 'name': myprodspec,
                     'sale_ok': mysaleok1, 'purchase_ok': mypurchaseok1, 'blank_weight': myblankweight1,
                     'casting_weight': mycasting1,'prod_weight': myprodweight1})

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '產品資料匯入完成！'
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