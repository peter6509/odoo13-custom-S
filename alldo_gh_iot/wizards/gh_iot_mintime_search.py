# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class ghiotmintimesearch(models.TransientModel):
    _name = "alldo_gh_iot.mintime_search_wizard"
    _description = "產品每工序最低工時精靈"

    product_id = fields.Many2one('product.product',string="產品",required=True)

    def run_mintime_search(self):
        self.env.cr.execute("""select runmintime(%d)""" % self.product_id.id)
        self.env.cr.execute("""commit""")

        myviewid = self.env.ref('alldo_gh_iot.gh_iot_mintime_list_tree')

        return {
            'view_name': 'gh_iot_mintime_list_tree',
            'name': (u'產品每工序最低工時查詢統計'),
            'type': 'ir.actions.act_window',
            'res_model': 'alldo_gh_iot.mintime_list',
            'view_id': myviewid.id,
            'view_type': 'form',
            'view_mode': 'tree',
            'target': 'list'}



