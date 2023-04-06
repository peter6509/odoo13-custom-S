# -*- coding: utf-8 -*-
from odoo import fields,api,models,_
import datetime


class ProductionSummaryReportWizard(models.TransientModel):
    _name = 'production.summary.report.wizard'
    _description = '生产汇总表'

    material_quality = fields.Char('品种')
    size = fields.Char('成型规格')
    date_start = fields.Date('起始时间', required=True,
                             default=(datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1))
    date_end = fields.Date('结束时间', required=True, default=fields.Date.context_today)

    def open_table(self):
        self.ensure_one()

        # domain = [('date_in', '>=', self.date_start), ('date_in', '<=', self.date_end)]
        # if self.material_quality:
        #     domain.append(('material_quality', 'ilike', self.material_quality))
        # if self.size:
        #     domain.append(('cx_size', 'ilike', self.size))

        self.env['production.summary.new.report']._create_report(
            self.date_start,self.date_end,self.material_quality,self.size
        )

        return {
            'name': _("生产汇总表（新）"),
            'view_mode': 'tree',
            'res_model': 'production.summary.new.report',
            # 'domain': domain,
            'type': 'ir.actions.act_window',
                }


