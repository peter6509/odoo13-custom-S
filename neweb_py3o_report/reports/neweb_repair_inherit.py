# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class Py3oNewebRepairInherit(models.Model):
    _inherit = "neweb_repair.repair"

    @api.depends('repair_lines')
    def _get_repair_parts(self):
        mycrepairparts=''
        for rec in self.repair_lines:
            for rec1 in rec.repair_parts:
                if mycrepairparts=='':
                    mycrepairparts=rec1.prod.name
                else:
                    mycrepairparts = mycrepairparts + ' , ' + rec1.prod.name
        self.crepairparts = mycrepairparts
        return mycrepairparts

    @api.depends('repair_work_logs')
    def _get_work_date(self):
        mycworkdate=''
        for rec in self.repair_work_logs:
            if mycworkdate=='':
                mycworkdate = fields.Date.from_string(rec.work_date).strftime('%Y%m%d')
            else:
                mycworkdate = mycworkdate + ' , ' + fields.Date.from_string(rec.work_date).strftime('%Y%m%d')
        self.cworkdate = mycworkdate
        return mycworkdate

    @api.depends('repair_work_logs')
    def _get_work_log(self):
        mycworklog = ''
        for rec in self.repair_work_logs:
            if mycworklog == '':
                mycworklog = rec.work_log
            else:
                mycworklog = mycworklog + ' , ' + rec.work_log
        self.cworklog = mycworklog
        return mycworklog


    crepairparts = fields.Char(string="報修用料py3o",compute=_get_repair_parts)
    cworkdate = fields.Char(string="處理日期py3o",compute=_get_work_date)
    cworklog = fields.Char(string="處理內容py3o",compute=_get_work_log)