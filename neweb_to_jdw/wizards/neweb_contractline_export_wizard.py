# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
# from odoo.addons import decimal_precision as dp
from datetime import datetime,timedelta,date
import xlsxwriter

class newebcontractlineexportjdwwizard(models.TransientModel):
    _name = "neweb_to_jdw.contractline_export_wizard"
    _description = "合約明細匯出給觔斗雲"

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.export_user = self.env.user.id

    contract_no = fields.Char(string="合約編號")
    start_date = fields.Date(string="異動起始日")
    end_date = fields.Date(string="異動截止日")
    export_user = fields.Many2one('res.users', string="匯出人員")
    export_date = fields.Datetime(string="匯出日期時間",default=datetime.today())

    def run_contractline_export(self):
        if self.contract_no:
            self.env.cr.execute("""select getjdwexportcontractline1('%s')""" % self.contract_no)
            myconid = self.env.cr.fetchone()[0]
            mycon_rec = self.env['neweb_contract.contract'].search([('id', '=', myconid)])
        else:
            self.env.cr.execute("""select getjdwexportcontractline('%s','%s')""" % (self.start_date,self.end_date))
            myconid = self.env.cr.fetchall()
            mycon_rec = self.env['neweb_contract.contract'].search([('id', 'in', myconid)])

        output = io.BytesIO()

        myxlsfilename1 = "合約明細資料_%s.xlsx" % (datetime.now().strftime("%Y%m%d"))
        mysubject = '合約明細資料_%s.xlsx' % (datetime.now().strftime("%Y%m%d"))

        wb1 = xlsxwriter.Workbook(output, {'in_memory': True})
        wb1.set_properties({
            'title': '合約列表資料(匯出For筋斗雲)',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '合約列表資料(匯出For筋斗雲)',
            'keywords': '合約列表資料(匯出For筋斗雲)',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws1 = wb1.add_worksheet("合約列表資料(匯出For筋斗雲)")

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

        titles1 = ['合約編號','設備編號','合約起日','合約迄日','定保週期','保養週期起算月份','金額','說明','不進行定保(Y/N)']
        title_width = [20, 20, 15,15,20,25,25,40,25]

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

        for line in mycon_rec:
            for line1 in line.contract_line_ids:
                ws1.write(row, 0, line.name if line.name else ' ', okl_content_format)
                ws1.write(row, 1, line1.machine_serial_no if line1.machine_serial_no else ' ', okl_content_format)
                ws1.write(row, 2, line.maintenance_start_date if line.maintenance_start_date else ' ', date_format)
                ws1.write(row, 3, line.maintenance_end_date if line.maintenance_end_date else ' ', date_format)
                mymethod = ' '
                mypm = 'Y'
                if line.inspection_method == 'monthly':
                    mymethod = '每月'
                    mypm = 'N'
                elif line.inspection_method == 'quarterly':
                    mymethod = '每季'
                    mypm = 'N'
                elif line.inspection_method == 'bimonthly':
                    mymethod = '雙月'
                    mypm = 'N'
                elif line.inspection_method == 'semiannually':
                    mymethod = '半年'
                    mypm = 'N'
                elif line.inspection_method == 'annually':
                     mymethod = '每年'
                     mypm = 'N'
                elif line.inspection_method == 'remote':
                     mymethod = '遠端'
                     mypm = 'Y'
                ws1.write(row, 4, mymethod if mymethod else ' ',okl_content_format)
                self.env.cr.execute("""select getconsmonth(%d)""" % line.id)
                mysmonth = self.env.cr.fetchone()[0]
                ws1.write(row, 5, mysmonth if mysmonth else ' ', okl_content_format)
                ws1.write(row, 6, 0, okl_content_format)
                ws1.write(row, 7, line1.memo if line1.memo else ' ', okl_content_format)
                ws1.write(row, 8, mypm,okl_content_format)

                row += 1
                nitem += 1

        wb1.close()
        output.seek(0)
        myxlsfile1 = base64.standard_b64encode(output.getvalue())
        output.close()

        myrec = self.env['neweb_to_jdw.excel_download'].search([])
        myrec.create({'export_date':self.export_date,'export_owner':self.env.user.id,'download_type':'4','xls_file': myxlsfile1, 'xls_file_name': myxlsfilename1})

        myviewid = self.env.ref('neweb_to_jdw.view_jdw_download_tree')

        return {
            'view_name': 'neweb_custom_to_jdw',
            'name': ('合約明細資料匯出給觔斗雲'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_to_jdw.excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}



