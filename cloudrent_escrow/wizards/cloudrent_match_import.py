# -*- coding: utf-8 -*-
# Author: Peter Wu

import base64
import xlrd
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import sys
from datetime import datetime

XL_CELL_EMPTY = 0
XL_CELL_TEXT = 1
XL_CELL_NUMBER = 2
XL_CELL_DATE = 3
XL_CELL_BOOLEAN = 4
XL_CELL_ERROR = 5
XL_CELL_BLANK = 6


class CloudRentMatchImpor(models.TransientModel):
    _name = "cloudrent.match_import_wizard"
    _description = " 媒合合約CSV匯入"

    excel_file = fields.Binary(string="上傳EXCEL檔案",attachment=False)
    sheet_num = fields.Integer(string="工作底稿(序)",default=0,required=True)
    escrow_agent = fields.Many2one('cloudrent.escrow',string="所屬代管業者",required=True)
    admin_area = fields.Selection([('1', '台北市'), ('2', '新北市'), ('3', '桃園市'), ('4', '台中市'), ('5', '台南市'), ('6', '高雄市')],string="所屬行政區")
    case_type = fields.Selection([('1', '包租/包管'), ('2', '代租/代管')], string="案件類型")
    start_row = fields.Integer(size=3, string="啟始ROW", default=0)
    end_row = fields.Integer(size=3, string="結止ROW", default=0)



    def match_action_import(self):
        if self.start_row == 1 :
            raise UserError("數值錯誤,ROW啟始數值從 2 開始")
        if self.start_row < 0 or self.end_row < 0:
            raise UserError("數值錯誤,ROW數值不能小於0")
        if self.start_row > self.end_row:
            raise UserError("數值錯誤,啟始ROW數值大於結止ROW")

        if not self.excel_file:
            raise UserError("檔案錯誤,沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodebytes(self.excel_file))
        sheet = xls.sheet_by_index(self.sheet_num)
        if self.start_row > 0 or self.end_row > 0:
            nstartrow = self.start_row
            if self.end_row > sheet.nrows:
               nendrow = sheet.nrows
            else:
               nendrow = self.end_row
        else:
            nstartrow = 2
            nendrow = sheet.nrows

        #self.ensure_one()
        # sys.setdefaultencoding('utf-8')
        match_rec = self.env['cloudrent.contract_match'].search([])
        mysaleid = self.env.context.get('sale_op_id')
        if not self.excel_file:
            raise UserError("沒有上傳正確的Excel File")
        xls = xlrd.open_workbook(file_contents=base64.decodebytes(self.excel_file))
        sheet = xls.sheet_by_index(self.sheet_num)
        # nstartrow = 1
        # nendrow = sheet.nrows

        myamounttot = 0

        for row in range(nstartrow -1, nendrow):
            cell0 = sheet.cell(row,0)    # 包租/代管
            casetype = '2'
            try:
                if cell0.ctype == XL_CELL_EMPTY:
                    casetype = '2'
                else:
                    if '代' in str(cell0.value):
                        casetype = '2'
                    else:
                        casetype = '1'
            except Exception as inst:
                casetype = '2'

            cell1 = sheet.cell(row, 1)   # 續約 lessee_renew1
            lesseerenew1=False
            lesseerenew2=False
            lesseeterminate=False
            try:
                if cell1.ctype == XL_CELL_EMPTY:
                    lesseerenew1=False
                    lesseerenew2=False
                else:
                    if '續１' in str(cell1.value):
                        lesseerenew1=True
                        lesseerenew2=False
                        lesseeterminate=False
                    elif '續２' in str(cell1.value):
                        lesseerenew1=False
                        lesseerenew2=True
                        lesseeterminate = False
                    elif '【解約】' in str(cell1.value):
                        lesseerenew1 = False
                        lesseerenew2 = False
                        lesseeterminate = True

            except Exception as inst:
                lesseerenew1 = False
                lesseerenew2 = False
                lesseeterminate = False

            cell2 = sheet.cell(row,2)   # 順序3 match_seq
            matchseq = ''
            try:
                if cell2.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchseq = int(cell2.value)
                else:
                    matchseq = ''
            except Exception as inst:
                matchseq = ''

            cell3 = sheet.cell(row,3)   # 媒合編號 match_no
            matchno=''
            try:
                if cell3.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchno = ''+str(cell3.value)
                else:
                    matchno = ''
            except Exception as inst:
                matchno = ''

            cell4 = sheet.cell(row, 4)  # 物件編號 object_no
            objectno=''
            try:
                if cell4.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    objectno = ''+str(cell4.value)
                else:
                    objectno = ''
            except Exception as inst:
                objectno = ''


            cell5 = sheet.cell(row, 5)  # 房客編號 lessee_no
            lesseeno=''
            try:
                if cell5.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseeno = ''+str(cell5.value)
                else:
                    lesseeno = ''
            except Exception as inst:
                lesseeno = ''

            cell6 = sheet.cell(row, 6)  # 地區 build_loc
            buildloc=''
            try:
                if cell6.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildloc = ''+str(cell6.value)
                else:
                    buildloc = ''
            except Exception as inst:
                buildloc = ''

            cell7 = sheet.cell(row, 7)  # 社區 build_community
            buildcommunity=''
            try:
                if cell7.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildcommunity = ''+str(cell7.value)
                else:
                    buildcommunity = ''
            except Exception as inst:
                buildcommunity = ''

            cell8 = sheet.cell(row, 8)  # 權狀地址 writ_addr
            writaddr=''
            try:
                if cell8.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    writaddr = ''+str(cell8.value)
                else:
                    writaddr = ''
            except Exception as inst:
                writaddr = ''

            cell9 = sheet.cell(row, 9)  # 所有權人  build_lessor   => cloudrent.escrow_member ecrow_type='1'
            buildlessor=''
            try:
                if cell9.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildlessor = ''+str(cell9.value)
                else:
                    buildlessor = ''
            except Exception as inst:
                buildlessor = ''

            cell10 = sheet.cell(row, 10)  # 所有權人電話 X compute
            lessorcell=''
            try:
                if cell10.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lessorcell = ''+str(cell10.value)
                else:
                    lessorcell = ''
            except Exception as inst:
                lessorcell = ''

            cell11 = sheet.cell(row, 11)  # 承租人 build_lessee => cloudrent.escrow_member ecrow_type='2'
            buildlessee=''
            try:
                if cell11.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildlessee = ''+str(cell11.value)
                else:
                    buildlessee = ''
            except Exception as inst:
                buildlessee = ''

            cell12 = sheet.cell(row, 12)  # 承租人電話 X compute
            lesseecell=''
            try:
                if cell12.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseecell = ''+str(cell12.value)
                else:
                    lesseecell = ''
            except Exception as inst:
                lesseecell = ''

            cell13 = sheet.cell(row, 13)  # 聯絡人 lessee_contact
            lesseecontact=''
            try:
                if cell13.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseecontact = ''+str(cell13.value)
                else:
                    lesseecontact = ''
            except Exception as inst:
                lesseecontact = ''

            cell14 = sheet.cell(row, 14)  # 型態 '1' 公寓  '2'華夏  '3'電梯大樓 build_type
            buildtype=''
            buildtype1=''
            try:
                if cell14.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildtype = ''+str(cell14.value)
                    if buildtype in '公寓':
                        buildtype1='1'
                    elif buildtype in '華廈':
                        buildtype1='2'
                    else:
                        buildtype1='3'
                else:
                    buildtype = ''
            except Exception as inst:
                buildtype = ''

            cell15 = sheet.cell(row, 15)  # 格局 build_pattern1 '1''套房','2''一房','3''二房','4''三房以上'
            buildpattern1=''
            buildpattern=''
            try:
                if cell15.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    buildpattern1 = ''+str(cell15.value)
                    if buildpattern1 in '套房':
                        buildpattern='1'
                    elif buildpattern1[:1] == '1':
                        buildpattern = '2'
                    elif buildpattern1[:1] == '2':
                        buildpattern = '3'
                    elif buildpattern1[:1] == '3':
                        buildpattern = '4'
                else:
                    buildpattern1 = ''
            except Exception as inst:
                buildpattern1 = ''

            cell16 = sheet.cell(row, 16)  # 一般戶租金 lesseetype0_rent
            lesseetype0rent=0
            try:
                if cell16.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseetype0rent = int(cell16.value)
                else:
                    lesseetype0rent = 0
            except Exception as inst:
                lesseetype0rent = 0

            cell17 = sheet.cell(row, 17)  # 一類戶租金 lesseetype1_rent
            lesseetype1rent=0
            try:
                if cell17.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseetype1rent = int(cell17.value)
                else:
                    lesseetype1rent = 0
            except Exception as inst:
                lesseetype1rent = 0

            cell18 = sheet.cell(row, 18)  # 二類戶租金 lesseetype2_rent
            lesseetype2rent=0
            try:
                if cell18.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseetype2rent = int(cell18.value)
                else:
                    lesseetype2rent = 0
            except Exception as inst:
                lesseetype2rent = 0

            cell19 = sheet.cell(row, 19)  # 管理費 management_fee
            managementfee=0
            try:
                if cell19.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    managementfee = int(cell19.value)
                else:
                    managementfee = 0
            except Exception as inst:
                managementfee = 0

            cell20 = sheet.cell(row, 20)  # 車位租金 parking_fee
            parkingfee=0
            try:
                if cell20.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    parkingfee = int(cell20.value)
                else:
                    parkingfee = 0
            except Exception as inst:
                parkingfee = 0

            cell21 = sheet.cell(row, 21)  # 客戶類別  '1''一般戶','2''第一類弱勢戶','3''第二類弱勢戶','4''就學,就業,警消' lessee_type
            lesseetype=''
            lesseetype1=''
            try:
                if cell21.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseetype1 = ''+str(cell21.value)
                    if '一般戶' in lesseetype1 :
                        lesseetype = '1'
                    elif '一類戶' in lesseetype1 :
                        lesseetype = '2'
                    elif '二類戶' in lesseetype1 :
                        lesseetype = '3'
                    elif '舊學' in lesseetype1 :
                        lesseetype = '4'
                    elif '300億' in lesseetype1 :
                        lesseetype = '5'
                    else:
                        lesseetype = '1'
                else:
                    lesseetype = '1'
                    lesseetype1 = ''
            except Exception as inst:
                lesseetype = ''

            cell22 = sheet.cell(row, 22)  # 補助款 lessee_grant
            lesseegrant=0
            try:
                if cell22.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseegrant = int(cell22.value)
                else:
                    lesseegrant = 0
            except Exception as inst:
                lesseegrant = 0

            cell23 = sheet.cell(row, 23)  # 入戶籍 register_household
            registerhousehold=False
            try:
                if cell23.ctype == XL_CELL_EMPTY:
                    registerhousehold=False
                else:
                    registerhousehold=True

            except Exception as inst:
                registerhousehold=False

            cell24 = sheet.cell(row, 24)  # 備註 lessee_memo
            lesseememo=''
            try:
                if cell24.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseememo = ''+str(cell24.value)
                else:
                    lesseememo = ''
            except Exception as inst:
                lesseememo = ''

            cell25 = sheet.cell(row, 25)  # 房客應繳租金 lessee_tot_rent
            lesseetotrent=0
            try:
                if cell25.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseetotrent = int(cell25.value)
                else:
                    lesseetotrent = 0
            except Exception as inst:
                lesseetotrent = 0

            cell26 = sheet.cell(row, 26)  # 起租年 match_start_date
            matchstarty=''
            try:
                if cell26.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchstarty = int(cell26.value)
                else:
                    matchstarty = ''
            except Exception as inst:
                matchstarty = ''

            cell27 = sheet.cell(row, 27)  # 起租月 match_start_date
            matchstartm=''
            try:
                if cell27.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchstartm = int(cell27.value)
                else:
                    matchstartm = ''
            except Exception as inst:
                matchstartm = ''

            cell28 = sheet.cell(row, 28)  # 起租日 match_start_date
            matchstartd=''
            try:
                if cell28.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchstartd = int(cell28.value)
                else:
                    matchstartd = ''
            except Exception as inst:
                matchstartd = ''

            cell29 = sheet.cell(row, 29)  # 到期年 match_end_date
            matchendy=''
            try:
                if cell29.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchendy = int(cell29.value)
                else:
                    matchendy = ''
            except Exception as inst:
                matchendy = ''

            cell30 = sheet.cell(row, 30)  # 到期月 match_end_date
            matchendm=''
            try:
                if cell30.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchendm = int(cell30.value)
                else:
                    matchendm = ''
            except Exception as inst:
                matchendm = ''

            cell31 = sheet.cell(row, 31)  # 到期日 match_end_date
            matchendd=''
            try:
                if cell31.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    matchendd = int(cell31.value)
                else:
                    matchendd = ''
            except Exception as inst:
                matchendd = ''

            cell32 = sheet.cell(row, 32)  # 通知到期月份 renew_ym 年月
            renewm=''
            try:
                if cell32.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renewm = int(cell32.value)
                else:
                    renewm = ''
            except Exception as inst:
                renewm = ''

            cell33 = sheet.cell(row, 33)  # 續約1客戶類別 renew1_lessee_type
            renew1lesseetype = ''
            renew1lesseetype1 = ''
            try:
                if cell33.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1lesseetype1 = '' + str(cell33.value)
                    if '一般戶' in renew1lesseetype1:
                        renew1lesseetype = '1'
                    elif '一類戶' in renew1lesseetype1:
                        renew1lesseetype = '2'
                    elif '二類戶' in renew1lesseetype1:
                        renew1lesseetype = '3'
                    elif '就學' in renew1lesseetype1:
                        renew1lesseetype = '4'
                    elif '300億' in renew1lesseetype1:
                        renew1lesseetype = '5'
                    else:
                        renew1lesseetype = '1'
                else:
                    renew1lesseetype = '1'
                    renew1lesseetype1 = ''
            except Exception as inst:
                renew1lesseetype1 = ''

            cell34 = sheet.cell(row, 34)  # 續1開始年 renew1starty
            renew1starty = ''
            try:
                if cell34.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1starty = int(cell34.value)
                else:
                    renew1starty = ''
            except Exception as inst:
                renew1starty = ''

            cell35 = sheet.cell(row, 35)  # 續1開始月 renew1startm
            renew1startm = ''
            try:
                if cell35.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1startm = int(cell35.value)
                else:
                    renew1startm = ''
            except Exception as inst:
                renew1startm = ''

            cell36 = sheet.cell(row, 36)  # 續1開始日 renew1startd
            renew1startd = ''
            try:
                if cell36.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1startd = int(cell36.value)
                else:
                    renew1startd = ''
            except Exception as inst:
                renew1startd = ''

            cell37 = sheet.cell(row, 37)  # 續1到期年 renew1endy
            renew1endy = ''
            try:
                if cell37.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1endy = int(cell37.value)
                else:
                    renew1endy = ''
            except Exception as inst:
                renew1endy = ''

            cell38 = sheet.cell(row, 38)  # 續1到期月 renew1endm
            renew1endm = ''
            try:
                if cell38.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1endm = int(cell38.value)
                else:
                    renew1endm = ''
            except Exception as inst:
                renew1endm = ''

            cell39 = sheet.cell(row, 39)  # 續1到期日 renew1endd
            renew1endd = ''
            try:
                if cell39.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew1endd = int(cell39.value)
                else:
                    renew1endd = ''
            except Exception as inst:
                renew1endd = ''

            cell40 = sheet.cell(row, 40)  # 續約2客戶類別 renew2_lessee_type
            renew2lesseetype = ''
            renew2lesseetype1 = ''
            try:
                if cell40.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2lesseetype1 = '' + str(cell40.value)
                    if '一般戶' in renew2lesseetype1:
                        renew2lesseetype = '1'
                    elif '一類戶' in renew2lesseetype1:
                        renew2lesseetype = '2'
                    elif '二類戶' in renew2lesseetype1:
                        renew2lesseetype = '3'
                    elif '就學' in renew2lesseetype1:
                        renew2lesseetype = '4'
                    elif '300億' in renew2lesseetype1:
                        renew2lesseetype = '5'
                    else:
                        renew2lesseetype = '1'
                else:
                    renew2lesseetype = '1'
                    renew2lesseetype1 = ''
            except Exception as inst:
                renew2lesseetype1 = ''

            cell41 = sheet.cell(row, 41)  # 續2開始年 renew2starty
            renew2starty = ''
            try:
                if cell41.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2starty = int(cell41.value)
                else:
                    renew2starty = ''
            except Exception as inst:
                renew2starty = ''

            cell42 = sheet.cell(row, 42)  # 續2開始月 renew2startm
            renew2startm = ''
            try:
                if cell42.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2startm = int(cell42.value)
                else:
                    renew2startm = ''
            except Exception as inst:
                renew2startm = ''

            cell43 = sheet.cell(row, 43)  # 續2開始日 renew2startd
            renew2startd = ''
            try:
                if cell43.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2startd = int(cell43.value)
                else:
                    renew2startd = ''
            except Exception as inst:
                renew2startd = ''

            cell44 = sheet.cell(row, 44)  # 續2到期年 renew2endy
            renew2endy = ''
            try:
                if cell44.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2endy = int(cell44.value)
                else:
                    renew2endy = ''
            except Exception as inst:
                renew2endy = ''

            cell45 = sheet.cell(row, 45)  # 續2到期月 renew2endm
            renew2endm = ''
            try:
                if cell45.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2endm = int(cell45.value)
                else:
                    renew2endm = ''
            except Exception as inst:
                renew2endm = ''

            cell46 = sheet.cell(row, 46)  # 續2到期日 renew2endd
            renew2endd = ''
            try:
                if cell46.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    renew2endd = int(cell46.value)
                else:
                    renew2endd = ''
            except Exception as inst:
                renew2endd = ''


            cell47 = sheet.cell(row, 47)  # 屋主業務 lessor_sale
            lessorsale=''
            try:
                if cell47.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lessorsale ='' + str(cell47.value)
                else:
                    lessorsale =''
            except Exception as inst:
                lessorsale = ''

            cell48 = sheet.cell(row, 48)  # 房客業務 lessee_sale
            lesseesale=''
            try:
                if cell48.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseesale ='' + str(cell48.value)
                else:
                    lesseesale =''
            except Exception as inst:
                lesseesale = ''

            cell49 = sheet.cell(row, 49)  # 備註 lessor_memo
            lessormemo = ''
            try:
                if cell49.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lessormemo = '' + str(cell49.value)
                else:
                    lessormemo = ''
            except Exception as inst:
                lessormemo = ''

            cell50 = sheet.cell(row, 50)  # 出租人身份證 lessor_pid
            lessorpid = ''
            try:
                if cell50.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lessorpid = '' + str(cell50.value)
                else:
                    lessorpid  = ''
            except Exception as inst:
                lessorpid  = ''

            cell51 = sheet.cell(row, 51)  # 承租人身份證 lessee_pid
            lesseepid = ''
            try:
                if cell51.ctype in (XL_CELL_TEXT, XL_CELL_NUMBER):
                    lesseepid = '' + str(cell51.value)
                else:
                    lesseepid = ''
            except Exception as inst:
                lesseepid = ''



            matchstartdate=''
            if matchstarty != '' and matchstartm != '' and matchstartd !='':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (matchstarty,matchstartm,matchstartd))
                matchstartdate = self.env.cr.fetchone()[0]
            matchenddate=''
            if matchendy != '' and matchstartm != '' and matchstartd != '':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (matchendy, matchendm, matchendd))
                matchenddate = self.env.cr.fetchone()[0]
            renew1startdate=False
            if renew1starty != '' and renew1startm !='' and renew1startd != '':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (renew1starty, renew1startm, renew1startd))
                renew1startdate = self.env.cr.fetchone()[0]
            renew1enddate=False
            if renew1endy != '' and renew1endm != '' and renew1endd != '':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (renew1endy, renew1endm, renew1endd))
                renew1enddate = self.env.cr.fetchone()[0]
            renew2startdate = False
            if renew2starty != '' and renew2startm !='' and renew2startd != '':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (renew2starty, renew2startm, renew2startd))
                renew2startdate = self.env.cr.fetchone()[0]
            renew2enddate=False
            if renew2endy != '' and renew2endm != '' and renew2endd != '':
                self.env.cr.execute("""select get_cymddate('%s','%s','%s')""" % (renew2endy, renew2endm, renew2endd))
                renew2enddate = self.env.cr.fetchone()[0]

            self.env.cr.execute("""select import_lessor(%d,'%s','%s','%s','%s')""" % (self.escrow_agent.id,buildlessor,lessorcell,writaddr,lessorpid))
            lessorid = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select import_lessee(%d,'%s','%s','%s','%s','%s')""" % (self.escrow_agent.id,buildlessee,lesseecell,lesseeno,buildloc,lesseepid))
            lesseeid = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select import_sale(%d,'%s')""" % (self.escrow_agent.id,lessorsale))
            lessorsaleid = self.env.cr.fetchone()[0]
            self.env.cr.execute("""select import_sale(%d,'%s')""" % (self.escrow_agent.id,lesseesale))
            lesseesaleid = self.env.cr.fetchone()[0]
            try:
                self.env.cr.execute("""select import_build(%d,'%s','%s','%s','%s','%s','%s','%s',%d)""" % (self.escrow_agent.id,objectno,writaddr,buildloc,matchstartdate,matchenddate,buildpattern,buildcommunity,lessorid))
                objectno1 = self.env.cr.fetchone()[0]
            except:
                A=1

            if lesseegrant == 0:
                if lesseetype=='1':
                    lesseegrant = 0
                elif lesseetype=='2':
                    lesseegrant = lesseetype0rent - lesseetype1rent
                elif lesseetype=='3':
                    lesseegrant = lesseetype0rent - lesseetype2rent
            if lesseerenew1==True and lesseerenew2==False:
                renewstartdate = renew1startdate
                renewenddate = renew1enddate
                olesseetype = lesseetype
                nlesseetype = renew1lesseetype
            elif lesseerenew1==False and lesseerenew2==True:
                renewstartdate = renew2startdate
                renewenddate = renew2enddate
                olesseetype = lesseetype
                nlesseetype = renew2lesseetype
            mycount = self.env['cloudrent.contract_match'].search_count([('match_no','=',matchno)])
            if mycount > 0 :
                match_rec1 = self.env['cloudrent.contract_match'].search([('match_no','=',matchno)])
                try:

                    match_rec1.write({'escrow_no':self.escrow_agent.id,'lessee_renew1':lesseerenew1,'lessee_renew2':lesseerenew2,'lessee_terminate':lesseeterminate,'match_seq':matchseq,'match_no':matchno,'object_no':objectno,'object_no1':objectno1,'lessee_no':lesseeno,
                                      'build_loc':buildloc,'build_community':buildcommunity,'writ_addr':writaddr,'build_lessor':lessorid,'build_lessee':lesseeid,'lessee_contact':lesseecontact,'build_type':buildtype1,'build_pattern1':buildpattern1,
                                      'build_pattern':buildpattern,'lesseetype0_rent':lesseetype0rent,'lesseetype1_rent':lesseetype1rent,'lesseetype2_rent':lesseetype2rent,'management_fee':managementfee,'parking_fee':parkingfee,'lessee_type':lesseetype,
                                      'lessee_grant':lesseegrant,'register_household':registerhousehold,'lessee_memo':lesseememo,'lessee_tot_rent':lesseetotrent,'match_start_date':matchstartdate,'match_end_date':matchenddate,
                                      'renew_start_date':renewstartdate,'renew_end_date':renewenddate,'origin_lessee_type':olesseetype,'new_lessee_type':nlesseetype,'lessor_sale':lessorsaleid,'lessee_sale':lesseesaleid,'admin_area': self.admin_area,
                                      'case_type':casetype,'build_for_rent':lesseetype0rent,'build_contract_rent':lesseetype0rent,'lessor_pid':lessorpid,'lessee_pid':lesseepid})
                except:
                    A=1
            else:
                try:
                    res = match_rec.create({'escrow_no':self.escrow_agent.id,'lessee_renew1':lesseerenew1,'lessee_renew2':lesseerenew2,'lessee_terminate':lesseeterminate,'match_seq':matchseq,'match_no':matchno,'object_no':objectno,'object_no1':objectno1,'lessee_no':lesseeno,
                                      'build_loc':buildloc,'build_community':buildcommunity,'writ_addr':writaddr,'build_lessor':lessorid,'build_lessee':lesseeid,'lessee_contact':lesseecontact,'build_type':buildtype1,'build_pattern1':buildpattern1,
                                      'build_pattern':buildpattern,'lesseetype0_rent':lesseetype0rent,'lesseetype1_rent':lesseetype1rent,'lesseetype2_rent':lesseetype2rent,'management_fee':managementfee,'parking_fee':parkingfee,'lessee_type':lesseetype,
                                      'lessee_grant':lesseegrant,'register_household':registerhousehold,'lessee_memo':lesseememo,'lessee_tot_rent':lesseetotrent,'match_start_date':matchstartdate,'match_end_date':matchenddate,
                                      'renew_start_date':renewstartdate,'renew_end_date':renewenddate,'origin_lessee_type':olesseetype,'new_lessee_type':nlesseetype,'lessor_sale':lessorsaleid,'lessee_sale':lesseesaleid,
                                      'admin_area':self.admin_area,'case_type':casetype,'build_for_rent':lesseetype0rent,'build_contract_rent':lesseetype0rent,'lessor_pid':lessorpid,'lessee_pid':lesseepid})
                except:
                    A=1
            # self.env.cr.execute("""select gen_lessee_grant(%d)""" % res.id)
            # self.env.cr.execute("""commit""")



        view = self.env.ref('sh_message.sh_message_wizard')
        #view_id = view and view.id of False
        context = dict(self._context or {})
        context['message']='租房代管媒合資料匯入完成'
        return {
            'name':'Success',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }
