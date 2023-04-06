# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api, _
from odoo.exceptions import UserError
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter
import json,logging,re
from lxml import etree

class newebpartnerexportwizard2(models.TransientModel):
    _name = "neweb.partner_export_wizard2"
    _description = "匯出藍新所有客戶資料"

    pass_code = fields.Char(string="PASSCODE",required=True)


    def run_allpartner_export(self):
        if self.pass_code != 'irene.cheng@newebinfo.com.tw':
            raise UserError("PASSCODE 不正確")
        self.env.cr.execute("""select genallpartnerlist()""")
        self.env.cr.execute("""commit""")
        mypartnerrec = self.env['neweb.partner_list'].search([])
        output = io.BytesIO()

        myxlsfilename = "PARTNER_ALL_%s.xlsx" % ( datetime.now().strftime("%Y%m%d"))
        mysubject = 'PARTNER_ALL_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))
        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': '業務員客戶資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '藍新資訊所有客戶資訊',
            'keywords': '藍新資訊所有客戶資訊',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})
        ws = wb.add_worksheet("藍新資訊所有客戶資訊檔")
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


        titles1 = ['業務代表','客戶名稱', '統一編號', '電話', '地址', '聯絡人', '人員別', '職稱', '聯絡人電話', '聯絡人手機', '聯絡人EMAIL',
                   '生日', '備註']
        title_width = [60, 45, 20, 25, 100, 20, 30, 20, 25, 25, 35, 15, 60]

        row = 0

        col = 0
        for title in titles1:
            ws.write(row, col, title, head_format)
            myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
            ws.set_row(row, 30)
            ws.set_column(myloc, title_width[col])
            col += 1

        ws.freeze_panes(row + 1, 0)
        row += 1
        nitem = 1

        for line in mypartnerrec:
            mycontacttype = line.contact_type.name
            ws.write(row, 0, line.sales if line.sales else ' ', okl_content_format)
            ws.write(row, 1, line.cus_name if line.cus_name else ' ', okl_content_format)
            ws.write(row, 2, line.vat if line.vat else ' ', okl_content_format)
            ws.write(row, 3, line.tel if line.tel else ' ', okl_content_format)
            ws.write(row, 4, line.address if line.address else ' ', okl_content_format)
            ws.write(row, 5, line.contact if line.contact else ' ', okl_content_format)
            ws.write(row, 6, line.contact_type.name if line.contact_type else ' ', okl_content_format)
            ws.write(row, 7, line.function if line.function else ' ', okl_content_format)
            ws.write(row, 8, line.tel1 if line.tel1 else ' ', okl_content_format)
            ws.write(row, 9, line.mobile if line.mobile else ' ', okl_content_format)
            ws.write(row, 10, line.email if line.email else ' ', okl_content_format)
            ws.write(row, 11, line.birthday if line.birthday else ' ', okc_content_format)
            ws.write(row, 12, line.comment if line.comment else ' ', okl_content_format)

            row += 1
            nitem += 1


        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()


        myrec = self.env['neweb.export_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename})

        myviewid = self.env.ref('neweb_projext.partner_export_download_tree')

        return {
            'view_name': 'newebpartnerexportdownload',
            'name': ('客戶資訊EXCEL匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb.export_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
    #     if context is None:
    #         context = {}
    #     res = super(newebpartnerexportwizard, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
    #                                                               submenu=submenu)
    #
    #     doc = etree.XML(res['arch'])
    #     if view_type == 'form':
    #         for node in doc.xpath("//field[@name='emp_id']"):
    #             if self.env['res.users'].has_group('neweb_project.neweb_sa40_user'):
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['invisible'] = True
    #                 node.set("modifiers", json.dumps(modifiers))
    #             elif self.env['res.users'].has_group('neweb_project.neweb_sa50_assi'):
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['invisible'] = False
    #                 node.set("modifiers", json.dumps(modifiers))
    #             elif self.env['res.users'].has_group('neweb_project.neweb_sa30_ass'):
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['invisible'] = False
    #                 node.set("modifiers", json.dumps(modifiers))
    #             else:
    #                 modifiers = json.loads(node.get("modifiers"))
    #                 modifiers['invisible'] = False
    #                 node.set("modifiers", json.dumps(modifiers))
    #
    #     res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res


