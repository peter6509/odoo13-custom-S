# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class iplamaintenanceinherit1(models.Model):
    _name = "maintenance.equipment_status"
    _order = "sequence,id"

    status_code = fields.Char(string="停機碼",required=True)
    status_name = fields.Char(string="停機說明",required=True)
    status_type = fields.Selection([('1','故障'),('2','換線'),('3','復歸')],string='類別')
    sequence = fields.Integer(string="SEQ",default=20)

    def name_get(self):
        result = []
        for myrec in self:
            myname = "[%s]%s" % (myrec.status_code,myrec.status_name)
            result.append((myrec.id, myname))
        return result


class alldoiplaiotoutofforderstatus(models.Model):
    _name = "alldo_ipla_iot.equipment_outofforder_status"
    _order = "start_datetime desc"

    iot_id = fields.Many2one('maintenance.equipment', ondelete='cascade')
    status_id = fields.Many2one('maintenance.equipment_status',string="停機類別")
    iot_workorder = fields.Many2one('alldo_ipla_iot.workorder', string="工單號碼")
    start_datetime = fields.Datetime(string="發生時間")
    end_datetime = fields.Datetime(string="排除時間")
    outoff_duration = fields.Float(digits=(6,1),string="停機時間(分鐘)")
    outoff_owner = fields.Many2one('hr.employee',string="工程師")



