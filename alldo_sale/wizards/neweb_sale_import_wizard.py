# -*- coding: utf-8 -*-
# Author: Peter Wu

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


class saleimportwizard(models.TransientModel):
    _name = "neweb.saleorder_import_wizard"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=0)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=0)
    # auto_finish = fields.Boolean(string=u"項次自動編號", default=True)


    def validate_date_str(self,date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def converdate(self,s):
        try:
            s = str(int(s))
        except ValueError:
            date_dt = ''
            print('日期格式不對')

        if len(s) == 6 or len(s) == 7 or len(s) == 8:
            if len(s) == 6:
                year_s = s[:2]
                mon = s[2:4]
                day = s[4:]
                year = str(int(year_s) + 1911)
            if len(s) == 7:
                year_s = s[:3]
                mon = s[3:5]
                day = s[5:]
                year = str(int(year_s) + 1911)
            if len(s) == 8:
                year = s[:4]
                mon = s[4:6]
                day = s[6:]
            date_str = year + '-' + str(mon) + '-' + str(day)
            try:
                date_dt = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                date_dt = ''
                print('日期格式不對')
        else:
            date_dt = ''
            print('日期格式不對')
        return (date_dt)

    def sale_action_import(self):
        if self.start_row == 1 :
            raise UserError(u"數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 0 or self.end_row < 0:
            raise UserError(u"數值錯誤,ROW數值不能小於0")
        if self.start_row > self.end_row:
            raise UserError(u"數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError(u"檔案錯誤,沒有上傳正確的Excel File")
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
            #print "%s" % nendrow
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.ensure_one()
        sale_rec = self.env['sale.order'].search([('id', '=', self.env.context.get('sale_op_id'))])
        mysaleid = self.env.context.get('sale_op_id')
        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        # nstartrow = 1
        # nendrow = sheet.nrows

        myamounttot = 0

        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 8)
            mysitemnum = 0
            try:
                if cell.ctype == XL_CELL_EMPTY:
                    raise UserError("數量必須大於0")
                    mysitemnum = 0
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemnum = float(sheet.cell(row, 8).value)  # 數量
                    else:
                        raise UserError("數量必須大於0")
                        mysitemnum = 0
            except Exception as inst:
                mysitemnum = 1
            # print "5:%s" % mysitemnum

            cell = sheet.cell(row, 9)
            mysitemprice = 0
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemprice = float(sheet.cell(row, 9).value)  # 單價
                    else:
                        mysitemprice = 0
            except Exception as inst:
                mysitemprice = 0

            myamounttot = myamounttot + (mysitemnum * mysitemprice)

        if myamounttot == 0 :
           raise UserError(u"報價單 Excel 總收入不能是 0 ")

        for row in range(nstartrow -1, nendrow):

            cell = sheet.cell(row, 1)
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitemitem = u'' + str(cell.value).decode('utf-8')  # 項次
                else:
                    mysitemitem = False
            except Exception as inst:
                myitemitem = False
            # print "3:%s" % mysitemdesc

            cell = sheet.cell(row, 2)
            myprodsetid = False
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                    mysitembrand = u'' + str(cell.value).decode('utf-8')  # 品牌
                    myprodset = self.env['neweb.prodbrand'].search([('name', 'ilike', mysitembrand)])
                    if myprodset:
                       for rec in myprodset:
                           if len(rec.name) == len(mysitembrand):
                              myprodsetid = rec.id
                           else:
                              myprodsetid = False
            except Exception as inst:
                myprodsetid = False
            # print "2:%s" % myprodsetid


            cell = sheet.cell(row, 3)                                  # 共契組別-項次
            mysitemmodeltype = ' '
            try:
                if cell.ctype == XL_CELL_EMPTY:
                   cell = sheet.cell(row,4)                                # 機種/機型-料號
                   if cell.ctype == XL_CELL_EMPTY:
                      # raise UserError("機種/機型-料號欄位不得空白")
                      mysitemmodeltype = '-'
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitemmodeltype = u'' + str(cell.value).decode('utf-8')  # 共契組別 & 機種-機型/料號
            except Exception as inst:
                mysitemmodeltype = '-'

            cell = sheet.cell(row, 5)
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitemserial = u'' + str(cell.value).decode('utf-8')  # 序號
                else:
                    mysitemserial = ' '
            except Exception as inst:
                mysitemserial = ' '

            cell = sheet.cell(row, 6)
            # try:
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymaindate = u'' + str(cell.value).decode('utf-8')  # 維護起迄日期
                mymaindate=mymaindate.strip()
                if mymaindate == '':
                    mymainstart = False
                    mymainend = False
                    mymaindate = False
                else:
                    mymainstart = self.converdate(mymaindate[0:8])
                    mymainend = self.converdate(mymaindate[9:])
            else:
                mymainstart = False
                mymainend = False
                mymaindate = False



            cell = sheet.cell(row, 7)
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                    mysitemdesc = u'' + str(cell.value).decode('utf-8')  # 品名規格
                else:
                    mysitemdesc = ' '
            except Exception as inst:
                mysitemdesc = ' '
            # print "3:%s" % mysitemdesc

            cell = sheet.cell(row, 8)
            mysitemnum = 0
            try:
                if cell.ctype == XL_CELL_EMPTY:
                   raise UserError("數量必須大於0")
                   mysitemnum = 0
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER :
                      mysitemnum = float(sheet.cell(row, 8).value)  # 數量
                   else:
                      raise UserError("數量必須大於0")
                      mysitemnum = 0
            except Exception as inst:
                mysitemnum = 1
            # print "5:%s" % mysitemnum

            cell = sheet.cell(row, 9)
            mysitemprice = 0
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER :
                      mysitemprice = float(sheet.cell(row, 9).value)  # 單價
                   else:
                      mysitemprice = 0
            except Exception as inst:
                mysitemprice = 0
            # print "6:%s" % mysitemprice

            cell = sheet.cell(row, 11)
            mysitemcost = 0
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER:
                      mysitemcost = float(sheet.cell(row, 11).value)  # 成本
                   else:
                      mysitemcost = 0
            except Exception as inst:
                mysitemcost = 0

            # print "8:%s" % mysitemcost
            if mymainstart == False or mymainend == False :
                try:
                    sale_rec.write({'display_line': [(0, 0, {'sitem_modeltype': mysitemmodeltype ,'sitem_brand': myprodsetid,
                                   'sitem_desc': mysitemdesc, 'sitem_num': mysitemnum,
                                   'sitem_price': mysitemprice, 'sitem_cost': mysitemcost,
                                   'sitem_item': mysitemitem,'sitem_serial':mysitemserial })]})
                except Exception as inst:
                    myresult = False
            else:
                try:
                    sale_rec.write(
                           {'maintenance_start':mymainstart,'maintenance_end':mymainend,
                            'display_line': [(0, 0, {'sitem_modeltype': mysitemmodeltype, 'sitem_brand': myprodsetid,
                                                  'sitem_desc': mysitemdesc, 'sitem_num': mysitemnum,
                                                  'sitem_price': mysitemprice, 'sitem_cost': mysitemcost,
                                                  'sitem_item': mysitemitem, 'sitem_serial': mysitemserial,
                                                  'maintenance_start':mymainstart,'maintenance_end':mymainend,
                                                  'newebmaindate':mymaindate})]})
                except Exception as inst:
                    myresult = False

        self.env.cr.execute("select update_discount_amount(%d)" % mysaleid)