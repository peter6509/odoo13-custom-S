---------------------------------------------
--报表: 特种制环产量明细表
SELECT
	t_pcr.NAME AS 炉号,t_pcr.state as 炉号单状态,zm_pp.material_quality as 材质, zm_pp.name as 产品名称,
	t_pcrl.start_time+interval'8 hours' as 开工时间,t_pcrl.completed_time+interval'8 hours' as 完工时间,
	(t_pcrl.completed_time - t_pcrl.start_time ) as 时长,
	round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS 时长分钟,
	t_hr.name  as 班组,t_gw.name  as 工位,t_gx.name as 工序 , t_pcrl.size as 完工规格, --工序  t_pcrl.worker_worker as 操作人员,t_pcrl.worker_workcenter as 工位
	t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
	t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
	t_pcrl.STATE as 明细状态

FROM
	production_circulation_record_line t_pcrl
	LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
	left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id	--pcr关联到视图zimo_view
	left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter	--pcrl关联到mrp_workcenter工位
	left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
	left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
WHERE

	t_pcrl.STATE IN (
	'completed',
	'wait_report')
	and t_pcrl.completed_time+interval'8 hours' >='2018-10-10 00:00:00'
	ORDER BY t_pcrl.size ,t_pcrl.start_time
	limit 10 ;
--end----------------------------------------


---------------------------------------------
--工作中心当前状态
SELECT
	t1.NAME as 设备名称,
	t1.code as 设备编码,
	t1.related_output ,
	t4.name as 灯控编码,
	t1.light_name as 灯控接口,
	t1.STATE as 当前状态,
	t1.routing , t3.name as 工序名称,
	t1.note as 备注,
	t1.pcrl_id ,
	t1.person,t2.name as 操作人员,
	t1.record_tag ,t5.name as 关联单据
FROM
	mrp_workcenter t1
	LEFT JOIN hr_employee t2 ON t2.ID = t1.person --关联人员表
	LEFT JOIN mrp_routing t3 ON t3.ID = t1.routing --关联工序
	LEFT JOIN rfids_output t4 ON t4.ID = t1.related_output --关联输出设备/灯显
	LEFT JOIN record_tag t5 ON t5.ID = t1.record_tag --关联单据标签(注意是单据标签,不是实际单据)
ORDER BY
	person ;
--end----------------------------------------


---------------------------------------------
--递归查询,测试使用
WITH RECURSIVE T ( ID, NAME, circulation_parent, PATH, DEPTH ) AS (
	SELECT ID,NAME,circulation_parent,ARRAY [ ID ] AS PATH,1 AS DEPTH
	FROM
		production_circulation_record
	WHERE
		NAME = '1809002'
	UNION ALL
	SELECT
		D.ID,
		D.NAME,
		D.circulation_parent,
		T.PATH || D.ID,
		T.DEPTH + 1 AS DEPTH
	FROM
		production_circulation_record D
		JOIN T ON D.circulation_parent = T.ID
	)
	SELECT ID,NAME,	circulation_parent,	PATH,DEPTH
FROM T
ORDER BY
	PATH;
--end----------------------------------------


---------------------------------------------
--报表: 在制品汇总表,关于在制品的逻辑算法(1,行明细领汇总减去汇报汇总;2,pcr数减去汇报汇总)两个都不准确
--working状态的数量为0,无法汇总,按领料也不准确
SELECT
	t_pcr.NAME AS 炉号,t_pcr.state as 炉号单状态,zm_pp.material_quality as 材质, zm_pp.name as 产品名称,t_pcr.product_qty as 炉号产品数量,t_gx.name as 工序 ,
-- 	t_pcrl.start_time+interval'8 hours' as 开工时间,t_pcrl.completed_time+interval'8 hours' as 完工时间,
-- 	(t_pcrl.completed_time - t_pcrl.start_time ) as 时长,
-- 	round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS 时长分钟,
-- 	t_hr.name  as 班组,t_gw.name  as 工位,t_gx.name as 工序 , t_pcrl.size as 完工规格, --工序  t_pcrl.worker_worker as 操作人员,t_pcrl.worker_workcenter as 工位
-- 	t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
--   t_pcrl.completed_qty as 报工数量,COALESCE(t_pcrl.discard_qty ,0)as 报废数量,COALESCE(t_pcrl.loss_qty,0) as 损失数
 sum (COALESCE(t_pcrl.collar_qty,0) )as 领料总数,
	sum(t_pcrl.completed_qty) as 报工总数,sum( COALESCE(t_pcrl.discard_qty ,0)) as 报废总数 , sum(COALESCE(t_pcrl.loss_qty,0)) as 损耗总数
	,(sum (COALESCE(t_pcrl.collar_qty,0) ) - sum(COALESCE(t_pcrl.completed_qty,0))  - sum( COALESCE(t_pcrl.discard_qty,0)) - sum(COALESCE(t_pcrl.loss_qty,0)) ) as 待制品数
-- 	t_pcrl.STATE as 明细状态
FROM
	production_circulation_record_line t_pcrl
	LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
	left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id	--pcr关联到视图zimo_view
	left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter	--pcrl关联到mrp_workcenter工位
	left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
	left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
WHERE
-- 1=1 ${if(len(材质)==0,"","and zm_pp.material_quality like '%"+材质+"%'")}
-- and
-- 1=1 ${if(len(工位)==0,"","and t_gw.code like '%"+工位+"%'")}
-- and
-- 1=1 ${if(len(炉号)==0,"","and t_pcr.NAME like '%"+炉号+"%'")}
-- and
t_pcrl.worker_workcenter is not null --工位不能为空,为空表示没作业
GROUP BY t_pcr.NAME,t_pcr.state,zm_pp.material_quality, zm_pp.name ,t_pcr.product_qty,t_gx.id
order by t_pcr.name
;
--end----------------------------------------


---------------------------------------------
--在视图,prcl行中,加工日期,时间长度,工位,工序等信息
--报表:设备 时段内 时间稼动率
SELECT t0.code,t0.name ,t0.state,t1.作业日期,COALESCE(sum(t1.累计时长),0) as 累计时长
,COALESCE(sum(t1.累计时长),0)/(24*60) as 使用比例
from mrp_workcenter t0
left join
zimo_view_pcrl_work_time_long t1 on t1.工位编码=t0.code
where
t1.作业日期 >= '2018-10-28'
AND
t1.作业日期 <= '2018-12-28'
AND
t0.code like '%168%'
group by
t0.code,t0.name ,t0.state,t1.作业日期
order by t1.作业日期
;
--end----------------------------------------


---------------------------------------------
--报表:开机率
select case state
when 'working' then '生产中'
WHEN 'waiting' then '待作业'
end as 状态
, count(*) as 数量 ,count(1)*100/(select count(1) from mrp_workcenter)  as 百分比 from  mrp_workcenter group by state
;
--end----------------------------------------


---------------------------------------------
--效率对比,by teddy
select
			 tt0.炉号,tt0.材质,tt0.工序,tt0.班组 ,tt0.报工数量,tt0.工位编码,tt0.作业日期,tt0.跨日数,tt0.报工数 ,
			 tt0.累计时长,tt0.总时长 ,
			 tt0.每分钟产能 as 实际产能 ,
			 COALESCE(tt1.capacity_per_minute,0) as 计划每分钟产能,
			 (tt0.每分钟产能-COALESCE(tt1.capacity_per_minute,0)) as 实际计划
FROM (
select
			 t0.炉号,t0.材质,t0.pcrid ,t0.工序,t0.工序id, t0.工位id,t0.班组 ,t0.报工数量,t0.工位编码,
			 t0.作业日期,t0.跨日数,((t0.累计时长/t1.总时长)*t0.报工数量) as 报工数 ,
			 t0.累计时长,t1.总时长 ,(t0.报工数量/t1.总时长) as 每分钟产能
from zimo_view_pcrl_work_time_long t0
left join (
					select 炉号,材质,pcrid ,工序id, 工位id,班组,COALESCE(sum(累计时长),0)as 总时长
					from zimo_view_pcrl_work_time_long
					GROUP BY 班组,炉号,材质,pcrid ,工序id, 工位id
					)  t1 on t0.炉号=t1.炉号  and t0.材质=t1.材质  and t0.工序id=t1.工序id  and t0.工位id=t1.工位id  and  t0.pcrid=t1.pcrid  and t0."班组"=t1.班组
where t0.累计时长>0
ORDER BY t1.炉号,t1.材质,t1.pcrid ,t1.工序id, t1.工位id)tt0
left join (
					select t2.material_quality,t0.workcenter_id,t0.routing_id,t0.capacity_per_minute
					from resource_productivity_record t0
					left join product_product t1 on t0.product_id=t1.id
					left join product_template t2 on t1.product_tmpl_id=t2.id
					where t0.type='current'
					) tt1  on tt0.材质=tt1.material_quality and tt0.工序id=tt1.routing_id and tt0.工位id=tt1.workcenter_id
--where (tt0.作业日期>='${作业日期开始}' and tt0.作业日期<='${作业日期结束}' )
--and 1=1 ${if(len(炉号)==0,"","and tt0.炉号 like '%"+炉号+"%'")}
;
--end----------------------------------------


---------------------------------------------

--end----------------------------------------


---------------------------------------------

--end----------------------------------------


---------------------------------------------