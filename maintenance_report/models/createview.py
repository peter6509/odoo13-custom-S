# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api, tools
import datetime


class CreateView(models.Model):
    _name = "my.createview"

    @api.model_cr
    def init(self):
        """ DAN_PROD VIEW CREATE"""
        tools.drop_view_if_exists(self._cr, 'dana_prod')
        self._cr.execute("""CREATE OR REPLACE VIEW public.dana_prod AS
                              (SELECT product_template.id,product_template.default_code,
                              product_template.name,product_template.description_purchase,
                              stock_quant.qty,stock_quant.location_id
                              FROM product_template
                              LEFT JOIN stock_quant ON product_template.id = stock_quant.product_id
                              ORDER BY product_template.default_code);""")
        # @api.model
        # def replace_loc_time(self):
