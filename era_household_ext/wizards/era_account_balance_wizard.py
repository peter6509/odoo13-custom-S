# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import datetime, pytz
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter

class EraAccountBalanceWizard(models.TransientModel):
    _name = "era.account_balance_wizard"
    _description = "案場房租費用結帳總表"

    project_no = fields.Many2one('era.household_house',string="案場名稱")

    def run_account_balance(self):
        myrec = self.env['era.household_member'].search([('house_id.house_id','=',self.project_no.id)],order='member_no')
        output = io.BytesIO()
        myxlsfilename = "ERA房租費用結帳總表(%s).xlsx" % (self.project_no.project_no)
        mysubject = 'ERA房租費用結帳總表(%s).xlsx' % (self.project_no.project_no)
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        wb.set_properties({
            'title': 'ERA房租費用結帳總表',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'ERA',
            'company': 'ERA',
            'category': '房租費用結帳總表',
            'keywords': '房租費用結帳總表',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
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
        okr_content_format = wb.add_format()
        okr_content_format.set_font_size(10)
        okr_content_format.set_border(1)
        okr_content_format.set_font_color('black')
        okr_content_format.set_align('right')
        okr_content_format.set_align('vcenter')
        okr_content_format.set_text_wrap()
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
        currency_format = wb.add_format({'num_format': '###,###,##0'})
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


        titles = ['項次', '房號', '租戶', '起租日', '退租日', '應繳日期', '每月租金/管理費','合計應繳租金/管理費(A)','合計已繳租金/管理費(B)','結算應繳租金/管理費餘額(A-B)','合計應繳電費(C)','合計已繳電費(D)','結算應繳電費餘額(C-D)','總計應繳餘額((A-B)+(C-D))']
        title_width = [5, 5, 20, 15, 15, 15, 20,25,25,25,25,25,25,25]
        nnum = 1
        ws = {}
        ws = wb.add_worksheet("ERA房租費用結帳總表(%s).xlsx" % (self.project_no.project_no))
        mytitle = "ERA房租費用結帳總表(%s)" % (self.project_no.project_no)
        mytitle1 = "ERA房租費用結帳總表(%s)" % (self.project_no.project_no)
        ########################################
        row = 0
        col = 0
        #ws.write(row, col, mytitle, title_format)
        row += 1
        ws.set_row(row, 20)
        ws.write(row, 5, mytitle1, title_format)
        row += 2
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 15)
            ws.set_column(myloc, title_width[col])
            col += 1
            ws.freeze_panes(row + 1, 0)
        nitem = 1
        for rec in myrec:
            row += 1
            ws.write(row, 0, nitem, okc_content_format)
            ws.write(row, 1, rec.house_id.house_no if rec.house_id else ' ', okl_content_format)
            ws.write(row, 2, rec.member_name if rec.member_name else ' ', okl_content_format)
            ws.write(row, 3, rec.period_start if rec.period_start else ' ',date_format )
            ws.write(row, 4, rec.period_end if rec.period_end else ' ', date_format)
            ws.write(row, 5, rec.now_ym if rec.now_ym else ' ', date_format)
            ws.write(row, 6, rec.period_subtot if rec.period_subtot else ' ', currency_format)
            ws.write(row, 7, rec.period_totrent if rec.period_totrent else ' ', currency_format)
            ws.write(row, 8, rec.period_totrentpay if rec.period_totrentpay else ' ', currency_format)
            ws.write(row, 9, rec.now_totrent_balance if rec.now_totrent_balance else ' ', currency_format)
            ws.write(row, 10, rec.period_totscale if rec.period_totscale else ' ', currency_format)
            ws.write(row, 11, rec.period_totscalepay if rec.period_totscalepay else ' ', currency_format)
            ws.write(row, 12, rec.now_totscalebalance if rec.now_totscalebalance else ' ', currency_format)
            ws.write(row, 13, rec.now_totbalance if rec.now_totbalance else ' ', currency_format)

            nitem = nitem + 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()
        myrec = self.env['era.excel_download']

        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, })
        myviewid = self.env.ref('era_household.era_excel_download_tree')

        return {
            'view_name': 'era_excel_download',
            'name': (u'房租費用結帳總表'),
            'type': 'ir.actions.act_window',
            'res_model': 'era.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
