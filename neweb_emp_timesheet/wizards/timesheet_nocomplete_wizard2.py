# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
from io import BytesIO
import base64
from datetime import timedelta
from odoo.exceptions import UserError
import xlwt


class timesheetnocompletewizard(models.TransientModel):
    _name = "neweb_emp_timesheet.timesheet_nocomplete_wizard"


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



    def run_check_timesheet_complete(self):

        if not self.emp_id and not self.dept_id:
            raise UserError("工程師 or 部門 不可同時空值")
        mytype='0'
        if self.emp_id:
            mytype='1'
            self.env.cr.execute(" delete from neweb_emp_timesheet_timesheet_nocomplete")
            self.env.cr.execute("commit")
            self.env.cr.execute("select gen_nocompleteemp(%d,'%s','%s')" % (self.emp_id.id,self.timesheet_start_date,self.timesheet_end_date))
            self.env.cr.execute("commit")
        else:
            mytype='2'
            # print('DEPT:%d' % self.dept_id.id)
            self.env.cr.execute(" delete from neweb_emp_timesheet_timesheet_nocomplete")
            self.env.cr.execute("commit")
            self.env.cr.execute("select gen_nocompletedept(%d,'%s','%s')" % (self.dept_id.id,self.timesheet_start_date,self.timesheet_end_date))
            self.env.cr.execute("commit")


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
        ws1 = wb.add_sheet('工時系統未達標記錄')
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

        titles1 = ['日期','人員','部門','當日工時數','時數判定','資訊不足筆數']
        title_width = [3600,7200,3600,3600,7200,3600]

        row = 0
        if mytype=='1':
            mytitle = "人員工時檢核表 %s(%s - %s)" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
        else:
            mytitle = "部門工時檢核表 %s(%s - %s)" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)
        ws1.write(row, 3, mytitle, title_style)
        row += 2
        col = 0
        for title in titles1:
            ws1.write(row, col, title, content_style)
            ws1.row(row).height = 1500
            ws1.col(col).width = title_width[col]
            col += 1



        timesheet_rec = self.env['neweb_emp_timesheet.timesheet_nocomplete'].sudo().search([])
        timesheet_rec.sorted(key=lambda R:(R.id))
        if mytype=='1':
            myxlsfilename = "人員工時檢核表 %s(%s - %s).xls" % (self.emp_id.name, self.timesheet_start_date,self.timesheet_end_date)
        else:
            myxlsfilename = "部門工時檢核表 %s(%s - %s).xls" % (self.dept_id.name, self.timesheet_start_date, self.timesheet_end_date)

        row += 1
        myn = 0
        for line in timesheet_rec:
            ws1.write(row, 0, (line.timesheet_date if line.timesheet_date else ' '), content_style)
            ws1.write(row, 1, (line.emp_id.name if line.emp_id else ' '), content_style)
            ws1.write(row, 2, (line.dept_id.name if line.dept_id else ' '), content_style)
            ws1.write(row, 3, (line.timesheet_hours if line.timesheet_hours else '0'), content_style)
            ws1.write(row, 4, ('工時數不足' if line.no_complete else ' '), content_style)
            ws1.write(row, 5, (line.illegal_num if line.illegal_num > 0 else ' '), content_style)
            row += 1

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



