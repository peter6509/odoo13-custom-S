# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from passlib.context import CryptContext
ESCROWTYPE = [('1','出租人/房東'),
              ('2','承租人/房客'),
              ('3','管理師'),
              ('4','不動產經紀人'),
              ('5','業務'),
              ('6','修繕廠商'),
              ('7','秘書')]
LESSEETYPE = [
    ('1','一般戶'),
    ('2','第一類弱勢戶'),
    ('3','第二類弱勢戶'),
    ('4','就學,就業,警消'),
    ('5','300億方案')]
BUILDTYPE=[('1','公寓'),
           ('2','華廈'),
           ('3','電梯大樓')]
BUILDPATTERN=[('1','套房'),
              ('2','一房'),
              ('3','二房'),
              ('4','三房以上')]
EQUIPCATEG=[('1','家電類'),
            ('2','家具類'),
            ('3','鑰匙類'),
            ('4','其他')]

class CloudRentSequenceNo(models.Model):
    _name = "cloudrent.sequence_no"
    _description = "單號序號主檔"

    escrow_no = fields.Many2one('cloudrent.escrow',string="代管業者")
    seq_type = fields.Char(string="單號前綴")
    seq_year = fields.Integer(string="年")
    seq_month = fields.Integer(string='月')
    seq_num = fields.Integer(string="序號")

class CloudRentEscrow(models.Model):
    _name = "cloudrent.escrow"
    _description = "雲房包租代管業者主檔"
    _order = "guild_no,bus_no"

    guild_no = fields.Char(string="公會編號")
    bus_no = fields.Char(string="業者編號")
    bus_name = fields.Char(string="公司名稱")
    bus_boss = fields.Char(string="負責人")
    bus_management = fields.Many2one('cloudrent.escrow_member',string="管理師")
    real_estat_agent = fields.Many2one('cloudrent.escrow_member',string="不動產經紀人")
    bus_address = fields.Char(string="公司地址")
    bus_phone = fields.Char(string="公司電話")
    bus_vat = fields.Char(string="公司統編")
    bus_memo = fields.Text(string="備註")
    license_no = fields.Char(string="許可字號")
    register_no = fields.Char(string="登記證字號")


    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.bus_no, myrec.bus_name)
            result.append((myrec.id, myname))
        return result


class CloudRentEscrowMember(models.Model):
    _name = "cloudrent.escrow_member"
    _description = "雲房包租代管人員主檔"
    _order = "escrow_agent"

    escrow_man = fields.Char(string="人員姓名",required=True)
    escrow_pid = fields.Char(string="身份證號",required=True)
    escrow_agent = fields.Many2one('cloudrent.escrow',string="所屬代管業",required=True,default=lambda self:self.env.user.escrow_no.id)
    escrow_type = fields.Selection(ESCROWTYPE,select=True,string="人員類別",required=True)
    line_user_id = fields.Char(string="LINE ID")
    fin_instno = fields.Char(string="金融機構代碼")
    fin_branch = fields.Char(string="分行代碼")
    fin_name = fields.Char(string="帳戶戶名")
    fin_account = fields.Char(string="帳戶號碼")
    member_sex = fields.Selection([('1','男'),('2','女')],string="性別")
    member_phone1 = fields.Char(string="連絡電話(日)")
    member_phone2 = fields.Char(string="連絡電話(夜)")
    member_cell = fields.Char(string="行動電話")
    member_addr1 = fields.Char(string="通訊地址")
    member_addr = fields.Char(string="戶籍地址")
    member_email = fields.Char(string="EMail")
    member_memo = fields.Text(string="備註")
    member_birthday = fields.Date(string="出生日")
    cloudrent_account = fields.Char(string="雲房登入帳號")
    cloudrent_passwd = fields.Char(string="雲房初始密碼")
    users_id = fields.Many2one('res.users',string="使用者")

    # 房客數據
    lessee_no = fields.Char(string="房客編號")
    lessee_age = fields.Integer(string="年齡")
    build_pattern = fields.Selection(BUILDPATTERN,select=True, string="房型")
    lessee_type = fields.Selection(LESSEETYPE,select=True,string="承租人身份類別")
    elevator = fields.Boolean(string="需有電梯?", default=False)
    lessee_expected_value = fields.Integer(string="租金(下限)")
    lessee_expected_value1 = fields.Integer(string="租金(上限)")
    build_area = fields.Char(string="區域")
    pet = fields.Boolean(string="寵物", default=False)
    worship_god = fields.Boolean(string="拜神", default=False)
    member_number = fields.Integer(string="同住人數 ")
    household_no = fields.Char(string="戶籍號碼")
    member_revenue = fields.Integer(string="年所得")

    lessee_family_line = fields.One2many('cloudrent.lessee_family_line','family_id',copy=False)
    lessee_family_realestate = fields.One2many('cloudrent.lessee_family_realestate','family_id',copy=False)
    lessee_family_assets = fields.One2many('cloudrent.lessee_family_assets','family_id',copy=False)

   # 業務相關許可證資訊
    license_no = fields.Char(string="證書字號")
    register_no = fields.Char(string="登記證字號")   # escrow_type=='3,4,5'
    leadid = fields.Many2one('crm.lead',string="商機來源")

    @api.onchange('escrow_pid')
    def onchangeescrowpid(self):
        self.cloudrent_account = self.escrow_pid
        if self.env.user.escrow_no.bus_vat:
           self.cloudrent_passwd = self.env.user.escrow_no.bus_vat
        else:
           self.cloudrent_passwd = self.escrow_pid

    def cloudrent_create_account(self):


        if self.escrow_type=='3':  # 管理師
            self.env.cr.execute("""update res_users set active=True where login='cloudrent_agent1'""")
            self.env.cr.execute("""commit""")
            myuser = self.env['res.users'].search([('login', '=', 'cloudrent_agent1')])
            res = myuser.copy()
            self.env.cr.execute("""update res_users set active=False where login='cloudrent_agent1'""")
            self.env.cr.execute("""commit""")
            myrec = self.env['res.users'].search([('id', '=', res.id)])

        elif self.escrow_type=='4': # 不動產經紀人
            self.env.cr.execute("""update res_users set active=True where login='cloudrent_agent2'""")
            self.env.cr.execute("""commit""")
            myuser = self.env['res.users'].search([('login', '=', 'cloudrent_agent2')])
            res = myuser.copy()
            self.env.cr.execute("""update res_users set active=False where login='cloudrent_agent2'""")
            self.env.cr.execute("""commit""")
            myrec = self.env['res.users'].search([('id', '=', res.id)])

        elif self.escrow_type=='5':   # 業務
            self.env.cr.execute("""update res_users set active=True where login='cloudrent_sale'""")
            self.env.cr.execute("""commit""")
            myuser = self.env['res.users'].search([('login','=','cloudrent_sale')])
            res = myuser.copy()
            self.env.cr.execute("""update res_users set active=False where login='cloudrent_sale'""")
            self.env.cr.execute("""commit""")
            myrec = self.env['res.users'].search([('id','=',res.id)])

        elif self.escrow_type=='6':  # 修繕廠商
            self.env.cr.execute("""update res_users set active=True where login='cloudrent_vendor'""")
            self.env.cr.execute("""commit""")
            myuser = self.env['res.users'].search([('login', '=', 'cloudrent_vendor')])
            res = myuser.copy()
            self.env.cr.execute("""update res_users set active=False where login='cloudrent_vendor'""")
            self.env.cr.execute("""commit""")
            myrec = self.env['res.users'].search([('id', '=', res.id)])

        elif self.escroe_type == '7':   # 秘書
            self.env.cr.execute("""update res_users set active=True where login='cloudrent_secretary'""")
            self.env.cr.execute("""commit""")
            myuser = self.env['res.users'].search([('login', '=', 'cloudrent_secretary')])
            res = myuser.copy()
            self.env.cr.execute("""update res_users set active=False where login='cloudrent_secretary'""")
            self.env.cr.execute("""commit""")
            myrec = self.env['res.users'].search([('id', '=', res.id)])


        mypasswd = (CryptContext(schemes=['pbkdf2_sha512']).encrypt(self.cloudrent_passwd))
        myrec.login = self.cloudrent_account
        myrec.password = self.cloudrent_passwd
        myrec.partner_id.name = self.escrow_man
        self.users_id = myrec.id

        view = self.env.ref('sh_message.sh_message_wizard')
        context = dict(self._context or {})
        context['message']='雲房登入帳號完成'
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




    @api.onchange('member_addr')
    def onchangeaddr(self):
        self.member_addr1 = self.member_addr

    def name_get(self):
        result = []
        for myrec in self:
            myname = "%s" % (myrec.escrow_man)
            result.append((myrec.id, myname))
        return result

    @api.model
    def create(self, vals):
        res = super(CloudRentEscrowMember, self).create(vals)
        if self.escrow_type=='2':
            self.env.cr.execute("""select genfamilyline(%d)""" % self.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genfamilyrealestate(%d)""" % self.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select genfamilyassets(%d)""" % self.id)
            self.env.cr.execute("""commit""")
        return res

    def write(self, vals):
        res = super(CloudRentEscrowMember, self).write(vals)
        for rec in self:
            if rec.escrow_type=='2':  # 房客時 重排seq
                self.env.cr.execute("""select genfamilyline(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select genfamilyrealestate(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select genfamilyassets(%d)""" % rec.id)
                self.env.cr.execute("""commit""")
        return res


class CloudRentLesseeFamilyLine(models.Model):
    _name = "cloudrent.lessee_family_line"
    _description = "申請人家屬成員資料"
    _order = "family_seq"

    family_id = fields.Many2one('cloudrent.escrow_member',ondelete='cascade')
    family_seq = fields.Integer(string="SEQ")
    escrow_man = fields.Char(string="家屬姓名")
    escrow_pid = fields.Char(string="家屬身份字號")
    member_birthday = fields.Date(string="家屬生日")
    escrow_title = fields.Char(string="家屬稱謂")
    escrow_revenue = fields.Integer(string="家屬年所得")

class CloudRentLesseeFamilyRealEstate(models.Model):
    _name = "cloudrent.lessee_family_realestate"
    _description = "申請人家屬成員房產清單"
    _order = "family_seq"

    family_id = fields.Many2one('cloudrent.escrow_member',ondelete='cascade')
    family_seq = fields.Integer(string="SEQ")
    lessee_estate_owner = fields.Char(string="房產持有者")
    lessee_estate_address = fields.Char(string="房屋所在地址")
    total_area = fields.Char(string="總面積(平方公尺)")
    stakeholder_per = fields.Char(string="持分比(分子/分母)")
    stakeholder_area = fields.Char(string="持分面積(平方公尺)")
    naturalization = fields.Selection([('Y','是'),('N','否')],string="是否設籍於該處")


class CloudRentLesseeFamilyAssets(models.Model):
    _name = "cloudrent.lessee_family_assets"
    _description = "申請人家屬(動產)/(不動產)總額清單"
    _order = "family_seq"

    family_id = fields.Many2one('cloudrent.escrow_member',ondelete='cascade')
    family_seq = fields.Integer(string="SEQ")
    lessee_assets_owner = fields.Char(string="持有者姓名")
    movable_property = fields.Integer(string="動產總額")
    real_estate = fields.Integer(string="不動產總額")



class CloudRentEquipPart(models.Model):
    _name = "cloudrent.equip_part"
    _description = "租房設備說明主檔"

    equip_categ = fields.Selection(EQUIPCATEG,select=True,string="設備分類",required=True)
    name = fields.Char(string="設備名稱")









