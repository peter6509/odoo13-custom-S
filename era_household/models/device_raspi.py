# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class erahouseholddevice(models.Model):
    _name = "era_household.devices"

    devices_id = fields.Char(string="Devices ID",required=True)    # 裝置ID
    modbus_id = fields.Char(string="Modbus ID",required=True)      # MODBUS ID
    value = fields.Float(digits=(10,2),string="VALUE")             # 數值

