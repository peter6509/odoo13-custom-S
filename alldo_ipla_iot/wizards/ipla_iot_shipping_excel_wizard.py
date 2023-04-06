# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class iplaiotshippingexcelwizard(models.TransientModel):
    _name = "alldo_ipla_iot.shipping_excel_wizard"
    _description = "客戶出貨記錄匯出EXCEL "

    partner_id = fields.Many2one('res.partner',string="客戶")
    product_no = fields.Many2one('product.product',string="產品")
    start_date = fields.Date(string="啟始日期",required=True)
    end_date = fields.Date(string="截止日期",required=True)
    run_desc = fields.Char(string="匯出說明")

    @api.onchange('partner_id')
    def onclientchangepo(self):
        self.env.cr.execute("""select getcusprod(%d)""" % self.partner_id.id)
        ids = []
        myids = self.env.cr.fetchall()
        if not myids:
            return {'domain': {'product_no': [(1, '=', 1)]}}
        else:
            for rec in myids:
                ids.append(rec[0])
            return {'domain': {'product_no': [('id', 'in', ids)]}}

    def run_shipping_excel(self):
        if not self.partner_id:
            partnerid = 0
        else:
            partnerid = self.partner_id.id
        if not self.product_no:
            prodid = 0
        else:
            prodid = self.product_no.id
        self.env.cr.execute("""select genshippingexcel(%d,%d,'%s','%s')""" % (partnerid, prodid, self.start_date, self.end_date))
        self.env.cr.execute("""commit""")
        myshippingrec = self.env['alldo_ipla_iot.shipping_list'].search([])
        mycount = self.env['alldo_ipla_iot.shipping_list'].search_count([])
        output = io.BytesIO()

        myxlsfilename = "客戶出貨記錄_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
        mysubject = '客戶出貨記錄_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))

        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '正璽金屬工業客戶出貨記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'JH',
            'company': '正璽金屬工業有限公司',
            'category': '客戶出貨記錄',
            'keywords': '客戶出貨記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("正璽金屬工業客戶出貨記錄")
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

        titles = ['內部單據', '出貨單號', '倉庫位置', '出貨客戶', '出貨日期', '產品料號', '來源單據', '出貨數量']
        title_width = [20, 20, 20, 40, 20, 80, 20, 20]

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
        for line in myshippingrec:
            nsum = nsum + line.qty_done
            ws.write(row, 0, line.name if line.name else ' ', okl_content_format)
            ws.write(row, 1, line.report_no if line.report_no else ' ', okl_content_format)
            ws.write(row, 2, line.location_id.name if line.location_id else ' ', okl_content_format)
            ws.write(row, 3, line.partner_id.name if line.partner_id else ' ', okl_content_format)
            ws.write(row, 4, line.shipping_date1[0:10] if line.shipping_date1 else ' ', okl_content_format)
            ws.write(row, 5, '[' + line.product_id.default_code + '] ' + line.product_id.name if line.product_id else ' ', okl_content_format)
            ws.write(row, 6, line.origin if line.origin else ' ', okl_content_format)
            ws.write(row, 7, line.qty_done if line.qty_done else ' ', okc_content_format)
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
            raise UserError("沒有出貨記錄可供匯出！")

        myviewid = self.env.ref('alldo_ipla_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'outsourcing_inout_list',
            'name': (u'出貨記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
