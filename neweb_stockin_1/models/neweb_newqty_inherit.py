# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api



class newqty_inherit(models.TransientModel):
    _inherit ="stock.change.product.qty"

    location_id = fields.Many2one('stock.location', 'Location', required=True, domain="[('usage', '=', 'internal')]",track_visibility='always')
    old_quantity = fields.Float(digits=(10,0),readonly=True)
    

    @api.onchange('product_id','location_id')
    def onchange_client(self):
        if self.product_id and self.location_id :
           self.env.cr.execute("select getstockquantqty(%d,%d)" % (self.product_id.id,self.location_id.id))
           myqty = self.env.cr.fetchone()
           mynewqty = myqty[0]
           self.old_quantity = mynewqty







