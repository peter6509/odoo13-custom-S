# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime
import xlsxwriter
import base64,io
from datetime import datetime,timedelta,date

class NewebMainContractExportWizard(models.TransientModel):
    _name = "neweb_contract.main_export_wizard"
    _description = "維護合約標地物明細匯出"

    contract_no = fields.Many2one('neweb_contract.contract',string="維護合約")

    def run_export_maintenance_line(self):
        if not self.contract_no:
            myconid = 0
        else:
            myconid = self.contract_no.id

        self.env.cr.execute("""select gencontractmainline(%d)""" % myconid)
        self.env.cr.execute("""commit""")

        # import xlwt
        output = io.BytesIO()
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        mysubject = '維護合約標地物明細匯出_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))
        wb.set_properties({
            'title': '維護合約標地物明細精靈',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB',
            'company': 'NEWEB',
            'category': '維護合約標地物明細記錄',
            'keywords': '維護合約標地物明細記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("維護合約標地物明細")
        ########################################
        title_format = wb.add_format()
        title_format.set_font_size(20)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb.add_format()
        head_format.set_font_size(10)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb.add_format()
        okc_content_format.set_font_size(10)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################

        okl_content_format = wb.add_format()
        okl_content_format.set_font_size(10)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()

        #########################################
        ngc_content_format = wb.add_format()
        ngc_content_format.set_font_size(10)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb.add_format()
        ngl_content_format.set_font_size(10)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################
        currency_format = wb.add_format({'num_format': '###,###,##0.00'})
        currency_format.set_font_size(10)
        currency_format.set_border(1)
        currency_format.set_font_color('black')
        currency_format.set_align('right')
        currency_format.set_align('vcenter')
        currency_format.set_text_wrap()
        ##########################################
        date_format = wb.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(10)
        date_format.set_border(1)
        date_format.set_font_color('black')
        date_format.set_align('right')
        date_format.set_align('vcenter')
        date_format.set_text_wrap()

        titles = ["專案編號","合約編號", "客戶名稱", "產品組別", "品牌", "機型-機種/料號", "機型名稱", "序號", "說明","設備位址","SLA", "合約起始日", "合約終止日","業務", "工程師",'維護服務時段','客戶統編',"ID"]
        title_width = [30, 30, 40, 30, 30, 40, 40, 30, 40,40,45, 30, 30, 30, 40,25,15,10]

        row = 1
        col = 0
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        mycontractrec = self.env['neweb_contract.mainline'].search([])
        mycontractrec.sorted(key=lambda r: (r.project_no, r.contract_no))
        for line in mycontractrec:
            ws.write(row, 0, line.project_no, okc_content_format)
            ws.write(row, 1, line.contract_no, okc_content_format)
            ws.write(row, 2, line.customer_name.name if line.customer_name else ' ', okl_content_format)
            ws.write(row, 3, line.prod_set.name if line.prod_set else ' ', okl_content_format)
            ws.write(row, 4, line.prod_brand.name if line.prod_brand else ' ',okl_content_format)
            ws.write(row, 5, line.prod_modeltype if line.prod_modeltype else ' ', okl_content_format)
            ws.write(row, 6, line.prod_modeltype1.name if line.prod_modeltype1 else ' ', okl_content_format)
            ws.write(row, 7, line.machine_serial_no if line.machine_serial_no else ' ', okl_content_format)
            ws.write(row, 8, line.memo if line.memo else ' ', okl_content_format)
            ws.write(row, 9, line.machine_loc if line.machine_loc else ' ', okl_content_format)
            ws.write(row, 10, line.prod_sla.name if line.prod_sla else ' ', okl_content_format)
            ws.write(row, 11, line.contract_start_date if line.contract_start_date else ' ', date_format)
            ws.write(row, 12, line.contract_end_date if line.contract_end_date else ' ', date_format)
            ws.write(row, 13, line.sales.name if line.sales else ' ', okl_content_format)
            ws.write(row, 14, line.ae1 if line.ae1 else ' ', date_format)
            ws.write(row, 15, line.main_service_rule_new.name if line.main_service_rule_new else ' ', okl_content_format)
            ws.write(row, 16, line.vat if line.vat else ' ', okl_content_format)
            ws.write(row, 17, line.id)

            row += 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()

        if myconid == 0 :
           myxlsfilename = "維護合約標地物明細_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
        else:
            myxlsfilename = "維護合約標地物明細_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),self.contract_no.name)
        myrec = self.env['neweb_contract.custom_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid1 = self.env.ref('neweb_contract.neweb_contract_excel_download_view_tree')
        return {
            'view_name': 'ContractDataWizard',
            'name': ('維護合約標地物明細'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_contract.custom_excel_download',
            'view_id': myviewid1.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
