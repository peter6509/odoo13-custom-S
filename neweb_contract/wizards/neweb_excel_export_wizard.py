# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
import datetime
import xlsxwriter
import base64,io
from odoo.exceptions import UserError
from datetime import datetime,timedelta,date

class excelexportwizard(models.TransientModel):
    _name = "neweb_contract.excel_export_wizard"

    main_due_date = fields.Date(string="維護到期日",required=True)
    contract_sales = fields.Many2many('hr.employee','neweb_contract_hr_employee_rel','wid','eid',string="業務代表")
    contract_eng = fields.Many2many('hr.employee','neweb_contract1_hr_employee_rel','wid','eid',string="工程師")
    export_memo = fields.Char(string="匯出檔案說明",required=True)


    @api.onchange('main_due_date')
    def onchangeclient(self):
        res = {}
        myowner = self.env['res.users'].search([('id','=',self.env.uid)])
        mysales = self.env.user.employee_ids.id
        if myowner.env.user.has_group('neweb_project.neweb_sa40_user') and self.env.uid != 1:
           res['domain'] = {'contract_sales': [('department_id','in',(151,152,164,165,166)),
                                             ('id', '=', mysales)],
                            'contract_eng': [('department_id','not in',(151,152,164,165,166))]}
        else:
           res['domain'] = {'contract_sales': [('department_id', 'in', (151, 152, 164, 165, 166))],
                            'contract_eng': [('department_id', 'not in', (151, 152, 164, 165, 166))]}
        return res

    def gen_custom_export(self):
        myowner = self.env['res.users'].search([('id', '=', self.env.uid)])
        mysales = self.env.user.employee_ids.id
        if myowner.env.user.has_group('neweb_project.neweb_sa40_user') and self.env.uid != 1 and not self.contract_sales:
           raise UserError("未輸入業務代表")
        self.env.cr.execute("""delete from neweb_contract_custom_excel_data ;""")

        mynum = 0
        for rec in self.contract_sales:
            mynum = mynum + 1
            self.env.cr.execute("""select gen_contract_custom_data('%s',%d)""" % (self.main_due_date,rec.id))
        if mynum == 0 :
            self.env.cr.execute("""select gen_contract_custom_data('%s',%d)""" % (self.main_due_date, 0))
        self.env.cr.execute("""delete from neweb_contract_excel_export_wizard""")
        # import xlwt
        output = io.BytesIO()
        wb = xlsxwriter.Workbook(output, {'in_memory': True})

        mysubject = '合約匯出記錄_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))
        wb.set_properties({
            'title': '合約記錄匯出精靈',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB',
            'company': 'NEWEB',
            'category': '合約記錄',
            'keywords': '合約記錄',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("NEWEB合約記錄記錄")
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
        titles = [ "合約編號","維護到期日","客戶名稱","業務","客戶聯絡人","滿意度勾選*","客戶聯絡人電郵","客戶聯絡人電話","終端客戶名稱","終端客戶聯絡人","滿意度勾選*","終端客戶電郵","終端客戶電話"]
        title_width = [72,36,72,72,36,36,72,72,72,36,36,72,72]

        row = 1
        ws.write(row, 0, "##查詢條件1:", okl_content_format)
        ws.write(row, 1, "維護到期日%s以後" % (self.main_due_date), okl_content_format)
        ws.write(row, 3, "##查詢條件2:", okl_content_format)
        if not self.contract_sales:
            ws.write(row, 4, "全業務", okl_content_format)
        else:
            ws.write(row, 4, "%s" % (self.contract_sales[0].resource_id.name), okl_content_format)
        # ws.row(row).height = 300
        row += 2

        col = 0
        for title in titles:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        # nitem = 1
        # nsum = 0
        mycontractrec = self.env['neweb_contract.custom_excel_data'].search([])
        try:
            mycontractrec.sorted(key=lambda r: (r.contact1,r.contact9,r.contact5))
        except Exception as inst:
            mycontractrec.sorted(key=lambda r: r.contact1)
        row += 1
        mycontractno = ''
        mycusname = ''
        myendcusname = ''
        myendcustom1 = ''
        for line in mycontractrec:
            if mycontractno == line.contact1 and mycusname == line.contact5 and myendcusname == line.contact9:
                continue
            if line.contact1 and mycontractno != line.contact1:
                ws.write(row, 0, line.contact1, okl_content_format)
                ws.write(row, 1, line.contact2, okl_content_format)
                ws.write(row, 2, line.contact3.name, okl_content_format)
                ws.write(row, 3, line.contact4.resource_id.name, okl_content_format)
                mycontractno = line.contact1
            else:
                ws.write(row, 0, ' ', okl_content_format)
                ws.write(row, 1, ' ', okl_content_format)
                ws.write(row, 2, ' ', okl_content_format)
                ws.write(row, 3, ' ', okl_content_format)
            if line.contact5 and mycusname != line.contact5:
                ws.write(row, 4, line.contact5, okl_content_format)
                ws.write(row, 5, line.contact12, okl_content_format)
                ws.write(row, 6, line.contact6, okl_content_format)
                ws.write(row, 7, line.contact7, okl_content_format)
                mycusname = line.contact5
            else:
                ws.write(row, 4, ' ', okl_content_format)
                ws.write(row, 5, ' ', okl_content_format)
                ws.write(row, 6, ' ', okl_content_format)
                ws.write(row, 7, ' ', okl_content_format)
            if myendcustom1 != line.contact8 and line.contact3 != line.contact8:
                ws.write(row, 8, line.contact8.name, okl_content_format)
                myendcustom1 = line.contact8
            else:
                ws.write(row, 8, ' ', okl_content_format)
            if line.contact8 and myendcusname != line.contact9:
                ws.write(row, 9, line.contact9, okl_content_format)
                ws.write(row, 10, line.contact13, okl_content_format)
                ws.write(row, 11, line.contact10, okl_content_format)
                ws.write(row, 12, line.contact11, okl_content_format)
                myendcusname = line.contact9
            else:
                ws.write(row, 9, ' ', okl_content_format)
                ws.write(row, 10, ' ', okl_content_format)
                ws.write(row, 11, ' ', okl_content_format)
                ws.write(row, 12, ' ', okl_content_format)
            row += 1
        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()

        myxlsfilename = "合約匯出記錄_%s-%s.xlsx" % (self.main_due_date, self.export_memo)

        myrec = self.env['neweb_contract.custom_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})
        myviewid1 = self.env.ref('neweb_contract.neweb_contract_excel_download_view_tree')
        return {
            'view_name': 'ContractDataWizard',
            'name': ('合約客戶聯絡人資料'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_contract.custom_excel_download',
            'view_id': myviewid1.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}


