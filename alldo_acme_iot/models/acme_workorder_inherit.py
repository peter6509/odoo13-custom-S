# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class AcmeWorkOrderInherit(models.Model):
    _inherit = "alldo_acme_iot.workorder"

    @api.depends('iot_line')
    def _get_iotnum(self):
        for rec in self:
            iotnum = 0
            for rec1 in rec.iot_line:
                iotnum = iotnum + rec1.iot_num
            rec.iot_num = iotnum

    iot_num = fields.Integer(string="IOT數量",compute=_get_iotnum)
