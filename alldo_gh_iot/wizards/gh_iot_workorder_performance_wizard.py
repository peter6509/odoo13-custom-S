# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class alldoghiotwkperformancewizard(models.TransientModel):
    _name = "alldo_gh_iot.wkorder_performance_wizard"

    wk_start_date =fields.Date(string="啟始日期",required=True)
    wk_end_date = fields.Date(string="截止日期",required=True)
    product_id = fields.Many2one('product.product',string="產品料號")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    iot_owner = fields.Many2one('hr.employee',string="作業者")


    def run_wk_performance(self):
        myprodid = 0
        if not self.product_id:
            myprodid = 0
        else:
            myprodid = self.product_id.id
        myownerid = 0
        if not self.iot_owner:
            myownerid = 0
        else:
            myownerid = self.iot_owner.id
        mynodeid = 0
        if not self.iot_node:
            mynodeid = 0
        else:
            mynodeid = self.iot_node.id
        self.env.cr.execute("""select genwkperformance('%s','%s',%d,%d,%d)""" % (self.wk_start_date,self.wk_end_date,myprodid,myownerid,mynodeid))
        self.env.cr.execute("""commit""")
        mywkrec = self.env['alldo_gh_iot.workorder_performance_list1'].search([])
        mycount = self.env['alldo_gh_iot.workorder_performance_list1'].search_count([])
        output = io.BytesIO()
        if not self.iot_owner:
            myxlsfilename = "工單生產數據表_(%s-%s)_ALL.xlsx" % (self.wk_start_date.strftime("%Y%m%d"), self.wk_end_date.strftime("%Y%m%d"))
            mysubject =  "工單生產數據表_(%s-%s)_ALL.xlsx" % (self.wk_start_date.strftime("%Y%m%d"), self.wk_end_date.strftime("%Y%m%d"))
        else:
            myxlsfilename =  "工單生產數據表_(%s-%s)_%s.xlsx" % (self.wk_start_date.strftime("%Y%m%d"), self.wk_end_date.strftime("%Y%m%d"),self.iot_owner.name)
            mysubject =  "工單生產數據表_(%s-%s)_%s.xlsx" % (self.wk_start_date.strftime("%Y%m%d"), self.wk_end_date.strftime("%Y%m%d"),self.iot_owner.name)

        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': '精宏機械工單生產效率表',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'JH',
            'company': '精宏機械股份有限公司',
            'category': '工單生產效率表',
            'keywords': '工單生產效率表',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("精宏機械工單生產效率表")
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

        titles = ['日期','工單編號', '機台','產品','工程別','啟始時間','截止時間','責任者','生產總數','材料不良','加工不良','標準量','達成率','總工時','產能/H']
        title_width = [20 ,30, 30 , 30, 20, 40, 40, 20, 20, 20 ,20 ,20 ,20 ,20 ,20]

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
            ws.write(row, 0, line.iot_date if line.iot_date else ' ', okl_content_format)
            ws.write(row, 1, line.wkorder_id.name if line.wkorder_id else ' ', okl_content_format)
            ws.write(row, 2, line.iot_node.name if line.iot_node else ' ', okl_content_format)
            ws.write(row, 3, line.product_no.default_code if line.product_no else ' ', okl_content_format)
            ws.write(row, 4, line.eng_type if line.eng_type else ' ', okl_content_format)
            ws.write(row, 5, line.iot_start if line.iot_start else ' ', okl_content_format)
            ws.write(row, 6, line.iot_end if line.iot_end else ' ', okl_content_format)
            ws.write(row, 7, line.iot_owner.name if line.iot_owner else ' ', okl_content_format)
            ws.write(row, 8, line.total_amount_num if line.total_amount_num else ' ', okc_content_format)
            ws.write(row, 9, line.material_ng_num if line.material_ng_num else ' ', okc_content_format)
            ws.write(row, 10, line.processing_ng_num if line.processing_ng_num else ' ', okc_content_format)
            ws.write(row, 11, line.std_num if line.std_num else ' ', okc_content_format)
            ws.write(row, 12, line.performance_rate if line.performance_rate else ' ', okc_content_format)
            ws.write(row, 13, line.iot_duration if line.iot_duration else ' ', okc_content_format)
            ws.write(row, 14, line.product_num if line.product_num else ' ', okc_content_format)
            row += 1
            nitem += 1

        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['alldo_gh_iot.excel_download']
        if mycount > 0:
            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        else:
            raise UserError("沒有工單生產記錄可供匯出！")

        myviewid = self.env.ref('alldo_gh_iot.view_alldo_excel_download_tree')

        return {
            'view_name': 'workorder_performance_list',
            'name': (u'工單生產數據匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
