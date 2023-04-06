# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class powkorderlistwizard(models.TransientModel):
    _name = "alldo_gh_iot.powkorder_list_wizard"

    product_no = fields.Many2one('product.product',string="料號")

    def run_powkorder_list(self):
        self.env.cr.execute("""select genpowkorderlist(%d)""" % self.product_no.id)
        self.env.cr.execute("""commit""")

        # myid = self.env['alldo_gh_iot.powkorder_list'].search([])
        # if not myid:
        #     raise UserError(u"沒有產品訂單項目,請確認")
        myviewid = self.env.ref('alldo_gh_iot.po_wkorder_list_tree').id


        return {
            # 'domain': [('id', 'in', list(new_invoice.values()))],
            'name': 'Similar Detail Tree View',
            'view_mode': 'tree,form',
            'res_model': 'alldo_gh_iot.powkorder_list',
            'view_id': False,
            'views': [(self.env.ref('alldo_gh_iot.po_wkorder_list_tree').id, 'tree'),(self.env.ref('alldo_gh_iot.po_wkorder_list_form').id, 'form')],
            # 'context': "{'type':'out_invoice'}",
            'type': 'ir.actions.act_window'
        }
