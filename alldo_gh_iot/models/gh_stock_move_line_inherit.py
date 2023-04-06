# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree

class ghstockmovelineinherit(models.Model):
    _inherit = "stock.move.line"

    po_no = fields.Many2many('alldo_gh_iot.po_wkorder','ghiot_moveline_powk_rel','move_id','po_id',string="客戶訂單")


    @api.onchange('product_id','qty_done')
    def onchangeprodid(self):
        self.env.cr.execute("""select getprodpo(%d)""" % self.product_id.id)
        myrec = self.env.cr.fetchall()
        ids=[]
        for line in myrec:
            ids.append(line[0])
        return {'domain':{'po_no': [('id', 'in', ids)]}}




