# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api


class maintenance_pivot(models.TransientModel):
    _name = "maintenance_month.pivot"

    name = fields.Char(string=u"單號")
    department_name = fields.Char(size=20, string=u'部門')
    equipment_name = fields.Char(size=100, string=u'機台編號')
    equipment_desc = fields.Char(size=100,string=u"機台名稱")
    maintenance_type = fields.Selection([('corrective',u'停機'),('preventive',u'未停機')],string=u"維修類型")
    request_date = fields.Datetime(string=u'請求時間')
    repaired_date = fields.Datetime(string=u'完修時間')
    process_date = fields.Datetime(string=u"維修開始時間")
    technician = fields.Char(size=20, string=u'維護人員')
    maintenance_content = fields.Char(size=100, string=u'維護內容')
    faulttext = fields.Char(size=100, string=u'故障原因')
    parts_name = fields.Char(size=100, string=u'更換零件')
    brokentime = fields.Float(digits=(10, 1), string=u'故障時間')
    waittime = fields.Float(digitals=(10, 1), string=u'待料時間')
    maintenancetime = fields.Float(digits=(10, 1), string=u'維修時間')
    name = fields.Char(size=20, string=u'單號')
