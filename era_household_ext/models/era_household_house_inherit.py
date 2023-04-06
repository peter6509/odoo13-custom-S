# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ERAHouseholdHouseInherit(models.Model):
    _inherit = "era.household_house"

    landlord_user1 = fields.Many2one('res.users',string="房東U1")
    landlord_user2 = fields.Many2one('res.users',string="房東U2")
    manage_user1 = fields.Many2one('res.users',string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")
    case_code = fields.Char(string="案場代號")
    rent_convention = fields.Binary(string="住戶公約")


class erahouseholdhouselineInherit(models.Model):
    _inherit = "era.household_house_line"

    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")

class alldoerahouseholdInherit(models.Model):
    _inherit = "era.household_member"

    landlord_user1 = fields.Many2one('res.users', string="房東U1")
    landlord_user2 = fields.Many2one('res.users', string="房東U2")
    manage_user1 = fields.Many2one('res.users', string="代管U1")
    manage_user2 = fields.Many2one('res.users', string="代管U2")
    manage_user3 = fields.Many2one('res.users', string="代管U3")




