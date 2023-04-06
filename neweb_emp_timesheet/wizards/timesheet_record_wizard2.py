# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from io import BytesIO
import base64
from datetime import timedelta
from odoo.exceptions import UserError
import xlwt


class timesheetrecordwizard(models.TransientModel):
    _name = "neweb_emp_timesheet.timesheet_record_wizard"


    emp_id = fields.Many2one('hr.employee',string='工程師')
    dept_id = fields.Many2one('hr.department',string='部門')
    timesheet_start_date = fields.Date(string="檢核啟始日期",required=True)
    timesheet_end_date = fields.Date(string="檢核截止日期",required=True)
    emp_level = fields.Char(string='level')



    @api.onchange('timesheet_start_date')
    def onchangeclient1(self):
        res = {}
        if self.env.user.has_group('neweb_project.neweb_en10_gm') or self.env.user.has_group('neweb_project.neweb_en20_vp'):
            res['domain'] = {'emp_id': [(1,'=',1)]}
        elif self.env.user.has_group('neweb_project.neweb_en40_mgt') or self.env.user.has_group('neweb_project.neweb_en30_ass'):
            res['domain'] = {'emp_id': [('department_id', 'in', [x.department_id.id for x in self.env.user.employee_ids])]}
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
            res['domain'] = {'dept_id': [('id', 'in', [x.id for x in self.env.user.employee_ids.department_id])]}

        return res



    def run_timesheet_record(self):

        if not self.emp_id and not self.dept_id:
            raise UserError("工程師 or 部門 不可同時空值")
        mytype='0'
        if self.emp_id:
            mytype='1'
            mydomain = (('emp_id','=',self.emp_id.id),('timesheet_start_date','>=',self.timesheet_start_date),('timesheet_start_date','<=',self.timesheet_end_date))


        else:
            mytype='2'
            mydomain = (('emp_id.department_id', '=', self.dept_id.id),('timesheet_start_date', '>=', self.timesheet_start_date),('timesheet_start_date', '<=', self.timesheet_end_date))
        timesheet_rec = self.env['neweb_emp_timesheet.timesheet_calendar_line'].sudo().search(mydomain,order="emp_id,timesheet_start_date")
        # timesheet_rec=timesheet_rec.sorted(key=lambda R: (R.emp_id,R.timesheet_start_date))
            # print('DEPT:%d' % self.dept_id.id)


        user_tz = self.env.user.tz
        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40

        center_alignment = xlwt.Alignment()  # Create Alignment
        center_alignment.horz = xlwt.Alignment.HORZ_CENTER
        center_alignment.vert = xlwt.Alignment.VERT_CENTER

        title_font = xlwt.Font()  # Create the Font
        title_font.height = 0x00C8 * 2

        title_style = xlwt.XFStyle()  # Create Style
        title_style.borders = borders  # Add Borders to Style
        title_style.alignment = center_alignment
        title_style.font = title_font
        # myxlsfilename = rack.name +'.xls'

        wb = xlwt.Workbook(encoding='utf-8')
        ws1 = wb.add_sheet('工時系統申報記錄表')
        # ws2 = wb1.add_sheet('PC Survey Rating')

        content_font = xlwt.Font()
        content_font.height = 0x00C8 * 1
        content_style = xlwt.XFStyle()  # Create Style

        content_style.borders = borders  # Add Borders to Style

        content_alignment = xlwt.Alignment()  # Create Alignment
        content_alignment.horz = xlwt.Alignment.HORZ_LEFT
        content_alignment.vert = xlwt.Alignment.VERT_CENTER
        content_style.alignment = content_alignment
        content_style.alignment.wrap = 1
        content_style.font = content_font

        titles1 = ['項次','開始時間','結束時間','人員','工時數','工時代碼','客戶/供應商','單據號碼','業務員','工時說明','資料狀態']
        title_width = [1800,3600,3600,4800,1800,3600,7200,4800,4800,7200,3600]

        row = 0
        if mytype=='1':
            mytitle = "人員工時數據表 %s(%s - %s)" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
        else:
            mytitle = "部門工時數據表 %s(%s - %s)" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)
        ws1.write(row, 6, mytitle, title_style)
        row += 2
        col = 0
        for title in titles1:
            ws1.write(row, col, title, content_style)
            ws1.row(row).height = 1500
            ws1.col(col).width = title_width[col]
            col += 1

        if mytype=='1':
            myxlsfilename = "人員工時數據表 %s(%s - %s).xls" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
        else:
            myxlsfilename = "部門工時數據表 %s(%s - %s).xls" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)

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
            ws1.write(row, 0, nitem, content_style)
            ws1.write(row, 1, mystart, content_style)
            ws1.write(row, 2, myend, content_style)
            ws1.write(row, 3, (line.emp_id.name if line.emp_id else ' '), content_style)
            ws1.write(row, 4, (line.timesheet_duration if line.timesheet_duration > 0 else '0'), content_style)
            ws1.write(row, 5, myworktype, content_style)
            ws1.write(row, 6, (line.timesheet_custom.name if line.timesheet_custom else ' '), content_style)
            ws1.write(row, 7, (line.timesheet_origin if line.timesheet_origin else ' '), content_style)
            ws1.write(row, 8, (line.sale_id.name if line.sale_id else ' '), content_style)
            ws1.write(row, 9, (line.timesheet_desc if line.timesheet_desc else ' '), content_style)
            ws1.write(row, 10, mystatus, content_style)


            row += 1
            nitem += 1

        output = BytesIO()

        wb.save(output)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        myrec = self.env['neweb_emp_timesheet.timesheet_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid = self.env.ref('neweb_emp_timesheet.view_timesheet_download_tree')

        return {
            'view_name': 'timesheetnocompletewizard',
            'name': ('工時為達標EXCEL匯出:%s' % myxlsfilename),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_emp_timesheet.timesheet_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'self'}



