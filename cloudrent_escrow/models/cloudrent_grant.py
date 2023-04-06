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

LESSEETYPE = [
    ('1','一般戶'),
    ('2','第一類弱勢戶'),
    ('3','第二類弱勢戶'),
    ('4','就學,就業,警消'),
    ('5','300億方案')]
GRANTFREQ=[('1','By件'),
           ('2','By月'),
           ('3','By年')]


class CloudRentGrant(models.Model):
    _name = "cloudrent.grant_item"
    _description = "補助項目名稱"
    _order = "grant_code"

    grant_code = fields.Char(string="補助代碼")
    grant_name = fields.Char(string="補助名稱")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.grant_code, myrec.grant_name)
            result.append((myrec.id, myname))
        return result


class CloudRentGrantFee(models.Model):
    _name = "cloudrent.grant_fee"
    _description = "市政府補助項目金額上限表"
    _order = "grant_item"

    grant_item = fields.Many2one('cloudrent.grant_item',string="補助名稱",required=True)
    lessor_type = fields.Selection(CASETYPE,select=True,string="媒合類別")
    lessee_type = fields.Selection(LESSEETYPE,select=True,string="承租人類別")
    admin_area = fields.Selection(ADMINAREA,select=True,string="所屬行政區")
    grant_freq = fields.Selection(GRANTFREQ,select=True,string="頻率")
    grant_time = fields.Integer(string="次數",required=True)
    discount_rate = fields.Float(digits=(5, 3), string="補助比率",default=0.000)
    grant_max_value = fields.Integer(string="補助上限",required=True)


    def name_get(self):
        result = []
        for myrec in self:
            if myrec.admin_area:
               myname = "[%s]%s" % (myrec.admin_area, myrec.grant_item.grant_name)
            else:
               myname = "%s" % myrec.grant_item.grant_name
            result.append((myrec.id, myname))
        return result
