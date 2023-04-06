# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError

class newebcontractinherit4(models.Model):
    _inherit = "neweb_contract.contract.line"
    _order = "sequence"

    conline_item = fields.Integer(string="項次",default=1)



# class newebcontractinherit4(models.Model):
#     _inherit = "neweb_contract.contract"

    # @api.multi
    # def write(self, vals):
    #
    #     res = super(newebcontractinherit4, self).write(vals)
    #     self.env.cr.execute("""select updateconlineitem(%d)""" % self.id)
    #     return res