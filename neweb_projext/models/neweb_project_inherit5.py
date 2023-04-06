# -*- coding: utf-8 -*-
# Author : Peter Wu


import io

from odoo import models,fields,api
from odoo.exceptions import UserError
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
from io import BytesIO
import base64,xlsxwriter



class saleorderexceldownload(models.Model):
    _name = "neweb.saleorder_excel_download"
    _order = "create_date desc"

    xls_file = fields.Binary(string="Download File",attachment=False)
    xls_file_name = fields.Char(string="File Description")
    run_desc = fields.Char(string="Export Description")



class newebsaleorderinherit5(models.Model):
    _inherit = "sale.order"


    def saleorder_export(self):
        myid = self.env.context.get("saleorderid")
        myrec = self.env['neweb.sitem_list'].search([('sitem_id', '=', myid)])
        myrec1 = self.env['sale.order'].search([('id', '=', myid)])
        myxlsfilename = "(報價單：%s)-%s.xlsx" % (myrec1.name, myrec1.partner_id.name)

        output = io.BytesIO()

        mysubject = "(報價單：%s)-%s.xlsx" % (myrec1.name, myrec1.partner_id.name)

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '專案資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '報價單',
            'keywords': '報價單',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet("報價單主檔")

        ########################################
        title_format = wb1.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb1.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb1.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb1.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb1.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb1.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################

        titles1 = ['產品組別', '項次', '品牌', '共契組別-項次', '機型-機種/料號','機型名稱', '序號', '維護期間', '規格說明', '數量', '優惠單價', '優惠總價', '成本單價', '報價廠商', '成本類型' , '成本 * 數量', '毛利', '毛利率', '部門']
        title_width = [36, 18, 36, 36 , 72, 36,36, 72, 108, 18,36,36,36,36,36,36,36,18,36]

        row = 0

        mytitle = "報價單主檔"

        col = 0
        for title in titles1:
            ws1.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws1.set_row(row, 30)
            ws1.set_column(myloc, title_width[col])
            col += 1

        ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in myrec:
            s1 = line.sitem_item            # 項次
            s2 = line.sitem_brand.name      # 品牌
            s3 = line.sitem_modeltype       # 機型-機種/料號
            s4 = line.sitem_modeltype1      # 機型名稱
            s5 = line.sitem_serial          # 序號
            s6 = line.newebmaindate         # 維護期間
            s7 = line.sitem_desc            # 規格說明
            s8 = line.sitem_num             # 數量
            s9 = line.sitem_price           # 優惠單價
            s10 = line.sitem_cost            # 成本單價
            s11 = line.cost_dept            # 部門
            s12 = line.cost_type            # 成本類型

            ws1.write(row, 0, ' ', okl_content_format)
            ws1.write(row, 1, (s1 if s1 else ' '), okl_content_format)
            ws1.write(row, 2, (s2 if s2 else ' '), okl_content_format)
            ws1.write(row, 3, ' ', okl_content_format)
            ws1.write(row, 4, (s3 if s3 else ' '), okl_content_format)
            ws1.write(row, 5, (s4 if s4 else ' '), okl_content_format)
            ws1.write(row, 6, (s5 if s5 else ' '), okl_content_format)
            ws1.write(row, 7, (s6 if s6 else ' '), okl_content_format)
            ws1.write(row, 8, (s7 if s7 else ' '), okl_content_format)
            ws1.write(row, 9, (round(s8) if s8 else 0), okl_content_format)
            ws1.write(row, 10, (round(s9) if s9 else 0), okl_content_format)
            ws1.write(row, 11,  ' ', okl_content_format)
            ws1.write(row, 12, (round(s10) if s10 else 0), okl_content_format)
            ws1.write(row, 13, ' ', okl_content_format)
            ws1.write(row, 14, (s12.name if s12 else ' '), okl_content_format)
            ws1.write(row, 15, ' ', okl_content_format)
            ws1.write(row, 16, ' ', okl_content_format)
            ws1.write(row, 17, ' ', okl_content_format)
            ws1.write(row, 18, (s11.name if s11 else ' '), okl_content_format)
            row += 1

        wb1.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()

        output = BytesIO()
        myrec = self.env['neweb.saleorder_excel_download']

        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid = self.env.ref('neweb_projext.saleorder_excel_download_tree')

        return {
            'view_name': 'saleorderexcelwizard',
            'name': ('匯出報價單明細內容:%s' % myxlsfilename),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb.saleorder_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'self'}



