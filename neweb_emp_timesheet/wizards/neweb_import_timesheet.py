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



class newebimporttimesheetwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.import_timesheet"

    emp_id = fields.Many2one('hr.employee',string="工程師",default=lambda self:self._getemp())
    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)


    def _getemp(self):
        myemp = self.env['hr.employee'].search([('user_id','=', self.env.uid)])
        return myemp.id

    def action_import(self):

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodebytes(self.excel_file))
        sheet = xls.sheet_by_index(0)

        nstartrow = 2
        nendrow = sheet.nrows

        print ("NEDROW:%s" % nendrow)
        print ("EMPID:%s" % self.emp_id.id)

        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        self.ensure_one()

        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        # xls = xlrd.open_workbook(file_contents=base64.decodestring(self.excel_file))
        # sheet = xls.sheet_by_index(0)
        # myworkdate1 = ''
        for row in range(nstartrow - 1, nendrow - 1):
            cell = sheet.cell(row, 0)  # 工程師代號

            myempno = ' '

            if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                myempno = '' + str(cell.value).strip().encode().decode('utf-8')  # 工程師代號
                myempno = myempno[:3]
            else:
                myempno= ' '

            print("工程師:%s" % myempno)


            cell = sheet.cell(row, 1)     # 工作日期

            myworkdate = ' '
            myworkdate1 = cell.value
            myworkdate = datetime.datetime(*xlrd.xldate_as_tuple(myworkdate1, xls.datemode))
            # if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
            #     #myworkdate = '' + str(cell.value).strip().encode().decode('utf-8')[0:10]  # 工作日期
            #     myworkdate = cell.value
            # else:
            #     myworkdate = ' '

            print ("工作日期:%s" % myworkdate)

            cell = sheet.cell(row, 2)   # 起始時間
            mystarttime = ' '
            mystarttime1 = cell.value
            mystarttime1 = mystarttime1 * 24

            #mystarttime = datetime.datetime(*xlrd.xldate_as_tuple(mystarttime1, xls.timemode))
            # if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER) :
            #     #mystarttime = '' + str(cell.value).strip().encode().decode('utf-8')[0:5]+':00'  # 起始時間
            #     mystarttime = cell.value
            # else:
            #     mystarttime = ' '

            print ("起始時間：%s" % mystarttime1)

            cell = sheet.cell(row, 3)  # 結束時間
            myendtime = ' '
            myendtime1 = cell.value
            myendtime1 = myendtime1 * 24
            #myendtime = datetime.datetime(*xlrd.xldate_as_tuple(myendtime1, xls.datemode))
            # try:
            #     myendtime = cell.value
            #     # if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER) :
            #     #     #myendtime = '' + str(cell.value).strip().encode().decode('utf-8')[0:5]+':00'  # 結束時間
            #     #     myendtime = cell.value
            #     # else:
            #     #     myendtime = ' '
            # except Exception as inst:
            #     myendtime = ' '

            print ("結束時間：%s" % myendtime1)
            cell = sheet.cell(row, 4)  # 工時代碼
            myworktype = ' '
            try:
                if cell.ctype in (XL_CELL_TEXT , XL_CELL_NUMBER) :
                    myworktype = '' + str(cell.value).strip().encode().decode('utf-8')[0:2]  # 工時代碼
                else:
                    myworktype = ' '
            except Exception as inst:
                myworktype = ' '
            print ("工作代碼：%s" % myworktype)
            cell = sheet.cell(row, 5)  # 單據編號
            myorigin = ' '
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER) :
                    myorigin = '' + str(cell.value).strip().encode().decode('utf-8')  # 單據編號
                else:
                    myorigin = ' '
            except Exception as inst:
                myorigin = ' '
            print ("單據編號:%s" % myorigin)
            cell = sheet.cell(row, 6)  # 描述說明
            mymemo = ' '
            try:
                if cell.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER) :
                    mymemo = '' + str(cell.value).strip().encode().decode('utf-8')  # MEMO
                else:
                    mymemo = ' '
            except Exception as inst:
                mymemo = ' '

            cell = sheet.cell(row, 7)  # 連續天數
            mydays = 0
            try:
                mydays = int(cell.value)  # days
            except Exception as inst:
                mydays = 0

            print ("MYDAYS:%s" % mydays)
            myworkdate1 = ""

            if mydays > 0 and (myworktype[0:1] == '5' or myworktype[0:1] == '4'):

                self.env.cr.execute("""select import_timesheet_set1('%s','%s','%s','%s','%s','%s','%s',%d)""" %
                                    (myempno, myworkdate, mystarttime1, myendtime1, myworktype, myorigin,
                                     mymemo,mydays))
                self.env.cr.execute("""commit ;""")
                    # myworkdate1 = myworkdate[0:7]
                # except Exception as inst:
                #     print ("No Excel Data import")
            else:
                # try:
                self.env.cr.execute("""select import_timesheet_set('%s','%s','%s','%s','%s','%s','%s')""" %
                                    (myempno, myworkdate, mystarttime1, myendtime1, myworktype, myorigin, mymemo))
                self.env.cr.execute("""commit ;""")
                #     # myworkdate1 = myworkdate[0:7]
                # except Exception as inst:
                #     print ("No Excel Data import")


        self.env.cr.commit()
        # self.env.cr.execute("""select gentimesheetnitem()""")
        # self.env.cr.execute("""commit ;""")
        view = self.env.ref('sh_message.sh_message_wizard')
        context = dict(self._context or {})
        context['message']='完成'
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
        # try:
        #     self.env.cr.execute("""select getmaxthcalym(%d)""" % self.emp_id.id)
        #     myworkdate1 = self.env.cr.fetchone()[0]
        #     print ("workdate:%s" % myworkdate1)
        #     self.env.cr.execute("""select sorttimesheetitem1(%d,'%s')""" % (self.emp_id.id, myworkdate1))
        #     self.env.cr.execute("""commit""")
        # except Exception as inst:
        #     print ("No Excel Data Sort")
        #
        # myrec = self.env['neweb_emp_timesheet.timesheet_calendar'].search([('timesheet_yearmonth','=',myworkdate1),('emp_id','=',self.emp_id.id)])
        # # mydomain = []
        # # mydomain.append(('id', '=', myactive_id.id))
        # return {'view_name': 'newebprojwizard',
        #         'name': ('專案維護'),
        #         'views': [[False, 'form'], ],
        #         'res_model': 'neweb_emp_timesheet.timesheet_calendar',
        #         'context': self._context,
        #         'type': 'ir.actions.act_window',
        #         'target': 'main',
        #         # 'domain': mydomain,
        #         'res_id': myrec.id,
        #         'flags': {'action_buttons': True},
        #         'view_mode': 'form',
        #         'view_type': 'form'
        #         }




