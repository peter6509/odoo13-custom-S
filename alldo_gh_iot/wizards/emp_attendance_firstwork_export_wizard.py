# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class attendancefwexportwizard(models.TransientModel):
    _name = "alldo_gh_iot.attendance_fw_export_wizard"

    emp_no = fields.Many2one('hr.employee',string="員工")
    attendance_start = fields.Date(string="啟始時間",required=True)
    attendance_end = fields.Date(string="截止時間",required=True)


    def run_attendance_fw_export(self):
        emprec = self.env['hr.employee'].search([('active','=',True),('emp_code','not in',['JH001','JH002','JH003','JH006','admin'])])
        if not self.emp_no:
            self.env.cr.execute("""select genattendancefw1('%s','%s')""" % (self.attendance_start,self.attendance_end))
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select genattendancefw2(%d,'%s','%s')""" % (self.emp_no.id,self.attendance_start,self.attendance_end))
            self.env.cr.execute("""commit""")

        output = io.BytesIO()

        if not self.emp_no:
            myxlsfilename = "全體人員上班/首工件時間對照表_%s.xlsx" % datetime.now().strftime("%Y%m%d")
            mysubject = '全體人員上班/首工件時間對照表_%s.xlsx' %  datetime.now().strftime("%Y%m%d")
        else:
            myxlsfilename = "上班/首工件時間對照表_%s_%s.xlsx" % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
            mysubject = '上班/首工件時間對照表_%s_%s.xlsx' % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
            emprec = self.env['hr.employee'].search([('active', '=', True), ('id', '=', self.emp_no.id)])
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '精宏機械上班/首工件時間對照表',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'JH',
            'company': '精宏機械股份有限公司',
            'category': '上班/首工件時間對照表',
            'keywords': '上班/首工件時間對照表',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
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
        titles = [ '人員工號', '人員姓名', '上班刷卡時間', '首件生產時間', '首件工單', '生產機台']
        title_width = [15, 15, 25, 25, 20, 15]
        nnum = 1
        ws={}
        for rec in emprec:
            myattendrec = self.env['alldo_gh_iot.attendance_firstwork'].search([('emp_id','=',rec.id)],order="emp_id,attendance_cdate")
            ws[nnum] = wb.add_worksheet("%s" % rec.name)
            ########################################
            row = 0
            col = 0
            for title in titles:
                ws[nnum].write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws[nnum].set_row(row, 30)
                ws[nnum].set_column(myloc, title_width[col])
                col += 1
                ws[nnum].freeze_panes(row + 1, 0)
            row += 1
            nitem = 1
            myattsum = 0.00
            myattsum1 = 0.00
            for line in myattendrec:
                ws[nnum].write(row, 0, line.emp_id.emp_code if line.emp_id else ' ', okl_content_format)
                ws[nnum].write(row, 1, line.emp_id.name if line.emp_id else ' ', okl_content_format)
                ws[nnum].write(row, 2, line.attendance_cdate if line.attendance_cdate else ' ', okl_content_format)
                ws[nnum].write(row, 3, line.iot_cdatetime if line.iot_cdatetime else ' ', okl_content_format)
                ws[nnum].write(row, 4, line.iot_workorder.name if line.iot_workorder.name else ' ', okl_content_format)
                ws[nnum].write(row, 5, line.iot_id.equipment_no if line.iot_id.equipment_no else ' ', okc_content_format)
                row += 1
                nitem += 1
            nnum = nnum + 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_gh_iot.excel_download']

        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})

        myviewid = self.env.ref('alldo_gh_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'emp_attendance_list',
            'name': (u'上班/首工件時間對照表'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



