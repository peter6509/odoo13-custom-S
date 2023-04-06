# -*- coding: utf-8 -*-
from odoo import fields,api,models,_


class zimo_pcr_stock_report_wizard(models.TransientModel):
    _name = 'zimo.pcr.stock.report.wizard'
    _description = '在制品库存量报表'

    @api.model
    def compute_routes(self):
        route_ids = self.env['mrp.routing'].search([('workshop_section', '!=', False)])
        workshop_sections = set(route_ids.mapped('workshop_section'))
        routes = []
        for workshop_section in workshop_sections:
            routes.append((workshop_section,workshop_section))
        return routes


    material_quality = fields.Char('品种')
    size = fields.Char('规格')
    route = fields.Selection(selection='compute_routes', string='工段')


    def open_table(self):
        self.ensure_one()
        domain = []
        if self.material_quality:
            domain.append(('material_quality','ilike',self.material_quality))
        if self.route:
            domain.append(('routing', '=', self.route))
        if self.size:
            domain.append(('size', 'ilike', self.size))
        return {
            'name': _("在制品库存报表"),
            'view_mode': 'tree,form,pivot',
            'res_model': 'zimo.pcr.stock.report',
            'domain': domain,
            'type': 'ir.actions.act_window',
                }


