# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_


class zimo_pcr_process_line_report(models.Model):
    _name = "zimo.pcr.process.line.report"
    _auto = False
    _description = '''生产单明细报表'''

    mo_name = fields.Char('任务单号')
    barcode = fields.Char('物料编码')
    product = fields.Char('物料名称')
    pcr_name = fields.Char('炉号')
    jy_state = fields.Char('挤压状态')
    jy_qty = fields.Float('挤压领料重量')
    ls_state = fields.Char('拉丝状态')
    ls_qty = fields.Float('拉丝汇报重量')
    cx_state = fields.Char('成型状态')
    cx_qty = fields.Float('成型汇报重量')
    db_qty = fields.Float('待包入库汇报重量')

    def init(self):
        tools.drop_view_if_exists(self._cr, 'zimo_pcr_process_line_report')
        self._cr.execute("""
            create or replace view  zimo_pcr_process_line_report as (
                with pcr as (select pp.barcode,pt.name product,mp.name mo_name,
							 pcr.name pcr_name,pcr.id,fcxsb from mrp_production mp 
                                join product_product pp on pp.id= mp.product_id
                                join product_template pt on pt.id = pp.product_tmpl_id
                                left join production_circulation_record pcr on pcr.production_id = mp.id
							 --筛选条件成型设备
							 	where fcxsb in '%(fcxsb)s'),                                
                        pcrl as (select line_id,start_time,completed_time + interval '8H' completed_time,
								 plan_qty,completed_qty,state,mr.name routing,
                                        last_completed
                                        from  production_circulation_record_line pcrl
                                        join mrp_routing mr on mr.id = pcrl.workorder_id),
                        jy_qty as (select line_id,max(start_time) start_time,max(completed_time)completed_time,
								   max(plan_qty) plan_qty from pcrl
                                    where routing = '08挤压'
                                    group by line_id),
                        jy_state as (select distinct pcrl.line_id,last_completed from pcrl
                                     join jy_qty on pcrl.start_time = jy_qty.start_time and pcrl.line_id = jy_qty.line_id
                                    where routing = '08挤压'),
                        ls_qty as (select line_id,max(start_time) start_time,max(completed_time)completed_time,
								   sum(completed_qty) completed_qty from pcrl
                                    where routing in ('10通用拉丝', '11特种拉丝')
                                    group by line_id),
                        ls_state as (select distinct pcrl.line_id,last_completed from pcrl
                                     join ls_qty on pcrl.start_time = ls_qty.start_time and pcrl.line_id = ls_qty.line_id
                                    where routing in ('10通用拉丝', '11特种拉丝')),
                        cx_qty as (select line_id,max(start_time) start_time,
								   sum(completed_qty) completed_qty from pcrl
                                    where routing = '14特种制环'
                                    group by line_id),
                        cx_state as (select distinct pcrl.line_id,last_completed from pcrl
                                     join ls_qty on pcrl.start_time = ls_qty.start_time and pcrl.line_id = ls_qty.line_id
                                    where routing in ('14特种制环','13通用制环','12矫直','16综合组')),
                        db_qty as (select line_id, sum(completed_qty) db_qty from pcrl
                                    where routing in ('25盘丝', '47检成', '24机检', '49挑棒') and last_completed = 't'
                                    group by line_id),
						pcr_ids as (select distinct line_id 
						from pcrl
						--筛选条件	日期 工艺		
						where routing in '%(routing)s'
								   and 
								 completed_time >= '%(date_start)s'
								 and 
								completed_time <= '%(date_end)s' )	
						--		   
                        select pcr_ids.line_id as id,	
                                mo_name, --任务单号
	                            pcr_name, --炉号
                                product, --物料名称
                                barcode, --物料编码
								jy_qty.completed_time jy_completed_time, --挤压完工时间
                                case 
                                when jy_state.last_completed = 't'
                                then '挤压完工'
                                when jy_state.last_completed = 'f'
                                then '挤压中'
                                else '未挤压' end jy_state, --挤压状态
                                plan_qty jy_qty, --挤压领料重量
                                case 
                                when ls_state.last_completed = 't'
                                then '拉丝完工'
                                when ls_state.last_completed = 'f'
                                then '拉丝中'
                                else '未拉丝' end ls_state, --拉丝状态
								ls_qty.completed_time ls_completed_time,
                                ls_qty.completed_qty ls_qty, --拉丝汇报重量
								fcxsb, --成型设备
                                case 
                                when cx_state.last_completed = 't'
                                then '成型完工'
                                when cx_state.last_completed = 'f'
                                then '成型中'
                                else '未成型' end cx_state, --成型状态
                                cx_qty.completed_qty cx_qty, --成型汇报重量
                                db_qty --待包入库汇报重量
                                from pcr_ids
								join pcr on pcr_ids.line_id = pcr.id
                            left join jy_qty on jy_qty.line_id = pcr.id
                            left join jy_state on jy_state.line_id = pcr.id
                            left join ls_qty on ls_qty.line_id = pcr.id
                            left join ls_state on ls_state.line_id = pcr.id
                            left join cx_qty on cx_qty.line_id = pcr.id
                            left join cx_state on cx_state.line_id = pcr.id
                            left join db_qty on db_qty.line_id = pcr.id
                            order by mo_name
                )""")

    @api.depends('material_quality', 'size', 'routing')
    def compute_pcr_line(self):
        for report in self:

            if report.routing == '光锭':
                routing = ('02浇铸','03连铸','05抛丸','06锯锭','09清洗（4#1F）')
            elif report.routing == '预成型丝':
                routing = ('08挤压', '10通用拉丝', '11特种拉丝', '21清洗（4#2F）')
            elif report.routing == '特种制环':
                routing = ('14特种制环')
            else:
                routing = ( '12矫直', '13通用制环', '14特种制环', '19通用碎环', '20特种碎环', '22清洗（3#2F）', '23检半',
             '24机检', '25盘丝', '45清洗（4#3F）', '47检成', '48检平', '49挑棒')

            pcr_ids = self.env['production.circulation.record'].search([('product_id.material_quality', '=', report.material_quality),
                                                                        ('product_id.size', '=', report.size),
                                                                        ('now_pcrl.workorder_id.name', 'in', routing)])

            report.pcr_ids = pcr_ids