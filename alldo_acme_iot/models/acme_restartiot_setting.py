# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import paramiko
from ..utils.acme_iot_util import IOT_UTIL

class acmeiotrestartsetting(models.Model):
    _name = "alldo_acme_iot.restartiot_setting"

    restart_time = fields.Char(string="重啟時間 HH:MM:SS ")
    restart_freq = fields.Integer(string="間隔天數",default=1)
    next_run_restart = fields.Datetime(string="下次時間")

    @api.model
    def create(self, vals):
        mycount = self.env['alldo_acme_iot.restartiot_setting'].search_count([])
        if mycount > 0 :
            raise UserError("只能設定一筆重啟記錄")
        res = super(acmeiotrestartsetting, self).create(vals)
        return res

    def run_iot_restarttime(self):
        self.env.cr.execute("""select iotresettime()""")
        self.env.cr.execute("""commit""")

    def run_iotrestart(self):
        self.env.cr.execute("""select geniotrestart()""")
        myres = self.env.cr.fetchone()[0]
        if myres == 'YES' :
            myrec = self.env['maintenance.equipment'].search([('category_id','=',2)])
            # for rec in myrec:
            #     IOT_UTIL.wip_reboot(rec.iot_ip)
            #     rec.update({'iot_status': '4'})
