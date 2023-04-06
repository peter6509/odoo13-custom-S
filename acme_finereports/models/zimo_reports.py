# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_
from datetime import datetime,timedelta

class zimo_wizard_mrp_pcrl(models.Model):
    _name = "zimo.wizard.mrp.pcrl"
    _description = '''生产单的流转明细'''


    date_start = fields.Date(string='起始日期')
    date_end = fields.Date(string='结束日期')

    def action_to_report(self):
        self.ensure_one()
        date_start = self.date_start
        date_end = self.date_end
        tools.drop_view_if_exists(self._cr,'zimo_report_mrp_pcrl')
        self._cr.execute('''
        create or replace view  zimo_report_mrp_pcrl as (
select --ROW_NUMBER ( ) OVER ( ) AS ID ,
* from (

--根据pcrl查询pcr关联的生产单,罗列当前生产单绑定的 生产单
SELECT 
t0.workorder_id as workorder_id,
t0.plan_qty as plan_qty,
t0.collar_qty as collar_qty,
t0.completed_qty as completed_qty,
t0.worker_workcenter as worker_workcenter,
t0.start_time as  start_time,
t0.completed_time as completed_time,
t0.last_report_time as last_report_time,
t0.workers_team as workers_team,
t0.size as size ,
t0.state as state,

t0.id as id,
t1.id as pcr_id ,
t2.id as pcr_mrp_id ,
-- t3.id as working_mrp_id ,
t2.product_id as product_id,
'绑定在此生产单' as binding_state

from  production_circulation_record_line t0 
left join production_circulation_record t1 on t1.id =t0.line_id 
left join mrp_production t2 on t2.id=t1.production_id  -- pcr 关联
left join mrp_production t3 on t3.id=t0.mrp_id --pclr 关联

where t0.create_date >'2020-01-01'
-- and( t2.id =16552 or t3.id=16552)
and t1.production_id is not null 

union all

--根据pcrl查询pcr关联的生产单,罗列生产过程中绑定的 生产单
SELECT 
t0.workorder_id as workorder_id,
t0.plan_qty as plan_qty,
t0.collar_qty as collar_qty,
t0.completed_qty as completed_qty,
t0.worker_workcenter as worker_workcenter,
t0.start_time as  start_time,
t0.completed_time as completed_time,
t0.last_report_time as last_report_time,
t0.workers_team as workers_team,
t0.size as size ,
t0.state as state,

t0.id as id,
t1.id as pcr_id ,
-- t2.id as pcr_mrp_id ,
t3.id as pcr_mrp_id ,
t3.product_id as product_id,
'未绑定在此生产单' as binding_state

from  production_circulation_record_line t0 
left join production_circulation_record t1 on t1.id =t0.line_id 
left join mrp_production t2 on t2.id=t1.production_id  -- pcr 关联
left join mrp_production t3 on t3.id=t0.mrp_id --pclr 关联

where t0.create_date >'2020-01-01'
and t1.production_id is null 
and t0.mrp_id is not null
) as aa
 where 
 aa.start_time >'%(date_start)s' 
 and aa.start_time < '%(date_end)s' 

        )
        '''%{'date_start': date_start, 'date_end': date_end}
                         )
        return {
            'name': _("生产单明细"+"："+str(date_start)+'至'+str(date_end)),
            'view_mode': 'tree,pivot',
            'res_model': 'zimo.report.mrp.pcrl',
            'type': 'ir.actions.act_window',
        }

class zimo_report_mrp_pcrl(models.Model):
    _name = "zimo.report.mrp.pcrl"
    _auto = False
    _description = '''生产单的流转明细'''

    # pcrl_id = fields.Many2one('production.circulation.record.line')
    pcr_id = fields.Many2one('production.circulation.record','炉号单')
    pcr_mrp_id = fields.Many2one('mrp.production','绑定生产单')
    # working_mrp_id = fields.Many2one('mrp.production','加工时生产单')
    product_id = fields.Many2one('product.product','生产单产品')
    binding_state = fields.Char('绑定关系')

    workorder_id = fields.Many2one('mrp.routing','工序')
    plan_qty = fields.Float('计划数')
    collar_qty = fields.Float('领料数')
    completed_qty = fields.Float('完成数')
    worker_workcenter = fields.Many2one('mrp.workcenter','工位')
    start_time = fields.Datetime(string='开工时间')
    completed_time = fields.Datetime(string='完工时间')
    last_report_time = fields.Datetime(string='汇报时间')
    workers_team = fields.Many2one('zimo.workers.team','班组')
    size = fields.Char('规格')
    state = fields.Char('加工状态')
