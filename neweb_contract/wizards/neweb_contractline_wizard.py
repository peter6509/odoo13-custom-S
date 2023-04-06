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


class contractlinewizard(models.TransientModel):
    _name = "neweb_contract.contractline_wizard"

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
    start_row = fields.Integer(size=3, string="啟始ROW", default=3)
    end_row = fields.Integer(size=3, string="結止ROW", default=3)


    def contractline_action_import(self):
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
        contract_rec = self.env['neweb_contract.contract'].search([('id', '=', self.env.context.get('contract_id'))])
        #print "%s" % contract_rec.id
        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        sheet = xls.sheet_by_index(0)

        for row in range(nstartrow -1, nendrow):

            cell = sheet.cell(row, 0)
            mybrand = False
            myprodbrand = False
            if cell.ctype == XL_CELL_EMPTY:
                continue
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mybrand = '' + str(cell.value)  # 品牌
                myrec = self.env['neweb.prodbrand'].search([('name','=',mybrand)])
                if myrec:
                    myprodbrand = myrec.id
                # print myprodmodeltype
            # print "1:%s" % mysitemmodeltype

            cell = sheet.cell(row, 1)
            myprodmodeltype = False
            if cell.ctype == XL_CELL_EMPTY :
               continue
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodmodeltype = '' + str(cell.value)  # 機種-機型/料號
               #print myprodmodeltype
            # print "1:%s" % mysitemmodeltype

            cell = sheet.cell(row, 2)
            mymachineserialno = False
            if cell.ctype == XL_CELL_EMPTY :
               continue
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mymachineserialno = '' + str(cell.value)  # 序號
               #print mymachineserialno

            cell = sheet.cell(row, 3)
            myprodsla = False
            myprodlinesla = contract_rec.sla.id
            if cell.ctype == XL_CELL_EMPTY :
                myprodlinesla = contract_rec.sla.id
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myprodsla = '' + str(cell.value)  # SLA
               myrec = self.env['neweb_base.sla'].search([('name','=',myprodsla),('disabled','=',False)])
               if myrec:
                  myprodlinesla = myrec.id

            cell = sheet.cell(row, 4)
            mycontractstartdate = False
            if cell.ctype == XL_CELL_EMPTY :
               continue
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycontractstartdate = datetime.datetime.strptime(str(cell.value),'%Y%m%d') # 合約啟始日
               #print mycontractstartdate


            cell = sheet.cell(row, 5)
            mycontractenddate = False
            if cell.ctype == XL_CELL_EMPTY :
               continue
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mycontractenddate = datetime.datetime.strptime(str(cell.value),'%Y%m%d')  # 合約截止日
               #print mycontractenddate


            cell = sheet.cell(row, 6)
            mypartnerid = False
            if cell.ctype == XL_CELL_EMPTY:
               mypartnerid = ''
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               mypartnername = ''+str(cell.value)         # 維護廠商
               myrec = self.env['res.partner'].search([('name','ilike',mypartnername),('is_company','=',True),('supplier_rank','=',1)])
               if myrec:
                  mypartnerid = myrec[0].id
               else:
                  mypartnerid = ''
            #print "partnerid:%s" % mypartnerid

            cell = sheet.cell(row, 7)
            mymemo = False
            if cell.ctype == XL_CELL_EMPTY:
                mymemo = '-'
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mymemo = ''+str(cell.value)          # 說明

            cell = sheet.cell(row, 8)
            myos = False
            if cell.ctype == XL_CELL_EMPTY:
               myos = '-'
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
               myos = ''+str(cell.value)              # 作業系統

            cell = sheet.cell(row, 9)
            myhasos = False
            if cell.ctype == XL_CELL_EMPTY :
               myhasos = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                myoshascontract = ''+str(cell.value)     # 作業系統有簽約?
                if myoshascontract == 'Y':
                   myhasos = True
                else:
                   myhasos = False

            cell = sheet.cell(row, 10)
            myfirmware = False
            if cell.ctype == XL_CELL_EMPTY:
                myfirmware = '-'
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myfirmware = ''+str(cell.value)        # firmware

            cell = sheet.cell(row, 11)
            mydb = False
            if cell.ctype == XL_CELL_EMPTY :
                mydb = '-'
            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                mydb = ''+str(cell.value)           # DB version

            cell = sheet.cell(row, 12)
            myhasdb = False
            if cell.ctype == XL_CELL_EMPTY :
                myhasdb = False
            if cell.ctype in (XL_CELL_TEXT,XL_CELL_NUMBER):
                mydbhascontract = ''+str(cell.value)  # DB有簽約?
                if mydbhascontract == 'Y':
                    myhasdb = True
                else:
                    myhasdb = False

            if mypartnerid != '':
               # self.env.cr.execute("""insert into neweb_contract_contract_line(contract_id,prod_modeltype,machine_serial_no,prod_sla,contract_start_date,contract_end_date,
               #                     maintain_partner,memo,prod_line_os,os_has_contract,prod_line_firmware,prod_line_db,db_has_contract) values
               #                     (%d,'%s','%s',%d,%s,%s,%d,'%s','%s',%s,'%s','%s',%s)""" % (contract_rec.id,myprodmodeltype,mymachineserialno,myprodsla,mycontractstartdate,
               #                      mycontractenddate,mypartnerid,mymemo,myos,myhasos,myfirmware,mydb,myhasdb))
               contract_rec.write({'contract_line_ids': [(0, 0, {'prod_modeltype': myprodmodeltype ,'machine_serial_no': mymachineserialno,
                           'prod_sla': myprodlinesla, 'contract_start_date': mycontractstartdate,'contract_end_date':mycontractenddate ,
                           'maintain_partner': mypartnerid, 'memo': mymemo,'prod_line_os':myos,'os_has_contract':myhasos,'prod_line_firmware':myfirmware,
                            'prod_line_db':mydb,'db_has_contract':myhasdb,'prod_brand':myprodbrand})]})

            if mypartnerid == '':
                contract_rec.write({'contract_line_ids': [(0, 0, {'prod_modeltype': myprodmodeltype, 'machine_serial_no': mymachineserialno,
                            'prod_sla': myprodlinesla, 'contract_start_date': mycontractstartdate,
                            'contract_end_date': mycontractenddate,
                            'memo': mymemo, 'prod_line_os': myos,
                            'os_has_contract': myhasos, 'prod_line_firmware': myfirmware,
                            'prod_line_db': mydb, 'db_has_contract': myhasdb,'prod_brand':myprodbrand})]})
