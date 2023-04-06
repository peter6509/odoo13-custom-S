# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, _
import datetime
from odoo.exceptions import UserError
import io
import base64

import pytz
# from odoo.addons import decimal_precision as dp
from datetime import timedelta,date
import xlsxwriter

class newebprojinvwizard(models.TransientModel):
    _name = "neweb_invoice.projinv_wizard"

    project_no = fields.Char(string=u"專案編號")
    cus_name = fields.Char(string=u"客戶名稱")
    project_ids = fields.Many2many('neweb.project', 'neweb_project_projinv_rel', 'projinv_id', 'proj_id',string=u"專案編號")
    start_date = fields.Date(string=u"啟始日期")
    end_date = fields.Date(string=u"截止日期")
    excel_desc = fields.Char(string=u"Excel彙整說明")

    def gen_projinvdata(self):
        if not self.project_ids and not self.start_date and not self.end_date and not self.project_no:
            raise UserError(u"專案編號或起訖日期至少要有一個數據")

        if not self.project_ids and not self.project_no:
            self._cr.execute("""select genprojinvdata1('%s','%s')""" % (self.start_date, self.end_date))
        elif (not self.start_date or not self.end_date) and not self.project_ids:
            self._cr.execute("""select genprojinvdata3('%s')""" % self.project_no)
        else:
            self._cr.execute("""select genprojinvdata2(%d)""" % self.id)
        self._cr.execute("""commit""")

        self.ensure_one()
        import xlwt

        borders = xlwt.Borders()  # Create Borders
        borders.left = xlwt.Borders.THIN  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40

        center_alignment = xlwt.Alignment()  # Create Alignment
        center_alignment.horz = xlwt.Alignment.HORZ_CENTER
        center_alignment.vert = xlwt.Alignment.VERT_CENTER

        title_font = xlwt.Font()  # Create the Font
        title_font.height = 0x00C8 * 1

        title_style = xlwt.XFStyle()  # Create Style
        title_style.borders = borders  # Add Borders to Style
        title_style.alignment = center_alignment
        title_style.font = title_font

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(u'成本分析')
        ws1 = wb.add_sheet(u'發票彙整')
        ws2 = wb.add_sheet(u"供應商請款")

        # ws.write_merge(0, 2, 0, 10, u"庫存帳齡表", title_style)

        content_font = xlwt.Font()
        content_font.height = 0x00C8 * 1
        content_style = xlwt.XFStyle()  # Create Style

        content_style.borders = borders  # Add Borders to Style

        content_alignment = xlwt.Alignment()  # Create Alignment
        content_alignment.horz = xlwt.Alignment.HORZ_LEFT
        content_alignment.vert = xlwt.Alignment.VERT_CENTER
        content_style.alignment = content_alignment
        content_style.alignment.wrap = 1
        content_style.font = content_font

        row = 0

        ws.row(row).height = 300
        row += 1
        ws_titles = [
            u"專案編號",
            u"產品組別",
            u"客戶名稱",
            u"機型-機種/料號",
            u"規格說明",
            u"數量",
            u"成本總價",
            u"報價廠商",
            u"銷售金額",
        ]

        col = 0
        for title in ws_titles:
            ws.write(row, col, title, content_style)
            col += 1
        ws.row(row).height = 500
        ws.col(0).width = 3600  # 專案編號
        ws.col(1).width = 3600  # 產品組別
        ws.col(2).width = 7200  # 客戶名稱
        ws.col(3).width = 7200  # 機型-機種/料號
        ws.col(4).width = 10800  # 規格說明
        ws.col(5).width = 3600  # 數量
        ws.col(6).width = 3600  # 成本總價
        ws.col(7).width = 7200  # 報價廠商
        ws.col(8).width = 3600  # 銷售金額
        myprojrec = self.env['neweb_invoice.projectdata'].search([])
        myprojrec = myprojrec.sorted(key=lambda r: (r.project_no.name, r.id))
        row += 1
        myprojno = ' '
        for line in myprojrec:
            if myprojno != line.project_no.name:
                ws.write(row, 0, line.project_no.name, content_style)
                myprojno = line.project_no.name
            else:
                ws.write(row, 0, ' ', content_style)
            ws.write(row, 1, line.prod_set.name if line.prod_set else ' ', content_style)
            ws.write(row, 2, line.cus_name.name if line.cus_name else ' ', content_style)
            ws.write(row, 3, line.prod_modeltype if line.prod_modeltype else ' ', content_style)
            ws.write(row, 4, line.prod_desc if line.prod_desc else ' ', content_style)
            ws.write(row, 5, line.prod_num if line.prod_num else ' ', content_style)
            ws.write(row, 6, line.prod_cost_price if line.prod_cost_price else ' ', content_style)
            ws.write(row, 7, line.supplier.name if line.supplier else ' ', content_style)
            ws.write(row, 8, line.prod_sale_price if line.prod_sale_price else ' ', content_style)
            row += 1

        row = 0
        ws1_titles = [
            u"專案編號",
            u"發票日",
            u"發票號碼",
            u"金額",
            u"請款日",
            u"備註",
        ]
        col = 0
        for title in ws1_titles:
            ws1.write(row, col, title, content_style)
            col += 1
        ws1.row(row).height = 500
        ws1.col(0).width = 3600  # 專案編號
        ws1.col(1).width = 3600  # 發票日
        ws1.col(2).width = 3600  # 發票號碼
        ws1.col(3).width = 3600  # 金額
        ws1.col(4).width = 3600  # 請款日
        ws1.col(5).width = 7200  # 備註

        myinvoicerec = self.env['neweb_invoice.invoicedata'].search([])
        myinvoicerec = myinvoicerec.sorted(key=lambda r: (r.project_no.name, r.id))
        row += 1
        myprojno = ' '
        for line in myinvoicerec:
            if myprojno != line.project_no.name:
                ws1.write(row, 0, line.project_no.name if line.project_no else ' ', content_style)
                myprojno = line.project_no.name
            else:
                ws1.write(row, 0, ' ', content_style)
            if line.invoice_cdate:
                ws1.write(row, 1, line.invoice_cdate if line.invoice_cdate else ' ', content_style)
            else:
                ws1.write(row, 1, ' ', content_style)
            if line.invoice_no:
                ws1.write(row, 2, line.invoice_no if line.invoice_no else ' ', content_style)
            else:
                ws1.write(row, 2, ' ', content_style)
            if line.invoice_untax_amount:
                ws1.write(row, 3, line.invoice_untax_amount, content_style)
            else:
                ws1.write(row, 3, ' ', content_style)
            if line.application_cdate:
                ws1.write(row, 4, line.application_cdate, content_style)
            else:
                ws1.write(row, 4, ' ', content_style)
            if line.other_memo:
                ws1.write(row, 5, line.other_memo, content_style)
            else:
                ws1.write(row, 5, ' ', content_style)
            row += 1

        row = 0
        ws2_titles = [
            u"專案編號",
            u"發票日",
            u"發票號碼",
            u"付款期限",
            u"付款對象",
            u"金額",
            u"是否請款",
        ]
        col = 0
        for title in ws2_titles:
            ws2.write(row, col, title, content_style)
            col += 1
        ws2.row(row).height = 500
        ws2.col(0).width = 3600  # 專案編號
        ws2.col(1).width = 3600  # 發票日
        ws2.col(2).width = 3600  # 發票號碼
        ws2.col(3).width = 3600  # 付款期限
        ws2.col(4).width = 7200  # 付款對象
        ws2.col(5).width = 3600  # 金額
        ws2.col(6).width = 3600  # 是否請款

        mypurinvrec = self.env['neweb_invoice.purinvdata'].search([])
        mypurinvrec = mypurinvrec.sorted(key=lambda r: (r.pitem_origin_no, r.id))
        row += 1
        myprojno = ' '
        for line in mypurinvrec:
            if myprojno != line.pitem_origin_no:
                ws2.write(row, 0, line.pitem_origin_no, content_style)
                myprojno = line.pitem_origin_no
            else:
                ws2.write(row, 0, ' ', content_style)
            if line.invoice_cdate:
                ws2.write(row, 1, line.invoice_cdate, content_style)
            else:
                ws2.write(row, 1, ' ', content_style)
            if line.invoice_no:
                ws2.write(row, 2, line.invoice_no, content_style)
            else:
                ws2.write(row, 2, ' ', content_style)
            if line.inv_cpaymentterm:
                ws2.write(row, 3, line.inv_cpaymentterm, content_style)
            else:
                ws2.write(row, 3, ' ', content_style)
            if line.invoice_partner:
                ws2.write(row, 4, line.invoice_partner.comp_sname, content_style)
            else:
                ws2.write(row, 4, ' ', content_style)
            if line.invoice_sum:
                ws2.write(row, 5, line.invoice_sum, content_style)
            else:
                ws2.write(row, 5, ' ', content_style)
            if line.payment_yn == '1':
                ws2.write(row, 6, u'未請款', content_style)
            else:
                ws2.write(row, 6, u'已請款', content_style)

            row += 1

        # output = StringIO.StringIO()
        output = io.BytesIO()
        wb.save(output)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        # self.state = '2'
        mydate = datetime.datetime.now()
        myxlsfilename = _(u"%s-%s.xls" % (self.env.user.name, self.excel_desc))

        myrec = self.env['neweb_invoice.proj_inv_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid1 = self.env.ref('neweb_invoice.projinv_excel_download_view_tree')
        return {
            'view_name': 'ProjectInvoiceWizard',
            'name': (u'成本分析-發票彙整分析'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_invoice.proj_inv_excel_download',
            'view_id': myviewid1.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
