# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class GhiotCusStocklistWizard(models.TransientModel):
    _name = "alldo_gh_iot.cus_stocklist_wizard"
    _description = "客戶庫存表"

    cus_no = fields.Many2one('res.partner',string="客戶",required=True)
    list_type = fields.Selection([('1','畫面顯示'),('2','匯出Excel')],string="產出模式",required=True)
    run_desc = fields.Char(string="匯出說明",required=True)

    def run_cusstocklist(self):
        self.env.cr.execute("""select gencusstocklist(%d)""" % self.cus_no.id)
        self.env.cr.execute("""commit""")
        if self.list_type=='1':
            myrec = self.env['alldo_gh_iot.cus_stocklist']
            myviewid = self.env.ref('alldo_gh_iot.view_ghiot_cus_stocklist_tree')
            return {
                'view_name': '客戶庫存表',
                'name': ('客戶庫存表'),
                'type': 'ir.actions.act_window',
                'res_model': 'alldo_gh_iot.cus_stocklist',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'main'}
        elif self.list_type=='2':
            myrec = self.env['alldo_gh_iot.cus_stocklist'].search([])
            mycount = self.env['alldo_gh_iot.cus_stocklist'].search_count([])
            output = io.BytesIO()
            myxlsfilename = "客戶庫存表_%s_%s.xlsx" % (self.cus_no.name, datetime.now().strftime("%Y%m%d"))
            mysubject = "客戶庫存表_%s_%s.xlsx" % (self.cus_no.name, datetime.now().strftime("%Y%m%d"))
            wb = xlsxwriter.Workbook(output, {'in_memory': True})
            wb.set_properties({
                'title': '精宏機械客戶庫存表',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'JH',
                'company': '精宏機械股份有限公司',
                'category': '精宏機械客戶庫存表',
                'keywords': '精宏機械客戶庫存表',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})
            ws = wb.add_worksheet("精宏機械客戶庫存表")
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
            row = 1
            col = 0
            ws.write(row,col,'客戶:%s' % self.cus_no.name, head_format)
            col=6
            ws.write(row,col,'列表日:%s' % datetime.now().strftime("%Y%m%d"),date_format)

            row += 2
            col = 0

            titles = ['項次', '料號', '倉別', '數量', '儲位', '最後異動日','備註']
            title_width = [20, 50, 30, 30, 40, 30, 50]
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
            for line in myrec:
                ws.write(row, 0, nitem, okl_content_format)
                ws.write(row, 1, line.prod_no.name if line.prod_no else ' ', okl_content_format)
                ws.write(row, 2, line.stock_loc.name if line.stock_loc else ' ', okl_content_format)
                ws.write(row, 3, line.stock_num if line.stock_num else ' ', okc_content_format)
                ws.write(row, 4, line.rack_loc if line.rack_loc else ' ', okl_content_format)
                ws.write(row, 5, line.last_update if line.last_update else ' ', date_format)
                ws.write(row, 6, line.memo if line.memo else ' ', okl_content_format)
                row += 1
                nitem += 1

            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()
            myrec = self.env['alldo_gh_iot.excel_download']
            if mycount > 0:
                myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'run_desc': self.run_desc})
            else:
                raise UserError("沒有客戶庫存記錄可供匯出！")

            myviewid = self.env.ref('alldo_gh_iot.view_alldo_excel_download_tree')

            return {
                'view_name': 'cusstock_list',
                'name': (u'客戶庫存記錄匯出'),
                'type': 'ir.actions.act_window',
                'res_model': 'alldo_gh_iot.excel_download',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'main'}




