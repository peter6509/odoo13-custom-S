# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebbaseslainherit(models.Model):
    _inherit = "neweb_base.sla"

    backup_equipment = fields.Boolean(string=u"提供備機服務",default=False)


    @api.model
    def create(self, vals):
        myname = ""
        if 'response_time' in vals and vals['response_time']:
           myname = "回應時間:%s小時 /" % vals['response_time']
        if 'onsite_time' in vals and vals['onsite_time']:
           myname = "%s到場時間:%s小時 /" % (myname,vals['onsite_time'])
        if 'maintenance_time' in vals and vals['maintenance_time']:
           myname = "%s完修時間:%s小時 /" % (myname,vals['maintenance_time'])
        if 'backup_equipment' in vals and vals['backup_equipment'] and vals['backup_equipment']==True :
           myname = "%s 時間內無法完修需提供備機 " % myname
        vals['name'] = myname
        myrecnum = self.env['neweb_base.sla'].search_count([('name','=',myname)])
        if int(myrecnum) > 0 :
            raise UserError("SLA 已重複了,請確認...")

        rec = super(newebbaseslainherit, self).create(vals)
        return rec


    def write(self, vals):
        myname = ""
        if 'response_time' in vals and vals['response_time']:
            myname = "回應時間:%s小時 /" % vals['response_time']
        if 'onsite_time' in vals and vals['onsite_time']:
            myname = "%s到場時間:%s小時 /" % (myname, vals['onsite_time'])
        if 'maintenance_time' in vals and vals['maintenance_time']:
            myname = "%s完修時間:%s小時 /" % (myname, vals['maintenance_time'])
        if 'backup_equipment' in vals and vals['backup_equipment'] and vals['backup_equipment'] == True:
            myname = "%s 時間內無法完修需提供備機" % myname
        vals['name'] = myname
        myrecnum = self.env['neweb_base.sla'].search_count([('name', '=', myname)])
        if int(myrecnum) > 0:
            raise UserError("SLA 已重複了,請確認...")

        rec = super(newebbaseslainherit, self).write(vals)
        return rec
