# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class GHSupplierinfoWizard(models.TransientModel):
    _name = "alldo_gh_iot.supplierinfo_wizard"

    supplier_id = fields.Many2one('res.partner',string="供應商")
    product_id = fields.Many2one('product.product',string="料號")

    def run_supplierinfo(self):
        if not self.supplier_id:
            mysupid = 0
        else:
            mysupid = self.supplier_id.id
        if not self.product_id:
            myprodid = 0
        else:
            myprodid = self.product_id.id

        if mysupid==0 and myprodid==0 :
           raise UserError("""必須至少選擇其中一個索引值""")

        self.env.cr.execute("""select gensupplierinfo(%d,%d)""" % (mysupid,myprodid))
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_gh_iot.view_supplierinfo_tree')
        return {
            'view_name': 'gh_supplierinfo_list',
            'name': (u'供應商供料複合查詢'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.supplierinfo',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
