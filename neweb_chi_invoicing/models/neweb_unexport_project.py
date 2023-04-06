# -*- coding: utf-8 -*-
# Author : Peter Wu


import io
import base64
from odoo import models,fields,api
from odoo.exceptions import UserError
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter


class newebunexportproject(models.Model):
    _inherit = "neweb.project"

    chi_export_project = fields.Boolean(string="匯出專案否?",default=False)
    chi_export_product = fields.Boolean(string="匯出產品否?",default=False)
    chi_export_outcome = fields.Boolean(string="銷項匯出否?",default=False)
    chi_export_income = fields.Boolean(string="進項匯出否？",default=False)
    chi_invoice_complete = fields.Boolean(string="結案否?",default=False)


class newebunexportprojsaleitem(models.Model):
    _inherit = "neweb.projsaleitem"

    chi_export_product = fields.Boolean(string="匯出產品否?",default=False)
    chi_product_no = fields.Char(string="產品料號")
    chi_sales_no = fields.Char(string="銷項單號")


class newebproductprodsetseq(models.Model):
    _name = "neweb_chi_invoicing.productset_seq"
    _description = "進銷存產品序號流水號檔"


    chi_year = fields.Char(string="年度")
    chi_sname = fields.Char(string="簡碼")
    chi_seq = fields.Integer(string="流水號",default=1)



class newebchiinvoicingunexportproj(models.Model):
    _name = "neweb_chi_invoicing.un_export_proj"
    _description = "生成未匯出專案數據暫存主檔"
    _rec_name = "export_user"

    export_user = fields.Many2one('res.users',string="匯出人員",compute='_get_current_user',store=True)
    export_date = fields.Date(string="匯出日期")
    is_export_project_master = fields.Boolean(string="匯出成本分析主檔？",default=False)
    is_export_project_product = fields.Boolean(string="匯出成本分析產品檔？",default=False)
    is_export_project_sale = fields.Boolean(string="匯出成本分析銷項記錄檔？",default=False)
    is_export_project_purchase = fields.Boolean(string="匯出成本分析進項記錄檔？",default=False)
    export_line = fields.One2many('neweb_chi_invoicing.un_export_proj_line','export_id',copy=True, string="專案清單")
    chi_export_type = fields.Char(compute='_get_export_type')

    @api.depends()
    def _get_export_type(self):
        for rec in self:
            myres = self.env.context.get('neweb_export_type', False)
            rec.chi_export_type = myres

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.export_user = self.env.user.id


    def selectitemall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_proj_line'].search([])
        for rec in myrec:
            rec.update({'selectyn': True})

    def selectitemallno(self):
        myrec = self.env['neweb_chi_invoicing.un_export_proj_line'].search([])
        for rec in myrec:
            rec.update({'selectyn': False})


    def selectall(self):
        myrec = self.env['neweb_chi_invoicing.un_export_proj_line'].search([])

    def run_project_export(self,projid):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]


        output = io.BytesIO()
        myprojrec = self.env['neweb.project'].search([('id','=',projid)])
        mypackageprojrec = self.env['neweb_chi_invoicing.package_project'].search([])


        myxlsfilename1 = "PROJ_%s_%s.xlsx" % (myprojrec.name, datetime.now().strftime("%Y%m%d"))
        mysubject = 'PROJ_%s_%s.xlsx' % (myprojrec.name, datetime.now().strftime("%Y%m%d"))

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '專案資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '進銷存專案數據',
            'keywords': '進銷存專案數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet("進銷存成本分析主檔")

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

        titles1 = ['專案編號', '專案名稱', '備註']
        title_width = [30, 60, 45]

        row = 0

        mytitle = "成本分析主檔"

        #ws1.write(row, 4, mytitle, title_format)
        #row += 2
        col = 0
        for title in titles1:
            ws1.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws1.set_row(row, 30)
            ws1.set_column(myloc, title_width[col])
            col += 1

        #ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in myprojrec:

            myprojno = line.name
            myprojname = line.cus_project[0:20]
            self.env.cr.execute("""select getprojmemo(%d)""" % projid)
            myprojmemo = self.env.cr.fetchone()[0]

            ws1.write(row, 0, myprojno, okl_content_format)
            ws1.write(row, 1, myprojname[0:20], okl_content_format)
            ws1.write(row, 2, myprojmemo, okl_content_format)
            mypackageprojrec.create({'project_no':myprojno,'project_desc':myprojname[0:20],'project_memo':myprojmemo})

            row += 1
            nitem += 1

        wb1.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()
        myprojcount = self.env['neweb_chi_invoicing.excel_download'].search_count([('project_no','=',projid)])
        if myprojcount > 0:
            myrec = self.env['neweb_chi_invoicing.excel_download'].search([('project_no','=',projid)])
            myrec.write({'xls_file1': myxlsfile1, 'xls_file_name1': myxlsfilename1})
            self.env.cr.execute("""update neweb_chi_invoicing_excel_download set invoicing1_date='%s',invoicing1_owner=%d,is_completed='1' where project_no=%d""" % (self.export_date, myempid, projid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""update neweb_project set chi_export_project=True where id=%d""" % projid)
            self.env.cr.execute("""commit""")
        else:
            myrec = self.env['neweb_chi_invoicing.excel_download']
            myrec.create({'xls_file1': myxlsfile1, 'xls_file_name1': myxlsfilename1,'project_no':projid})
            self.env.cr.execute("""update neweb_project set chi_export_project=True where id=%d""" % projid)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""update neweb_chi_invoicing_excel_download set invoicing1_date='%s',invoicing1_owner=%d where project_no=%d""" % (self.export_date, myempid, projid))
            self.env.cr.execute("""commit""")


    ######################### Package Project

    def run_package_project_export(self):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]


        output = io.BytesIO()
        myprojrec = self.env['neweb_chi_invoicing.package_project'].search([])

        mytoday = date.today()
        # mytd = mytoday.strftime('%Y%m%d')
        self.env.cr.execute("""select getsetnum('%s','%s')""" % (mytoday, '3'))
        myres = self.env.cr.fetchone()[0]
        mystr = str(myres).zfill(3)
        myxlsfilename1 = "PROJ_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)
        mysubject = "PROJ_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)

        wb5 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb5.set_properties({
            'title': '專案資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '進銷存專案數據',
            'keywords': '進銷存專案數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws5 = wb5.add_worksheet("進銷存成本分析主檔(匯整)")

        ########################################
        title_format = wb5.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb5.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb5.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb5.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb5.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb5.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################

        titles1 = ['專案編號', '專案名稱', '備註']
        title_width = [30, 60, 45]

        row = 0

        mytitle = "成本分析主檔"

        #ws1.write(row, 4, mytitle, title_format)
        #row += 2
        col = 0
        for title in titles1:
            ws5.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws5.set_row(row, 30)
            ws5.set_column(myloc, title_width[col])
            col += 1

        #ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1
        myfilename = ''
        mypnamerec=[]
        for line in myprojrec:

            myprojno = line.project_no
            myprojname = line.project_desc[0:20]
            myprojmemo = line.project_memo

            ws5.write(row, 0, myprojno, okl_content_format)
            ws5.write(row, 1, myprojname[0:20], okl_content_format)
            ws5.write(row, 2, myprojmemo, okl_content_format)
            if line.project_no not in mypnamerec:
                mypnamerec.append(line.project_no)
            # if myfilename == '':
            #     myfilename = myprojno
            # else:
            #     myfilename = myfilename + ' / ' + myprojno
            row += 1
            nitem += 1

        wb5.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()
        myprojno=''
        for rec in mypnamerec:
            if myprojno=='':
                myprojno = rec
            else:
                myprojno = myprojno + ' /' + rec
        self.env.cr.execute("""select getpackageprojno()""")
        myprojno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getpackdownloadid(%d,'%s')""" % (myempid,'1'))
        mypid = self.env.cr.fetchone()[0]
        # myrec = self.env['neweb_chi_invoicing.package_excel_download']
        # myrec.create({'xls_file1': myxlsfile1, 'xls_file_name1': myxlsfilename1,'project_no':myprojno,'invoicing1_owner':myempid,'invoicing1_date':self.export_date})
        myrec = self.env['neweb_chi_invoicing.package_excel_download'].search([('id', '=', mypid)])
        myrec.write({'xls_file1': myxlsfile1, 'xls_file_name1': myxlsfilename1, 'project_no': myprojno,
                     'invoicing1_owner': myempid, 'invoicing1_date': self.export_date})





    ########################
    def run_product_export(self,projid):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select genprojchiprodno(%d)""" % projid)
        self.env.cr.execute("""commit""")
        output = io.BytesIO()
        myprojrec = self.env['neweb.project'].search([('id','=',projid)])
        mypackageprodrec = self.env['neweb_chi_invoicing.package_product'].search([])

        myxlsfilename2 = "PROD_%s_%s.xlsx" % (myprojrec.name, datetime.now().strftime("%Y%m%d"))
        mysubject = 'PROD_%s_%s.xlsx' % (myprojrec.name, datetime.now().strftime("%Y%m%d"))

        wb2 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb2.set_properties({
            'title': '專案產品資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '進銷存專案數據',
            'keywords': '進銷存專案數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws2 = wb2.add_worksheet("進銷存成本分析產品料號檔")

        ########################################
        title_format = wb2.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb2.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb2.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb2.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb2.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb2.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################

        titles1 = ['產品類別', '產品編號', '品名規格','使用幣別','自定欄一']
        title_width = [15, 30, 150,15,30]

        row = 0

        mytitle = "成本分析產品料號檔"

        #ws1.write(row, 4, mytitle, title_format)
        #row += 2
        col = 0
        for title in titles1:
            ws2.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws2.set_row(row, 30)
            ws2.set_column(myloc, title_width[col])
            col += 1

        #ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in myprojrec.saleitem_line:
            if line.chi_product_no and line.not_chiout != True :
                myprojno = line.saleitem_id.name
                myprodset = line.prod_set.sname
                mychiprodno = line.chi_product_no
                if not line.prod_modeltype:
                    myprodmodeltype = 'None'
                else:
                    myprodmodeltype = line.prod_modeltype.replace('\n','')
                if not line.prod_desc:
                    myproddesc = 'None'
                else:
                    myproddesc = line.prod_desc.replace('\n','')
                myprodspec = myprodmodeltype +' / '+ myproddesc
                ws2.write(row, 0, myprodset, okl_content_format)
                ws2.write(row, 1, mychiprodno, okl_content_format)
                ws2.write(row, 2, myprodspec[0:60], okl_content_format)
                ws2.write(row, 3, 'NTD', okl_content_format)
                ws2.write(row, 4, myprojno, okl_content_format)
                mypackageprodrec.create({'prod_set':myprodset,'prod_no':mychiprodno,'prod_spec':myprodspec[0:60],'prod_currency':'NTD','prod_memo':myprojno,'proj_no':myprojno})
                row += 1
                nitem += 1

        wb2.close()
        output.seek(0)
        myxlsfile2 = base64.standard_b64encode(output.getvalue())
        output.close()
        myprojcount = self.env['neweb_chi_invoicing.excel_download'].search_count([('project_no','=',projid)])
        if myprojcount > 0:
            myrec = self.env['neweb_chi_invoicing.excel_download'].search([('project_no','=',projid)])
            myrec.write({'xls_file2': myxlsfile2, 'xls_file_name2': myxlsfilename2})
            self.env.cr.execute("""update neweb_chi_invoicing_excel_download set invoicing2_date='%s',invoicing2_owner=%d where project_no=%d""" % (self.export_date,myempid,projid))
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""update neweb_project set chi_export_product=True where id=%d""" % projid)
            self.env.cr.execute("""commit""")
        else:
            myrec = self.env['neweb_chi_invoicing.excel_download']
            myrec.create({'xls_file2': myxlsfile2, 'xls_file_name2': myxlsfilename2,'project_no':projid})
            self.env.cr.execute("""update neweb_project set chi_export_product=True where id=%d""" % projid)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""update neweb_chi_invoicing_excel_download set invoicing2_date='%s',invoicing2_owner=%d where project_no=%d""" % (self.export_date, myempid, projid))
            self.env.cr.execute("""commit""")



    ################### package prod
    def run_package_product_export(self):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]

        output = io.BytesIO()
        myprodrec = self.env['neweb_chi_invoicing.package_product'].search([])

        mytoday = date.today()
        # mytd = mytoday.strftime('%Y%m%d')
        self.env.cr.execute("""select getsetnum('%s','%s')""" % (mytoday, '4'))
        myres = self.env.cr.fetchone()[0]
        mystr = str(myres).zfill(3)
        myxlsfilename2 = "PROD_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)
        mysubject = "PROD_%s_%s_%s.xlsx" % (datetime.now().strftime("%Y%m%d"),mystr,self.export_user.name)

        wb6 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb6.set_properties({
            'title': '專案產品資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '進銷存專案數據',
            'keywords': '進銷存專案數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws6= wb6.add_worksheet("進銷存成本分析產品料號檔(匯整)")

        ########################################
        title_format = wb6.add_format()
        title_format.set_font_size(30)
        title_format.set_bold()
        title_format.set_underline(2)
        title_format.set_font_color('black')
        title_format.set_align('left')
        title_format.set_align('vcenter')
        ########################################
        head_format = wb6.add_format()
        head_format.set_font_size(15)
        head_format.set_border(2)
        head_format.set_font_color('yellow')
        head_format.set_fg_color('blue')
        head_format.set_align('center')
        head_format.set_align('vcenter')
        ########################################
        okc_content_format = wb6.add_format()
        okc_content_format.set_font_size(15)
        okc_content_format.set_border(1)
        okc_content_format.set_font_color('black')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb6.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('black')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb6.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        ngc_content_format.set_italic()
        ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb6.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        ngl_content_format.set_italic()
        ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################

        titles1 = ['產品類別', '產品編號', '品名規格', '使用幣別', '自定欄一']
        title_width = [15, 30, 150, 15, 30]

        row = 0

        mytitle = "成本分析產品料號檔"

        # ws1.write(row, 4, mytitle, title_format)
        # row += 2
        col = 0
        for title in titles1:
            ws6.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws6.set_row(row, 30)
            ws6.set_column(myloc, title_width[col])
            col += 1

        # ws1.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        mypnamerec=[]
        for line in myprodrec:
            myprodset = line.prod_set
            mychiprodno = line.prod_no
            myprodspec = line.prod_spec
            myprodmemo = line.prod_memo
            if line.proj_no not in mypnamerec:
                mypnamerec.append(line.proj_no)
            ws6.write(row, 0, myprodset, okl_content_format)
            ws6.write(row, 1, mychiprodno, okl_content_format)
            ws6.write(row, 2, myprodspec[0:60], okl_content_format)
            ws6.write(row, 3, 'NTD', okl_content_format)
            ws6.write(row, 4, myprodmemo, okl_content_format)

            row += 1
            nitem += 1

        wb6.close()
        output.seek(0)
        myxlsfile2 = base64.standard_b64encode(output.getvalue())
        output.close()

        myprojno = ''
        for rec in mypnamerec:
            if myprojno =='':
                myprojno = rec
            else:
                myprojno = myprojno + ' /' + rec
        self.env.cr.execute("""select getpackageprodprojno()""")
        myprojno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select getpackdownloadid(%d,'%s')""" % (myempid, '2'))
        mypid = self.env.cr.fetchone()[0]
        # myrec = self.env['neweb_chi_invoicing.package_excel_download']
        # myrec.create({'xls_file2': myxlsfile2, 'xls_file_name2': myxlsfilename2, 'project_no': myprojno,'invoicing2_owner':myempid,'invoicing2_date':self.export_date})
        myrec = self.env['neweb_chi_invoicing.package_excel_download'].search([('id', '=', mypid)])
        myrec.write({'xls_file2': myxlsfile2, 'xls_file_name2': myxlsfilename2, 'project_no': myprojno,
                     'invoicing2_owner': myempid, 'invoicing2_date': self.export_date})

    ################################
    def run_purchase_export(self, purid):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select genincomeoutcomeno(%d)""" % (purid))
        self.env.cr.execute("commit")
        output = io.BytesIO()

        mypackagepurrec = self.env['neweb_chi_invoicing.package_purchase']
        mypurrec = self.env['neweb_chi_invoicing.export_purchase_log'].search([('chi_purchase_no', '=', purid)])
        if mypurrec:
            myprojno = mypurrec[0].chi_project_no
            myxlsfilename3 = "PURCHASE_%s_%s.xlsx" % (mypurrec.chi_purchase_no.name, datetime.now().strftime("%Y%m%d"))
            mysubject = 'PURCHASE_%s_%s.xlsx' % (mypurrec.chi_purchase_no.name, datetime.now().strftime("%Y%m%d"))

            wb3 = xlsxwriter.Workbook(output, {'in_memory': True})
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
            date_format = wb3.add_format({'num_format': 'yyyy-mm-dd'})
            date_format.set_font_size(15)
            date_format.set_border(1)
            date_format.set_font_color('black')
            date_format.set_align('right')
            date_format.set_align('vcenter')
            date_format.set_text_wrap()

            titles1 = ['單據號碼', '進貨日期', '廠商編號', '使用幣別', '倉庫編號','所屬專案','付款日期','產品編號','數量','單價']
            title_width = [20, 15, 15, 15, 15,30,15,20,15,15]

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
                ws3.write(row, 0, line.chi_purchase_name if line.chi_purchase_name else ' ', okl_content_format)
                ws3.write(row, 1, line.chi_income_date if line.chi_income_date else ' ', date_format)
                ws3.write(row, 2, line.chi_purchase_vat, okl_content_format)
                ws3.write(row, 3, line.chi_currency_type, okl_content_format)
                ws3.write(row, 4, line.chi_wh, okl_content_format)
                ws3.write(row, 5, line.chi_project_no, okl_content_format)
                ws3.write(row, 6, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                ws3.write(row, 7, line.chi_product, okl_content_format)
                ws3.write(row, 8, line.chi_purchase_num, okl_content_format)
                ws3.write(row, 9, round(line.chi_purchase_price,0) if line.chi_purchase_price else 0, okl_content_format)

                mypackagepurrec.create({'purchase_no':line.chi_purchase_no,'purchase_indate':line.chi_income_date,'purchase_suppvat':line.chi_purchase_vat,
                                        'purchase_currency':line.chi_currency_type,'purchase_wh':line.chi_wh,'purchase_projno':line.chi_project_no,
                                        'purchase_payment':line.chi_paymentdate,'purchase_prod':line.chi_product,'purchase_num':line.chi_purchase_num,
                                        'purchase_price':round(line.chi_purchase_price,0)})
                row += 1
                nitem += 1

            wb3.close()
            output.seek(0)
            myxlsfile3 = base64.standard_b64encode(output.getvalue())
            output.close()
            myprojcount = self.env['neweb_chi_invoicing.purinv_excel_download'].search_count([('purchase_no', '=', purid)])
            if myprojcount > 0:
                myrec = self.env['neweb_chi_invoicing.purinv_excel_download'].search([('purchase_no', '=', purid)])
                myrec.write({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3})
                self.env.cr.execute("""update neweb_chi_invoicing_purinv_excel_download set invoicing_date='%s',invoicing_owner=%d where purchase_no=%d""" % (
                    self.export_date, myempid, purid))
                self.env.cr.execute("""commit""")
                # self.env.cr.execute("""update neweb_project set chi_export_income=True where id=%d""" % projid)
                # self.env.cr.execute("""commit""")
            else:
                myrec = self.env['neweb_chi_invoicing.purinv_excel_download']
                myrec.create({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3, 'purchase_no': purid})
                # self.env.cr.execute("""update neweb_project set chi_export_income=True where id=%d""" % projid)
                # self.env.cr.execute("""commit""")
                self.env.cr.execute("""update neweb_chi_invoicing_purinv_excel_download set invoicing_date='%s',invoicing_owner=%d where purchase_no=%d""" % (
                    self.export_date, myempid, purid))
                self.env.cr.execute("""commit""")


    ##################  Package Purchase
    def run_package_purchase_export(self):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        # self.env.cr.execute("""select genincomeoutcomeno(%d)""" % (projid))
        # self.env.cr.execute("commit")
        output = io.BytesIO()
        mypurrec = self.env['neweb_chi_invoicing.package_purchase'].search([])
        if mypurrec:
            # myprojno = mypurrec[0].chi_project_no
            myxlsfilename3 = "PURCHASE_%s.xlsx" % datetime.now().strftime("%Y%m%d")
            mysubject = 'PURCHASE_%s.xlsx' % datetime.now().strftime("%Y%m%d")

            wb7 = xlsxwriter.Workbook(output, {'in_memory': True})
            wb7.set_properties({
                'title': '專案進項資訊',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據',
                'keywords': '進銷存專案數據',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws7 = wb7.add_worksheet("進銷存成本分析進項憑證檔(匯整)")

            ########################################
            title_format = wb7.add_format()
            title_format.set_font_size(30)
            title_format.set_bold()
            title_format.set_underline(2)
            title_format.set_font_color('black')
            title_format.set_align('left')
            title_format.set_align('vcenter')
            ########################################
            head_format = wb7.add_format()
            head_format.set_font_size(15)
            head_format.set_border(2)
            head_format.set_font_color('yellow')
            head_format.set_fg_color('blue')
            head_format.set_align('center')
            head_format.set_align('vcenter')
            ########################################
            okc_content_format = wb7.add_format()
            okc_content_format.set_font_size(15)
            okc_content_format.set_border(1)
            okc_content_format.set_font_color('black')
            okc_content_format.set_align('center')
            okc_content_format.set_align('vcenter')
            okc_content_format.set_text_wrap()
            #########################################
            okl_content_format = wb7.add_format()
            okl_content_format.set_font_size(15)
            okl_content_format.set_border(1)
            okl_content_format.set_font_color('black')
            okl_content_format.set_align('left')
            okl_content_format.set_align('vcenter')
            okl_content_format.set_text_wrap()
            #########################################
            ngc_content_format = wb7.add_format()
            ngc_content_format.set_font_size(15)
            ngc_content_format.set_border(1)
            ngc_content_format.set_font_color('red')
            ngc_content_format.set_italic()
            ngc_content_format.set_fg_color('yellow')
            ngc_content_format.set_align('center')
            ngc_content_format.set_align('vcenter')
            ngc_content_format.set_text_wrap()
            ##########################################
            ngl_content_format = wb7.add_format()
            ngl_content_format.set_font_size(15)
            ngl_content_format.set_border(1)
            ngl_content_format.set_font_color('red')
            ngl_content_format.set_italic()
            ngl_content_format.set_fg_color('yellow')
            ngl_content_format.set_align('left')
            ngl_content_format.set_align('vcenter')
            ngl_content_format.set_text_wrap()
            ##########################################
            date_format = wb7.add_format({'num_format': 'yyyy-mm-dd'})
            date_format.set_font_size(15)
            date_format.set_border(1)
            date_format.set_font_color('black')
            date_format.set_align('right')
            date_format.set_align('vcenter')
            date_format.set_text_wrap()

            titles1 = ['單據號碼', '進貨日期', '廠商編號', '使用幣別', '倉庫編號','所屬專案','付款日期','產品編號','數量','單價']
            title_width = [20, 15, 15, 15, 15,30,15,20,15,15]

            row = 0


            col = 0
            for title in titles1:
                ws7.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws7.set_row(row, 30)
                ws7.set_column(myloc, title_width[col])
                col += 1

            # ws1.freeze_panes(row + 1, 0)
            row += 1
            nitem = 1

            for line in mypurrec:
                ws7.write(row, 0, line.purchase_no, okl_content_format)
                ws7.write(row, 1, line.purchase_indate if line.purchase_indate else ' ', date_format)
                ws7.write(row, 2, line.purchase_suppvat, okl_content_format)
                ws7.write(row, 3, line.purchase_currency, okl_content_format)
                ws7.write(row, 4, line.purchase_wh, okl_content_format)
                ws7.write(row, 5, line.purchase_projno, okl_content_format)
                ws7.write(row, 6, line.purchase_payment if line.purchase_payment else ' ', date_format)
                ws7.write(row, 7, line.purchase_prod, okl_content_format)
                ws7.write(row, 8, line.purchase_num, okc_content_format)
                ws7.write(row, 9, line.purchase_price, okc_content_format)

                row += 1
                nitem += 1

            wb7.close()
            output.seek(0)
            myxlsfile3 = base64.standard_b64encode(output.getvalue())
            output.close()
            self.env.cr.execute("""select getpackagepurchasepurchaseno()""")
            mypurchaseno = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getpackdownloadid(%d,'%s')""" % (myempid, '3'))
            mypid = self.env.cr.fetchone()[0]
            myrec = self.env['neweb_chi_invoicing.package_purinv_excel_download'].search([('id', '=', mypid)])
            myrec.write({'xls_file': myxlsfile3, 'xls_file_name': myxlsfilename3, 'purchase_no': mypurchaseno,'invoicing_owner':myempid,'invoicing_date':self.export_date})


    ####################################



    def run_sale_export(self, projid):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]
        self.env.cr.execute("""select genincomeoutcomeno1(%d)""" % (projid))
        self.env.cr.execute("commit")
        output = io.BytesIO()
        mypsalerec = self.env['neweb_chi_invoicing.package_sales']
        mysalerec = self.env['neweb_chi_invoicing.export_sales_log'].search([('proj_no', '=', projid)])
        if mysalerec:
            myprojno = mysalerec[0].chi_project_no
            myxlsfilename4 = "SALES_%s_%s.xlsx" % (myprojno, datetime.now().strftime("%Y%m%d"))
            mysubject = 'SALES_%s_%s.xlsx' % (myprojno, datetime.now().strftime("%Y%m%d"))

            wb4 = xlsxwriter.Workbook(output, {'in_memory': True})
            wb4.set_properties({
                'title': '專案進項資訊',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據',
                'keywords': '進銷存專案數據',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws4 = wb4.add_worksheet("進銷存成本分析銷項憑證檔")

            ########################################
            title_format = wb4.add_format()
            title_format.set_font_size(30)
            title_format.set_bold()
            title_format.set_underline(2)
            title_format.set_font_color('black')
            title_format.set_align('left')
            title_format.set_align('vcenter')
            ########################################
            head_format = wb4.add_format()
            head_format.set_font_size(15)
            head_format.set_border(2)
            head_format.set_font_color('yellow')
            head_format.set_fg_color('blue')
            head_format.set_align('center')
            head_format.set_align('vcenter')
            ########################################
            okc_content_format = wb4.add_format()
            okc_content_format.set_font_size(15)
            okc_content_format.set_border(1)
            okc_content_format.set_font_color('black')
            okc_content_format.set_align('center')
            okc_content_format.set_align('vcenter')
            okc_content_format.set_text_wrap()
            #########################################
            okl_content_format = wb4.add_format()
            okl_content_format.set_font_size(15)
            okl_content_format.set_border(1)
            okl_content_format.set_font_color('black')
            okl_content_format.set_align('left')
            okl_content_format.set_align('vcenter')
            okl_content_format.set_text_wrap()
            #########################################
            ngc_content_format = wb4.add_format()
            ngc_content_format.set_font_size(15)
            ngc_content_format.set_border(1)
            ngc_content_format.set_font_color('red')
            ngc_content_format.set_italic()
            ngc_content_format.set_fg_color('yellow')
            ngc_content_format.set_align('center')
            ngc_content_format.set_align('vcenter')
            ngc_content_format.set_text_wrap()
            ##########################################
            ngl_content_format = wb4.add_format()
            ngl_content_format.set_font_size(15)
            ngl_content_format.set_border(1)
            ngl_content_format.set_font_color('red')
            ngl_content_format.set_italic()
            ngl_content_format.set_fg_color('yellow')
            ngl_content_format.set_align('left')
            ngl_content_format.set_align('vcenter')
            ngl_content_format.set_text_wrap()
            ##########################################
            date_format = wb4.add_format({'num_format': 'yyyy-mm-dd'})
            date_format.set_font_size(15)
            date_format.set_border(1)
            date_format.set_font_color('black')
            date_format.set_align('right')
            date_format.set_align('vcenter')
            date_format.set_text_wrap()

            titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '業務人員', '倉庫編號', '所屬專案' , '自定欄二', '付款日期', '產品編號', '數量', '單價','備註']
            title_width = [20, 15, 15, 15, 15, 15, 20, 20, 15, 20,15,15]

            row = 0

            col = 0
            for title in titles1:
                ws4.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws4.set_row(row, 30)
                ws4.set_column(myloc, title_width[col])
                col += 1

            # ws1.freeze_panes(row + 1, 0)
            row += 1
            nitem = 1

            for line in mysalerec:
                ws4.write(row, 0, line.chi_sales_no, okl_content_format)
                ws4.write(row, 1, line.chi_outcome_date if line.chi_outcome_date else ' ', date_format)
                ws4.write(row, 2, line.chi_sales_vat, okl_content_format)
                ws4.write(row, 3, line.chi_currency_type, okl_content_format)
                ws4.write(row, 4, line.proj_sale_name, okl_content_format)
                ws4.write(row, 5, line.chi_wh, okl_content_format)
                ws4.write(row, 6, line.chi_project_no, okl_content_format)
                ws4.write(row, 7, line.chi_cus_order, okl_content_format)
                ws4.write(row, 8, line.chi_paymentdate if line.chi_paymentdate else ' ', date_format)
                ws4.write(row, 9, line.chi_product, okl_content_format)
                ws4.write(row, 10, line.chi_sales_num, okc_content_format)
                ws4.write(row, 11, round(line.chi_sales_price,0) if line.chi_sales_price else 0, okc_content_format)
                mypsalerec.create({'sales_no':line.chi_sales_no,'sales_outdate':line.chi_outcome_date,'sales_cusvat':line.chi_sales_vat,
                                   'sales_currency':line.chi_currency_type,'sales_man':line.proj_sale_name,'sales_wh':line.chi_wh,
                                   'sales_proj_no':line.chi_project_no,'sales_cus_order':line.chi_cus_order,'sales_paymentdate':line.chi_paymentdate,
                                   'sales_prod':line.chi_product,'sales_num':line.chi_sales_num,'sales_price':round(line.chi_sales_price,0)})
                row += 1
                nitem += 1

            wb4.close()
            output.seek(0)
            myxlsfile4 = base64.standard_b64encode(output.getvalue())
            output.close()
            myprojcount = self.env['neweb_chi_invoicing.invoiceopen_excel_download'].search_count([('project_no', '=', projid)])
            if myprojcount > 0:
                myrec = self.env['neweb_chi_invoicing.invoiceopen_excel_download'].search([('project_no', '=', projid)])
                myrec.write({'xls_file': myxlsfile4, 'xls_file_name': myxlsfilename4})
                self.env.cr.execute(
                    """update neweb_chi_invoicing_invoiceopen_excel_download set invoicing_date='%s',invoicing_owner=%d where project_no=%d""" % (
                        self.export_date, myempid, projid))
                self.env.cr.execute("""commit""")
                # self.env.cr.execute("""update neweb_project set chi_export_outcome=True where id=%d""" % projid)
                # self.env.cr.execute("""commit""")
            else:
                myrec = self.env['neweb_chi_invoicing.invoiceopen_excel_download']
                myrec.create({'xls_file': myxlsfile4, 'xls_file_name': myxlsfilename4, 'project_no': projid})
                # self.env.cr.execute("""update neweb_project set chi_export_outcome=True where id=%d""" % projid)
                # self.env.cr.execute("""commit""")
                self.env.cr.execute(
                    """update neweb_chi_invoicing_invoiceopen_excel_download set invoicing_date='%s',invoicing_owner=%d where project_no=%d""" % (
                        self.export_date, myempid, projid))
                self.env.cr.execute("""commit""")

    ################ Package Sales
    def run_package_sale_export(self):
        self.env.cr.execute("""select getexportempid(%d)""" % self.export_user.id)
        myempid = self.env.cr.fetchone()[0]

        output = io.BytesIO()
        mysalerec = self.env['neweb_chi_invoicing.package_sales'].search([])
        if mysalerec:
            myxlsfilename4 = "SALES_%s.xlsx" % datetime.now().strftime("%Y%m%d")
            mysubject = 'SALES_%s.xlsx' %  datetime.now().strftime("%Y%m%d")

            wb8 = xlsxwriter.Workbook(output, {'in_memory': True})
            wb8.set_properties({
                'title': '專案進項資訊',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'NEWEB INFO',
                'company': '藍新資訊股份有限公司',
                'category': '進銷存專案數據',
                'keywords': '進銷存專案數據',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})

            ws8 = wb8.add_worksheet("進銷存成本分析銷項憑證檔(匯整)")

            ########################################
            title_format = wb8.add_format()
            title_format.set_font_size(30)
            title_format.set_bold()
            title_format.set_underline(2)
            title_format.set_font_color('black')
            title_format.set_align('left')
            title_format.set_align('vcenter')
            ########################################
            head_format = wb8.add_format()
            head_format.set_font_size(15)
            head_format.set_border(2)
            head_format.set_font_color('yellow')
            head_format.set_fg_color('blue')
            head_format.set_align('center')
            head_format.set_align('vcenter')
            ########################################
            okc_content_format = wb8.add_format()
            okc_content_format.set_font_size(15)
            okc_content_format.set_border(1)
            okc_content_format.set_font_color('black')
            okc_content_format.set_align('center')
            okc_content_format.set_align('vcenter')
            okc_content_format.set_text_wrap()
            #########################################
            okl_content_format = wb8.add_format()
            okl_content_format.set_font_size(15)
            okl_content_format.set_border(1)
            okl_content_format.set_font_color('black')
            okl_content_format.set_align('left')
            okl_content_format.set_align('vcenter')
            okl_content_format.set_text_wrap()
            #########################################
            ngc_content_format = wb8.add_format()
            ngc_content_format.set_font_size(15)
            ngc_content_format.set_border(1)
            ngc_content_format.set_font_color('red')
            ngc_content_format.set_italic()
            ngc_content_format.set_fg_color('yellow')
            ngc_content_format.set_align('center')
            ngc_content_format.set_align('vcenter')
            ngc_content_format.set_text_wrap()
            ##########################################
            ngl_content_format = wb8.add_format()
            ngl_content_format.set_font_size(15)
            ngl_content_format.set_border(1)
            ngl_content_format.set_font_color('red')
            ngl_content_format.set_italic()
            ngl_content_format.set_fg_color('yellow')
            ngl_content_format.set_align('left')
            ngl_content_format.set_align('vcenter')
            ngl_content_format.set_text_wrap()
            ##########################################
            date_format = wb8.add_format({'num_format': 'yyyy-mm-dd'})
            date_format.set_font_size(15)
            date_format.set_border(1)
            date_format.set_font_color('black')
            date_format.set_align('right')
            date_format.set_align('vcenter')
            date_format.set_text_wrap()

            titles1 = ['單據號碼', '銷貨日期', '客戶編號', '使用幣別', '業務人員', '倉庫編號', '所屬專案' , '自定欄二', '付款日期', '產品編號', '數量', '單價']
            title_width = [20, 15, 15, 15, 15, 15, 20, 20, 15, 20,15,15]

            row = 0

            col = 0
            for title in titles1:
                ws8.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws8.set_row(row, 30)
                ws8.set_column(myloc, title_width[col])
                col += 1

            # ws1.freeze_panes(row + 1, 0)
            row += 1
            nitem = 1

            for line in mysalerec:
                ws8.write(row, 0, line.sales_no, okl_content_format)
                ws8.write(row, 1, line.sales_outdate if line.sales_outdate else ' ', date_format)
                ws8.write(row, 2, line.sales_cusvat, okl_content_format)
                ws8.write(row, 3, line.sales_currency, okl_content_format)
                ws8.write(row, 4, line.sales_man , okl_content_format)
                ws8.write(row, 5, line.sales_wh, okl_content_format)
                ws8.write(row, 6, line.sales_proj_no, okl_content_format)
                ws8.write(row, 7, line.sales_cus_order, okl_content_format)
                ws8.write(row, 8, line.sales_paymentdate if line.sales_paymentdate else ' ', date_format)
                ws8.write(row, 9, line.sales_prod, okl_content_format)
                ws8.write(row, 10, line.sales_num, okc_content_format)
                ws8.write(row, 11, round(line.sales_price,0) if line.sales_price else 0, okc_content_format)

                row += 1
                nitem += 1

            wb8.close()
            output.seek(0)
            myxlsfile4 = base64.standard_b64encode(output.getvalue())
            output.close()
            self.env.cr.execute("""select getpackagesalesprojno()""")
            myprojno = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select getpackdownloadid(%d,'%s')""" % (myempid, '4'))
            mypid = self.env.cr.fetchone()[0]
            myrec = self.env['neweb_chi_invoicing.package_saleinv_excel_download'].search([('id', '=', mypid)])
            myrec.write({'xls_file': myxlsfile4, 'xls_file_name': myxlsfilename4, 'project_no': myprojno,'invoicing_owner':myempid,'invoicing_date':self.export_date})
    ##############################


    def selectbtn(self):                 # 點選匯入
        myrec = self.env['neweb_chi_invoicing.un_export_proj_line'].search([('selectyn','=',True)])
        my_export_type = self.env.context.get('neweb_export_type',False)
        ismaster = self.is_export_project_master        # 勾選成本分析
        isproduct = self.is_export_project_product      # 勾選產品
        issale = self.is_export_project_sale            # 勾選銷貨憑證
        ispurchase = self.is_export_project_purchase    # 勾選進貨憑證
        self.env.cr.execute("""select prerunpackageexport()""")
        if my_export_type == 'S1':       # 整批銷貨憑證匯出
            if ismaster:     # 要產出專案資訊
                for rec in myrec:
                    self.run_project_export(rec.proj_no.id)
                self.run_package_project_export()
            if isproduct:
                for rec in myrec:
                    self.run_product_export(rec.proj_no.id)
                self.run_package_product_export()
            if issale:
                for rec in myrec:
                    self.run_sale_export(rec.proj_no.id)
                self.run_package_sale_export()


        elif my_export_type == 'S2':     # 單筆銷貨憑證匯出
            if ismaster:  # 要產出專案資訊
                for rec in myrec:
                    self.run_project_export(rec.proj_no.id)
            if isproduct:
                for rec in myrec:
                    self.run_product_export(rec.proj_no.id)
            if issale:
                for rec in myrec:
                    self.run_sale_export(rec.proj_no.id)


        elif my_export_type == 'P1':     # 整批進貨憑證匯出
            if ismaster:  # 要產出專案資訊
                for rec in myrec:
                    self.run_project_export(rec.proj_no.id)
                self.run_package_project_export()
            if isproduct:
                for rec in myrec:
                    self.run_product_export(rec.proj_no.id)
                self.run_package_product_export()
            if ispurchase:
                for rec in myrec:
                    self.run_purchase_export(rec.proj_no.id)
                self.run_package_purchase_export()

        elif my_export_type == 'P2':     # 單筆進貨憑證匯出
            if ismaster:  # 要產出專案資訊
                for rec in myrec:
                    self.run_project_export(rec.proj_no.id)
            if isproduct:
                for rec in myrec:
                    self.run_product_export(rec.proj_no.id)
            if ispurchase:
                for rec in myrec:
                    self.run_purchase_export(rec.proj_no.id)
        else:                            # False
            A= 'S5'

        if my_export_type=='P1' or my_export_type=='S1' :
            myviewid = self.env.ref('neweb_chi_invoicing.view_neweb_chi_invoicing_package_download_tree')

            return {
                'view_name': 'newebinvoicingexportpackagewizard',
                'name': ('進銷存EXCEL整批匯出'),
                'type': 'ir.actions.act_window',
                'res_model': 'neweb_chi_invoicing.package_excel_download',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'current'}
        else:
            myviewid = self.env.ref('neweb_chi_invoicing.view_neweb_chi_invoicing_download_tree')

            return {
                'view_name': 'newebinvoicingexportwizard',
                'name': ('進銷存EXCEL匯出'),
                'type': 'ir.actions.act_window',
                'res_model': 'neweb_chi_invoicing.excel_download',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'current'}


class newebchiinvoicingunexportprojline(models.Model):
    _name = "neweb_chi_invoicing.un_export_proj_line"
    _description = "生成未匯出專案數據暫存明細檔"


    export_id = fields.Many2one('neweb_chi_invoicing.un_export_proj',required=True,ondelete="cascade")
    proj_no = fields.Many2one('neweb.project',string="專案編號")
    partner_id = fields.Many2one('res.partner',string="專案客戶")
    amount_untaxed = fields.Float(digits=(11,2),string="未稅金額")
    amount_tax = fields.Float(digits=(10,2),string="稅金")
    amount_total = fields.Float(digits=(12,2),string="合計金額")
    export_memo = fields.Text(string="匯出說明",default=' ')
    chi_export_project = fields.Boolean(string="匯出專案否?", default=False)
    chi_export_product = fields.Boolean(string="匯出產品否?", default=False)
    chi_export_outcome = fields.Boolean(string="匯出銷項否?", default=False)
    chi_export_income = fields.Boolean(string="匯出進項否？", default=False)
    chi_invoice_complete = fields.Boolean(string="結案否?", default=False)
    selectyn = fields.Boolean(default=False,string="選")


    # @api.multi
    def get_select(self):
        for rec in self:
            if rec.selectyn == True:
                rec.update({'selectyn': False})
            else:
                rec.update({'selectyn': True})


class newebchiinvoicingunexportprojlog(models.Model):
    _name = "neweb_chi_invoicing.export_proj_log"
    _description = "生成匯出專案數據記錄"

    project_no = fields.Many2one('neweb.project',string="專案編號")
    export_user = fields.Many2one('res.users',string="匯出人員")
    export_date = fields.Date(string="匯出日期")
    is_export_project_master = fields.Boolean(string="匯出成本分析主檔？",default=False)
    is_export_project_product = fields.Boolean(string="匯出成本分析產品檔？",default=False)
    is_export_project_sale = fields.Boolean(string="匯出成本分析銷項記錄檔？",default=True)
    is_export_project_purchase = fields.Boolean(string="匯出成本分析進項記錄檔？",default=True)
