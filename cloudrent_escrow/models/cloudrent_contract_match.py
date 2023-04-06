# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import shutil
import base64, os
from base64 import b64decode,b64encode
from io import open
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

class CloudRentCotractMatch(models.Model):
    _name = "cloudrent.contract_match"
    _description = "租戶代管媒合合約"
    _order = "match_seq"

    @api.depends('build_createdate')
    def _get_buildage(self):
        for rec in self:
            if rec.build_createdate == False:
                rec.build_age = 0
            else:
                self.env.cr.execute("""select getbuildage('%s')""" % rec.build_createdate)
                rec.build_age = self.ev.cr.fetchone()[0]

    @api.depends('build_area')
    def _get_buildarea1(self):
        for rec in self:
            if not rec.build_area or rec.build_area==0:
                rec.build_area1 = 0.0
            else:
                rec.build_area1 = round((rec.build_area/0.3025),2)

    @api.depends('build_lessor')
    def _get_lessorcell(self):
        for rec in self:
            mylessorcell=''
            if rec.build_lessor:
                if not rec.build_lessor.member_cell:
                    mylessorcell = rec.build_lessor.member_phone1
                else:
                    mylessorcell = rec.build_lessor.member_cell
            rec.lessor_cell = mylessorcell

    @api.depends('build_lessee')
    def _get_lesseecell(self):
        for rec in self:
            mylesseecell = ''
            if rec.build_lessee:
                if not rec.build_lessee.member_cell:
                    mylesseecell = rec.build_lessee.member_phone1
                else:
                    mylesseecell = rec.build_lessee.member_cell
            rec.lessee_cell = mylesseecell

    @api.depends('lesseetype0_rent','lessee_type','admin_area')
    def _get_lesseetype1(self):
        for rec in self:
            if rec.lessee_type not in  ('4','5') :   # 300 億方案
                self.env.cr.execute("""select get_grant4_value('%s','%s')""" % (rec.lessee_type,rec.admin_area))
                myvalue = self.env.cr.fetchall()
                myvalue1 = myvalue[0][0]
                mymax = myvalue[1][0]
                #mymax = 4545
                myrent = 0
                if rec.lesseetype0_rent:
                    #if (rec.lesseetype0_rent * 0.225) >= mymax:
                    if (rec.lesseetype0_rent * myvalue1) >= mymax:
                        myrent = rec.lesseetype0_rent - mymax
                    else:
                        #myrent = round(rec.lesseetype0_rent * 0.775)
                        myrent = round(rec.lesseetype0_rent - round(rec.lesseetype0_rent * myvalue1))
                else:
                    myrent = 0
            else:
                myrent = 0
            rec.lesseetype1_rent = myrent

    @api.depends('lesseetype0_rent','lessee_type','admin_area')
    def _get_lesseetype2(self):
        for rec in self:
            if rec.lessee_type not in ('4','5'):
                self.env.cr.execute("""select get_grant4_value('%s','%s')""" % (rec.lessee_type, rec.admin_area))
                myvalue = self.env.cr.fetchall()
                #mymax = 7200
                myvalue1 = myvalue[0][0]
                mymax = myvalue[1][0]
                myrent = 0
                if rec.lesseetype0_rent:
                    #if (rec.lesseetype0_rent * 0.445) >= mymax:
                    if (rec.lesseetype0_rent * myvalue1) >= mymax:
                        myrent = rec.lesseetype0_rent - mymax
                    else:
                        #myrent = round(rec.lesseetype0_rent * 0.555)
                        myrent = round(rec.lesseetype0_rent - round(rec.lesseetype0_rent * myvalue1))
                else:
                    myrent = 0
            else:
                myrent = 0
            rec.lesseetype2_rent = myrent

    @api.depends('match_end_date')
    def _get_renewym(self):
        for rec in self:
            if not rec.match_end_date:
                rec.renew_ym = ''
            else:
                self.env.cr.execute("""select get_renew_ym('%s')""" % rec.match_end_date)
                rec.renew_ym = self.env.cr.fetchone()[0]

    @api.depends('lessee_renew1','lessee_renew2')
    def _can_renew(self):
        for rec in self:
            if not rec.lessee_renew1 and not rec.lessee_renew2:
                rec.can_renew = True
            elif rec.lessee_renew1 and not rec.lessee_renew2:
                rec.can_renew = True
            else:
                rec.can_renew = False

    @api.depends()
    def _get_matchenable(self):
        for rec in self:
            self.env.cr.execute("""select getmatchenable(%d)""" % rec.id)
            rec.match_enable = self.env.cr.fetchone()[0]


    escrow_no = fields.Many2one('cloudrent.escrow',string="業者",default=lambda self:self.env.user.escrow_no.id)
    crm_lead_id = fields.Many2one('crm.lead',string="業務商機")
    match_no = fields.Char(string="媒合編號")
    object_no = fields.Char(string="物件編號")
    lessee_no = fields.Char(string="房客編號")
    case_type = fields.Selection([('1','包租/包管'),('2','代租/代管')],string="案件類型")
    admin_area = fields.Selection([('1','台北市'),('2','新北市'),('3','桃園市'),('4','台中市'),('5','台南市'),('6','高雄市')],string="所屬行政區")
    build_sec = fields.Char(string="段")
    build_msec = fields.Char(string="小段")
    build_number = fields.Char(string="建號")
    house_number = fields.Char(string="建物門牌")
    place_number = fields.Char(string="建物坐落地號")
    parking_space = fields.Boolean(string="車位")
    ancillary_equipment = fields.Boolean(string="附屬設備")
    build_rent_situatiuon = fields.Selection([('1','所有權人自行使用'),('2','空屋無人使用'),('3','現有人承租'),('4','其他')],string="租賃住宅現況")
    rent_man = fields.Char(string="現承租人")         # build_rent_situation='3'
    rent_duedate = fields.Date(string="租期屆滿日")   # build_rent_situation='3'
    rent_other_desc = fields.Char(string="其他說明")  # build_rent_situation='4'
    entrust_start_date = fields.Date(string="委託租賃起始日")
    entrust_end_date = fields.Date(string="委託租賃截止日")
    build_createdate = fields.Date(string="建築完成日期")
    build_age = fields.Integer(string="屋齡",compute=_get_buildage)
    build_area = fields.Integer(string="坪數")
    build_area1 = fields.Float(digits=(8,2),string="平方公尺",store=True,compute=_get_buildarea1)
    build_for_rent = fields.Integer(string="待租租金(元/月)")
    build_contract_rent = fields.Integer(string="簽約租金(元/月)")
    general_build = fields.Selection([('1','透天厝'),('2','別墅')],string="一般建物")
    build_type = fields.Selection(BUILDTYPE,select=True,string="區分所有建物")
    build_pattern = fields.Selection(BUILDPATTERN,select=True,string="格局")
    build_pattern1 = fields.Char(string="格局")
    object_no1 = fields.Many2one('cloudrent.build',string="物件標的")
    build_lessor = fields.Many2one('cloudrent.escrow_member',string="所有權人")
    lessor_fin_instno = fields.Char(string="(出租人)金融機構代碼")
    lessor_fin_branch = fields.Char(string="(出租人)分行代碼")
    lessor_fin_name = fields.Char(string="(出租人)帳號戶名")
    lessor_fin_account = fields.Char(string="(出租人)帳戶號碼")
    lessor_pid = fields.Char(string="(出租人)身份證號碼")
    build_lessee = fields.Many2one('cloudrent.escrow_member',string="承租人")
    lessee_fin_instno = fields.Char(string="(承租人)金融機構代碼")
    lessee_fin_branch = fields.Char(string="(承租人)分行代碼")
    lessee_fin_name = fields.Char(string="(承租人)帳號戶名")
    lessee_fin_account = fields.Char(string="(承租人)帳戶號碼")
    lessee_pid = fields.Char(string="(承租人)身份證號碼")
    lessee_type = fields.Selection(LESSEETYPE,select=True,string="承租人身份類別")
    is_gov_300 = fields.Boolean(string="300億補貼專案", default=False)

    member_type = fields.Char(string="身份別")
    is_send = fields.Boolean(string="是否已送件?",default=False)
    match_start_date = fields.Date(string="合約起始日")
    match_end_date = fields.Date(string="合約截止日")
    safe_ins_fee_line = fields.One2many('cloudrent.safe_insurance_fee','safe_id',string="居家安全保險費",copy=False)
    notarial_fee_line = fields.One2many('cloudrent.notarial_fee','notarial_id',string="公證費",copy=False)
    escrow_repair_line = fields.One2many('cloudrent.repair_fee','repair_id',string="住宅出租修繕補助費",copy=False)
    grant_rent_line = fields.One2many('cloudrent.grant_rent','grant_id',string="租金補助",copy=False)
    escrow_develop_line = fields.One2many('cloudrent.escrow_develop','develop_id',string="開發費",copy=False)
    escrow_guarantee_line = fields.One2many('cloudrent.guarantee_fee','guarantee_id',string="包管費",copy=False)
    contract_match_line = fields.One2many('cloudrent.contract_match_fee','match_id',string="媒合費",copy=False)
    escrow_fee_line = fields.One2many('cloudrent.escrow_fee','escrow_id',string="代管費",copy=False)
    equip_part_line = fields.One2many('cloudrent.match_equip_part','equip_id',string="租屋家俱設備",copy=True)
    match_doc_line = fields.One2many('cloudrent.match_doc_line','doc_id',string="申請書/契約書",copy=False)

    match_doc_ids = fields.Many2many('cloudrent.doc_filename','cloudrent_match_docfilename_rel','match_id','doc_id',string="(申請書/契約書)篩選")
    week_seq = fields.Integer(string="週次")
    match_year = fields.Char(string="年")
    match_month = fields.Char(string="月")

    lessee_renew1 = fields.Boolean(string="續1")
    lessee_renew2 = fields.Boolean(string="續2")
    lessee_terminate = fields.Boolean(string="解約")
    match_seq = fields.Integer(string="序")
    writ_addr = fields.Char(string="權狀地址")
    build_community = fields.Char(string="社區")
    build_loc = fields.Char(string="地區")
    lesseetype0_rent = fields.Integer(string="一般戶租金")
    lesseetype1_rent = fields.Integer(string="一類戶租金",store=True,compute=_get_lesseetype1)
    lesseetype2_rent = fields.Integer(string="二類戶租金",store=True,compute=_get_lesseetype2)
    management_fee = fields.Integer(string="管理費")
    parking_fee = fields.Integer(string="車位租金")
    lessee_grant = fields.Integer(string="補助款")
    register_household = fields.Boolean(string="入戶籍")
    lessee_memo = fields.Text(string="備註")
    lessee_tot_rent = fields.Integer(string="房客應繳租金")
    substitue_rent = fields.Boolean(string="申請代墊租金?",default=False)
    renew_ym = fields.Char(string="通知續約年月",store=True,compute=_get_renewym)
    lessor_notice_date = fields.Date(string="房東通知續約日")
    lessee_notice_date = fields.Date(string="房客通知續約日")
    renew_notarial_date = fields.Date(string="續約公證日期")
    origin_lessee_type = fields.Selection(LESSEETYPE,select=True,string="原客戶類別")
    new_lessee_type = fields.Selection(LESSEETYPE,select=True,string="新客戶類別")
    renew_start_date = fields.Date(string="續約起始日")
    renew_end_date = fields.Date(string="續約截止日")
    lessor_sale = fields.Many2one('cloudrent.escrow_member',string="屋主業務")
    lessee_sale = fields.Many2one('cloudrent.escrow_member',string="房客業務")
    lessor_cell = fields.Char(string="出租人電話",compute=_get_lessorcell)
    lessee_cell = fields.Char(string="承租人電話",compute=_get_lesseecell)
    lessee_contact = fields.Char(string="聯絡人")
    lessee_visit = fields.Date(string='[1-3月]訪視日期')
    lessee_visit1 = fields.Date(string="[4-6月]訪視日期")
    lessee_visit2 = fields.Date(string="[7-9月]訪視日期")
    lessee_visit3 = fields.Date(string="[10-12月]訪視日期")
    active = fields.Boolean(string="ACTIVE",default=True)
    match_status = fields.Selection([('1','入住'),('2','退租')],string="狀態",default='1')
    quit_date = fields.Date(string="退租日期")
    quit_line = fields.Many2one('cloudrent.quit_lease',string="退租點交記錄")
    match_version = fields.Many2one('cloudrent.contract_version',string="申請書合約版本期數")
    gen_doc_ids = fields.Many2many('cloudrent.doc_filename', 'cloudrent_match_docfilename_rel', 'match_id', 'doc_id',string="(申請書/契約書)篩選")
    can_renew = fields.Boolean(string="能續約?",compute=_can_renew)
    renew1 = fields.Many2one('cloudrent.contract_match',string="來源合約")
    match_complete_date = fields.Date(string="媒合成立日")
    match_enable = fields.Boolean(string="有效?",store=True,compute=_get_matchenable)


    # 手動產生 租房設備清單 from build to match
    def gen_btom_equip_part(self):
        self.env.cr.execute("""select gen_btom_equip_part(%d,%d)""" % (self.object_no1.id,self.id))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '完成同步出租建物的設備清單'
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

    def gen_new_fee(self):
        self.env.cr.execute("""select genmatchfee(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']= '費用及補助數據重新產生完成'
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

    def name_get(self):
        result = []
        for myrec in self:
            if not myrec.lessee_renew1 and not myrec.lessee_renew2:
               myname = "[%s]%s_%s" % (myrec.match_no, '新約',myrec.build_lessor.escrow_man)
            elif myrec.lessee_renew1 and not myrec.lessee_renew2:
                myname = "[%s]%s_%s" % (myrec.match_no, '續一', myrec.build_lessor.escrow_man)
            elif not myrec.lessee_renew1 and myrec.lessee_renew2:
                myname = "[%s]%s_%s" % (myrec.match_no, '續二', myrec.build_lessor.escrow_man)
            result.append((myrec.id, myname))
        return result

    @api.onchange('match_start_date')
    def onchangemsd(self):
        if not self.entrust_start_date:
            self.env.cr.execute("""select get_enddate('%s')""" % self.match_start_date)
            self.match_end_date = self.env.cr.fetchone()[0]
            self.entrust_start_date = self.match_start_date
            self.entrust_end_date = self.match_end_date

    @api.onchange('match_end_date')
    def onchangemed(self):
        if not self.entrust_end_date:
            self.entrust_end_date = self.match_end_date

    @api.model
    def create(self, vals):
        res = super(CloudRentCotractMatch, self).create(vals)
        try:
            self.env.cr.execute("""select gen_new_build(%d)""" % self.id)
            self.env.cr.execute("""commit""")
        except:
            A=1
        try:
            self.env.cr.execute("""select gen_lessee_grant(%d)""" % self.id)
            self.env.cr.execute("""commit""")
        except:
            A=1
        return res


    def write(self, vals):
        res = super(CloudRentCotractMatch, self).write(vals)
        for rec in self:
            # 同步到 建物主檔
            self.env.cr.execute("""select gen_new_build(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
            self.env.cr.execute("""select gen_lessee_grant(%d)""" % rec.id)
            self.env.cr.execute("""commit""")

        return res

    def run_docx_replace(self):  # 申請書自動生成
        havelicense = self.env['ir.config_parameter'].sudo().get_param('have_aspose_license')
        if havelicense=='Y':
           import aspose.words as aw
        # 原 DOCX 表格
        docx_path = self.env['ir.config_parameter'].sudo().get_param('cloudrent.docx.path')
        # copy 到目的端檔案
        docx_path1 = self.env['ir.config_parameter'].sudo().get_param('cloudrent.docx.path1')
        for rec in self.gen_doc_ids:
            mydocid = rec.id
            mydocrec = self.env['cloudrent.doc_filename'].search([('id','=',mydocid)])
            myfilename = mydocrec.doc_filename
            mydocname = self.match_no + "_"+ mydocrec.name

            # myfilename = "sh_escrow_rent_contract.docx"
            if docx_path[-1:] != "/":
                fn = docx_path + "/" + myfilename
            else:
                fn = docx_path + myfilename

            self.env.cr.execute("""select get_docxtemp()""")
            tempfilename = self.env.cr.fetchone()[0]
            if docx_path1[-1:] != "/":
                docxnewname = docx_path1 + "/" + tempfilename
            else:
                docxnewname = docx_path1 + tempfilename
            if havelicense=='N':
                if mydocrec.doc_binfile1:
                    bfile = b64decode(mydocrec.doc_binfile1)
                    with open(docxnewname, "wb") as f:
                        f.write(bfile)
                    with open(docxnewname, "rb") as f:
                        myout = f.read()
                    self.env.cr.execute("""select gendocline1(%d,%d)""" % (self.id,mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.match_doc_line'].sudo().search([('id','=',mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.match_no,'doc_file': b64encode(myout),'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)
            else:
                if mydocrec.doc_binfile:
                    bfile = b64decode(mydocrec.doc_binfile)
                    with open(docxnewname, "wb") as f:
                        f.write(bfile)
                self.env.cr.execute("""select get_contract_tag(%d)""" % mydocid)
                mydocid1 = self.env.cr.fetchone()[0]

                doc = aw.Document(docxnewname)  # 出租人申請書
                if mydocid1 == 1: # 社會住宅代租代管委託租賃契約書
                    # replace text
                    if self.build_lessor_name :
                        myescrowman = self.build_lessor_name
                    else:
                        myescrowman = ' '
                    mybuildlessor = self.build_lessor.escrow_man
                    doc.range.replace("build_lessor", myescrowman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_name :
                        mybusname = self.escrow_agent.bus_name
                    else:
                        mybusname = ' '
                    doc.range.replace("escrow_agent", mybusname,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.parking_space :
                        myps1 = '■'
                        myps2 = '□'
                    else:
                        myps2 = '■'
                        myps1 = '□'
                    doc.range.replace("ps1", myps1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ps2", myps2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.ancillary_equipment:
                        myae1 = '■'
                        myae2 = '□'
                    else:
                        myae2 = '■'
                        myae1 = '□'
                    doc.range.replace("ae1", myae1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ae2", myae2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.rent_man:
                        myrentman = self.rent_man
                    else :
                        myrentman = '  '
                    doc.range.replace("rent_man", myrentman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.rent_duedate:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.rent_duedate)
                        myrd = self.env.cr.fetchall()
                        doc.range.replace("rdy", myrd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdm", myrd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdd", myrd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.rent_other_desc:
                        myrod = self.rent_other_desc
                    else:
                        myrod = ' '
                    doc.range.replace("rod", myrod,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_start_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_start_date)
                        myesdy = self.env.cr.fetchall()
                        doc.range.replace("esdy", myesdy[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm", myesdy[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd", myesdy[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_end_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_end_date)
                        myesdy1 = self.env.cr.fetchall()
                        doc.range.replace("esdy1", myesdy1[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm1", myesdy1[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd1", myesdy1[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_for_rent:
                        mybfr = str(self.build_for_rent)
                    else:
                        mybfr = ' '
                    doc.range.replace("bfr", mybfr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_instno:
                        mylfi = self.lessor_fin_instno
                    else:
                        mylfi = ' '
                    doc.range.replace("lfi", mylfi,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_name:
                        mylfn = self.lessor_fin_name
                    else:
                        mylfn = ' '
                    doc.range.replace("lfn", mylfn,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_account:
                        mylfa = self.lessor_fin_account
                    else:
                        mylfa = ' '
                    doc.range.replace("lfa", mylfa,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_pid:
                        mylessorpid = self.lessor_pid
                    else:
                        mylessorpid = ' '
                    doc.range.replace("lessor_pid", mylessorpid,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_addr1:
                        mylessoraddr1 = self.lessor_addr1
                    else:
                        mylessoraddr1 = ' '
                    doc.range.replace("lessor_addr1", mylessoraddr1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_phone1:
                        mylessorphone1 = self.lessor_phone1
                    else:
                        mylessorphone1 = ' '
                    doc.range.replace("lessor_phone1", mylessorphone1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_vat:
                        myescrowvat = self.escrow_agent.bus_vat
                    else:
                        myescrowvat = ' '
                    doc.range.replace("escrow_vat", myescrowvat,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_boss:
                        myescrowboss = self.escrow_agent.bus_boss
                    else:
                        myescrowboss = ' '
                    doc.range.replace("escrow_boss", myescrowboss,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.license_no:
                        myescrowlicenseno = self.escrow_agent.license_no
                    else:
                        myescrowlicenseno = ' '
                    doc.range.replace("escrow_license_no", myescrowlicenseno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.register_no:
                        myescrowregisterno = self.escrow_agent.register_no
                    else:
                        myescrowregisterno = ' '
                    doc.range.replace("escrow_register_no", myescrowregisterno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        myescrowbusaddr = self.escrow_agent.bus_address
                    else:
                        myescrowbusaddr = ' '
                    doc.range.replace("escrow_bus_addr", myescrowbusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.house_number:
                        myhousenumber = self.house_number
                    else:
                        myhousenumber = ' '
                    doc.range.replace("house_number", myhousenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.place_number:
                        myplacenumber = self.place_number
                    else:
                        myplacenumber = ' '
                    doc.range.replace("place_number", myplacenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_number:
                        mybuildnumber = self.build_number
                    else:
                        mybuildnumber = ' '
                    doc.range.replace("build_number", mybuildnumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_area1:
                        mybuildarea1 = str(self.build_area1)
                    else:
                        mybuildarea1 = ' '
                    doc.range.replace("build_area1", mybuildarea1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_rent_situation == '1':
                        mybrs1='■'
                        mybrs2='□'
                        mybrs3='□'
                        mybrs4='□'
                    elif self.build_rent_situation=='2':
                        mybrs1 = '□'
                        mybrs2 = '■'
                        mybrs3 = '□'
                        mybrs4 = '□'
                    elif self.build_rent_situation=='3':
                        mybrs1 = '□'
                        mybrs2 = '□'
                        mybrs3 = '■'
                        mybrs4 = '□'
                    elif self.build_rent_situation=='4':
                        mybrs1 = '□'
                        mybrs2 = '□'
                        mybrs3 = '□'
                        mybrs4 = '■'
                    else:
                        mybrs1 = '□'
                        mybrs2 = '□'
                        mybrs3 = '□'
                        mybrs4 = '□'
                    doc.range.replace("brs1", mybrs1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("brs2", mybrs2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("brs3", mybrs3,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("brs4", mybrs4,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.rent_paytype=='1':
                        myrpt1 = '■'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    elif self.rent_paytype=='2':
                        myrpt1 = '□'
                        myrpt2 = '■'
                        myrpt3 = '□'
                    elif self.rent_paytype=='3':
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '■'
                    else:
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    doc.range.replace("rpt1", myrpt1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt2", myrpt2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt3", myrpt3,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % fields.Date.today())
                    mytd = self.env.cr.fetchall()
                    doc.range.replace("apy", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ry", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    mybusphone = self.escrow_agent.bus_phone
                    doc.range.replace("escrow_bus_phone", mybusphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.save(docxnewname)
                    with open(docxnewname, "rb") as f:
                        myout = f.read()
                    self.env.cr.execute("""select gendocline(%d,%d)""" % (self.id,mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.match_doc_line'].sudo().search([('id','=',mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.match_no,'doc_file': b64encode(myout),'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)
                elif mydocid1 == 2:  # 社會住宅代租代管委託管理契約書
                    # replace text
                    if self.object_no:
                        mybuildno = self.object_no
                    else:
                        mybuildno = ' '
                    doc.range.replace("build_no", mybuildno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.match_no:
                        mymatchno = self.match_no
                    else:
                        mymatchno = ' '
                    doc.range.replace("match_no", mymatchno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_lessor_name:
                        myescrowman = self.build_lessor_name
                    else:
                        myescrowman = ' '
                    mybuildlessor = self.build_lessor.escrow_man
                    doc.range.replace("build_lessor", myescrowman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_name:
                        mybusname = self.escrow_agent.bus_name
                    else:
                        mybusname = ' '
                    doc.range.replace("escrow_agent", mybusname,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.parking_space:
                        myps1 = '■'
                        myps2 = '□'
                    else:
                        myps2 = '■'
                        myps1 = '□'
                    doc.range.replace("ps1", myps1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ps2", myps2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.ancillary_equipment:
                        myae1 = '■'
                        myae2 = '□'
                    else:
                        myae2 = '■'
                        myae1 = '□'
                    doc.range.replace("ae1", myae1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ae2", myae2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_start_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_start_date)
                        myesdy = self.env.cr.fetchall()
                        doc.range.replace("rdy", myesdy[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdm", myesdy[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdd", myesdy[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("rdy", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdm", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdd", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_end_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_end_date)
                        myesdy1 = self.env.cr.fetchall()
                        doc.range.replace("rdy1", myesdy1[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdm1", myesdy1[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdd1", myesdy1[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("rdy1", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdm1", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("rdd1", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.lessor_fin_instno:
                        mylfi = self.lessor_fin_instno
                    else:
                        mylfi = ' '
                    doc.range.replace("lfi", mylfi,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_name:
                        mylfn = self.lessor_fin_name
                    else:
                        mylfn = ' '
                    doc.range.replace("lfn", mylfn,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_account:
                        mylfa = self.lessor_fin_account
                    else:
                        mylfa = ' '
                    doc.range.replace("lfa", mylfa,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_pid:
                        mylessorpid = self.lessor_pid
                    else:
                        mylessorpid = ' '
                    doc.range.replace("lessor_pid", mylessorpid,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_addr1:
                        mylessoraddr1 = self.lessor_addr1
                    else:
                        mylessoraddr1 = ' '
                    doc.range.replace("lessor_address", mylessoraddr1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_phone1:
                        mylessorphone1 = self.lessor_phone1
                    else:
                        mylessorphone1 = ' '
                    doc.range.replace("lessor_phone", mylessorphone1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_vat:
                        myescrowvat = self.escrow_agent.bus_vat
                    else:
                        myescrowvat = ' '
                    doc.range.replace("escrow_vat", myescrowvat,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_boss:
                        myescrowboss = self.escrow_agent.bus_boss
                    else:
                        myescrowboss = ' '
                    doc.range.replace("escrow_boss", myescrowboss,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.license_no:
                        myescrowlicenseno = self.escrow_agent.license_no
                    else:
                        myescrowlicenseno = ' '
                    doc.range.replace("escrow_license_no", myescrowlicenseno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.register_no:
                        myescrowregisterno = self.escrow_agent.register_no
                    else:
                        myescrowregisterno = ' '
                    doc.range.replace("escrow_register_no", myescrowregisterno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        myescrowbusaddr = self.escrow_agent.bus_address
                    else:
                        myescrowbusaddr = ' '
                    doc.range.replace("escrow_bus_addr", myescrowbusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.house_number:
                        myhousenumber = self.house_number
                    else:
                        myhousenumber = ' '
                    doc.range.replace("house_number", myhousenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.place_number:
                        myplacenumber = self.place_number
                    else:
                        myplacenumber = ' '
                    doc.range.replace("place_number", myplacenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_number:
                        mybuildnumber = self.build_number
                    else:
                        mybuildnumber = ' '
                    doc.range.replace("build_number", mybuildnumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_area1:
                        mybuildarea1 = str(self.build_area1)
                    else:
                        mybuildarea1 = ' '
                    doc.range.replace("build_area1", mybuildarea1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.rent_paytype == '1':
                        myrpt1 = '■'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    elif self.rent_paytype == '2':
                        myrpt1 = '□'
                        myrpt2 = '■'
                        myrpt3 = '□'
                    elif self.rent_paytype == '3':
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '■'
                    else:
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    doc.range.replace("rpt1", myrpt1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt2", myrpt2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt3", myrpt3,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % fields.Date.today())
                    mytd = self.env.cr.fetchall()
                    doc.range.replace("apy", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ry", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_phone:
                        mybusphone = self.escrow_agent.bus_phone
                    else:
                        mybusphone = ' '
                    doc.range.replace("escrow_bus_phone", mybusphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        mybusaddr=self.escrow_agent.bus_address
                    else:
                        mybusaddr = ' '
                    doc.range.replace("escrow_bus_addr", mybusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.save(docxnewname)
                    with open(docxnewname, "rb") as f:
                        myout = f.read()
                    self.env.cr.execute("""select gendocline(%d,%d)""" % (self.id, mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.match_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.match_no, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)
                elif mydocid1 == 3:   # 社會住宅租賃契約書
                    # replace text
                    if self.object_no:
                        mybuildno = self.object_no
                    else:
                        mybuildno = ' '
                    doc.range.replace("build_no", mybuildno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.match_no:
                        mymatchno = self.match_no
                    else:
                        mymatchno = ' '
                    doc.range.replace("match_no", mymatchno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_lessor_name:
                        myescrowman = self.build_lessor_name
                    else:
                        myescrowman = ' '
                    mybuildlessor = self.build_lessor.escrow_man
                    doc.range.replace("build_lessor", myescrowman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_name:
                        myrentman = self.lessee_name
                    else:
                        myrentman = ' '
                    doc.range.replace("rent_man", myrentman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_name:
                        mybusname = self.escrow_agent.bus_name
                    else:
                        mybusname = ' '
                    doc.range.replace("escrow_agent", mybusname,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.parking_space:
                        myps1 = '■'
                        myps2 = '□'
                    else:
                        myps2 = '■'
                        myps1 = '□'
                    doc.range.replace("ps1", myps1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ps2", myps2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.ancillary_equipment:
                        myae1 = '■'
                        myae2 = '□'
                    else:
                        myae2 = '■'
                        myae1 = '□'
                    doc.range.replace("ae1", myae1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ae2", myae2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_start_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_start_date)
                        myesdy = self.env.cr.fetchall()
                        doc.range.replace("esdy", myesdy[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm", myesdy[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd", myesdy[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("esdy", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_end_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_end_date)
                        myesdy1 = self.env.cr.fetchall()
                        doc.range.replace("eedy", myesdy1[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedm", myesdy1[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedd", myesdy1[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("eedy", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedm", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedd", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.lessor_fin_instno:
                        mylfi = self.lessor_fin_instno
                    else:
                        mylfi = ' '
                    doc.range.replace("lfi", mylfi,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_name:
                        mylfn = self.lessor_fin_name
                    else:
                        mylfn = ' '
                    doc.range.replace("lfn", mylfn,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_fin_account:
                        mylfa = self.lessor_fin_account
                    else:
                        mylfa = ' '
                    doc.range.replace("lfa", mylfa,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_pid:
                        mylessorpid = self.lessor_pid
                    else:
                        mylessorpid = ' '
                    doc.range.replace("lessor_pid", mylessorpid,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_addr1:
                        mylessoraddr1 = self.lessor_addr1
                    else:
                        mylessoraddr1 = ' '
                    doc.range.replace("lessor_address", mylessoraddr1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessor_phone1:
                        mylessorphone1 = self.lessor_phone1
                    else:
                        mylessorphone1 = ' '
                    doc.range.replace("lessor_phone", mylessorphone1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_pid:
                        myrentpid = self.lessee_pid
                    else:
                        myrentpid = ' '
                    doc.range.replace("rent_pid", myrentpid,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_addr:
                        myrentaddr = self.lessee_addr
                    else:
                        myrentaddr = ' '
                    doc.range.replace("rent_address", myrentaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_cell:
                        myrentphone = self.lessee_cell
                    else:
                        myrentphone = ' '
                    doc.range.replace("rent_phone", myrentphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_contract_rent and self.build_contract_rent >0:
                        mybfr = str(self.build_contract_rent)
                    else:
                        mybfr = ' '
                    doc.range.replace("bfr", mybfr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.parking_fee and self.parking_fee >0:
                        mypf = str(self.parking_fee)
                    else:
                        mypf = ' '
                    doc.range.replace("pf", mypf,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_contract_rent and self.parking_fee and (self.build_contract_rent+self.parking_fee)>0 :
                        mybfrp = str(self.build_contract_rent + self.parking_fee)
                    else:
                        mybfrp = ' '
                    doc.range.replace("bfrp", mypf,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        myescrowbusaddr = self.escrow_agent.bus_address
                    else:
                        myescrowbusaddr = ' '
                    doc.range.replace("escrow_bus_addr", myescrowbusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.house_number:
                        myhousenumber = self.house_number
                    else:
                        myhousenumber = ' '
                    doc.range.replace("house_number", myhousenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.place_number:
                        myplacenumber = self.place_number
                    else:
                        myplacenumber = ' '
                    doc.range.replace("place_number", myplacenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_number:
                        mybuildnumber = self.build_number
                    else:
                        mybuildnumber = ' '
                    doc.range.replace("build_number", mybuildnumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_area1:
                        mybuildarea1 = str(self.build_area1)
                    else:
                        mybuildarea1 = ' '
                    doc.range.replace("build_area1", mybuildarea1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.rent_paytype == '1':
                        myrpt1 = '■'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    elif self.rent_paytype == '2':
                        myrpt1 = '□'
                        myrpt2 = '■'
                        myrpt3 = '□'
                    elif self.rent_paytype == '3':
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '■'
                    else:
                        myrpt1 = '□'
                        myrpt2 = '□'
                        myrpt3 = '□'
                    doc.range.replace("rpt1", myrpt1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt2", myrpt2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("rpt3", myrpt3,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % fields.Date.today())
                    mytd = self.env.cr.fetchall()
                    doc.range.replace("apy", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_phone:
                        mybusphone = self.escrow_agent.bus_phone
                    else:
                        mybusphone = ' '
                    doc.range.replace("escrow_bus_phone", mybusphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        mybusaddr = self.escrow_agent.bus_address
                    else:
                        mybusaddr = ' '
                    doc.range.replace("escrow_bus_addr", mybusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.deposit_value and self.deposit_value > 0:
                        mydeposit = str(self.deposit_value)
                    else:
                        mydeposit = ' '
                    doc.range.replace("deposit", mydeposit,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_fee and self.management_fee > 0:
                        mymanfee = str(self.management_fee)
                    else:
                        mymanfee = ' '
                    doc.range.replace("rmf", mymanfee,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_man:
                        mymm = self.management_man.escrow_man
                    else:
                        mymm = ' '
                    doc.range.replace("mm", mymm,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.save(docxnewname)
                    with open(docxnewname, "rb") as f:
                        myout = f.read()
                    self.env.cr.execute("""select gendocline(%d,%d)""" % (self.id, mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.match_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.match_no, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)
                elif mydocid1 == 4:   # 社會住宅轉租契約書
                    # replace text
                    if self.lessee_name:
                        myrentman = self.lessee_name
                    else:
                        myrentman = ' '
                    doc.range.replace("rent_man", myrentman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_name:
                        mybusname = self.escrow_agent.bus_name
                    else:
                        mybusname = ' '
                    doc.range.replace("escrow_agent", mybusname,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.object_no:
                        mybuildno = self.object_no
                    else:
                        mybuildno = ' '
                    doc.range.replace("build_no", mybuildno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.match_no:
                        mymatchno = self.match_no
                    else:
                        mymatchno = ' '
                    doc.range.replace("match_no", mymatchno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_lessor_name:
                        myescrowman = self.build_lessor_name
                    else:
                        myescrowman = ' '
                    mybuildlessor = self.build_lessor.escrow_man
                    doc.range.replace("build_lessor", myescrowman,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_name:
                        mybusname = self.escrow_agent.bus_name
                    else:
                        mybusname = ' '
                    doc.range.replace("escrow_agent", mybusname,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.parking_space:
                        myps1 = '■'
                        myps2 = '□'
                    else:
                        myps2 = '■'
                        myps1 = '□'
                    doc.range.replace("ps1", myps1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ps2", myps2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.ancillary_equipment:
                        myae1 = '■'
                        myae2 = '□'
                    else:
                        myae2 = '■'
                        myae1 = '□'
                    doc.range.replace("ae1", myae1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("ae2", myae2,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_start_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_start_date)
                        myesdy = self.env.cr.fetchall()
                        doc.range.replace("esdy", myesdy[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm", myesdy[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd", myesdy[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("esdy", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdm", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("esdd", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.entrust_end_date:
                        self.env.cr.execute("""select gen_twyy_mm_dd('%s')""" % self.entrust_end_date)
                        myesdy1 = self.env.cr.fetchall()
                        doc.range.replace("eedy", myesdy1[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedm", myesdy1[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedd", myesdy1[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    else:
                        doc.range.replace("eedy", '   ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedm", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                        doc.range.replace("eedd", '  ',aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    if self.lessee_pid:
                        myrentpid = self.lessee_pid
                    else:
                        mylesseepid = ' '
                    doc.range.replace("rent_pid", mylessorpid,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_addr:
                        myrentaddr = self.lessee_addr
                    else:
                        myrentaddr = ' '
                    doc.range.replace("rent_address", myrentaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.lessee_cell:
                        myrentphone = self.lessee_cell
                    else:
                        myrentphone = ' '
                    doc.range.replace("rent_phone", myrentphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_vat:
                        myescrowvat = self.escrow_agent.bus_vat
                    else:
                        myescrowvat = ' '
                    doc.range.replace("escrow_vat", myescrowvat,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_boss:
                        myescrowboss = self.escrow_agent.bus_boss
                    else:
                        myescrowboss = ' '
                    doc.range.replace("escrow_boss", myescrowboss,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.license_no:
                        myescrowlicenseno = self.escrow_agent.license_no
                    else:
                        myescrowlicenseno = ' '
                    doc.range.replace("escrow_license_no", myescrowlicenseno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.register_no:
                        myescrowregisterno = self.escrow_agent.register_no
                    else:
                        myescrowregisterno = ' '
                    doc.range.replace("escrow_register_no", myescrowregisterno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        myescrowbusaddr = self.escrow_agent.bus_address
                    else:
                        myescrowbusaddr = ' '
                    doc.range.replace("escrow_bus_addr", myescrowbusaddr,
                                      aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.house_number:
                        myhousenumber = self.house_number
                    else:
                        myhousenumber = ' '
                    doc.range.replace("house_number", myhousenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.place_number:
                        myplacenumber = self.place_number
                    else:
                        myplacenumber = ' '
                    doc.range.replace("place_number", myplacenumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_number:
                        mybuildnumber = self.build_number
                    else:
                        mybuildnumber = ' '
                    doc.range.replace("build_number", mybuildnumber,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_area1:
                        mybuildarea1 = str(self.build_area1)
                    else:
                        mybuildarea1 = ' '
                    doc.range.replace("build_area1", mybuildarea1,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    self.env.cr.execute("""select gen_twyy_mm_dd(%s)""" % fields.Date.today())
                    mytd = self.env.cr.fetchall()
                    doc.range.replace("apy", mytd[0][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apm", mytd[1][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    doc.range.replace("apd", mytd[2][0],aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_phone:
                        mybusphone = self.escrow_agent.bus_phone
                    else:
                        mybusphone = ' '
                    doc.range.replace("escrow_bus_phone", mybusphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.escrow_agent.bus_address:
                        mybusaddr = self.escrow_agent.bus_address
                    else:
                        mybusaddr = ' '
                    doc.range.replace("escrow_bus_addr", mybusaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_fee and self.management_fee > 0:
                        mymanfee = str(self.management_fee)
                    else:
                        mymanfee = ' '
                    doc.range.replace("rmf", mymanfee,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.build_contract_rent and self.build_contract_rent >0:
                        mybfr = str(self.build_contract_rent)
                    else:
                        mybfr = ' '
                    doc.range.replace("bfr", mybfr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_man:
                        mymm = self.management_man.escrow_man
                    else:
                        mymm = ' '
                    doc.range.replace("mm", mymm,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_man.license_no:
                        mylicno = self.management_man.license_no
                    else:
                        mylicno = ' '
                    doc.range.replace("mm_license_no", mylicno,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_man.member_addr1:
                        mymmaddr = self.management_man.member_addr1
                    else:
                        mymmaddr = ' '
                    doc.range.replace("mm_addr", mymmaddr,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))
                    if self.management_man.member_cell:
                        mymmphone = self.management_man.member_cell
                    else:
                        mymmphone = ' '
                    doc.range.replace("mm_phone", mymmphone,aw.replacing.FindReplaceOptions(aw.replacing.FindReplaceDirection.FORWARD))

                    doc.save(docxnewname)
                    with open(docxnewname, "rb") as f:
                        myout = f.read()
                    self.env.cr.execute("""select gendocline(%d,%d)""" % (self.id, mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.match_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.match_no, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)



class CloudRentSafeInsFeeLine(models.Model):
    _name = "cloudrent.safe_insurance_fee"
    _description = "居家安全保險費(M1)"
    _order = "safe_seq"

    safe_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    safe_seq = fields.Integer(string="次")
    real_insurance_fee = fields.Integer(string="實際投保金額")
    ins_applyfor_date = fields.Date(string="申請日期")
    ins_applyfor_year = fields.Char(string="年")
    ins_applyfor_month = fields.Char(string="月")
    ins_applyfor_fee = fields.Integer(string="申請金額")
    is_applyfor = fields.Boolean(string="已申請")

    # @api.model
    # def create(self, vals):
    #     res = super(CloudRentSafeInsFeeLine, self).create(vals)
    #     self.env.cr.execute("""select chk_grant_repair(%d)""" % self.safe_id.id)
    #     myres = self.env.cr.fetchone()[0]
    #     if not myres:
    #         raise UserError("""保險費+修繕補助申請金額超過上限""")
    #     return res



class CloudRentNotarialFeeLine(models.Model):
    _name = "cloudrent.notarial_fee"
    _description = "公證費(M2)"
    _order = "notarial_seq"

    notarial_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    notarial_seq = fields.Integer(string="次")
    real_notarial_fee = fields.Integer(string="實際支付金額")
    notarial_applyfor_date = fields.Date(string="申請日期")
    notarial_applyfor_fee = fields.Integer(string="申請金額")
    notarial_applyfor_year = fields.Char(string="年")
    notarial_applyfor_month = fields.Char(string="月")
    is_applyfor = fields.Boolean(string="已申請")

class CloudRentEscrowRepairLine(models.Model):
    _name = "cloudrent.repair_fee"
    _description = "住宅出租修繕補助費(M3)"
    _order = "repair_seq"

    repair_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    repair_seq = fields.Integer(string="序")
    real_repair_fee = fields.Integer(string="實際已修繕金額")
    repair_applyfor_date = fields.Date(string="申請日期")
    repair_year = fields.Char(string="年")
    repair_month = fields.Char(string="月")
    repair_applyfor_fee = fields.Integer(string="申請金額")
    is_applyfor = fields.Boolean(string="已申請")

    # @api.model
    # def create(self, vals):
    #     res = super(CloudRentEscrowRepairLine, self).create(vals)
    #     self.env.cr.execute("""select chk_grant_repair(%d)""" % self.repair_id.id)
    #     myres = self.env.cr.fetchone()[0]
    #     if not myres:
    #         raise UserError("""保險費+修繕補助申請金額超過上限""")
    #     return res

class CloudRentGrantRentLine(models.Model):
    _name = "cloudrent.grant_rent"
    _description = "租金補助(M4)"
    _order = "rent_seq"

    grant_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    rent_seq = fields.Integer(string="序")
    contract_rent_fee = fields.Integer(string="簽約租金(元/月)")
    applyfor_rent_fee = fields.Integer(string="可申請補助款")
    applyfor_rent_date = fields.Date(string="申請日期")
    applyfor_rent_year = fields.Char(string="年")
    applyfor_rent_month = fields.Char(string="月")
    rent_period = fields.Integer(string="期數")
    tot_rent_period = fields.Integer(string="總期數")
    is_applyfor = fields.Boolean(string="已申請")


class CloudRentEscrowDevelopLine(models.Model):
    _name = "cloudrent.escrow_develop"
    _description = "開發費(M5)"
    _order = "develop_seq"


    develop_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    develop_seq = fields.Integer(string="序")
    develop_applyfor_date = fields.Date(string="申請日期")
    develop_applyfor_fee = fields.Integer(string="可申請金額")
    develop_applyfor_year = fields.Char(string="年")
    develop_applyfor_month = fields.Char(string="月")
    is_applyfor = fields.Boolean(string="已申請")


class CloudRentEscrowGuaranteeLine(models.Model):
    _name = "cloudrent.guarantee_fee"
    _description = "包管費(M6)"
    _order = "guarantee_seq"

    guarantee_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    guarantee_seq = fields.Integer(string="序")
    guarantee_applyfor_date = fields.Date(string="申請日期")
    guarantee_applyfor_fee = fields.Integer(string="可申請金額")
    guarantee_applyfor_year = fields.Char(string="年")
    guarantee_applyfor_month = fields.Char(string="月")
    guarantee_period = fields.Integer(string="期數")
    guarantee_tot_period = fields.Integer(string="總期數")
    is_applyfor = fields.Boolean(string="已申請")

class CloudRentContractMatchLine(models.Model):
    _name = "cloudrent.contract_match_fee"
    _description = "媒合費(M7)"
    _order = "match_seq"

    match_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    match_seq = fields.Integer(string="序")
    match_applyfor_date = fields.Date(string="申請日期")
    match_applyfor_fee = fields.Integer(string="可申請金額")
    match_applyfor_year = fields.Char(string="年")
    match_applyfor_month = fields.Char(string="月")
    is_applyfor = fields.Boolean(string="已申請")


class CloudRentEscrowFeeLine(models.Model):
    _name = "cloudrent.escrow_fee"
    _description = "代管費(M8)"
    _order = "escrow_seq"

    escrow_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    escrow_seq = fields.Integer(string="序")
    escrow_period = fields.Integer(string="序")
    escrow_applyfor_date = fields.Date(string="申請日期")
    escrow_applyfor_fee = fields.Integer(string="可申請金額")
    escrow_applyfor_year = fields.Char(string="年")
    escrow_applyfor_month = fields.Char(string="月")
    escrow_applyfor_period = fields.Char(string="期數")
    escrow_tot_period = fields.Integer(string="總期數")
    is_applyfor = fields.Boolean(string="已申請")


class CloudRentMatchEquipPart(models.Model):
    _name = "cloudrent.match_equip_part"
    _description = "租屋家俱設備清單"

    equip_id = fields.Many2one('cloudrent.contract_match', ondelete='cascade')
    equip_categ = fields.Selection([('1', '家電類'), ('2', '家具類'), ('3', '鑰匙類'), ('4', '其他')], string="設備分類", required=True)
    equip_no = fields.Many2one('cloudrent.equip_part', string="設備名稱", required=True)
    equip_qty = fields.Integer(string="數量")
    equip_status = fields.Char(string="設備狀態描述")
    equip_image1 = fields.Binary(string='照片1',attachment=False)
    equip_image2 = fields.Binary(string="照片2",attachment=False)
    equip_image3 = fields.Binary(string="照片3",attachment=False)


    @api.onchange('equip_categ')
    def onchangeequipcateg(self):
        myrec = self.env['cloudrent.equip_part'].search([('equip_categ','=',self.equip_categ)])
        myids=[]
        for rec in myrec:
            myids.append(rec.id)
        return {'domain': {'equip_no': [('id', 'in', myids)]}}

class CloudRentMatchDocLine(models.Model):
    _name = "cloudrent.match_doc_line"
    _description = "媒合相關申請書/契約書"
    _order = "doc_name"

    doc_id = fields.Many2one('cloudrent.contract_match',ondelete='cascade')
    doc_date = fields.Date(string="存檔日期", default=lambda self: fields.Date.today())
    doc_name = fields.Many2one('cloudrent.doc_filename',string="表單名稱",required=True)
    doc_desc = fields.Char(string="說明")
    doc_file = fields.Binary(string="系統樣板",attachment=False)
    doc_file1 = fields.Binary(string="用印完上傳",attachment=False)
    doc_applyfor_id = fields.Integer(string="申請書ID")
    doc_filename = fields.Char(string="檔名")
    doc_filename1 = fields.Char(string="檔名1")






