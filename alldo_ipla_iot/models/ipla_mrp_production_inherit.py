# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class iplamrpproductioninherit(models.Model):
    _inherit = "mrp.production"

    @api.model
    def create(self, vals):

        res = super(iplamrpproductioninherit, self).create(vals)
        self.env.cr.execute("""select mrpproductionupdate('%s')""" % res.name)
        self.env.cr.execute("""commit""")
        return res

    def write(self, vals):

        res = super(iplamrpproductioninherit, self).write(vals)
        for rec in self:
            self.env.cr.execute("""select mrpproductionupdate('%s')""" % rec.name)
            self.env.cr.execute("""commit""")
        return res

    def name_get(self):
        result = []
        for record in self:
            result.append(
                (record.id, '%s-(%s)[訂單數量:%s]' % (record.name,record.product_id.default_code,record.product_qty)))
        return result