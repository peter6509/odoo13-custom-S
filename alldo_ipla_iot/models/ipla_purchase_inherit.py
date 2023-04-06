# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplapurchaseinherit(models.Model):
    _inherit = "purchase.order"

    def name_get(self):
        result = []

        for record in self:
            myprod = ''
            for rec in record.order_line:
                if myprod=='':
                    myprod = rec.product_id.default_code
                else:
                    myprod = myprod + '/ ' + rec.product_id.default_code
            result.append(
                (record.id, '[%s]%s-(%s)' % (record.name, record.partner_id.name,myprod)))
        return result