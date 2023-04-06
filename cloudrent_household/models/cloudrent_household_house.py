# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
import pickle,os


class CloudRentHouseholdhouse(models.Model):
    _name = "cloudrent.household_house"
    _description = "cloudrent租屋基本資料"
    _order = "project_no"

    @api.depends('project_line')
    def _get_houseamount(self):
        for rec in self:
            ncount = 0
            for rec1 in rec.project_line:
                ncount = ncount + 1
            rec.project_amount = ncount

    project_no = fields.Char(string='租案案名',required=True)
    project_desc = fields.Char(string="租案說明")
    project_address = fields.Char(string="租案地址")
    manager_man = fields.Char(string="管理員")
    manager_address = fields.Char(string="管理員地址")
    manager_phone = fields.Char(string="管理員電話")
    project_amount = fields.Integer(string="租案戶數",default=_get_houseamount)
    project_line = fields.One2many('cloudrent.household_house_line','house_id',string="租屋房間明細",copy=False)
    project_prefixcode = fields.Char(string="案場前綴碼")
    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")
    case_code = fields.Char(string="案場代號",required=True)
    rent_convention = fields.Binary(string="住戶公約")

    def name_get(self):
        result = []
        for myrec in self:
            if myrec.project_desc:
                myprojdesc= myrec.project_desc
            else:
                myprojdesc = ' '
            myname = "[%s]%s" % (myrec.project_no, myprojdesc)
            result.append((myrec.id, myname))
        return result




class CloudRentHouseholdElectricMeter(models.Model):
    _name = "cloudrent.household_electric_meter"
    _description = "cloudrent MODBUS電錶"
    _order = "emeter_name"
    _rec_name = "emeter_name"

    @api.depends()
    def _get_emeter_status(self):
        for rec in self:
            try:
                self.env.cr.execute("""select get_emeter_status(%d)""" % rec.id)
                mystatus = self.env.cr.fetchone()[0]
                rec.emeter_status = mystatus
            except:
                mystatus='NG'
            return mystatus


    emeter_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    emeter_name = fields.Char(string="電錶說明")
    ig8000_id = fields.Char(string="IG8000 ID")
    pi_id = fields.Char(string="裝置ID")
    modbus_id = fields.Char(string="MODBUS16 ID")
    modbus10_id = fields.Char(string="MODBUS10 ID")
    emeter_line = fields.One2many('cloudrent.household_emeter_line','emeter_id',copy=False)
    emeter_status = fields.Selection([('OK','正常'),('NG','異常')],string="電錶狀態",compute=_get_emeter_status)



    @api.model
    def create(self, vals):
        myig8000 = vals['ig8000_id']
        mymodbus = vals['modbus_id']
        mycount = self.env['cloudrent.household_electric_meter'].search_count([('ig8000_id','=',myig8000),('modbus_id','=',mymodbus)])
        if mycount > 1:
            raise UserError('不可在同一IG8000上有相同的 MODBUS ID')
        res = super(CloudRentHouseholdElectricMeter, self).create(vals)

        return res

    def mes_push_file(self, node_ip, localpath, remotepath):  ## 傳檔到終端點
        import paramiko
        t = paramiko.Transport((node_ip, 22))
        t.connect(username='pi', password='pi')
        sftp = paramiko.SFTPClient.from_transport(t)
        if os.path.exists(localpath):
            try:
                sftp.put(localpath, remotepath)
            except Exception as inst:
                print('Push NO OK')
        else:
            print('Local No such File')
        t.close()

    def run_push_scale(self):
        emeterid = '33'
        with open('/opt/odoo/modbus.pickle', 'wb') as files:
            pickle.dump(emeterid, files, protocol=pickle.HIGHEST_PROTOCOL)
        localfile = '/opt/odoo/modbus.pickle'
        remotefile = '/home/pi/modbus.pickle'
        myip = '192.168.100.52'
        self.mes_push_file(myip,localfile,remotefile)


class cloudrentHouseholdEmeterLine(models.Model):
    _name = "cloudrent.household_emeter_line"

    emeter_id = fields.Many2one('cloudrent.household_electric_meter',ondelete='cascade')
    emeter_dt = fields.Datetime(string="電錶時間")
    emeter_status = fields.Selection([('OK','正常'),('NG','異常')],string="電錶狀態",default='OK')


class cloudrenthouseholdhouseline(models.Model):
    _name = "cloudrent.household_house_line"
    _description = "cloudrent租屋房間明細"
    _order = "house_no"

    @api.depends('bill_line')
    def _get_currentemeter(self):
        for line in self:
            myfee = 0
            for rec in line.bill_line:
                myfee = myfee + rec.emeter_amount
            line.current_emeter_fee=myfee

    @api.depends('member_id','current_emeter_fee','uncomplete_fee','water_fee')
    def _get_currenttot(self):
        mytot = 0
        for line in self:
            if not line.member_id.water_fee:
                mywaterfee = 0
            else:
                mywaterfee = line.member_id.water_fee
            mytot = mytot + (line.current_emeter_fee + line.member_id.house_rental_fee + line.member_id.house_management_fee + line.member_id.parking_space_rent + line.member_id.parking_management + line.member_id.lo_parking_management + line.uncomplete_fee + mywaterfee)
        self.current_total_fee = mytot

    @api.depends()
    def _get_paymentbank(self):
        myrec = self.env['cloudrent.household_config'].search([])
        for line in self:
            line.payment_bank = myrec.payment_bank

    @api.depends()
    def _get_paymentaccount(self):
        myrec = self.env['cloudrent.household_config'].search([])
        for line in self:
            line.payment_account = myrec.payment_account

    @api.depends('house_no','bill_ym')
    def _get_uncompletefee(self):
        for rec in self:
            if not rec.bill_ym:
                myres = 0
            else:
                myy = rec.bill_ym[0:4]
                mym = rec.bill_ym[5:7]
                mynm = int(mym) - 1
                if mynm < 0 :
                    mym = '12'
                    myny = int(myy) - 1
                    myy = str(myny)
                else:
                    mym = str(mynm).zfill(2)
                myym = myy + mym
                myrec = self.env['cloudrent.household_payment_line'].search([('house_no','=',rec.house_no),('payment_ym','=',myym)])
                if myrec:
                    myres = myrec.uncomplete_fee
                else:
                    myres = 0
            rec.uncomplete_fee = myres
            return myres

    @api.depends()
    def _get_priceunit(self):
        myrec = self.env['cloudrent.household_config'].search([])
        if myrec:
            self.price_unit = myrec.price_unit
            return myrec.price_unit

    @api.depends('repair_grant_line','repair_fee_payment_line')
    def _get_repair_grant_amount(self):
        for rec in self:
            mypayment = 0
            for rec1 in rec.repair_fee_payment_line:
                mypayment = mypayment + rec1.payment_amount
            mygrant = 0
            for rec2 in rec.repair_grant_line:
                if rec2.grant_active:
                    mygrant = mygrant + rec2.grant_amount
            rec.repair_grant_amount = mygrant - mypayment

    @api.depends('repair_fee_payment_line')
    def _get_repair_payment_amount(self):
        for rec in self:
            mypayment = 0
            for rec1 in rec.repair_fee_payment_line:
                # if rec1.payment_active:
                mypayment = mypayment + rec1.payment_amount
            rec.repair_payment_amount = mypayment


    house_id = fields.Many2one('cloudrent.household_house',ondelete='cascade')
    house_no = fields.Char(string="房號",required=True)
    house_level = fields.Integer(string="樓層")
    member_id = fields.Many2one('cloudrent.household_member',string="住戶")
    emeter_line = fields.One2many('cloudrent.household_electric_meter','emeter_id',string="電錶配置",copy=False)
    in_used = fields.Boolean(string="入住否？",default=False)
    store_amount = fields.Float(digits=(10,0),string="儲值度數餘額")
    start_scale = fields.Float(digits=(10,1),string="期初累計度數")
    start110_scale = fields.Float(digits=(10,1),string="(110V)合約期初度數")
    start220_scale = fields.Float(digits=(10,1),string="(220V)合約期初度數")
    current110_scale = fields.Float(digits=(10,1),string="(110V)目前累計度數")
    current220_scale = fields.Float(digits=(10, 1), string="(220V)目前累計度數")
    start_date = fields.Date(string="期初日期")
    prepaid_line = fields.One2many('cloudrent.household_prepaid_line','prepaid_id',string="儲值明細",copy=False)
    used_line = fields.One2many('cloudrent.household_used_line','used_id',string="用電明細",copy=False)
    bill_line = fields.One2many('cloudrent.household_bill_line','bill_id',string="當期月帳單明細",copy=False)
    bill_line_his = fields.One2many('cloudrent.household_bill_line_his', 'bill_id', string="歷史月帳單明細", copy=False)
    invoice_line = fields.One2many('cloudrent.household_invoice_line','invoice_id',string="對帳明細記錄",copy=False)
    payment_line = fields.One2many('cloudrent.household_payment_line','payment_id',string="付款核銷記錄",copy=False)
    repair_grant_line = fields.One2many('cloudrent.repair_grant_line','grant_id',string="修繕補助明細",copy=False)
    repair_fee_payment_line = fields.One2many('cloudrent.repair_fee_payment_line','payment_id',string="修繕核銷記錄",copy=False)
    user_id = fields.Many2one('res.users', string="使用者")
    current_emeter_fee = fields.Float(digits=(10,0),string="本期電費",compute=_get_currentemeter)
    current_total_fee = fields.Float(digits=(10,0),string="本期應付總金額",compute=_get_currenttot)
    payment_bank = fields.Char(string="電匯銀行",compute=_get_paymentbank)
    payment_account = fields.Char(string="電匯帳戶",compute=_get_paymentaccount)
    house_rental_fee = fields.Float(related='member_id.house_rental_fee',string="房屋租金")
    house_management_fee = fields.Float(related='member_id.house_management_fee',string="房屋管理費")
    parking_space_rent = fields.Float(related='member_id.parking_space_rent',string="車位租金")
    parking_management = fields.Float(related='member_id.parking_management',string="車位管理費")
    lo_parking_management = fields.Float(related='member_id.lo_parking_management',string="機車位管理費")
    is_payment = fields.Boolean(related='bill_line.is_payment',string="本期已繳費")
    bill_ym = fields.Char(related='bill_line.bill_ym',string="帳單年月")
    start_rental = fields.Date(related='member_id.start_rental',string="起租日期")
    uncomplete_fee = fields.Float(digits=(10,0),string="前期未繳餘額",compute=_get_uncompletefee)
    price_unit = fields.Float(digits=(5, 1), string="一度電單價", required=True,store=True,default=_get_priceunit)
    water_fee = fields.Float(related='member_id.water_fee',string="水費")

    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")


    equip_line = fields.One2many('cloudrent.equip_list','equip_id',copy=False)

    repair_grant_amount = fields.Float(digits=(10,0),compute=_get_repair_grant_amount,string="補助修繕餘額")
    repair_payment_amount = fields.Float(digits=(10,0),compute=_get_repair_payment_amount,string="已核銷修繕費用")
    landlord_owner = fields.Many2one('cloudrent.household_member',string="所屬房東")
    agent_owner = fields.Many2one('cloudrent.household_member',string="指派管理師")

    def run_daily_amount(self):
        self.env.cr.execute("""select rundailyamount();""")
        self.env.cr.execute("""commit""")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.house_id.project_no, myrec.house_no)
            result.append((myrec.id, myname))
        return result

class cloudrenthouseholdinvoiceline(models.Model):
    _name = "cloudrent.household_invoice_line"
    _description = "對帳明細記錄"

    invoice_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    house_no = fields.Char(string="房號")
    member_id = fields.Many2one('cloudrent.household_member', string="住戶")
    emeter_line = fields.Many2one('cloudrent.household_electric_meter', string="電錶")
    invoice_start_date = fields.Date(string="對帳啟始日期")
    invoice_end_date = fields.Date(string="對帳截止日期")
    invoice_start_scale = fields.Float(digits=(10,1),string="對帳啟始累計度數")
    invoice_end_scale = fields.Float(digits=(10,1),string="對帳截止累計度數" )
    invoice_price_unit = fields.Float(digits=(5,1),string="一度電單價")
    invoice_amount = fields.Float(digits=(10,0),string="本期電費金額")
    invoice_state = fields.Selection([('draft','草稿'),('send','寄送通知'),('payment','電費已付')],string="對帳狀態",default='1')
    payment_date = fields.Date(string="支付日期")

class cloudrenthouseholdprepaidline(models.Model):
    _name = "cloudrent.household_prepaid_line"
    _description = "預付儲值電力度數明細"
    _order = "prepaid_date desc"

    prepaid_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    prepaid_date = fields.Date(string="儲值日期")
    prepaid_code = fields.Char(string="匯款帳號後5碼")
    prepaid_money = fields.Float(digits=(10,0),string="儲值金額",required=True)
    start_value = fields.Float(string="期初電錶度數")
    prepaid_power_store = fields.Float(digits=(5,0),string="儲值電力度數",required=True)
    end_value = fields.Float(string="到期電錶度數")




class cloudrenthouseholdusedline(models.Model):
    _name = "cloudrent.household_used_line"
    _description = "住戶電力日常使用記錄"
    _order = "used_datetime desc"

    used_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    used_emeter_id = fields.Many2one('cloudrent.household_electric_meter',string="電錶")
    used_datetime = fields.Datetime(string="日期")
    used_scale = fields.Float(digits=(10,1),string="電錶累計度數")

class cloudrenthousebillline(models.Model):
    _name = "cloudrent.household_bill_line"
    _description = "當期區間帳單明細"
    _order = "bill_ym desc"



    bill_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    house_no = fields.Char(string="房號")
    bill_ym = fields.Char(string="年-月",size=7)
    bill_start_date = fields.Date(string="對帳期初日期")
    bill_end_date = fields.Date(string="對帳截止日期")
    emeter_id = fields.Many2one('cloudrent.household_electric_meter', string="電錶")
    emeter_start_scale = fields.Float(digits=(13,2),string="期初累計度數")
    emeter_end_scale = fields.Float(digits=(13,2),string="期末累計度數")
    emeter_used_scale = fields.Float(digits=(10,1),string="使用度數")
    emeter_current_scale = fields.Float(digits=(10,1),string="累計度數")
    emeter_price_unit = fields.Float(digits=(6,2),string="單價(度)")
    emeter_amount = fields.Float(digits=(8,0),string="電費小計")
    is_payment = fields.Boolean(string="是否已核銷",default=False)


class cloudrenthousebilllinehis(models.Model):
    _name = "cloudrent.household_bill_line_his"
    _description = "歷史月帳單明細"
    _order = "bill_ym desc"

    bill_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    house_no = fields.Char(string="房號")
    bill_ym = fields.Char(string="年-月",size=7)
    bill_start_date = fields.Date(string="對帳期初日期")
    bill_end_date = fields.Date(string="對帳截止日期")
    emeter_id = fields.Many2one('cloudrent.household_electric_meter', string="電錶")
    emeter_start_scale = fields.Float(digits=(13, 2), string="期初累計度數")
    emeter_end_scale = fields.Float(digits=(13, 2), string="截止累計度數")
    emeter_used_scale = fields.Float(digits=(10, 1), string="使用度數")
    emeter_current_scale = fields.Float(digits=(10, 1), string="累計度數")
    emeter_price_unit = fields.Float(digits=(6, 2), string="單價(度)")
    emeter_amount = fields.Float(digits=(8, 1), string="電費小計")

class cloudrenthouseholdpaymentline(models.Model):
    _name = "cloudrent.household_payment_line"
    _description = "租戶費用核銷明細"
    _order = "payment_ym desc,id desc"

    payment_id = fields.Many2one('cloudrent.household_house_line', ondelete='cascade')
    house_no = fields.Char(string="房號")
    payment_ym = fields.Char(string="年-月", size=7)
    payment_start_date = fields.Date(string="對帳期初日期")
    payment_end_date = fields.Date(string="對帳截止日期")
    payment_amount = fields.Float(digits=(10,0),string="收款入帳金額",default=0)
    emeter_scale = fields.Boolean(string="電費核銷",default=False)
    house_rental = fields.Boolean(string="房屋租金核銷",default=False)
    house_management = fields.Boolean( string="房屋管理費核銷",default=False)
    parking_space_rent = fields.Boolean(string="車位租金核銷",default=False)
    parking_management = fields.Boolean(string="車位管理費核銷",default=False)
    lo_parking_management = fields.Boolean(string="機車位管理費核銷",default=False)
    payment_date = fields.Date(string="電匯日期")
    payment_desc = fields.Char(string="電匯說明")
    uncomplete_fee = fields.Float(digits=(10,0),string="未結餘額")

class CloudRentEquipList(models.Model):
    _name = "cloudrent.equip_list"
    _description = "住屋設備清單"

    equip_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    equip_categ = fields.Selection([('1','家電類'),('2','家具類'),('3','鑰匙類'),('4','其他')],string="設備分類",required=True)
    equip_no = fields.Many2one('cloudrent.equip_part',string="設備名稱",required=True)
    equip_qty = fields.Integer(string="數量")
    equip_status = fields.Char(string="設備狀態描述")
    equip_image = fields.Binary(string='照片')

    @api.onchange('equip_categ')
    def onchangecusname(self):
        myids = []
        mycateg = self.equip_categ
        myrec = self.env['cloudrent.equip_part'].search([('equip_categ','=',self.equip_categ)])
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'equip_no': [('id', 'in', myids)]}}

    def name_get(self):
        result = []
        mycateg = ''
        for myrec in self:
            if myrec.equip_categ == '1':
                mycateg = '家電類'
            elif myrec.equip_categ == '2':
                mycateg = '家具類'
            elif myrec.equip_categ == '3':
                mycateg = '鑰匙類'
            else:
                mycateg = '其他'
            myname = "[%s]%s" % (mycateg, myrec.equip_no.name)
            result.append((myrec.id, myname))
        return result

class CloudRentEquipPart(models.Model):
    _name = "cloudrent.equip_part"
    _description = "租房設備說明主檔"

    equip_categ = fields.Selection([('1','家電類'),('2','家具類'),('3','鑰匙類'),('4','其他')],string="設備分類",required=True)
    name = fields.Char(string="設備名稱")


class CloudRentRepairGrantLine(models.Model):
    _name = "cloudrent.repair_grant_line"
    _description = "雲房修繕補助明細記錄"
    _order = "grant_start"

    grant_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    grant_no = fields.Char(string="單號",default='New',copy=False)
    grant_start = fields.Date(string="補助起始日",required=True)
    grant_end = fields.Date(string="補助截止日",required=True)
    grant_alert = fields.Date(string="到期前警示日",required=True)
    grant_amount = fields.Float(digits=(10,0),string="補助金額",required=True)
    grant_active = fields.Boolean(string="有效",default=True)
    setup_man = fields.Many2one('res.users',string="建檔人")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s-%s/%s" % (myrec.grant_no, myrec.grant_start,myrec.grant_end,myrec.grant_amount)
            result.append((myrec.id, myname))
        return result

    @api.model
    def create(self, vals):
        if vals.get('grant_no', _('New')) == _('New'):
            vals['grant_no'] = self.env['ir.sequence'].next_by_code('cloudrent.grant_line') or _('New')
        res = super(CloudRentRepairGrantLine, self).create(vals)
        return res


class CloudRentRepairFeePaymentLine(models.Model):
    _name = "cloudrent.repair_fee_payment_line"
    _description = "雲房修繕核銷記錄"
    _order = "payment_date"

    payment_id = fields.Many2one('cloudrent.household_house_line',ondelete='cascade')
    repair_no = fields.Many2one('cloudrent.household_maintenance',string="報修單號")
    grant_no = fields.Many2one('cloudrent.repair_grant_line',string="補助單號",required=True)
    payment_date = fields.Date(string="修繕費核銷日期",required=True)
    supplier = fields.Many2one('cloudrent.household_member',string="廠商",required=True)
    maintenance_id = fields.Many2one('cloudrent.equip_list',string="報修設備")
    maintenance_memo = fields.Text(string="修繕說明")
    payment_amount = fields.Float(digits=(10,0),string="修繕費用")
    invoice_no = fields.Char(string="發票號碼",required=True)
    before_repair_img = fields.Binary(string="修繕前照片")
    process_repair_img = fields.Binary(string="修繕處理中照片")
    compltete_repair_img = fields.Binary(string="修繕完成照片")

    @api.onchange('payment_id')
    def onchangemainid(self):
        myids = []
        myids1 = []
        mypaymentid = self.payment_id.id
        myrec = self.env['cloudrent.equip_list'].search([('equip_id', '=', mypaymentid)])
        for rec in myrec:
            myids.append(rec.id)
        myrec1 = self.env['cloudrent.repair_grant_line'].search([('grant_id','=',mypaymentid),('grant_active','=',True)])
        for rec1 in myrec1:
            myids1.append(rec1.id)
        return {'domain': {'maintenance_id': [('id', 'in', myids)],'grant_no': [('id', 'in', myids1)]}}










