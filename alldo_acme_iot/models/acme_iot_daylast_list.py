# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmeiotdaylastlist(models.Model):
    _name = "alldo_acme_iot.daylast_list"

    iot_id = fields.Many2one('maintenance.equipment')
    last_date1 = fields.Char(string="日期")
    last_date2 = fields.Date(string="日期")
    iot_datetime = fields.Datetime(string="第一員最後一件時間")
    iot_owner = fields.Many2one('hr.employee',string="操作員")

class acmeiotdaylastemp(models.Model):
    _name = "alldo_acme_iot.daylast_manlist"

    item_id = fields.Integer(string="SEQ")
    emp_id = fields.Many2one('hr.employee',string="EMP ID")
    emp_name = fields.Char(string="操作員")


class acmeiotdaylastsumlist(models.Model):
    _name = "alldo_acme_iot.daylast_sum_list"
    _order = "last_date1"


    last_date1 = fields.Char(string="日期")
    last_date2 = fields.Date(string="日期")
    iot_datetime1 = fields.Datetime(string="第一員最後一件時間")
    cdatetime1 = fields.Char(string="第一員最後一件時間")
    iot_datetime2 = fields.Datetime(string="第二員最後一件時間")
    cdatetime2 = fields.Char(string="第二員最後一件時間")
    iot_datetime3 = fields.Datetime(string="第三員最後一件時間")
    cdatetime3 = fields.Char(string="第三員最後一件時間")
    iot_datetime4 = fields.Datetime(string="第四員最後一件時間")
    cdatetime4 = fields.Char(string="第四員最後一件時間")
    iot_datetime5 = fields.Datetime(string="第五員最後一件時間")
    cdatetime5 = fields.Char(string="第五員最後一件時間")
    iot_datetime6 = fields.Datetime(string="第六員最後一件時間")
    cdatetime6 = fields.Char(string="第六員最後一件時間")
    iot_datetime7 = fields.Datetime(string="第七員最後一件時間")
    cdatetime7 = fields.Char(string="第七員最後一件時間")
    iot_datetime8 = fields.Datetime(string="第八員最後一件時間")
    cdatetime8 = fields.Char(string="第八員最後一件時間")
    iot_datetime9 = fields.Datetime(string="第九員最後一件時間")
    cdatetime9 = fields.Char(string="第九員最後一件時間")
    iot_datetime10 = fields.Datetime(string="第十員最後一件時間")
    cdatetime10 = fields.Char(string="第十員最後一件時間")


