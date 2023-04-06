# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
import base64
import pickle
import os,os.path
from ..utils.gh_iot_util import IOT_UTIL

class ghiotbells(models.Model):
    _name = "alldo_gh_iot.bells_set"

    name = fields.Char(string="名稱",required=True)
    bells_ip = fields.Char(string="IP ADDRESS",required=True)
    bells_line = fields.One2many('alldo_gh_iot.bells_line','bells_id',string="bells line")


    @api.model
    def create(self, vals):
        mycount = self.env['alldo_gh_iot.bells_set'].search_count([])
        if mycount > 0 :
            raise UserError("只能設定一筆鐘聲記錄")
        res = super(ghiotbells, self).create(vals)
        return res

    # def _write(self, vals):
    #     res = super(ghiotbells, self)._write(vals)
    #     self.env.cr.execute("""select resetbells()""")
    #     self.env.cr.execute("""commit""")
    #     return res

    def run_reset_bells(self):
        self.env.cr.execute("""select resetbells()""")
        self.env.cr.execute("""commit""")

    def run_mp3_checktime(self):
        myrec = self.env['alldo_gh_iot.bells_set'].search([])
        myip = myrec[0].bells_ip
        self.env.cr.execute("""select genbells()""")
        myres = self.env.cr.fetchone()[0]
        # print(myres)
        # print(myip)
        if myres != 'NO' :
            mylocalfile = '/opt/odoo13/dbbackup/music.pickle'
            myremotefile = '/home/pi/alldo_config/music.pickle'
            with open(mylocalfile, 'wb') as music_info:
                pickle.dump('/home/pi/%s' % myres, music_info,protocol=pickle.HIGHEST_PROTOCOL)
            IOT_UTIL.iot_push_file(myip, mylocalfile, myremotefile)

    def run_mp3_test(self):
        myrec = self.env['alldo_gh_iot.bells_set'].search([])
        myip = myrec[0].bells_ip
        self.env.cr.execute("""select genbells()""")
        myres = self.env.cr.fetchone()[0]
        print(myres)
        print(myip)
        # if myres != 'NO' :
        mylocalfile = '/opt/odoo13/dbbackup/music.pickle'
        myremotefile = '/home/pi/alldo_config/music.pickle'
        with open(mylocalfile, 'wb') as music_info:
            pickle.dump('/home/pi/workinghours.mp3' , music_info,protocol=pickle.HIGHEST_PROTOCOL)
        IOT_UTIL.iot_push_file(myip, mylocalfile, myremotefile)


    def run_sync_mp3(self):
        for rec in self.bells_line:
            mylocalfile = '%s%s' % ('/opt/odoo13/dbbackup/',rec.bells_file_name)
            # mylocalfile = '%s%s' % ('/Users/odoo/music/', rec.bells_file_name)
            with open(mylocalfile,'wb') as f:
                f.write(base64.b64decode(rec.bells_file))
            myremotefile = '%s%s' % ('/home/pi/',rec.bells_file_name)
            IOT_UTIL.iot_push_file(self.bells_ip, mylocalfile, myremotefile)

        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message'] = 'IOT裝置已同步公司鈴聲MP3！'
        return {
            'name': '系統通知訊息',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': context,
        }

class ghiotbellsline(models.Model):
    _name = "alldo_gh_iot.bells_line"

    bells_id = fields.Many2one('alldo_gh_iot.bells_set',ondelete='cascade')
    bells_time = fields.Char(string="播放時間 HH:MM:SS ")
    bells_file = fields.Binary(string=u"MP3檔案")
    bells_file_name = fields.Char(string=u"檔名")
    next_run_bells = fields.Datetime(string="下次時間")

    def manual_test(self):
        mylocalfile = '/opt/odoo13/dbbackup/music.pickle'
        # mylocalfile = '%s%s' % ('/Users/odoo/music/', self.bells_file_name)
        myremotefile = '/home/pi/alldo_config/music.pickle'
        with open(mylocalfile, 'wb') as music_info:
            pickle.dump('/home/pi/%s' % self.bells_file_name, music_info, protocol=pickle.HIGHEST_PROTOCOL)
        IOT_UTIL.iot_push_file(self.bells_id.bells_ip, mylocalfile, myremotefile)
