---------------------------------------------
--视图:产品表和模板表,方便查询产品名称和属性
drop view  IF EXISTS zimo_view_product ; --删除视图
CREATE OR REPLACE VIEW zimo_view_product AS (
SELECT
	t_pp.id,
	t_pt.NAME,
	t_pp.barcode,
	t_pt.material_quality,
	t_pt.SIZE,
	t_pt.uom_id
FROM
	product_product t_pp
	LEFT JOIN product_template t_pt ON t_pt.ID = t_pp.product_tmpl_id
	);
--end----------------------------------------



---------------------------------------------
--判断 删除视图
DROP VIEW  IF EXISTS zimo_view_pcrl_work_time_long;
--视图,prcl行中,加工日期,时间长度,工位,工序等信息
--加工日期的算法是以开始时间算
--完工日期跨天数时 分开算
--第1部分 先算没有分开的
--添加pcrid 、工位id、工序id
CREATE OR REPLACE VIEW zimo_view_pcrl_work_time_long AS (
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_hr.name  as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
	t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.start_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours'),t_pcrl.start_time,t_pcrl.completed_time
-- 	round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
	production_circulation_record_line t_pcrl
	LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
	left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id	--pcr关联到视图zimo__view
	left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter	--pcrl关联到mrp_workcenter工位
	left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
	left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
WHERE
	t_pcrl.STATE IN (	'completed',	'wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- 	and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
	and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') )=0
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-10-10'
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-12-10'
-- 	GROUP BY t_gw.name,t_gw.code
-- 	ORDER BY t_pcrl.size ,t_pcrl.start_time
-- 	limit 100 ;

UNION ALL

--第2.1部分,算开工日期和完工日期跨1日的情况
--这里列出开工日期当天的
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_hr.name  as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
	t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.start_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours'),t_pcrl.start_time,t_pcrl.completed_time
-- 	round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
	production_circulation_record_line t_pcrl
	LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
	left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id	--pcr关联到视图zimo_view
	left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter	--pcrl关联到mrp_workcenter工位
	left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
	left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
WHERE
	t_pcrl.STATE IN (	'completed',	'wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- 	and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
	and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') )=1
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-10-10'
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-12-10'
-- 	GROUP BY t_gw.name,t_gw.code
-- 	ORDER BY t_pcrl.size ,t_pcrl.start_time
-- 	limit 100 ;

UNION ALL

--第2.2部分,算开工日期和完工日期跨1日的情况
--这里列出完工日期当天的
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_hr.name  as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
	t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.completed_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
round(date_part('epoch', t_pcrl.completed_time + interval'8 hours'  -  date_trunc('day', t_pcrl.completed_time + interval'8 hours')  )::NUMERIC / 60) AS "累计时长" --按分钟算
-- round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours')
-- ,t_pcrl.start_time,t_pcrl.completed_time
-- 	round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
	production_circulation_record_line t_pcrl
	LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
	left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id	--pcr关联到视图zimo_view
	left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter	--pcrl关联到mrp_workcenter工位
	left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
	left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
WHERE
	t_pcrl.STATE IN (	'completed',	'wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- 	and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
	and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') ) = 1
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-10-10'
-- 	and date(t_pcrl.start_time + interval'8 hours') >='2018-12-10'
-- 	GROUP BY t_gw.name,t_gw.code
-- 	ORDER BY t_pcrl.size ,t_pcrl.start_time
-- 	limit 100 ;
);
--end----------------------------------------