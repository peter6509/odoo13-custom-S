# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class iplaiotngreturnexcelwizard(models.TransientModel):
    _name = "alldo_ipla_iot.ngreturn_excel_wizard"

    partner_id = fields.Many2one('res.partner',string="委外廠商",required=True)
    product_no = fields.Many2one('product.product',string="料號")
    start_date = fields.Date(string="啟始日期",required=True)
    end_date = fields.Date(string="截止日期",required=True)
    run_desc = fields.Char(string="匯出說明",default=' ')

    @api.onchange('partner_id')
    def onclientchangepo(self):
        self.env.cr.execute("""select getsupplierprod(%d)""" % self.partner_id.id)
        ids = []
        myids = self.env.cr.fetchall()
        if not myids:
            return {'domain': {'product_no': [(1, '=', 1)]}}
        else:
            for rec in myids:
                ids.append(rec[0])
            return {'domain': {'product_no': [('id', 'in', ids)]}}

    def run_ngreturn_excel(self):
        if not self.product_no:
            myprodid = 0
        else:
            myprodid = self.product_no.id
        self.env.cr.execute("""select genngreturnexcel(%d,%d,'%s','%s')""" % (self.partner_id.id, myprodid, self.start_date, self.end_date))
        self.env.cr.execute("""commit""")
        myngreturnrec = self.env['alldo_ipla_iot.ngreturn_list'].search([])
        mycount = self.env['alldo_ipla_iot.ngreturn_list'].search_count([])
        output = io.BytesIO()

        myxlsfilename = "委外加工記錄_%s_%s_%s.xlsx" % (self.partner_id.name,self.product_no.name, datetime.now().strftime("%Y%m%d"))
        mysubject = '委外加工記錄_%s_%s_%s.xlsx' % (self.partner_id.name,self.product_no.name, datetime.now().strftime("%Y%m%d"))

        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': 'ipla委外加工記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'JH',
            'company': 'ipla',
            'category': 'ipla委外加工記錄',
            'keywords': 'ipla委外加工記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("ipla委外加工記錄")
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

        titles = ['委外號碼', '委外廠商', '檢驗日期', '產品料號', '加工良品數' ,'加工不良數' ]
        title_width = [30, 60, 20, 60, 30, 30]

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
        for line in myngreturnrec:
            # if line.ngreturn_type=='1':
            #     mytype = '廠內NG'
            # else:
            #     mytype = '託工NG'
            ws.write(row, 0, line.name if line.name else ' ', okl_content_format)
            ws.write(row, 1, line.partner_id.name if line.partner_id else ' ', okl_content_format)
            ws.write(row, 2, line.ngreturn_date1 if line.ngreturn_date1 else ' ', okl_content_format)
            ws.write(row, 3, line.product_id.name if line.product_id else ' ', okl_content_format)
            ws.write(row, 4, line.return_good_num if line.return_good_num > 0 else ' ', okl_content_format)
            ws.write(row, 5, line.processing_ng_num if line.processing_ng_num > 0 else ' ', okl_content_format)
            # ws.write(row, 5, mytype, okc_content_format)

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
            raise UserError("沒委外加工記錄可供匯出！")

        myviewid = self.env.ref('alldo_ipla_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'ngreturn_list',
            'name': (u'NG記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
