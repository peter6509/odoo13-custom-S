# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools,_



class ProductionSummaryReport(models.Model):
    _name = "production.summary.new.report"
    _description = '''生产汇总表（新）'''

    workcenter = fields.Char('成型设备')
    date_in = fields.Date('入库日期')
    material_quality = fields.Char('品种')
    cx_size = fields.Char('成型规格')
    pcr_id = fields.Many2one('production.circulation.record','炉号')
    rl_collar_qty_amount = fields.Float("熔炼投料重量")
    rl_completed_qty_amount = fields.Float("熔炼完工重量")
    jy_completed_qty_amount = fields.Float("薄带挤压薄带完工重量")
    xc_completed_qty_amount = fields.Float("薄带铣床完工重量")
    ls_completed_qty_amount = fields.Float("拉丝完工重量")
    bz_qty_amount = fields.Float("小包装入库重量")
    ls_rate = fields.Char("拉丝成材率")
    all_finished_in = fields.Char("炉号成品率")
    note = fields.Char("备注")

    @api.model
    def _create_report(self,date_start,date_end,material_quality,size_wizard):
        mark = str(material_quality) if material_quality else ''
        size = str(size_wizard) if size_wizard else ''

        sql = """
                with pcr as (
        
                    select
                        pcr.id,
                        pcr.name,
                        pt.material_quality,
                        b.name parent_name,
                        pcr.top_parent,
                        t.last_report_time,
                        mp.stp_002  workcenter
                        from production_circulation_record pcr
                        left join product_product pp on pcr.product_id = pp.id
                        left join production_circulation_record b on b.id = pcr.parent_id and pcr.parent_id is not null
                        left join product_template pt on pt.id = pp.product_tmpl_id
                        left join mrp_production mp on mp.id = pcr.production_id
                        join (select distinct pcrl.line_id,
                                max(pcrl.last_report_time + interval '8H') last_report_time
                                FROM  production_circulation_record_line pcrl
                                join production_circulation_record pcr on pcrl.line_id = pcr.id
                                join mrp_routing mr on mr.id = pcrl.workorder_id
                                where pcrl.state = 'completed' and pcrl.last_completed = 'true'
                                and mr.routing_type = 'db'
                                group by pcrl.line_id) t on t.line_id = pcr.id
                    where pcr.state != 'draft'
                        and pcr.create_date >= '2022-07-01 00:00:01'
                        and date(t.last_report_time) >= '{}'
                        and date(t.last_report_time) <= '{}'
                        and pt.material_quality ilike '%{}%'
                        -- and pcr.id not in (select distinct pcr_id from production_summary_new_report) 
                    ),
                    pcrl as (select line_id,size,collar_qty,pcr.top_parent,completed_qty,
                             mr.routing_type,mr.name routing,last_completed,plan_qty
                             from production_circulation_record_line pcrl
                             join mrp_routing mr on mr.id = pcrl.workorder_id
                             join pcr on pcrl.line_id = pcr.id
                    where pcrl.state = 'completed'
                          and date(pcrl.last_report_time) >= '2022-07-01'),
        
                   rl as
                        (SELECT distinct pcrl.line_id,--炉号单
                        pcrl.size rl_size,
                        routing,
                        sum(coalesce(computer_collar,0)) rl_collar_qty_amount,
                        sum(coalesce(completed_qty,0)) rl_completed_qty_amount,
                        case when sum(coalesce(computer_collar,0)) > 0 and sum(coalesce(completed_qty,0)) > 0
                        then sum(completed_qty) / sum(computer_collar) * 100
                        else 0 end rl_rate
                        FROM pcrl
                        where routing_type = 'rl'
                        group by pcrl.line_id,pcrl.size,routing),
                   ls as      -- 拉丝数据查询
                        (SELECT distinct pcrl.line_id,--炉号单
                        sum(coalesce(completed_qty,0)) ls_completed_qty_amount
                        FROM pcrl
                        where routing_type = 'ls' and last_completed = 't'
                        group by pcrl.line_id),                        
                   jy as      --薄带挤压数据查询
                        (SELECT distinct pcrl.line_id,--炉号单
                        max(coalesce(plan_qty,0)) jy_collar_qty_amount,
                        sum(coalesce(completed_qty,0)) jy_completed_qty_amount
                        FROM pcrl
                        where routing ilike '%薄带挤压%'
                        group by pcrl.line_id),                        
                   xc as      --铣床数据查询
                        (SELECT distinct pcrl.line_id,--炉号单
                        sum(coalesce(completed_qty,0)) xc_completed_qty_amount
                        FROM pcrl
                        where routing ilike '%铣床%'
                        group by pcrl.line_id),
                   bz as      --包装数据查询
                        (sELECT distinct pcrl.line_id,
                                pcrl.size cx_size,
                        sum(coalesce(completed_qty,0)) bz_qty_amount
                        FROM  pcrl
                        where pcrl.last_completed = 't'
                        and routing_type = 'db'
                        group by pcrl.line_id,pcrl.size),
        
                        bz_size_all as --包装按规格汇总
                                    (select distinct case when top_parent is not null
                                            then top_parent
                                            else line_id end line_id,
                                            bz.cx_size,
                                            sum(bz_qty_amount) bz_qty_total
                                        from bz
                                        join pcr on pcr.id = line_id
                                        group by
                                        case when top_parent is not null
                                            then top_parent
                                            else line_id end, cx_size),
                        bz_f as	--bz是否有最后一批未完成的
                                (select distinct * from
                                 (select distinct case when top_parent is not null
                                                 then top_parent
                                                 else line_id end line_id,
                                                 last_completed
                                            from pcrl
                                            where last_completed = 'f' and routing_type = 'db'
                                 union all
                                 select distinct line_id,
                                                 last_completed
                                            from pcrl
                                            where last_completed = 'f' and routing_type = 'db'
                                            and top_parent is not null) a
                                ),
                        bz_e_f as	--bz是否有最后一批未完成的
                                (select distinct line_id,
                                                 last_completed
                                            from pcrl
                                            where last_completed = 'f' and routing_type = 'db'),
                        bz_all as  --包装不按规格合计
                                    (select line_id,
                                            sum(bz_qty_total) bz_all_qty_total
                                        from bz_size_all
                                        group by line_id)
                        select  pcr.material_quality, --品种
                                date(pcr.last_report_time) date_in, --成品入库时间
                                pcr.id pcr_id, --炉号                               
                                rl.rl_size, --熔炼规格
                                rl_collar_qty_amount, --熔炼投料重量
                                rl_completed_qty_amount, --熔炼完工重量
                                case when rl_rate is not null
                                then CAST(rl_rate as DECIMAL(20,2)) || '%'
                                else null end rl_rate,--熔炼成材率
                                jy_completed_qty_amount, --挤压完工重量
                                ls_completed_qty_amount, --拉丝完工重量
                                xc_completed_qty_amount, --铣床完工重量
                                bz_qty_amount, --包装重量
                                case when coalesce(jy_collar_qty_amount,0) > 0 and coalesce(ls_completed_qty_amount) > 0
                                then CAST(ls_completed_qty_amount / jy_collar_qty_amount * 100 as DECIMAL(20,2)) || '%'
                                else null end ls_rate, --拉丝成材率
                                pcr.workcenter, --成型设备
                                bz.cx_size, --成型规格                
                                case
                                when bz_f.last_completed = 'f'
                                then '*'
                                when coalesce(rl_collar_qty_amount,0) > 0 and coalesce(bz_all_qty_total) > 0
                                and pcr.top_parent is null
                                then CAST(bz_all_qty_total / rl_collar_qty_amount * 100 as DECIMAL(10,2)) || '%'
                                when pcr.top_parent is null and (coalesce(rl_collar_qty_amount,0) = 0 or coalesce(bz_all_qty_total) = 0)
                                then null
                                else '+' end all_finished_in --成品率
                                from pcr
                                left join rl on rl.line_id = pcr.id
                                left join ls on ls.line_id = pcr.id
                                left join jy on jy.line_id = pcr.id
                                left join xc on xc.line_id = pcr.id
                                left join bz on bz.line_id = pcr.id
                                left join bz_size_all on bz_size_all.line_id = pcr.id and bz_size_all.cx_size = bz.cx_size
                                left join bz_all on bz_all.line_id = pcr.id
                                left join bz_f on bz_f.line_id = pcr.id
                                left join bz_e_f on bz_e_f.line_id = pcr.id
                                where bz.cx_size ilike '%{}%' 
                                order by pcr.name
                """.format(date_start,date_end,mark,size)

        ##先删除结果
        self.env.cr.execute('delete from production_summary_new_report ;')
        ##先删除结果

        self.env.cr.execute(sql)
        # print('------------*********----------------\n',sql)
        dicts = self.env.cr.dictfetchall()
        # print(len(dicts),'009988')
        if not dicts:
            return
        for dict in dicts:
            self.create({'workcenter': dict['workcenter'],
                         'date_in': dict['date_in'],
                         'material_quality': dict['material_quality'],
                         'cx_size': dict['cx_size'],
                         'pcr_id': dict['pcr_id'],
                         'rl_collar_qty_amount': dict['rl_collar_qty_amount'],
                         'rl_completed_qty_amount': dict['rl_completed_qty_amount'],
                         'jy_completed_qty_amount': dict['jy_completed_qty_amount'],
                         'xc_completed_qty_amount': dict['xc_completed_qty_amount'],
                         'ls_completed_qty_amount': dict['ls_completed_qty_amount'],
                         'bz_qty_amount': dict['bz_qty_amount'],
                         'ls_rate': dict['ls_rate'],
                         'all_finished_in': dict['all_finished_in'],
                         })
        return True







