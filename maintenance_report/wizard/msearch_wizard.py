# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import except_orm


class MainReqSearchWizard(models.TransientModel):
    _name = "msearch.wizard"

    department_id = fields.Many2one('department', 'Department', track_visibility='onchange')
    equipment_id = fields.Many2one('maintenance.equipment', 'Equipment')
    start_date = fields.Date()
    end_date = fields.Date()
    part_id = fields.Many2one('product.template', 'Parts')

    @api.onchange("department_id")
    def onchange_department_id(self):
        res = {}
        if self.department_id:
            res['domain'] = {'equipment_id': [('department_id', '=', self.department_id.id)]}
        return res

    @api.multi
    def main_smart_search(self):
        my_department_id = self.department_id.id
        my_equipment_id = self.equipment_id.id
        my_start_date = self.start_date
        my_end_date = self.end_date
        my_part_id = self.part_id.id
        mydomain = []
        # mydomain.append((1,'=',1))
        if my_department_id:
            mydomain.append(('department_id', '=', my_department_id))
        if my_equipment_id:
            mydomain.append(('equipment_id', '=', my_equipment_id))
        if my_start_date:
            mydomain.append(('repaired_date', '>=', my_start_date))
        if my_end_date:
            mydomain.append(('repaired_date', '<=', my_end_date))
        if my_part_id:
            # print '%s' % my_part_id
            myids = []
            myreqid = self.env['maintenance.request.part_line'].search([('part_id', '=', my_part_id)])
            if len(myreqid) > 0:
                # myreqid.ensure_one()
                for record in myreqid:
                    myids.append(record.request_id.id)
                    # print '%s' % record.request_id.id
                mydomain.append(('id', 'in', myids))
        if len(mydomain) == 0:
            raise except_orm(u'條件錯誤', u'沒有符合的維修記錄')

        return {'view_name': 'MainReqSearchWizard',
                'name': (u'設備維修履歷複合查詢'),
                'views': [[False, 'tree'], [False, 'form'], [False, 'pivot']],
                'res_model': 'maintenance.request',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'current',
                'domain': mydomain,
                'flags': {'action_buttons': False},
                'view_mode': 'tree,form,pivot',
                'view_type': 'form'
                }
