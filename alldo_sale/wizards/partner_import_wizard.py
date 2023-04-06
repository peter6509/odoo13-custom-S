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


class partnerwizard(models.TransientModel):
    _name = "centtech_sale.partner_wizard"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    partner_type = fields.Selection([('1',u'客戶'),('2',u'供應商'),('3',u'兩者皆是')],string=u"合作伙伴類別",default='1')
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=0)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=0)


    @api.model_cr
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
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.ensure_one()
        # partner_rec = self.env['res.partner'].search([])
        # #print "%s" % contract_rec.id
        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        for row in range(nstartrow -1, nendrow):
            mypartnertype='1'
            if self.partner_type:
               mypartnertype=self.partner_type

            cell = sheet.cell(row, 0)
            myvat = ''
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myvat = u'' + str(cell.value).decode('utf-8')              # vat
                if len(myvat) > 8:
                    myvat=myvat[:-2]



            cell = sheet.cell(row, 1)
            myname = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myname = u'' + str(cell.value).decode('utf-8')             # name

            cell = sheet.cell(row, 2)
            mycompsname = ''
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mycompsname = u'' + str(cell.value).decode('utf-8')       # comp_sname


            cell = sheet.cell(row, 3)
            myzop = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myzip = u'' + str(cell.value).decode('utf-8')               # zopcode
               if not myzip:
                   myzip = ''
               else:
                   myzip = myzip[:-2]


            cell = sheet.cell(row, 4)
            mystreet = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mystreet = u''+ str(cell.value).decode('utf-8')             # street
               mystreet = "(%s)%s" % (myzip,mystreet)


            cell = sheet.cell(row, 5)
            mycontactname = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycontactname = u''+str(cell.value).decode('utf-8')         # contactname


            cell = sheet.cell(row, 6)
            myphone = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myphone = u''+str(cell.value).decode('utf-8')               # phone


            cell = sheet.cell(row, 7)
            mymobile = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mymobile = u''+str(cell.value).decode('utf-8')             # mobile

            cell = sheet.cell(row, 8)
            myfax = ''
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myfax = u'' + str(cell.value).decode('utf-8')              # fax


            cell = sheet.cell(row, 9)
            myemail = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myemail = u''+str(cell.value).decode('utf-8')               # email


            cell = sheet.cell(row, 10)
            mycheckoutdate = 1
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mycheckoutdaye = int(cell.value)                            # checkoutdate


            cell = sheet.cell(row, 11)
            mypaymentdays = 30
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mypaymentdays = int(cell.value)                             # payment_days


            #print "%s %s" % (mypartnername,mypartnertype1[0:1])
            if self.partner_type=='1':
               self._cr.execute("select partner1_insert('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%d)" %
                   (myvat,myname,mycompsname,mystreet,mycontactname,myphone,mymobile,myfax,myemail,mycheckoutdate,mypaymentdays))
               self._cr.execute("commit")
            if self.partner_type=='2':
               self._cr.execute("select partner2_insert('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%d)" %
                                 (myvat, myname, mycompsname, mystreet, mycontactname, myphone, mymobile, myfax, myemail,mycheckoutdate, mypaymentdays))
               self._cr.execute("commit")
            if self.partner_type=='3':
               self._cr.execute("select partner3_insert('%s','%s','%s','%s','%s','%s','%s','%s','%s',%d,%d)" %
                                 (myvat, myname, mycompsname, mystreet, mycontactname, myphone, mymobile, myfax, myemail,mycheckoutdate, mypaymentdays))
               self._cr.execute("commit")