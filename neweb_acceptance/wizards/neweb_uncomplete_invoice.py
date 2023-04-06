# -*- coding: utf-8 -*-
# Author : Peter Wu

import io
import base64
from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta,date
import xlsxwriter

class NewebUncompleteInvoice(models.TransientModel):
    _name = "neweb_acceptance.uncomplete_invoice_wizard"
    _description = "尚未完成發票開立"

    sales = fields.Many2one('hr.employee',string="業務")

    @api.onchange('create_date')
    def onchangeuid(self):
        myids = []
        self.env.cr.execute("""select get_proj_sale()""")
        myids1 = self.env.cr.fetchall()
        for rec in myids1:
            myids.append(rec[0])
        res = {}
        res['domain'] = {'sales': [('id', 'in', myids)]}
        return res

    def run_uncomplete_invoice(self):
        if self.sales:
            saleid = self.sales.id
        else:
            saleid = 0

        self.env.cr.execute("""select gen_uncomplete_invoice(%d)""" % saleid)
        self.env.cr.execute("""commit""")
        myrec = self.env['neweb_acceptance.uncomplete_list'].search([])
        myrec.sorted(key=lambda r: (r.proj_sale, r.project_no))

        # 排序 按 業務,專案編號
        output = io.BytesIO()
        if not self.sales:
            mysale = "ALL"
        else:
            mysale = "%s" % self.sales.name
        myxlsfilename1 = "未完成驗收專案清單(%s).xlsx" % mysale
        mysubject = '未完成驗收專案清單(%s)' % mysale


        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '未完成驗收專案清單',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '未完成驗收專案清單',
            'keywords': '未完成驗收專案清單',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet(mysubject)
        ########################################
        title_format = wb1.add_format()
        title_format.set_font_size(20)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb1.add_format()
        head_format.set_font_size(10)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb1.add_format()
        okc_content_format.set_font_size(10)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb1.add_format()
        okl_content_format.set_font_size(10)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb1.add_format()
        ngc_content_format.set_font_size(10)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb1.add_format()
        ngl_content_format.set_font_size(10)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################
        date_format = wb1.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(10)
        date_format.set_border(1)
        date_format.set_font_color('black')
        date_format.set_align('right')
        date_format.set_align('vcenter')
        date_format.set_text_wrap()

        titles1 = ['專案編號','合約編號','客戶名稱','專案業務']
        title_width = [25,25,60,40]

        row = 0
        # mytitle = "客戶專案貨品狀態情況表"
        ws1.set_row(row, 20)
        ws1.write(row, 2, mysubject, title_format)
        row += 2
        col = 0
        for title in titles1:
            ws1.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws1.set_row(row, 15)
            ws1.set_column(myloc, title_width[col])
            col += 1

        ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in myrec:


            ws1.write(row, 0, line.project_no.name if line.project_no else ' ', okc_content_format)
            ws1.write(row, 1, line.contract_no.name if line.contract_no else ' ', okc_content_format)
            ws1.write(row, 2, line.cus_name.name if line.cus_name else ' ', okc_content_format)
            ws1.write(row, 3, line.proj_sale.name if line.proj_sale else ' ', okc_content_format)

            row += 1
            nitem += 1

        wb1.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()
        mydownrec = self.env['neweb_acceptance.excel_download']
        mydownrec.create({'xls_file': myxlsfile1, 'xls_file_name': myxlsfilename1})
        myviewid = self.env.ref('neweb_acceptance.neweb_acceptance_download_tree')
        return {
            'view_name': 'NEWEB_ACCEPTANCE',
            'name': ('neweb_acceptace'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_acceptance.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

