# -*- coding: utf-8 -*-
# Author : Peter Wu

import io
import base64
from odoo import models,fields,api
from odoo.exceptions import UserError
from datetime import datetime,timedelta,date
import xlsxwriter

class NewebAcceptanceAlertWizard(models.TransientModel):
    _name = "neweb_acceptance.alert_wizard"

    proj_sale = fields.Many2one('hr.employee',string="業務員")
    proj_sdate = fields.Date(string="專案成立起始日",required=True)
    proj_edate = fields.Date(string="專案成立截止日",required=True)

    @api.onchange('start_date')
    def onchangeuid(self):
        myids=[]
        self.env.cr.execute("""select get_proj_sale()""")
        myids1 = self.env.cr.fetchall()
        for rec in myids1:
            myids.append(rec[0])
        res = {}
        res['domain'] = {'proj_sale': [('id', 'in', myids)]}
        return res

    def run_acceptance_alert(self):
        if not self.proj_sale:
            mysaleid = 0
        else:
            mysaleid = self.proj_sale.id
        if (self.proj_sdate and not self.proj_edate) or (not self.proj_sdate and self.proj_edate) :
            raise UserError("""專案日期區間起迄必須同時輸入""")
        if not self.proj_sdate:
            myprojsdate = '2022-01-01'
        else :
            myprojsdate = self.proj_sdate
        if not self.proj_edate:
            myprojedate = fields.Date.today()
        else:
            myprojedate = self.proj_edate
        self.env.cr.execute("""select genacceptancelist4(%d,'%s','%s')""" % (mysaleid,self.proj_sdate,self.proj_edate))
        self.env.cr.execute("""commit""")
        myrec = self.env['neweb_acceptance.acc_list'].search([])
        myrec.sorted(key=lambda r:(r.proj_sale,r.project_no,r.stockout_no,r.accym))

        # 排序 按 業務,專案編號 出貨單 年月
        output = io.BytesIO()
        # if (not self.start_date) or (not self.end_date):
        #     mydate = "ALL"
        # else:
        #     mydate = "%s - %s" % (self.start_date.strftime("%Y%m%d"),self.end_date.strftime("%Y%m%d"))
        if not self.proj_sale:
            myxlsfilename1 = "存貨追蹤表(異常).xlsx"
            mysubject = '存貨追蹤表(異常)'
        else:
            myxlsfilename1 = "存貨追蹤表(異常)-%s.xlsx" % self.proj_sale.name
            mysubject = '存貨追蹤表(異常)-%s' % self.proj_sale.name

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '存貨追蹤表(異常)',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '存貨追蹤表(異常)',
            'keywords': '存貨追蹤表(異常)',
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

        titles1 = ['填單日', '業務', '採購單號','出貨單號','專案編號','客戶名稱','客戶專案/標案名稱','產品料號','機種-機型/料號','規格說明','數量','供應商','預計驗收日','收貨日期','出貨日期','結案日期','狀態','年月']
        title_width = [10,15,10,15,15,10,25,10,25,40,10,10,10,10,10,10,25,10]

        row = 0
        # mytitle = "客戶專案貨品狀態情況表"
        ws1.set_row(row, 30)
        ws1.write(row, 6, mysubject, title_format)
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
            if line.projsaleitem_status=='1':
                mystatus='貨在公司待貨齊'
            elif line.projsaleitem_status=='2':
                mystatus = '貨在公司待出貨'
            elif line.projsaleitem_status == '3':
                mystatus = '貨在公司測試安裝中'
            elif line.projsaleitem_status == '4':
                mystatus = '貨在客戶端待貨齊'
            elif line.projsaleitem_status == '5':
                mystatus = '貨在客戶端待裝機'
            elif line.projsaleitem_status == '6':
                mystatus = '貨在客戶端裝機中'
            elif line.projsaleitem_status == '7':
                mystatus = '貨在客戶端待驗收'
            elif line.projsaleitem_status == '8':
                mystatus = '貨在客戶端驗收中'
            else:
                mystatus = ' '

            ws1.write(row, 0, line.keyin_date if line.keyin_date else ' ', date_format)
            ws1.write(row, 1, line.proj_sale.name if line.proj_sale else ' ', okl_content_format)
            ws1.write(row, 2, line.purchase_no if line.purchase_no else ' ', okc_content_format)
            ws1.write(row, 3, line.stockout_no.name if line.stockout_no else ' ', okc_content_format)
            ws1.write(row, 4, line.project_no.name if line.project_no else ' ', okc_content_format)
            ws1.write(row, 5, line.cus_name.comp_sname if line.cus_name else ' ', okl_content_format)
            ws1.write(row, 6, line.cus_project if line.cus_project else ' ', okl_content_format)
            ws1.write(row, 7, line.prod_no if line.prod_no else ' ', okl_content_format)
            ws1.write(row, 8, line.prod_modeltype if line.prod_modeltype else ' ', okl_content_format)
            ws1.write(row, 9, line.prod_desc if line.prod_desc else ' ', okl_content_format)
            ws1.write(row, 10, line.prod_num if line.prod_num else ' ', okc_content_format)
            ws1.write(row, 11, line.supplier if line.supplier else ' ', okl_content_format)
            ws1.write(row, 12, line.acceptanced_date1 if line.acceptanced_date1 else ' ', date_format)
            ws1.write(row, 13, line.stockin_date if line.stockin_date else ' ', date_format)
            ws1.write(row, 14, line.stockout_date if line.stockout_date else ' ', date_format)
            ws1.write(row, 15, line.acceptanced_date2 if line.acceptanced_date2 else ' ', date_format)
            ws1.write(row, 16, mystatus , okl_content_format)
            ws1.write(row, 17, line.accym if line.accym else ' ', okc_content_format)

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



