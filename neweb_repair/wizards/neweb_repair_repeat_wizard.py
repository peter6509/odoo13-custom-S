# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import io
import base64
from datetime import timedelta,datetime
from odoo.exceptions import UserError
import xlsxwriter

class newebrepairrepeatcallwizard(models.TransientModel):
    _name = "neweb_repair.repair_repeat_call_wizard"

    repair_start = fields.Date(string="報修啟始日期",requires=True)
    repair_end = fields.Date(string="報修截止日期",requires=True)
    repeat_num = fields.Integer(string="大於等於次數",default=2,requires=True)

    def run_repeat_call(self):
        self.env.cr.execute("""select runrepeatcall('%s','%s',%d)""" % (self.repair_start,self.repair_end,self.repeat_num))

        output = io.BytesIO()
        myxlsfilename3 = "REPEAT_CALL_%s-%s_%s%d.xlsx" % (
        self.repair_start, self.repair_end, '次數大於等於', self.repeat_num)
        mysubject = "REPEAT_CALL_%s-%s_%s%d.xlsx" % (self.repair_start, self.repair_end, '次數大於等於', self.repeat_num)

        wb = xlsxwriter.Workbook(output, {'in_memory': True})
        wb.set_properties({
            'title': 'Repair Repeat Call 資訊',
            'subject': mysubject,
            'author': '%s' % self.env.user.name,
            'manager': 'NEWEB INFO',
            'company': '藍新資訊股份有限公司',
            'category': '客戶報修數據',
            'keywords': '客戶報修數據',
            'created': datetime.now(),
            'comments': 'Created By Odoo'})

        ws = wb.add_worksheet("Repair Repeat Call Info")

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
        okc_content_format.set_font_color('green')
        okc_content_format.set_align('center')
        okc_content_format.set_align('vcenter')
        okc_content_format.set_text_wrap()
        #########################################
        okl_content_format = wb.add_format()
        okl_content_format.set_font_size(15)
        okl_content_format.set_border(1)
        okl_content_format.set_font_color('green')
        okl_content_format.set_align('left')
        okl_content_format.set_align('vcenter')
        okl_content_format.set_text_wrap()
        #########################################
        ngc_content_format = wb.add_format()
        ngc_content_format.set_font_size(15)
        ngc_content_format.set_border(1)
        ngc_content_format.set_font_color('red')
        # ngc_content_format.set_italic()
        # ngc_content_format.set_fg_color('yellow')
        ngc_content_format.set_align('center')
        ngc_content_format.set_align('vcenter')
        ngc_content_format.set_text_wrap()
        ##########################################
        ngl_content_format = wb.add_format()
        ngl_content_format.set_font_size(15)
        ngl_content_format.set_border(1)
        ngl_content_format.set_font_color('red')
        # ngl_content_format.set_italic()
        # ngl_content_format.set_fg_color('yellow')
        ngl_content_format.set_align('left')
        ngl_content_format.set_align('vcenter')
        ngl_content_format.set_text_wrap()
        ##########################################

        titles1 = ['報修單號', '報修時間', '終端客戶', '派工工程師', '機器序號', '機型', '次數', '期間總次數','問題描述','處理說明']
        title_width = [30, 30, 30, 30, 30, 30, 30, 30,90,90]
        row = 0
        col = 0
        row = 0

        mytitle = "報修 REPEAT CALL 檢視表(%s - %s)%s%d" % (self.repair_start, self.repair_end,'總次數大於等於 ',self.repeat_num)
        ws.write(row, 1, mytitle, title_format)
        row += 2
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
        myrepeatcallrec = self.env['neweb_repair.repeat_call_report'].search([])
        for line in myrepeatcallrec:
            mydate = fields.Datetime.from_string(line.repair_datetime)
            myrepairdatetime = (mydate + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')
            # if (line.tot_amount % 2) > 0:
            #     ws.write(row, 0, line.name if line.name else ' ', okl_content_format)
            #     ws.write(row, 1, myrepairdatetime if myrepairdatetime else ' ', okl_content_format)
            #     ws.write(row, 2, line.end_customer.name if line.end_customer else ' ', okl_content_format)
            #     ws.write(row, 3, line.ae_id.name if line.ae_id else ' ', okl_content_format)
            #     ws.write(row, 4, line.prod_serial_no if line.prod_serial_no else ' ', okl_content_format)
            #     ws.write(row, 5, line.prod_serial if line.prod_serial else ' ', okl_content_format)
            #     ws.write(row, 6, line.device_amount if line.device_amount else ' ', okc_content_format)
            #     ws.write(row, 7, line.tot_amount if line.tot_amount else ' ', okc_content_format)
            # else:
            ws.write(row, 0, line.name if line.name else ' ', ngl_content_format)
            ws.write(row, 1, myrepairdatetime if myrepairdatetime else ' ', ngl_content_format)
            ws.write(row, 2, line.end_customer.name if line.end_customer else ' ', ngl_content_format)
            ws.write(row, 3, line.ae_id.name if line.ae_id else ' ', ngl_content_format)
            ws.write(row, 4, line.prod_serial_no if line.prod_serial_no else ' ', ngl_content_format)
            ws.write(row, 5, line.prod_serial if line.prod_serial else ' ', ngl_content_format)
            ws.write(row, 6, line.device_amount if line.device_amount else ' ', ngc_content_format)
            ws.write(row, 7, line.tot_amount if line.tot_amount else ' ', ngc_content_format)
            ws.write(row, 8, line.problem_desc if line.problem_desc else ' ', ngl_content_format)
            ws.write(row, 9, line.process_desc if line.process_desc else ' ', ngl_content_format)
            row += 1
            nitem += 1

        wb.close()
        output.seek(0)
        myxlsfile = base64.standard_b64encode(output.getvalue())
        output.close()


        myrec = self.env['neweb_repair.repeatcall_excel_download']
        myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename3})

        myviewid = self.env.ref('neweb_repair.view_repeatcall_download_tree')

        return {
            'view_name': 'newebrepairrepeatcallwizard',
            'name': ('REPEAT CALL EXCEL 匯出'),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb_repair.repeatcall_excel_download',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}

