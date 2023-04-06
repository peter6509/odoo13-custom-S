# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,tools
from odoo.exceptions import UserError

class ACMEFineReportView(models.Model):
    _name = "alldo_acme_iot.finereport_view"
    _description = "FineReport View"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getdevstatus(mystatus varchar) cascade""")
        self._cr.execute("""create or replace function getdevstatus(mystatus varchar) returns varchar as $BODY$
         DECLARE
           myres varchar ;
         BEGIN
           if mystatus='1' then
              myres = '架模' ;
           elsif mystatus='2' then
              myres = '開工' ;
           elsif mystatus='3' then
              myres = '烘模' ;
           else
              myres = '停機';
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getdevtype(mytype varchar) cascade""")
        self._cr.execute("""create or replace function getdevtype(mytype varchar) returns varchar as $BODY$
         DECLARE
           myres varchar ;
         BEGIN
           if mytype='1' then
              myres = '鑄件' ;
           elsif mytype='2' then
              myres = '熔爐' ;
           elsif mytype='3' then
              myres = '加工機' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geniotdurtime(equid int) cascade""")
        self._cr.execute("""create or replace function geniotduration(equid int) returns Float as $BODY$
         DECLARE
           nowdt timestamp;
           sdt timestamp ;
           totdur float ;
           ddur int ;
           hdur int ;
           mdur int ; 
         BEGIN
           select current_timestamp into nowdt ;
           select iot_start_datetime into sdt from maintenance_equipment where id = equid ;
           if sdt is not null then
              select date_part('day',age(nowdt,sdt))::INT into ddur ;
              select date_part('hour',age(nowdt,sdt))::INT into ddur ;
              select date_part('minute',age(nowdt,sdt))::INT into mdur ;
              totdur = 24 * coalesce(ddur,0) + coalesce(ddur,0) + round(coalesce(mdur,0)/60,2) ;
           else
              totdur = 0 ;
           end if ;
           return totdur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getiotowner(equipid int) cascade""")
        self._cr.execute("""create or replace function getiotowner(equipid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           ownid1 int ;
           ownid2 int ;
           owner1 varchar ;
           owner2 varchar ;
         BEGIN
           select iot_owner,iot_owner1 into ownid1,ownid2 from maintenance_equipment where id = equipid ;
           if ownid1 is not null then
              select name into owner1 from hr_employee where id = ownid1 ;
           else
              owner1='' ;
           end if ;
           if ownid2 is not null then
              select name into owner2 from hr_employee where id = ownid2 ;
           else
              owner2='' ;
           end if ;
           if owner1 is not null then
              myres = concat(owner1,',',coalesce(owner2,' ')) ;
           else
              myres = coalesce(owner2,' ') ;
           end if ;
           return myres ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getstatusnum(iotstatus varchar) cascade""")
        self._cr.execute("""create or replace function getstatusnum(iotstatus varchar) returns INT as $BODY$
         DECLARE
           myres int ;
         BEGIN
           select count(*) into myres from maintenance_equipment where iot_status=iotstatus and active=True and category_id=2 ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getstatusper(iotstatus varchar) cascade""")
        self._cr.execute("""create or replace function getstatusper(iotstatus varchar) returns Float as $BODY$
         DECLARE
           myres float ;
           snum int ;
           tot int ;
         BEGIN
           select count(*) into snum from maintenance_equipment where iot_status=iotstatus and active=True and category_id=2 ;
           select count(*) into tot from maintenance_equipment where  active=True and category_id=2 ;
           myres = round((snum::numeric/tot::numeric)*100,0);
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getequtodaynum(moid int) cascade""")
        self._cr.execute("""create or replace function getequtodaynum(moid int) returns INT as $BODY$
         DECLARE
           myres int ;
           mytoday date ;
           nowdt timestamp ;
           nowdt1 timestamp ;
         BEGIN
           /* select now() into mytoday ; */
           select max(iot_date::DATE) into mytoday from alldo_acme_iot_workorder_iot_data ; 
           select concat(mytoday::TEXT,' 00:00:00')::timestamp - interval '8 hour' into nowdt ;
           select concat(mytoday::TEXT,' 16:00:00')::timestamp  into nowdt1 ; 
           select sum(iot_num) into myres from alldo_acme_iot_workorder_iot_data where order_id=moid and iot_date >= nowdt and iot_date < nowdt1 ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getequreplqceline(moid int) cascade""")
        self._cr.execute("""create or replace function getequreplqceline(moid int) returns INT as $BODY$
         DECLARE
           myres INT ;
         BEGIN
           select sum(replace_duration) into myres from alldo_acme_iot_wkorder_replaceline where order_id=moid;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists get_report2_stdnum(moid int) cascade""")
        self._cr.execute("""create or replace function get_report2_stdnum(moid int) returns float as $BODY$
         DECLARE
           myres float ;
           iotdate date ;
         BEGIN
           select max(iot_date) into iotdate from alldo_acme_iot_cnc_performance_report2 where wkorder_id=moid ;
           select coalesce(std_num,0) into myres from alldo_acme_iot_cnc_performance_report2 where wkorder_id=moid and iot_date=iotdate ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists get_report2_iotdur(moid int) cascade""")
        self._cr.execute("""create or replace function get_report2_iotdur(moid int) returns float as $BODY$
         DECLARE
           myres float ;
           iotdate date ;
         BEGIN
           select max(iot_date) into iotdate from alldo_acme_iot_cnc_performance_report2 where wkorder_id=moid ;
           select coalesce(iot_duration,0) into myres from alldo_acme_iot_cnc_performance_report2 where wkorder_id=moid and iot_date=iotdate ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)




        self._cr.execute("""drop view if exists finereport_main_equip_view cascade""")
        self._cr.execute("""CREATE VIEW finereport_main_equip_view as (
          select A.name as name,A.equipment_no,A.iot_status,(select getdevstatus(A.iot_status)) as dev_status,(select getiotowner(A.id)) as dev_owner,
          (select getdevtype(A.equipment_type)) as dev_type,B.name as mo_no,A.today_prodnum,B.eng_type,C.default_code,C.id as prod_id,B.order_num,B.prod_num,(select get_report2_stdnum(B.id)) as stdnum,(select get_report2_iotdur(B.id)) as iotdur 
            from maintenance_equipment A 
           left join alldo_acme_iot_workorder B on A.mo_no = B.id 
           left join product_product C on B.product_no=C.id where A.active=True and A.category_id=2 order by equipment_no asc
           )""")

        self._cr.execute("""drop view if exists finereport_main_equip_view1 cascade""")
        self._cr.execute("""CREATE VIEW finereport_main_equip_view1 as (
                  select distinct dev_status,(select getstatusnum(iot_status)) as status_num,(select getstatusper(iot_status)) as status_per
                  from finereport_main_equip_view
                   )""")

        self._cr.execute("""drop view if exists finereport_todaynum_view cascade""")
        self._cr.execute("""CREATE VIEW finereport_todaynum_view as (
                          select A.mo_no,A.equipment_no,(select getequreplqceline(B.id)) as replace_duration,B.prod_duration,B.id,(select getequtodaynum(B.id)) as today_num
                          from maintenance_equipment A left join alldo_acme_iot_workorder B on A.mo_no=B.id where A.category_id=2 and A.active=true
                           )""")

        self._cr.execute("""drop view if exists finereport_outsuborder_view cascade""")
        self._cr.execute("""CREATE VIEW finereport_outsuborder_view as (
                              select A.name,A.cus_name,B.name as partner,A.product_no,C.default_code,A.blank_num,A.prod_num from alldo_acme_iot_outsuborder A
                              ,res_partner B,product_product C where A.cus_name=B.id and A.product_no = C.id and A.active=true and A.state in ('1','2') and A.blank_num is not null 
                                   )""")

        self._cr.execute("""drop function if exists getiotdatanum(iotnode int) cascade""")
        self._cr.execute("""create or replace function getiotdatanum(iotnode int) returns INT as $BODY$
         DECLARE
           myres int ;
           mynowdate date ;
         BEGIN
           select max(iot_date::DATE) into mynowdate ;
           select sum(iot_num) into myres from alldo_acme_iot_workorder_iot_data where iot_node=iotnode and iot_date::DATE = mynowdate::DATE ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getiotdatakpi(iotnode int) cascade""")
        self._cr.execute("""create or replace function getiotdatakpi(iotnode int) returns Float as $BODY$
         DECLARE
           myres Float ;
           totdur int ;
           totstd int ;
           mynowdate date ;
         BEGIN
           select max(iot_date::DATE) into mynowdate ; 
           select coalesce(sum(iot_duration),0) into totdur from alldo_acme_iot_workorder_iot_data where iot_node=iotnode and iot_date::DATE = mynowdate::DATE ;
           select coalesce(sum(std_duration),0) into totstd from alldo_acme_iot_workorder_iot_data where iot_node=iotnode and iot_date::DATE = mynowdate::DATE ;
           if totdur = 0 then
              myres = 0 ;
           else   
              myres = round((totstd::numeric/totdur::numeric)*100) ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getiotprodname(orderid int) cascade""")
        self._cr.execute("""create or replace function getiotprodname(orderid int) returns varchar as $BODY$
         DECLARE
            myres varchar ;
            prodid int ;
            defaultcode varchar ;
         BEGIN
            select product_no into prodid from alldo_acme_iot_workorder where id = orderid ;
            select default_code into myres from product_product where id = prodid ;
            return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        tools.drop_view_if_exists(self.env.cr, 'alldo_acme_iot_cnc_performance_now')
        self._cr.execute("""CREATE VIEW alldo_acme_iot_cnc_performance_now as (select distinct A.iot_node,B.equipment_no,
            (select getiotdatanum(A.iot_node)) as todaynum,(select getiotdatakpi(A.iot_node)) as equkpi
            from alldo_acme_iot_workorder_iot_data A,maintenance_equipment B
            where A.iot_date::DATE = now()::DATE and A.iot_node = B.id)""")

        self._cr.execute("""drop function if exists gettodayduration(equipid int) cascade""")
        self._cr.execute("""create or replace function gettodayduration(equipid int) returns Float as $BODY$
          DECLARE
             ncount int ;
             myh int ;
             mym int ;
             myd int ;
             stt timestamp ;
             ent timestamp ;
             initdt timestamp ;
             myres float ;
             mynowdate date ;
          BEGIN
             select max(iot_datetime::DATE) into mynowdate from alldo_acme_iot_equipment_iot_data ; 
             initdt = concat(mynowdate::DATE::TEXT,' 00:00:00')::timestamp - interval '8 hour' ;
             select count(*) into ncount from alldo_acme_iot_equipment_iot_data where iot_id=equipid and iot_datetime >= initdt ;
             if ncount > 0 then
                select min(iot_datetime) into stt from alldo_acme_iot_equipment_iot_data where iot_id=equipid and iot_datetime >= initdt ;
                select max(iot_datetime) into ent from alldo_acme_iot_equipment_iot_data where iot_id=equipid and iot_datetime >= initdt ;
                select date_part('hour',age(ent::timestamp,stt::timestamp)) into myh ;
                select date_part('minute',age(ent::timestamp,stt::timestamp)) into mym ;
                myres = myh + round((mym::numeric/60::numeric),1);
             else
                myres = 0 ;
             end if ;
             return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        tools.drop_view_if_exists(self.env.cr, 'acme_maintenance_equipment_today')
        self._cr.execute("""CREATE VIEW acme_maintenance_equipment_today as (select equipment_no,id,mo_no,(select gettodayduration(id)) as todaydur
            from maintenance_equipment where category_id=2 and active=true order by equipment_no)""")

        self._cr.execute("""drop function if exists getmonthngrate() cascade""")
        self._cr.execute("""create or replace function getmonthngrate() returns float as $BODY$
         DECLARE
           myyear varchar ;
           mymonth varchar ;
           months date ;
           monthe date ;
           totnum int ;
           ngnum int ;
           ngratio float ;
           mynowdate date ;
         BEGIN
           select max(iot_date::DATE) into mynowdate from alldo_acme_iot_cnc_performance_report2 ;
           select date_part('year',mynowdate)::TEXT into myyear ;
           select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
           select concat(myyear,'-',mymonth,'-01')::DATE into months ;
           select months + interval '1 month' - interval '1 day' into monthe ;
           select sum(total_amount_num),sum(coalesce(processing_ng_num,0)+coalesce(material_ng_num,0)) into totnum,ngnum from 
              alldo_acme_iot_cnc_performance_report2 where iot_date >= months and iot_date <= monthe ;
           if totnum > 0 then
              ngratio = round((ngnum::numeric/totnum::numeric)*100,2) ;
           else
              ngratio = 0.0 ;
           end if ;
           return ngratio ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmonthperrate() cascade""")
        self._cr.execute("""create or replace function getmonthperrate() returns float as $BODY$
         DECLARE
           myyear varchar ;
           mymonth varchar ;
           months date ;
           monthe date ;
           totnum int ;
           totprratio float ;
           prratio float ;
           mynowdate date ;
         BEGIN
           select max(iot_date::DATE) into mynowdate from alldo_acme_iot_cnc_performance_report2 ; 
           select date_part('year',mynowdate)::TEXT into myyear ;
           select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
           select concat(myyear,'-',mymonth,'-01')::DATE into months ;
           select months + interval '1 month' - interval '1 day' into monthe ;
          /* months = '2022-11-01'::DATE ;
           monthe = '2022-11-30'::DATE ; */
          /* select sum(coalesce(total_amount_num,0)*coalesce(performance_rate,0)),sum(coalesce(total_amount_num,0)) into totprratio,totnum from 
              alldo_acme_iot_cnc_performance_report2 where iot_date >= months and iot_date <= monthe ;*/
           select avg(performance_rate) into prratio from alldo_acme_iot_cnc_performance_report2 where iot_date >= months and iot_date <= monthe and performance_rate is not null;
          /* if totnum > 0 then
              prratio = round((totprratio::numeric/totnum::numeric),2) ;
           else
              prratio = 0.0 ;
           end if ;*/
           return prratio ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_month_ng_rate')
        self._cr.execute("""CREATE VIEW acme_cnc_month_ng_rate as (select getmonthngrate() as ngrate,getmonthperrate() as perrate)""")

        self._cr.execute("""drop function if exists getiotmaxdate() cascade""")
        self._cr.execute("""drop function if exists getiotmaxdate(equipno varchar) cascade""")
        self._cr.execute("""create or replace function getiotmaxdate(equipno varchar) returns date as $BODY$
         DECLARE
           mynowdate date ;
           equipid int ;
         BEGIN
           select id into equipid from maintenance_equipment where equipment_no=equipno ;
           select max(iot_date::DATE) into mynowdate from alldo_acme_iot_cnc_performance_report2 where iot_node=equipid ;
           return mynowdate ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node1')
        self._cr.execute("""CREATE VIEW acme_cnc_node1 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast01' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node2')
        self._cr.execute("""CREATE VIEW acme_cnc_node2 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast02' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node3')
        self._cr.execute("""CREATE VIEW acme_cnc_node3 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast03' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node4')
        self._cr.execute("""CREATE VIEW acme_cnc_node4 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast04' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node7')
        self._cr.execute("""CREATE VIEW acme_cnc_node7 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast07' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")

        tools.drop_view_if_exists(self.env.cr, 'acme_cnc_node8')
        self._cr.execute("""CREATE VIEW acme_cnc_node8 as (
          select A.equipment_no,A.mo_no,A.default_code,A.dev_owner,B.id,C.total_amount_num,C.processing_ng_num,C.std_num,C.iot_duration,C.performance_rate
          from finereport_main_equip_view A left join maintenance_equipment B on A.equipment_no = B.equipment_no
          left join alldo_acme_iot_cnc_performance_report2 C on B.id = C.iot_node
          where A.equipment_no='cast08' and C.iot_date = (select getiotmaxdate(A.equipment_no)) 
          )""")














