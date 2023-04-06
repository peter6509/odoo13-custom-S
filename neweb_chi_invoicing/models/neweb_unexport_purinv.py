# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
from odoo.tools.float_utils import float_round as round
import xlsxwriter

class newebunexportpurinv(models.Model):
    _name = "neweb_chi_invoicing.un_export_purinv"
    _description = "生成未匯出進項數據暫存主檔"
    _rec_name = "export_user"

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.export_user = self.env.user.id

    export_user = fields.Many2one('res.users', string="匯出人員", compute=_get_current_user, store=True)
    export_date = fields.Date(string="匯出日期")
    export_line = fields.One2many('neweb_chi_invoicing.un_export_purinvline','export_id')



    def selectitemall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_purinvline'].search([])
        for rec in myrec:
            rec.update({'selectyn': True})

    def selectitemallno(self):
        myrec = self.env['neweb_chi_invoicing.un_export_purinvline'].search([])
        for rec in myrec:
            rec.update({'selectyn': False})


    def selectall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_purinvline'].search([])

    def selectbtn(self):
        mytype = self.env.context.get('neweb_export_type' or False)
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        myporec =[]
        mychipurchasename=''
        mypurchaseno = ''
        mypackagepurrec = self.env['neweb_chi_invoicing.package_purchase']
        self.env.cr.execute("""update neweb_purinv_invoiceline set main_purno='' where main_purno='D001';""")
        self.env.cr.execute("""commit;""")
        self.env.cr.execute("""delete from neweb_chi_invoicing_export_purchase_log where chi_purchase_name = 'D001';""")
        self.env.cr.execute("""commit;""")

        for myrec in self.export_line:
            self.env.cr.execute("""select check_null_reportdate(%d)""" % myrec.purchase_no.id)
            myres = self.env.cr.fetchone()[0]
            if myres:
                self.env.cr.execute("""select return_purinvno(%d)""" % myrec.purchase_no.id)
                raise UserError("廠商請款單製表日期空白 =>%s" % self.env.cr.fetchone()[0])
            if mytype=='M2':  ## 維護進項
                self.env.cr.execute("""select genincomeoutcomenom2(%d,%d)""" % (myrec.purchase_no.id,myrec.id))
                self.env.cr.execute("commit")
            else:             ## 買賣進項
                self.env.cr.execute("""select genincomeoutcomeno(%d)""" % (myrec.purchase_no.id))
                self.env.cr.execute("commit")

            output = io.BytesIO()

            if mytype=='M2':   ## 維護進項
                # self.env.cr.execute("""select ckmchipurchase(%d)""" % myrec.purchase_no.id)
                # self.env.cr.execute("""commit""")
                mypurrec = self.env['neweb_chi_invoicing.export_purchase_log'].search([('chi_origin_id', '=', myrec.chi_origin_id)])
                # mypurrec = self.env['neweb_chi_invoicing.export_purchase_log'].search([('chi_origin_id', '=', myrec.chi_origin_id),('chi_purchase_name','!=',False),('chi_purchase_name','!=','D001'),('chi_product','=','ZZB00000001')], order='chi_purchase_no')
            else:              ## 買賣進項
                self.env.cr.execute("""select getselectpurchaselog()""")
                ids = self.env.cr.fetchall()
                myids=[]
                for rec in ids:
                    myids.append(rec[0])
                # mypurrec = self.env['neweb_chi_invoicing.export_purchase_log'].search([('chi_purchase_no', '=', myrec.purchase_no.id), ('pitem_id', 'in', myids)],order="chi_purchase_name,pitem_id")
                mypurrec = self.env['neweb_chi_invoicing.export_purchase_log'].search([('chi_purchase_no', '=', myrec.purchase_no.id)],order="chi_purchase_name,pitem_id")
            if mypurrec:
                myprojno = mypurrec[0].chi_project_no
                wb3 = xlsxwriter.Workbook(output, {'in_memory': True})
                if mytype=='M2':
                    myxlsfilename3 = "PURCHASE_MAIN_%s_%s.xlsx" % (myrec.purchase_no.name, datetime.now().strftime("%Y%m%d"))
                    mysubject = 'PURCHASE_MAIN_%s_%s.xlsx' % (myrec.purchase_no.name, datetime.now().strftime("%Y%m%d"))
                    wb3.set_properties({
                        'title': '專案進項資訊(維護)',
                        'subject': mysubject,
                        'author': '%s' % self.env.user.name,
                        'manager': 'NEWEB INFO',
                        'company': '藍新資訊股份有限公司',
                        'category': '進銷存專案數據(維護)',
                        'keywords': '進銷存專案數據(維護)',
                        'created': datetime.now(),
                        'comments': 'Created By Odoo'})
                    ws3 = wb3.add_worksheet("進銷存(維護)成本分析進項憑證檔")
                else:
                    myxlsfilename3 = "PURCHASE_%s_%s.xlsx" % (myrec.purchase_no.name,datetime.now().strftime("%Y%m%d"))
                    mysubject = 'PURCHASE_%s_%s.xlsx' % (myrec.purchase_no.name,datetime.now().strftime("%Y%m%d"))
                    wb3.set_properties({
                        'title': '專案進項資訊',
                        'subject': mysubject,
                        'author': '%s' % self.env.user.name,
                        'manager': 'NEWEB INFO',
                        'company': '藍新資訊股份有限公司',
                        'category': '進銷存專案數據',
                        'keywords': '進銷存專案數據',
                        'created': datetime.now(),
                        'comments': 'Created By Odoo'})
                    ws3 = wb3.add_worksheet("進銷存成本分析進項憑證檔")

                ########################################
                # currency_format = wb3.add_format({'num_format': '$#,##0.00'})
                # # ws3.write('A1', 1234.56, currency_format)
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

                titles1 = ['單據號碼', '進貨日期', '廠商編號', '使用幣別', '倉庫編號', '所屬專案', '付款日期', '產品編號', '數量', '單價']
                title_width = [20, 15, 15, 15, 15, 30, 15, 20, 15, 20]

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

                for line in mypurrec:
                    if mytype=='M2':
                        if line.chi_purchase_name[0:1] == 'D':
                            mychipurchasename = line.chi_purchase_name
                            mypurchaseno = line.chi_purchase_no.id
                            ws3.write(row, 0, line.chi_purchase_name if line.chi_purchase_name else ' ', okl_content_format)
                            ws3.write(row, 1, line.chi_income_date if line.chi_income_date else ' ', date_format)
                            ws3.write(row, 2, line.chi_purchase_vat, okl_content_format)
                            ws3.write(row, 3, line.chi_currency_type, okl_content_format)
                            ws3.write(row, 4, line.chi_wh, okl_content_format)
                            ws3.write(row, 5, line.chi_project_no, okl_content_format)
                            ws3.write(row, 6, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                            ws3.write(row, 7, line.chi_product, okl_content_format)
                            ws3.write(row, 8, line.chi_purchase_num, okl_content_format)
                            # ws3.write(row, 9, round(line.chi_purchase_price,3) if line.chi_purchase_price else 0.00, currency_format)
                            # print round(line.chi_purchase_price,3)
                            # myckcount = self.env['neweb_chi_invoicing.package_purchase'].search_count([('purchase_no','=',line.chi_purchase_no.name)])
                            # if myckcount==0:
                            mypackagepurrec.create(
                                {'purchase_no': line.chi_purchase_no.name,'purchase_no1': line.chi_purchase_name , 'purchase_indate': line.chi_income_date,
                                 'purchase_suppvat': line.chi_purchase_vat,
                                 'purchase_currency': line.chi_currency_type, 'purchase_wh': line.chi_wh,
                                 'purchase_projno': line.chi_project_no,
                                 'purchase_payment': line.chi_paymentdate, 'purchase_prod': line.chi_product,
                                 'purchase_num': line.chi_purchase_num,
                                 'purchase_price': round(line.chi_purchase_price, 3)})
                    else:
                        mychipurchasename = line.chi_purchase_name
                        mypurchaseno = line.chi_purchase_no.id
                        ws3.write(row, 0, line.chi_purchase_name if line.chi_purchase_name else ' ', okl_content_format)
                        ws3.write(row, 1, line.chi_income_date if line.chi_income_date else ' ', date_format)
                        ws3.write(row, 2, line.chi_purchase_vat, okl_content_format)
                        ws3.write(row, 3, line.chi_currency_type, okl_content_format)
                        ws3.write(row, 4, line.chi_wh, okl_content_format)
                        ws3.write(row, 5, line.chi_project_no, okl_content_format)
                        ws3.write(row, 6, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                        ws3.write(row, 7, line.chi_product, okl_content_format)
                        ws3.write(row, 8, line.chi_purchase_num, okl_content_format)
                        # ws3.write(row, 9, round(line.chi_purchase_price,3) if line.chi_purchase_price else 0.00, currency_format)
                        # print round(line.chi_purchase_price,3)
                        # myckcount = self.env['neweb_chi_invoicing.package_purchase'].search_count([('purchase_no','=',line.chi_purchase_no.name)])
                        # if myckcount==0:
                        mypackagepurrec.create(
                            {'purchase_no': line.chi_purchase_no.name, 'purchase_no1': line.chi_purchase_name,
                             'purchase_indate': line.chi_income_date,
                             'purchase_suppvat': line.chi_purchase_vat,
                             'purchase_currency': line.chi_currency_type, 'purchase_wh': line.chi_wh,
                             'purchase_projno': line.chi_project_no,
                             'purchase_payment': line.chi_paymentdate, 'purchase_prod': line.chi_product,
                             'purchase_num': line.chi_purchase_num,
                             'purchase_price': round(line.chi_purchase_price, 3)})
                    row += 1
                    nitem += 1

                wb3.close()
                output.seek(0)
                myxlsfile3 = base64.standard_b64encode(output.getvalue())
                output.close()

                myprojcount = self.env['neweb_chi_invoicing.purinv_excel_download'].search_count([('purchase_no', '=', mypurchaseno)])
                if myprojcount > 0:
                    myrec = self.env['neweb_chi_invoicing.purinv_excel_download'].search([('purchase_no', '=', mypurchaseno)])
                    myrec.write({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3,'invoicing_date':self.export_date,'invoicing_owner':myempid})
                    # self.env.cr.execute("""update neweb_chi_invoicing_purinv_excel_download set invoicing_date='%s',invoicing_owner=%d where purchase_no=%d""" % (self.export_date, myempid,mypurchaseno))
                    # self.env.cr.execute("""commit""")

                else:
                    myrec = self.env['neweb_chi_invoicing.purinv_excel_download']
                    myrec.create({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3, 'purchase_no': mypurchaseno,'chi_purchase_name':mychipurchasename,'invoicing_date':self.export_date,'invoicing_owner':myempid})
                    # self.env.cr.execute("""update neweb_chi_invoicing_purinv_excel_download set invoicing_date='%s',invoicing_owner=%d where purchase_no=%d""" % (self.export_date, myempid, mypurchaseno))
                    # self.env.cr.execute("""commit""")
                if mypurchaseno == False or mypurchaseno=='':
                    self.env.cr.execute("""select purinvgenstatus(%d,%d)""" % (0, myempid))
                    self.env.cr.execute("""commit""")
                else:
                    self.env.cr.execute("""select purinvgenstatus(%d,%d)""" % (mypurchaseno,myempid))
                    self.env.cr.execute("""commit""")

        ########################## 整包輸出作業 #########################
        mytoday = date.today()
        # mytd = mytoday.strftime('%Y%m%d')
        self.env.cr.execute("""select getsetnum('%s','%s')""" % (mytoday, '1'))
        myres = self.env.cr.fetchone()[0]
        mystr = str(myres).zfill(3)



        if mytype=='M2':
            mypackagepurrec = self.env['neweb_chi_invoicing.package_purchase'].search([])
            myxlsfilename = "PURCHASE_MAIN_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"), mystr, self.export_user.name)
            mysubject = "PURCHASE_MAIN_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"), mystr, self.export_user.name)

        else:
            mypackagepurrec = self.env['neweb_chi_invoicing.package_purchase'].search([])
            myxlsfilename = "PURCHASE_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)
            mysubject = "PURCHASE_SET_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)

        output1 = io.BytesIO()

        wb = xlsxwriter.Workbook(output1, {'in_memory': True})
        if mytype=='M2':
            wb.set_properties({
                'title': '專案進項資訊(維護)',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據(維護)',
                'keywords': '進銷存專案數據(維護)',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws = wb.add_worksheet("進銷存(維護)成本分析整批進項憑證檔")
        else:
            wb.set_properties({
                'title': '專案進項資訊',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據',
                'keywords': '進銷存專案數據',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws = wb.add_worksheet("進銷存成本分析整批進項憑證檔")

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

        titles1 = ['單據號碼', '進貨日期', '廠商編號', '使用幣別', '倉庫編號', '所屬專案', '付款日期', '產品編號', '數量', '單價']
        title_width = [20, 15, 15, 15, 15, 30, 15, 20, 15, 20]

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
        mypurchaseno=''
        for line in mypackagepurrec:
            # if mypurchaseno=='' :
            #     mypurchaseno = line.purchase_no
            # else:
            #     mypurchaseno = mypurchaseno + ' /' + line.purchase_no
            if line.purchase_no not in myporec:
                myporec.append(line.purchase_no)
            ws.write(row, 0, line.purchase_no1 if line.purchase_no1 else ' ', okl_content_format)
            ws.write(row, 1, line.purchase_indate if line.purchase_indate else ' ', date_format)
            ws.write(row, 2, line.purchase_suppvat, okl_content_format)
            ws.write(row, 3, line.purchase_currency, okl_content_format)
            ws.write(row, 4, line.purchase_wh, okl_content_format)
            ws.write(row, 5, line.purchase_projno, okl_content_format)
            ws.write(row, 6, line.purchase_payment if line.purchase_payment else ' ', date_format)
            ws.write(row, 7, line.purchase_prod if line.purchase_prod else ' ', okl_content_format)
            ws.write(row, 8, line.purchase_num if line.purchase_num else 0, okc_content_format)
            ws.write(row, 9, round(line.purchase_price,3) if line.purchase_price else 0,currency_format)

            row += 1
            nitem += 1

        wb.close()
        output1.seek(0)
        myxlsfile = base64.standard_b64encode(output1.getvalue())
        output1.close()
        mypurchaseno= ' '
        for rec in myporec:
            if mypurchaseno == ' ':
                if rec != False:
                   mypurchaseno =  rec
            else:
                if rec != False:
                   mypurchaseno = mypurchaseno + ' /' + rec
        myrec = self.env['neweb_chi_invoicing.package_purinv_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename, 'purchase_no': mypurchaseno})
        self.env.cr.execute("""update neweb_chi_invoicing_package_purinv_excel_download set invoicing_date='%s',
             invoicing_owner=%d where purchase_no='%s'""" % (self.export_date, myempid, mypurchaseno))
        self.env.cr.execute("""commit""")


        myviewid = self.env.ref('neweb_chi_invoicing.view_neweb_chi_invoicing_package_purinv_download_tree')

        return {
            'view_name': 'newebinvoicingexportpackagewizard',
            'name': ('進銷存EXCEL整批匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_chi_invoicing.package_purinv_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

        ##############################




class newebunexportpurinvline(models.Model):
    _name = "neweb_chi_invoicing.un_export_purinvline"
    _description = "生成未匯出進項數據暫存明細檔"

    export_id = fields.Many2one('neweb_chi_invoicing.un_export_purinv', required=True, ondelete='cascade')
    inv_prodspec = fields.Char(string="品名")
    cus_partner = fields.Char(string="客戶簡稱")
    purchase_no = fields.Many2one('purchase.order', string="採購單號")
    pitem_origin_no = fields.Char(string="來源單號")
    inv_paymentterm = fields.Date(string="付款期限")
    currency_id = fields.Many2one('res.currency', string="幣別")
    invoice_sum = fields.Float(digits=(10, 0), string="付款金額(含税)")
    invoice_partner = fields.Many2one('res.partner', string="付款對象")
    invoice_date = fields.Date(string="發票日期")
    invoice_no = fields.Char(string="發票號碼")
    sequence = fields.Integer(string="sequence", default=10)
    invline_memo = fields.Text(string="備註")
    selectyn = fields.Boolean(default=False, string="選")
    purno = fields.Char(string="請款單號")
    chi_origin_id = fields.Integer(string="來源PITEM_ID")


    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})
