# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class outsourcinginoutwizard(models.TransientModel):
    _name = "alldo_ipla_iot.outsourcing_inout_wizard"

    partner_id = fields.Many2one('res.partner',string="委外廠商",required=True)
    product_id = fields.Many2one('product.product',string="產品")
    start_date = fields.Date(string="啟始日期",required=True)
    end_date = fields.Date(string="截止日期",required=True)
    run_desc = fields.Char(string="匯出說明",default=' ')

    def run_outsourcing_inout(self):
        if not self.product_id:
            myprodid = 0
        else:
            myprodid = self.product_id.id
        self.env.cr.execute("""select genoutsourcinginout(%d,%d,'%s','%s')""" % (self.partner_id.id,myprodid,self.start_date,self.end_date))
        self.env.cr.execute("""commit""")
        myinoutrec = self.env['alldo_ipla_iot.inout_prod_list'].search([])
        mycount = self.env['alldo_ipla_iot.inout_prod_list'].search_count([])
        output = io.BytesIO()


        myxlsfilename = "委外廠商進出料記錄_%s_%s.xlsx" % (self.partner_id.name,datetime.now().strftime("%Y%m%d"))
        mysubject = '委外廠商進出料記錄_%s_%s.xlsx' % (self.partner_id.name,datetime.now().strftime("%Y%m%d"))

        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': 'IPLA委外料件進出記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'ALLDO',
            'company': 'IPLA',
            'category': '委外料件進出記錄',
            'keywords': '委外料件進出記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("IPLA委外料件進出記錄")
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

        titles = ['進出日期','委外廠商', '產品料號', '出廠數量', '回廠良品數', '回廠NG數', '餘額', '出廠承辦人', '回廠承辦人']
        title_width = [20,60, 60, 20, 20, 20, 20, 20, 20]

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
        myprod = ''
        for line in myinoutrec:
            ws.write(row, 0, line.inout_date1 if line.inout_date1 else ' ', okl_content_format)
            ws.write(row, 1, line.inout_partner.name if line.inout_partner else ' ', okl_content_format)
            ws.write(row, 2, line.product_id.name if line.product_id else ' ', okl_content_format)
            ws.write(row, 3, line.out_num if line.out_num else ' ', okc_content_format)
            ws.write(row, 4, line.in_good_num if line.in_good_num else ' ', okc_content_format)
            ws.write(row, 5, line.in_ng_num if line.in_ng_num else ' ', okc_content_format)
            ws.write(row, 6, line.balance_num if line.balance_num else '0', okc_content_format)
            ws.write(row, 7, line.out_owner.name if line.out_owner else ' ', okc_content_format)
            ws.write(row, 8, line.in_owner.name if line.in_owner else ' ', okc_content_format)
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
            raise UserError("沒有委外進出料記錄可供匯出！")

        myviewid = self.env.ref('alldo_ipla_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'outsourcing_inout_list',
            'name': (u'委外廠商進出料記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}


