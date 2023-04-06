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


class moldwizard(models.TransientModel):
    _name = "alldo_acme_iot.mold_wizard"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    excel_sheet_num = fields.Integer(string=u"工作底稿序號", default=0)
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=2)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=2)

    def mold_import(self):
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

        myrec = self.env['alldo_acme_iot.acme_mold'].search([])
        for row in range(nstartrow -1, nendrow):
            cell = sheet.cell(row, 0)   # 料號
            myproductno = ' '
            myprodtmplid = 0
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myproductno = str(cell.value)
               if myproductno[-2:]=='.0':
                   myproductno = int(myproductno[:-2])
               myprodtmplid = self.env['product.template'].search([('default_code','like',myproductno)]).id

            print('料號:%s' % myproductno)
            print('prodtmplid:%d' % myprodtmplid)

            cell = sheet.cell(row, 1)   # 模具編號
            mymoldno = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mymoldno = str(cell.value)
               if mymoldno[-2:]=='.0':
                   mymoldno = int(mymoldno[:-2])
            print('模具編號：%s' % mymoldno)

            cell = sheet.cell(row, 2)  # 模具說明
            mymoldspec = ' '
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymoldspec = str(cell.value)
            if mymoldspec == ' ' :
                mymoldspec = mymoldno
            print('模具說明：%s' % mymoldspec)

            cell = sheet.cell(row, 3)   # 版次
            myversion = ' '
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myversion = str(cell.value)
            print('版次:%s' % myversion)

            cell = sheet.cell(row, 4)  # 所屬客戶
            mycusname = ' '
            mycusno = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycusname = str(cell.value)
            if mycusname != ' ':
                mycusrec = self.env['res.partner'].search([('name', 'like', mycusname)])
                mycusno = mycusrec.id
            print('所屬客戶：%s' % mycusname)
            print('所屬客戶：%s' % mycusno)


            cell = sheet.cell(row, 6)   # 開模廠商
            mymoldsupp = ' '
            mymoldsupp1 = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymoldsupp = str(cell.value)
            if mymoldsupp != ' ':
                mymoldsupprec = self.env['res.partner'].search([('name', 'like', mymoldsupp)])
                mymoldsupp1 = mymoldsupprec.id
            print('開模廠商：%s' % mymoldsupp)
            print('開模廠商：%s' % mymoldsupp1)


            cell = sheet.cell(row, 7)  # 使用壽命次數
            mylifespan = ' '
            mylifespan1 = 0
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mylifespan = str(cell.value)
                if mylifespan.isdigit():
                   mylifespan1 = int(mylifespan)
                else:
                   mylifespan1 = 0
            print('壽命:%s' % mylifespan)
            print('壽命:%s' % mylifespan1)

            cell = sheet.cell(row, 8)  # 目前次數
            mycurrenttime = ' '
            mycurrenttime1 = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycurrenttime = str(cell.value)
                if mycurrenttime.isdigit():
                    mycurrenttime1 = int(mycurrenttime)
                else:
                    mycurrenttime1 = 0
            print('目前次數:%s' % mycurrenttime)
            print('目前次數:%s' % mycurrenttime1)

            cell = sheet.cell(row, 9)  # 模穴數
            mymoldcavity = ' '
            # mymoldcavity1 = 1
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mymoldcavity = str(cell.value)
                mymoldcavity1 = int(float(mymoldcavity))
            print('模穴數:%s' % mymoldcavity1)


            myid = myrec.create({'mold_no':mymoldno,'mold_barcode':mymoldno,'name':mymoldno,'mold_ver':myversion,
                                 'lifespan_times':mylifespan1,'current_times':mycurrenttime1,'mold_cavity':mymoldcavity1})

            if mycusno > 0 :
                self.env.cr.execute("""update alldo_acme_iot_acme_mold set partner_id=%d where id=%d""" % (mycusno,myid))
                self.env.cr.execute("""commit""")
            if mymoldsupp1 > 0 :
                self.env.cr.execute("""update alldo_acme_iot_acme_mold set mold_supplier_id=%d where id=%d""" % (mymoldsupp1, myid))
                self.env.cr.execute("""commit""")

            self.env.cr.execute("""select setprodmold(%d,%d)""" % (myprodtmplid, myid))
            self.env.cr.execute("""commit""")




        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '模具資料匯入完成！'
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