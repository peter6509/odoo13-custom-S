# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NewebProdPriceAnalysisWizard(models.TransientModel):
    _name = "neweb.prod_price_analysys_wizard"
    _description = "業務單價與採購單價比較表"

    start_date = fields.Date(string="成本分析起始日期")
    end_date = fields.Date(string="成本分析截止日期")

    def run_price_analysis(self):
        self.env.cr.execute("""select genprojectpriceanalysis('%s','%s')""" % (self.start_date,self.end_date))
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('neweb_purchase.view_neweb_prod_price_tree')
        return {
            'view_name': '',
            'name': (''),
            'type': 'ir.actions.act_window',
            'res_model': 'neweb.prod_price_list',
            'view_id': myviewid.id,
            'flags': {'action_buttons': True},
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'main'}
