# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class NewebRPSWizard(models.TransientModel):
    _name = "neweb.rps_wizard"
    _description = "申購-採購-進貨狀態查詢精靈"

    rps_type = fields.Selection([('1','輸入單號'),('2','輸入申購日期區間')],string="搜尋模式",required=True,default='1')
    require_no = fields.Char(string="申購單號(模糊搜尋)")
    emp_name = fields.Many2one('res.users', string=u"申請人", default=lambda self: self.env.uid)
    start_date = fields.Date(string="起始日期")
    end_date = fields.Date(string="截止日期")
    display_type = fields.Selection([('1','畫面顯示'),('2','匯出EXCEL')],string="輸出模式",default='1')

    def run_rps_search(self):
        if self.rps_type=='1':
            if not self.require_no:
                raise UserError("""申購單號不能為空值""")
            if self.emp_name:
                self.env.cr.execute("""select genrpsdata1emp('%s',%d)""" % (self.require_no,self.emp_name.id))
                self.env.cr.execute("""commit""")
            else:
                self.env.cr.execute("""select genrpsdata1('%s')""" % self.require_no)
                self.env.cr.execute("""commit""")
        else:
            if not self.start_date or not self.end_date:
                raise UserError("""起迄日期輸入不完整""")
            if self.emp_name:
                self.env.cr.execute("""select genrpsdata2emp('%s','%s',%d)""" % (self.start_date,self.end_date,self.emp_name.id))
                self.env.cr.execute("""commit""")
            else:
                self.env.cr.execute("""select genrpsdata2('%s','%s')""" % (self.start_date,self.end_date))
                self.env.cr.execute("""commit""")
        if self.display_type=='1':
            myviewid = self.env.ref('neweb_purchase.view_rps_schedule_tree')
            return {
                'view_name': '申購-採購-進貨狀態查詢',
                'name': ('申購-採購-進貨狀態查詢'),
                'type': 'ir.actions.act_window',
                'res_model': 'neweb.rps_schedule',
                'view_id': myviewid.id,
                'flags': {'action_buttons': False},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'main'}
        else:
            myrpsrec = self.env['neweb.rps_schedule'].search([])
            output = io.BytesIO()
            if self.rps_type=='1':
                myxlsfilename = "申購-採購-進貨狀態_%s.xlsx" % (self.require_no)
                mysubject = "申購-採購-進貨狀態_%s.xlsx" % (self.require_no)
                rpsno = self.require_no
                rpssedate = ' '
            else:  ## S1
                myxlsfilename = "申購-採購-進貨狀態_%s-%s.xlsx" % (self.start_date.strftime("%Y%m%d"),self.end_date.strftime("%Y%m%d"))
                mysubject = "申購-採購-進貨狀態_%s-%s.xlsx" % (self.start_date.strftime("%Y%m%d"),self.end_date.strftime("%Y%m%d"))
                rpsno = ' '
                rpssedate = self.start_date.strftime("%Y%m%d")+ 'to' +self.end_date.strftime("%Y%m%d")
            wb = xlsxwriter.Workbook(output, {'in_memory': True})

            wb.set_properties({
                'title': '申購-採購-進貨狀態',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '申購-採購-進貨狀態',
                'keywords': '申購-採購-進貨狀態',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})
            ws = wb.add_worksheet("申購-採購-進貨狀態")


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


            titles1 = ['申購單號', '機種-機型/料號', '庫存料號', '規格說明', '申購日期', '申購數量', '預算總價','採購單號', '採購日期', '採購數量', '供應商','進貨單據','收貨數量', '進貨驗收日']
            title_width = [15, 20, 15, 50, 15, 15,15, 15, 15, 15, 50,25, 15,15]

            row = 0

            col = 0
            for title in titles1:
                ws.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws.set_row(row, 30)
                ws.set_column(myloc, title_width[col])
                col += 1

            # ws1.freeze_panes(row + 1, 0)
            row += 1
            nitem = 1

            for line in myrpsrec:
                ws.write(row, 0, line.rp_no.name if line.rp_no else ' ', okl_content_format)
                ws.write(row, 1, line.rp_modeltype if line.rp_modeltype else ' ', okl_content_format)
                ws.write(row, 2, line.rp_pid.default_code if line.rp_pid else ' ', okl_content_format)
                ws.write(row, 3, line.rp_pitemspec if line.rp_pitemspec else ' ', okl_content_format)
                ws.write(row, 4, line.rp_date if line.rp_date else ' ', date_format)
                ws.write(row, 5, line.rp_num if line.rp_num else ' ', okc_content_format)
                ws.write(row, 6, line.rp_budget if line.rp_budget else ' ', currency_format)
                ws.write(row, 7, line.po_no.name if line.po_no else ' ', okl_content_format)
                ws.write(row, 8, line.po_date if line.po_date else ' ', date_format)
                ws.write(row, 9, line.po_num if line.po_num else ' ', okc_content_format)
                ws.write(row, 10, line.po_partner.name if line.po_partner else ' ', okl_content_format)
                ws.write(row, 11, line.stockin_no.name if line.stockin_no else ' ', okl_content_format)
                ws.write(row, 12, line.stockin_num if line.stockin_num else ' ', okc_content_format)
                ws.write(row, 13, line.stockin_date if line.stockin_date else ' ', date_format)
                row += 1
                nitem += 1

            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()


            myrpsrec = self.env['neweb.rps_download']
            myrpsrec.create({'rps_no':rpsno,'rps_sedate':rpssedate,'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})

            myviewid = self.env.ref('neweb_purchase.view_neweb_rps_download_tree')
            return {
                'view_name': '申購-採購-進貨狀態',
                'name': ('申購-採購-進貨狀態'),
                'type': 'ir.actions.act_window',
                'res_model': 'neweb.rps_download',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'main'}



