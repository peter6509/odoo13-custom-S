# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeLast10QCWizard(models.TransientModel):
    _name = "alldo_acme_iot.last10_qc_wizard"
    _description = "產品最近10次生產良率KPI精靈"

    prod_no = fields.Many2one('product.product',string="產品料號")

    def run_last10_qc(self):
        self.env.cr.execute("""select genprodkpi(%d,'%s')""" % (self.prod_no.id,'鑄造'))
        self.env.cr.execute("""commit""")

        return { 'name' : 'Go to website',
               'res_model':'ir.actions.act_url',
               'type':'ir.actions.act_url',
               'target':'new',
               'url':'http://192.168.10.135:8080/webroot/decision/view/report?viewlet=acme_prodlast10qc.cpt'
                    }