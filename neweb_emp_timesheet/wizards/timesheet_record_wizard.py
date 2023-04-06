# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter


class timesheetrecordwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.timesheet_record_wizard"


    emp_id = fields.Many2one('hr.employee',string='工程師')
    dept_id = fields.Many2one('hr.department',string='部門')
    timesheet_start_date = fields.Date(string="檢核啟始日期",required=True)
    timesheet_end_date = fields.Date(string="檢核截止日期",required=True)
    emp_level = fields.Char(string='level')
    alldept = fields.Boolean(string="全體部門",default=False)



    @api.onchange('timesheet_start_date')
    def onchangeclient1(self):
        res = {}
        if self.env.user.has_group('neweb_project.neweb_en10_gm') or self.env.user.has_group('neweb_project.neweb_en20_vp'):
            res['domain'] = {'emp_id': [(1,'=',1)]}
        elif self.env.user.has_group('neweb_project.neweb_en40_mgt') or self.env.user.has_group('neweb_project.neweb_en30_ass'):
            mylist = []
            myrec = self.env['hr.department'].search(['|', ('manager_id', '=', self.env.user.employee_ids.id),
                                                      ('id', '=', self.env.user.employee_ids.department_id.id)])
            for rec in myrec:
                mylist.append(rec.id)
            res['domain'] = {'emp_id': [('department_id', 'in', mylist)]}
            #res['domain'] = {'emp_id': [('department_id', 'in', [x.department_id.id for x in self.env.user.employee_ids])]}
        elif self.env.user.has_group('neweb_project.neweb_en70_user'):
            #print("en70")
            res['domain'] = {'emp_id': [('id','in',[x.id for x in self.env.user.employee_ids])]}


        return res

    @api.onchange('timesheet_end_date')
    def onchangeclient2(self):
        if  self.env.user.has_group('neweb_project.neweb_en10_gm') :
            self.update({'emp_level':'en10'})
        elif self.env.user.has_group('neweb_project.neweb_en20_vp') :
            self.update({'emp_level': 'en20'})
        elif self.env.user.has_group('neweb_project.neweb_en30_ass') :
            self.update({'emp_level': 'en30'})
        elif self.env.user.has_group('neweb_project.neweb_en40_mgt') :
            self.update({'emp_level': 'en40'})
        else :
            self.update({'emp_level': 'en70'})

        # print "%s" % self.emp_level
        res = {}
        if self.env.user.has_group('neweb_project.neweb_en40_mgt'):
            res['domain'] = {'dept_id': ['|',('id', 'in', [x.id for x in self.env.user.employee_ids.department_id]),('manager_id','=',self.env.user.employee_ids.id)]}

        return res



    def run_timesheet_record(self):

        if not self.emp_id and not self.dept_id and not self.alldept:
            raise UserError("工程師 or 部門 不可同時空值")
        mytype='0'
        if self.alldept:
            mytype = '0'
            mydomain = (('timesheet_start_date', '>=', self.timesheet_start_date),('timesheet_start_date', '<=', self.timesheet_end_date))

        elif self.emp_id:
            mytype='1'
            mydomain = (('emp_id','=',self.emp_id.id),('timesheet_start_date','>=',self.timesheet_start_date),('timesheet_start_date','<=',self.timesheet_end_date))
        else:
            mytype='2'
            mydomain = (('emp_id.department_id', '=', self.dept_id.id),('timesheet_start_date', '>=', self.timesheet_start_date),('timesheet_start_date', '<=', self.timesheet_end_date))
        timesheet_rec = self.env['neweb_emp_timesheet.timesheet_calendar_line'].sudo().search(mydomain,order="emp_id,timesheet_start_date")
        # timesheet_rec=timesheet_rec.sorted(key=lambda R: (R.emp_id,R.timesheet_start_date))
            # print('DEPT:%d' % self.dept_id.id)

        output = io.BytesIO()
        if mytype=='1':
            myxlsfilename1 = "人員工時數據表 %s(%s - %s).xlsx" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
            mysubject = '%s(%s to %s)人員工時數據表' % (self.emp_id.name, self.timesheet_start_date, self.timesheet_end_date)
        elif mytype=='2':
            myxlsfilename1 = "部門工時數據表 %s(%s - %s).xlsx" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)
            mysubject = '%s(%s to %s)部門工時數據表' % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)
        else:
            myxlsfilename1 = "全體部門工時數據表 (%s - %s).xlsx" % (self.timesheet_start_date, self.timesheet_end_date)
            mysubject = '(%s to %s)部門工時數據表' % (self.timesheet_start_date, self.timesheet_end_date)



        wb2 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb2.set_properties({
            'title': '工時數據報告',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '工時報工',
            'keywords': '工時數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws2 = wb2.add_worksheet("工時系統申報記錄表")

        ########################################
        title_format = wb2.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb2.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb2.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb2.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb2.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb2.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################
        date_format = wb2.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(15)
        date_format.set_border(1)
        date_format.set_font_color('black')
        date_format.set_align('right')
        date_format.set_align('vcenter')
        date_format.set_text_wrap()


        titles1 = ['項次','開始時間','結束時間','人員','工時數','工時代碼','客戶/供應商','單據號碼','業務員','工時說明','資料狀態']
        title_width = [15,30,30,30,15,30,60,30,30,60,30]

        row = 0
        if mytype=='1':
            mytitle = "人員工時數據表 %s(%s - %s)" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
        elif mytype=='2':
            mytitle = "部門工時數據表 %s(%s - %s)" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)
        else:
            mytitle = "全體部門工時數據表 (%s - %s)" % (self.timesheet_start_date, self.timesheet_end_date)
        ws2.write(row, 4, mytitle, title_format)
        row += 2
        col = 0
        for title in titles1:
            ws2.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws2.set_row(row, 30)
            ws2.set_column(myloc, title_width[col])
            col += 1

        ws2.freeze_panes(row+1, 0)
        row += 1
        nitem = 1
        for line in timesheet_rec:
            mystartdate = fields.Datetime.from_string(line.timesheet_start_date)
            if mystartdate:
                mystart = (mystartdate + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
            else:
                mystart = ' '
            myenddate = fields.Datetime.from_string(line.timesheet_end_date)
            if myenddate:
                myend = (myenddate + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
            else:
                myend = ' '
            if line.is_complete=='ok':
                mystatus = 'OK'
            else:
                mystatus = 'NG'
            if line.timesheet_worktype:
                myworktype = "[%s]%s" % (line.timesheet_worktype.worktype_code,line.timesheet_worktype.worktype_desc)
            else:
                myworktype = ' '
            if mystatus=='OK':
                ws2.write(row, 0, nitem, okc_content_format)
                ws2.write(row, 1, mystart, date_format)
                ws2.write(row, 2, myend, date_format)
                ws2.write(row, 3, (line.emp_id.name if line.emp_id else ' '), okc_content_format)
                ws2.write(row, 4, (round(line.timesheet_duration,2) if line.timesheet_duration > 0 else '0'), okc_content_format)
                ws2.write(row, 5, myworktype, okl_content_format)
                ws2.write(row, 6, (line.timesheet_custom.name if line.timesheet_custom else ' '), okl_content_format)
                ws2.write(row, 7, (line.timesheet_origin if line.timesheet_origin else ' '), okl_content_format)
                ws2.write(row, 8, (line.sale_id.name if line.sale_id else ' '), okl_content_format)
                ws2.write(row, 9, (line.timesheet_desc if line.timesheet_desc else ' '), okl_content_format)
                ws2.write(row, 10, mystatus, okc_content_format)
            else:
                ws2.write(row, 0, nitem, ngc_content_format)
                ws2.write(row, 1, mystart, date_format)
                ws2.write(row, 2, myend, date_format)
                ws2.write(row, 3, (line.emp_id.name if line.emp_id else ' '), ngc_content_format)
                ws2.write(row, 4, (round(line.timesheet_duration,2) if line.timesheet_duration > 0 else '0'), ngc_content_format)
                ws2.write(row, 5, myworktype, ngl_content_format)
                ws2.write(row, 6, (line.timesheet_custom.name if line.timesheet_custom else ' '), ngl_content_format)
                ws2.write(row, 7, (line.timesheet_origin if line.timesheet_origin else ' '), ngl_content_format)
                ws2.write(row, 8, (line.sale_id.name if line.sale_id else ' '), ngl_content_format)
                ws2.write(row, 9, (line.timesheet_desc if line.timesheet_desc else ' '), ngl_content_format)
                ws2.write(row, 10, mystatus, ngc_content_format)

            row += 1
            nitem += 1

        wb2.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['neweb_emp_timesheet.timesheet_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename1})
        myviewid = self.env.ref('neweb_emp_timesheet.view_timesheet_download_tree')

        return {
            'view_name': 'timesheetnocompletewizard',
            'name': ('工時為達標EXCEL匯出:%s' % myxlsfilename1),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_emp_timesheet.timesheet_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'self'}



