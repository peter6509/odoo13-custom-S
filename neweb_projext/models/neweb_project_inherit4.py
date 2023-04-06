# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class projcusaddress(models.Model):
    _inherit = "neweb.project"

    revenue_ratio = fields.Float(digits=(4,2),string="新約認列比率",default=0.4)


    # @api.model
    #     # def create(self, vals):
    #     #     res = super(projcusaddress, self).create(vals)
    #     #     self.env.cr.execute("""select check_cus_address(%d)""" % res.id)
    #     #     self.env.cr.execute("""commit""")
    #     #     return res