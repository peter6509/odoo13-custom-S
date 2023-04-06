# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm


class MProductWizard(models.TransientModel):
    _name = "mproduct.wizard"

    defaultcode = fields.Char(size=30)
    prodname = fields.Char(size=30)
    qtystatus = fields.Selection([('1', u'小於'), ('2', u'等於'), ('3', u'大於')], default='2')
    qtyvalue = fields.Integer(default=0)

    @api.multi
    def product_qty_print(self):
        data = dict()
        data["defaultcode"] = self.defaultcode
        data["prodname"] = self.prodname
        data["qtystatus"] = self.qtystatus
        data["qtyvalue"] = self.qtyvalue

        return self.env['report'].get_action(self, 'maintenance_report.mproduct_report', data=data)
