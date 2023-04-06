# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class empattendanceexportwizard(models.TransientModel):
    _name = "alldo_ipla_iot.emp_attendance_export_wizard"
    _description = "人員出勤記錄匯出EXCEL"

    emp_no = fields.Many2one('hr.employee',string="員工")
    attendance_start = fields.Date(string="啟始時間",required=True)
    attendance_end = fields.Date(string="截止時間",required=True)
    run_desc = fields.Char(string="匯出說明",required=True)

    def run_attendance_export(self):
        if not self.emp_no:
            self.env.cr.execute("""select genattendance1('%s','%s')""" % (self.attendance_start,self.attendance_end))
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select genattendance2(%d,'%s','%s')""" % (self.emp_no.id,self.attendance_start,self.attendance_end))
            self.env.cr.execute("""commit""")
        myattendrec =  self.env['alldo_ipla_iot.emp_attendance_list'].search([])
        mycount = self.env['alldo_ipla_iot.emp_attendance_list'].search_count([])
        output = io.BytesIO()

        if not self.emp_no:
            myxlsfilename = "全體人員出勤記錄_%s.xlsx" % datetime.now().strftime("%Y%m%d")
            mysubject = '全體人員出勤記錄_%s.xlsx' %  datetime.now().strftime("%Y%m%d")
        else:
            myxlsfilename = "人員出勤記錄_%s_%s.xlsx" % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
            mysubject = '人員出勤記錄_%s_%s.xlsx' % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '正璽金屬工業人員出勤記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': '正璽金屬工業',
            'company': '正璽金屬工業有限公司',
            'category': '人員出勤',
            'keywords': '人員出勤',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("正璽金屬工業人員出勤記錄")
        ########################################
        title_format = wb.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################

        okl_content_format = wb.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()

        #########################################
        ngc_content_format = wb.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################
        currency_format = wb.add_format({'num_format': '###,###,##0.00'})
        currency_format.set_font_size(15)
        currency_format.set_border(1)
        currency_format.set_font_color('black')
        currency_format.set_align('right')
        currency_format.set_align('vcenter')
        currency_format.set_text_wrap()


        titles = ['刷卡日期','人員工號', '人員姓名', '上班時間' , '下班時間' , '上班時數(HR)']
        title_width = [40, 40, 40,40, 40, 40 ]

        row = 0

        col = 0
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1
        myattsum = 0.00
        for line in myattendrec:
            myattsum = myattsum + round(line.att_duration,2)
            ws.write(row, 0, line.attend_date1 if line.attend_date1 else ' ', okl_content_format)
            ws.write(row, 1, line.emp_no.emp_code if line.emp_no else ' ', okl_content_format)
            ws.write(row, 2, line.emp_no.name if line.emp_no else ' ', okl_content_format)
            ws.write(row, 3, line.attendance_start if line.attendance_start else ' ', okl_content_format)
            ws.write(row, 4, line.attendance_end if line.attendance_end else ' ', okl_content_format)
            ws.write(row, 5, line.att_duration if line.att_duration else '0', okc_content_format)
            row += 1
            nitem += 1
        ws.write(row, 4, '時數合計：', okc_content_format)
        ws.write(row, 5, myattsum, okc_content_format)
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_ipla_iot.excel_download']
        if mycount > 0:
            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename,'run_desc':self.run_desc})
        else:
            raise UserError("沒有出勤記錄可供匯出！")

        myviewid = self.env.ref('alldo_ipla_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'emp_attendance_list',
            'name': (u'人員出勤記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



