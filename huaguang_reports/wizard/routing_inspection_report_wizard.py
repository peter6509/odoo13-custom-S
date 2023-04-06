# -*- coding: utf-8 -*-
from odoo import fields,api,models,_


class routing_inspection_report_wizard(models.TransientModel):
    _name = 'routing.inspection.report.wizard'
    _description = '品质报表'

    pcr_name = fields.Char('炉号')
    material_quality = fields.Char('品种')
    date_start = fields.Datetime('起始时间', required='1', default=fields.Datetime.now)
    date_end = fields.Datetime('结束时间', required='1', default=fields.Datetime.now)

    def open_table(self):
        self.ensure_one()



        if self.pcr_name:
            op1 = 'ilike'
        else:
            op1 = '!='

        if self.material_quality:
            op2 = '='
        else:
            op2 = '!='

        return {
            'name': _("品质巡检报表"),
            'view_mode': 'tree,pivot',
            'domain': [('pcr_id.name', op1, self.pcr_name),
                       ('material_quality', op2, self.material_quality),
                       ('date', '>=', self.date_start),
                       ('date', '<=', self.date_end)],
            'res_model': 'routing.inspection.report',
            'type': 'ir.actions.act_window',
                }


