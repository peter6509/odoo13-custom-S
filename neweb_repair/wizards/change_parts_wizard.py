# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import Warning


class changepartswizard(models.TransientModel):
    _name = "neweb_repair.change_parts_wizard"


    repair_no = fields.Many2one('neweb_repair.repair',string='報修單號',required=True)
    origin_parts = fields.Many2one('product.product',string="原始零組件",required=True)
    change_parts = fields.Many2one('product.product',string="變更零組件",required=True)

    def changeparts(self):
        self.env.cr.execute("""select changeparts(%d,%d,%d)""" % (self.repair_no.id,self.origin_parts.id,self.change_parts.id))
        # raise Warning("如果輸入之數據正確,報修單零組件料號已變更！")

