# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotprodstockwizard(models.TransientModel):
    _name ="alldo_ipla_iot.prodstock_wizard"

    product_no = fields.Many2one('product.product',string="產品")

    def run_prod_stock(self):
        if not self.product_no:
            myprodid = 0
        else:
            myprodid = self.product_no.id
        self.env.cr.execute("""select genprodstock(%d)""" % myprodid)
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_ipla_iot.ipla_iot_prodstock_tree')
        return {
            'view_name': 'prod_stock_list',
            'name': (u'產品庫存查詢'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_ipla_iot.prod_stock_list',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}