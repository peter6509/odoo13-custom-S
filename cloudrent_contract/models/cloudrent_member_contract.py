# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentMemberContract(models.Model):
    _inherit = "cloudrent.household_member"

    contract_line = fields.One2many('cloudrent.member_contract','member_id',copy=False)


class cloudrentMemberContractLine(models.Model):
    _name = 'cloudrent.member_contract'
    _description = "租戶合約記錄明細"


    member_id = fields.Many2one('cloudrent.household_member',ondelete='cascade')
    contract_id = fields.Many2one('cloudrent.contract',string="租屋合約")
    start_rental = fields.Date(string="合約啟始日期")
    end_rental = fields.Date(string="合約截止日期")
    contract_status = fields.Selection([('1','生效'),('2','失效')],string="狀態")

