# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ProductCategoryInherit(models.Model):
    _inherit = "product.category"

    active = fields.Boolean(string="ARCH",default=True)

    @api.model
    def create(self,vals):
        mycount = self.env['product.category'].search_count([('name','=',vals['name'])])
        if mycount > 0:
            raise UserError("產品分類已重複！")
        res = super(ProductCategoryInherit, self).create(vals)
        return res
