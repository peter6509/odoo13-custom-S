# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm


class MReportWizard(models.TransientModel):
    _name = "mreport.wizard"

    department_id = fields.Many2one('department', 'Department', track_visibility='onchange')
    equipment_id = fields.Many2one('maintenance.equipment', 'Equipment')
    start_date = fields.Datetime()
    end_date = fields.Datetime()

    # part_id = fields.Many2one('product.template', 'Parts')

    @api.onchange("department_id")
    def onchange_department_id(self):
        res = {}
        if self.department_id:
            res['domain'] = {'equipment_id': [('department_id', '=', self.department_id.id)]}
        return res

    @api.multi
    def main_smart_print(self):
        # raise except_orm(u'TEST','%s %s %s' % (self.department_id.id,self.equipment_id.id,self.start_date))
        if self.department_id.id == False and self.equipment_id.id == False and self.start_date == False and self.end_date == False:
            raise except_orm(u'條件不符', u'沒有設定過濾資料,請確認....')
        self.ensure_one()
        data = dict()
        data["department_id"] = self.department_id.id
        data["equipment_id"] = self.equipment_id.id
        data["start_date"] = self.start_date
        data["end_date"] = self.end_date
        # data["part_id"] = self.part_id.id
        # raise except_orm('INFO', '%s / %s / %s' % (self.department_id.name,self.equipment_id.name,self.part_id.name))

        return self.env['report'].get_action(self, 'maintenance_report.mreport_request', data=data)
