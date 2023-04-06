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

class newebpartnerexportwizard1(models.TransientModel):
    _name = "neweb.partner_export_wizard1"
    _description = "匯出供應商資料"

    export_memo = fields.Char(string="匯出說明",required=True)


    def run_partner_export(self):


        self.env.cr.execute("""select genallpartnerlist1()""")
        self.env.cr.execute("""commit""")
        mypartnerrec = self.env['neweb.partner_list'].search([])
        output = io.BytesIO()

        myxlsfilename = "PARTNER_%s.xlsx" % (self.export_memo)
        mysubject = 'PARTNER_%s.xlsx' % (self.export_memo)
        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': '供應商資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '供應商資訊',
            'keywords': '供應商資訊',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("供應商資訊檔")
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

        titles1 = ['廠商名稱', '統一編號', '電話', '地址', '聯絡人', '人員別', '職稱', '聯絡人電話', '聯絡人手機', '聯絡人EMAIL','付款天數','備註']
        title_width = [45, 20, 25, 60, 20, 30, 20, 25, 25, 35,25, 60]

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

        for line in mypartnerrec:
            mycontacttype = line.contact_type.name
            ws.write(row, 0, line.cus_name if line.cus_name else ' ', okl_content_format)
            ws.write(row, 1, line.vat if line.vat else ' ', okl_content_format)
            ws.write(row, 2, line.tel if line.tel else ' ', okl_content_format)
            ws.write(row, 3, line.address if line.address else ' ', okl_content_format)
            ws.write(row, 4, line.contact if line.contact else ' ', okl_content_format)
            ws.write(row, 5, line.contact_type.name if line.contact_type else ' ', okl_content_format)
            ws.write(row, 6, line.function if line.function else ' ', okl_content_format)
            ws.write(row, 7, line.tel1 if line.tel1 else ' ', okl_content_format)
            ws.write(row, 8, line.mobile if line.mobile else ' ', okl_content_format)
            ws.write(row, 9, line.email if line.email else ' ', okl_content_format)
            ws.write(row, 10, line.payment_days if line.payment_days else ' ', okc_content_format)
            ws.write(row, 11, line.comment if line.comment else ' ', okl_content_format)
            row += 1
            nitem += 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()


        myrec = self.env['neweb.export_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})

        myviewid = self.env.ref('neweb_projext.partner_export_download_tree')

        return {
            'view_name': 'newebpartnerexportdownload',
            'name': ('廠商資訊EXCEL匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb.export_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
