# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime


class supermainmod(models.TransientModel):
    _name = "maintenance.supermod"

    name = fields.Many2one('maintenance.request', string=u"維修單號")
    department_id = fields.Many2one('department', string=u"部門別")
    equipment_id = fields.Many2one('maintenance.equipment', string=u'機台編號')
    technician_user_id = fields.Many2one('res.users', string=u"維修人員")
    process_date = fields.Datetime(string=u"接單處理開始時間")
    repaired_date = fields.Datetime(string=u"維修完成時間")
    maintenance_time = fields.Float(string=u"維修時數", digits=(10, 1))
    keyin_wait_time = fields.Float(string=u"待料時數", digits=(10, 1))
    broken_time = fields.Float(string=u"故障時數", digits=(10, 1))

    @api.onchange("name")
    def onchange_main_id(self):
        res = {}
        if self.name:
            main_rec = self.env['maintenance.request'].search([('name', '=', self.name.name)])
            self.department_id = main_rec.department_id
            self.equipment_id = main_rec.equipment_id
            self.technician_user_id = main_rec.technician_user_id
            myprodate = fields.Datetime.from_string(main_rec.process_date)
            myrepdate = fields.Datetime.from_string(main_rec.repaired_date)
            self.process_date = myprodate
            self.repaired_date = myrepdate
            self.maintenance_time = main_rec.maintenance_time
            self.keyin_wait_time = main_rec.keyin_wait_time
            self.broken_time = main_rec.broken_time
        return

    @api.multi
    def main_request_mod(self):
        if not self.repaired_date:
            raise except_orm(u"資料錯誤", u"維修完成時間未輸入")
        if not self.keyin_wait_time or self.keyin_wait_time < 0:
            self.keyin_wait_time = 0
        main_rec = self.env['maintenance.request'].search([('name', '=', self.name.name)])
        myrepdate = fields.Datetime.from_string(self.repaired_date)
        myprodate = fields.Datetime.from_string(self.process_date)
        main_rec.write({'repaired_date': myrepdate,
                        'process_date': myprodate,
                        'keyin_wait_time': self.keyin_wait_time,
                        })

    @api.model_cr
    @api.model
    def change_request_data(self):
        change_rec = self.env['maintenance.request'].search([])
        for myrec in change_rec:
            self._cr.execute("select change_departmentid(%d)" % myrec.department_id)
            mydepartmentid = self._cr.fetchone()
            self._cr.execute("select change_equipmentid(%d)" % myrec.equipment_id)
            myequipmentid = self._cr.fetchone()
            myrec.write({'department_id': mydepartmentid,
                         'equipment_id': myequipmentid})
        self._cr.execute(
            "delete from maintenance_equipment where id not in (select equipment_id from maintenance_request) and id > 627")
        self._cr.execute(
            "delete from department where id not in (select department_id from maintenance_request) and id > 32")
