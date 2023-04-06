# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter
import json,logging,re
from lxml import etree

class newebsecurityexportwizard(models.TransientModel):
    _name = "neweb_enhancement.security_export_wizard"

    desc = fields.Char(string="匯出說明",required=True)


    def security_expand(self):
        output = io.BytesIO()
        myxlsfilename = "SECURITY_%s_%s.xlsx" % (self.desc, datetime.now().strftime("%Y%m%d"))
        mysubject = "SECURITY_%s_%s.xlsx" % (self.desc, datetime.now().strftime("%Y%m%d"))
        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': 'NEWEB人員Odoo系統權限一覽表',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': 'NEWEB人員Odoo系統權限一覽表',
            'keywords': 'NEWEB人員Odoo系統權限一覽表',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("NEWEB人員Odoo系統權限一覽表")
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

        titles1 = ['姓名', '帳號', '作業組別','權限']
        title_width = [40, 60,60,40]
        self.env.cr.execute("""select gen_security_category()""")
        self.env.cr.execute("""select category_name,group_name,emp_name,login,seq from neweb_enhancement_security_group order by emp_name""")
        security_category = self.env.cr.fetchall()

        row = 0

        col = 0
        for title in titles1:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        coln = 2
        # if myrange
        cempname=' '
        clogin=' '
        for line in security_category:
            s1 = line[0]   # category_name
            s2 = line[1]   # group_name
            s3 = line[2]   # emp_name
            s4 = line[3]   # login
            s5 = line[4]   # seq
            if s3 == cempname:
               s3=' '
            else:
               cempname=s3
            if s4 == clogin:
               s4 = ' '
            else:
               clogin = s4

            if clogin != 'admin' or clogin != 'timesheet_report':
                ws.write(row, 0, s3 if s3 else ' ', okl_content_format)
                ws.write(row, 1, s4 if s4 else ' ', okl_content_format)
                ws.write(row, 2, s1 if s1 else ' ', okl_content_format)
                ws.write(row, 3, s2 if s2 else ' ', okl_content_format)


                row += 1
                nitem += 1




        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        # self.state = '2'
        mydate = datetime.now()

        myxlsfilename = _("NEWEB Odoo 使用者權限表-%s-%s.xls" % (self.desc, mydate))

        myrec = self.env['neweb_enhancement.security_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid = self.env.ref('neweb_enhancement.security_excel_download_view_tree')

        return {
            'view_name': 'Security_enhancement',
            'name': ('Odoo權限表'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_enhancement.security_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}






        # wb.close()
        # output.seek(0)
        # myxlsfile = base64.standard_b64encode(output.getvalue())
        # output.close()
        #
        # myrec = self.env['neweb.export_excel_download']
        # myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        #
        # myviewid = self.env.ref('neweb_projext.partner_export_download_tree')
        #
        # return {
        #     'view_name': 'newebpartnerexportdownload',
        #     'name': ('客戶資訊EXCEL匯出'),
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'neweb.export_excel_download',
        #     'view_id': myviewid.id,
        #     'flags': {'action_buttons': True},
        #     'view_type': 'form',
        #     'view_mode': 'tree',
        #     'target': 'main'}
        #
        #
        #
        #
        #
        #
        # import xlwt
        # borders = xlwt.Borders()  # Create Borders
        # borders.left = xlwt.Borders.THIN  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        # borders.right = xlwt.Borders.THIN
        # borders.top = xlwt.Borders.THIN
        # borders.bottom = xlwt.Borders.THIN
        # borders.left_colour = 0x40
        # borders.right_colour = 0x40
        # borders.top_colour = 0x40
        # borders.bottom_colour = 0x40
        #
        # center_alignment = xlwt.Alignment()  # Create Alignment
        # center_alignment.horz = xlwt.Alignment.HORZ_CENTER
        # center_alignment.vert = xlwt.Alignment.VERT_CENTER
        #
        # title_font = xlwt.Font()  # Create the Font
        # title_font.height = 0x00C8 * 2
        #
        # title_style = xlwt.XFStyle()  # Create Style
        # title_style.borders = borders  # Add Borders to Style
        # title_style.alignment = center_alignment
        # title_style.font = title_font
        #
        # wb = xlwt.Workbook(encoding='utf-8')
        # ws = wb.add_sheet('NEWEB人員Odoo系統權限表')
        #
        # ws.write_merge(0, 2, 0, 13, "NEWEB人員Odoo系統權限一覽表", title_style)
        #
        # content_font = xlwt.Font()
        # content_font.height = 0x00C8 * 1
        # content_style = xlwt.XFStyle()  # Create Style
        #
        # # content_style.borders = borders  # Add Borders to Style
        #
        # content_alignment = xlwt.Alignment()  # Create Alignment
        # content_alignment.horz = xlwt.Alignment.HORZ_CENTER
        # content_alignment.vert = xlwt.Alignment.VERT_CENTER
        # content_style.alignment = content_alignment
        # content_style.alignment.wrap = 1
        # content_style.font = content_font
        #
        # content1_font = xlwt.Font()
        # content1_font.height = 0x00C8 * 1
        # content1_style = xlwt.XFStyle()  # Create Style
        #
        # content1_style.borders = borders  # Add Borders to Style
        #
        # content1_alignment = xlwt.Alignment()  # Create Alignment
        # content1_alignment.horz = xlwt.Alignment.HORZ_CENTER
        # content1_alignment.vert = xlwt.Alignment.VERT_CENTER
        # content1_style.alignment = content_alignment
        # content1_style.alignment.wrap = 1
        # content1_style.font = content1_font
        #
        # row = 3
        # self.env.cr.execute("""select gen_security_category()""")
        # self.env.cr.execute("""select category_name,group_name,seq from neweb_enhancement_security_category order by seq""")
        # security_category = self.env.cr.fetchall()
        # row += 1
        # ws.write(row, 0, "姓名", content1_style)
        # ws.write(row, 1, "帳號", content1_style)
        # ws.col(1).width = 7200
        # ws.col(0).width = 3600
        # ws.row(row).height = 700
        # coln = 2
        # # if myrange
        # for line in security_category:
        #     s1=line[0]
        #     s2=line[1]
        #     title = "("+ s1 + ")" + s2
        #     ws.write(row, coln, title, content1_style)
        #     ws.col(coln).width = 3600
        #     ws.row(row).height = 700
        #     coln += 1
        #
        #
        #
        # self.env.cr.execute("""select login,emp_name,seq,user_id from neweb_enhancement_security_group order by user_id,group_id""")
        # security_group = self.env.cr.fetchall()
        # myuserid=0
        # for line in security_group:
        #     s1=line[0]
        #     s2=line[1]
        #     s3=line[2]
        #     s4=line[3]
        #     if myuserid != s4 :
        #         row += 1
        #         ws.write(row, 0, s2, content_style)
        #         ws.write(row, 1, s1, content_style)
        #         myuserid = s4
        #
        #     ws.write(row, s3+1, "Y", content_style)
        #     ws.row(row).height = 700
        #
        #
        # output = StringIO.StringIO()
        # wb.save(output)
        # myxlsfile = base64.standard_b64encode(output.getvalue())
        # # self.state = '2'
        # mydate = datetime.datetime.now()
        #
        #
        # myxlsfilename = _("NEWEB Odoo 使用者權限表-%s-%s.xls" % (self.desc,mydate))
        #
        # myrec = self.env['neweb_enhancement.security_download']
        # myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        # myviewid = self.env.ref('neweb_enhancement.security_excel_download_view_tree')
        #
        # return {
        #     'view_name': 'Security_enhancement',
        #     'name': ('Odoo權限表'),
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'neweb_enhancement.security_download',
        #     'view_id': myviewid.id,
        #     'flags': {'action_buttons': False},
        #     'view_type': 'form',
        #     'view_mode': 'tree',
        #     'target': 'main'}