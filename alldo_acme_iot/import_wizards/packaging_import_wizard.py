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


class packagingimportwizard(models.TransientModel):
    _name = "alldo_acme_iot.packaging_import_wizard"
    _description = "出貨耗材清單匯入精靈"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=2)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=2)

    def packaging_import(self):
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

        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        # xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        # sheet = xls.sheet_by_index(0)

        myrec = self.env['product.template'].search([])
        for row in range(nstartrow -1, nendrow):

            cell = sheet.cell(row, 0)   # 包材料號
            mypackagingno = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mypackagingno = str(cell.value)
            # print('包材料號:%s' % mypackagingno)


            cell = sheet.cell(row, 1)   # 品名規格
            myprodspec = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodspec = str(cell.value)
            # print('品名規格：%s' % myprodspec)

            cell = sheet.cell(row, 2)   # 類型 原物料'1'/成品'2'/包材'3'
            mytype1 = '3'
            mycategid=4
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mytype1 = str(cell.value).strip()
               if mytype1=='1':
                   mycategid=5
               elif mytype1=='2':
                   mycategid=1
               else:
                   mycategid=4


            cell = sheet.cell(row, 3)   # 庫存型態 可庫存產品'1'/消耗品'2'/服務'3'
            mycateg = '1'
            mytype='product'
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycateg = str(cell.value).strip()
               if mycateg=='1':
                   mytype='product'
               elif mycateg=='2':
                   mytype='consu'
               else:
                   mytype='service'


            cell = sheet.cell(row, 4)  # 可用於銷售 'Y/N'
            mysale='Y'
            saleok=True
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mysale = str(cell.value).strip()
                if mysale=='Y':
                    saleok=True
                else:
                    saleok=False


            cell = sheet.cell(row, 5)  # 可用於採購 'Y/N'
            mypurchase='Y'
            purchasok=True
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mypurchase = str(cell.value).strip()
               if mypurchase=='Y':
                   purchaseok=True
               else:
                   purchaseok=False


            cell = sheet.cell(row, 6)  # 對應產品
            myproductno = ' '
            mycusno = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                myproductno = str(cell.value)
                myprodid = self.env['product.template'].search([('default_code','=',myproductno)]).id
                self.env.cr.execute("""select getprodcus(%d)""" % myprodid)
                mycusno=self.env.cr.fetchone()[0]


            cell = sheet.cell(row, 7)  # 對比數
            myprodnum=' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myprodnum = str(cell.value).strip()
                x = myprodnum.find('：')
                # print('%s' % myprodnum[:x])
                # print('%s' % myprodnum[x+1:])
                myprodnum1 = int(myprodnum[:x])
                myprodnum2 = int(myprodnum[x+1:])
                print(myprodnum1)
                print(myprodnum2)


            # if mycusno > 0 :
            self.env.cr.execute("""select chkhaveprod('%s')""" % mypackagingno)
            myres = self.env.cr.fetchone()[0]

            if not myres:
                myrec.create({'default_code':mypackagingno,'barcode':mypackagingno,'type':mytype,'name':myprodspec,'categ_id':mycategid,
                              'sale_ok':saleok,'purchase_ok':purchasok,'blank_weight':0,'casting_weight':0,
                              'prod_weight':0,'cus_no':mycusno})
            self.env.cr.execute("""select genpackagingbom('%s','%s',%d,%d)""" % (mypackagingno,myproductno,myprodnum1,myprodnum2))
            self.env.cr.execute("""commit""")

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