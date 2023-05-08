# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class newebdevexportjdwwizard(models.TransientModel):
    _name = "neweb_to_jdw.dev_export_wizard"
    _description = "設備明細匯出給觔斗雲"

    @api.depends()
    def _get_current_user(self):
        self.export_user = self.env.user.id
        return self.env.user.id

    start_date = fields.Date(string="異動起始日")
    end_date = fields.Date(string="異動截止日")
    export_user = fields.Many2one('res.users', string="匯出人員")
    export_date = fields.Datetime(string="匯出日期時間",default=datetime.today())

    def run_dev_export(self):
        self.env.cr.execute("""select getjdwexportdev('%s','%s')""" % (self.start_date,self.end_date))
        myconid = self.env.cr.fetchall()

        output = io.BytesIO()
        mydev_rec = self.env['neweb_contract.contract.line'].search([('id', 'in', myconid)],order='contract_id,id')


        myxlsfilename1 = "設備資料_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
        mysubject = '設備資料_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '設備資料(匯出For筋斗雲)',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '設備資料(匯出For筋斗雲)',
            'keywords': '設備資料(匯出For筋斗雲)',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet("設備資料(匯出For筋斗雲)")

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

        titles1 = ['設備名稱', '設備編號', '廠牌','櫃位','負責部門','啟用狀態','客戶類型','客戶編號','工程師','SLA規範','合約啟始日','合約截止日','服務時段','負責工程師','定期維護條款','維修技能','設備安裝地點','備註','合約編號']
        title_width = [20, 20, 15,15,20,15,15,15,20,15,20,20,20,20,20,20,20,20,20]

        row = 0
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

        for line in mydev_rec:
            ws1.write(row, 0, line.prod_modeltype if line.prod_modeltype else ' ', okl_content_format)
            ws1.write(row, 1, line.machine_serial_no if line.machine_serial_no else ' ', okl_content_format)
            ws1.write(row, 2, line.prod_brand.name if line.prod_brand.name else ' ', okl_content_format)
            ws1.write(row, 3, line.rack_loc if line.rack_loc else ' ', okl_content_format)
            self.env.cr.execute("""select getcondepartment(%d)""" % line.contract_id.id)
            mydepartment = self.env.cr.fetchone()[0]
            ws1.write(row,4, mydepartment if mydepartment else ' ',okl_content_format)
            ws1.write(row,5, '啟用',okl_content_format)
            ws1.write(row,6,'公司',okl_content_format)
            ws1.write(row, 7, line.contract_id.end_customer.vat if line.contract_id.end_customer.vat else ' ', okl_content_format)
            self.env.cr.execute("""select getcontractae1(%d)""" % line.contract_id.id)
            myae1 = self.env.cr.fetchone()[0]
            ws1.write(row, 8, myae1 if myae1 else ' ', okl_content_format)
            self.env.cr.execute("""select getslabrief(%d)""" % line.contract_id.sla.id)
            myslabrief = self.env.cr.fetchone()[0]
            ws1.write(row, 9, myslabrief if myslabrief else ' ', okl_content_format)
            ws1.write(row, 10, line.contract_id.maintenance_start_date if line.contract_id.maintenance_start_date else ' ', date_format)
            ws1.write(row, 11, line.contract_id.maintenance_end_date if line.contract_id.maintenance_end_date else ' ', date_format)
            ws1.write(row, 12, line.contract_id.main_service_rule_new.name if line.contract_id.main_service_rule_new.name else ' ', okl_content_format)
            ws1.write(row, 13, myae1 if myae1 else ' ', okl_content_format)
            ws1.write(row, 14, line.contract_id.routine_maintenance_new.name if line.contract_id.routine_maintenance_new.name else ' ', okl_content_format)
            ws1.write(row, 15, ' ', okl_content_format)
            ws1.write(row, 16, line.machine_loc if line.machine_loc else ' ', okl_content_format)
            ws1.write(row, 17, ' ', okl_content_format)
            ws1.write(row, 18, line.contract_id.name if line.contract_id.name else ' ', okl_content_format)
            row += 1
            nitem += 1

        wb1.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()

        myrec = self.env['neweb_to_jdw.excel_download'].search([])
        myrec.create({'export_date':self.export_date,'export_owner':self.env.user.id,'download_type':'2','xls_file': myxlsfile1, 'xls_file_name': myxlsfilename1})

        myviewid = self.env.ref('neweb_to_jdw.view_jdw_download_tree')

        return {
            'view_name': 'neweb_custom_to_jdw',
            'name': ('設備資料匯出給觔斗雲'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_to_jdw.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



