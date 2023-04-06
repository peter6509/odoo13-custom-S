# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class cncperformancePivotReport(models.Model):
    _name = 'alldo_ipla_iot.cnc_performance'
    _description = "CASTING produce performance Statistics"
    _auto = False


class ProjectPivotanalysisreport(cncperformancePivotReport):
    _name = 'alldo_ipla_iot.cnc_performance_report'
    # _order = "iot_date,iot_owner"


    iot_date = fields.Date(string="日期")
    iot_owner = fields.Many2one('hr.employee', string="責任者")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    wkorder_id = fields.Many2one('alldo_ipla_iot.workorder',string="工單號碼")
    iot_start = fields.Datetime(string="起始時間")
    iot_end = fields.Datetime(string="截止時間")
    product_no = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    total_amount_num = fields.Float(digits=(13, 2), string="生產量",default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="料不良數", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="工不良數", default=0)
    std_num = fields.Float(digits=(6, 0), string="標準量")
    performance_rate = fields.Float(digits=(4,2),string="達成率")
    iot_duration = fields.Float(digits=(6,2),string="工時")
    product_num = fields.Float(digits=(6,0),string="產能/H")

    def init(self):
        self.env.cr.execute("""drop function if exists getwkordertot(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getwkordertot(qcid int) returns int as $BODY$
         DECLARE 
            empid int;
            workorderid int ;
            qcdate date ;
            startdate timestamp ;
            enddate timestamp ;
            prodid int ;
            engtype varchar ;
            prodtmplid int ;
            myres int ;
            htime int;
            mtime int;
            totnum int ;
         BEGIN
           select iot_owner1,order_id,qc_date,total_amount_num into empid,workorderid,qcdate,totnum from alldo_ipla_iot_workorder_qc where id = qcid ;
           if totnum is null then
              myres = 0 ;
           else
              myres = totnum ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getiotduration(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getiotduration(qcid int) returns Float as $BODY$
          DECLARE
            empid int;
            workorderid int ;
            qcdate date ;
            startdate timestamp ;
            enddate timestamp ;
            prodid int ;
            engtype varchar ;
            prodtmplid int ;
            myres float ;
            htime int;
            mtime int;
            tottime float ;
            avg_duration float ;
            ncount int ;
            totamount float;
            reptot float ;
            reptoth float ;
          BEGIN
           select iot_owner1,order_id,qc_date,total_amount_num into empid,workorderid,qcdate,totamount from alldo_ipla_iot_workorder_qc where id = qcid ;
           select sum(coalesce(iot_duration,0)) into tottime from alldo_ipla_iot_workorder_iot_data where (iot_date::timestamp + interval '8 hours')::DATE = qcdate::DATE 
                 and order_id = workorderid ;     
 
           myres = round((tottime::numeric/60::numeric),2) ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getstartdate(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getstartdate(qcid int) returns timestamp as $BODY$
         DECLARE
           myres timestamp ;
           empid int ;
           workorderid int ;
           qcdate date ;
         BEGIN
           select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_ipla_iot_workorder_qc where id = qcid ;
           select min(iot_date) into myres from alldo_ipla_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
               and order_id = workorderid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getenddate(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getenddate(qcid int) returns timestamp as $BODY$
         DECLARE
           myres timestamp ;
           empid int ;
           workorderid int ;
           qcdate date ;
         BEGIN
           select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_ipla_iot_workorder_qc where id = qcid ;
           select max(iot_date) into myres from alldo_ipla_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate 
             and order_id = workorderid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getstdnum(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getstdnum(qcid int) returns INT as $BODY$
         DECLARE
           myres int ;
           prodid int ;
           prodtmplid int ;
           engtype varchar ;
           stdnum int ;
           nowstdnum float ;
           tottime float ;
           tottime1 float ;
           workorderid int ;
           moldcavity int ;
           moldid int ;
         BEGIN
           select order_id into workorderid from alldo_ipla_iot_workorder_qc where id = qcid ;
           select product_no,eng_type into prodid,engtype from alldo_ipla_iot_workorder where id = workorderid ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;  
            select mold_id into moldid from product_template where id = prodtmplid ;
            select mold_cavity into moldcavity from alldo_ipla_iot_ipla_mold where id = moldid ;
           select coalesce(standard_num,0) into stdnum from alldo_ipla_iot_eng_order where prod_id=prodtmplid and eng_type= engtype ;
           select getiotduration(qcid) into tottime ; 
           /* nowstdnum = round((stdnum::numeric * tottime::numeric),0) * moldcavity ; */
           nowstdnum = round((stdnum::numeric * tottime::numeric),0) ;
           myres = nowstdnum::INTEGER ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getperformance(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getperformance(qcid int) returns float as $BODY$
         DECLARE
           prodnum float ;
           stdnum float ;
           totamountnum float ;
           iotduration float ;
           myres float ;
         BEGIN
           select getwkordertot(qcid) into totamountnum ;
           select getiotduration(qcid) into iotduration ;
           if iotduration = 0 then
              prodnum = 0 ;
           else   
              select round((totamountnum::numeric/iotduration::numeric),2) into prodnum ;
           end if ;   
           select getstdnum(qcid) into stdnum ;
           if stdnum = 0 then
              myres = 0 ;
           else   
              select round((totamountnum::numeric/stdnum::numeric),2) into myres ; 
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodnum(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getprodnum(qcid int) returns float as $BODY$
         DECLARE
           totnum float ;
           iotduration float ;
           myres float ;
         BEGIN
           select getwkordertot(qcid) into totnum ;
           select getiotduration(qcid) into iotduration ;
           if iotduration =0 then
              myres = 0 ;
           else
              myres = round((totnum::numeric/iotduration::numeric),2) ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")



        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
           SELECT A.qc_date as iot_date,A.iot_owner1 as iot_owner,A.iot_node as iot_node,(select getstartdate(A.id)) as iot_start,
               (select getenddate(A.id)) as iot_end,A.product_no as product_no,B.eng_type as eng_type,(select getwkordertot(A.id)) as total_amount_num,
               A.processing_ng_num as processing_ng_num,A.material_ng_num as material_ng_num,(select getstdnum(A.id)) as std_num,
               (select getiotduration(A.id)) as iot_duration,getprodnum(A.id) as product_num,
               getperformance(A.id) as performance_rate,A.id as id,B.id as wkorder_id  from alldo_ipla_iot_workorder_qc A
                LEFT JOIN alldo_ipla_iot_workorder B ON A.order_id = B.id
                GROUP BY A.qc_date,A.iot_owner,A.iot_node,A.product_no,B.eng_type,A.id,B.id
        )""" % self._table)



