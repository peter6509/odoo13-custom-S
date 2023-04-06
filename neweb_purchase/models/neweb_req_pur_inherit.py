# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class newebreqpurinherit(models.Model):
    _inherit = "neweb.require_purchase"

    @api.depends('asset_machine_type')
    def _get_assetmach(self):
        i = 1
        mymachinedesc = ""
        for rec in self.asset_machine_type:
            mymachinedesc = mymachinedesc + "(%d)%s " % (i, rec.name)
            i = i + 1
        self.asset_machine_desc = mymachinedesc
        return mymachinedesc

    @api.depends('expense_machine_type')
    def _get_expmach(self):
        i = 1
        myexpmachinedesc = ""
        for rec in self.expense_machine_type:
            myexpmachinedesc = myexpmachinedesc + "(%s)%s " % (i, rec.name)
            i = i + 1
        self.expense_machine_desc = myexpmachinedesc
        return myexpmachinedesc

    asset_machine_desc = fields.Char(string="MA備機類別說明",compute=_get_assetmach)
    expense_machine_desc = fields.Char(string="MA零件類別說明",compute=_get_expmach)

