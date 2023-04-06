# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class genbomwizard(models.TransientModel):
    _name = "alldo_acme_iot.genbom_wizard"
    _description = "自動生成產品BOM精靈"

    passcode = fields.Char(string="PASSCODE：")

    def auto_gen_bom(self):
        if self.passcode != '!99999ibm':
            raise UserError("請輸入正確的passcode！")
        myrec = self.env['product.template'].search([('blank_weight','>',0)])
        mybomrec = self.env['mrp.bom']
        for rec in myrec:
            mycount = self.env['mrp.bom'].search_count([('product_tmpl_id','=',rec.id)])
            if mycount == 0 :   # BOM 未建檔
                mybomrec.create({'product_tmpl_id':rec.id,'product_qty':1,'product_uom_id':1,'type':'normal','consumption':'strict'})
