# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

class acmestockquantinherit(models.Model):
    _inherit = "stock.quant"

    quant_note = fields.Char(string="Note")


    def name_get(self):
        result = []
        for record in self:
            if self.env.context.get('lot_search', False):
                # Only goes off when the custom_search is in the context values.
                result.append((record.id, "%s" % record.product_id.default_code))
            else:
                result.append((record.id,'%s-批號(%s)在手量[%s]' %(record.product_id.default_code,record.lot_id.name,record.quantity)))
        return result

