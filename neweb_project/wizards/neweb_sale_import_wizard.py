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

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
    start_row = fields.Integer(size=3, string="啟始ROW", default=0)
    end_row = fields.Integer(size=3, string="結止ROW", default=0)
    # auto_finish = fields.Boolean(string="項次自動編號", default=True)


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
            #print "%s" % nendrow
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        self.ensure_one()
        sale_rec = self.env['sale.order'].search([('id', '=', self.env.context.get('sale_op_id'))])
        mysaleid = self.env.context.get('sale_op_id')
        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        # nstartrow = 1
        # nendrow = sheet.nrows

        myamounttot = 0

        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 9)
            mysitemnum = 0
            try:
                if cell.ctype == XL_CELL_EMPTY:
                    raise UserError("數量必須大於0")
                    mysitemnum = 0
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemnum = float(sheet.cell(row, 9).value)  # 數量
                    else:
                        raise UserError("數量必須大於0")
                        mysitemnum = 0
            except Exception as inst:
                mysitemnum = 1
            # print "5:%s" % mysitemnum

            cell = sheet.cell(row, 10)
            mysitemprice = 0
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    if cell.ctype == XL_CELL_NUMBER:
                        mysitemprice = float(sheet.cell(row, 10).value)  # 單價
                    else:
                        mysitemprice = 0
            except Exception as inst:
                mysitemprice = 0

            myamounttot = myamounttot + (mysitemnum * mysitemprice)

        if myamounttot == 0 :
           raise UserError("報價單 Excel 總收入不能是 0 ")

        for row in range(nstartrow -1, nendrow):
            cell = sheet.cell(row, 0)
            myprodset = False
            myprodsetid = False
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    myprodset = '' + str(cell.value)  # 產品組別
                    myprodset1 = myprodset.replace(' ', '').replace('/', '').replace(' ', '').upper()
                    myprodsetrec = self.env['neweb.prodset'].search([('name1', '=ilike', myprodset1)])
                    if myprodsetrec:
                        for rec in myprodsetrec:
                            myprodsetid = rec.id
            except Exception as inst:
                myprodsetid = False


            # cell = sheet.cell(row, 0)
            # myprodset = False
            # myprodsetid = False
            # if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
            #     myprodset = '' + str(cell.value)  # 產品組別
            #     myprodset1 = myprodset.replace(' ', '').replace('/', '').replace(' ', '').upper()
            #     if myprodset1 != False:
            #         self.env.cr.execute("""select getprodset1('%s')""" % myprodset1)
            #         myprodsetid = self.env.cr.fetchone()[0]
            #         self.env.cr.execute("""commit""")
            #     else:
            #         myprodsetid = False


            cell = sheet.cell(row, 1)
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitemitem = '' + str(cell.value)  # 項次
                else:
                    mysitemitem = False
            except Exception as inst:
                myitemitem = False
            # print "3:%s" % mysitemdesc

            cell = sheet.cell(row, 2)
            myprodbrandid = False
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                    mysitembrand = '' + str(cell.value)  # 品牌
                    if mysitembrand != False:
                        self.env.cr.execute("""select getprodbrand1('%s')""" % mysitembrand)
                        myprodbrandid = self.env.cr.fetchone()[0]
                        #self.env.cr.execute("""commit""")
                    else:
                        myprodbrandid = False

            except Exception as inst:
                myprodbrandid = False
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
                    if str(cell.value)[-2:] == '.0':
                        mysitemmodeltype = '' + str(cell.value)[:-2]  # 共契組別 & 機種-機型/料號
                    else:
                        mysitemmodeltype = '' + str(cell.value)  # 共契組別 & 機種-機型/料號
            except Exception as inst:
                mysitemmodeltype = '-'

            mysitemmodeltype1 = False
            cell = sheet.cell(row, 5)  # 機型名稱
            try:
                if cell.ctype == XL_CELL_EMPTY:
                    mysitemmodeltype1 = False
                else:
                    mymodeltype1=''+str(cell.value) # 機型名稱
                    self.env.cr.execute("""select getmodeltype1('%s')""" % mymodeltype1)
                    mysitemmodeltype1 = self.env.cr.fetchone()[0] # 機型名稱
                    # mysitemmodeltype1 = int(cell.value)    # 機型名稱

            except Exception as inst:
                mysitemmodeltype1 = False

            cell = sheet.cell(row, 6)
            mysitemserial = ' '
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mysitemserial = '' + str(cell.value)  # 序號
                else:
                    mysitemserial = ' '
            except Exception as inst:
                mysitemserial = ' '

            cell = sheet.cell(row, 7)
            # try:
            mymainstart = False
            mymainend = False
            mymaindate = False
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mymaindate = '' + str(cell.value)  # 維護起迄日期
                mymaindate=mymaindate.strip()
                if len(mymaindate[0:8]) != 8 :
                    raise UserError("""%s 維護起始日期碼數不正確！""" % mymaindate[0:8])
                if len(mymaindate[9:17]) != 8 :
                    raise UserError("""%s 維護截止日期碼數不正確！""" % mymaindate[9:17])
                if mymaindate == '':
                    mymainstart = False
                    mymainend = False
                    mymaindate = False
                else:
                    mymainstart = self.converdate(mymaindate[0:8])
                    mymainend = self.converdate(mymaindate[9:17])
            else:
                mymainstart = False
                mymainend = False
                mymaindate = False



            cell = sheet.cell(row, 8)
            mysitemdesc = ' '
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                    mysitemdesc = '' + str(cell.value)  # 品名規格
                else:
                    mysitemdesc = ' '
            except Exception as inst:
                mysitemdesc = ' '
            # print "3:%s" % mysitemdesc

            cell = sheet.cell(row, 9)
            mysitemnum = 0
            try:
                if cell.ctype == XL_CELL_EMPTY:
                   raise UserError("數量必須大於0")
                   mysitemnum = 0
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER :
                      mysitemnum = float(sheet.cell(row, 9).value)  # 數量
                   else:
                      raise UserError("數量必須大於0")
                      mysitemnum = 0
            except Exception as inst:
                mysitemnum = 1
            # print "5:%s" % mysitemnum

            cell = sheet.cell(row, 10)
            mysitemprice = 0
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER :
                      mysitemprice = float(sheet.cell(row, 10).value)  # 單價
                   else:
                      mysitemprice = 0
            except Exception as inst:
                mysitemprice = 0
            # print "6:%s" % mysitemprice

            cell = sheet.cell(row, 12)
            mysitemcost = 0
            try:
                if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                   if cell.ctype == XL_CELL_NUMBER:
                      mysitemcost = float(sheet.cell(row, 12).value)  # 成本
                   else:
                      mysitemcost = 0
            except Exception as inst:
                mysitemcost = 0

            cell = sheet.cell(row, 13)
            mysupplier = False
            if cell.ctype in (XL_CELL_EMPTY, XL_CELL_BLANK):
                mysupplier = False
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mysuppliername = '' + str(cell.value)  # 供應商
                mysupplierrec = self.env['res.partner'].search(
                    [('comp_sname', 'like', mysuppliername), ('active', '=', True), ('is_company', '=', True)])
                if mysupplierrec:
                    for rec in mysupplierrec:
                        mysupplier = rec.id
                else:
                    mysupplier = False

            cell = sheet.cell(row, 14)
            mycosttypeid = False
            if cell.ctype == XL_CELL_EMPTY:
                mycosttypeid = False
            else:
                mycosttype = '' + str(cell.value)  # 成本類型
                if mycosttype != False:
                    self.env.cr.execute("""select getcosttype1('%s')""" % mycosttype)
                    mycosttypeid = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""commit""")
                else:
                    mycosttypeid = False
                # mycosttyperec = self.env['neweb.costtype'].search([('name', '=ilike', mycosttype)])
                # if mycosttyperec:
                #     for rec in mycosttyperec:
                #         mycosttypeid = rec.id
                #         # mycosttypeid = mycosttyperec[0].id
                # else:
                #     mycosttypeid = False

            cell = sheet.cell(row, 18)
            mycostdeptid = False
            if cell.ctype in (XL_CELL_EMPTY, XL_CELL_BLANK):
                mycostdeptid = False
            else:
                mycostdept = '' + str(cell.value)  # 部門
                if mycostdept != False:
                    self.env.cr.execute("""select getcostdept('%s')""" % mycostdept)
                    mycostdeptid = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""commit""")
                else:
                    mycostdeptid = False
                if mycostdeptid == 0:
                    mycostdeptid = False

            # print "8:%s" % mysitemcost
            if mymainstart == False or mymainend == False :
                try:
                    sale_rec.write({'display_line': [(0, 0, {'sitem_modeltype': mysitemmodeltype,'sitem_modeltype1': mysitemmodeltype1 ,'sitem_brand': myprodbrandid,
                                   'sitem_desc': mysitemdesc, 'sitem_num': mysitemnum,
                                   'sitem_price': mysitemprice, 'sitem_cost': mysitemcost,
                                   'sitem_item': mysitemitem,'sitem_serial':mysitemserial,
                                    'cost_type': mycosttypeid,'cost_dept':mycostdeptid,'prod_set':myprodsetid,'supplier':mysupplier})]})

                except Exception as inst:
                    myresult = False
            else:

                sale_rec.write(
                       {'maintenance_start':mymainstart,'maintenance_end':mymainend,
                        'display_line': [(0, 0, {'sitem_modeltype': mysitemmodeltype,'sitem_modeltype1': mysitemmodeltype1 , 'sitem_brand': myprodbrandid,
                                              'sitem_desc': mysitemdesc, 'sitem_num': mysitemnum,'prod_set':myprodsetid,
                                              'sitem_price': mysitemprice, 'sitem_cost': mysitemcost,
                                              'sitem_item': mysitemitem, 'sitem_serial': mysitemserial,
                                              'maintenance_start':mymainstart,'maintenance_end':mymainend,
                                              'newebmaindate':mymaindate,'cost_type': mycosttypeid,'cost_dept':mycostdeptid,'supplier':mysupplier})]})


            # sale_rec.env.cr.commit()

        self.env.cr.execute("select update_discount_amount(%d)" % mysaleid)
        self.env.cr.execute("""commit""")