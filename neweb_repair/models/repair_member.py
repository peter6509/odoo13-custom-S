# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebrepairmember(models.Model):
    _name = "neweb_repair.mail_member"

    name = fields.Char(string="說明")
    repair_member = fields.Many2many('hr.employee','neweb_repair_mail_member_rel','rid','eid',string="報修額外通知信名單")
    outsource_member = fields.Many2many('hr.employee','neweb_repair_outsource_mail_member_rel','rid','eid',string="維運客戶報修額外通知信名單")

    @api.model
    def create(self, vals):
        myres = self.env['neweb_repair.mail_member'].search_count([])
        if myres >= 1 :
            raise UserError("只能編輯一筆資料")
        vals['name']='Default Member Send Mail'
        res = super(newebrepairmember, self).create(vals)
        return res
