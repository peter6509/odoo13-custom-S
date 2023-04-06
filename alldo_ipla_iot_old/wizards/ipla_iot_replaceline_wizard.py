# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class iplaiotreplacelinewizard(models.TransientModel):
    _name = "alldo_ipla_iot.replaceline_wizard"

    rep_start_date = fields.Date(string="啟始日期",required=True)
    rep_end_date = fields.Date(string="截止日期",required=True)
    rep_owner = fields.Many2one('hr.employee',string="架機工程師")
    run_desc = fields.Char(string="匯出說明",default=' ')

    def run_replaceline(self):
        if self.rep_owner.id == False:
            self.env.cr.execute("""select genreplaceline1('%s','%s')""" % (self.rep_start_date, self.rep_end_date))
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select genreplaceline2('%s','%s',%d)""" % (self.rep_start_date, self.rep_end_date, self.rep_owner.id))
            self.env.cr.execute("""commit""")

        mywkrec = self.env['alldo_ipla_iot.replaceline_list'].search([])
        mycount = self.env['alldo_ipla_iot.replaceline_list'].search_count([])
        output = io.BytesIO()
        if self.rep_owner.id == False :
            myxlsfilename = "工程師換線記錄表_(%s-%s)_ALL.xlsx" % (self.rep_start_date.strftime("%Y%m%d"), self.rep_end_date.strftime("%Y%m%d"))
            mysubject = "工程師換線記錄表_(%s-%s)_ALL.xlsx" % (self.rep_start_date.strftime("%Y%m%d"), self.rep_end_date.strftime("%Y%m%d"))
        else:
            myxlsfilename = "工程師換線記錄表_(%s-%s)_%s.xlsx" % (
            self.rep_start_date.strftime("%Y%m%d"), self.rep_end_date.strftime("%Y%m%d"), self.rep_owner.name)
            mysubject = "工程師換線記錄表_(%s-%s)_%s.xlsx" % (
            self.rep_start_date.strftime("%Y%m%d"), self.rep_end_date.strftime("%Y%m%d"), self.rep_owner.name)

        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '精宏機械工程師換線記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'JH',
            'company': '精宏機械股份有限公司',
            'category': '工程師換線記錄表',
            'keywords': '工程師換線記錄表',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("精宏機械工程師換線記錄表")
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
        currency_format.set_align('riiplat')
        currency_format.set_align('vcenter')
        currency_format.set_text_wrap()

        titles = ['工單編號', '產品名稱',  '機台名稱', '工程師', '開始換線時間', '結束換線時間', '實際工時(分鐘)']
        title_width = [25, 60, 25, 20, 30, 30, 30]

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
        for line in mywkrec:
            myprod = line.product_no.name + '#' + line.eng_type
            ws.write(row, 0, line.order_id.name if line.order_id else ' ', okl_content_format)
            ws.write(row, 1, myprod if line.product_no else ' ', okl_content_format)
            ws.write(row, 2, line.equipment_id.equipment_no if line.equipment_id else ' ', okl_content_format)
            ws.write(row, 3, line.replace_owner.name if line.replace_owner else ' ', okl_content_format)
            ws.write(row, 4, line.replace_start_datetime[:-7] if line.replace_start_datetime else ' ', okl_content_format)
            ws.write(row, 5, line.replace_end_datetime[:-7] if line.replace_end_datetime else ' ', okl_content_format)
            ws.write(row, 6, line.replace_duration if line.replace_duration else ' ', okl_content_format)

            row += 1
            nitem += 1

        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_ipla_iot.excel_download']
        if mycount > 0:
            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'run_desc': self.run_desc})
        else:
            raise UserError("沒有工程師換線記錄可供匯出！")

        myviewid = self.env.ref('alldo_ipla_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'replaceline_list',
            'name': (u'工程師換線記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
