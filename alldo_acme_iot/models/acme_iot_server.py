# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoacmeiotserverinfo(models.Model):
    _name = "alldo_acme_iot.server_info"
    _description = "IOT Server資訊"
    _rec_name = "iot_server_name"

    iot_server_name = fields.Char(string="IOT伺服器名稱",required=True)
    iot_server_ip = fields.Char(string="IOT Server IP",required=True)
    iot_db_name = fields.Char(string="IOT DB NAME",required=True)
    iot_db_username = fields.Char(string="IOT DB USERNAME",required=True)
    iot_db_passwd = fields.Char(string="IOT DB PASSWORD",required=True)
    server_path = fields.Char(string="伺服器檔案路徑",required=True,default='/alldo_config')
    client_path = fields.Char(string="IOT 終端檔案路徑",required=True,default='/home/pi/alldo_config')

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.iot_server_name, myrec.iot_db_name)
            result.append((myrec.id, myname))
        return result


    @api.model
    def create(self, vals_list):

        res = super(alldoacmeiotserverinfo, self).create(vals_list)
        mynum = self.env['alldo_acme_iot.server_info'].search_count([])
        if mynum > 1:
            raise UserError("只能存在一筆IOT主機資訊")

        return res





