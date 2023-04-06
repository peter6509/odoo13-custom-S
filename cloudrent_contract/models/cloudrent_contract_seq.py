# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class cloudrentContractSeq(models.Model):
    _name = "cloudrent.contract_seq"
    _description = "合約流水編號"

    name = fields.Char(string="Contract code")
    seq = fields.Integer(string="Sequence",default=0)

    @api.model
    def create(self, vals):
        mycount = self.env['cloudrent.contract_seq'].search_count([('name','=',vals['name'])])
        if mycount > 0 :
            raise UserError("合約前綴碼已重複")
        res = super(cloudrentContractSeq, self).create(vals)
        return res

