# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplaiotsaleorderinherit(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchangepartner(self):
        self.env.cr.execute("""select getcusprod(%d)""" % self.partner_id.id)
        myres = self.env.cr.fetchall()
        return {'domain':{'order_line.product_id': [('id', 'in', myres)]}}


class iplaiotsaleorderlineinherit(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('order_id.partner_id')
    def onchangepartner(self):
        self.env.cr.execute("""select getcusprod(%d)""" % self.order_id.partner_id.id)
        myres = self.env.cr.fetchall()
        return {'domain':{'product_id': [('id', 'in', myres)]}}