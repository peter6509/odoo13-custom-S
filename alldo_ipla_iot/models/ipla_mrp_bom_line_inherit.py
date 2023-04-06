# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplamrpbominherit(models.Model):
    _inherit = "mrp.bom"

    packaging_line = fields.One2many('alldo_ipla_iot.packaging_line','bom_id',string="包材用量",copy=False)

    @api.model
    def create(self, vals):

        res = super(iplamrpbominherit, self).create(vals)
        self.env.cr.execute("""select getfurnaceqty(%d)""" % res.id)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):

        res = super(iplamrpbominherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select getfurnaceqty(%d)""" % rec.id)
            self.env.cr.execute("""commit""")
        return res


class iplamrpbomlineinherit1(models.Model):
    _name = "alldo_ipla_iot.packaging_line"
    _description = "包材用量"

    bom_id = fields.Many2one('mrp.bom',ondelete='cascade')
    product_id = fields.Many2one('product.product',string="包材料號")
    product_uom_id = fields.Many2one('uom.uom',string="單位")
    m_set_qty = fields.Float(digits=(10,2),string="每箱產品數")
    c_set_qty = fields.Float(digits=(10,2),string="每箱包材數")



