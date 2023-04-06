from datetime import datetime, timedelta
import psycopg2

today = datetime.today()  # .replace#(hour=datetime.today().hour , minute=0, second=0, microsecond=0)

if today.hour >= 7:
    # print(datetime.today().replace(day=datetime.now().day - 1,hour=22, minute=0, second=0, microsecond=0))
    newday = datetime.today() - timedelta(days=1)
    time_value = newday.replace(hour=23, minute=0, second=0, microsecond=0)
else:
    # print(datetime.today().replace(day=datetime.now().day - 2, hour=22, minute=0, second=0, microsecond=0))
    newday = datetime.today() - timedelta(days=2)
    time_value = newday.replace(hour=23, minute=0, second=0, microsecond=0)

sql = '''
DROP VIEW IF 	EXISTS zimo_auto_view_pcrl_by_day_7 ;--删除视图
CREATE 	OR REPLACE VIEW zimo_auto_view_pcrl_by_day_7  AS (
	SELECT
		t_pcrl.ID AS pcrl_id,
		t_gx.NAME AS "加工工序",
		t_pcrl.workorder_id AS "加工工序id",
		t_pcr.NAME AS "炉号",
		zm_mrp.NAME AS "加工生产单",
		t_pcr.STATE AS "炉号单状态",
		t_gw.NAME AS "工位",
		t_pcrl.worker_workcenter AS "工位id",
		t_bz.NAME AS "班组",
		t_bz.ID AS "班组id",
		( t_pcrl.start_time + '08:00:00' :: INTERVAL ) AS "开工时间",
		( t_pcrl.completed_time + '08:00:00' :: INTERVAL ) AS "完工时间",
		t_pcrl.duration AS "加工时长",
		( t_pcrl.last_report_time + '08:00:00' :: INTERVAL ) AS "汇报时间",
		zm_pt1.NAME AS "领料产品名称",
		zm_pd1.barcode AS "领料物料代码",
		zm_pt1.material_quality AS "领料产品材质",
		zm_pt1.SIZE AS "领料规格",
		t_pcrl.main_material AS "领料产品id",
		t_hr.NAME AS "管理员",
		t_pcrl.worker_manager AS "管理员id",
		zm_pt2.NAME AS "完工产品名称",
		zm_pd2.barcode AS "完工物料代码",
		zm_pt2.material_quality AS "完工产品材质",
		t_pcrl.SIZE AS "完工规格",
		t_pcrl.completed_product AS "完工产品id",
		t_pcrl.plan_qty AS "计划数量",
		t_pcrl.collar_qty AS "领料数量",
		t_pcrl.feeding_qty AS "投料数量",
		t_pcrl.completed_qty AS "报工数量",
		t_pcrl.nondefective_qty AS "合格品数",
		t_pcrl.discard_qty AS "报废数量",
		t_pcrl.loss_qty AS "损失数",
		t_pcrl.STATE AS "工序明细状态",
		t_pcrl.share_state AS "余料分摊状态",
		t_pcrl.back_state AS "生产单反写状态",
		t_pcrl.last_completed AS "最后一批完成"
	FROM
		production_circulation_record_line t_pcrl
		LEFT JOIN production_circulation_record t_pcr ON t_pcr.ID = t_pcrl.line_id
		LEFT JOIN mrp_workcenter t_gw ON t_gw.ID = t_pcrl.worker_workcenter
		LEFT JOIN mrp_routing t_gx ON t_gx.ID = t_pcrl.workorder_id
		LEFT JOIN hr_employee t_hr ON t_hr.ID = t_pcrl.worker_manager
		LEFT JOIN zimo_workers_team t_bz ON t_bz.ID = t_pcrl.workers_team
		LEFT JOIN product_product zm_pd1 ON zm_pd1.ID = t_pcrl.main_material
		LEFT JOIN product_template zm_pt1 ON zm_pt1.ID = zm_pd1.product_tmpl_id
		LEFT JOIN product_product zm_pd2 ON zm_pd2.ID = t_pcrl.completed_product
		LEFT JOIN product_template zm_pt2 ON zm_pt2.ID = zm_pd2.product_tmpl_id
		LEFT JOIN mrp_production zm_mrp ON zm_mrp.ID = t_pcrl.mrp_id
	WHERE
		( t_pcrl.start_time >= '%s')--::timestamp without time zone)

	) ''' % (time_value)

# print(sql)
#
conn = psycopg2.connect(database="huaguang", user="odoo", password="odoo", host="10.18.1.51", port="5432")
cur = conn.cursor()
try:
    # 正常的操作
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
except:
    # 发生异常，执行这块代码
    print(str(time_value), "sql执行异常!")
else:
    # 如果没有异常执行这块代码
    print(str(time_value), "数据已更新!")
