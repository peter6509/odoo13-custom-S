# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoiotstoreproc1(models.Model):
    _name = "alldo_gh_iot.storeproc1"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genattendancefw1(startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function genattendancefw1(startdate date,enddate date) returns void as $BODY$
        DECLARE
          att_cur refcursor ;
          att_rec record ;
          ncount int ;
          mymindatetime timestamp ;
          myminid int ;
          myequipid int ;
          mywkorderid int ;
          
        BEGIN
          delete from alldo_gh_iot_attendance_firstwork ;
          open att_cur for select * from  alldo_gh_iot_emp_attendance where (attendance_date + interval '8 hours')::DATE >= startdate::DATE
             and (attendance_date + interval '8 hours')::DATE <= enddate::DATE and attendance_type='1' order by attendance_id ;
          loop
             fetch att_cur into att_rec ;
             exit when not found ;
             select count(*) into ncount from alldo_gh_iot_attendance_firstwork where emp_id=att_rec.attendance_id and attendance_cdate=att_rec.attendance_date::DATE::TEXT ;
             if ncount = 0 then
                select min(id) into myminid from alldo_gh_iot_equipment_iot_data where (iot_datetime + interval '8 hours')::DATE >= startdate and iot_datetime > att_rec.attendance_date and iot_owner=att_rec.attendance_id ;
                select iot_id,iot_workorder,(iot_datetime + interval '8 hours') into myequipid,mywkorderid,mymindatetime from alldo_gh_iot_equipment_iot_data where id = myminid ;
                if myminid is null then
                   insert into alldo_gh_iot_attendance_firstwork(emp_id,attendance_cdate) values (att_rec.attendance_id,substring((att_rec.attendance_date + interval '8 hours')::TEXT,1,16)) ;
                else
                   
                   insert into alldo_gh_iot_attendance_firstwork(emp_id,attendance_cdate,iot_cdatetime,iot_workorder,iot_id) values (att_rec.attendance_id,substring((att_rec.attendance_date + interval '8 hours')::TEXT,1,16),substring(mymindatetime::TEXT,1,16),mywkorderid,myequipid) ;
                end if ;
             end if ;
          end loop ;
          close att_cur ;  
        END;$BODY$ 
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genattendancefw2(empid int,startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function genattendancefw2(empid int,startdate date,enddate date) returns void as $BODY$
        DECLARE
          att_cur refcursor ;
          att_rec record ;
          ncount int ;
          mymindatetime timestamp ;
          myminid int ;
          myequipid int ;
          mywkorderid int ;

        BEGIN
          delete from alldo_gh_iot_attendance_firstwork ;
          open att_cur for select * from  alldo_gh_iot_emp_attendance where (attendance_date + interval '8 hours')::DATE >= startdate::DATE
             and (attendance_date + interval '8 hours')::DATE <= enddate::DATE and attendance_type='1' and attendance_id=empid ;
          loop
             fetch att_cur into att_rec ;
             exit when not found ;
             select count(*) into ncount from alldo_gh_iot_attendance_firstwork where emp_id=att_rec.attendance_id and attendance_cdate=att_rec.attendance_date::DATE::TEXT ;
             if ncount = 0 then
                select min(id) into myminid from alldo_gh_iot_equipment_iot_data where (iot_datetime + interval '8 hours')::DATE >= startdate and iot_datetime > att_rec.attendance_date and iot_owner=att_rec.attendance_id ;
                select iot_id,iot_workorder,(iot_datetime + interval '8 hours') into myequipid,mywkorderid,mymindatetime from alldo_gh_iot_equipment_iot_data where id = myminid ;
                if myminid is null then
                   insert into alldo_gh_iot_attendance_firstwork(emp_id,attendance_cdate) values (att_rec.attendance_id,substring((att_rec.attendance_date + interval '8 hours')::TEXT,1,16)) ;
                else
                   insert into alldo_gh_iot_attendance_firstwork(emp_id,attendance_cdate,iot_cdatetime,iot_workorder,iot_id) values (att_rec.attendance_id,substring((att_rec.attendance_date + interval '8 hours')::TEXT,1,16),substring(mymindatetime::TEXT,1,16),mywkorderid,myequipid) ;
                end if ;
             end if ;
          end loop ;
          close att_cur ;  
        END;$BODY$ 
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastlogin() cascade""")
        self._cr.execute("""create or replace function getlastlogin() returns varchar as $BODY$
         DECLARE
           myres varchar ;
           mynowint int ;
           maxlen int ;
           myprefix varchar ;
         BEGIN
           select max(login) into myres from res_users where id > 5 ;
           select length(myres) into maxlen ;
           select substring(myres,1,2) into myprefix ;
           select (substring(myres,3,(maxlen-2)))::INT into mynowint ;
           mynowint = mynowint + 1 ;
           myres = concat(myprefix,lpad(mynowint::TEXT,3,'0')) ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runmintime(prodid int) cascade""")
        self._cr.execute("""create or replace function runmintime(prodid int) returns void as $BODY$
         DECLARE
           eng_cur refcursor ;
           eng_rec record ;
           list_cur refcursor ;
           list_rec record ;
           nitem int ;
           prodtmplid int ;
           mogroupid int ;
           mindur float ;
           mindurid int ;
           mindurid1 int ;
           dur_num int ;
           dur1 float ;
           dur2 float ;
           dur3 float ;
           dur4 float ;
           dur5 float ;
           duravg float ;
           mono int ;
           equipno varchar ;
           engfixcode varchar ;
           dispdur varchar ;
           dispdurtot varchar ;
           iotnode int ;
           duravgtot float ;
           wkorderid int ;
           equipid int ;
           iotstartid int ;
           iotfirstid int ;
         BEGIN
           delete from alldo_gh_iot_mintime_list ;
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;
           select max(mo_group_id) into mogroupid from alldo_gh_iot_workorder where product_no=prodid ;
           open eng_cur for select * from alldo_gh_iot_eng_order where prod_id=prodtmplid order by eng_order ;
           loop
             fetch eng_cur into eng_rec ;
             exit when not found ;
             select min(id) into wkorderid from alldo_gh_iot_workorder where mo_group_id=mogroupid and eng_type like '%'|| eng_rec.eng_type ||'%'; 
             select distinct iot_node into equipid from alldo_gh_iot_workorder_iot_data where order_id=wkorderid ;
             insert into alldo_gh_iot_mintime_list(product_id,eng_order,eng_type,mold_cavity,equip_id) values (prodid,eng_rec.eng_order,eng_rec.eng_type,coalesce(eng_rec.mold_cavity,1),equipid) ;
           end loop ;
           close eng_cur ;
           duravgtot = 0 ;
           open list_cur for select * from alldo_gh_iot_mintime_list ;
           loop
             fetch list_cur into list_rec ;
             exit when not found ;
             select id into mono from alldo_gh_iot_workorder where mo_group_id=mogroupid and eng_seq=list_rec.eng_order ;
             select max(iot_node) into iotnode from alldo_gh_iot_workorder_iot_data where order_id=mono ;            
             select equipment_no into equipno from maintenance_equipment where id=iotnode ;      
             if substring(equipno,1,1)='L' then
                 engfixcode = '(車)' ;
             else
                 engfixcode = '(銑)' ;
             end if ;
             dur_num = 0 ;
             mindur = 0 ;
             select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 ;
             select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0  and id > iotstartid ;
             select min(iot_duration1) into mindur from alldo_gh_iot_workorder_iot_data 
                where order_id=mono and iot_seq > 2 and iot_duration1 > 10  and id > iotfirstid ;
             if mindur > 0 then
                dur1 = mindur ;
                select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num = 0 and id > iotfirstid ;
                select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and id > iotstartid ;
                select min(id) into mindurid1 from alldo_gh_iot_workorder_iot_data 
                  where order_id=mono and iot_num > 0 and iot_duration1 > 10 and iot_seq > 2 ;
                mindurid = mindurid1 ;
                iotfirstid = mindurid1 ;
                dur_num = dur_num + 1 ;
             else
                dur1 = 0 ;   
             end if ;
             select min(iot_duration1) into mindur from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_seq > 2 and id > mindurid and iot_duration > 10;
             if mindur > 0 then
                dur2 = mindur ;
                select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num = 0 and id > iotfirstid ;
                select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and id > iotstartid ;
                select min(id) into mindurid1 from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and iot_duration1 > 10 and id > iotfirstid ;
                mindurid = mindurid1 ;
                iotfirstid = mindurid1 ;
                dur_num = dur_num + 1 ;
             else
                dur2 = 0 ;   
             end if ;
             select min(iot_duration1) into mindur from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_seq > 2 and id > mindurid and iot_duration1 > 10;
             if mindur > 0 then
                dur3 = mindur ;
                select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num = 0 and id > iotfirstid ;
                select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and id > iotstartid ;
                select min(id) into mindurid1 from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and iot_duration1 > 10 and id > iotfirstid ;
                mindurid = mindurid1 ;
                iotfirstid = mindurid1 ;
                dur_num = dur_num + 1 ;
             else
                dur3 = 0 ;   
             end if ;
             select min(iot_duration) into mindur from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_seq > 2 and id > mindurid  and iot_duration > 10;
             if mindur > 0 then
                dur4 = mindur ;
                select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num = 0 and id > iotfirstid ;
                select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and id > iotstartid ;
                select min(id) into mindurid1 from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and iot_duration1 > 10 and id > iotfirstid ;
                mindurid = mindurid1 ;
                iotfirstid = mindurid1 ;
                dur_num = dur_num + 1 ;
             else
                dur4 = 0 ;   
             end if ;
             select min(iot_duration1) into mindur from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_seq > 2 and id > mindurid and iot_duration > 10 ;
             if mindur > 0 then
                dur5 = mindur ; 
                select min(id) into iotstartid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num = 0 and id > iotfirstid ;
                select min(id) into iotfirstid from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and id > iotstartid ;
                select min(id) into mindurid1 from alldo_gh_iot_workorder_iot_data where order_id=mono and iot_num > 0 and iot_duration1 > 10 and id > iotfirstid ;
                mindurid = mindurid1 ;
                iotfirstid = mindurid1 ;
                dur_num = dur_num + 1 ;
             else
                dur5 = 0 ;   
             end if ;
             if dur_num = 0 then
                duravg=0 ;
                dispdur = ' ' ;
             else   
                duravg=round(((coalesce(dur1,0) + coalesce(dur2,0) + coalesce(dur3,0) + coalesce(dur4,0) + coalesce(dur5,0))::numeric / dur_num::numeric) ,1); 
                select TO_CHAR(concat(duravg::TEXT,' second')::interval, 'HH24:MI:SS') into dispdur ;
             end if ;  
             duravgtot = duravgtot + duravg ;
             update alldo_gh_iot_mintime_list set eng_type=concat(coalesce(eng_type,' '), engfixcode),duration=duravg,display_duration=dispdur where id = list_rec.id ; 
           end loop ;  
           close list_cur ;
           select TO_CHAR(concat(duravgtot::TEXT,' second')::interval, 'HH24:MI:SS') into dispdurtot ;
           insert into alldo_gh_iot_mintime_list(product_id,eng_type,eng_order,duration,display_duration) values (prodid,'合計工時',99,duravgtot,dispdurtot) ;
           delete from alldo_gh_iot_mintime_list where duration=0 ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geniotseq() cascade""")
        self._cr.execute("""create or replace function geniotseq() returns void as $BODY$
          DECLARE
           ord_cur refcursor ;
           ord_rec record ;
           ior_cur refcursor ;
           iot_rec record ;
           nseq int ;
           orderid int ;
           iotdur1 float ;
           iotdur2 float ;
           iotid1 int ;
           iotid2 int ;
           prodno int ;
           prodtmplid int ;
           engtype varchar ;
           iscombine Boolean ;
           nmod int ;
          BEGIN
           nseq = 0 ; 
           iotid1 = 0 ;
           iotid2 = 0 ;
           open ord_cur for select id,order_id,iot_serial,iot_seq,iot_num,iot_duration from alldo_gh_iot_workorder_iot_data where iot_seq is null order by order_id,iot_serial ;
           loop
             fetch ord_cur into ord_rec ;
             exit when not found ;
             select product_no,eng_type into prodno,engtype from alldo_gh_iot_workorder where id=ord_rec.order_id ;
             select product_tmpl_id into prodtmplid from product_product where id = prodno ;
            /* select is_combine into iscombine from alldo_gh_iot_eng_order where prod_id=prodtmplid and eng_type like '%'|| engtype ||'%' ; */
             if ord_rec.iot_num=0 then
                 nseq = 0 ;      
             else
                 nseq = nseq + 1 ;    
             end if ;
            /* if iscombine=True then
                select mod(nseq,2) into nmod ;
                if nmod = 0 then
                   iotid1 = ord_rec.id ;
                   iotdur1 = coalesce(ord_rec.iot_duration,0) ;
                else
                   iotid2 = ord_rec.id ;
                   if iotdur1 = 0 or iotdur1 is null then
                      iotdur1 = coalesce(ord_rec.iot_duration,0) ;
                   end if ;
                   iotdur2 = coalesce(ord_rec.iot_duration,0) ;
                   if iotdur2 = 0 or iotdur2 is null then
                      iotdur2 = iotdur1 ;
                   end if ;
                end if ;
                update alldo_gh_iot_workorder_iot_data set iot_seq=nseq where id = ord_rec.id ;
                update alldo_gh_iot_workorder_iot_data set iot_duration1=(iotdur1+iotdur2) where id in (iotid1,iotid2) ;
             else */
                update alldo_gh_iot_workorder_iot_data set iot_seq=nseq where id = ord_rec.id ;
           /* end if ;   */
           end loop ;
           close ord_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geniotseq1() cascade""")
        self._cr.execute("""create or replace function geniotseq1() returns void as $BODY$
          DECLARE
           ord_cur refcursor ;
           ord_rec record ;
           ior_cur refcursor ;
           iot_rec record ;
           nseq int ;
           orderid int ;
           iotdur1 float ;
           iotdur2 float ;
           iotid1 int ;
           iotid2 int ;
           prodno int ;
           prodtmplid int ;
           engtype varchar ;
           iscombine Boolean ;
           nmod int ;
          BEGIN
           nseq = 0 ; 
           iotid1 = 0 ;
           iotid2 = 0 ;
           open ord_cur for select id,order_id,iot_serial,iot_seq,iot_num,iot_duration from alldo_gh_iot_workorder_iot_data order by order_id,iot_serial ;
           loop
             fetch ord_cur into ord_rec ;
             exit when not found ;
             select product_no,eng_type into prodno,engtype from alldo_gh_iot_workorder where id=ord_rec.order_id ;
             select product_tmpl_id into prodtmplid from product_product where id = prodno ;
             select is_combine into iscombine from alldo_gh_iot_eng_order where prod_id=prodtmplid and eng_type like '%'|| engtype ||'%' ;
             if ord_rec.iot_num=0 then
                 nseq = 0 ;      
             else
                 nseq = nseq + 1 ;    
             end if ;
             if iscombine=True then
                select mod(nseq,2) into nmod ;
                if nmod = 0 then
                   iotid1 = ord_rec.id ;
                   iotdur1 = coalesce(ord_rec.iot_duration,0) ;
                else
                   iotid2 = ord_rec.id ;
                   if iotdur1 = 0 or iotdur1 is null then
                      iotdur1 = coalesce(ord_rec.iot_duration,0) ;
                   end if ;
                   iotdur2 = coalesce(ord_rec.iot_duration,0) ;
                   if iotdur2 = 0 or iotdur2 is null then
                      iotdur2 = iotdur1 ;
                   end if ;
                end if ;
                update alldo_gh_iot_workorder_iot_data set iot_seq=nseq where id = ord_rec.id ;
                update alldo_gh_iot_workorder_iot_data set iot_duration1=(iotdur1+iotdur2) where id in (iotid1,iotid2) ;
             else
                update alldo_gh_iot_workorder_iot_data set iot_seq=nseq,iot_duration1=coalesce(iot_duration,0) where id = ord_rec.id ;
             end if ;   
           end loop ;
           close ord_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genavgdataline(prodtmplid int) cascade""")
        self._cr.execute("""create or replace function genavgdataline(prodtmplid int) returns void as $BODY$
         DECLARE
           ncount int ;
           eng_cur refcursor ;
           eng_rec record ;
         BEGIN
           delete from alldo_gh_iot_workorder_avgdata where prod_id=prodtmplid ;
           open eng_cur for select sequence,prod_id,eng_type from alldo_gh_iot_eng_order where prod_id=prodtmplid order by sequence,id ;
           loop
             fetch eng_cur into eng_rec ;
             exit when not found ;
             insert into alldo_gh_iot_workorder_avgdata(sequence,prod_id,eng_type) values (eng_rec.sequence,eng_rec.prod_id,eng_rec.eng_type) ;
           end loop ;
           close eng_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallavgdata() cascade""")
        self._cr.execute("""create or replace function genallavgdata() returns void as $BODY$
         DECLARE
           prod_cur refcursor ;
           prod_rec record ;
         BEGIN
           open prod_cur for select id from product_template where active=True ;
           loop
             fetch prod_cur into prod_rec ;
             exit when not found ;
             execute genavgdataline(prod_rec.id) ;
           end loop ;
           close prod_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentotavgdata() cascade""")
        self._cr.execute("""create or replace function gentotavgdata() returns void as $BODY$
         DECLARE
           avg_cur refcursor ;
           avg_rec record ;
           prodid int ;
           prodtmplid int ;
           avgdur float ;
           mindur1 float ;
           mindur2 float ;
           mindur3 float ;
           mindur4 float ;
           mindur5 float ;
           mindur float ;
           maxid int ;
           iotnode int ;
           categid int ;
           categname varchar ;
           nnum int ;
         BEGIN
           open avg_cur for select * from alldo_gh_iot_workorder_avgdata order by prod_id ;
           loop
             fetch avg_cur into avg_rec ;
             exit when not found ;
             avgdur = 0 ;
             mindur1 = 0 ;
             mindur2 = 0 ;
             mindur3 = 0 ;
             mindur4 = 0 ;
             mindur5 = 0 ;
             nnum = 0 ;
             select id into prodid from product_product where product_tmpl_id=avg_rec.prod_id ;
             select min(iot_duration) into mindur1 from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
              and iot_seq > 2 and iot_duration > 10  ;   
             /* select coalesce(min(iot_duration),0) into mindur2 from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
               and iot_duration > mindur1 and iot_duration <= (mindur1 * 1.5) and iot_duration > 10 ; 
             select coalesce(min(iot_duration),0) into mindur3 from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
               and iot_duration > mindur2 and iot_duration <= (mindur1 * 1.5) and iot_duration > 10 ;      
             select coalesce(min(iot_duration),0) into mindur4 from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
                and iot_duration > mindur3 and iot_duration <= (mindur1 * 1.5) and iot_duration > 10 ; 
              select coalesce(min(iot_duration),0) into mindur5 from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
                and iot_duration > mindur4 and iot_duration <= (mindur1 * 1.5) and iot_duration > 10 ;   */
              select avg(iot_duration) into avgdur from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%')
               and iot_duration <= (mindur1 * 2) and iot_duration > 10 and iot_seq > 2 ;   
              avgdur = round(avgdur::numeric/60::numeric,1) ;  
           /*  if mindur1 > 0 then
                nnum = nnum + 1 ;
             end if ;
             if mindur2 > 0 then
                nnum = nnum + 1 ;
             end if ;
             if mindur3 > 0 then
                nnum = nnum + 1 ;
             end if ;
             if mindur4 > 0 then
                nnum = nnum + 1 ;
             end if ;
             if mindur5 > 0 then
                nnum = nnum + 1 ;
             end if ;
             if nnum = 0 then
                mindur = round((avgdur::numeric * 0.9),1) ;
             else   
                mindur = round(round((mindur1+mindur2+mindur3+mindur4+mindur5)::numeric/nnum::numeric,1)/60::numeric,1) ;
             end if ;   */
             mindur = round(mindur1::numeric/60::numeric,1) ;
             if mindur = 0 then
                mindur = round(coalesce(mindur1,0)::numeric/60::numeric,1) ; 
             end if ;
             select max(id) into maxid from alldo_gh_iot_workorder_iot_data where order_id in 
               (select id from alldo_gh_iot_workorder where product_no=prodid and eng_type like '%'|| avg_rec.eng_type ||'%') ;
             select iot_node into iotnode from alldo_gh_iot_workorder_iot_data where id=maxid ;
             select category_id into categid from maintenance_equipment where id = iotnode ;
             select name into categname from maintenance_equipment_category where id = categid ;
             /* if mindur > avgdur then
                mindur = round((avgdur::numeric * 0.9),1) ;
             end if ;
             if mindur = 0 then
                mindur = round((avgdur::numeric * 0.9),1) ;
             end if ;  */ 
             update  alldo_gh_iot_workorder_avgdata set iot_machine=categname,iot_single_avg=avgdur,iot_min_avg=mindur where id=avg_rec.id ;            
           end loop ;
           close avg_cur ;
          /* update alldo_gh_iot_workorder_avgdata set iot_min_avg=round((iot_single_avg::numeric * 0.9),1) where iot_min_avg is null ;*/
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentotavgdata1() cascade""")
        self._cr.execute("""create or replace function gentotavgdata1() returns void as $BODY$
         DECLARE
           lastdt timestamp ;
           startdt timestamp ;
           stddur float ;
           iotdur float ;
           minid int ;
           iot_cur refcursor ;
           iot_rec record ;
           iotdursecond float ;
           iotdurmin float ;
           iotdur1 float ;
           iotdurhour float ;
           iotdurday float ;
           mycavity int ;
           mono varchar ;
         BEGIN
           open iot_cur for select * from alldo_gh_iot_workorder_iot_data where (cal_process=False or cal_process is null)
               order by order_id,iot_date ;
           loop
              fetch iot_cur into iot_rec ;
              exit when not found ;
              select name into mono from alldo_gh_iot_workorder where id=iot_rec.order_id ;
              /* select getmomoldcavity(mono) into mycavity ; */
              mycavity = 1 ;
              if lastdt is null then
                 lastdt = iot_rec.iot_date ;
                 iotdur = abs(iot_rec.std_duration * mycavity)  ;
              else
                 if iot_rec.iot_seq=0 then
                    iotdur = abs(iot_rec.std_duration * mycavity) ;
                 else
                     select round(extract(second from (select age(iot_rec.iot_date,lastdt)))::numeric,0) into iotdursecond ;
                     select extract(minute from (select age(iot_rec.iot_date,lastdt))) into iotdurmin ;
                     select extract(hours from (select age(iot_rec.iot_date,lastdt))) into iotdurhour ;  
                     select extract(days from (select age(iot_rec.iot_date,lastdt))) into iotdurday ; 
                     iotdur1 = iotdursecond + (iotdurmin * 60) + (iotdurhour * 60 * 60) + (iotdurday * 24 * 60 * 60) ;
                     iotdur1 = abs(iotdur1) ;
                     if (iotdur1 > (iot_rec.std_duration * mycavity * 3)) and iot_rec.std_duration > 0 then
                          iotdur1 = abs(iot_rec.std_duration * mycavity) ;
                     end if ;
                     iotdur = abs(iotdur1) ;       
                 end if ;    
                 lastdt = iot_rec.iot_date ;
              end if ;
              if iotdur = 0 then
                 iotdur = abs(iot_rec.std_duration * mycavity)  ;
              end if ;
              update alldo_gh_iot_workorder_iot_data set iot_duration1=iotdur,cal_process=True where id = iot_rec.id ;
           end loop ;
           close iot_cur ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_attendance() cascade""")
        self._cr.execute("""create or replace function check_attendance() returns void as $BODY$
         DECLARE
           att_cur refcursor ;
           att_rec record ;
           emp_cur refcursor ;
           emp_rec record ;
           ncount int ;
           minid int ;
         BEGIN   
          update alldo_gh_iot_emp_attendance_list set att_start_date1=null,attendance_start1=null,att1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where att_start_date1 between att_start_date and att_end_date) ;
          update alldo_gh_iot_emp_attendance_list set att_end_date1=null,attendance_end1=null,att1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where att_end_date1 between att_start_date and att_end_date) ;
          update alldo_gh_iot_emp_attendance_list set att_start_date2=null,attendance_start2=null,att2_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where att_start_date2 between att_start_date and att_end_date) ;
          update alldo_gh_iot_emp_attendance_list set att_end_date2=null,attendance_end2=null,att2_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where att_end_date2 between att_start_date and att_end_date) ;  
            
          update alldo_gh_iot_emp_attendance_list set otatt_start_date=null,otattendance_start=null,otatt_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_start_date between att_start_date and att_end_date) ;
          update alldo_gh_iot_emp_attendance_list set otatt_end_date=null,otattendance_end=null,otatt_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_end_date between att_start_date and att_end_date) ;
          
          update alldo_gh_iot_emp_attendance_list set otatt_start_date1=null,otattendance_start1=null,otatt1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_start_date1 between att_start_date and att_end_date) ;
          update alldo_gh_iot_emp_attendance_list set otatt_end_date1=null,otattendance_end1=null,otatt1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_end_date1 between att_start_date and att_end_date) ;  
            
          update alldo_gh_iot_emp_attendance_list set otatt_start_date1=null,otattendance_start1=null,otatt1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_start_date1 between otatt_start_date and otatt_end_date) ;
          update alldo_gh_iot_emp_attendance_list set otatt_end_date1=null,otattendance_end1=null,otatt1_duration=null where id in 
            (select id from alldo_gh_iot_emp_attendance_list where otatt_end_date1 between otatt_start_date and otatt_end_date) ;  
            
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastblankinnum(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastblankinnum(partnerid int,prodid int) returns float as $BODY$
         DECLARE
            myres float ;
            pickingid int ;
         BEGIN
            select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
              (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
            select product_qty into myres from stock_move where product_id=prodid and picking_id=pickingid ;
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastblankindate(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastblankindate(partnerid int,prodid int) returns DATE as $BODY$
         DECLARE
            myres DATE ;
            pickingid int ;
         BEGIN
            select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
              (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
            select date_done into myres from stock_picking where id=pickingid ;
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastoutsourcingnum(sourceloc int,destloc int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastoutsourcingnum(sourceloc int,destloc int,prodid int) returns Float as $BODY$
         DECLARE
            myres Float ;
            myid int ;
         BEGIN
            select max(id) into myid from stock_move_line where location_id=sourceloc and location_dest_id=destloc and product_id=prodid
               and state='done' ;
            select qty_done into myres from  stock_move_line where id = myid ;  
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastoutsourcingdate(sourceloc int,destloc int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastoutsourcingdate(sourceloc int,destloc int,prodid int) returns DATE as $BODY$
         DECLARE
            myres DATE ;
            myid int ;
         BEGIN
            select max(id) into myid from stock_move_line where location_id=sourceloc and location_dest_id=destloc and product_id=prodid
               and state='done' ; 
            select create_date::DATE into myres from stock_move_line where id = myid ;  
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastsemiinnum(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastsemiinnum(partnerid int,prodid int) returns float as $BODY$
         DECLARE
            myres float ;
            pickingid int ;
         BEGIN
            select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
              (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
            select product_qty into myres from stock_move where product_id=prodid and picking_id=pickingid ;
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastsemiindate(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastsemiindate(partnerid int,prodid int) returns DATE as $BODY$
         DECLARE
            myres DATE ;
            pickingid int ;
         BEGIN
            select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
              (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
            select date_done into myres from stock_picking where id=pickingid ;
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists recheckpopicking() cascade;""")
        self._cr.execute("""create or replace function recheckpopicking() returns void as $BODY$
          DECLARE
             po_cur refcursor ;
             po_rec record ;
             mvl_cur refcursor ;
             mvl_rec record ;
             ref varchar ;
             myqty float ;
             pickingid int ;
             pickingdate date ;
          BEGIN
             open po_cur for select * from alldo_gh_iot_picking_line where picking_id is null ;
             loop
               fetch po_cur into po_rec ;
               exit when not found ;
               open mvl_cur for select * from ghiot_moveline_powk_rel where po_id=po_rec.po_id ;
               loop
                 fetch mvl_cur into mvl_rec ;
                 exit when not found ;
                 select reference,qty_done,"date" into ref,myqty,pickingdate from stock_move_line where id = mvl_rec.move_id ;
                 select id into pickingid from stock_picking where name = ref ;
                 update alldo_gh_iot_picking_line set picking_id=pickingid where id=po_rec.id and picking_num=myqty and picking_date::DATE=pickingdate::DATE ;
               end loop ;
               close mvl_cur ;
             end loop ;
             close po_cur ;
             
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastprodinnum(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastprodinnum(partnerid int,prodid int) returns float as $BODY$
         DECLARE
            myres float ;
            pickingid int ;
         BEGIN
            select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
              (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
            select product_qty into myres from stock_move where product_id=prodid and picking_id=pickingid ;
            return myres ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastprodindate(partnerid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getlastprodindate(partnerid int,prodid int) returns DATE as $BODY$
        DECLARE
           myres DATE ;
           pickingid int ;
        BEGIN
           select max(id) into pickingid from stock_picking where partner_id=partnerid and picking_type_id=1 and id in
             (select picking_id from stock_move where picking_type_id=1 and product_id=prodid) ;
           select date_done into myres from stock_picking where id=pickingid ;
           return myres ;    
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensupplierinfo(supid int,prodid int) cascade""")
        self._cr.execute("""create or replace function gensupplierinfo(supid int,prodid int) returns void as $BODY$
          DECLARE
            ncount int ;
            sup_cur refcursor ;
            sup_rec record ;
          BEGIN
            delete from alldo_gh_iot_supplierinfo ;
            if supid = 0 and prodid !=0 then
                open sup_cur for select * from gh_supplierinfo_product where product_id=prodid order by name ;
            elsif supid != 0 and prodid = 0 then
                open sup_cur for select * from gh_supplierinfo_product where name=supid order by product_id ;
            else
                open sup_cur for select * from gh_supplierinfo_product where name=supid and product_id=prodid  ;
            end if ;
            loop
               fetch sup_cur into sup_rec ;
               exit when not found ;
               insert into alldo_gh_iot_supplierinfo(supplier_id,product_id,min_qty,price) values 
                 (sup_rec.name,sup_rec.product_id,sup_rec.min_qty,sup_rec.price) ;
            end loop ;
            close sup_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpowkrel() cascade""")
        self._cr.execute("""create or replace function genallpowkrel() returns void as $BODY$
          DECLARE
            ncount int ;
            po_cur refcursor ;
            po_rec record ;
            qtydone float ;
            pickingdate date ;
            pickingid int ;
            ptid int ;
            mvid int ;
            ref1 varchar ;
          BEGIN
            open po_cur for select * from ghiot_moveline_powk_rel ;
            loop
              fetch po_cur into po_rec ;
              exit when not found ;
              select qty_done,move_id into qtydone,mvid from stock_move_line where id = po_rec.move_id ;
              select max(picking_id),max(date) into pickingid,pickingdate from stock_move where id = mvid ;
              select origin into ref1 from stock_picking where id = pickingid ;
              select max(picking_type_id) into ptid from stock_move where id = mvid ;
              select count(*) into ncount from alldo_gh_iot_picking_line where po_id = po_rec.po_id and picking_id=pickingid ;
              if ncount = 0 then
                 if ptid = 1 then      /* IN */
                    insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_num,picking_type_id,picking_date,origin) values 
                        (po_rec.po_id,pickingid,(qtydone * -1),ptid,pickingdate,ref1) ;
                 elsif ptid = 2 then   /* OUT */
                     insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_num,picking_type_id,picking_date,origin) values 
                        (po_rec.po_id,pickingid,qtydone,ptid,pickingdate,ref1) ;
                 end if ;
              else
                 update alldo_gh_iot_picking_line set origin=ref1 where po_id = po_rec.po_id and picking_id=pickingid ;   
              end if ;
            end loop ;
            close po_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getwkorderpono(wkid int) cascade""")
        self._cr.execute("""create or replace function getwkorderpono(wkid int) returns varchar as $BODY$
          DECLARE
            po_cur refcursor ;
            po_rec record ;
            pono varchar ;
            myres varchar ;
          BEGIN
            myres='';
            open po_cur for select * from powkorder_iotwkorder_rel where wk_id=wkid ;
            loop
              fetch po_cur into po_rec ;
              exit when not found ;
              select po_no into pono from alldo_gh_iot_po_wkorder where id = po_rec.po_id ;
              if myres = '' then
                 myres = pono ;
              else
                 myres = concat(myres,',',pono) ;
              end if ;
            end loop;
            close po_cur ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallwkpono() cascade""")
        self._cr.execute("""create or replace function genallwkpono() returns void as $BODY$
          DECLARE
            wk_cur refcursor ;
            wk_rec record ;
            pono varchar ;
          BEGIN
            open wk_cur for select id from alldo_gh_iot_workorder ;
            loop
              fetch wk_cur into wk_rec ;
              exit when not found ;
              select getwkorderpono(wk_rec.id) into pono ;
              if pono is not null then
                 update alldo_gh_iot_workorder set po_no=pono where id = wk_rec.id ;
              end if ;   
            end loop ;
            close wk_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpurchaseprice(prodid int) cascade""")
        self._cr.execute("""create or replace function getpurchaseprice(prodid int) returns float as $BODY$
          DECLARE
            myres float ;
            maxid int ;
          BEGIN
            select max(id) into maxid from purchase_order_line where product_id = prodid ;
            select round(price_unit,2) into myres from purchase_order_line where id = maxid ;
            if myres is null then
               myres = 0.00 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW purchase_order_last10_view AS
                  SELECT A.product_id,A.price_unit,A.product_qty,A.qty_received,B.date_order,B.partner_id,C.product_tmpl_id,D.prod_material,D.prod_spec,D.default_code,B.id as purchaseid
                  from purchase_order_line A left join purchase_order B on A.order_id=B.id
                                             left join product_product C on A.product_id = C.id
                                             left join product_template D on C.product_tmpl_id = D.id
                                             where B.state='purchase' order by date_order desc;""")

        self._cr.execute("""drop function if exists genpurchaselast10(prodid int) cascade""")
        self._cr.execute("""create or replace function genpurchaselast10(prodid int) returns void as $BODY$
          DECLARE
            nitem int ;
            p_cur refcursor ;
            p_rec record ;
            maxspid int ;
            datedone date ;
          BEGIN
            delete from alldo_gh_iot_purchase_last10_list ;
            nitem = 1 ;
            open p_cur for select  *  from purchase_order_last10_view where product_id = prodid order by date_order desc;
            loop
              fetch p_cur into p_rec ;
              exit when not found ;
              select max(stock_picking_id) into maxspid from purchase_order_stock_picking_rel where purchase_order_id = p_rec.purchaseid ;
              if maxspid is not null then
                 select date_done into datedone from stock_picking where id = maxspid ;
              else
                 datedone = null ;   
              end if ;
              insert into alldo_gh_iot_purchase_last10_list(date_order,partner_id,product_id,product_qty,qty_received,price_unit,prod_material,prod_spec,last_date) values
               (p_rec.date_order,p_rec.partner_id,p_rec.product_id,p_rec.product_qty,p_rec.qty_received,p_rec.price_unit,p_rec.prod_material,p_rec.prod_spec,datedone) ;
               nitem = nitem + 1 ;
            end loop ;
            close p_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # self._cr.execute("""update product_template set categ_id=30 where categ_id in (31,43,26,27);""")
        # self._cr.execute("""delete from product_category where id in (31,43,26,27);""")
        #
        # self._cr.execute("""update product_template set categ_id=46 where categ_id=47 ;""")
        # self._cr.execute("""delete from product_category where id = 47;""")
        #
        # self._cr.execute("""update product_template set categ_id=39 where categ_id=40 ;""")
        # self._cr.execute("""delete from product_category where id = 40;""")
        #
        # self._cr.execute("""update product_template set categ_id=11 where categ_id=12 ;""")
        # self._cr.execute("""delete from product_category where id = 12;""")
        #
        # self._cr.execute("""update product_template set categ_id=36 where categ_id=37 ;""")
        # self._cr.execute("""delete from product_category where id = 37;""")
        #
        # self._cr.execute("""update product_template set categ_id=23 where categ_id=24 ;""")
        # self._cr.execute("""delete from product_category where id = 24;""")

        self._cr.execute("""drop function if exists rechkstkloc() cascade""")
        self._cr.execute("""create or replace function rechkstkloc() returns void as $BODY$
          DECLARE
            l_cur refcursor ;
            l_rec record ;
            nlen int ;
          BEGIN
            update stock_location set active=False where id=1 ;
            open l_cur for select id,parent_path from stock_location where substring(parent_path,1,3)='3/1' ;
            loop
              fetch l_cur into l_rec;
              exit when not found ;
              nlen = length(l_rec.parent_path) ;
              update stock_location set parent_path=substring(l_rec.parent_path,3,nlen-2) where id = l_rec.id ;
            end loop ;
            close l_cur ;
            update stock_location set parent_path='1/7/154',location_id=7 where id=154 ;
            update stock_location set active=false where id=153 ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencusstocklist(cusid int) cascade""")
        self._cr.execute("""create or replace function gencusstocklist(cusid int) returns void as $BODY$
         DECLARE
           bloc int ;
           blocnum int ;
           sloc int ;
           slocnum int ;
           ploc int ;
           plocnum int ;
           ngloc int ;
           nglocnum int ;
           rbloc int ;
           rblocnum int ;
           rsloc int ;
           rslocnum int ;
           rploc int ;
           rplocnum int ;
           prodid int ;
           p_cur refcursor ;
           p_rec record ;
           q_cur refcursor ;
           q_rec record ;
           ld date ;
           ncount int ;
           prodtmplid int ;
           prodlocation  varchar ;
         BEGIN
           delete from alldo_gh_iot_cus_stocklist ;
           open p_cur for select * from ghiot_prodstock_view where cus_no=cusid and location_id in (8,19) and prodactive=True order by product_id,location_id ;
           loop
              fetch p_cur into p_rec ;
              exit when not found ;
              select product_tmpl_id into prodtmplid from product_product where id=p_rec.product_id ;
              select prod_location into prodlocation from product_template where id=prodtmplid ;
              if prodlocation is null then
                 prodlocation = ' ' ;
              end if ;
              select count(*) into ncount from alldo_gh_iot_cus_stocklist where prod_no=p_rec.product_id and stock_loc = p_rec.location_id ;
              select max(coalesce(write_date,create_date)) into ld from stock_quant where product_id=p_rec.product_id and location_id=p_rec.location_id ;
              if ncount > 0 then
                 update alldo_gh_iot_cus_stocklist set stock_num = coalesce(stock_num,0) + coalesce(p_rec.quantity,0),last_update=ld  where prod_no=p_rec.product_id and stock_loc = p_rec.location_id ;
              else
                 insert into alldo_gh_iot_cus_stocklist(cus_no,prod_no,stock_loc,stock_num,last_update,rack_loc) values (p_rec.cus_no,p_rec.product_id,p_rec.location_id,p_rec.quantity,ld,prodlocation) ;
              end if ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprodequip(prodid int) cascade""")
        self._cr.execute("""create or replace function getprodequip(prodid int) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
           prodtmplid int ;
           equipid int ;
         BEGIN
           select product_tmpl_id into prodtmplid from product_product where id = prodid ;
           if prodtmplid is not null then
              select equip_id into equipid from product_template where id = prodtmplid ;
              if equipid is not null then
                 myres = equipid ;
              else
                 myres = 0 ;
              end if ;
           else
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

