# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class AcmeKpiWizard(models.TransientModel):
    _name = "alldo_acme_iot.kpi_wizard"

    partner_id = fields.Many2one('res.partner',strin="委外商",domain=lambda self:[('is_company','=',True)])
    start_date = fields.Date(strin="啟始日期",required=True)
    end_date = fields.Date(strin="截止日期",required=True)

    def run_cal_kpi(self):
        if not self.partner_id :
            mypartnerid = 0
        else:
            mypartnerid = self.partner_id.id
        self.env.cr.execute("""select genoutsuborderkpi(%d,'%s','%s')""" % (mypartnerid,self.start_date,self.end_date))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select genkpiquant()""")
        self.env.cr.execute("""commit""")
        # out_rec = self.env['alldo_acme_iot.outsuborder_kpi'].search([])
        out_rec = self.env['alldo_acme_iot.outsuborder_kpi_quant'].search([],order="quant_id,quant_seq")
        # mycount = self.env['alldo_acme_iot.outsuborder_kpi'].search_count([])
        mycount = self.env['alldo_acme_iot.outsuborder_kpi_quant'].search_count([])
        if mypartnerid ==0:
            myxlsfilename = "委外加工交貨KPI_ALL_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
            mysubject = '委外加工交貨KPI_ALL_%s.xlsx' %  (datetime.now().strftime("%Y%m%d"))
        else:
            myxlsfilename = "委外加工交貨KPI_%s_%s.xlsx" % (self.partner_id.name,datetime.now().strftime("%Y%m%d"))
            mysubject = '委外加工交貨KPI_%s_%s.xlsx' % (self.partner_id.name,datetime.now().strftime("%Y%m%d"))
        output = io.BytesIO()
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': '正璽金屬工業委外加工交貨KPI統計',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': '正璽金屬工業',
            'company': '正璽金屬工業有限公司',
            'category': '委外加工交貨KPI統計',
            'keywords': '委外加工交貨KPI統計',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws = wb.add_worksheet("正璽金屬工業委外加工交貨KPI統計")

        ########################################
        title_format = wb.add_format()
        title_format.set_font_size(15)
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
        ###########################################
        date_format = wb.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(12)
        date_format.set_border(1)
        date_format.set_align('center')
        date_format.set_align('vcenter')



        titles = ['項次','供應商','委外加工單','產品料號', '應交日期', '實際交期' ,'應交數量', '交貨數量' , '達成率%','扣點']
        title_width = [5,25,15,20, 15, 15,15, 15, 10 ,10]

        row = 0

        col = 0
        out_header = "委外加工交貨達成率統計報告(區間:%s-%s)" % (self.start_date,self.end_date)
        ws.set_row(row, 30)
        ws.write(row,2,out_header,title_format)

        row += 1
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 15)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1
        myattsum = 0.00
        mystate=' '

        for line in out_rec:
            if line.date_due!=False:
                ws.write(row, 0, nitem, okc_content_format)
                ws.write(row, 1, line.quant_id.partner_id.name if line.quant_id.partner_id else ' ', okl_content_format)
                ws.write(row, 2, line.quant_id.outsub_id.name if line.quant_id.outsub_id else ' ', okl_content_format)
                ws.write(row, 3, line.quant_id.product_no.default_code if line.quant_id.product_no else ' ', okl_content_format)
                ws.write(row, 4, line.date_due if line.date_due else ' ', date_format)
                ws.write(row, 5, line.date_delivery if line.date_delivery else ' ', date_format)
                ws.write(row, 6, line.supply_num if line.supply_num else ' ',okc_content_format)
                ws.write(row, 7, line.delivery_num if line.delivery_num else ' ', okc_content_format)
                ws.write(row, 8, line.kpi_ratio if line.kpi_ratio else ' ', okc_content_format)
                ws.write(row, 9, line.kpi_deduction if line.kpi_deduction else ' ', okc_content_format)
                row += 1
                nitem += 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_acme_iot.excel_download']
        if mycount > 0:
            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        else:
            raise UserError("沒有符合的記錄可供匯出！")


        myviewid = self.env.ref('alldo_acme_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'outsuborder_kpi',
            'name': (u'委外加工交貨達成率統計報告'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_acme_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
