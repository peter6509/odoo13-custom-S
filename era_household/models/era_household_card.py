# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class erahouseholdcard(models.Model):
    _name = "era.household_card"
    _description = "ERA房卡明細檔"

    card_no = fields.Char(string="卡號")
    active = fields.Boolean(string="啟用？",default=True)
    used_date = fields.Date(string="啟用日期")
    in_used = fields.Boolean(string="配發？",default=False)


class erabillconfig(models.Model):
    _name = "era.household_config"
    _description = "ERA 對帳參數設定"

    bill_ym = fields.Char(string="對帳年月",required=True,size=7)
    price_unit = fields.Float(digits=(5,1),string="一度電單價",required=True)
    payment_bank = fields.Char(string="電匯銀行")
    payment_account = fields.Char(string="電匯帳號")

    @api.model
    def create(self, vals):
        mycount = self.env['era.household_config'].search_count([])
        if mycount > 1:
            raise UserError("只能存在一筆記錄")
        res = super(erabillconfig, self).create(vals)

        return res

    # 每日執行一次
    def run_household_config(self):
        self.env.cr.execute("""select genmeterinused()""")
        self.env.cr.execute("""commit""")
        self.env.cr.execute("""select checkconfig()""")
        self.env.cr.execute("""commit""")

    # 每小時執行一次
    def run_household_scale(self):
        self.env.cr.execute("""select runemeterscale()""")
        self.env.cr.execute("""commit""")

    # 每小時執行一次
    def run_member_lineinfo(self):
        self.env.cr.execute("""select checkconfig()""")
        self._cr.execute("""commit""")
        self._cr.execute("""select genmemberlineinfo()""")
        self._cr.execute("""commit""")

    def run_pi_id(self):
        myrec =self.env['era.household_electric_meter'].search([])
        for rec in myrec:
            piid = rec.ig8000_id
            modbus10id = str(int(rec.modbus_id,16))
            rec.write({'pi_id':piid,'modbus10_id':modbus10id})


