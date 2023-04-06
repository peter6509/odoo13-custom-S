# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
QUITTYPE=[('1','租賃期滿契約終止'),
          ('2','租賃住宅未合於居住使用，並有修繕之必要，經承租人(包租業)催告仍不於期限內修繕'),
          ('3','租賃住宅因不可歸責承租人(包租業)之事由致一部滅失，且其存餘部分不能達租賃之目的'),
          ('4','承租人因疾病、意外產生有長期療養之需要'),
          ('5','因第三人就租賃住宅主張其權利，致承租人不能為約定之居住使用'),
          ('6','原出租人為重新建築而必須收回'),
          ('7','承租人遲付租金之總額達二個月之金額，經相當期限催告，仍不為支付'),
          ('8','承租人積欠管理費或其他應負擔之費用達相當二個月之租金額，經相當期限催告，仍不為支付'),
          ('9','承租人違法使用、存放有爆炸性或易燃性物品，經勸告仍繼續為之'),
          ('10','其他〔請填寫原因說明]')]
EQUIPCATEG=[('1','家電類'),
            ('2','家具類'),
            ('3','鑰匙類'),
            ('4','其他')]

class CloudRentQuitLease(models.Model):
    _name = "cloudrent.quit_lease"
    _description = "退租點交記錄"

    escrow_no = fields.Many2one('cloudrent.escrow',string="業者",default=lambda self:self.env.user.escrow_no.id,required=True)
    match_no = fields.Many2one('cloudrent.contract_match',string="媒合編號",required=True)
    member_no = fields.Many2one('cloudrent.escrow_member',string="負責人員",default=lambda self:self.env.user.escrow_member.id,required=True)
    lessor_no = fields.Many2one('cloudrent.escrow_member',string="出租人")
    lessor_cell = fields.Char(string="出租人手機")
    lessee_no = fields.Many2one('cloudrent.escrow_member',string="承租人")
    lessee_cell = fields.Char(string="承租人手機")
    is_notice1 = fields.Boolean(string="已告知房東?",default=False)
    notice1_date = fields.Date(string="告知日期")
    is_notice2 = fields.Boolean(string="清點傢俱設備?",default=False)
    notice2_date = fields.Date(string="清點日期")
    is_notice3 = fields.Boolean(string="整理,清潔?",default=False)
    notice3_date = fields.Date(string="清潔日期")
    is_notice4 = fields.Boolean(string="當面點交確認?",default=False)
    notice4_date = fields.Date(string="點交日期")
    quit_date = fields.Date(string="租約終止日",required=True)
    quit_year = fields.Char(string="年")
    quit_month = fields.Char(string="月")
    quit_type = fields.Selection(QUITTYPE,select=True,string="契約終止模式",required=True)
    memo = fields.Text(string="其他說明")
    equip_part_line = fields.One2many('cloudrent.quit_equip_part','equip_id',copy=False)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.match_no.match_no, myrec.match_no.object_no)
            result.append((myrec.id, myname))
        return result

    @api.onchange('escrow_no')
    def onchangeescrowno(self):
        self.env.cr.execute("""select getonlinematch()""")
        myrec = self.env.cr.fetchall()
        myids=[]
        for rec in myrec:
            myids.append(rec[0])
        return {'domain': {'match_no': [('id', 'in', myids)]}}


    @api.onchange('match_no')
    def onchangematchno(self):
        self.lessor_no = self.match_no.build_lessor.id
        self.lessee_no = self.match_no.build_lessee.id
        self.lessor_cell = self.match_no.lessor_cell
        self.lessee_cell = self.match_no.lessee_cell


class CloudRentQuitEquipPart(models.Model):
    _name = "cloudrent.quit_equip_part"
    _description = "退租點交家俱設備狀態明細"

    equip_id = fields.Many2one('cloudrent.quit_lease', ondelete='cascade')
    equip_categ = fields.Selection(EQUIPCATEG,select=True,string="設備分類",required=True)
    equip_no = fields.Many2one('cloudrent.equip_part', string="設備名稱", required=True)
    equip_qty = fields.Integer(string="入租前數量")
    equip_qty1 = fields.Integer(string="退租點交數量")
    equip_status = fields.Char(string="入租前設備狀態")
    equip_status1 = fields.Char(string="退租點交設備狀態")
    equip_image1 = fields.Binary(string='入租前照片1',attachment=False)
    equip_image2 = fields.Binary(string="入租前照片2",attachment=False)
    equip_image3 = fields.Binary(string="入租前照片3",attachment=False)
    quit_image1 = fields.Binary(string='退租點交照片1',attachment=False)
    quit_image2 = fields.Binary(string="退租點交照片2",attachment=False)
    quit_image3 = fields.Binary(string="退租點交照片3",attachment=False)