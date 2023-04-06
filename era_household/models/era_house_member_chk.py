# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class EraHouseMemberCHK(models.Model):
    _name = "era.house_member_chk"

    house_id = fields.Many2one('era.household_house_line',string="租房")
    member_id = fields.Many2one('era.household_member',string="租戶")