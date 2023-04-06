# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebcontractinherit2(models.Model):
    _inherit = "neweb_contract.contract"

    @api.depends('ae1')
    def _get_ae(self):
        myae2 = ""
        for rec in self.ae1:
            if myae2 == "":
                myae2 = rec.resource_id.name
            else:
                myae2 = myae2 + "/" + rec.resource_id.name
        self.ae2 = myae2
        return myae2

    need_control = fields.Boolean(string="是否需系統監控軟體", default=False)
    ae2 = fields.Char(string="工程師",compute=_get_ae)
    cus_project = fields.Char(string="客戶專案")


