# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class newebcustomexportjdwwizard(models.TransientModel):
    _name = "neweb_to_jdw.custom_export_wizard"
    _description = "客戶資料匯出給觔斗雲"

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.export_user = self.env.user.id

    cus_name = fields.Many2one('res.partner',string="客戶")
    start_date = fields.Date(string="異動起始日")
    end_date = fields.Date(string="異動截止日")
    export_user = fields.Many2one('res.users', string="匯出人員")
    export_date = fields.Datetime(string="匯出日期時間",default=datetime.today())

    def run_custom_export(self):
        if self.cus_name:
            mycusid = self.cus_name.id
            mycus_rec = self.env['res.partner'].search([('id', '=', mycusid)])
        else:
            self.env.cr.execute("""select getjdwexportcus('%s','%s')""" % (self.start_date,self.end_date))
            mycusid = self.env.cr.fetchall()
            mycus_rec = self.env['res.partner'].search([('id', 'in', mycusid)])

        output = io.BytesIO()

        myxlsfilename1 = "客戶資料_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
        mysubject = '客戶資料_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '客戶資料(匯出For筋斗雲)',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '客戶資料(匯出For筋斗雲)',
            'keywords': '客戶資料(匯出For筋斗雲)',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet("客戶資料(匯出For筋斗雲)")

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
        date_format = wb1.add_format({'num_format': 'yyyy-mm-dd'})
        date_format.set_font_size(15)
        date_format.set_border(1)
        date_format.set_font_color('black')
        date_format.set_align('right')
        date_format.set_align('vcenter')
        date_format.set_text_wrap()

        titles1 = ['公司客戶編號', '公司客戶名稱', '公司群組','客戶類型','負責業務','所屬部門','啟用狀態','統編','電話','傳真','服務地址','發票地址','備註','聯絡人1姓名','聯絡人1電話','聯絡人1通訊帳號']
        title_width = [20, 45, 20,20,20,20,20,20,20,20,45,45,20,30,30,30]

        row = 0

        mytitle = "(維護案)成本分析主檔"

        # ws1.write(row, 4, mytitle, title_format)
        # row += 2
        col = 0
        for title in titles1:
            ws1.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws1.set_row(row, 30)
            ws1.set_column(myloc, title_width[col])
            col += 1

        # ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in mycus_rec:


            ws1.write(row, 0, line.vat if line.vat else ' ', okl_content_format)
            ws1.write(row, 1, line.name if line.name else ' ', okl_content_format)
            ws1.write(row, 2, ' ', okl_content_format)
            ws1.write(row, 3, ' ', okl_content_format)
            self.env.cr.execute("""select getcussale(%d)""" % line.id)
            salename = self.env.cr.fetchone()[0]
            ws1.write(row,4, salename if salename else ' ',okl_content_format)
            ws1.write(row,5, ' ',okl_content_format)
            ws1.write(row,6,'啟用',okl_content_format)
            ws1.write(row, 7, line.vat if line.vat else ' ', okl_content_format)
            ws1.write(row, 8, line.phone if line.phone else ' ', okl_content_format)
            ws1.write(row, 9, line.fax if line.fax else ' ', okl_content_format)
            ws1.write(row, 10, line.street if line.street else ' ', okl_content_format)
            self.env.cr.execute("""select getcusinvaddr(%d)""" % line.id)
            invaddr = self.env.cr.fetchone()[0]
            ws1.write(row, 11, invaddr if invaddr else ' ', okl_content_format)
            ws1.write(row, 12, ' ', okl_content_format)
            self.env.cr.execute("""select getjdwcontact(%d)""" % line.id)
            jdwcontact = self.env.cr.fetchall()
            # c1 = jdwcontact[0][0]
            # c2 = jdwcontact[1][0]
            # c3 = jdwcontact[2][0]
            ws1.write(row, 13, jdwcontact[0][0] if jdwcontact[0][0] else ' ', okl_content_format)
            ws1.write(row, 14, jdwcontact[1][0] if jdwcontact[1][0] else ' ', okl_content_format)
            ws1.write(row, 15, jdwcontact[2][0] if jdwcontact[2][0] else ' ', okl_content_format)
            row += 1
            nitem += 1

        wb1.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()

        myrec = self.env['neweb_to_jdw.excel_download'].search([])
        myrec.create({'export_date':self.export_date,'export_owner':self.env.user.id,'download_type':'1','xls_file': myxlsfile1, 'xls_file_name': myxlsfilename1})

        myviewid = self.env.ref('neweb_to_jdw.view_jdw_download_tree')

        return {
            'view_name': 'neweb_custom_to_jdw',
            'name': ('客戶資料匯出給觔斗雲'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_to_jdw.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



