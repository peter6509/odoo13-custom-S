# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class accmoveexportwizard(models.TransientModel):
    _name = "alldo_acme_iot.accmove_excel_export_wizard"
    _description = "應收應付帳款匯出EXCEL精靈"

    emp_no = fields.Many2one('res.users',string="匯出人員",default=lambda self:self.env.uid)
    acc_type = fields.Selection([('1','應收未收帳款'),('2','應付未付帳款')],string="帳款模式",default='1')
    run_desc = fields.Char(string="匯出說明",required=True)

    def run_accmove_export(self):
        if self.acc_type=='1':
            myaccmoverec =  self.env['account.move'].search([('state','!=','cancel'),('amount_residual','!=',0),('type','=','out_invoice')],order="invoice_date desc")
            mycount = self.env['account.move'].search_count([('state','!=','cancel'),('amount_residual','!=',0),('type','=','out_invoice')])
        else:
            myaccmoverec =  self.env['account.move'].search([('state','!=','cancel'),('amount_residual','!=',0),('type','=','in_invoice')],order="invoice_date desc")
            mycount = self.env['account.move'].search_count([('state','!=','cancel'),('amount_residual','!=',0),('type','=','in_invoice')])
        output = io.BytesIO()

        if self.acc_type=='1':
            myxlsfilename = "應收未收帳款記錄_%s_%s.xlsx" % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
            mysubject = '應收未收帳款記錄_%s_%s.xlsx' %  (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
        else:
            myxlsfilename = "應付未付帳款記錄_%s_%s.xlsx" % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
            mysubject = '應付未付帳款記錄_%s_%s.xlsx' % (self.emp_no.name,datetime.now().strftime("%Y%m%d"))
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '正璽金屬工業應收應付記錄',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': '正璽金屬工業',
            'company': '正璽金屬工業有限公司',
            'category': '應收應付記錄',
            'keywords': '應收應付記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        if self.acc_type=='1':
           ws = wb.add_worksheet("正璽金屬工業應收未收記錄")
        else:
           ws = wb.add_worksheet("正璽金屬工業應付未付記錄")
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
        ###########################################
        date_format = wb.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(15)
        date_format.set_border(1)
        date_format.set_align('center')
        date_format.set_align('vcenter')


        if self.acc_type=='1':
           titles = ['項次','立帳單號','立帳日期','客戶名稱', '來源單號', '幣別' , '應收金額' , '未收金額','發票號碼','狀態']
           title_width = [15,30,30, 50, 30,20, 30, 30 ,30,20]
        else:
            titles = ['項次', '立帳單號', '立帳日期', '客戶名稱', '來源單號', '幣別', '應收金額', '未收金額', '發票號碼', '狀態']
            title_width = [15, 30, 30, 50, 30, 20, 30, 30, 30, 20]

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
        myattsum = 0.00
        mystate=' '
        if self.acc_type=='1':
            for line in myaccmoverec:
                if line.state=='draft':
                    mystate='草稿'
                elif line.state=='posted':
                    mystate='過帳'
                ws.write(row, 0, nitem, okc_content_format)
                ws.write(row, 1, line.name if line.name else ' ', okl_content_format)
                ws.write(row, 2, line.invoice_date if line.invoice_date else ' ', date_format)
                ws.write(row, 3, line.partner_id.name if line.partner_id else ' ', okl_content_format)
                ws.write(row, 4, line.invoice_origin if line.invoice_origin else ' ', okl_content_format)
                ws.write(row, 5, line.currency_id.name if line.currency_id else ' ', okc_content_format)
                ws.write(row, 6, line.amount_total if line.amount_total else '0', currency_format)
                ws.write(row, 7, line.amount_residual if line.amount_residual else '0', currency_format)
                ws.write(row, 8, line.taiwan_receipt if line.taiwan_receipt else ' ', okl_content_format)
                ws.write(row, 9, mystate,okc_content_format)
                row += 1
                nitem += 1
            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()
            myrec = self.env['alldo_acme_iot.accmove_excel_download']
            if mycount > 0:
                myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename,'run_desc':self.run_desc})
            else:
                raise UserError("沒有符合的記錄可供匯出！")
        else:
            for line in myaccmoverec:
                if line.state == 'draft':
                    mystate = '草稿'
                elif line.state == 'posted':
                    mystate = '過帳'
                ws.write(row, 0, nitem, okc_content_format)
                ws.write(row, 1, line.name if line.name else ' ', okl_content_format)
                ws.write(row, 2, line.invoice_date if line.invoice_date else ' ', date_format)
                ws.write(row, 3, line.partner_id.name if line.partner_id else ' ', okl_content_format)
                ws.write(row, 4, line.invoice_origin if line.invoice_origin else ' ', okl_content_format)
                ws.write(row, 5, line.currency_id.name if line.currency_id else ' ', okc_content_format)
                ws.write(row, 6, line.amount_total if line.amount_total else '0', currency_format)
                ws.write(row, 7, line.amount_residual if line.amount_residual else '0', currency_format)
                ws.write(row, 8, line.taiwan_receipt if line.taiwan_receipt else ' ', okl_content_format)
                ws.write(row, 9, mystate, okc_content_format)
                row += 1
                nitem += 1
            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()
            myrec = self.env['alldo_acme_iot.accmove_excel_download']
            if mycount > 0:
                myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'run_desc': self.run_desc})
            else:
                raise UserError("沒有符合的記錄可供匯出！")

        myviewid = self.env.ref('alldo_acme_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'emp_attendance_list',
            'name': (u'應收應付記錄匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_acme_iot.accmove_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



