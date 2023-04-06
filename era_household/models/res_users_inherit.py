# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class resusersinherit(models.Model):
    _inherit = "res.users"

    house_id = fields.Many2one('era.household_house',string="房號")
    member_id = fields.Many2one('era.household_member',string="租戶")

    # def write(self, vals):
    #     res = super(resusersinherit, self).write(vals)
    #     for rec in self:
    #         self.env.cr.execute("""select genusermember(%d)""" % rec.id)
    #         self.env.cr.execute("""commit""")
    #     return res
