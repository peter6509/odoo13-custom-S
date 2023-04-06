# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeLast10ShippingWizard(models.TransientModel):
    _name = "alldo_acme_iot.last10_shipping_wizard"
    _description = "產品最近10次出貨達成率KPI精靈"

    prod_no = fields.Many2one('product.product',string="產品料號")

    def run_last10_shipping(self):
        self.env.cr.execute("""select genprodshippingkpi(%d)""" % self.prod_no.id)
        self.env.cr.execute("""commit""")

        return { 'name' : 'Go to website',
               'res_model':'ir.actions.act_url',
               'type':'ir.actions.act_url',
               'target':'new',
               'url':'http://192.168.10.135:8080/webroot/decision/view/report?viewlet=acme_prodlast10shipping.cpt'
                    }