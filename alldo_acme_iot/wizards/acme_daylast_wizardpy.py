# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class acmedaylastwizard(models.TransientModel):
    _name = "alldo_acme_iot.daylast_wizard"

    start_date = fields.Date(string="啟始時間",required=True)
    end_date = fields.Date(string="截止時間",required=True)

    def run_daylast_list(self):
        self.env.cr.execute("""select gendaylasttime('%s','%s')""" % (self.start_date,self.end_date))
        self.env.cr.execute("""commit""")

        self.env.cr.execute("""select gendaylastman()""")
        self.env.cr.execute("""commit""")

        mydaylastsumrec = self.env['alldo_acme_iot.daylast_sum_list'].search([])
        mycount = self.env['alldo_acme_iot.daylast_manlist'].search_count([])
        output = io.BytesIO()

        myxlsfilename = "每日最後工件時間記錄_%s_%s.xlsx" % (self.start_date, self.end_date)
        mysubject = "每日最後工件時間記錄_%s_%s.xlsx" % (self.start_date, self.end_date)

        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '每日最後工件時間記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'ACME',
            'company': 'ACME',
            'category': '每日最後工件時間記錄',
            'keywords': '每日最後工件時間記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("每日最後工件時間記錄")
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
        mymanlist = self.env['alldo_acme_iot.daylast_manlist'].search([])
        mymancount = self.env['alldo_acme_iot.daylast_manlist'].search_count([])

        titles = ['日期']
        title_width = [80]
        for rec in mymanlist:
            titles.append(rec.emp_name)
            title_width.append(60)

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
        nsum = 0
        for line in mydaylastsumrec:
            ws.write(row, 0, line.last_date1 if line.last_date1 else ' ', okc_content_format)
            if mymancount > 0:
               ws.write(row, 1, line.cdatetime1 if line.cdatetime1 else ' ', okc_content_format)
            if mymancount > 1:
               ws.write(row, 2, line.cdatetime2 if line.cdatetime2 else ' ', okc_content_format)
            if mymancount > 2:
               ws.write(row, 3, line.cdatetime3 if line.cdatetime3 else ' ', okc_content_format)
            if mymancount > 3:
               ws.write(row, 4, line.cdatetime4 if line.cdatetime4 else ' ', okc_content_format)
            if mymancount > 4:
               ws.write(row, 5, line.cdatetime5 if line.cdatetime5 else ' ', okc_content_format)
            if mymancount > 5:
               ws.write(row, 6, line.cdatetime6 if line.cdatetime6 else ' ', okc_content_format)
            if mymancount > 6:
               ws.write(row, 7, line.cdatetime7 if line.cdatetime7 else ' ', okc_content_format)
            if mymancount > 7:
               ws.write(row, 8, line.cdatetime8 if line.cdatetime8 else ' ', okc_content_format)
            if mymancount > 8:
               ws.write(row, 9, line.cdatetime9 if line.cdatetime9 else ' ', okc_content_format)
            if mymancount > 9:
               ws.write(row, 10, line.cdatetime10 if line.cdatetime10 else ' ', okc_content_format)


            row += 1
            nitem += 1

        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_acme_iot.excel_download']
        if mycount > 0:
            myrundesc = "最後工件記錄 日期區間:%s - %s" % (self.start_date,self.end_date)
            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'run_desc': myrundesc})
        else:
            raise UserError("沒每日最後工件時間記錄可供匯出！")

        myviewid = self.env.ref('alldo_acme_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'ngreturn_list',
            'name': (u'每日最後工件時間記錄'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_acme_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}


