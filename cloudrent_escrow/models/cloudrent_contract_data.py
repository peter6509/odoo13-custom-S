# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentContractData(models.Model):
    _name = "cloudrent.contract_data"
    _description = "社會住宅管理契約書"

    name = fields.Char(string="契約書名稱",required=True)
    contract_tag = fields.Integer(string="TAGS")
    active = fields.Boolean(string="ACTIVE",default=True)

    @api.model
    def create(self, vals):
        mycount = self.env['cloudrent.contract_data'].search_count([('name','=',vals['name'])])
        if mycount > 0 :
            raise UserError("""契約書名稱已重複""")
        res = super(CloudRentContractData, self).create(vals)

        return res
