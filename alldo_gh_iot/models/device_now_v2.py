# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class devicenow2(models.Model):
    _name = "device.now_v2"

    ip_adrs = fields.Char(string="IP Address",required=True)
    modbus_cmd = fields.Char(string="modbus cmd",required=True)
    seqno = fields.Integer(string="seqno",required=True)
    did = fields.Char(string="DID")
    val_name = fields.Char(string="val name")
    val_unit = fields.Char(string="Val unit")
    value = fields.Float(string="VALUE")
    dat = fields.Datetime(string="dat")
    val_per = fields.Integer(string="val per",default=1)
    ch_val_name = fields.Char(string="ch val name")
    did_seq = fields.Integer(string="did seq")
    gw_desc = fields.Char(string="gw desc")
    real_data_showed = fields.Char(string="real data showed")
    val_type = fields.Char(string="val type")
    cust_id = fields.Char(string="cust id")
    c_val_name = fields.Char(string="c val name")
    e_val_name = fields.Char(string="e val name")
    v_val_name = fields.Char(string="vv val name")
    longitude = fields.Char(string="longitude")
    latitude = fields.Char(string="latitude")
    rdno = fields.Char(string="rdno")
    machine = fields.Char(string="machie")
    model_no = fields.Char(string="model no")
    model_desc = fields.Char(string="model desc")
    machineid = fields.Char(string="machine id")

