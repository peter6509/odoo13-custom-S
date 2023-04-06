# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_


class zimo_pcr_stock_report(models.Model):
    _name = "zimo.pcr.stock.report"
    _auto = False
    _description = '''在制品库存量报表'''

    size = fields.Char('规格')
    material_quality = fields.Char('品种')
    process_qty = fields.Float("在制数量")
    inventory_qty = fields.Float("库存量")
    routing = fields.Char('工段')
    pcr_ids = fields.One2many('production.circulation.record', compute='compute_pcr_line', string='炉号')


    def init(self):
        tools.drop_view_if_exists(self._cr, 'zimo_pcr_stock_report')
        self._cr.execute("""
            create or replace view  zimo_pcr_stock_report as (
            with pcrl as (
                        select 
                        pt.material_quality,
                        pt.size,
                        coalesce(pcr.plan_qty_now,0) plan_qty, 
                        mr.workshop_section routing,
                        pcrl.state			  
                        from production_circulation_record pcr
                        join production_circulation_record_line pcrl on pcrl.id = pcr.now_pcrl
						join product_product pp on pp.id = pcr.product_id
						join product_template pt on pt.id = pp.product_tmpl_id
                        left join mrp_routing mr on mr.id = pcrl.workorder_id and mr.workshop_section is not null
                        where  pcr.now_pcrl is not null),
                    pcr as (select distinct 
                            material_quality,
                            size,
                            routing from pcrl),
                    zz as (select   material_quality,
                            size,
                            routing,
                            sum(pcrl.plan_qty) plan_qty
                            from pcrl
                            where state in ('working','wait_report','wait_qty')
                            group by material_quality,size,routing),
                    inventory as (select  material_quality,
                            size,
                       		routing,
							sum(plan_qty) plan_qty
							from pcrl
						 where state = 'completed'				  
                        group by material_quality,size,routing)
                select row_number() over(order by pcr.material_quality,pcr.size, pcr.routing) as id,
                       pcr.material_quality,
                       pcr.size,
                       pcr.routing,
                       coalesce(zz.plan_qty,0) process_qty,
                       coalesce(i.plan_qty,0) inventory_qty
                       from pcr 
                       left join zz on zz.material_quality = pcr.material_quality and zz.size = pcr.size
                                and zz.routing = pcr.routing
                        left join inventory i on i.material_quality = pcr.material_quality and i.size = pcr.size
                                and i.routing = pcr.routing
                        where coalesce(zz.plan_qty,0) > 0 or  coalesce(i.plan_qty,0) > 0
                    )""")

    @api.depends('material_quality', 'size', 'routing')
    def compute_pcr_line(self):
        for report in self:
            report.pcr_ids = self.env['production.circulation.record'].search([('product_id.material_quality', '=', report.material_quality),
                                                                               ('product_id.size', '=', report.size),
                                                                               ('now_pcrl.workorder_id.workshop_section', '=', report.routing)])

