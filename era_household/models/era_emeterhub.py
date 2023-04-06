# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class EraEmeterHub(models.Model):
    _name = "era.emeterhub_status"

    pi_id = fields.Char(string="PI數據收集器名稱")
    last_update = fields.Datetime(string="最後異動時間")
    ip_address = fields.Char(string="PI IP位址")
    emeter_line = fields.One2many('era.emeter_status','emeter_id1',string="電錶明細記錄")

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s](IP:%s)" % (myrec.pi_id, myrec.ip_address)
            result.append((myrec.id, myname))
        return result



class EraEmeterDevice(models.Model):
    _name = "era.emeter_status"

    emeter_id1 = fields.Many2one('era.emeterhub_status',ondelete='cascade')
    emeter_id = fields.Many2one('era.household_electric_meter',string="電錶")
    last_update = fields.Datetime(string="最後異動時間")
    emeter_status = fields.Char(string="電錶狀態")
    ng_count = fields.Integer(string="NG累計次數")

