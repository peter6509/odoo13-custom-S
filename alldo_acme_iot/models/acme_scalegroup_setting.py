# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmescalegroupsetting(models.Model):
    _name = "alldo_acme_iot.scalegroup_setting"
    _description = "電子磅秤投料分析料號設定"
    _order = "sequence,item_seq"

    sequence = fields.Integer(string="SEQ",default=20)
    product_no = fields.Many2one('product.product',string="投料樞紐分析料號")
    product_gpid = fields.Integer(string="群組編號")
    item_seq = fields.Integer(string="順序")


    @api.model
    def create(self, vals):
        myprod = vals['product_no']
        mycount = self.env['alldo_acme_iot.scalegroup_setting'].search_count([('product_no','=',myprod)])
        if mycount > 0 :
            raise UserError("料號重複了！")
        res = super(acmescalegroupsetting, self).create(vals)

        return res
