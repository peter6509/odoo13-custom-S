        # -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
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

class CloudRentBuild(models.Model):
    _name = "cloudrent.build"
    _description = "包租代管物件基本資料"

    @api.depends('build_createdate')
    def _get_buildage(self):
        for rec in self:
            if rec.build_createdate == False:
                rec.build_age = 0
            else:
                self.env.cr.execute("""select getbuildage('%s')""" % rec.build_createdate)
                rec.build_age = self.ev.cr.fetchone()[0]

    @api.depends('build_area1')
    def _get_buildarea(self):
        for rec in self:
            if not rec.build_area1 or rec.build_area1 == 0:
                rec.build_area = 0.0
            else:
                rec.build_area = round((rec.build_area1 * 0.3025), 2)

    @api.depends('build_for_rent')
    def _get_guarantee_fee(self):
        for rec in self:
            if not rec.build_for_rent or rec.build_for_rent == 0:
                rec.guarantee_fee = 0
            else:
                rec.guarantee_fee = round((rec.build_for_rent * 0.8),0)

    @api.depends('build_for_rent')
    def _get_escrow_fee(self):
        for rec in self:
            if not rec.build_for_rent or rec.build_for_rent == 0:
                rec.escrow_fee = 0
            else:
                rec.escrow_fee = round((rec.build_for_rent * 0.9),0)

    object_no = fields.Char(string="物件編號")
    escrow_agent = fields.Many2one('cloudrent.escrow',string="代管業者")
    case_type = fields.Selection(CASETYPE,select=True, string="案件類型")
    admin_area = fields.Selection(ADMINAREA,select=True,string="所屬行政區")
    build_sec = fields.Char(string="段")
    build_msec = fields.Char(string="小段")
    build_loc = fields.Char(string="地區")
    build_community = fields.Char(string="社區")
    build_number = fields.Char(string="建號")
    house_number = fields.Char(string="建物門牌")
    place_number = fields.Char(string="建物坐落地號")
    parking_space = fields.Boolean(string="車位")
    ancillary_equipment = fields.Boolean(string="附屬設備")
    build_rent_situation = fields.Selection(RENTSITUATION,select=True,string="租賃住宅現況")
    rent_man = fields.Char(string="現承租人")  # build_rent_situation='3'
    rent_duedate = fields.Date(string="租期屆滿日")  # build_rent_situation='3'
    rent_other_desc = fields.Char(string="其他說明")  # build_rent_situation='4'
    entrust_start_date = fields.Date(string="委託租賃起始日")
    entrust_end_date = fields.Date(string="委託租賃截止日")
    build_createdate = fields.Date(string="建築完成日期")
    build_age = fields.Integer(string="屋齡", store=True,compute=_get_buildage)
    build_area = fields.Float(digits=(10, 2),store=True,string="坪數", compute=_get_buildarea)
    guarantee_fee = fields.Float(digits=(8,0),string="包租包管租金",store=True,compute=_get_guarantee_fee)
    escrow_fee = fields.Float(digits=(8,0),string="代租代管租金",store=True,compute=_get_escrow_fee)
    build_area1 = fields.Float(digits=(8, 0), string="平方公尺")
    build_for_rent = fields.Integer(string="待租租金(元/月)")
    general_build = fields.Selection([('1', '透天厝'), ('2', '別墅')], string="一般建物")
    build_type = fields.Selection(BUILDTYPE,select=True, string="區分所有建物")
    build_pattern = fields.Selection(BUILDPATTERN,select=True, string="格局")
    build_pattern1 = fields.Char(string="格局")
    build_lessor = fields.Many2one('cloudrent.escrow_member', string="出租人")
    build_elevator = fields.Boolean(string="有電梯?", default=False)
    build_pet = fields.Boolean(string="養寵物?", default=False)
    build_line = fields.One2many('cloudrent.build_line','build_id',string="物件照片")
    build_equip_part = fields.One2many('cloudrent.build_equip_part','equip_id',string="傢俱清單")
    is_rent = fields.Boolean(string="目前已出租",default=False)
    leadid = fields.Many2one('crm.lead',string="商機來源")
    build_repair_line = fields.One2many('cloudrent.build_repair_line','repair_id',string="修繕記錄")

    def name_get(self):
        result = []
        for myrec in self:
            if myrec.build_lessor:
                mylessor = myrec.build_lessor.escrow_man
            else:
                mylessor = ' '

            if myrec.build_type=='1':
                mybtype = '公寓'
            elif myrec.build_type=='2':
                mybtype = '華廈'
            else :
                mybtype = '電梯大樓'

            if myrec.build_pattern=='1':
                mypattern = '套房'
            elif myrec.build_pattern=='2':
                mypattern = '一房'
            elif myrec.build_pattern=='3':
                mypattern = '二房'
            else:
                mypattern = '三房以上'

            mybuild = mybtype + '-' + mypattern
            myname = "[%s]%s" % (myrec.object_no, mylessor)
            result.append((myrec.id, myname))
        return result



class CloudRentBuildLine(models.Model):
    _name = "cloudrent.build_line"
    _description = "包租代管場勘物件照片明細"

    build_id = fields.Many2one('cloudrent.build',ondelete='cascade')
    sequence = fields.Integer(string="序")
    pic_type = fields.Selection([('1','必要'),('2','非必要')],string="類型",default='1')
    build_desc = fields.Char(string="項目")
    build_pic = fields.Binary(string="照片1",attachment=False)
    build_pic1 = fields.Binary(string="照片2",attachment=False)
    build_pic2 = fields.Binary(string="照片3",attachment=False)
    originid = fields.Integer(string="來源ID")




class CloudRentBuildEquipPart(models.Model):
    _name = "cloudrent.build_equip_part"
    _description = "租屋家俱設備清單"

    equip_id = fields.Many2one('cloudrent.build',ondelete='cascade')
    equip_categ = fields.Selection(EQUIPCATEG,select=True, string="設備分類", required=True)
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


class CloudRentBuildRepairLine(models.Model):
    _name = "cloudrent.build_repair_line"
    _description = "年度修繕補助申請記錄"
    _order = "repair_date desc"

    repair_id = fields.Many2one('cloudrent.build',ondelete='cascade')
    repair_year = fields.Char(string="年度")
    repair_date = fields.Date(string="修繕日期")
    repair_desc = fields.Char(string="修繕內容")
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號")
    repair_vendor = fields.Many2one('res.partner',string="廠商")
    repair_fee = fields.Integer(string="修繕金額")

