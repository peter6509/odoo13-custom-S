# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class newebunexportinvoiceopen(models.Model):
    _name = "neweb_chi_invoicing.un_export_invoiceopen"
    _description = "生成未匯出銷項數據暫存主檔"
    _rec_name = "export_user"

    export_user = fields.Many2one('res.users', string="匯出人員", compute='_get_current_user', store=True)
    export_date = fields.Date(string="匯出日期")
    export_line = fields.One2many('neweb_chi_invoicing.un_export_invoiceopenline','export_id')

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.export_user = self.env.user.id

    def selectitemall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_invoiceopenline'].search([])
        for rec in myrec:
            rec.update({'selectyn': True})

    def selectitemallno(self):
        myrec = self.env['neweb_chi_invoicing.un_export_invoiceopenline'].search([])
        for rec in myrec:
            rec.update({'selectyn': False})


    def selectall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_invoiceopenline'].search([])

    def selectbtn(self):
        mytype = self.env.context.get('neweb_export_type',False)
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        myoutrec =[]
        mychisalesno=''
        mypurchaseno = ''
        mypackagesalesrec = self.env['neweb_chi_invoicing.package_sales']
        for myrec in self.export_line:
            if mytype=='M1':
                self.env.cr.execute("""select genincomeoutcomenom1(%d)""" % (myrec.project_no.id))
                self.env.cr.execute("commit")
            else:    ## S1
                self.env.cr.execute("""select genincomeoutcomeno1(%d)""" % (myrec.project_no.id))
                self.env.cr.execute("commit")
            output = io.BytesIO()

            if mytype=='M1':
                mysalerec = self.env['neweb_chi_invoicing.export_sales_log'].search([('proj_no', '=', myrec.project_no.id),('chi_outcome_date','=',myrec.invoice_date),('chi_product', '=', 'ZZB00000001')], order='chi_origin_id')
                # 原先排序 chi_sales_no
            else:      ## S1
                mysalerec = self.env['neweb_chi_invoicing.export_sales_log'].search([('proj_no', '=', myrec.project_no.id)],order='saleitem_seq')
            if mysalerec:
                myprojno = mysalerec[0].chi_project_no
                if mytype == 'M1':
                    myxlsfilename3 = "SALES_MAINTENANCE_%s_%s.xlsx" % (myrec.project_no.name, datetime.now().strftime("%Y%m%d"))
                    mysubject = 'SALES_MAINTENANCE_%s_%s.xlsx' % (myrec.project_no.name, datetime.now().strftime("%Y%m%d"))
                else:       ## S1
                    myxlsfilename3 = "SALES_%s_%s.xlsx" % (myrec.project_no.name,datetime.now().strftime("%Y%m%d"))
                    mysubject = 'SALES_%s_%s.xlsx' % (myrec.project_no.name,datetime.now().strftime("%Y%m%d"))

                wb3 = xlsxwriter.Workbook(output, {'in_memory': True})
                if mytype == 'M1':
                    wb3.set_properties({
                        'title': '專案銷項資訊(維護)',
                        'subject': mysubject,
                        'author': '%s' % self.env.user.name,
                        'manager': 'NEWEB INFO',
                        'company': '藍新資訊股份有限公司',
                        'category': '進銷存專案數據(維護)',
                        'keywords': '進銷存專案數據(維護)',
                        'created': datetime.now(),
                        'comments': 'Created By Odoo'})
                    ws3 = wb3.add_worksheet("進銷存成本分析(維護)銷項憑證檔")
                else:  ## S1
                    wb3.set_properties({
                        'title': '專案銷項資訊',
                        'subject': mysubject,
                        'author': '%s' % self.env.user.name,
                        'manager': 'NEWEB INFO',
                        'company': '藍新資訊股份有限公司',
                        'category': '進銷存專案數據',
                        'keywords': '進銷存專案數據',
                        'created': datetime.now(),
                        'comments': 'Created By Odoo'})
                    ws3 = wb3.add_worksheet("進銷存成本分析銷項憑證檔")



                ########################################
                title_format = wb3.add_format()
                title_format.set_font_size(30)
                title_format.set_bold()
                title_format.set_underline(2)
                title_format.set_font_color('black')
                title_format.set_align('left')
                title_format.set_align('vcenter')
                ########################################
                head_format = wb3.add_format()
                head_format.set_font_size(15)
                head_format.set_border(2)
                head_format.set_font_color('yellow')
                head_format.set_fg_color('blue')
                head_format.set_align('center')
                head_format.set_align('vcenter')
                ########################################
                okc_content_format = wb3.add_format()
                okc_content_format.set_font_size(15)
                okc_content_format.set_border(1)
                okc_content_format.set_font_color('black')
                okc_content_format.set_align('center')
                okc_content_format.set_align('vcenter')
                okc_content_format.set_text_wrap()
                #########################################

                okl_content_format = wb3.add_format()
                okl_content_format.set_font_size(15)
                okl_content_format.set_border(1)
                okl_content_format.set_font_color('black')
                okl_content_format.set_align('left')
                okl_content_format.set_align('vcenter')
                okl_content_format.set_text_wrap()

                #########################################
                ngc_content_format = wb3.add_format()
                ngc_content_format.set_font_size(15)
                ngc_content_format.set_border(1)
                ngc_content_format.set_font_color('red')
                ngc_content_format.set_italic()
                ngc_content_format.set_fg_color('yellow')
                ngc_content_format.set_align('center')
                ngc_content_format.set_align('vcenter')
                ngc_content_format.set_text_wrap()
                ##########################################
                ngl_content_format = wb3.add_format()
                ngl_content_format.set_font_size(15)
                ngl_content_format.set_border(1)
                ngl_content_format.set_font_color('red')
                ngl_content_format.set_italic()
                ngl_content_format.set_fg_color('yellow')
                ngl_content_format.set_align('left')
                ngl_content_format.set_align('vcenter')
                ngl_content_format.set_text_wrap()
                ##########################################
                currency_format = wb3.add_format({'num_format': '###,###,##0.00'})
                currency_format.set_font_size(15)
                currency_format.set_border(1)
                currency_format.set_font_color('black')
                currency_format.set_align('right')
                currency_format.set_align('vcenter')
                currency_format.set_text_wrap()
                ##########################################
                date_format = wb3.add_format({'num_format': 'yyyy-mm-dd'})
                date_format.set_font_size(15)
                date_format.set_border(1)
                date_format.set_font_color('black')
                date_format.set_align('right')
                date_format.set_align('vcenter')
                date_format.set_text_wrap()


                if mytype == 'M1':
                    titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '倉庫編號', '所屬專案', '自定欄二', '收款日期', '產品編號','品名規格',
                               '數量', '單價', '備註']
                    title_width = [20, 15, 15, 15, 20, 20, 30, 20, 20, 30, 15, 20, 60]

                    row = 0

                    col = 0
                    for title in titles1:
                        ws3.write(row, col, title, head_format)
                        myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                        ws3.set_row(row, 30)
                        ws3.set_column(myloc, title_width[col])
                        col += 1

                    # ws1.freeze_panes(row + 1, 0)
                    row += 1
                    nitem = 1

                    for line in mysalerec:
                        mychisalesno = line.chi_sales_no
                        # mypurchaseno = line.chi_purchase_no.id
                        ws3.write(row, 0, line.chi_sales_no if line.chi_sales_no else ' ', okl_content_format)
                        ws3.write(row, 1, line.chi_outcome_date if line.chi_outcome_date else ' ', date_format)
                        ws3.write(row, 2, line.chi_sales_vat if line.chi_sales_vat else ' ', okl_content_format)
                        ws3.write(row, 3, line.chi_currency_type, okl_content_format)
                        # ws3.write(row, 4, line.proj_sale_name if line.proj_sale_name else ' ', okl_content_format)
                        ws3.write(row, 4, line.chi_wh, okl_content_format)
                        ws3.write(row, 5, line.chi_project_no, okl_content_format)
                        ws3.write(row, 6, line.chi_cus_order if line.chi_cus_order else ' ', okl_content_format)
                        ws3.write(row, 7, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                        ws3.write(row, 8, 'ZZB00000001', okl_content_format)
                        ws3.write(row, 9,  line.chi_sale_spec if line.chi_sale_spec else ' ', okl_content_format)
                        ws3.write(row, 10, '1',okc_content_format)
                        ws3.write(row, 11, round(line.chi_sales_price, 2) if line.chi_sales_price else 0,
                                  currency_format)
                        ws3.write(row, 12, line.chi_sale_memo if line.chi_sale_memo else ' ', okl_content_format)

                        myckcount =  self.env['neweb_chi_invoicing.package_sales'].search_count([('sales_no','=',line.chi_sales_no)])
                        if myckcount==0:
                            mypackagesalesrec.create(
                                {'sales_no': line.chi_sales_no, 'sales_outdate': line.chi_outcome_date,
                                 'sales_cusvat': line.chi_sales_vat, 'sales_currency': line.chi_currency_type,
                                 'sales_man': line.proj_sale_name, 'sales_wh': line.chi_wh,
                                 'sales_proj_no': line.chi_project_no, 'sales_cus_order': line.chi_cus_order,
                                 'sales_paymentdate': line.chi_paymentdate, 'sales_prod': 'ZZB00000001',
                                 'sales_num': 1,
                                 'sale_spec': line.chi_sale_spec ,
                                 'sales_price': round(line.chi_sales_price, 0),
                                 'sales_memo': line.chi_sale_memo})
                        row += 1
                        nitem += 1
                else:  ## S1
                    titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '業務人員', '倉庫編號', '所屬專案', '自定欄二', '收款日期', '產品編號', '數量', '單價','備註']
                    title_width = [20, 15, 15, 15, 20, 15, 30, 20, 15, 20, 15, 20,60]

                    row = 0

                    col = 0
                    for title in titles1:
                        ws3.write(row, col, title, head_format)
                        myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                        ws3.set_row(row, 30)
                        ws3.set_column(myloc, title_width[col])
                        col += 1

                    # ws1.freeze_panes(row + 1, 0)
                    row += 1
                    nitem = 1

                    for line in mysalerec:
                        mychisalesno = line.chi_sales_no
                        # mypurchaseno = line.chi_purchase_no.id
                        ws3.write(row, 0, line.chi_sales_no if line.chi_sales_no else ' ', okl_content_format)
                        ws3.write(row, 1, line.chi_outcome_date if line.chi_outcome_date else ' ', date_format)
                        ws3.write(row, 2, line.chi_sales_vat if line.chi_sales_vat else ' ', okl_content_format)
                        ws3.write(row, 3, line.chi_currency_type, okl_content_format)
                        ws3.write(row, 4, line.proj_sale_name if line.proj_sale_name else ' ', okl_content_format)
                        ws3.write(row, 5, line.chi_wh, okl_content_format)
                        ws3.write(row, 6, line.chi_project_no, okl_content_format)
                        ws3.write(row, 7, line.chi_cus_order if line.chi_cus_order else ' ', okl_content_format)
                        ws3.write(row, 8, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                        ws3.write(row, 9, line.chi_product if line.chi_product else ' ', okl_content_format)
                        ws3.write(row, 10, round(line.chi_sales_num, 0) if line.chi_sales_num else 0, okc_content_format)
                        ws3.write(row, 11, round(line.chi_sales_price, 2) if line.chi_sales_price else 0,currency_format)
                        ws3.write(row, 12, line.chi_sale_memo if line.chi_sale_memo else ' ',okl_content_format)

                        # myckcount = self.env['neweb_chi_invoicing.package_sales'].search_count([('sales_no', '=', line.chi_sales_no)])
                        # if myckcount == 0:
                        mypackagesalesrec.create(
                            {'sales_no': line.chi_sales_no, 'sales_outdate': line.chi_outcome_date,
                             'sales_cusvat': line.chi_sales_vat,'sales_currency': line.chi_currency_type,
                             'sales_man':line.proj_sale_name, 'sales_wh': line.chi_wh,
                             'sales_proj_no': line.chi_project_no,'sales_cus_order':line.chi_cus_order,
                             'sales_paymentdate': line.chi_paymentdate, 'sales_prod': line.chi_product,
                             'sales_num': round(line.chi_sales_num, 0),
                             'sales_price': round(line.chi_sales_price, 0),
                             'sales_memo':line.chi_sale_memo,'saleitem_seq':line.saleitem_seq})
                        row += 1
                        nitem += 1

                wb3.close()
                output.seek(0)
                myxlsfile3 = base64.standard_b64encode(output.getvalue())
                output.close()

                myprojcount = self.env['neweb_chi_invoicing.invoiceopen_excel_download'].search_count([('project_no', '=', myrec.project_no.id)])
                if myprojcount > 0:
                    myrec = self.env['neweb_chi_invoicing.invoiceopen_excel_download'].search([('project_no', '=', myrec.project_no.id)])
                    myrec.write({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3})
                    self.env.cr.execute("""update neweb_chi_invoicing_invoiceopen_excel_download set invoicing_date='%s',invoicing_owner=%d where project_no=%d""" % (
                            self.export_date, myempid,myrec.project_no.id))
                    self.env.cr.execute("""commit""")

                else:
                    myrec = self.env['neweb_chi_invoicing.invoiceopen_excel_download']
                    myrec.create({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3, 'project_no': myrec.project_no.id,'chi_sales_no':mychisalesno})
                    self.env.cr.execute("""update neweb_chi_invoicing_invoiceopen_excel_download set invoicing_date='%s',invoicing_owner=%d where project_no=%d""" % (
                            self.export_date, myempid, myrec.project_no.id))
                    self.env.cr.execute("""commit""")

                self.env.cr.execute("""select saleinvgenstatus(%d,%d)""" % (myrec.project_no.id,myempid))
                self.env.cr.execute("""commit""")

        ########################## 整包輸出作業 #########################
        mytoday = date.today()
        # mytd = mytoday.strftime('%Y%m%d')
        self.env.cr.execute("""select getsetnum('%s','%s')""" % (mytoday,'2'))
        myres = self.env.cr.fetchone()[0]
        mystr = str(myres).zfill(3)
        mypackagesalesrec = self.env['neweb_chi_invoicing.package_sales'].search([],order="sales_no")
        if mytype == 'M1':
            myxlsfilename = "SALES_MAIN_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)
            mysubject = "SALES_MAIN_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)
        else:
            myxlsfilename = "SALES_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"), mystr, self.export_user.name)
            mysubject = "SALES_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"), mystr, self.export_user.name)
        output1 = io.BytesIO()

        wb = xlsxwriter.Workbook(output1, {'in_memory': True})
        if mytype == 'M1':
            wb.set_properties({
                'title': '專案銷項資訊(維護)',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據(維護)',
                'keywords': '進銷存專案數據(維護)',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws = wb.add_worksheet("進銷存(維護)成本分析整批銷項憑證檔")
        else:
            wb.set_properties({
                'title': '專案銷項資訊',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據',
                'keywords': '進銷存專案數據',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws = wb.add_worksheet("進銷存成本分析整批銷項憑證檔")

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

        if mytype == 'M1':
            titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '倉庫編號', '所屬專案', '自定欄二', '收款日期', '產品編號', '品名規格',
                       '數量', '單價', '備註']
            title_width = [20, 15, 15, 15, 20, 20, 30, 20, 20, 30, 15, 20, 60]
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

            for line in mypackagesalesrec:
                if line.sales_proj_no not in myoutrec:
                    myoutrec.append(line.sales_proj_no)
                # if mysalesno=='' :
                #     mysalesno = line.sales_proj_no
                # else:
                #     mysalesno = mysalesno + ' /' + line.sales_proj_no
                ws.write(row, 0, line.sales_no if line.sales_no else ' ', okl_content_format)
                ws.write(row, 1, line.sales_outdate if line.sales_outdate else ' ', date_format)
                ws.write(row, 2, line.sales_cusvat if line.sales_cusvat else ' ', okl_content_format)
                ws.write(row, 3, line.sales_currency, okl_content_format)
                # ws.write(row, 4, line.sales_man, okl_content_format)
                ws.write(row, 4, line.sales_wh, okl_content_format)
                ws.write(row, 5, line.sales_proj_no, okl_content_format)
                ws.write(row, 6, line.sales_cus_order if line.sales_cus_order else ' ', okl_content_format)
                ws.write(row, 7, line.sales_paymentdate if line.sales_paymentdate else ' ', date_format)
                ws.write(row, 8, line.sales_prod if line.sales_prod else ' ', okl_content_format)
                ws.write(row, 9, line.sale_spec if line.sale_spec else ' ', okl_content_format)
                ws.write(row, 10, 1, okc_content_format)
                ws.write(row, 11, round(line.sales_price, 2) if line.sales_price else 0, currency_format)
                ws.write(row, 12, line.sales_memo if line.sales_memo else ' ', okl_content_format)
                row += 1
                nitem += 1
        else:
            titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '業務人員', '倉庫編號', '所屬專案', '自定欄二', '收款日期', '產品編號', '數量', '單價','備註']
            title_width = [20, 15, 15, 15, 20, 15, 30, 20, 15, 20, 15, 20,60]

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

            for line in mypackagesalesrec:
                if line.sales_proj_no not in myoutrec:
                    myoutrec.append(line.sales_proj_no)
                # if mysalesno=='' :
                #     mysalesno = line.sales_proj_no
                # else:
                #     mysalesno = mysalesno + ' /' + line.sales_proj_no
                ws.write(row, 0, line.sales_no if line.sales_no else ' ', okl_content_format)
                ws.write(row, 1, line.sales_outdate if line.sales_outdate else ' ', date_format)
                ws.write(row, 2, line.sales_cusvat if line.sales_cusvat else ' ', okl_content_format)
                ws.write(row, 3, line.sales_currency, okl_content_format)
                ws.write(row, 4, line.sales_man, okl_content_format)
                ws.write(row, 5, line.sales_wh, okl_content_format)
                ws.write(row, 6, line.sales_proj_no, okl_content_format)
                ws.write(row, 7, line.sales_cus_order if line.sales_cus_order else ' ', okl_content_format)
                ws.write(row, 8, line.sales_paymentdate if line.sales_paymentdate else ' ', date_format)
                ws.write(row, 9, line.sales_prod if line.sales_prod else ' ', okl_content_format)
                ws.write(row, 10, round(line.sales_num, 0) if line.sales_num else 0, okc_content_format)
                ws.write(row, 11, round(line.sales_price,2) if line.sales_price else 0,currency_format)
                ws.write(row, 12, line.sales_memo if line.sales_memo else ' ', okl_content_format)
                row += 1
                nitem += 1

        wb.close()
        output1.seek(0)
        myxlsfile = base64.standard_b64encode(output1.getvalue())
        output1.close()
        mysalesno = ''
        for rec in myoutrec:
            if mysalesno == '':
                mysalesno = rec
            else:
                try:
                    mysalesno = mysalesno + ' /' + rec
                except Exception as inst:
                    A=1

        myrec = self.env['neweb_chi_invoicing.package_saleinv_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'project_no': mysalesno})
        self.env.cr.execute("""update neweb_chi_invoicing_package_saleinv_excel_download set invoicing_date='%s',
             invoicing_owner=%d where project_no='%s'""" % (self.export_date, myempid, mysalesno))
        self.env.cr.execute("""commit""")


        myviewid = self.env.ref('neweb_chi_invoicing.view_neweb_chi_invoicing_package_saleinv_download_tree')

        return {
            'view_name': 'newebinvoicingexportpackagewizard',
            'name': ('進銷存EXCEL整批匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_chi_invoicing.package_saleinv_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

        ##############################




class newebunexportinvoiceopenline(models.Model):
    _name = "neweb_chi_invoicing.un_export_invoiceopenline"
    _description = "生成未匯出銷項數據暫存明細檔"
    _order = "project_no"

    export_id = fields.Many2one('neweb_chi_invoicing.un_export_invoiceopen', required=True, ondelete='cascade')
    inv_prodspec = fields.Char(string="說明")
    cus_partner = fields.Char(string="客戶簡稱")
    project_no = fields.Many2one('neweb.project', string="專案編號")
    invoice_origin_no = fields.Char(string="來源單號")
    inv_paymentterm = fields.Date(string="收款日期")
    inv_cpaymentterm = fields.Date(string="C收款日期")
    currency_id = fields.Many2one('res.currency', string="幣別")
    invoice_sum = fields.Float(digits=(10, 0), string="收款金額")
    invoice_partner = fields.Many2one('res.partner', string="客戶名稱")
    invoice_date = fields.Date(string="發票日期")
    invoice_cdate = fields.Date(string="C發票日期")
    invoice_no = fields.Char(string="發票號碼")
    sequence = fields.Integer(string="sequence", default=10)
    invline_memo = fields.Text(string="備註")
    selectyn = fields.Boolean(default=False, string="選")


    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})
