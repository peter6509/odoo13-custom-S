# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime, pytz
import io
import base64
from datetime import datetime,timedelta,date
import xlsxwriter


class ERAReportWizard(models.TransientModel):
    _name = "era_household.month_report_wizard"

    @api.depends()
    def _get_billym(self):
        myrec = self.env['era.household_config'].search([])
        if myrec:
            # mybillm = myrec.bill_ym[5:7]
            # mybilly = myrec.bill_ym[0:4]
            # if mybillm=='01':
            #    mybillym = str(int(mybilly) - 1)+ '-12'
            # else:
            #    mybillym = mybilly + '-' + (str(int(mybillm) - 1)).zfill(2)
            mybillym = myrec.bill_ym
            self.bill_ym = mybillym
            return mybillym

    bill_ym = fields.Char(string="對帳年月",required=True,default=_get_billym)
    house_id = fields.Many2one('era.household_house',string="案場名稱",required=True)
    report_type = fields.Selection([('1','對帳報表PDF'),('2','對帳報表EXCEL')],string="輸出型態",default='1')


    def era_month_print(self):

        if self.report_type=='1':  # PDF對帳單
            data = dict()
            mybillm = self.bill_ym[5:7]
            mybilly = self.bill_ym[0:4]
            if mybillm == '01':
                mybillym = str(int(mybilly) - 1) + '-12'
            else:
                mybillym = mybilly + '-' + (str(int(mybillm) - 1)).zfill(2)
            data["bill_ym"] = mybillym
            data["bill_ym1"] = self.bill_ym
            data["house_id"] = self.house_id.id
            data["project_no"] = self.house_id.project_no
            return self.env.ref('era_household.action_era_mmonth_report').report_action(self, data=data)
        else:                  # EXCEL 對帳單
            # mybillm = self.bill_ym[5:7]
            # mybilly = self.bill_ym[0:4]
            # if mybillm == '01':
            #     mybillym = str(int(mybilly) - 1) + '-12'
            # else:
            #     mybillym = mybilly + '-' + (str(int(mybillm) - 1)).zfill(2)
            # date_format = xlsxwriter.Workbook({'num_format':'mmmm d yyyy'})
            mybillym = self.bill_ym
            month_rec = self.env['era.household_house_line'].search([])
            output = io.BytesIO()
            myxlsfilename = "ERA租戶月費用對帳報表_%s.xlsx" % datetime.now().strftime("%Y%m%d")
            mysubject = 'ERA租戶月費用對帳報表_%s.xlsx' % datetime.now().strftime("%Y%m%d")
            wb = xlsxwriter.Workbook(output, {'in_memory': True})

            wb.set_properties({
                'title': 'ERA租戶月費用對帳報表',
                'subject': mysubject,
                'author': '%s' % self.env.user.name,
                'manager': 'ERA',
                'company': 'ERA',
                'category': '對帳報表',
                'keywords': '對帳報表',
                'created': datetime.now(),
                'comments': 'Created By Odoo'})
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
            okr_content_format = wb.add_format()
            okr_content_format.set_font_size(15)
            okr_content_format.set_border(1)
            okr_content_format.set_font_color('black')
            okr_content_format.set_align('right')
            okr_content_format.set_align('vcenter')
            okr_content_format.set_text_wrap()
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
            titles = ['房號', '租戶', '起租日', '啟始日', '截止日', '前期餘額', '電費', '房屋租金', '房屋管理費','車位租金','車位管理費','機車位管理費','水費','應繳總額','繳費','繳費日期','繳費金額','繳費說明']
            title_width = [10, 20, 15, 15, 15, 18, 18, 18, 18,18,18,18,10,20,10,18,18,30]
            nnum = 1
            ws = {}
            ws = wb.add_worksheet("ERA(%s)-%s對帳單" % (month_rec[0].house_id.project_no,mybillym))
            ########################################
            row = 0
            col = 0
            for title in titles:
                ws.write(row, col, title, head_format)
                myloc = "%s:%s" % (chr(65 + col), chr(65 + col))
                ws.set_row(row, 30)
                ws.set_column(myloc, title_width[col])
                col += 1
                ws.freeze_panes(row + 1, 0)
            for rec in month_rec:
                row += 1
                nitem = 1
                myattsum = 0.00
                myattsum1 = 0.00
                if rec.is_payment:
                    self.env.cr.execute("""select getpaymentamount('%s',%d)""" % (mybillym, rec.id))
                    paymentamount = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""select getpaymentdate('%s',%d)""" % (mybillym, rec.id))
                    paymentdate = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""select getpaymentdesc('%s',%d)""" % (mybillym, rec.id))
                    paymentdesc = self.env.cr.fetchone()[0]
                else:
                    paymentamount = ' '
                    paymentdate= ' '
                    paymentdesc= ' '
                self.env.cr.execute("""select getstartrental(%d)""" % rec.id)
                startrental = self.env.cr.fetchone()[0]
                self.env.cr.execute("""select getbsdate(%d)""" % rec.id)
                billstartdate = self.env.cr.fetchone()[0]
                self.env.cr.execute("""select getbedate(%d)""" % rec.id)
                billenddate = self.env.cr.fetchone()[0]

                if rec.is_payment:
                    ispayment='已繳'
                else:
                    ispayment=' '

                if not rec.uncomplete_fee:
                    uncompletefee = 0
                else:
                    uncompletefee = rec.uncomplete_fee
                if not rec.current_emeter_fee:
                    currentemeterfee = 0
                else:
                    currentemeterfee = rec.current_emeter_fee
                if not rec.house_rental_fee:
                    houserentalfee = 0
                else:
                    houserentalfee = rec.house_rental_fee
                if not rec.house_management_fee:
                    housemanagementfee = 0
                else:
                    housemanagementfee = rec.house_management_fee
                if not rec.parking_space_rent:
                    parkingspacerent = 0
                else:
                    parkingspacerent = rec.parking_space_rent
                if not rec.parking_management:
                    parkingmanagement = 0
                else:
                    parkingmanagement = rec.parking_management
                if not rec.lo_parking_management:
                    loparkingmanagement=0
                else:
                    loparkingmanagement = rec.lo_parking_management
                if not rec.water_fee:
                    waterfee =0
                else:
                    waterfee = rec.water_fee

                currenttotalfee = uncompletefee + currentemeterfee + houserentalfee + housemanagementfee + parkingspacerent + parkingmanagement + loparkingmanagement + waterfee

                ws.write(row, 0, rec.house_no if rec.house_no else ' ', okl_content_format)
                ws.write(row, 1, rec.member_id.member_name if rec.member_id.member_name else ' ', okl_content_format)
                ws.write(row, 2, startrental, okl_content_format)
                ws.write(row, 3, billstartdate ,okl_content_format)
                ws.write(row, 4, billenddate ,okl_content_format)
                ws.write(row, 5, rec.uncomplete_fee if rec.uncomplete_fee else ' ', okr_content_format)
                ws.write(row, 6, rec.current_emeter_fee if rec.current_emeter_fee else ' ',okr_content_format)
                ws.write(row, 7, rec.house_rental_fee if rec.house_rental_fee else ' ', okr_content_format)
                ws.write(row, 8, rec.house_management_fee if rec.house_management_fee else ' ', okr_content_format)
                ws.write(row, 9, rec.parking_space_rent if rec.parking_space_rent else ' ' , okr_content_format)
                ws.write(row, 10, rec.parking_management if rec.parking_management else ' ' , okr_content_format)
                ws.write(row, 11, rec.lo_parking_management if rec.lo_parking_management else ' ' , okr_content_format)
                ws.write(row, 12, rec.water_fee if rec.water_fee else ' ', okr_content_format)
                ws.write(row, 13, currenttotalfee, okr_content_format)
                ws.write(row, 14, ispayment, okc_content_format)
                ws.write(row, 15, paymentdate if paymentdate else ' ', okl_content_format)
                ws.write(row, 16, paymentamount if paymentamount else ' ', okr_content_format)
                ws.write(row, 17, paymentdesc if paymentdesc else ' ', okl_content_format)
            wb.close()
            output.seek(0)
            myxlsfile = base64.standard_b64encode(output.getvalue())
            output.close()
            myrec = self.env['era.excel_download']

            myrec.create({'xls_file': myxlsfile, 'xls_file_name': myxlsfilename,})
            myviewid = self.env.ref('era_household.era_excel_download_tree')

            return {
                'view_name': 'era_excel_download',
                'name': (u'租戶月對帳匯出'),
                'type': 'ir.actions.act_window',
                'res_model': 'era.excel_download',
                'view_id': myviewid.id,
                'flags': {'action_buttons': True},
                'view_type': 'form',
                'view_mode': 'tree',
                'target': 'main'}


