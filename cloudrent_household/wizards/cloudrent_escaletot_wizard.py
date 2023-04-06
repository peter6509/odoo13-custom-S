# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime, pytz
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class cloudrentEscaletotWizard(models.TransientModel):
    _name = "cloudrent.escaletot_wizard"

    start_date = fields.Date(string="啟始日",required=True)
    end_date = fields.Date(string="截止日",required=True)
    project_no = fields.Many2one('cloudrent.household_house',string="案名",required=True)

    def run_scaletot(self):
        self.env.cr.execute("""select genescaletot(%d,'%s','%s')""" % (self.project_no,self.start_date,self.end_date))
        self.env.cr.execute("""commit""")
        scale_rec = self.env['cloudrent.escaletot_line'].search([])
        self.env.cr.execute("""select sum(duration_scale) from cloudrent_escaletot_line""")
        mytotscale = self.env.cr.fetchone()[0]
        output = io.BytesIO()
        myxlsfilename = "CloudRent案場區間用電數報表(%s ~ %s).xlsx" % (self.start_date,self.end_date)
        mysubject = 'CloudRent案場區間用電數報表(%s ~ %s).xlsx' % (self.start_date,self.end_date)
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': 'CloudRent案場區間用電數報表',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'cloudrent',
            'company': 'cloudrent',
            'category': '統計報表',
            'keywords': '統計報表',
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
        okr_content_format = wb.add_format()
        okr_content_format.set_font_size(15)
        okr_content_format.set_border(1)
        okr_content_format.set_font_color('black')
        okr_content_format.set_align('right')
        okr_content_format.set_align('vcenter')
        okr_content_format.set_text_wrap()
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
        titles = ['項次','房號', '租戶','電錶','啟始度數', '截止度數', '區間用電度數']
        title_width = [10,15, 45, 45, 20, 20, 30]
        nnum = 1
        ws = {}
        ws = wb.add_worksheet("CloudRent案場區間用電數報表(%s ~ %s)" % (self.start_date,self.end_date))
        mytitle = "%s-區間用電數報表(%s ~ %s)" % (self.project_no.project_no,self.start_date,self.end_date)
        mytitle1 = "%s-區間總用電數合計：%s 度" % (self.project_no.project_no,mytotscale)
        ########################################
        row = 0
        col = 0
        ws.write(row, col, mytitle, title_format)
        row += 1
        ws.write(row, col, mytitle1, title_format)
        row += 2
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1
            ws.freeze_panes(row + 1, 0)
        nitem = 1
        for rec in scale_rec:
            row += 1
            ws.write(row, 0, nitem, okc_content_format)
            ws.write(row, 1, rec.house_no if rec.house_no else ' ', okl_content_format)
            ws.write(row, 2, rec.member_id.member_name if rec.member_id else ' ', okl_content_format)
            ws.write(row, 3, rec.emeter_id.emeter_name if rec.emeter_id else ' ', okl_content_format)
            ws.write(row, 4, rec.start_scale if rec.start_scale else ' ', okl_content_format)
            ws.write(row, 5, rec.end_scale if rec.end_scale else ' ', okl_content_format)
            ws.write(row, 6, rec.duration_scale if rec.duration_scale else ' ', okl_content_format)
            nitem = nitem + 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['cloudrent.excel_download']

        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, })
        myviewid = self.env.ref('cloudrent_household.cloudrent_excel_download_tree')

        return {
            'view_name': 'cloudrent_excel_download',
            'name': (u'案場別區間用電度數統計'),
            'type': 'ir.actions.act_window',
            'res_model': 'cloudrent.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}