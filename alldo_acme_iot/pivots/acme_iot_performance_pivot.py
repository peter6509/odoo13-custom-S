# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class cncperformancePivotReport(models.Model):
    _name = 'alldo_acme_iot.cnc_performance'
    _description = "CASTING produce performance Statistics"
    _auto = False


class ProjectPivotanalysisreport(cncperformancePivotReport):
    _name = 'alldo_acme_iot.cnc_performance_report'
    # _order = "iot_date,iot_owner"


    iot_date = fields.Date(string="日期")
    iot_owner = fields.Many2one('hr.employee', string="責任者")
    iot_node = fields.Many2one('maintenance.equipment', string="機台")
    wkorder_id = fields.Many2one('alldo_acme_iot.workorder',string="工單號碼")
    iot_start = fields.Datetime(string="起始時間")
    iot_end = fields.Datetime(string="截止時間")
    product_no = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    total_amount_num = fields.Float(digits=(13, 2), string="生產總量",default=0)
    material_ng_num = fields.Float(digits=(13, 2), string="料不良數", default=0)
    processing_ng_num = fields.Float(digits=(13, 2), string="鑄造不良", default=0)
    std_num = fields.Float(digits=(6, 0), string="標準量")
    performance_rate = fields.Float(digits=(4,2),string="達成率")
    iot_duration = fields.Float(digits=(6,2),string="工時")
    product_num = fields.Float(digits=(6,2),string="產能/H",group_operator="avg")


    # @api.depends('total_amount_num','iot_duration')
    # def _get_productnum(self):
    #     for rec in self:
    #         if rec.iot_duration > 0:
    #            myproductnum = round((rec.total_amount_num/rec.iot_duration),2)
    #         else:
    #            myproductnum = 0
    #         rec.product_num = myproductnum
    #         return myproductnum

    @api.model
    def init(self):
        self.env.cr.execute("""drop function if exists getwkordertot(qcid int) cascade""")
        self.env.cr.execute("""create or replace function getwkordertot(qcid int) returns float as $BODY$
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
            totnum float ;
            qcgoodnum float ;
            pngnum float ;
            mngnum float ;
         BEGIN
           select iot_owner1,order_id,qc_date,coalesce(qc_good_num,0),coalesce(material_ng_num,0),coalesce(processing_ng_num,0) into empid,workorderid,qcdate,qcgoodnum,mngnum,pngnum from alldo_acme_iot_workorder_qc where id = qcid ;
           totnum = qcgoodnum ;
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
           select iot_owner1,order_id,qc_date,total_amount_num into empid,workorderid,qcdate,totamount from alldo_acme_iot_workorder_qc where id = qcid ;
           select sum(coalesce(iot_duration,0)) into tottime from alldo_acme_iot_workorder_iot_data where iot_date::DATE = qcdate::DATE 
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
           select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_acme_iot_workorder_qc where id = qcid ;
           select min(iot_date) into myres from alldo_acme_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate
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
           select iot_owner1,order_id,qc_date into empid,workorderid,qcdate from alldo_acme_iot_workorder_qc where id = qcid ;
           select max(iot_date) into myres from alldo_acme_iot_workorder_iot_data where iot_owner=empid and (iot_date + interval '8 hours')::DATE = qcdate 
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
           prodnum int ;
         BEGIN
           myres = 0 ;
           select order_id into workorderid from alldo_acme_iot_workorder_qc where id = qcid ;
           select product_no,eng_type,prod_num into prodid,engtype,prodnum from alldo_acme_iot_workorder where id = workorderid ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;  
            select mold_id into moldid from product_template where id = prodtmplid ;
            select mold_cavity into moldcavity from alldo_acme_iot_acme_mold where id = moldid ;
           select coalesce(standard_num,0) into stdnum from alldo_acme_iot_eng_order 
              where prod_id=prodtmplid and is_outsourcing is null and standard_num > 0  ;
          /* select getiotduration(qcid) into tottime ; */
           /* nowstdnum = round((stdnum::numeric * tottime::numeric),0) * moldcavity ; */
           /*if stdnum is null then
              stdnum = 0 ;
           end if ;
           nowstdnum = round((stdnum::numeric * tottime::numeric),0) ;*/
           if prodnum > 0 then
              myres = round((prodnum::numeric/stdnum::numeric),0) ;
           else
              myres = 0 ;   
           end if ;
           /* myres = nowstdnum::INTEGER ;*/
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


        # tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""drop materialized view if exists alldo_acme_iot_cnc_performance_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (
           SELECT A.qc_date as iot_date,A.iot_owner1 as iot_owner,A.iot_node as iot_node,(select getstartdate(A.id)) as iot_start,
               (select getenddate(A.id)) as iot_end,A.product_no as product_no,B.eng_type as eng_type,(select getwkordertot(A.id)) as total_amount_num,
               A.processing_ng_num as processing_ng_num,A.material_ng_num as material_ng_num,(select getstdnum(A.id)) as std_num,
               (select getiotduration(A.id)) as iot_duration,(select getprodnum(A.id)) as product_num,
               getperformance(A.id) as performance_rate,A.id as id,B.id as wkorder_id  from alldo_acme_iot_workorder_qc A
                LEFT JOIN alldo_acme_iot_workorder B ON A.order_id = B.id where (select getiotduration(A.id)) > 0
                GROUP BY A.qc_date,A.iot_owner,A.iot_node,A.product_no,B.eng_type,A.id,B.id
        )""" % self._table)

        self._cr.execute("""create index cnc_performance1 on %s (iot_date)""" % self._table)
        self._cr.execute("""create index cnc_performance2 on %s (iot_owner)""" % self._table)
        self._cr.execute("""create index cnc_performance3 on %s (iot_node)""" % self._table)
        self._cr.execute("""create index cnc_performance4 on %s (wkorder_id)""" % self._table)
        self._cr.execute("""create index cnc_performance5 on %s (product_no)""" % self._table)
        self._cr.execute("""create index cnc_performance6 on %s (eng_type)""" % self._table)

        self.env.cr.execute("""drop function if exists getstartdate1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getstartdate1(wkid int) returns timestamp as $BODY$
         DECLARE
           myres timestamp ;
           empid int ;
           workorderid int ;
           qcdate date ;
         BEGIN
           select min(iot_owner1),min(order_id),min(qc_date) into empid,workorderid,qcdate from alldo_acme_iot_workorder_qc where order_id = wkid ;
           select min(iot_date) into myres from alldo_acme_iot_workorder_iot_data where  order_id = workorderid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getenddate1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getenddate1(wkid int) returns timestamp as $BODY$
         DECLARE
           myres timestamp ;
           empid int ;
           workorderid int ;
           qcdate date ;
         BEGIN
           select min(iot_owner1),min(order_id),min(qc_date) into empid,workorderid,qcdate from alldo_acme_iot_workorder_qc where order_id = wkid ;
           select max(iot_date) into myres from alldo_acme_iot_workorder_iot_data where  order_id = workorderid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwkordertot1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getwkordertot1(wkid int) returns float as $BODY$
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
            totnum float ;
            qcgoodnum float ;
            pngnum float ;
            mngnum float ;
         BEGIN
           select min(iot_owner1),min(order_id),min(qc_date),sum(coalesce(qc_good_num,0)),sum(coalesce(material_ng_num,0)),sum(coalesce(processing_ng_num,0)) into empid,workorderid,qcdate,qcgoodnum,mngnum,pngnum from alldo_acme_iot_workorder_qc where order_id = wkid ;
           totnum = qcgoodnum ;
           if totnum is null then
              myres = 0 ;
           else
              myres = totnum ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getiotduration1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getiotduration1(wkid int) returns Float as $BODY$
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
           select min(iot_owner1),min(order_id),min(qc_date),sum(total_amount_num) into empid,workorderid,qcdate,totamount from alldo_acme_iot_workorder_qc where order_id = wkid ;
           select sum(coalesce(iot_duration,0)) into tottime from alldo_acme_iot_workorder_iot_data where order_id = workorderid ;     
           myres = round(tottime::numeric/60::numeric,2) ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getstdnum1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getstdnum1(wkid int) returns INT as $BODY$
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
           prodnum int ;
         BEGIN
           myres = 0 ;
           select order_id into workorderid from alldo_acme_iot_workorder_qc where order_id = wkid ;
           select product_no,eng_type,prod_num into prodid,engtype,prodnum from alldo_acme_iot_workorder where id = wkid ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;  
           select mold_id into moldid from product_template where id = prodtmplid ;
           select mold_cavity into moldcavity from alldo_acme_iot_acme_mold where id = moldid ;
           select coalesce(standard_num,0) into stdnum from alldo_acme_iot_eng_order 
              where prod_id=prodtmplid and is_outsourcing is null and standard_num > 0  ;
           if prodnum > 0 then
              myres = round((prodnum::numeric/stdnum::numeric),0) ;
           else
              myres = 0 ;   
           end if ;
           /* myres = nowstdnum::INTEGER ;*/
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 實際產能
        self.env.cr.execute("""drop function if exists getprodnum1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getprodnum1(wkid int) returns float as $BODY$
         DECLARE
           totnum float ;
           iotduration float ;
           myres float ;
         BEGIN
           select getwkordertot1(wkid) into totnum ;
           select getiotduration1(wkid) into iotduration ;
           if iotduration =0 then
              myres = 0 ;
           else
              myres = round((totnum::numeric/iotduration::numeric),0) ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 生產工單數量的標準工時
        self.env.cr.execute("""drop function if exists getstdtime1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getstdtime1(wkid int) returns float as $BODY$
         DECLARE
           totnum float ;
           prodid int ;
           iotduration float ;
           prodtmplid int ;
           myres float ;
           stdnum int ;
         BEGIN
           select prod_num,product_no into totnum,prodid from alldo_acme_iot_workorder where id = wkid ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;
           select coalesce(standard_num,0) into stdnum from alldo_acme_iot_eng_order 
              where prod_id=prodtmplid and is_outsourcing is null and standard_num > 0  ;
           if stdnum is null then
              myres = 0 ;
           else
              myres = round((totnum::numeric/stdnum::numeric),2) ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getperformance1(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getperformance1(wkid int) returns float as $BODY$
         DECLARE
           prodnum float ;
           totamountnum float ;
           iotduration float ;
           myres float ;
           prodid int ;
           prodtmplid int ;
           stdnum int ;
           stdtotnum int ;
         BEGIN
           select getwkordertot1(wkid) into totamountnum ;
           select getiotduration1(wkid) into iotduration ;
           if iotduration = 0 then
              prodnum = 0 ;
           else   
              select round((totamountnum::numeric/iotduration::numeric),2) into prodnum ;
           end if ;   
           select product_no into prodid from alldo_acme_iot_workorder where id = wkid ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;
           select coalesce(standard_num,0) into stdnum from alldo_acme_iot_eng_order 
              where prod_id=prodtmplid and is_outsourcing is null and standard_num > 0  ;
           if stdnum = 0 then
              myres = 0 ;
           else   
              stdtotnum = round((stdnum::numeric * iotduration::numeric),0) ; 
              if stdtotnum=0 then
                 myres = 0 ;
              else
                 select round((totamountnum::numeric/stdtotnum::numeric)*100,0) into myres ; 
              end if ;   
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""drop materialized view if exists alldo_acme_iot_cnc_performance_report2 cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW alldo_acme_iot_cnc_performance_report2 as (
                   SELECT min(A.qc_date) as iot_date,min(A.iot_owner1) as iot_owner,min(A.iot_node) as iot_node,(select getstartdate1(B.id)) as iot_start,
                       (select getenddate1(B.id)) as iot_end,B.product_no as product_no,B.eng_type as eng_type,(select getwkordertot1(B.id)) as total_amount_num,
                       sum(A.processing_ng_num) as processing_ng_num,sum(A.material_ng_num) as material_ng_num,(select getstdnum1(B.id)) as std_num,
                       (select getiotduration1(B.id)) as iot_duration,(select getprodnum1(B.id)) as prod_num,
                       getperformance1(B.id) as performance_rate,B.id as wkorder_id from alldo_acme_iot_workorder B,alldo_acme_iot_workorder_qc A 
                        where A.order_id = B.id GROUP BY A.order_id,B.id)""" )

        self._cr.execute("""create index cnc_performance11 on alldo_acme_iot_cnc_performance_report2 (iot_date)""")
        self._cr.execute("""create index cnc_performance12 on alldo_acme_iot_cnc_performance_report2 (iot_owner)""")
        self._cr.execute("""create index cnc_performance13 on alldo_acme_iot_cnc_performance_report2 (iot_node)""")
        self._cr.execute("""create index cnc_performance14 on alldo_acme_iot_cnc_performance_report2  (wkorder_id)""")
        self._cr.execute("""create index cnc_performance15 on alldo_acme_iot_cnc_performance_report2  (product_no)""")
        self._cr.execute("""create index cnc_performance16 on alldo_acme_iot_cnc_performance_report2  (eng_type)""")







class scalePivotanalysisreport(cncperformancePivotReport):
    _name = 'alldo_acme_iot.scale_performance_report'
    _order = "item_seq,product_gpid"

    product_no = fields.Many2one('product.product', string="料號")
    scale_weight = fields.Float(digits=(10, 3), string="重量")
    scale_total = fields.Float(digits=(10,3),string="群組總重")
    product_gpid = fields.Integer(string="群組編號")
    item_seq = fields.Integer(string="順序")
    scale_ratio = fields.Float(digits=(6,2),string="比例%",group_operator="avg")
    uom_id = fields.Many2one('uom.uom', string="單位")
    scale_date = fields.Date(string="投料日期")
    day_amount = fields.Float(digits=(10, 0), string="天數")

    def init(self):
        # tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""drop materialized view if exists alldo_acme_iot_scale_performance_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (
                   SELECT A.id as id,A.product_no as product_no,A.scale_weight as scale_weight,A.uom_id as uom_id,A.item_seq as item_seq,
                          A.scale_date as scale_date,A.product_gpid as product_gpid,A.scale_total as scale_total,count(A.id) as day_amount,
                          A.scale_ratio as scale_ratio from alldo_acme_iot_day_scale A
                          GROUP BY A.id,A.product_no,A.uom_id,A.product_gpid,A.scale_date
                          order by A.product_gpid,A.product_no
                )""" % self._table)

        self._cr.execute("""create index scale_performance1 on %s (product_no)""" % self._table)
        self._cr.execute("""create index scale_performance2 on %s (scale_date)""" % self._table)




