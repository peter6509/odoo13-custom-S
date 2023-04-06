# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class CloudRentEntrustEscrowContract(models.Model):
    _name = "cloudrent.entrust_escrow_contract"
    _decription = "社會住宅代租代管委託租賃契約書(entrust1)"
    _order = "entrust_applyfor_date desc"

    @api.depends('build_area')
    def _get_buildarea1(self):
        for rec in self:
            if not rec.build_area or rec.build_area == 0:
                rec.build_area1 = 0.0
            else:
                rec.build_area1 = round((rec.build_area / 0.3025), 2)

    name = fields.Char(string="契約書單號",default="New",copy=False)
    escrow_no = fields.Many2one('cloudrent.escrow', string="歸屬代管業者",required=True)
    build_no = fields.Many2one('cloudrent.build',string="物件編號",required=True)
    build_number = fields.Char(string="建號")
    house_number = fields.Char(string="建物門牌")
    place_number = fields.Char(string="建物坐落地號")
    parking_space = fields.Boolean(string="車位")
    ancillary_equipment = fields.Boolean(string="附屬設備")
    build_rent_situation = fields.Selection([('1', '所有權人自行使用'), ('2', '空屋無人使用'), ('3', '現有人承租'), ('4', '其他')],string="租賃住宅現況")
    rent_man = fields.Char(string="現承租人")  # build_rent_situation='3'
    rent_duedate = fields.Date(string="租期屆滿日")  # build_rent_situation='3'
    rent_other_desc = fields.Char(string="其他說明")  # build_rent_situation='4'
    entrust_start_date = fields.Date(string="委託租賃起始日")
    entrust_end_date = fields.Date(string="委託租賃截止日")
    build_for_rent = fields.Integer(string="待租租金(元/月)")
    rent_paytype = fields.Selection([('1', '轉帳'), ('2', '票據'), ('3', '現金')], string="收款方式")
    deposit_nmonth = fields.Integer(string="押金N月")
    escrow_nyear = fields.Integer(string="委託租賃N年")
    escrow_nmonth = fields.Integer(string="委託租賃N月")
    build_lessor_name = fields.Char(string="出租人姓名")
    lessor_pid = fields.Char(string="出租人身份證號")
    build_lessor = fields.Many2one('cloudrent.escrow_member', string="出租人")
    lessor_fin_instno = fields.Char(string="(出租人)金融機構代碼")
    lessor_fin_branch = fields.Char(string="(出租人)分行代碼")
    lessor_fin_account = fields.Char(string="(出租人)帳戶號碼")
    agent_man = fields.Many2one('cloudrent.escrow_member',string="委託負責人")
    entrust_applyfor_date = fields.Date(string="申請日期")
    build_area = fields.Integer(string="坪數")
    build_area1 = fields.Float(digits=(8, 2), string="平方公尺", compute=_get_buildarea1)
    real_estate_broker = fields.Many2one('cloudrent.escrow_member',string="不動產經紀人")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            self.env.cr.execute("""select get_cloudrent_seqno(%d,'%s')""" % (vals['escrow_no'],'C1'))
            vals['name'] = self.env.cr.fetchone()[0]
        res = super(CloudRentEntrustEscrowContract, self).create(vals)
        return res

    @api.onchange('entrust_start_date','entrust_end_date')
    def onchangeentrustdate(self):
        if not self.entrust_start_date and not self.entrust_end_date:
           self.env.cr.execute("""select entrust_year('%s','%s')""")
           self.escrow_nyear = self.env.cr.fetchone()[0]
           self.env.cr.execute("""select entrust_month('%s','%s')""")
           self.escrow_nmonth = self.env.cr.fetchone()[0]
        else:
           self.escrow_nyear = 0
           self.escrow_nmonth = 0
