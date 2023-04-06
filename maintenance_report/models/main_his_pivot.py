# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api


class mainhispivot(models.TransientModel):
    _name = "maintenance_his.pivot"

    department_name = fields.Char(size=20, string=u'部門')
    equipment_name = fields.Char(size=100, string=u'機台編號')
    equipment_desc = fields.Char(size=100,string=u"機台名稱")
    request_date = fields.Datetime(string=u'申請時間')
    repaired_date = fields.Datetime(string=u'完修時間')
    broken_time = fields.Float(digits=(10, 1), string=u'故障時間')
    maintenance_content = fields.Char(size=100, string=u'維護內容')
    parts_name = fields.Char(size=100, string=u'更換零件')
    technician = fields.Char(size=20, string=u'維護人員')
    faulttext = fields.Char(size=100, string=u'故障原因')
