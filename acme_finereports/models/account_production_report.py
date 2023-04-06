# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_
from datetime import datetime,timedelta
from odoo.exceptions import UserError
import operator


OPERATORS = {
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '=': operator.eq,
    '!=': operator.ne
}


class AccountProductionReport(models.Model):
    _name = "account.production.report"
    _auto = False
    _description = '''炉号成品率报表'''

    line_id = fields.Many2one('production.circulation.record', '炉号')
    material_quality = fields.Char('完工产品名称')
    size = fields.Char('完工规格')
    routing = fields.Char('工序')
    completed_time = fields.Datetime('入库时间')
    material_size = fields.Char("领料规格")
    rl_collar_qty = fields.Float("投料重量")
    plan_qty = fields.Float("领料重量")
    completed_qty = fields.Float("完工重量")
    duration = fields.Float("生产工时")
    cc_rate = fields.Char("成材率", )
    cp_rate = fields.Char("成品率")

    def init(self):
        tools.drop_view_if_exists(self._cr, 'account_production_report')
        self._cr.execute("""
            create or replace view  account_production_report as (
                  with pcrl as (select pcrl.line_id,pt.material_quality,mr.name routing,pcrl.size,
    			  		 pcr.top_parent, mt.size material_size,pcr.name,
                         sum(coalesce(pcrl.collar_qty,0)) collar_qty,
                         sum(coalesce(pcrl.completed_qty,0)) completed_qty,
    			  		 max(coalesce(pcrl.plan_qty,0)) plan_qty,
                         max(pcrl.last_report_time) completed_time,
                         case when sum(coalesce(pcrl.completed_qty,0)) > 0 and max(coalesce(pcrl.plan_qty,0)) > 0
    					 then sum(coalesce(pcrl.completed_qty,0)) / max(coalesce(pcrl.plan_qty,0))
    					 else 0 end cc_rate,
                         cast(sum(coalesce(pcrl.duration,0)) / 60 as DECIMAL(10,4)) duration
                         from production_circulation_record_line pcrl
                                join production_circulation_record pcr on pcr.id =pcrl.line_id
                                join product_product pp on pcr.product_id = pp.id 
                                join product_template pt on pt.id = pp.product_tmpl_id
                                left join product_product mp on pcrl.main_material = mp.id 
                                left join product_template mt on mt.id = mp.product_tmpl_id
                                join mrp_routing mr on mr.id = pcrl.workorder_id
                                where pcrl.state = 'completed'
                                group by pcrl.line_id,pt.material_quality,mr.name,pcrl.size,pcr.name,
                                     pcr.top_parent, mt.size),
                    rl as (select distinct pcrl.line_id,sum(pcrl.collar_qty) rl_collar_qty
                           from pcrl where pcrl.routing in ('02浇铸','03连铸') group by line_id),
    				un_cx_child as (select case when top_parent is null 
    							 			then line_id 
    							 			else top_parent end line_id,
    										top_parent,
    										routing,
    							 			sum(completed_qty) completed_qty,
    										case when sum(completed_qty) > 0 and sum(plan_qty) > 0
    							 				 then sum(completed_qty) / sum(plan_qty)
    							 				 else 0 end cc_rate,sum(duration) duration
    										from pcrl where pcrl.top_parent is not null and
    							   routing not in ('47检成', '24机检', '25盘丝', '49挑棒')
    							   group by case when top_parent is null 
    							 			then line_id 
    							 			else top_parent end,
    										top_parent,routing), --非成型工艺				
    				cx_child as (select case when top_parent is null 
    							 			then line_id 
    							 			else top_parent end line_id,
    							 			sum(completed_qty) completed_qty,
    							 			case when sum(completed_qty) > 0 and sum(plan_qty) > 0
    							 				 then sum(completed_qty) / sum(plan_qty)
    							 				 else 0 end cc_rate,
    							 			sum(duration) duration 
    							 from pcrl 
    							 where routing in ('47检成', '24机检', '25盘丝', '49挑棒')
    							 group by case when top_parent is null 
    							 			then line_id 
    							 			else top_parent end),
    				 f_uncx as (select distinct 
    							case when pcr.top_parent is null
    							then pcrl.line_id
    							else pcr.top_parent end line_id,
    							mr.name routing,
    							pcrl.last_completed from production_circulation_record_line pcrl
    							join production_circulation_record pcr on pcr.id =pcrl.line_id
    							join mrp_routing mr on mr.id = pcrl.workorder_id and 
    							mr.name not in  ('47检成', '24机检', '25盘丝', '49挑棒')
    							join product_product pp on pcr.product_id = pp.id 
    							join product_template pt on pt.id = pp.product_tmpl_id
    							where pcrl.state = 'completed' and pcrl.last_completed = 'f'),
    					f_cx as (select distinct 
    							case when pcr.top_parent is null
    							then pcrl.line_id
    							else pcr.top_parent end line_id,
    							pcrl.last_completed from production_circulation_record_line pcrl
    							join production_circulation_record pcr on pcr.id =pcrl.line_id
    							join mrp_routing mr on mr.id = pcrl.workorder_id and 
    							mr.name in  ('47检成', '24机检', '25盘丝', '49挑棒')
    							join product_product pp on pcr.product_id = pp.id 
    							join product_template pt on pt.id = pp.product_tmpl_id
    							where pcrl.state = 'completed' and pcrl.last_completed = 'f')
    					select row_number() over() as id,
    					        c.material_quality,
    							c.size,
    							c.routing,
    							c.completed_time,
    							c.line_id,
    							c.material_size,
    	                        coalesce(d.rl_collar_qty,0) rl_collar_qty,
    							c.plan_qty,
    							c.completed_qty,
    							case when e.last_completed = 'f' or f.last_completed = 'f'
    								 then '*'
    								 when a.cc_rate is null and b.cc_rate is null and c.top_parent is null 
    								 and e.last_completed is null and f.last_completed is null
    								 then CAST(c.cc_rate * 100 as DECIMAL(10,2))  || '%'
    								 when a.cc_rate is not null and c.top_parent is null 
    								 and e.last_completed is null and f.last_completed is null
    								 then CAST(a.cc_rate * 100 as DECIMAL(10,2)) || '%'
    						    	 when b.cc_rate is not null and c.top_parent is null
    								 and e.last_completed is null and f.last_completed is null
    								 then CAST(b.cc_rate * 100 as DECIMAL(10,2))  || '%'
    								 else '+' end cc_rate,	--成材率							 
    							case when f.last_completed = 'f'
    								 then '*' --未完成
    								 when c.routing in ('47检成', '24机检', '25盘丝', '49挑棒') and c.top_parent is null
    								 and coalesce (d.rl_collar_qty,0) > 0 and coalesce(b.completed_qty,0) > 0
    								 and f.last_completed is null
    						     	 then CAST(coalesce(b.completed_qty,0) / coalesce (d.rl_collar_qty,0)
    										   * 100 as DECIMAL(10,2))  || '%' 
    								 when c.routing not in ('47检成', '24机检', '25盘丝', '49挑棒')
    								 or (coalesce (d.rl_collar_qty,0) = 0 and coalesce(b.completed_qty,0) = 0
    								 and c.routing in ('47检成', '24机检', '25盘丝', '49挑棒') and c.top_parent is null
    								 and f.last_completed is null)
    								 then null
    								 else '+' end cp_rate, --成品率
    							case when a.duration is not null and c.top_parent is null
    								 then a.duration
    								 when b.duration is not null and c.top_parent is null
    								 then b.duration
    								 else c.duration end duration
    							from pcrl c
    							left join un_cx_child a on a.line_id = c.line_id and a.routing = c.routing
    							left join cx_child b on b.line_id = c.line_id and c.routing in 
    							('47检成', '24机检', '25盘丝', '49挑棒')						
    							left join rl d on d.line_id = c.line_id
    							left join f_uncx e on e.line_id = case when c.top_parent is null
    																   then c.line_id
    																   else c.top_parent end
    													and c.routing = e.routing
    							left join f_cx f on f.line_id = case when c.top_parent is null
    																   then c.line_id
    																   else c.top_parent end
    												and c.routing in ('47检成', '24机检', '25盘丝', '49挑棒')
    			    )""")




    # def compute_child_ids(self):
    #     for pcr in self:
    #         if pcr.routing not in ('47检成', '24机检', '25盘丝', '49挑棒'):
    #             child_ids = self.env['account.production.report'].search([('line_id.parent_id', '=', pcr.line_id.id),
    #                                                                       ('routing', '=', pcr.routing)])
    #             report_ids = self.env['account.production.report']
    #             while child_ids:
    #                 report_ids += child_ids
    #                 child_ids = self.env['account.production.report'].search([('line_id.parent_id', 'in', child_ids.ids),
    #                                                                           ('routing', '=', pcr.routing)])
    #
    #         else:
    #             child_ids = self.env['account.production.report'].search([('line_id.parent_id', '=', pcr.line_id.id),
    #                                                                       ('routing', 'in', ('47检成', '24机检', '25盘丝', '49挑棒'))])
    #             report_ids = self.env['account.production.report']
    #             while child_ids:
    #                 report_ids += child_ids
    #                 child_ids = self.env['account.production.report'].search([('line_id.parent_id', 'in', child_ids.ids),
    #                                                                           ('routing', 'in', ('47检成', '24机检', '25盘丝', '49挑棒'))])
    #         pcr.child_ids = report_ids
    #
    # @api.depends('line_id.all_record_line_ids', 'child_ids', 'line_id')
    # def _compute_qty(self):
    #     for report in self:
    #         all_record_line_ids = report.line_id.all_record_line_ids.filtered(lambda r: r.state == 'completed'
    #                                                                              and r.workorder_id.name == report.routing)
    #         un_record_line_ids = all_record_line_ids.filtered(
    #             lambda c: not c.last_completed)
    #         last_record_line_ids = all_record_line_ids.filtered(
    #             lambda c:  c.last_completed)
    #         cx_all_record_line_ids = report.line_id.all_record_line_ids.filtered(lambda r: r.workorder_id.name in
    #                                                                                        ('47检成', '24机检', '25盘丝','49挑棒')
    #                                                                                         and r.state == 'completed')
    #         un_cx_record_line_ids = cx_all_record_line_ids.filtered(
    #             lambda c: not c.last_completed)
    #         cx_record_line_ids = cx_all_record_line_ids.filtered(
    #             lambda c: c.last_completed)
    #         #无分单
    #         if not report.line_id.child_ids and not report.line_id.parent_id:
    #             report.sum_duration = report.duration
    #             #非成型工艺成品率
    #             if report.routing not in ('47检成', '24机检', '25盘丝', '49挑棒'):
    #                 report.cp_rate = False
    #             else:
    #             #成型成品率
    #                 if report.completed_qty > 0 and report.rl_collar_qty > 0 and not un_record_line_ids\
    #                         and last_record_line_ids:
    #                     report.cp_rate = str(format(report.completed_qty / report.rl_collar_qty * 100, ".2f")) + '%'
    #                 else:
    #                     report.cp_rate = False
    #             #成材率
    #             if report.completed_qty > 0 and report.plan_qty > 0 and not un_record_line_ids\
    #                         and last_record_line_ids:
    #                 report.cc_rate = str(format(report.completed_qty / report.plan_qty * 100, ".2f")) + '%'
    #             else:
    #                 report.cc_rate = False
    #         #有分单
    #         else:
    #             parent_id = report.line_id.parent_id
    #             #母单
    #             if report.child_ids and not parent_id:
    #                 report.sum_duration = report.duration + sum(report.child_ids.mapped('duration'))
    #                 for line in report.child_ids:
    #                     line.sum_duration = line.duration
    #                 completed_qty = report.completed_qty + sum(report.child_ids.mapped('completed_qty'))
    #                 plan_qty = report.plan_qty + sum(report.child_ids.mapped('plan_qty'))
    #                 #非成型
    #                 if report.routing not in ('47检成', '24机检', '25盘丝', '49挑棒'):
    #                     report.cp_rate = False
    #                     for line in report.child_ids:
    #                         line.cp_rate = False
    #
    #                     if not un_record_line_ids and last_record_line_ids:
    #                         for line in report.child_ids:
    #                             line.cc_rate = '+'
    #                         if completed_qty > 0 and plan_qty > 0:
    #                             report.cc_rate = str(
    #                                 format(completed_qty / plan_qty * 100, ".2f")) + '%'
    #                         else:
    #                             report.cc_rate = '0'
    #                     elif un_record_line_ids:
    #                         report.cc_rate = '*'
    #                         for line in report.child_ids:
    #                             line.cc_rate = '*'
    #                 #成型
    #                 else:
    #                     if un_cx_record_line_ids:
    #                         report.cp_rate = '*'
    #                         report.cc_rate = '*'
    #                         for line in report.child_ids:
    #                             line.cp_rate = '*'
    #                             line.cc_rate = '*'
    #                     elif not un_cx_record_line_ids and cx_record_line_ids:
    #                         if completed_qty > 0 and report.rl_collar_qty > 0:
    #                             report.cp_rate = str(format(completed_qty / report.rl_collar_qty * 100, ".2f")) + '%'
    #                         else:
    #                             report.cp_rate = '0'
    #                         if completed_qty > 0 and plan_qty > 0 and not un_record_line_ids \
    #                                 and last_record_line_ids:
    #                             report.cc_rate = str(format(completed_qty / plan_qty * 100, ".2f")) + '%'
    #                         else:
    #                             report.cc_rate = '0'
    #                         for line in report.child_ids:
    #                             line.cp_rate = '+'
    #                             line.cc_rate = '+'



                # if all_record_line_ids.filtered(lambda r: r.completed_qty):
                #     report.completed_qty = sum(all_record_line_ids.filtered(lambda r: r.completed_qty).mapped("completed_qty"))
                # else:
                #     report.completed_qty = 0
                # if not parent_id and not report.line_id.child_ids:
                #     if not all_record_line_ids:
                #         if report.routing not in ('47检成', '24机检', '25盘丝', '49挑棒'):
                #             report.cc_rate = '*'
                #             report.cp_rate = '*'
                #     else:
                #         ids = []
                #         for line in all_record_line_ids:
                #             ids.append(line.line_id.id)
                #         line_ids = list(set(ids))
                #         reports = self.env["account.production.report"].search([('line_id', 'in', line_ids)])
                #         if un_record_line_ids:
                #             if reports:
                #                 for line in reports:
                #                     line.cc_rate = '*'
                #                     line.cp_rate = '*'
                #         elif not un_record_line_ids and last_record_line_ids:
                #             if reports:
                #                 child_reports = reports.filtered(lambda r: r.line_id != report.line_id)
                #                 if child_reports:
                #                     for line in child_reports:
                #                         line.cc_rate = '+'
                #                         line.cp_rate = '+'
                #             #成材率
                #             if report.completed_qty > 0 and report.plan_qty > 0:
                #                 report.cc_rate = str(format(report.completed_qty / report.plan_qty * 100, ".2f")) + '%'
                #             else:
                #                 report.cc_rate = False
                #             #成品率
                #             if report.routing in ('47检成', '24机检', '25盘丝', '49挑棒'):
                #                 if report.completed_qty > 0 and report.rl_collar_qty > 0:
                #                     report.cp_rate = str(format(report.completed_qty / report.rl_collar_qty * 100, ".2f")) + '%'
                #                 else:
                #                     report.cp_rate = False
                #             else:
                #                 report.cp_rate = False


