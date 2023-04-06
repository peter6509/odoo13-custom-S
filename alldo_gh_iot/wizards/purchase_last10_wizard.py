# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class PurchaseLast10Wizard(models.TransientModel):
    _name = "alldo_gh_iot.purchase_last10_wizard"

    product_id = fields.Many2one('product.product',string="料號")

    def run_purchase_last10(self):
        self.env.cr.execute("""select genpurchaselast10(%d)""" % self.product_id.id)
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_gh_iot.view_purchase_last10_tree')
        return {
            'view_name': '最近採購單價清單',
            'name': ('最近採購單價清單'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.purchase_last10_list',
            'view_id': myviewid.id,
            'flags': {'action_buttons': False},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'new'}
