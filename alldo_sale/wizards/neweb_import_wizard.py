# -*- coding: utf-8 -*-
# Author: Peter Wu

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


class projimportwizard(models.TransientModel):
    _name = "neweb.saleitem_import_wizard"
    _description = u"成本分析直接匯入excel"

    excel_file = fields.Binary(string=u"上傳EXCEL檔案")
    start_row = fields.Integer(size=3, string=u"啟始ROW", default=0)
    end_row = fields.Integer(size=3, string=u"結止ROW", default=0)
    auto_finish = fields.Boolean(string=u"項次自動編號", default=True)


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

    def action_import(self):
        self.env.cr.execute("""update alldo_sale set proj_import_status=TRUE where id = %d""" % self.env.context.get('proj_op_id'))
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
            print "%s" % nendrow
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.ensure_one()
        proj_rec = self.env['neweb.project'].search([('id', '=', self.env.context.get('proj_op_id'))])

        if not self.excel_file:
            raise UserError(u"沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)
        # nstartrow = 2
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

        if myamounttot == 0:
            raise UserError(u"匯入成本分析 Excel 總收入不能是 0 ")


        for row in range(nstartrow - 1, nendrow):
            cell = sheet.cell(row, 0)
            myprodset = False
            myprodsetid = False
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
               myprodset = u'' + str(cell.value).decode('utf-8')  # 產品組別
               myprodset1 = myprodset.replace(' ','').replace('/','').replace(' ','').upper()
               myprodsetrec = self.env['neweb.prodset'].search([('name1','=ilike',myprodset1)])
               if myprodsetrec:
                  for rec in myprodsetrec:
                      myprodsetid = rec.id

            cell = sheet.cell(row, 1)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mysaleitemitem = u'' + str(cell.value).decode('utf-8')  # 項次
            else:
                mysaleitemitem = ' '


            cell = sheet.cell(row, 2)
            myprodbrandid = False
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myprodbrand = u'' + str(cell.value).decode('utf-8')  # 品牌
                myprodbrandrec = self.env['neweb.prodbrand'].search([('name', '=ilike', myprodbrand)])
                if myprodbrandrec:
                    for rec in myprodbrandrec:
                        myprodbrandid = rec.id

            myprodmodeltype = ' '
            cell = sheet.cell(row, 3)  # 共契組別-項次
            try:
                if cell.ctype == XL_CELL_EMPTY:
                    cell = sheet.cell(row, 4)  # 機種/機型-料號
                    if cell.ctype == XL_CELL_EMPTY:
                        myprodmodeltype = '-'
                        # continue
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    myprodmodeltype = u'' + str(cell.value).decode('utf-8')  # 共契組別 & 機種-機型/料號
                    # myprodmodeltype = myprodmodeltype.replace("'","''")
            except Exception as inst:
                myprodmodeltype = '-'
            # if sheet.cell(row,3).ctype == XL_CELL_EMPTY and sheet.cell(row,4).ctype == XL_CELL_EMPTY :
            #     myprodmodeltype = '-'

            cell = sheet.cell(row, 5)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myprodserial = u'' + str(cell.value).decode('utf-8')  # 序號
                myprodserial = myprodserial.replace("'","''")
            else:
                myprodserial = False
                # print "3:%s" % mysitemdesc

            cell = sheet.cell(row, 6)
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    mymaindate = u'' + str(cell.value).decode('utf-8')  # 維護起迄日期
                    mymaindate = mymaindate.strip()
                    mymainstart = self.converdate(mymaindate[0:8])
                    mymainend = self.converdate(mymaindate[9:])
                else:
                    mymainstart = False
                    mymainend = False
            except Exception as inst:
                mymainstart = False
                mymainend = False


            cell = sheet.cell(row, 7)
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myproddesc = u'' + str(cell.value).decode('utf-8')  # 規格說明
                # myproddesc = myproddesc.replace("'","''")
            else:
                myproddesc = False
                # print "3:%s" % mysitemdesc


            cell = sheet.cell(row, 8)
            myprodnum = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                if cell.ctype == XL_CELL_NUMBER:
                    myprodnum = float(sheet.cell(row, 8).value)  # 數量

            # print "4:%s" % mysitemnum

            cell = sheet.cell(row, 9)
            myprodrevenue = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                if cell.ctype == XL_CELL_NUMBER:
                    myprodrevenue = float(sheet.cell(row, 9).value)  # 優惠銷價

            cell = sheet.cell(row, 11)
            myprodprice = 0
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                if cell.ctype == XL_CELL_NUMBER:
                    myprodprice = float(sheet.cell(row, 11).value)   # 成本單價


            cell = sheet.cell(row, 12)
            mysupplier = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mysuppliername = u'' + str(cell.value).decode('utf-8')  # 供應商
               mysupplierrec = self.env['res.partner'].search([('name','ilike',mysuppliername),('active','=',True),('supplier','=',True),('is_company','=',True)])
               if mysupplierrec:
                   for rec in mysupplierrec:
                       mysupplier = rec.id

            cell = sheet.cell(row, 13)
            mycosttypeid = False
            if cell.ctype == XL_CELL_EMPTY:
                mycosttypeid = 1
            else:
                mycosttype = u'' + str(cell.value).decode('utf-8')  # 成本類型
                mycosttyperec = self.env['neweb.costtype'].search([('name', '=ilike', mycosttype)])
                if mycosttyperec:
                    for rec in mycosttyperec:
                        mycosttypeid = rec.id
                        # mycosttypeid = mycosttyperec[0].id
                else:
                    mycosttypeid = 1

            # if  mymainstart != False:
            #     mycosttypeid = 4
            #     # continue



            if mymainstart == False or mymainstart== False :
                proj_rec.write({'saleitem_line': [(0, 0, {'prod_set':myprodsetid,'prod_brand':myprodbrandid,'prod_modeltype': myprodmodeltype, 'prod_serial': myprodserial,
                                                          'prod_desc': myproddesc,'prod_num': myprodnum, 'prod_price': myprodprice,'prod_revenue': myprodrevenue ,
                                                          'supplier':mysupplier,'cost_type':mycosttypeid,'saleitem_item':mysaleitemitem})]})
            else:
                proj_rec.write({'main_start_date':mymainstart,'main_end_date':mymainend,
                                'saleitem_line': [(0, 0, {'prod_set': myprodsetid, 'prod_brand': myprodbrandid,
                                                          'prod_modeltype': myprodmodeltype,
                                                          'prod_serial': myprodserial,
                                                          'prod_desc': myproddesc, 'prod_num': myprodnum,
                                                          'prod_price': myprodprice, 'prod_revenue': myprodrevenue,
                                                          'supplier': mysupplier, 'cost_type': mycosttypeid,
                                                          'saleitem_item': mysaleitemitem,
                                                          'neweb_start_date': mymainstart , 'neweb_end_date' : mymainend,})]})
            #self.env.cr.execute("select proj_drop_cost(%s,%s)" % (self.env.context.get('proj_op_id'),mycosttypeid))
        self.env.cr.execute("select proj_cal_cost(%d)" % self.env.context.get('proj_op_id'))
        self.env.cr.execute("""select proj_rcal_cost(%d)""" % self.env.context.get('proj_op_id'))
        self.env.cr.execute("""update alldo_sale set proj_import_status=FALSE where id = %d""" % self.env.context.get('proj_op_id'))
        self.env.cr.execute("""select get_discount_amount(%d)""" % self.env.context.get('proj_op_id'))
        mydiscountamount = self.env.cr.fetchone()
        self.env.cr.execute("select updatecalcost(%d)" % self.env.context.get('proj_op_id'))
        analysis_status = self.env.cr.fetchone()
        #print "%s" % analysis_status[0]
        # if not analysis_status[0]:
        #     raise Warning(u"成本分析收入金額總計不合,請確認！報價單優惠總價(未税):NT$ %s" % mydiscountamount[0])

        #self.env.cr.execute("select proj_adjust_cost(%s)" % self.env.context.get('proj_op_id'))

