# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError


class ERAHouseholdMemberInherit(models.Model):
    _inherit = "era.household_member"

    line_user_ids = fields.One2many('era.member_line_user', 'member_id', copy=False)
    contract_id = fields.Many2one('era.contract',string="合約編號")
    rent_convention = fields.Binary(related="house_id.house_id.rent_convention", string="租戶公約")


class ERAMemberLineUser(models.Model):
    _name = "era.member_line_user"
    _description = "LINE APP綁定記錄"

    member_id = fields.Many2one('era.household_member',ondelete='cascade')
    line_user_id = fields.Char(string='Line User ID')
    line_rich_menu_id = fields.Char(string='Line Rich menu ID')
    member_pid = fields.Char(string="身份字號")
    member_name = fields.Char(string="姓名")
    send_acc_bill = fields.Boolean(string="發送帳單?",default=True)
    send_announcement = fields.Boolean(string="發送公告訊息?",default=True)
    send_bus_adv = fields.Boolean(string="發送廣告訊息?",default=False)
    active = fields.Boolean(string="生效",default=True)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.member_pid, myrec.member_name)
            result.append((myrec.id, myname))
        return result








