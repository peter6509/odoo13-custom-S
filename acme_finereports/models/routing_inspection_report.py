# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_
from datetime import datetime,timedelta
from odoo.exceptions import UserError
import operator




class routing_inspection_report(models.Model):
    _name = "routing.inspection.report"
    _auto = False
    _description = '''品质巡检报表'''


    pcr_id = fields.Many2one('production.circulation.record', '炉号')
    material_quality = fields.Char('品种')
    product_qty = fields.Float('重量')
    size = fields.Char('规格')
    product_id = fields.Many2one('product.product','产品')
    person_id = fields.Many2one('hr.employee', '人员')
    date = fields.Datetime('时间')
    qc_state = fields.Selection([
        ('合格', '合格'),
        ('不合格', '不合格')], string='合格状态')
    unqualified_remarks = fields.Many2one('unqualified.remarks',string='不合格描述')
    results = fields.Selection([
        ('is_pending','待处理'),
        ('accept','接收'),
        ('concession','让步接收'),
        ('scrap','报废'),
    ],string='处理方式')
    duty_routing = fields.Many2one('mrp.routing', '责任工序')
    discover_routing = fields.Many2one('mrp.routing', '发现工序')


    def init(self):
        tools.drop_view_if_exists(self._cr, 'routing_inspection_report')
        self._cr.execute("""
                CREATE or REPLACE view routing_inspection_report AS (
                    select 
                        pq.id,   
                        pq.pcr_id, --炉号
					    pt.material_quality, --品种
						pcr.product_qty, --重量
						pt.size, --规格
						pcr.product_id, --产品
                        pq.processing_person person_id,  --巡检人员
						pq.date, --时间
						case 
						when pq.results is null
						then ''
						when pq.results = 'accept'
						then '合格'
						else '不合格' end qc_state, --质检状态
						pq.results, --处理方式
						pq.duty_routing, --责任工序
                       	pq.discover_routing, --发现工序
                        pq.unqualified_remarks --不合格描述
                        from pcr_qc pq
                     	join production_circulation_record pcr
                        on pcr.id = pq.pcr_id 
                        join product_product pp on pp.id = pcr.product_id
                        join product_template pt on pt.id = pp.product_tmpl_id
                        where pq.type = 'inspection'
			    )""" )

