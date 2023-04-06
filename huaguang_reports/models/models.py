# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools, _
from datetime import datetime, timedelta
import psycopg2
from odoo.exceptions import UserError



class Zimo_view(models.Model):
    _name = 'zimo.view'
    _auto = False
    _description = "子墨视图,多个视图放在一起,特殊视图再做区分"

    def init(self):
        #tools.drop_view_if_exists(self.env.cr, self._table)
        tools.drop_view_if_exists(self.env.cr, 'zimo_view_pcr_hierarchy')#视图--pcr单据的层次结构
        tools.drop_view_if_exists(self.env.cr, 'zimo_view_product')#视图--产品模板与产品表
        tools.drop_view_if_exists(self.env.cr, 'zimo_view_pcrl_work_time_long')#视图--pcrl加工数据整理表,含跨一日的时间分割
        tools.drop_view_if_exists(self.env.cr, 'zimo_view_pcrl_record')##视图--pcrl信息表
        tools.drop_view_if_exists(self.env.cr,'zimo_view_mrp_workcenter') ##视图,工作中心
        self.env.cr.execute('''
---------------------------------------------
--视图: pcr单据的层次结构
CREATE OR REPLACE VIEW zimo_view_pcr_hierarchy AS (
WITH RECURSIVE T 
(ID, NAME, PARENT_ID, PATH1,path2, DEPTH ,aaa )  AS (
    SELECT ID, NAME, PARENT_ID, 
        ARRAY[name] AS PATH1, 
        ARRAY[name] AS PATH2,
        1 AS DEPTH ,
        COALESCE(' ', name) as aaa -- 用' ' as aaa 还不行
    FROM production_circulation_record
    WHERE PARENT_ID IS NULL

    UNION ALL

    SELECT  D.ID, D.NAME, D.PARENT_ID, 
        T.PATH1 || D.name,
        T.PATH2 ,
        T.DEPTH + 1 AS DEPTH ,
        t.name as aaa
    FROM production_circulation_record D
    JOIN T ON D.PARENT_ID = T.ID
    )
SELECT 
ID, 
NAME,
PARENT_ID as parent_id,aaa as "parent_name" ,
DEPTH as "depth",

(path2)[1] as "first_depth" , -- 取数组中的第一个元素
-- unnest(PATH2),--(这里是拆分成行,由于该数组只有一行,才能这么用
-- (path2)[array_upper(path2, 1)] , --数组中获取最后一个元素的值 ,需要先将数组的上届值或者长度查询出来,然后用长度作为下标来获取数组中的值

PATH1 as "path_info"
FROM T
-- where  name like 'P70195-10101%'
ORDER BY id, DEPTH
);
--end----------------------------------------



---------------------------------------------
--视图:产品表和模板表,方便查询产品名称和属性
--drop view  IF EXISTS zimo_view_product ; --删除视图
CREATE OR REPLACE VIEW zimo_view_product AS (
--列出产品模板,产品,分类 表内容,方便其它表查询引用
SELECT
t_pt.active ,
t_pt.k3_fitemid,
t_categ.name as categ_name,
t_pp.id,
t_pt.NAME,
t_pp.barcode,
t_pt.material_quality,
t_pt.SIZE,
t_pt.uom_id

FROM
product_product t_pp
LEFT JOIN product_template t_pt ON t_pt.ID = t_pp.product_tmpl_id
left join product_category t_categ on t_categ.id=t_pt.categ_id

where t_pt.active = True
);
--end----------------------------------------





---------------------------------------------
--判断 删除视图
--DROP VIEW  IF EXISTS zimo_view_pcrl_work_time_long;
--视图,prcl行中,加工日期,时间长度,工位,工序等信息
--加工日期的算法是以开始时间算
--完工日期跨天数时 分开算
--第1部分 先算没有分开的
--添加pcrid 、工位id、工序id
CREATE OR REPLACE VIEW zimo_view_pcrl_work_time_long AS (
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_team.name as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.start_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours'),t_pcrl.start_time,t_pcrl.completed_time
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
production_circulation_record_line t_pcrl
LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id--pcr关联到视图zimo__view
left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter--pcrl关联到mrp_workcenter工位
left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
left join zimo_workers_team t_team on t_team.id=t_pcrl.workers_team -- 关联 班组
WHERE
t_pcrl.STATE IN ('completed','wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') )=0
-- and t_pcr.name='A31198-07492Q'
-- and date(t_pcrl.start_time + interval'8 hours') >='2018-10-10'
-- and date(t_pcrl.start_time + interval'8 hours') >='2018-12-10'
-- GROUP BY t_gw.name,t_gw.code
-- ORDER BY t_pcrl.size ,t_pcrl.start_time
-- limit 100 ;

UNION ALL

--第2.1部分,算开工日期和完工日期跨1日的情况
--这里列出开工日期当天的
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_team.name as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.start_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours'),t_pcrl.start_time,t_pcrl.completed_time
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
production_circulation_record_line t_pcrl
LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id--pcr关联到视图zimo_view
left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter--pcrl关联到mrp_workcenter工位
left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
left join zimo_workers_team t_team on t_team.id=t_pcrl.workers_team -- 关联 班组
WHERE
t_pcrl.STATE IN ('completed','wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') )=1
and t_pcr.name='A31198-07492Q'
-- and date(t_pcrl.start_time + interval'8 hours') >='2018-10-10'
-- and date(t_pcrl.start_time + interval'8 hours') >='2018-12-10'
-- GROUP BY t_gw.name,t_gw.code
-- ORDER BY t_pcrl.size ,t_pcrl.start_time
-- limit 100 ;

UNION ALL

--第2.2部分,算开工日期和完工日期跨1日的情况
--这里列出完工日期当天的
SELECT
t_pcr.name as 炉号,t_pcr.id as pcrid,zm_pp.material_quality as 材质,t_gx.name as 工序,t_gx.id as 工序Id,t_team.name as 班组,t_pcrl.collar_qty as "领料数量",t_pcrl.feeding_qty as 投料数量,
t_pcrl.completed_qty as 报工数量,t_pcrl.nondefective_qty as 合格品数,t_pcrl.discard_qty as 报废数量,t_pcrl.loss_qty as 损失数,
t_gw.name  as 工位,t_gw.id as 工位ID,t_gw.code as 工位编码,
date(t_pcrl.completed_time + interval'8 hours') as 作业日期,
 date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') as 跨日数,
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC / 60) AS "累计时长" --按分钟算
round(date_part('epoch', t_pcrl.completed_time + interval'8 hours'  -  date_trunc('day', t_pcrl.completed_time + interval'8 hours')  )::NUMERIC / 60) AS "累计时长" --按分钟算
-- round(date_part('epoch',   date_trunc('day', t_pcrl.completed_time + interval'8 hours')    - (t_pcrl.start_time+ interval'8 hours'))::NUMERIC / 60) AS "累计时长" --按分钟算
-- ,date_trunc('day', t_pcrl.completed_time + interval'8 hours')
-- ,t_pcrl.start_time,t_pcrl.completed_time
-- round(date_part('epoch', t_pcrl.completed_time - t_pcrl.start_time)::NUMERIC )/(24*60*60),
FROM
production_circulation_record_line t_pcrl
LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
left join zimo_view_product zm_pp on zm_pp.id = t_pcr.product_id--pcr关联到视图zimo_view
left join mrp_workcenter t_gw on t_gw.id = t_pcrl.worker_workcenter--pcrl关联到mrp_workcenter工位
left join mrp_routing t_gx on t_gx.id = t_gw.routing --mrp_workcenter关联mrp_routing工序
left join hr_employee t_hr on t_hr.id = t_pcrl.worker_worker --pcrl 关联到hr.employee 员工
left join zimo_workers_team t_team on t_team.id=t_pcrl.workers_team -- 关联 班组
WHERE
t_pcrl.STATE IN ('completed','wait_report') and t_pcrl.start_time is not null--状态中只 开工,没有完工或汇报的不算,没有开始过的也不算,开工时间为空的也不算(去掉无效数据)
-- and date(t_pcrl.start_time + interval'8 hours') <> date(t_pcrl.completed_time + interval'8 hours') --开工日期与完工日期在同一天
and( date(t_pcrl.completed_time + interval'8 hours') - date(t_pcrl.start_time + interval'8 hours') ) = 1
);
--end----------------------------------------

---------------------------------------------
--视图,prcl行中,加工日期,时间长度,工位,工序等信息,只是将行明细与其它表关联信息名称等展示,不做运算类
CREATE OR REPLACE VIEW zimo_view_pcrl_record AS (
SELECT
t_pcrl.id as pcrl_id,
t_gx.NAME AS 加工工序 ,t_pcrl.workorder_id as "加工工序id" ,
t_pcr.NAME AS 炉号,--炉号
zm_mrp.name as 加工生产单 ,
t_pcr.STATE AS 炉号单状态,
t_gw.NAME AS 工位,--加工工位
t_pcrl.worker_workcenter as "工位id",
t_bz.NAME AS 班组,--班组
t_bz.id as "班组id",
t_pcrl.start_time + INTERVAL '8 hours' AS 开工时间,
t_pcrl.completed_time + INTERVAL '8 hours' AS 完工时间,--开工日期--完工日期
t_pcrl.duration AS 加工时长,
t_pcrl.last_report_time + INTERVAL '8 hours' AS 汇报时间,--系统中新增了汇报日期
zm_pd1.NAME AS 领料产品名称,
zm_pd1.barcode AS 领料物料代码,
t_pcrl.material_quality AS 领料产品材质,
zm_pd1.SIZE AS 领料规格,t_pcrl.main_material as "领料产品id" ,
t_hr.NAME AS 管理员,t_pcrl.worker_manager as "管理员id" ,
zm_pd2.NAME AS 完工产品名称,
zm_pd2.barcode AS 完工物料代码,
t_pcrl.material_quality AS 完工产品材质,
t_pcrl.SIZE AS 完工规格, t_pcrl.completed_product as "完工产品id" ,
t_pcrl.plan_qty AS 计划数量,
t_pcrl.collar_qty AS "领料数量",
t_pcrl.feeding_qty AS 投料数量,
t_pcrl.completed_qty AS 报工数量,
t_pcrl.nondefective_qty AS 合格品数,
t_pcrl.discard_qty AS 报废数量,
t_pcrl.loss_qty AS 损失数,
t_pcrl.STATE AS 工序明细状态,
t_pcrl.share_state AS 余料分摊状态,
t_pcrl.last_report_size AS 上道汇报规格,
t_pcrl.last_routing_size AS 上道加工规格,
t_pcrl.back_state AS 生产单反写状态 ,
t_pcrl.last_completed AS 最后一批完成
FROM
production_circulation_record_line t_pcrl
LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id --pcrl关联到pcr
LEFT JOIN zimo_view_product zm_pp ON zm_pp.ID = t_pcr.product_id --pcr关联到视图zimo_view
LEFT JOIN mrp_workcenter t_gw ON t_gw.ID = t_pcrl.worker_workcenter --pcrl关联到mrp_workcenter工位
LEFT JOIN mrp_routing t_gx ON t_gx.ID = t_pcrl.workorder_id --pcrl 关联工序mrp_routing
LEFT JOIN hr_employee t_hr ON t_hr.ID = t_pcrl.worker_manager --pcrl 关联到hr.employee 管理员
LEFT JOIN zimo_workers_team t_bz ON t_bz.ID = t_pcrl.workers_team --班组信息
LEFT JOIN zimo_view_product zm_pd1 ON zm_pd1.ID = t_pcrl.main_material --领料产品
LEFT JOIN zimo_view_product zm_pd2 ON zm_pd2.ID = t_pcrl.completed_product --完成产品
left join mrp_production zm_mrp on zm_mrp.id = t_pcrl.mrp_id  --生产单
);
--end----------------------------------------


---------------------------------------------
--视图,工作中心/生产设备清单
CREATE OR REPLACE VIEW zimo_view_mrp_workcenter AS (
SELECT
 t_mwc.id as "设备id" ,
 t_mwc.NAME AS 设备名称,
 t_mwc.address_location AS "车间id",
 tt_mwc.NAME AS 车间名称,
 t_mwc.code AS 设备编码,
 t_mwc.related_output AS "灯控id",
 t_ro.NAME AS 灯控编码,
 t_mwc.light_name AS 灯控接口,
 t_mwc.STATE AS 当前状态,
 t_mwc.routing AS "工序id",
 t_mrt.NAME AS 工序名称,
 t_mwc.note AS 备注,
 t_mwc.pcrl_id AS pcrl_id,
 t_pcrl.start_time AS 最后开工时间,
 t_pcr.NAME AS 炉号单,
 t_team.NAME AS 签到班组,
 t_team2.NAME AS 当前加工班组 
FROM
 mrp_workcenter t_mwc
 LEFT JOIN mrp_routing t_mrt ON t_mrt.ID = t_mwc.routing --关联工序
 LEFT JOIN rfids_output t_ro ON t_ro.ID = t_mwc.related_output --关联输出设备/灯显
 LEFT JOIN mrp_workcenter tt_mwc ON tt_mwc.ID = t_mwc.address_location -- 关联本身,车间
 LEFT JOIN zimo_workers_team t_team ON t_mwc.workers_team = t_team.ID -- 关联班组表
 LEFT JOIN zimo_workers_team t_team2 ON t_mwc.working_workers_team = t_team2.ID --关联班组表
 LEFT JOIN production_circulation_record_line t_pcrl ON t_pcrl.ID = t_mwc.pcrl_id
 LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id 
 );
--end----------------------------------------

''')

