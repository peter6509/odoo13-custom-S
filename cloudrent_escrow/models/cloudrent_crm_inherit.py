# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
from odoo.http import request
import shutil
import base64, os
from base64 import b64decode,b64encode
from io import open
CASETYPE=[('1', '包租/包管'),
          ('2', '代租/代管')]
ADMINAREA=[('1', '台北市'),
           ('2', '新北市'),
           ('3', '桃園市'),
           ('4', '台中市'),
           ('5', '台南市'),
           ('6', '高雄市')]
RENTSITUATION=[('1', '所有權人自行使用'),
               ('2', '空屋無人使用'),
               ('3', '現有人承租'),
               ('4', '其他')]
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

class CloudRentCrmInherit(models.Model):
    _inherit = "crm.team"

    escrow_no = fields.Many2one('cloudrent.escrow', string="所屬代管業者")


class CloudRentCrmLead(models.Model):
    _inherit = "crm.lead"

    @api.depends('stage_id')
    def _get_crmstage(self):
        for rec in self:
            rec.stage_num = rec.stage_id.sequence

    @api.depends('build_createdate')
    def _get_buildage(self):
        for rec in self:
            if rec.build_createdate == False:
                rec.build_age = 0
            else:
                self.env.cr.execute("""select getbuildage('%s')""" % rec.build_createdate)
                rec.build_age = self.env.cr.fetchone()[0]

    @api.depends('build_area')
    def _get_buildarea1(self):
        for rec in self:
            if not rec.build_area or rec.build_area == 0:
                rec.build_area1 = 0.0
            else:
                rec.build_area1 = round((rec.build_area / 0.3025), 2)

    cus_name = fields.Char(string="客戶名稱")
    stage_num = fields.Integer(string="階段序號",store=True,compute=_get_crmstage)
    escrow_man = fields.Char(string="客戶姓名")
    escrow_pid = fields.Char(string="身份證號")
    escrow_agent = fields.Many2one('cloudrent.escrow', string="所屬代管業",default=lambda self:self.env.user.escrow_no)
    escrow_sale = fields.Many2one('cloudrent.escrow_member',string="本案業務")
    # escrow_type = fields.Selection([('1', '出租人/房東'), ('2', '承租人/房客'), ('3', '代管管理師'), ('4', '代管高級管理者'), ('5', '修繕廠商'), ('6', '系統管理員')],string="人員類別",default='2')

    # 屬場勘階段資料
    survey_date = fields.Date(string="場勘日期",default=fields.Date.today())
    case_type = fields.Selection(CASETYPE,select=True, string="案件類型")
    admin_area = fields.Selection(ADMINAREA,select=True,string="所屬行政區")
    build_sec = fields.Char(string="段")
    build_msec = fields.Char(string="小段")

    build_number = fields.Char(string="建號")
    house_number = fields.Char(string="建物門牌")
    place_number = fields.Char(string="建物坐落地號")
    parking_space = fields.Boolean(string="車位")
    ancillary_equipment = fields.Boolean(string="附屬設備")
    build_rent_situation = fields.Selection(RENTSITUATION,select=True,string="租賃住宅現況")
    rent_man = fields.Char(string="現承租人")  # build_rent_situation='3'
    rent_duedate = fields.Date(string="租期屆滿日")  # build_rent_situation='3'
    rent_other_desc = fields.Char(string="其他說明")  # build_rent_situation='4'
    entrust_start_date = fields.Date(string="委託(租賃/管理)起始日")
    entrust_end_date = fields.Date(string="委託(租賃/管理)截止日")

    build_createdate = fields.Date(string="建築完成日期")
    build_age = fields.Integer(string="屋齡", store=True,compute=_get_buildage)
    build_area = fields.Integer(string="坪數")
    build_area1 = fields.Float(digits=(8, 2), string="平方公尺",stroe=True ,compute=_get_buildarea1)
    general_build = fields.Selection([('1', '透天厝'), ('2', '別墅')], string="一般建物")
    build_type = fields.Selection(BUILDTYPE,select=True, string="區分所有建物")
    build_pattern = fields.Selection(BUILDPATTERN,select=True, string="格局")
    build_elevator = fields.Boolean(string="有電梯?", default=False)
    build_pet = fields.Boolean(string="養寵物?", default=False)

    # 場勘階段 拍照圖片
    sitecheck_pic_line = fields.One2many('cloudrent.sitecheck_pic_line','sitecheck_id',string="場勘圖片")

    # 屬申請書相關資訊
    lessor_doc_line = fields.One2many('cloudrent.lessor_doc_line','doc_id',string="申請書夾檔")

    equip_part_line = fields.One2many('cloudrent.crm_lead_equip_part','equip_id',string="場勘傢俱設備點交清單")

    # 屬招租階段相關資訊
    build_for_rent = fields.Integer(string="待租租金(元/月)")
    parking_fee = fields.Integer(string="車位租金(元/月)")
    management_fee = fields.Integer(string="管理費(元/月)")
    rent_paytype = fields.Selection([('1','轉帳'),('2','票據'),('3','現金')], string="收款方式")
    build_lessor_name = fields.Char(string="(出租人)姓名")
    lessor_pid = fields.Char(string="(出租人)身份證號")
    build_lessor = fields.Many2one('cloudrent.escrow_member', string="出租人")
    lessor_fin_instno = fields.Char(string="(出租人)金融機構代碼")
    lessor_fin_branch = fields.Char(string="(出租人)分行代碼")
    lessor_fin_name = fields.Char(string="(出租人)帳戶戶名")
    lessor_fin_account = fields.Char(string="(出租人)帳戶號碼")
    deposit_nmonth = fields.Integer(string="押金N月")
    deposit_value = fields.Integer(string="押金金額")
    escrow_nyear = fields.Integer(string="委託租賃N年")
    escrow_nmonth = fields.Integer(string="委託租賃N月")
    lessor_sex = fields.Selection([('1', '男'), ('2', '女')], string="出租人性別")
    lessor_phone1 = fields.Char(string="(出租人)電話1")
    lessor_phone2 = fields.Char(string="(出租人)電話2")
    lessor_cell = fields.Char(string="(出租人)手機")
    lessor_email = fields.Char(string="(出租人)EMail")
    lessor_addr = fields.Char(string="(出租人)戶籍地址")
    lessor_addr1 = fields.Char(string="(出租人)通訊地址")
    lessor_birthday = fields.Date(string="(出租人)出生日期")
    lessor_memo = fields.Text(string="(出租人)備註")

    # 屬帶看相關資訊
    lessee_line = fields.One2many('cloudrent.lessee_sitecheck','lessee_id',string="帶看客戶")

    # 屬收訂相關資訊
    lessee_deposit_line = fields.One2many('cloudrent.lessee_deposit_line','deposit_id',string="收訂資訊")

    # 屬簽約前相關資訊
    build_lessee = fields.Many2one('cloudrent.escrow_member', string="承租人")
    lessee_name = fields.Char(string="(承租人)姓名")
    lessee_fin_instno = fields.Char(string="(承租人)金融機構代碼")
    lessee_fin_branch = fields.Char(string="(承租人)分行代碼")
    lessee_fin_name = fields.Char(string="(承租人)帳戶戶名")
    lessee_fin_account = fields.Char(string="(承租人)帳戶號碼")
    lessee_pid = fields.Char(string="(承租人)身份證號")
    lessee_email = fields.Char(string="(承租人)EMail")
    lessee_birthday = fields.Date(string="(承租人)出生日期")
    lessee_addr1 = fields.Char(string="(承租人)戶籍地址")
    lessee_addr = fields.Char(string="(承租人)通訊地址")
    lessee_cell = fields.Char(string="(承租人)手機")


    # 簽約前相關資訊
    build_contract_rent = fields.Integer(string="簽約租金(元/月)")
    match_no = fields.Char(string="媒合編號")
    object_no = fields.Char(string="物件編號")
    object_no1 = fields.Many2one('cloudrent.build', string="物件編號")
    lessee_no = fields.Char(string="房客編號")

    lessee_no1 = fields.Many2one('cloudrent.escrow_member',string="房客編號")
    agent_man = fields.Many2one('cloudrent.escrow_member', string="委託負責人")
    management_man = fields.Many2one('cloudrent.escrow_member', string="管理人員")
    lessee_type = fields.Selection(LESSEETYPE,select=True, string="承租人身份類別")


    # 已轉成正式媒合合約
    is_trans_complete = fields.Boolean(string="已生成媒合合約",default=False)

    # escrow_build

    # entrust1
    entrust1_id = fields.Many2one('cloudrent.entrust_escrow_contract',string="社會住宅代租代管委託租賃契約書")
    entrust2_id = fields.Many2one('cloudrent.entrust_management_contract', string="社會住宅代租代管委託管理契約書")

    applyfor_version = fields.Many2one('cloudrent.contract_version', string="申請書版本期數")
    gen_doc_ids = fields.Many2many('cloudrent.doc_filename','cloudrent_crm_docfilename_rel','crm_id','doc_id',string="(申請書/契約書)篩選")
    gen_new_contract = fields.Boolean(string="重新產生契約書",default=False)

    @api.onchange('lessee_addr1')
    def onchangelesseeaddr1(self):
        if not self.lessee_addr:
            self.lessee_addr = self.lessee_addr1

    @api.onchange('lessor_addr1')
    def onchangelessoraddr1(self):
        if not self.lessor_addr:
            self.lessor_addr = self.lessor_addr1


    # cron job 5 minutes run
    def gen_contract_docx(self):
        myrec = self.env['crm.lead'].sudo().search([('gen_new_contract','=',True)])
        for rec in myrec:
            rec.run_docx_replace
            rec.update({'gen_new_contract': False})

    def action_cloudrent_applyfor_escrow1(self):
        # 出租人出租住宅申請書(代管)
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/crm_applyfor_escrow1/%s" % (bf_url, self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }

    def action_cloudrent_applyfor_escrow2(self):
        # 出租人出租住宅申請書(包租)
        bf_url = request.env['ir.config_parameter'].sudo().get_param('web.bf.url')
        url = "%s/report/odt_to_x/crm_applyfor_escrow2/%s" % (bf_url, self.id)
        return {'name': 'Go to website',
                'res_model': 'ir.actions.act_url',
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': url
                }


    def gen_escrow_lessee(self):     # 承租人數據建檔
        self.env.cr.commit()
        self.env.cr.execute("""select gen_member_lessee(%d)""" % self.id)
        mylesseeno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set build_lessee=%d where id=%d""" % (mylesseeno, self.id))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '承租人數據建檔產生完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def gen_escrow_lessor(self):     # 出租人數據建檔
        self.env.cr.commit()
        self.env.cr.execute("""select gen_member_lessor(%d)""" % self.id)
        mylessorno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set build_lessor=%d where id=%d""" % (mylessorno, self.id))
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '出租人數據建檔產生完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }


    def gen_escrow_build(self):      # 建立建物主檔數據
        self.env.cr.commit()
        self.env.cr.execute("""select gen_escrow_build(%d)""" % self.id)
        mybuildno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set object_no1=%d where id=%d""" % (mybuildno,self.id))
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_build_line_pic(%d)""" % self.id) # 必要物件照片記錄
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select gen_build_equip_part(%d)""" % self.id) # 建立建物傢俱清單
        self.env.cr.execute("""commit""")
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='建物主檔數據產生完成'
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

    def gen_entrust1_contract(self): # 社會住宅代租代管委託租賃契約書 [button]
        if not self.entrust1_id :
            A=1
        else :
            raise UserError("""已產生過 [社會住宅代租代管委託租賃契約書]單號：%s""" % self.entrust1_id.name)

    def gen_entrust2_contract(self): # 社會住宅代租代管委託管理契約書 [button]
        if not self.entrust2_id :
            A=1
        else :
            raise UserError("""已產生過 [社會住宅代租代管委託管理契約書]單號：%s""" % self.entrust2_id.name)

    def gen_entrust3_contract(self):
        A=1

    def cloudrent_lead_cancel(self):
        myrec = self.env['crm.stage'].search([('sequence','=',999)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='案件取消已完成'
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


    def cloudrent_lead1_action(self):
        myrec = self.env['crm.stage'].search([('sequence','=',20)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='場勘階段已完成'
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

    def cloudrent_lead2_action(self):
        myrec = self.env['crm.stage'].search([('sequence', '=', 30)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '申請書階段已完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }


    def cloudrent_lead3_action(self):
        myrec = self.env['crm.stage'].search([('sequence', '=', 40)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '招租階段已完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def cloudrent_lead4_action(self):
        myrec = self.env['crm.stage'].search([('sequence', '=', 50)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '帶看階段已完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def cloudrent_lead5_action(self):
        myrec = self.env['crm.stage'].search([('sequence', '=', 60)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '收訂階段已完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def cloudrent_lead6_action(self):
        myrec = self.env['crm.stage'].search([('sequence', '=', 70)])
        self.stage_id = myrec.id
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '預簽階段已完成'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

    def cloudrent_lead7_action(self):
        if not self.match_no:
            raise UserError("""媒合編號空白!""")
        if not self.object_no:
            raise UserError("""物件編號空白!""")
        if not self.lessee_no:
            raise UserError("""房客編號空白!""")
        # 彙整 建物基本資料
        self.env.cr.execute("""select gen_escrow_build(%d)""" % self.id)
        mybuildno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set object_no1=%d where id=%d""" % (mybuildno, self.id))
        self.env.cr.execute("""commit""")
        # 將租房設備清單 從 crm to build
        self.env.cr.execute("""select gen_ctob_equip_part(%d,%d)""" % (mybuildno,self.id))
        self.env.cr.execute("""commit""")
        # 彙整 出租人基本資料
        self.env.cr.execute("""select gen_member_lessor(%d)""" % self.id)
        mylessorno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set build_lessor=%d where id=%d""" % (mylessorno, self.id))
        self.env.cr.execute("""commit""")
        # 彙整 承租人基本資料
        self.env.cr.execute("""select gen_member_lessee(%d)""" % self.id)
        mylesseeno = self.env.cr.fetchone()[0]
        self.env.cr.execute("""update crm_lead set build_lessee=%d where id=%d""" % (mylesseeno, self.id))
        self.env.cr.execute("""commit""")

        # 產生 媒合契約主檔
        self.env.cr.execute("""select gen_contract_match(%d)""" % self.id)
        self.env.cr.execute("""commit""")

        # 產生 媒合契約的入住前家俱設備清單及狀態
        self.env.cr.execute("""select gen_match_equip_part(%d)""" % self.id)
        self.env.cr.execute("""commit""")


        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = '簽約階段已完成,系統將客戶資料轉成媒合合約'
        return {
            'name': 'Success',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

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
            mydocname = self.name + "_"+ mydocrec.name
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
                    self.env.cr.execute("""select gendocline(%d,%d)""" % (self.id,mydocid))
                    mydoclineid = self.env.cr.fetchone()[0]
                    mydocrec = self.env['cloudrent.lessor_doc_line'].sudo().search([('id','=',mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.name,'doc_file': b64encode(myout),'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
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
                    mydocrec = self.env['cloudrent.lessor_doc_line'].sudo().search([('id','=',mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.name,'doc_file': b64encode(myout),'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
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
                    mydocrec = self.env['cloudrent.lessor_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.name, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
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
                    mydocrec = self.env['cloudrent.lessor_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.name, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
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
                    mydocrec = self.env['cloudrent.lessor_doc_line'].sudo().search([('id', '=', mydoclineid)])
                    mydocrec.sudo().update({'doc_desc': self.name, 'doc_file': b64encode(myout), 'doc_filename': mydocname,'create_uid':self.env.user.id,'doc_date':fields.Date.today()})
                    mydocrec.env.cr.commit()
                    os.remove(docxnewname)



class CloudRentLessorDocLine(models.Model):
    _name = "cloudrent.lessor_doc_line"
    _description = "雲房招租前申請書"
    _order = "doc_name"

    doc_id = fields.Many2one('crm.lead',ondelete='cascade')
    doc_date = fields.Date(string="存檔日期",default=lambda self:fields.Date.today())
    doc_name = fields.Many2one('cloudrent.doc_filename',string="表單名稱",required=True)
    doc_desc = fields.Char(string="說明")
    doc_file = fields.Binary(string="系統樣板",attachment=False)
    doc_file1 = fields.Binary(string="用印完上傳",attachment=False)
    doc_applyfor_id = fields.Integer(string="申請書ID")
    doc_filename = fields.Char(string="檔名")
    doc_filename1 = fields.Char(string="檔名1")

class CloudRentLesseeSiteCheck(models.Model):
    _name = "cloudrent.lessee_sitecheck"
    _description = "雲房帶看客人資訊"

    lessee_id = fields.Many2one('crm.lead',ondelete='cascade')
    lessee_date = fields.Date(string='帶看日期')
    lessee_name = fields.Char(string="姓名")
    lessee_pid = fields.Char(string="身份證號")
    lessee_sex = fields.Selection([('1','男'),('2','女')],string="性別")
    lessee_age = fields.Integer(string="年齡")
    lessee_phone1 = fields.Char(string="電話1")
    lessee_phone2 = fields.Char(string="電話2")
    lessee_cell = fields.Char(string='手機')
    lessee_email = fields.Char(string="EMail")
    build_pattern = fields.Selection([('1', '套房'), ('2', '一房'), ('3', '二房'), ('4', '三房以上')], string="期望房型")
    elevator = fields.Boolean(string="需電梯?",default=False)
    lessee_expected_value = fields.Integer(string="期望租金(下限)")
    lessee_expected_value1 = fields.Integer(string="期望租金(上限)")
    build_area = fields.Char(string="期望區域")
    pet = fields.Boolean(string="養寵物?",default=False)
    worship_god = fields.Boolean(string="拜神?",default=False)
    member_number = fields.Integer(string="同住人數")
    lessee_memo = fields.Text(string="備註")
    rent_success = fields.Boolean(string="確認承租",default=False)

class CloudRentLesseeDepositLine(models.Model):
    _name = "cloudrent.lessee_deposit_line"
    _description = "承租人收訂資訊"

    deposit_id = fields.Many2one('crm.lead',ondelete='cascade')
    deposit_name = fields.Char(string="承租人姓名")
    deposit_date = fields.Date(string="收訂日期")
    deposit_value = fields.Integer(string="金額")
    deposit_desc = fields.Text(string="備註")
    deposit_file = fields.Binary(string="夾檔",attachment=False)
    deposit_filename = fields.Char(string="檔名")

class CloudRentSiteCheckPicLine(models.Model):
    _name = "cloudrent.sitecheck_pic_line"
    _description = "場勘現場拍照圖檔"
    _order = "sequence"

    sitecheck_id = fields.Many2one('crm.lead',ondelete='cascade')
    sequence = fields.Integer(string="序")
    sitecheck_type = fields.Selection([('1', '必要'), ('2', '非必要')], string="類型", default='1')
    sitecheck_desc = fields.Char(string="項目")
    sitecheck_pic = fields.Binary(string="照片1",attachment=False)
    sitecheck_pic1 = fields.Binary(string="照片2",attachment=False)
    sitecheck_pic2 = fields.Binary(string="照片3",attachment=False)



class CloudRentCrmLeadEquipPart(models.Model):
    _name = "cloudrent.crm_lead_equip_part"
    _description = "場勘租屋家俱設備清單"

    equip_id = fields.Many2one('crm.lead', ondelete='cascade')
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


