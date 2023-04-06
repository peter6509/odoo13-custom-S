# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class resusersinherit(models.Model):
    _inherit = "res.users"

    house_id = fields.Many2one('cloudrent.household_house',string="房號")
    member_id = fields.Many2one('cloudrent.household_member',string="租戶")
    landlord_id = fields.Many2one('cloudrent.household_member', string="房東")
    agent_id = fields.Many2one('cloudrent.household_member', string="代管業務")
    household_group = fields.Selection([('1', '房客群組'), ('2', '房東群組'), ('3', '代管群組'), ('4', '系統管理群組')], string="使用者類型")

