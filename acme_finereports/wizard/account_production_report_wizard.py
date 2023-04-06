# -*- coding: utf-8 -*-
from odoo import fields,api,models,_


class AccountProductionReportWizard(models.TransientModel):
    _name = 'account.production.report.wizard'
    _description = '炉号成品率表'

    pcr_name = fields.Char('炉号')
    material_quality = fields.Char('品种')
    date_start = fields.Date('起始时间', required=True, default=fields.Date.context_today)
    date_end = fields.Date('结束时间', required=True, default=fields.Date.context_today)
    route_ids = fields.Many2many('mrp.routing', string='工艺')


    def open_table(self):
        self.ensure_one()

        routing_id = []
        domain = [('completed_time', '>=', self.date_start),
                  ('completed_time', '<=', self.date_end),]
        for route in self.route_ids:
            routing_id.append(route.name)
        routing_ids = tuple(routing_id)
        if len(routing_ids) > 0:
            domain.append(('routing', 'in', routing_ids),)
        if self.pcr_name:
            domain.append(('line_id.name', 'ilike', self.pcr_name),)
        if self.material_quality:
            domain.append(('material_quality', 'ilike', self.material_quality))


        return {
            'name': _("炉号成品率报表" + "："+str(self.date_start)+'至'+str(self.date_end)),
            'view_mode': 'tree,form',
            'res_model': 'account.production.report',
            'domain': domain,
            'type': 'ir.actions.act_window',
                }


