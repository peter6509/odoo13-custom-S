# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class cncperformancePivotReport(models.Model):
    _name = 'alldo_gh_iot.cnc_performance'
    _description = "CNC produce performance Statistics"
    _auto = False


class ProjectPivotanalysisreport(cncperformancePivotReport):
    _name = 'alldo_gh_iot.cnc_performance_report'
    # _order = "iot_date,iot_owner"


    iot_date = fields.Date(string="日期")
    iot_owner = fields.Many2one('hr.employee', string="責任者")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    wkorder_id = fields.Many2one('alldo_gh_iot.workorder',string="工單號碼")
    iot_start = fields.Datetime(string="起始時間")
    iot_end = fields.Datetime(string="截止時間")
    product_no = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    total_amount_num = fields.Float(digits=(13, 2), string="生產量",default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="料不良數", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="工不良數", default=0)
    std_num = fields.Float(digits=(10, 2), string="標準量")
    performance_rate = fields.Float(digits=(10,4),string="達成率")
    iot_duration = fields.Float(digits=(6,2),string="工時")
    product_num = fields.Float(digits=(6,0),string="產能/H")

    # def init(self):
    #     self.env.cr.execute("""drop function if exists getwkordertot(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getwkordertot(qcid int) returns int as $BODY$
    #      DECLARE
    #         empid int;
    #         workorderid int ;
    #         qcdate date ;
    #         startdate timestamp ;
    #         enddate timestamp ;
    #         prodid int ;
    #         engtype varchar ;
    #         prodtmplid int ;
    #         myres int ;
    #         htime int;
    #         mtime int;
    #         totnum int ;
    #      BEGIN
    #        select iot_owner1,order_id,qc_date,total_amount_num into empid,workorderid,qcdate,totnum from alldo_gh_iot_workorder_qc where id = qcid ;
    #        select sum(iot_num) into totnum from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date::timestamp + interval '8 hours')::DATE = qcdate::DATE
    #              and order_id = workorderid ;
    #        if totnum is null then
    #           myres = 0 ;
    #        else
    #           myres = totnum ;
    #        end if ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getiotduration1(iot_start timestamp,iot_end timestamp) cascade""")
    #     self.env.cr.execute("""create or replace function getiotduration1(iot_start timestamp,iot_end timestamp) returns Float as $BODY$
    #      DECLARE
    #        myres float ;
    #        time1 timestamp ;
    #        time2 timestamp ;
    #        durtime float ;
    #        date1 date ;
    #        wktype char ;
    #        fixnum float ;
    #        hr int ;
    #        min int ;
    #      BEGIN
    #        select iot_start::DATE into date1 ;
    #        select concat(date1::TEXT,' 00:00:00')::timestamp into time1 ;
    #        select concat(date1::TEXT,' 09:00:00')::timestamp into time2 ;
    #        select age(iot_end,iot_start) into durtime ;
    #        select date_part('hours',age(iot_end,iot_start))::INTEGER into hr ;
    #        select date_part('minutes',age(iot_end,iot_start))::INTEGER into min ;
    #        durtime = hr * 60 + min ;
    #        if iot_start >= time1 and iot_start <= time2 then
    #           wktype = '1' ;
    #           fixnum = 60 ;
    #        else
    #           wktype = '2' ;
    #           fixnum = 30 ;
    #        end if ;
    #        if durtime >= 240 then
    #           durtime = durtime - fixnum ;
    #        end if ;
    #        myres = round(durtime::numeric/60::numeric,2) ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;
    #      """)
    #
    #
    #     self.env.cr.execute("""drop function if exists getiotduration(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getiotduration(qcid int) returns Float as $BODY$
    #       DECLARE
    #         date1 date ;
    #         empid int;
    #         workorderid int ;
    #         qcdate date ;
    #         startdate timestamp ;
    #         enddate timestamp ;
    #         prodid int ;
    #         engtype varchar ;
    #         prodtmplid int ;
    #         myres float ;
    #         htime int;
    #         mtime int;
    #         tottime float ;
    #         avg_duration float ;
    #         ncount int ;
    #         totamount float;
    #         reptot float ;
    #         reptoth float ;
    #         time1 timestamp ;
    #         time2 timestamp ;
    #         durtime float ;
    #         iot_start timestamp ;
    #         iot_end timestamp ;
    #          wktype char ;
    #          fixnum float ;
    #          hr int ;
    #          min int ;
    #       BEGIN
    #        select getstartdate(qcid) into iot_start ;
    #        select getenddate(qcid) into iot_end ;
    #        select iot_owner1,order_id,qc_date,total_amount_num into empid,workorderid,qcdate,totamount from alldo_gh_iot_workorder_qc where id = qcid ;
    #        select qcdate::DATE into date1 ;
    #        select qcdate::DATE::timestamp into time1 ;
    #        select time1 + interval '9 hours' into time2 ;
    #        /* select concat(date1::TEXT,' 00:00:00')::timestamp into time1 ;
    #        select concat(date1::TEXT,' 09:00:00')::timestamp into time2 ; */
    #        select date_part('hours',age(iot_end,iot_start))::INTEGER into hr ;
    #        select date_part('minutes',age(iot_end,iot_start))::INTEGER into min ;
    #        durtime = hr * 60 + min ;
    #        if iot_start >= time1 and iot_start <= time2 then
    #           wktype = '1' ;
    #           fixnum = 60 ;
    #        else
    #           wktype = '2' ;
    #           fixnum = 30 ;
    #        end if ;
    #        if durtime >= 240 then
    #           durtime = durtime - fixnum ;
    #        end if ;
    #        myres = round(durtime::numeric/60::numeric,2) ;
    #        return myres ;
    #       END;$BODY$
    #       LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getstartdate(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getstartdate(qcid int) returns timestamp as $BODY$
    #      DECLARE
    #        myres timestamp ;
    #        empid int ;
    #        workorderid int ;
    #        qcdate date ;
    #        minid int ;
    #        minid1 int ;
    #        ncount int ;
    #        ncount1 int ;
    #      BEGIN
    #        select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_gh_iot_workorder_qc where id = qcid ;
    #        select count(*) into ncount from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #            and order_id = workorderid and iot_num=0 ;
    #        if ncount > 0 then
    #            select min(id) into minid from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #                and order_id = workorderid and iot_num=0 ;
    #            select min(id) into minid1 from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #                and order_id = workorderid and id > minid ;
    #        else
    #            select min(id) into minid1 from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #                and order_id = workorderid ;
    #        end if ;
    #        /* select min(iot_date) into myres from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #            and order_id = workorderid ; */
    #        select count(*) into ncount1 from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate and
    #             order_id = workorderid ;
    #        if ncount1 > 2 then
    #           select min(iot_date) into myres from alldo_gh_iot_workorder_iot_data where id=minid1 ;
    #        else
    #           select min(iot_date) into myres from alldo_gh_iot_workorder_iot_data where id=minid ;
    #        end if ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getenddate(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getenddate(qcid int) returns timestamp as $BODY$
    #      DECLARE
    #        myres timestamp ;
    #        empid int ;
    #        workorderid int ;
    #        qcdate date ;
    #      BEGIN
    #        select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_gh_iot_workorder_qc where id = qcid ;
    #        select max(iot_date) into myres from alldo_gh_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
    #          and order_id = workorderid ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getstdnum(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getstdnum(qcid int) returns float as $BODY$
    #      DECLARE
    #        myres float ;
    #        prodid int ;
    #        prodtmplid int ;
    #        engtype varchar ;
    #        stdnum int ;
    #        nowstdnum float ;
    #        tottime float ;
    #        tottime1 float ;
    #        workorderid int ;
    #        moldcavity int ;
    #      BEGIN
    #        select order_id into workorderid from alldo_gh_iot_workorder_qc where id = qcid ;
    #        select product_no,eng_type into prodid,engtype from alldo_gh_iot_workorder where id = workorderid ;
    #        select product_tmpl_id into prodtmplid from product_product where id = prodid ;
    #        select coalesce(standard_num,0),coalesce(mold_cavity,1) into stdnum,moldcavity from alldo_gh_iot_eng_order where prod_id=prodtmplid and eng_type= engtype ;
    #        select getiotduration(qcid) into tottime ;
    #        nowstdnum = round((stdnum::numeric * tottime::numeric),2) ;
    #        myres = nowstdnum ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getperformance(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getperformance(qcid int) returns float as $BODY$
    #      DECLARE
    #        prodnum float ;
    #        stdnum float ;
    #        totamountnum float ;
    #        iotduration float ;
    #        myres float ;
    #      BEGIN
    #        select getwkordertot(qcid) into totamountnum ;
    #        select getiotduration(qcid) into iotduration ;
    #        if iotduration = 0 then
    #           prodnum = 0 ;
    #        else
    #           select round((totamountnum::numeric/iotduration::numeric),2) into prodnum ;
    #        end if ;
    #        select getstdnum(qcid) into stdnum ;
    #        if stdnum = 0 then
    #           myres = 0 ;
    #        else
    #           /* select round((prodnum::numeric/stdnum::numeric),2) into myres ; */
    #           select round((totamountnum::numeric/stdnum::numeric),4) into myres ;
    #        end if ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #     self.env.cr.execute("""drop function if exists getprodnum(qcid int) cascade""")
    #     self.env.cr.execute("""create or replace function getprodnum(qcid int) returns float as $BODY$
    #      DECLARE
    #        totnum float ;
    #        iotduration float ;
    #        myres float ;
    #      BEGIN
    #        /* select total_amount_num into totnum from alldo_gh_iot_workorder_qc where id = qcid ; */
    #        select getwkordertot(qcid) into totnum ;
    #        select getiotduration(qcid) into iotduration ;
    #        if iotduration =0 then
    #           myres = 0 ;
    #        else
    #           myres = round((totnum::numeric/iotduration::numeric),2) ;
    #        end if ;
    #        return myres ;
    #      END;$BODY$
    #      LANGUAGE plpgsql;""")
    #
    #
    #
    #     # self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
    #     #    SELECT A.qc_date as iot_date,A.iot_owner1 as iot_owner,A.iot_node as iot_node,(select getstartdate(A.id)) as iot_start,
    #     #        (select getenddate(A.id)) as iot_end,A.product_no as product_no,B.eng_type as eng_type,(select getwkordertot(A.id)) as total_amount_num,
    #     #        A.processing_ng_num as processing_ng_num,A.material_ng_num as material_ng_num,(select getstdnum(A.id)) as std_num,
    #     #        (select getiotduration(A.id)) as iot_duration,getprodnum(A.id) as product_num,
    #     #        getperformance(A.id) as performance_rate,A.id as id,B.id as wkorder_id  from alldo_gh_iot_workorder_qc A
    #     #         LEFT JOIN alldo_gh_iot_workorder B ON A.order_id = B.id
    #     #        where B.state in ('4','5') and (select getwkordertot(A.id)) > 0
    #     #         GROUP BY A.qc_date,A.iot_owner,A.iot_node,A.product_no,B.eng_type,A.id,B.id
    #     # )""" % self._table)
    #
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
    #                SELECT A.qc_date as iot_date,A.iot_owner1 as iot_owner,A.iot_node as iot_node,(select getstartdate(A.id)) as iot_start,
    #                    (select getenddate(A.id)) as iot_end,A.product_no as product_no,B.eng_type as eng_type,(select getwkordertot(A.id)) as total_amount_num,
    #                    A.processing_ng_num as processing_ng_num,A.material_ng_num as material_ng_num,(select getstdnum(A.id)) as std_num,
    #                    (select getiotduration(A.id)) as iot_duration,(select getprodnum(A.id)) as product_num,
    #                    (select getperformance(A.id)) as performance_rate,A.id as id,B.id as wkorder_id from alldo_gh_iot_workorder_qc A
    #                     LEFT JOIN alldo_gh_iot_workorder B ON A.order_id = B.id
    #                     GROUP BY A.qc_date,A.iot_owner,A.iot_node,A.product_no,B.eng_type,A.id,B.id
    #             )""" % self._table)
    #
    #     self.env.cr.execute("""create or replace view gh_supplierinfo_product as select S.name,S.min_qty,S.price,T.default_code,P.id as product_id from product_supplierinfo S left join
    #         product_template T on S.product_tmpl_id = T.id left join product_product P on P.product_tmpl_id=T.id ;""")
    #
    #     # self.env.cr.execute("""drop MATERIALIZED view alldo_gh_iot_cnc_performance_report cascade""")
    #     # self.env.cr.execute("""CREATE MATERIALIZED VIEW alldo_gh_iot_cnc_performance_report as (
    #     #                    SELECT A.qc_date as iot_date,A.iot_owner1 as iot_owner,A.iot_node as iot_node,(select getstartdate(A.id)) as iot_start,
    #     #                        (select getenddate(A.id)) as iot_end,A.product_no as product_no,B.eng_type as eng_type,(select getwkordertot(A.id)) as total_amount_num,
    #     #                        A.processing_ng_num as processing_ng_num,A.material_ng_num as material_ng_num,(select getstdnum(A.id)) as std_num,
    #     #                        (select getiotduration(A.id)) as iot_duration,getprodnum(A.id) as product_num,
    #     #                        getperformance(A.id) as performance_rate,A.id as id,B.id as wkorder_id  from alldo_gh_iot_workorder_qc A
    #     #                         LEFT JOIN alldo_gh_iot_workorder B ON A.order_id = B.id
    #     #                         GROUP BY A.qc_date,A.iot_owner,A.iot_node,A.product_no,B.eng_type,A.id,B.id
    #     #                 )""")
    #     # self.env.cr.execute("""create index cnc_per1 on alldo_gh_iot_cnc_performance_report (iot_owner)""")
    #     # self.env.cr.execute("""create index cnc_per2 on alldo_gh_iot_cnc_performance_report (iot_date)""")
    #     # self.env.cr.execute("""create index cnc_per3 on alldo_gh_iot_cnc_performance_report (product_no)""")
    #     # self.env.cr.execute("""create index cnc_per4 on alldo_gh_iot_cnc_performance_report (iot_node)""")
    #     #
    #     # self.env.cr.execute("""refresh materialized view alldo_gh_iot_cnc_performance_report""")
    #
