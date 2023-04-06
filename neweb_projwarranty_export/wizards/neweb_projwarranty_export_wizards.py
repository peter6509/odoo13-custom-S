# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter

class newebprojwarrantyexport(models.TransientModel):
    _name = "neweb.projwarranty_export_wizard"

    proj_ids = fields.Many2many('neweb.project','neweb_projwarranty_export_rel','wizard_id','proj_id',string="成本分析")
    proj_desc = fields.Char(string="成本分析檢索")
    run_desc = fields.Char(string="匯出說明",required=True)
    run_owner = fields.Many2one('res.users',string="匯出人員",default=lambda self:self.env.uid)


    def run_projwarranty_export(self):
        if not self.proj_desc:
            self.env.cr.execute("""select getprojname(%d)""" % self.id)
            myres = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select genprojwarrantyexport(%d)""" % self.id)
            self.env.cr.execute("""commit""")
        else:
            self.env.cr.execute("""select getprojname1('%s')""" % self.proj_desc)
            myres = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select genprojwarrantyexport1('%s')""" % self.proj_desc)
            self.env.cr.execute("""commit""")
        myprojwarrantyrec = self.env['neweb.projwarrantyinfo_export'].search([])
        output = io.BytesIO()
        myxlsfilename = "%s_%s.xlsx" % (self.run_desc,datetime.now().strftime("%Y%m%d"))
        mysubject = '%s_%s.xlsx' % (self.run_desc,datetime.now().strftime("%Y%m%d"))
        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': '專案保固匯出資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '專案保固數據',
            'keywords': '專案保固數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws = wb.add_worksheet("成本分析保固資訊匯出檔")

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

        ##########################################
        date_format = wb.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(15)
        date_format.set_border(1)
        date_format.set_font_color('black')
        date_format.set_align('right')
        date_format.set_align('vcenter')
        date_format.set_text_wrap()

        titles = ['填寫日期', '專案編號', '客戶名稱', '案名', '機種-機型', '序號', '保固年限', '實際出貨日', '發票日', '發票號碼',
                   '原廠保固(起)', '原廠保固(迄)', '藍新保固(起)','藍新保固(迄)','負責業務','廠商','備註','是否已報保固']
        title_width = [30, 30, 60, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,30,30,15,60,20]
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

        for line in myprojwarrantyrec:
            # mychisalesno = line.chi_sales_no
            # mypurchaseno = line.chi_purchase_no.id
            ws.write(row, 0, datetime.now().strftime("%Y%m%d"), okl_content_format)
            ws.write(row, 1, line.proj_no if line.proj_no else ' ', okl_content_format)
            ws.write(row, 2, line.cus_name if line.cus_name else ' ', okl_content_format)
            ws.write(row, 3, ' ', okl_content_format)
            ws.write(row, 4, line.prod_modeltype if line.prod_modeltype else ' ', okl_content_format)
            ws.write(row, 5, line.prod_serial if line.prod_serial else ' ', okl_content_format)
            ws.write(row, 6, ' ', okl_content_format)
            ws.write(row, 7, line.shipping_date if line.shipping_date else ' ', date_format)
            ws.write(row, 8, line.invoice_date if line.invoice_date else ' ', date_format)
            ws.write(row, 9, line.invoice_no if line.invoice_no else ' ', okl_content_format)
            ws.write(row, 10, ' ', okl_content_format)
            ws.write(row, 11, ' ', okl_content_format)
            ws.write(row, 12, line.neweb_start_date if line.neweb_start_date else ' ', date_format)
            ws.write(row, 13, line.neweb_end_date if line.neweb_end_date else ' ', date_format)
            ws.write(row, 14, line.sale_id.name if line.sale_id else ' ', okl_content_format)
            ws.write(row, 15, line.supplier_id.comp_sname if line.supplier_id else ' ', okl_content_format)
            ws.write(row, 16,  ' ', okl_content_format)
            ws.write(row, 17,  ' ', okl_content_format)

            row += 1
            nitem += 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['neweb.projwarranty_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename,'run_desc':self.run_desc,
                      'export_owner':self.run_owner.id,'export_date':datetime.now(),
                      'proj_no':myres})

        myviewid = self.env.ref('neweb_projwarranty_export.view_neweb_projwarranty_download_tree')

        return {
            'view_name': 'newebprojwarrantyexportwizard',
            'name': ('專案保固資料匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb.projwarranty_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

