# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class alldoiotstoreproc(models.Model):
    _name = "alldo_gh_iot.storeproc"

    @api.model
    def init(self):
        # return 'E'=> 員工 ; 'W' => 工單號 ; 'N' => Nothin  'X' => 故障  'Y' => 換線   'Z' => 機台復歸
        self.env.cr.execute("""drop function if exists getcodetype(mycode varchar,iotnode varchar) cascade""")
        self.env.cr.execute("""create or replace function getcodetype(mycode varchar,iotnode varchar) returns char as $BODY$
          DECLARE
            myres char ;
            ncount int ;
            ncount1 int ;
            equipstatusid int ; 
            ncountq int ;
            equipid int ;
            mynowdatetime timestamp ;
            outofforderid int ;
            mymaxid int ;
            mystatustype char ;
          BEGIN
            select id into equipid from maintenance_equipment where equipment_no = iotnode ;    
            if substring(mycode,1,3) = 'CNC' then
               select id,status_type into equipstatusid,mystatustype from maintenance_equipment_status where status_code = mycode ;
              if mystatustype = '1' then  /* 故障 */
                   myres = 'X' ;     
              elsif mystatustype = '2' then
                   myres = 'Y' ;          /* 換線 */
              else
                   myres = 'Z' ;          /* 復歸 */     
              end if ;   
            else
                select count(*) into ncount from hr_employee where emp_code = mycode ;
                if ncount > 0 then     /* 員工代碼 return 'E' */
                   myres = 'E' ;
                else
                   select count(*) into ncount1 from alldo_gh_iot_workorder where name = mycode  ;
                   if ncount1 > 0 then   /*  工單號碼 return 'W' */    
                      myres = 'W' ;
                   else
                      myres = 'N' ;     /*  都不是 return 'N' */
                   end if ;   
                end if ;
            end if ;    
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckoutoffstatus(nodename varchar) cascade""")
        self.env.cr.execute("""create or replace function ckoutoffstatus(nodename varchar) returns void as $BODY$
          DECLARE
             ncount int ;
             mymaxid int ;
             equipid int ;
             mynowdatetime timestamp ;
          BEGIN
             select id into equipid from maintenance_equipment where equipment_no = nodename ;
             if equipid is not null then
                select current_timestamp into mynowdatetime ;
                select max(id) into mymaxid from alldo_gh_iot_equipment_outofforder_status where 
                   iot_id=equipid ;
                update alldo_gh_iot_equipment_outofforder_status set end_datetime=mynowdatetime,write_date=mynowdatetime where 
                   id = mymaxid and end_datetime is null ;      
             end if ;
          END;$BODY$
          LANGUAGE plpgsql ;""")


        self.env.cr.execute("""drop function if exists genworkorderqcline(workorderid int,qcdate date,iotnode int,prodnum float,iotowner int) cascade""")
        self.env.cr.execute("""create or replace function genworkorderqcline(workorderid int,qcdate date,iotnode int,prodnum float,iotowner int) returns void as $BODY$ 
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
             mycusname int ;
             myproductno int ;
           BEGIN
             select cus_name,product_no into mycusname,myproductno from alldo_gh_iot_workorder where id = workorderid ;
             select current_timestamp into mynowdatetime ;
             select count(*) into ncount from alldo_gh_iot_workorder_qc where order_id=workorderid and qc_date::DATE=qcdate::DATE 
                   and iot_node=iotnode and iot_owner1=iotowner ;
             if ncount > 0 then
                update alldo_gh_iot_workorder_qc set total_amount_num = coalesce(total_amount_num,0) + prodnum,write_date=mynowdatetime,
                cus_name = mycusname,product_no=myproductno where order_id=workorderid and qc_date::DATE=qcdate::DATE and iot_node=iotnode and iot_owner1=iotowner;
             else  
                if prodnum > 0 then
                    insert into alldo_gh_iot_workorder_qc(order_id,qc_date,iot_node,total_amount_num,iot_owner1,create_date,cus_name,product_no) values
                      (workorderid,qcdate::DATE,iotnode,prodnum,iotowner,mynowdatetime,mycusname,myproductno) ;
                end if ;      
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;
        """)

        # iotstate => '1' 代表啟動   '2' 代表開工   '3' 代表暫停  '4' 代表停止
        self.env.cr.execute("""drop function if exists setiotstatus(workorder varchar,iotnode varchar,iotstate char) cascade""")
        self.env.cr.execute("""create or replace function setiotstatus(workorder varchar,iotnode varchar,iotstate char) returns void as $BODY$
          DECLARE
            ncount int ;
            iotnodeid int ;
            mynowdatetime timestamp ;
            myworkorderid int ;
            mylastid int ;
          BEGIN
            if workorder != 'ALLDO' and iotstate != '1' then
               select id into myworkorderid from alldo_gh_iot_workorder where name = workorder ; 
            else
               myworkorderid = 0 ;   
            end if ;   
            select id into iotnodeid from maintenance_equipment where equipment_no = iotnode ;
            select current_timestamp into mynowdatetime ; 
            if iotnodeid is not null and myworkorderid is not null then  
               update maintenance_equipment set iot_status=iotstate where id = iotnodeid ;
               if myworkorderid > 0 then
                   insert into alldo_gh_iot_equipment_iot_status (iot_id,iot_datetime,iot_workorder,iot_status,create_date) values
                    (iotnodeid,mynowdatetime,myworkorderid,iotstate,mynowdatetime) ;
                   insert into alldo_gh_iot_node_change_status (order_id,node_status,iot_node,node_datetime,create_date) values 
                     (myworkorderid,iotstate,iotnodeid,mynowdatetime,mynowdatetime) ; 
               end if ;      
            end if ;
            if iotstate='2' or iotstate='3' then
               update maintenance_equipment set mo_no=myworkorderid where id = iotnodeid ;
               if iotstate='2' then
                  execute ckoutoffstatus(iotnode) ; 
                  execute runcnccompleteline(iotnode) ;
               end if ;
            else
               update maintenance_equipment set write_date=mynowdatetime where id = iotnodeid ;  
            end if ;
            if iotstate='2' and myworkorderid is not null and iotnodeid is not null then
                select id into mylastid from alldo_gh_iot_workorder_lastwork where work_datetime::DATE = mynowdatetime::DATE and 
                   equipment_id=iotnodeid and workorder_id=myworkorderid ;
                if mylastid is not null then
                   update alldo_gh_iot_workorder_lastwork set work_datetime = mynowdatetime,write_date=mynowdatetime where id = mylastid ;
                else
                   insert into alldo_gh_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date) values 
                      (mynowdatetime,iotnodeid,myworkorderid,mynowdatetime) ;
                end if ;           
            end if ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        # iotstate => '1' 代表啟動   '2' 代表開工   '3' 代表暫停  '4' 代表停工
        self.env.cr.execute("""drop function if exists queryiotstatus(iotnode varchar) cascade""")
        self.env.cr.execute("""create or replace function queryiotstatus(iotnode varchar) returns char as $BODY$
          DECLARE
            myres char ;
            ncount int ;
            iotnodeid int ;
          BEGIN
            select id into iotnodeid from maintenance_equipment where equipment_no = iotnode ;
            myres = '3' ;
            if iotnodeid is not null then
               select iot_status into myres from  maintenance_equipment where id = iotnodeid ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists ipgetequipmentno(iotip varchar) cascade""")
        self.env.cr.execute("""create or replace function ipgetequipmentno(iotip varchar) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            myid int ;
          BEGIN
            select id,equipment_no into myid,myres from maintenance_equipment where iot_ip = iotip ;
            if myid is null then
               myres = 'NOTHING' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists geniotdata(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar) cascade""")
        self.env.cr.execute("""create or replace function geniotdata(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar) returns void 
           as $BODY$
           DECLARE
              myworkorderid int;
              mynodeid int ;
              myempid int ;
              mynowdatetime timestamp ;
              mynowdatetime1 timestamp ;
              mylastworktime timestamp ;
              iotdursecond float ;
              iotdurmin float ;
              iotdurhour float ;
              iotdurday float ;
              iotdurmin1 float ;
              iotdursecond1 float ;
              mylastid int ;
              ncount int ;
              mymoldcavity int ;
              stdduration int ;
           BEGIN
              /*   確認 geniotdata 是否有重複    */
              select count(*) into ncount from alldo_gh_iot_equipment_iot_data where iot_serial=iotserial ;
              select current_timestamp  into mynowdatetime ;
              select current_timestamp + interval '8 hours' into mynowdatetime1 ;
              select getmomoldcavity(workorderno) into mymoldcavity ;
              prodnum = (prodnum * mymoldcavity) ;
              if ncount = 0 then
                  select id into myworkorderid from alldo_gh_iot_workorder where name = workorderno ;
                  select id into mynodeid from maintenance_equipment where equipment_no = nodename ;
                  select id into myempid from hr_employee where emp_code = empno ;   
                  select work_datetime,id into mylastworktime,mylastid from alldo_gh_iot_workorder_lastwork where equipment_id=mynodeid and workorder_id=myworkorderid 
                     and work_datetime::DATE = mynowdatetime::DATE ;
                   select getmostdduration(myworkorderid) into stdduration ;
                  if mylastworktime is not null then  
                      select round(extract(second from (select age(mynowdatetime,mylastworktime)))::numeric,0) into iotdursecond ;
                      select extract(minute from (select age(mynowdatetime,mylastworktime))) into iotdurmin ;
                      select extract(hours from (select age(mynowdatetime,mylastworktime))) into iotdurhour ;  
                      select extract(days from (select age(mynowdatetime,mylastworktime))) into iotdurday ;
                      iotdurmin1 = iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60) ;
                      if (iotdurmin1 * 60) > (stdduration * 2) and stdduration > 0 then
                          iotdurmin1 = round((stdduration::numeric/60),2) ;
                      end if ;
                      if mylastworktime::DATE != mynowdatetime::DATE and stdduration > 0 then
                        iotdursecond1 = stdduration  ;
                      else
                        iotdursecond1 = iotdursecond + (iotdurmin1 * 60) ;
                      end if ;
                      update alldo_gh_iot_workorder_lastwork set work_datetime=mynowdatetime,write_date=mynowdatetime where id = mylastid ;
                  else
                      iotdurmin1 = 0 ;
                      iotdursecond1 = 0 ;
                      insert into alldo_gh_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date) values (mynowdatetime,mynodeid,myworkorderid,mynowdatetime) ;
                  end if ;    
                  if myworkorderid is not null and mynodeid is not null and myempid is not null then   
                     if iotdursecond1 > stdduration * 2 and stdduration > 0 then
                        iotdursecond1 = stdduration ;
                     end if ;
                     insert into alldo_gh_iot_workorder_iot_data(order_id,iot_date,iot_node,iot_owner,iot_num,iot_duration,iot_serial,create_date,std_duration) values
                      (myworkorderid,mynowdatetime,mynodeid,myempid,prodnum,iotdursecond1,iotserial,mynowdatetime,stdduration) ;
                      update alldo_gh_iot_workorder set prod_num = coalesce(prod_num,0) + prodnum,write_date=mynowdatetime where id = myworkorderid ;
                     insert into alldo_gh_iot_equipment_iot_data(iot_id,iot_datetime,iot_owner,iot_workorder,iot_num,iot_serial,create_date) values
                     (mynodeid,mynowdatetime,myempid,myworkorderid,prodnum,iotserial,mynowdatetime) ; 
                     update alldo_gh_iot_workorder set prod_duration=coalesce(prod_duration,0)+iotdurmin1,prod_num=coalesce(prod_num,0)+prodnum,write_date=mynowdatetime 
                         where id = myworkorderid ;
                     update alldo_gh_iot_workorder set prod_date=mynowdatetime where id = myworkorderid ;
                     update maintenance_equipment set iot_status='2',write_date=mynowdatetime where id = mynodeid ;
                     update maintenance_equipment set iot_start_datetime=mynowdatetime where iot_start_datetime is null and id = mynodeid ;  
                     execute genworkorderqcline(myworkorderid,mynowdatetime1::DATE,mynodeid,prodnum,myempid) ;
                     execute wkorderwip(myworkorderid,prodnum) ;
                     execute genpowkorder(myworkorderid,prodnum) ;
                     execute getmogoodnum(myworkorderid) ;
                     execute genwkngratio(myworkorderid) ;
                  end if ; 
              end if ;    
           END;$BODY$
           LANGUAGE plpgsql ;""")

        self.env.cr.execute("""drop function if exists geniotdata1(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar) cascade""")
        self.env.cr.execute("""create or replace function geniotdata1(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar) returns void 
           as $BODY$
           DECLARE
              myworkorderid int;
              mynodeid int ;
              myempid int ;
              mynowdatetime timestamp ;
              mylastworktime timestamp ;
              iotdursecond float ;
              iotdurmin float ;
              iotdurhour float ;
              iotdurday float ;
              iotdurmin1 float ;
              iotdursecond1 float ;
              mylastid int ;
              ncount int ;
              mymoldcavity int ;
              stdduration int ;
           BEGIN
              /*   確認 geniotdata 是否有重複    */
              select count(*) into ncount from alldo_gh_iot_equipment_iot_data where iot_serial=iotserial ;
              select current_timestamp  into mynowdatetime ;
              select getmomoldcavity(workorderno) into mymoldcavity ;
              prodnum = (prodnum * mymoldcavity) ;
              if ncount = 0 then
                  select id into myworkorderid from alldo_gh_iot_workorder where name = workorderno ;
                  select id into mynodeid from maintenance_equipment where equipment_no = nodename ;
                  select id into myempid from hr_employee where emp_code = empno ;   
                  select work_datetime,id into mylastworktime,mylastid from alldo_gh_iot_workorder_lastwork where equipment_id=mynodeid and workorder_id=myworkorderid 
                     and work_datetime::DATE = mynowdatetime::DATE ;
                   select getmostdduration(myworkorderid) into stdduration ;
                  if mylastworktime is not null then  
                      select round(extract(second from (select age(mynowdatetime,mylastworktime)))::numeric,0) into iotdursecond ;
                      select extract(minute from (select age(mynowdatetime,mylastworktime))) into iotdurmin ;
                      select extract(hours from (select age(mynowdatetime,mylastworktime))) into iotdurhour ;  
                      select extract(days from (select age(mynowdatetime,mylastworktime))) into iotdurday ;
                      iotdurmin1 = iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60) ;
                      if (iotdurmin1 * 60) > (stdduration * 2) and stdduration > 0 then
                          iotdurmin1 = round((stdduration::numeric/60),2) ;
                      end if ;
                      if mylastworktime::DATE != mynowdatetime::DATE and stdduration > 0 then
                        iotdursecond1 = stdduration  ;
                      else
                        iotdursecond1 = iotdursecond + (iotdurmin1 * 60) ;
                      end if ;
                      update alldo_gh_iot_workorder_lastwork set work_datetime=mynowdatetime,write_date=mynowdatetime where id = mylastid ;
                  else
                      iotdurmin1 = 0 ;
                      iotdursecond1 = 0 ;
                      insert into alldo_gh_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date) values (mynowdatetime,mynodeid,myworkorderid,mynowdatetime) ;
                  end if ;    
                  if myworkorderid is not null and mynodeid is not null and myempid is not null then   
                     if iotdursecond1 > stdduration * 2 and stdduration > 0 then
                        iotdursecond1 = stdduration ;
                     end if ;
                     insert into alldo_gh_iot_workorder_iot_data(order_id,iot_date,iot_node,iot_owner,iot_num,iot_duration,iot_serial,create_date,std_duration) values
                      (myworkorderid,mynowdatetime,mynodeid,myempid,prodnum,iotdursecond1,iotserial,mynowdatetime,stdduration) ;
                      update alldo_gh_iot_workorder set prod_num = coalesce(prod_num,0) + prodnum,write_date=mynowdatetime where id = myworkorderid ;
                     insert into alldo_gh_iot_equipment_iot_data(iot_id,iot_datetime,iot_owner,iot_workorder,iot_num,iot_serial,create_date) values
                     (mynodeid,mynowdatetime,myempid,myworkorderid,prodnum,iotserial,mynowdatetime) ; 
                     update alldo_gh_iot_workorder set prod_duration=coalesce(prod_duration,0)+iotdurmin1,prod_num=coalesce(prod_num,0)+prodnum,write_date=mynowdatetime 
                         where id = myworkorderid ;
                     update alldo_gh_iot_workorder set prod_date=mynowdatetime where id = myworkorderid ;
                     update maintenance_equipment set iot_status='2',write_date=mynowdatetime where id = mynodeid ;
                     update maintenance_equipment set iot_start_datetime=mynowdatetime where iot_start_datetime is null and id = mynodeid ;  
                     execute genworkorderqcline(myworkorderid,mynowdatetime::DATE,mynodeid,prodnum,myempid) ;
                     execute wkorderwip(myworkorderid,prodnum) ;
                     execute genpowkorder(myworkorderid,prodnum) ;
                     execute getmogoodnum(myworkorderid) ;
                  end if ; 
              end if ;    
           END;$BODY$
           LANGUAGE plpgsql ;""")


        self.env.cr.execute("""drop function if exists checkdbinfo(mynodeno varchar) cascade""")
        self.env.cr.execute("""create or replace function checkdbinfo(mynodeno varchar) returns Integer as $BODY$
           DECLARE
             ncount int ;
             myres Integer ;
             mynodeid int ;
           BEGIN
             /* select id into mynodeid from maintenance_equipment where equipment_no=mynodeno ;
              if mynodeid is not null then
                update maintenance_equipment set iot_status='1' where id=mynodeid ;
             end if ; */
             select count(*) into myres from maintenance_equipment ;
             if myres is null then
                myres = 0 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;  """)

        self.env.cr.execute("""drop function if exists getnodewkorder(mynodeno varchar) cascade""")
        self.env.cr.execute("""create or replace function getnodewkorder(mynodeno varchar) returns varchar as $BODY$
           DECLARE
             myequipid int ;
             myprodid int ;
             mywkorderid int ;
             myres varchar ;
             myname varchar ;
             myproductname varchar ;
             myengtype varchar ;
             myiotstatus char ;
             myprodtmplid int ;
           BEGIN
             select id,iot_status into myequipid,myiotstatus from maintenance_equipment where equipment_no = mynodeno ;
             if myequipid is not null then
                select iot_workorder into mywkorderid from alldo_gh_iot_equipment_iot_status where 
                id = (select max(id) from alldo_gh_iot_equipment_iot_status where iot_id=myequipid and iot_datetime::DATE = now()::DATE)  ;
                select name,product_no,eng_type into myname,myprodid,myengtype from alldo_gh_iot_workorder where id = mywkorderid ;
                select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
                select name into myproductname from product_template where id = mtprodtmplid ;
                myres = concat(myname,'-',myproductname,'-',myengtype) ; 
             else
                myres = 'NOTHING' ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwkordertotal(mywkorderno varchar) cascade""")
        self.env.cr.execute("""create or replace function getwkordertotal(mywkorderno varchar) returns Float as $BODY$
           DECLARE
             myres Float ;
           BEGIN
             select order_num into myres from alldo_gh_iot_workorder where name=mywkorderno ;
             if myres is null then
                myres = 0.0 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwkorderrealtot(mywkorderno varchar) cascade""")
        self.env.cr.execute("""create or replace function getwkorderrealtot(mywkorderno varchar) returns Float as $BODY$
           DECLARE
             myres Float ;
           BEGIN
             select order_num into myres from alldo_gh_iot_workorder where name=mywkorderno ;
             if myres is null then
                myres = 0.0 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists checkprodqcline(myprodid int) cascade""")
        self.env.cr.execute("""create or replace function checkprodqcline(myprodid int) returns Boolean as $BODY$
           DECLARE
           ins_cur refcursor ;
           ins_rec record ;
           ncount int ;
           myres Boolean ;
           BEGIN
             myres := True ; 
             open ins_cur for select eng_type from alldo_gh_iot_workorder_inspect where product_id=myprodid ;
             loop
                fetch ins_cur into ins_rec ;
                exit when not found ;
                select count(*) into ncount from alldo_gh_iot_eng_order AA where TRIM(AA.eng_type) like TRIM(ins_rec.eng_type) and
                   AA.prod_id=myprodid ;
                if ncount = 0 then
                   myres := False ;
                end if ;  
             end loop ;
             close ins_cur ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setworkordercomplete(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function setworkordercomplete(wkorderid int) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             update alldo_gh_iot_workorder set state='4',write_date=mynowdatetime where id = wkorderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genstopduration(mywkorderid int,mynodeid int) cascade""")
        self.env.cr.execute("""create or replace function genstopduration(mywkorderid int,mynodeid int) returns void as $BODY$
           DECLARE
             mywkstopdur float ;
             myiotstopdur  float ;
             mynowdatetime timestamp ;
             wk_cur refcursor ;
             wk_rec record ;
             iotstopdt timestamp ;
             stoparr TEXT[] := ARRAY[]::TEXT[];
             startarr TEXT[] := ARRAY[]::TEXT[];
             stopflag Boolean ;
             myloop int ;
             wkloop int ;
             mystopdatetime timestamp ;
             mystartdatetime timestamp ;
             iotdurmin float ;
             iotdurhour float;
             iotdurday float ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             /*  整個工單 */
             select count(*) into wkloop from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and node_status in ('2','3') ;
             if wkloop > 0 then  
                 stopflag := False ;
                 open wk_cur for select * from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                     order_id = mywkorderid  order by id ;
                 loop
                   fetch wk_cur into wk_rec ;
                   exit when not found ;
                   if wk_rec.node_status in ('2','3') and stopflag=False then
                      stoparr = array_append(stoparr,wk_rec.node_datetime::TEXT) ;
                      stopflag := True ;
                   end if ;
                   if wk_rec.node_status='1'  and stopflag=True then
                      startarr = array_append(startarr,wk_rec.node_datetime::TEXT) ;
                      stopflag := False ;
                   end if ;
                 end loop ; 
                 close wk_cur ;
                select coalesce(array_length(stoparr,1),0) into wkloop ;  
                 myloop = 1 ;
                 mywkstopdur = 0;
                 loop
                   exit when myloop > wkloop ;
                   select stoparr[myloop] into mystopdatetime ;
                   select startarr[myloop] into mystartdatetime ;
                   if  mystartdatetime is null then
                       mystartdatetime = mynowdatetime ;
                   end if ;
                   select extract(minute from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurmin ;
                   select extract(hours from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurhour ;  
                   select extract(days from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurday ;
                   mywkstopdur = mywkstopdur + (iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60)) ;
                   myloop = myloop + 1 ;
                 end loop ;
                 update alldo_gh_iot_workorder set stop_duration=mywkstopdur where id = mywkorderid ;
             end if ;   
             /* 分機台計算 */
             select count(*) into wkloop from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and iot_node=mynodeid and node_status in ('2','3') ;
             if wkloop > 0 then  
                 stopflag := False ;
                 open wk_cur for select * from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                     order_id = mywkorderid and iot_node=mynodeid order by id ;
                 loop
                   fetch wk_cur into wk_rec ;
                   exit when not found ;
                   if wk_rec.node_status in ('2','3') and stopflag=False then
                      stoparr = array_append(stoparr,wk_rec.node_datetime::TEXT) ;
                      stopflag := True ;
                   end if ;
                   if wk_rec.node_status='1' and stopflag=True then
                      startarr = array_append(startarr,wk_rec.node_datetime::TEXT) ;
                      stopflag := False ;
                   end if ;
                 end loop ;  
                 close wk_cur ; 
                 myloop = 1 ;
                 select coalesce(array_length(stoparr,1),0) into wkloop ; 
                 myiotstopdur = 0;
                 loop
                   exit when myloop > wkloop ;
                   select stoparr[myloop] into mystopdatetime ;
                   select startarr[myloop] into mystartdatetime ;
                   if  mystartdatetime is null then
                       mystartdatetime = mynowdatetime ;
                   end if ;
                   select extract(minute from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurmin ;
                   select extract(hours from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurhour ;  
                   select extract(days from (select age(mystartdatetime::TIMESTAMP,mystopdatetime::TIMESTAMP))) into iotdurday ;
                   myiotstopdur = myiotstopdur + (iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60)) ;
                   myloop = myloop + 1 ;
                 end loop ;
                 update maintenance_equipment set stop_duration=myiotstopdur where id = mynodeid ;
             end if ;       
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genstartduration(mywkorderid int,mynodeid int) cascade""")
        self.env.cr.execute("""create or replace function genstartduration(mywkorderid int,mynodeid int) returns void as $BODY$
           DECLARE
             mywkstartdur float ;
             myiotstartdur  float ;
             mynowdatetime timestamp ;
             wk_cur refcursor ;
             wk_rec record ;
             stoparr TEXT[] := ARRAY[]::TEXT[];
             startarr TEXT[] := ARRAY[]::TEXT[];
             startflag Boolean ;
             myloop int ;
             wkloop int ;
             mystopdatetime timestamp ;
             mystartdatetime timestamp ;
             iotdurmin float ;
             iotdurhour float;
             iotdurday float ;
           BEGIN
             select current_timestamp  into mynowdatetime ;
             /*  整個工單 */
             select count(*) into wkloop from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and node_status = '1' ;
             if wkloop > 0 then  
                 startflag := False ;
                 open wk_cur for select * from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                     order_id = mywkorderid  order by id ;
                 loop
                   fetch wk_cur into wk_rec ;
                   exit when not found ;
                   if wk_rec.node_status ='1' and startflag=False then
                      startarr = array_append(startarr,wk_rec.node_datetime::TEXT) ;
                      startflag := True ;
                   end if ;
                   if wk_rec.node_status in ('2','3')  and startflag=True then
                      stoparr = array_append(startarr,wk_rec.node_datetime::TEXT) ;
                      startflag := False ;
                   end if ;
                 end loop ;  
                 close wk_cur ; 
                 myloop = 1 ;
                 select coalesce(array_length(startarr,1),0) into wkloop ;
                 mywkstartdur = 0;
                 loop
                   exit when myloop > wkloop ;
                   select stoparr[myloop] into mystopdatetime ;
                   select startarr[myloop] into mystartdatetime ;
                   if  mystopdatetime is null then
                       mystopdatetime = mynowdatetime ;
                   end if ;
                   select extract(minute from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurmin ;
                   select extract(hours from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurhour ;  
                   select extract(days from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurday ;
                   mywkstartdur = mywkstartdur + (iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60)) ;
                   myloop = myloop + 1 ;
                 end loop ;
                 update alldo_gh_iot_workorder set start_duration=mywkstartdur where id = mywkorderid ;
             end if ;   
             /* 分機台計算 */
             select count(*) into wkloop from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and iot_node=mynodeid and node_status='1' ;
             if wkloop > 0 then  
                 startflag := False ;
                 open wk_cur for select * from alldo_gh_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                     order_id = mywkorderid and iot_node=mynodeid order by id ;
                 loop
                   fetch wk_cur into wk_rec ;
                   exit when not found ;
                   if wk_rec.node_status='1' and startflag=False then
                      startarr = array_append(startarr,wk_rec.node_datetime::TEXT) ;
                      startflag := True ;
                   end if ;
                   if wk_rec.node_status in ('2','3') and startflag=True then
                      stoparr = array_append(stoparr,wk_rec.node_datetime::TEXT) ;
                      startflag := False ;
                   end if ;
                 end loop ;  
                 close wk_cur ; 
                 myloop = 1 ;
                 select coalesce(array_length(startarr,1),0) into wkloop ;
                 myiotstartdur = 0;
                 loop
                   exit when myloop > wkloop ;
                   select stoparr[myloop] into mystopdatetime ;
                   select startarr[myloop] into mystartdatetime ;
                   if  mystopdatetime is null then
                       mystopdatetime = mynowdatetime ;
                   end if ;
                   select extract(minute from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurmin ;
                   select extract(hours from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurhour ;  
                   select extract(days from (select age(mystopdatetime::TIMESTAMP,mystartdatetime::TIMESTAMP))) into iotdurday ;
                   myiotstartdur = myiotstartdur + (iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60)) ;
                   myloop = myloop + 1 ;
                 end loop ;
                 update maintenance_equipment set start_duration=myiotstartdur where id = mynodeid ;
             end if ;       
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewwkorderreport(myuid int) cascade""")
        self.env.cr.execute("""create or replace function gennewwkorderreport(myuid int) returns void as $BODY$
           DECLARE
             myid int ; 
             wk_cur refcursor ;
             wk_rec record ;
             cncprog varchar ;
             mynowdatetime timestamp ;
             myprodtmplid int ;
           BEGIN
             delete from alldo_gh_iot_wkorder_selectitem ;
             select current_timestamp into mynowdatetime ;
             insert into alldo_gh_iot_wkorder_selectitem(report_owner,report_date,create_date) values (myuid,mynowdatetime::DATE,mynowdatetime) ;
             select max(id) into myid from alldo_gh_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_gh_iot_workorder where state='1' ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_gh_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               insert into alldo_gh_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,create_date) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,cncprog,wk_rec.po_no,wk_rec.order_num,wk_rec.blank_num,wk_rec.shipping_date,mynowdatetime) ; 
             end loop ;
             close wk_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldwkorderreport(myuid int,mywizid int) cascade""")
        self.env.cr.execute("""create or replace function genoldwkorderreport(myuid int,mywizid int) returns void as $BODY$
           DECLARE
             myid int ; 
             wk_cur refcursor ;
             wk_rec record ;
             cncprog varchar ;
             mynowdatetime timestamp ;
             myprodtmplid int ;
           BEGIN
             delete from alldo_gh_iot_wkorder_selectitem ;
             select current_timestamp into mynowdatetime ;
             insert into alldo_gh_iot_wkorder_selectitem(report_owner,report_date,create_date) values (myuid,mynowdatetime::DATE,mynowdatetime) ;
             select max(id) into myid from alldo_gh_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_gh_iot_workorder where id in (select wkorder_id from alldo_workorder_newreport_rel where wizard_id = mywizid) ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_gh_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               insert into alldo_gh_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,create_date) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,cncprog,wk_rec.po_no,wk_rec.order_num,wk_rec.blank_num,wk_rec.shipping_date,mynowdatetime) ; 
             end loop ;
             close wk_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getequipmo(nodeid int) cascade""")
        self.env.cr.execute("""create or replace function getequipmo(nodeid int) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            iotstatus char ;
            mymaxid int ;
            statusid int ;
            wkorderid int ;
            mono varchar ;
          BEGIN
            select iot_status,mo_no into iotstatus,wkorderid from maintenance_equipment where id=nodeid ;
            if iotstatus='4' or iotstatus='1' then
               select name into mono from alldo_gh_iot_workorder where id = wkorderid ;
               myres = mono ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists getalliotinfo() cascade""")
        self.env.cr.execute("""create or replace function getalliotinfo() returns setof TEXT[] as $BODY$
           DECLARE
             ncount INTEGER := 0;
             myres TEXT[] := ARRAY[]::TEXT[];
             iot_cur refcursor ;
             iot_rec record ;
             nitem INTEGER := 0;
             iotstatus char ;
             ordernum integer ;
             prodnum integer ;
             tprodnum integer ;
             standardnum integer ;
             opentime float ;
             wkorderid int ;
             wkorder varchar ;
             prodid int ;
             prodtmplid int ;
             prodname varchar ;
             engtype varchar ;
             stdminnum int ;
             nodestatus varchar ;
             mynowdate date ;
             mynowdatetime timestamp ;
             mystartdatetime timestamp ;
             opentimeh int ;
             opentimem int ;
             mymaxid int ;
             empid int ;
             empname varchar ;
             ncount1 int ;
             wkorderid1 int ;
             mymaxid1 int ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select current_timestamp::DATE into mynowdate ;
             mystartdatetime = (concat(mynowdate::TEXT,' 00:00:00'))::timestamp ;
             
             open iot_cur for select * from maintenance_equipment order by sequence,id ;
             loop
               fetch iot_cur into iot_rec ;
               exit when not found ;
               if iot_rec.iot_status='1' or iot_rec.iot_status='4' then
                  iotstatus = '3' ;
               elsif iot_rec.iot_status='2' then
                  iotstatus = '1' ;
               else
                  iotstatus = '2' ;
               end if ;   
               /*  判斷是否架機階段  */   
               select max(id) into mymaxid1 from alldo_gh_iot_wkorder_replaceline where equipment_id=iot_rec.id ;            
               select count(*) into ncount1 from alldo_gh_iot_wkorder_replaceline where equipment_id=iot_rec.id and 
                      id = mymaxid1 and replace_end_datetime is null ;
               if ncount1 > 0 and iot_rec.iot_status='4' then
                   select order_id,replace_owner into wkorderid,empid from alldo_gh_iot_wkorder_replaceline where id = mymaxid1 ;
                   select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_gh_iot_workorder where id = wkorderid ; 
                   iotstatus = '2' ;
               else        
                   select iot_workorder into wkorderid from alldo_gh_iot_equipment_iot_data where 
                       id = (select max(id) from alldo_gh_iot_equipment_iot_data where iot_id=iot_rec.id);
                   select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_gh_iot_workorder where id = wkorderid ;   
                   select max(id) into mymaxid from alldo_gh_iot_workorder_iot_data where order_id=wkorderid and iot_node=iot_rec.id ;
                   select iot_owner into empid from alldo_gh_iot_workorder_iot_data where id = mymaxid ; 
                   if iot_rec.iot_status='1' or iot_rec.iot_status='4' then
                      iotstatus = '3' ;
                   else
                      iotstatus = '1' ;
                   end if ;   
               end if ;         
               select name into empname from hr_employee where id = empid ;
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select default_code into prodname from product_template where id = prodtmplid ;
               if prodname is null then
                  prodname = ' ' ;
               end if ;
               /* wkorder = concat(wkorder,'-',prodname) ; */
               select sum(iot_num) into prodnum from alldo_gh_iot_equipment_iot_data where iot_id=iot_rec.id and iot_workorder=wkorderid ;
               select sum(iot_num) into tprodnum from alldo_gh_iot_equipment_iot_data where iot_id=iot_rec.id and iot_workorder=wkorderid 
                 and iot_datetime::DATE = now()::DATE ;
               nodestatus = 'OK' ;  
               /*   計算開工時間 及 停機時間   */
               execute genstartduration(wkorderid,iot_rec.id) ;
               execute genstopduration(wkorderid,iot_rec.id) ;
               /* **********************   */ 
               /* opentime = coalesce(iot_rec.start_duration,0) - coalesce(iot_rec.stop_duration,0) ; */
               select date_part('hours',age(mynowdatetime,mystartdatetime))::INTEGER into opentimeh ;
               if opentimeh >= 5 then
                  opentimeh = opentimeh - 1 ;    /* 中午午休 不算 */ 
               end if ;   
               select date_part('minutes',age(mynowdatetime,mystartdatetime))::INTEGER into opentimem ;
               opentime = (opentimeh * 60) + opentimem ;
               
               select standard_num into standardnum from alldo_gh_iot_eng_order where prod_id=prodtmplid and TRIM(eng_type) like TRIM(engtype) ;
               select round((standardnum::numeric/60::numeric)*opentime::numeric,0) into stdminnum;
               
               myres := ARRAY[]::TEXT[] ;
               /* if iotstatus = '3' then
                  select getequipmo(iot_rec.id) into wkorder ;
                
                  if wkorder is not null then
                     iotstatus='2' ;
                     select mo_no into wkorderid from maintenance_equipment where id = iot_rec.id ;
                     select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_gh_iot_workorder where id = wkorderid ;   
                     select product_tmpl_id into prodtmplid from product_product where id = prodid ;
                     select default_code into prodname from product_template where id = prodtmplid ;
                  end if ;
              
                  prodnum = null ; 
                  stdminnum = null ;
                  tprodnum = null ;
                  nodestatus = null ;
                  empname = null ;
               end if ; */
               myres = array_append(myres,iot_rec.equipment_no::TEXT) ;
               myres = array_append(myres,iotstatus::TEXT) ;
               myres = array_append(myres,coalesce(wkorder::TEXT,'')) ;
               myres = array_append(myres,coalesce(ordernum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(prodnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(stdminnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(tprodnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(nodestatus::TEXT,'')) ; 
               myres = array_append(myres,coalesce(prodname::TEXT,'')) ;
               myres = array_append(myres,coalesce(empname::TEXT,'')) ;
               return next myres ;
             end loop ;
             close iot_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getarraytest() cascade""")
        self.env.cr.execute("""create or replace function getarraytest() returns setof TEXT[] as $BODY$
           DECLARE
             var1 varchar;
             var2 varchar;
             var3 varchar;
             myres TEXT[] := ARRAY[]::TEXT[];
             nitem int := 0 ;
           BEGIN
             loop
                 exit when nitem = 9 ;
                 myres := ARRAY[]::TEXT[] ;
                 myres = array_append(myres,(nitem*10)::TEXT) ;
                 myres = array_append(myres,(nitem*11)::TEXT) ;
                 myres = array_append(myres,(nitem*12)::TEXT) ;
                 myres = array_append(myres,(nitem*13)::TEXT) ;
                 myres = array_append(myres,(nitem*14)::TEXT) ;
                 nitem = nitem + 1 ;
                 return next myres ;
             end loop;    
            
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setprodengorder(prodid int) cascade""")
        self.env.cr.execute("""create or replace function setprodengorder(prodid int) returns void as $BODY$
           DECLARE
             myprodtmplid int;
             nitem int ;
             eng_cur refcursor ;
             eng_rec record ;
             mynowdatetime timestamp ;
           BEGIN
             nitem = 1 ;
             select current_timestamp into mynowdatetime ;
             open eng_cur for select * from alldo_gh_iot_eng_order where prod_id = prodid  order by sequence,id;
             loop
               fetch eng_cur into eng_rec ;
               exit when not found ;
               update alldo_gh_iot_eng_order set eng_order=nitem,write_date=mynowdatetime where id = eng_rec.id ;
               nitem = nitem + 1 ;
             end loop ;
             close eng_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodengorder(prodid int,engtype varchar) cascade""")
        self.env.cr.execute("""create or replace function getprodengorder(prodid int,engtype varchar) returns char as $BODY$
           DECLARE
             myres char ;
             mymaxid int ;
             myprodtmplid int ;
             myengorder int ;
             myengcount int ;
             ispackage Boolean ;
           BEGIN
             select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
             select count(*) into myengcount from alldo_gh_iot_eng_order where prod_id = myprodtmplid ;
             select max(eng_order) into mymaxid from alldo_gh_iot_eng_order where prod_id = myprodtmplid and (is_package is null or is_package = False) ;
             select coalesce(is_package,False) into ispackage from alldo_gh_iot_eng_order where prod_id= myprodtmplid and TRIM(eng_type) like TRIM(engtype) ;
             select eng_order into myengorder from alldo_gh_iot_eng_order where prod_id= myprodtmplid and TRIM(eng_type) like TRIM(engtype) ;
             if myengorder = 1 then
                myres = '1' ;
             elsif myengorder <= mymaxid then
                myres = '2' ;
             else
                myres = '3' ;
             end if ;                   
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodengseq(prodid int,engtype varchar) cascade""")
        self.env.cr.execute("""create or replace function getprodengseq(prodid int,engtype varchar) returns int as $BODY$
          DECLARE
            myres int ;
            mymaxid int ;
            myprodtmplid int ;
            myengorder int ;
          BEGIN
            select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
            select max(eng_order) into mymaxid from alldo_gh_iot_eng_order where prod_id = myprodtmplid ;
            select eng_order into myres from alldo_gh_iot_eng_order where prod_id= myprodtmplid and 
               TRIM(eng_type) like TRIM(engtype) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getnextwkorder(wkorderid int) cascade;""")
        self.env.cr.execute("""create or replace function getnextwkorder(wkorderid int) returns int as $BODY$
           DECLARE
             myres int ;
             mypono varchar ;
             prodid int ;
             engseq int ;
             engorder char ;
             mogroupid int ;
           BEGIN
             select po_no,eng_seq,eng_order,product_no,mo_group_id into mypono,engseq,engorder,prodid,mogroupid from alldo_gh_iot_workorder 
                    where id = wkorderid ;
             if engorder != '3' then
                select id into myres from alldo_gh_iot_workorder where mo_group_id=mogroupid and eng_seq = engseq + 1 ;
             else
                myres := 0 ;
             end if ; 
             if myres is null then
                myres = 0 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getlastwkorder(wkorderid int) cascade;""")
        self.env.cr.execute("""create or replace function getlastwkorder(wkorderid int) returns int as $BODY$
           DECLARE
             myres int ;
             mypono varchar ;
             prodid int ;
             engseq int ;
             engorder char ;
           BEGIN
             select po_no,eng_seq,eng_order,product_no into mypono,engseq,engorder,prodid from alldo_gh_iot_workorder 
                    where id = wkorderid ;
             if engorder != '1' then
                select id into myres from alldo_gh_iot_workorder where po_no=mypono and product_no=prodid and eng_seq = engseq - 1 ;
             else
                myres := 0 ;
             end if ; 
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckisoutsourcing(prodtmplid int,engseq int) cascade""")
        self.env.cr.execute("""create or replace function ckisoutsourcing(prodtmplid int,engseq int) returns Boolean as $BODY$
           DECLARE
             myres Boolean ;
           BEGIN
             select is_outsourcing into myres from alldo_gh_iot_eng_order where prod_id = prodtmplid and eng_order=engseq ;
             if myres is null then
                myres := false ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckispackage(prodtmplid int,engseq int) cascade""")
        self.env.cr.execute("""create or replace function ckispackage(prodtmplid int,engseq int) returns Boolean as $BODY$
           DECLARE
             myres Boolean ;
           BEGIN
             select coalesce(is_package,False) into myres from alldo_gh_iot_eng_order where prod_id = prodtmplid and eng_order=engseq ;
             if myres is null then
                myres := false ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists wkorderwip(wkorderid int,prodnum float) cascade;""")
        self.env.cr.execute("""create or replace function wkorderwip(wkorderid int,prodnum float) returns void as $BODY$
           DECLARE
             ncount int ;
             ncount1 int ; 
             myprodid int ;
             mywkorderno varchar ;
             myengorder char ;
             myintype char ;
             myouttype char ;
             myinloc varchar ;
             myoutloc varchar ;
             mypono varchar ;
             myprodinid int ;
             myprodoutid int ;
             mylastwkid int ;
             mynextwkid int ;
             myengseq int ;
             myprodtmplid int ;
             isoutsourcing Boolean ;
             ispackage Boolean ;
             mynowdatetime timestamp ;
             mynowdate date ;
           BEGIN
             /*  先處理自己工單 wkorder_prodin 的已使用來料 */
             select current_timestamp into mynowdatetime ;
             select mynowdatetime::DATE into mynowdate ;
             select id into myprodinid from alldo_gh_iot_wkorder_prodin where order_id = wkorderid and prodin_datetime::DATE = mynowdate ;         
             select name,product_no,eng_order,po_no,eng_seq into mywkorderno,myprodid,myengorder,mypono,myengseq from alldo_gh_iot_workorder 
                 where id = wkorderid ;
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;    
             if myprodinid is null then
                 if myengorder='1' then  /* 首工序 */
                    myinloc := mypono ;
                    myintype := '1' ;
                 else
                    select getlastwkorder(wkorderid) into mylastwkid ;
                    select name into myinloc from alldo_gh_iot_workorder where id = mylastwkid ;
                    myintype := '2' ;
                 end if ;
                 insert into alldo_gh_iot_wkorder_prodin(order_id,prodin_datetime,product_no,process_num,in_type,in_loc,create_date) values
                      (wkorderid,mynowdatetime,myprodid,prodnum,myintype,myinloc,mynowdatetime) ;
             else
                 update alldo_gh_iot_wkorder_prodin set process_num = coalesce(process_num,0) + prodnum,write_date=mynowdatetime where id = myprodinid ;
             end if ;
             /*  處理 自己工單 的 wkorder_prodout 轉出加工料件 */
             select id into myprodoutid from alldo_gh_iot_wkorder_prodout where order_id = wkorderid and prodout_datetime::DATE = mynowdate ;
             if myprodoutid is null then
                if myengorder='3' then  /* 完工序 */
                    myoutloc := mypono ;
                    myouttype := '1' ;
                 else
                    select getnextwkorder(wkorderid) into mynextwkid ;
                    select name into myoutloc from alldo_gh_iot_workorder where id = mynextwkid ;
                    myouttype := '2' ;
                 end if ;
                insert into alldo_gh_iot_wkorder_prodout(order_id,prodout_datetime,product_no,out_type,out_good_num,out_loc,create_date) values
                  (wkorderid,mynowdatetime,myprodid,myouttype,prodnum,myoutloc,mynowdatetime) ;
             else
                update alldo_gh_iot_wkorder_prodout set out_good_num = coalesce(out_good_num,0) + prodnum,write_date=mynowdatetime where id = myprodoutid ;
             end if ;
             execute genwkamountnum(wkorderid) ;
             /* 處理 下一工序 wkorder_prodin 轉入投料 */
             select ckisoutsourcing(myprodtmplid,myengseq+1) into isoutsourcing ;
             select ckispackage(myprodtmplid,myengseq+1) into ispackage ;
             if myengorder != '3' and isoutsourcing = False and ispackage = False then  /*  如果不是完工序且非委外加工單 即執行 */
                 select getnextwkorder(wkorderid) into mynextwkid ;
                 select id into myprodinid from alldo_gh_iot_wkorder_prodin where order_id = mynextwkid and prodin_datetime::DATE = mynowdate ;
                 myintype := '2' ;
                 if myprodoutid is null then
                   select getlastwkorder(wkorderid) into mylastwkid ;
                   select name into myinloc from alldo_gh_iot_workorder where id = mylastwkid ;       
                   myinloc := mywkorderno ;
                   if mynextwkid > 0 then
                      insert into alldo_gh_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_type,in_loc,create_date) values
                          (mynextwkid,mynowdatetime,myprodid,prodnum,myintype,myinloc,mynowdatetime) ;
                   end if ;       
                 else
                    update alldo_gh_iot_wkorder_prodin set in_good_num = coalesce(in_good_num,0) + prodnum,write_date=mynowdatetime,in_type=myintype where id = myprodinid ;
                 end if ;
             end if ;    
             execute genwkamountnum(mynextwkid);
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getiotlastinfo(nodeid int) cascade""")
        self.env.cr.execute("""create or replace function getiotlastinfo(nodeid int) returns varchar as $BODY$
           DECLARE
             myres varchar ;
             mywkorderid int ;
             myempid int ;
             myempcode varchar ;
             mywkordername varchar ;
           BEGIN
             select order_id,iot_owner into mywkorderid,myempid from alldo_gh_iot_wkorder_iot_data where 
                     id = (select max(id) from alldo_gh_iot_workorder_iot_data where iot_node=nodeid) ;
             select coalesce(name,' ') into mywkordername from alldo_gh_iot_workorder where id = mywkorderid ;
             select coalesce(emp_code,' ') into myempcode from hr_employee where id = myempid ;        
             myres = concat(mywkordername,'-',myempcode) ;
             return myres ;  
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists createpowkorder(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function createpowkorder(wkorderid int) returns void as $BODY$
           DECLARE
             mypono int ;
             mysono int ;
             mycusno int ;
             myprodid int ;
             ncount int ;
             myponum float ;
             myblanknum float ;
             myengseq int ;
             myengorder char ;
             myengtype varchar;
             mypoid int ;
             myshipdate date;
             mynowdatetime timestamp ;
           BEGIN
            select current_timestamp into mynowdatetime ;
             select po_no1,so_no,cus_name,product_no,order_num,blank_num,eng_order,eng_seq,eng_type,shipping_date into 
                mypoid,mysono,mycusno,myprodid,myponum,myblanknum,myengorder,myengseq,myengtype,myshipdate
                  from alldo_gh_iot_workorder where id = wkorderid ;
             /* if mypoid is null then
                insert into alldo_gh_iot_po_wkorder(so_no,cus_name,product_no,po_num,blank_num,shipping_date,state,create_date) values 
                   (mysono,mycusno,myprodid,myponum,myblanknum,myshipdate,'1',mynowdatetime) ;
                select id into mypoid from alldo_gh_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             end if ; */
             if mypoid is not null then
                 insert into alldo_gh_iot_po_wkorder_line(po_id,wkorder_id,eng_seq,eng_order,eng_type,create_date) values  
                     (mypoid,wkorderid,myengseq,myengorder,myengtype,mynowdatetime) ; 
             end if ;        
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpowkorder(wkorderid int,prodnum float) cascade""")
        self.env.cr.execute("""create or replace function genpowkorder(wkorderid int,prodnum float) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
             poid int ;
           BEGIN
             select current_timestamp into mynowdatetime ; 
             select count(*) into ncount from alldo_gh_iot_po_wkorder_line where wkorder_id=wkorderid ;
             if ncount > 0 then
                update alldo_gh_iot_po_wkorder_line set complete_num=coalesce(complete_num,0)+prodnum,write_date=mynowdatetime where wkorder_id=wkorderid ;
                select max(po_id) into poid from alldo_gh_iot_po_wkorder_line where wkorder_id=wkorderid ;
                update alldo_gh_iot_po_wkorder set state='2' where id = poid ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpoprod(poid int) cascade""")
        self.env.cr.execute("""create or replace function getpoprod(poid int) returns int as $BODY$
           DECLARE
             ncount int ;
             myres int ;
           BEGIN
             select count(*) into ncount from alldo_gh_iot_po_wkorder where id=poid ;
             if ncount > 0 then
                select product_no into myres from alldo_gh_iot_po_wkorder where id=poid ;
             else
                myres = 0 ;   
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists getponum(poid int) cascade""")
        self.env.cr.execute("""create or replace function getponum(poid int) returns float as $BODY$
           DECLARE
             myid int ;
             myres float ;
           BEGIN
             select (coalesce(complete_num,0) - coalesce(ng_num,0)) into myres from alldo_gh_iot_po_wkorder_line where po_id=poid
               and eng_order='3' ;
             if myres is null then
               myres = 0.00 ;
             end if ;   
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql""")


        self.env.cr.execute("""drop function if exists genpowkorderngnum(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function genpowkorderngnum(wkorderid int) returns void as $BODY$
           DECLARE
             myngnum float ;
             mynowdatetime timestamp ;
             mytotnum float ;
             mycompletenum float ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)+coalesce(loss_num,0)),sum(coalesce(total_amount_num,0)) into myngnum,mytotnum from alldo_gh_iot_workorder_qc
                where order_id=wkorderid ;
             mycompletenum = mytotnum - myngnum ;   
             update alldo_gh_iot_po_wkorder_line set ng_num=myngnum,complete_num=mycompletenum,write_date=mynowdatetime where wkorder_id=wkorderid ;  
             update alldo_gh_iot_workorder set new_ng_num=myngnum,ng_complete=False where id = wkorderid ;
           END;$BODY$
           LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists genselectitemreport() cascade""")
        self.env.cr.execute("""create or replace function genselectitemreport() returns void as $BODY$
           DECLARE
             sel_cur refcursor ;
             sel_rec record ;
             ins_cur refcursor ;
             ins_rec record ;
             myprodtmplid int ;
             myprodcode varchar ;
             myprodblank varchar ;
             myblankno int ;
             mynewrecid int ;
             nitem int := 1 ;
             myclamppower varchar ;
             mystandardnum int ;
             myinscode varchar ;
             workordermemo varchar ;
           BEGIN
             delete from alldo_gh_iot_wkorder_printsheet ;
             open sel_cur for select * from alldo_gh_iot_wkorder_selectitem_line ;
             loop
               fetch sel_cur into sel_rec ;
               exit when not found ;
               select workorder_memo,blank_no into workordermemo,myblankno from alldo_gh_iot_workorder where name=sel_rec.name ;
               select product_tmpl_id into myprodtmplid from product_product where id = sel_rec.product_no ;
               select default_code into myprodcode from product_template where id = myprodtmplid ;
               select default_code into myprodblank from product_product where id = myblankno ;
               select clamping_power,standard_num into myclamppower,mystandardnum from alldo_gh_iot_eng_order where 
                 prod_id=myprodtmplid and TRIM(sel_rec.eng_type)=TRIM(eng_type) ;
               insert into alldo_gh_iot_wkorder_printsheet (name,product_no,product_blank,po_no,order_num,blank_num,eng_type,cnc_prog,shipping_date,
               clamping_power,standard_num,workorder_memo) values (sel_rec.name,myprodcode,myprodblank,sel_rec.po_no,sel_rec.order_num::NUMERIC,
               sel_rec.blank_num::NUMERIC,sel_rec.eng_type,sel_rec.cnc_prog,sel_rec.shipping_date,myclamppower,mystandardnum,workordermemo) ;
                 select max(id) into mynewrecid from alldo_gh_iot_wkorder_printsheet ;
               nitem = 1 ;  
               open ins_cur for select * from alldo_gh_iot_workorder_inspect where product_id=myprodtmplid and 
                   TRIM(sel_rec.eng_type) = TRIM(eng_type) order by sequence,id;
               loop
                 fetch ins_cur into ins_rec ;
                 exit when not found ;
                 select inspect_code into myinscode from alldo_gh_iot_measure_tool where id = ins_rec.inspect_tool ;
                 if nitem = 1 then
                    update alldo_gh_iot_wkorder_printsheet set ins1_name=ins_rec.inspect_name,ins1_size=ins_rec.inspect_size,ins1_tolerance=ins_rec.drawing_tolerance,
                    ins1_real_size=ins_rec.real_work_size,ins1_testtype=ins_rec.inspect_point,ins1_testmode=myinscode,correct_no1=ins_rec.correct_no,inspect_tool1=ins_rec.inspect_tool,
                     inspect1_point=ins_rec.inspect_point where id = mynewrecid ;
                 elsif nitem = 2 then
                    update alldo_gh_iot_wkorder_printsheet set ins2_name=ins_rec.inspect_name,ins2_size=ins_rec.inspect_size,ins2_tolerance=ins_rec.drawing_tolerance,
                    ins2_real_size=ins_rec.real_work_size,ins2_testtype=ins_rec.inspect_point,ins2_testmode=myinscode,correct_no2=ins_rec.correct_no,inspect_tool2=ins_rec.inspect_tool,
                     inspect2_point=ins_rec.inspect_point where id = mynewrecid ;
                 elsif nitem = 3 then
                    update alldo_gh_iot_wkorder_printsheet set ins3_name=ins_rec.inspect_name,ins3_size=ins_rec.inspect_size,ins3_tolerance=ins_rec.drawing_tolerance,
                    ins3_real_size=ins_rec.real_work_size,ins3_testtype=ins_rec.inspect_point,ins3_testmode=myinscode,correct_no3=ins_rec.correct_no,inspect_tool3=ins_rec.inspect_tool,
                     inspect3_point=ins_rec.inspect_point where id = mynewrecid ;
                 elsif nitem = 4 then
                    update alldo_gh_iot_wkorder_printsheet set ins4_name=ins_rec.inspect_name,ins4_size=ins_rec.inspect_size,ins4_tolerance=ins_rec.drawing_tolerance,
                    ins4_real_size=ins_rec.real_work_size,ins4_testtype=ins_rec.inspect_point,ins4_testmode=myinscode,correct_no4=ins_rec.correct_no,inspect_tool4=ins_rec.inspect_tool,
                     inspect4_point=ins_rec.inspect_point where id = mynewrecid ;
                 else
                    update alldo_gh_iot_wkorder_printsheet set ins5_name=ins_rec.inspect_name,ins5_size=ins_rec.inspect_size,ins5_tolerance=ins_rec.drawing_tolerance,
                    ins5_real_size=ins_rec.real_work_size,ins5_testtype=ins_rec.inspect_point,ins5_testmode=myinscode,correct_no5=ins_rec.correct_no,inspect_tool5=ins_rec.inspect_tool,
                     inspect5_point=ins_rec.inspect_point where id = mynewrecid ;
                 end if ;
                
                 nitem = nitem + 1 ;
               end loop ;
               close ins_cur ;
                if sel_rec.blank_input_date is not null then
                    update alldo_gh_iot_wkorder_printsheet set blank_input_date=sel_rec.blank_input_date where id = mynewrecid ;
                 end if ;
             end loop ;
             close sel_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genselectitemreport1() cascade""")
        self.env.cr.execute("""create or replace function genselectitemreport1() returns void as $BODY$
           DECLARE
             sel_cur refcursor ;
             sel_rec record ;
             ins_cur refcursor ;
             ins_rec record ;
             myprodtmplid int ;
             myprodcode varchar ;
             myprodblank varchar ;
             mynewrecid int ;
             nitem int := 1 ;
             myclamppower varchar ;
             mystandardnum int ;
             myinscode varchar ;
             workordermemo varchar ;
             ncount int ;
             shippingdate DATE ;
             blankinputdate DATE ;
             myproductdesc varchar ;
           BEGIN
             delete from alldo_gh_iot_wkorder_printsheet1 ;
             open sel_cur for select * from alldo_gh_iot_wkorder_selectitem_line1 ;
             loop
               fetch sel_cur into sel_rec ;
               exit when not found ;
               select workorder_memo,shipping_date,blank_input_date into workordermemo,shippingdate,blankinputdate from alldo_gh_iot_workorder where name=sel_rec.name ;
               select product_tmpl_id into myprodtmplid from product_product where id = sel_rec.product_no ;
               select default_code,product_blank,coalesce(description,' ') into myprodcode,myprodblank,myproductdesc from product_template where id = myprodtmplid ;
               select clamping_power,standard_num into myclamppower,mystandardnum from alldo_gh_iot_eng_order where 
                 prod_id=myprodtmplid and TRIM(sel_rec.eng_type)=TRIM(eng_type) ;
               select count(*) into ncount from alldo_gh_iot_wkorder_printsheet1 ;
               if ncount = 0 then
                  insert into alldo_gh_iot_wkorder_printsheet1(product_no,order_num,blank_num,shipping_date,blank_input_date,productdesc) values (myprodcode,sel_rec.order_num::NUMERIC,
                      sel_rec.blank_num::NUMERIC,shippingdate::DATE,blankinputdate::DATE,myproductdesc) ;
               end if ;
               select max(id) into mynewrecid from alldo_gh_iot_wkorder_printsheet1 ;
               if nitem=1 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name1=sel_rec.name where id = mynewrecid;
               elsif nitem = 2 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name2=sel_rec.name where id = mynewrecid;
               elsif nitem = 3 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name3=sel_rec.name where id = mynewrecid;
               elsif nitem = 4 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name4=sel_rec.name where id = mynewrecid;
               elsif nitem = 5 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name5=sel_rec.name where id = mynewrecid;
               elsif nitem = 6 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name6=sel_rec.name where id = mynewrecid;
               elsif nitem = 7 then
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name7=sel_rec.name where id = mynewrecid;
               else
                  update alldo_gh_iot_wkorder_printsheet1 set wk_name8=sel_rec.name where id = mynewrecid;
               end if ;
               nitem = nitem + 1 ;
             end loop ;
             close sel_cur ;  
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkorderreport(myuid int,mywkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkorderreport(myuid int,mywkid int) returns void as $BODY$
           DECLARE
             myid int ; 
             wk_cur refcursor ;
             wk_rec record ;
             cncprog varchar ;
             mynowdatetime timestamp ;
             myprodtmplid int ;
             mymaxid int ;
             pono varchar ;
           BEGIN     
             select current_timestamp  into mynowdatetime ;
             insert into alldo_gh_iot_wkorder_selectitem(report_owner,report_date) values (myuid,mynowdatetime::DATE) ;
             select max(id) into myid from alldo_gh_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_gh_iot_workorder where id=mywkid ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_gh_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               select getwkorderpono(wk_rec.id) into pono ;
               insert into alldo_gh_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,select_yn) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,cncprog,pono,wk_rec.order_num,wk_rec.blank_num,wk_rec.shipping_date,True) ; 
               select max(id) into mymaxid from  alldo_gh_iot_wkorder_selectitem_line ;
               if wk_rec.blank_input_date is not null then
                  update alldo_gh_iot_wkorder_selectitem_line set blank_input_date=wk_rec.blank_input_date where id = mymaxid ;
               end if ;
             end loop ;
             close wk_cur ;
             update alldo_gh_iot_workorder set state='2' where id=mywkid and state = '1' ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkorderreport1(myuid int,mywkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkorderreport1(myuid int,mywkid int) returns void as $BODY$
           DECLARE
             myid int ; 
             wk_cur refcursor ;
             wk_rec record ;
             cncprog varchar ;
             mynowdatetime timestamp ;
             myprodtmplid int ;
             mymaxid int ;
           BEGIN
             select current_timestamp  into mynowdatetime ;
             select max(id) into myid from alldo_gh_iot_wkorder_selectitem1 ;
             update alldo_gh_iot_wkorder_selectitem1 set report_date=mynowdatetime::DATE where id = myid ;
             open wk_cur for select * from alldo_gh_iot_workorder where id=mywkid ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_gh_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               insert into alldo_gh_iot_wkorder_selectitem_line1(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,select_yn) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,cncprog,wk_rec.po_no,wk_rec.order_num,wk_rec.blank_num,wk_rec.shipping_date,True) ; 
               select max(id) into mymaxid from  alldo_gh_iot_wkorder_selectitem_line ;
               if wk_rec.blank_input_date is not null then
                  update alldo_gh_iot_wkorder_selectitem_line1 set blank_input_date=wk_rec.blank_input_date where id = mymaxid ;
               end if ;
             end loop ;
             close wk_cur ;
             update alldo_gh_iot_workorder set state='2' where id=mywkid and state = '1' ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getsonoseq(soid int) cascade""")
        self.env.cr.execute("""create or replace function getsonoseq(soid int) returns void as $BODY$
           DECLARE
             myres varchar ;
             myseq int ;
             myyear varchar ;
             ncount int ;
             myyear1 varchar;
             myid int ;
             prefixcode varchar ;
             mypartnerid int ;
           BEGIN
             select partner_id into mypartnerid from sale_order where id = soid ;
             select coalesce(so_prefixcode,' ') into prefixcode from res_partner where id = mypartnerid ;
             select date_part('year',now())::TEXT into myyear ;
             select substr(myyear,3,2) into myyear1 ;
             select id into myid from alldo_gh_iot_so_sequence where so_prefixcode=prefixcode and so_year=myyear ;
             if myid is null then
                myres = concat(prefixcode,myyear1,'001') ;
                insert into alldo_gh_iot_so_sequence(so_prefixcode,so_year,so_seq) values (prefixcode,myyear,2) ;
             else
                select coalesce(so_seq,0) into myseq from alldo_gh_iot_so_sequence where id = myid ;
                myres = concat(prefixcode,myyear1,LPAD((myseq+1)::TEXT,3,'0')) ;
                update alldo_gh_iot_so_sequence set so_seq=coalesce(so_seq,0) + 1 where id = myid;
             end if ;
             update sale_order set name=myres where id = soid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getsoprodnum(soid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getsoprodnum(soid int,prodid int) returns float as $BODY$
           DECLARE
             myres float ;
           BEGIN
             select coalesce(product_uom_qty,0) into myres from sale_order_line where order_id=soid and product_id=prodid ;
             if myres is null then
                myres = 0.0 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists cksoiswkopen(soid int) cascade""")
        self.env.cr.execute("""create or replace function cksoiswkopen(soid int) returns void as $BODY$
           DECLARE
             myres Boolean ;
             ncount int ;
           BEGIN
             select count(*) into ncount from sale_order_line where order_id=soid and is_openwkorder=False ;
             if ncount > 0 then
                myres := False ;
             else
                myres := True ;
             end if ; 
             update sale_order set is_openwkorder=myres where id=soid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getnonopenwkso(soid int) cascade""")
        self.env.cr.execute("""create or replace function getnonopenwkso(soid int) returns INT[] as $BODY$
           DECLARE
              myres INT[] := ARRAY[]::INT[];
             so_cur refcursor ;
             so_rec record ;
           BEGIN
             open so_cur for select id,product_id from sale_order_line where order_id = soid and is_openwkorder=False ;
             loop
               fetch so_cur into so_rec ;
               exit when not found ;
               myres = array_append(myres,so_rec.product_id) ;
             end loop ;
             close so_cur ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists createpooutsuborder(outsuborderid int) cascade""")
        self.env.cr.execute("""create or replace function createpooutsuborder(outsuborderid int) returns void as $BODY$
           DECLARE
             mypono int ;
             mysono int ;
             mycusno int ;
             myprodid int ;
             ncount int ;
             myponum float ;
             myblanknum float ;
             myengseq int ;
             myengorder char ;
             myengtype varchar;
             mypoid int ;
             myshipdate date;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select po_no1,so_no,cus_name,product_no,order_num,blank_num,eng_order,eng_seq,eng_type,shipping_date into 
                mypono,mysono,mycusno,myprodid,myponum,myblanknum,myengorder,myengseq,myengtype,myshipdate
                  from alldo_gh_iot_outsuborder where id = outsuborderid ;
             select id into mypoid from alldo_gh_iot_po_wkorder where po_no1=mypono ;
             if mypoid is null then
                insert into alldo_gh_iot_po_wkorder(po_no1,so_no,cus_name,product_no,po_num,blank_num,shipping_date,state,create_date) values 
                   (mypono,mysono,mycusno,myprodid,myponum,myblanknum,myshipdate,'1',mynowdatetime) ;
                select id into mypoid from alldo_gh_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             end if ;
             insert into alldo_gh_iot_po_suborder_line(po_id,outsourcing_id,eng_seq,eng_order,eng_type,create_date) values  
                 (mypoid,outsuborderid,myengseq,myengorder,myengtype,mynowdatetime) ; 
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setoutsubordercomplete(outsuborderid int) cascade""")
        self.env.cr.execute("""create or replace function setoutsubordercomplete(outsuborderid int) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             update alldo_gh_iot_outsuborder set state='3',write_date=mynowdatetime where id = outsuborderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpooutsuborderngnum(outsuborderid int) cascade""")
        self.env.cr.execute("""create or replace function genpooutsuborderngnum(outsuborderid int) returns void as $BODY$
           DECLARE
             myngnum float ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into myngnum from alldo_gh_iot_outsuborder_qc
                where order_id=outsuborderid ;
             update alldo_gh_iot_po_suborder_line set ng_num=myngnum,write_date=mynowdate where outsourcing_id=outsuborderid ;  
           END;$BODY$
           LANGUAGE plpgsql""")


        self.env.cr.execute("""drop function if exists genoutsourcingout(outid int,outownerid int,outnum int) cascade""")
        self.env.cr.execute("""create or replace function genoutsourcingout(outid int,outownerid int,outnum int) returns void as $BODY$
           DECLARE
              mynowdatetime timestamp ;
              myprodid int ;
           BEGIN
              select product_no into myprodid from alldo_gh_iot_outsuborder where id=outid ; 
              select current_timestamp into mynowdatetime ;
              insert into alldo_gh_iot_outsuborder_prodout(order_id,prodout_datetime,product_no,out_good_num,out_owner,create_date)
                 values (outid,mynowdatetime,myprodid,outnum,outownerid,mynowdatetime) ;
              update alldo_gh_iot_outsuborder set order_num=coalesce(order_num,0) + outnum,state='2',write_date=mynowdatetime where id = outid ;    
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists genoutsourcingin(suborderid int,inownerid int,ingoodnum int,inngnum int) cascade""")
        self.env.cr.execute("""drop function if exists genoutsourcingin(suborderid int,inownerid int,ingoodnum int,inngnum int,lossnum int) cascade""")
        self.env.cr.execute("""create or replace function genoutsourcingin(suborderid int,inownerid int,ingoodnum int,inngnum int,lossnum int) returns void as $BODY$
           DECLARE
             myprodid int ;
             mynowdatetime timestamp ;
             myengorder char ;
             myengseq int ;
             sono int ;
             myprodtmplid int ;
             isoutsourcing Boolean ;
             mynextoutsourcingid int ;
             mynextwkorderid int ;
             myname varchar ;
             mypowkorderid int ;
             myengtype varchar ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select product_no,so_no,eng_order,eng_seq,name into myprodid,sono,myengorder,myengseq,myname from alldo_gh_iot_outsuborder where id = suborderid ;
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
             insert into alldo_gh_iot_outsuborder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_ng_num,in_owner,create_date,loss_num) values 
                 (suborderid,mynowdatetime,myprodid,ingoodnum,inngnum,inownerid,mynowdatetime,lossnum) ;
             update alldo_gh_iot_outsuborder set prod_num=coalesce(prod_num,0)+ingoodnum+inngnum,write_date=mynowdatetime where id=suborderid ;
             if myengorder='1' or myengorder='2' then  /* 委外為首工序 或 中工序 */
                select is_outsourcing into isoutsourcing from alldo_gh_iot_eng_order where prod_id=myprodtmplid and 
                   eng_order=myengseq + 1 ;
                if isoutsourcing = true then  /* 後一工序為委外加工 */
                   select id into mynextoutsourcingid from alldo_gh_iot_outsuborderalldo_gh_iot_outsuborder where so_no=sono and 
                      product_no=myprodid and eng_seq = myengseq + 1 ;
                   insert into alldo_gh_iot_outsuborder_prodout(order_id,prodout_datetime,product_no,out_good_num,out_ng_num,out_loc,out_owner,create_date) values (mynextoutsourcingid,mydatetime,myprodid,ingoodnum,inngnum,myname,inownerid,mynowdatetime) ;   
                else  /* 一般廠內工單 */
                   select id into mynextwkorderid from alldo_gh_iot_workorder where so_no=sono and product_no=myprodid and 
                      eng_seq = myengseq + 1 ;
                   insert into alldo_gh_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_type,in_good_num,in_ng_num,in_loc,in_owner,create_date,loss_num) values (mynextwkorderid,mydatetime,myprodid,'2',ingoodnum,inngnum,myname,inownerid,mynowdatetime,lossnum) ;   
                end if ;   
             end if ;
             select id into mypowkorderid from alldo_gh_iot_po_wkorder where so_no=sono and product_no=myprodid ;
             update alldo_gh_iot_po_suborder_line set complete_num = coalesce(complete_num,0) + ingoodnum,
                ng_num=coalesce(ng_num,0)+inngnum,write_date=mynowdatetime where po_id=mypowkorderid and outsourcing_id = suborderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setpowkordercomplete(powkorderid int) cascade""")
        self.env.cr.execute("""create or replace function setpowkordercomplete(powkorderid int) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             update alldo_gh_iot_po_wkorder set state='3',write_date=mynowdatetime where id = powkorderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists getsonostocknum(sonoid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getsonostocknum(sonoid int,prodid int) returns Float as $BODY$
           DECLARE
             myres Float ;
             isoutsourcing Boolean ;
             myprodtmplid int ;
             maxengseq int ;
             myoutsourcingid int ;
             mywkorderid int ;
           BEGIN
             select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
             select max(eng_order) into maxengseq from alldo_gh_iot_eng_order where prod_id=myprodtmplid ;
             select is_outsourcing into isoutsourcing from alldo_gh_iot_eng_order where prod_id=myprodtmplid and
                 eng_order=maxengseq ; 
             if isoutsourcing = True then   /* 如果為委外加工    */
                select id into myoutsourcingid from alldo_gh_iot_outsuborder where so_no=sonoid and product_no=prodid
                  and eng_seq=maxengseq ;
                select sum(coalesce(in_good_num,0) - coalesce(in_stock_num,0)) into myres from alldo_gh_iot_outsuborder_prodin  
                   where order_id = myoutsourcingid ;
             else                           /* 如果為一般工單    */
                 select id into mywkorderid from alldo_gh_iot_workorder where so_no=sonoid and product_no=prodid
                     and eng_seq=maxengseq ; 
                 select sum(coalesce(out_good_num,0) - coalesce(out_stock_num,0)) into myres from alldo_gh_iot_wkorder_prodout                                where order_id = mywkorderid ;
             end if ;
             if myres is null then
                myres := 0 ;
             end if ;
             return myres ;    
           END;$BODY$
           LANGUAGE plpgsql;
        """)

        self.env.cr.execute("""drop function if exists getsonostockorigin(sonoid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getsonostockorigin(sonoid int,prodid int) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            isoutsourcing Boolean ;
            myprodtmplid int ;
            maxengseq int ;
            myoutsourcingid int ;
            mywkorderid int ;
          BEGIN
            select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
            select max(eng_order) into maxengseq from alldo_gh_iot_eng_order where prod_id=myprodtmplid ;
            select is_outsourcing into isoutsourcing from alldo_gh_iot_eng_order where prod_id=myprodtmplid and
                eng_order=maxengseq ; 
            if isoutsourcing = True then   /* 如果為委外加工    */
               select name into myres from alldo_gh_iot_outsuborder where so_no=sonoid and product_no=prodid
                and eng_seq=maxengseq ; 
            else                           /* 如果為一般工單    */
                select name into myres from alldo_gh_iot_workorder where so_no=sonoid and product_no=prodid
                    and eng_seq=maxengseq ; 
            end if ;
            if myres is null then
               myres := ' ' ;
            end if ;
            return myres ;    
          END;$BODY$
          LANGUAGE plpgsql;
       """)

        self.env.cr.execute("""drop function if exists genblankstockin(sonoid int,prodid int,blanknum float,outowner int) cascade""")
        self.env.cr.execute("""create or replace function genblankstockin(sonoid int,prodid int,blanknum float,outowner int) returns void as $BODY$
           DECLARE
             myprodtmplid int ;
             isoutsourcing Boolean ;
             myoutsourcingid int ;
             mywkorderid int ;
             myname varchar ;
             mynowblanknum float ;
             mynowwkordernum float ;
             mysalenum float ;
             ncount int ;
             mysalelineid int ;
             mypickingid int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select name into myname from sale_order where id = sonoid ;
             select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
             select is_outsourcing into isoutsourcing from alldo_gh_iot_eng_order where prod_id=myprodtmplid and eng_order=1 ;
             if isoutsourcing = True then     /* 第一工序為委外加工單 */
                select id into myoutsourcingid from alldo_gh_iot_outsuborder where so_no=sonoid and eng_seq=1 and
                   product_no=prodid ;
                insert into alldo_gh_iot_outsuborder_prodout(order_id,product_no,out_good_num,out_loc,out_owner,prodout_datetime,create_date) values
                  (myoutsourcingid,prodid,blanknum,myname,outowner,mynowdatetime,mynowdatetime) ;   
                update alldo_gh_iot_outsuborder set blank_num=coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id =myoutsourcingid ;
                select blank_num into mynowblanknum from alldo_gh_iot_outsuborder where id = myoutsourcingid ;
                select id,product_uom_qty into mysalelineid,mysalenum from sale_order_line where order_id=sonoid 
                    and product_id=prodid ;
                if mynowblanknum > mysalenum then
                   update sale_order_line set product_uom_qty=mynowblanknum,write_date=mynowdatetime where id = mysalelineid ;
                   select id into mypickingid from stock_picking where origin=myname ;
                   update stock_move set product_uom_qty=mynowblanknum,write_date=mynowdatetime where picking_id=mypickingid and product_id=prodid ;
                end if ;
             else                             /* 第一工序為一般工單   */
                 select id into mywkorderid from alldo_gh_iot_workorder where so_no=sonoid and eng_seq=1 and
                   product_no=prodid ;    
                 insert into alldo_gh_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_loc,in_owner,in_type,create_date) values
                   (mywkorderid,mynowdatetime,prodid,blanknum,myname,outowner,'1',mynowdatetime) ; 
                 update alldo_gh_iot_workorder set blank_num = coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id = mywkorderid ;
                 select blank_num into mynowblanknum from alldo_gh_iot_workorder where id = mywkorderid ;
                 select id,product_uom_qty into mysalelineid,mysalenum from sale_order_line where order_id=sonoid 
                    and product_id=prodid ;
                 if mynowblanknum > mysalenum then
                   update alldo_gh_iot_workorder set order_num=mynowblanknum,write_date=mynowdatetime where id = mywkorderid ;
                   update sale_order_line set product_uom_qty=mynowblanknum,write_date=mynowdatetime where id = mysalelineid ;
                   select id into mypickingid from stock_picking where origin=myname ;
                   update stock_move set product_uom_qty=mynowblanknum,write_date=mynowdatetime where picking_id=mypickingid and product_id=prodid ;
                 end if ;                     
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists emponduty(empno varchar) cascade""")
        self.env.cr.execute("""create or replace function emponduty(empno varchar) returns varchar as $BODY$
           DECLARE
             myid int ;
             mynowdate DATE;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             ncount int ;
             myname varchar ;
             mydutytime varchar ;
             mydate varchar ;
             mytime varchar ;
             myres varchar ;
           BEGIN
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp  into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select mynowdatetime1::DATE::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno and active=True ;
             if myid is not null then
               insert into alldo_gh_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'1',mynowdatetime) ;
               update hr_employee set duty_type='1',duty_datetime=mynowdatetime,write_date=mynowdatetime where id=myid ;
               myres = concat(myname,'-',mydutytime);
               return myres ;       
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists empoffduty(empno varchar) cascade""")
        self.env.cr.execute("""create or replace function empoffduty(empno varchar) returns varchar as $BODY$
           DECLARE
             myid int ;
             mynowdate DATE;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             ncount int ;
             mydate varchar ;
             mytime varchar ;
             mydutytime varchar ;
             myres varchar ;
             myname varchar ;
           BEGIN
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp  into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select mynowdatetime1::DATE::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno and active=True ;
             if myid is not null then
               insert into alldo_gh_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'2',mynowdatetime) ;
               update hr_employee set duty_type='2',duty_datetime=mynowdatetime,write_date=mynowdatetime where id=myid ;
               myres = concat(myname,'-',mydutytime) ;
               return myres ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genempbarcode(wizid int) cascade""")
        self.env.cr.execute("""create or replace function genempbarcode(wizid int) returns void as $BODY$
           DECLARE
             emp_cur refcursor ;
             emp_rec record ;
             myitem int = 1 ;
             mymaxid int ;
             mymaxid1 int ;
             mynowdate date ;
           BEGIN
             select now()::DATE into mynowdate ;
             delete from alldo_gh_iot_empinfo ;
             insert into alldo_gh_iot_empinfo (empinfo_date) values (mynowdate) ;
             select max(id) into mymaxid1 from alldo_gh_iot_empinfo ;
             open emp_cur for select id,emp_code,name from hr_employee where id in 
               (select emp_id from alldo_gh_iot_empbarcode_rel where wizard_id=wizid)
               and active=true order by emp_code ;
             loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               if myitem = 1 then
                  insert into alldo_gh_iot_empbarcode (barcode_id,emp_code1,emp_name1) values (mymaxid1,emp_rec.emp_code,emp_rec.name) ;
                  select max(id) into mymaxid from alldo_gh_iot_empbarcode ;
               end if ;
               if myitem = 2 then
                  update alldo_gh_iot_empbarcode set emp_code2=emp_rec.emp_code,emp_name2=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 3 then
                  update alldo_gh_iot_empbarcode set emp_code3=emp_rec.emp_code,emp_name3=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 4 then
                  update alldo_gh_iot_empbarcode set emp_code4=emp_rec.emp_code,emp_name4=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 5 then
                  update alldo_gh_iot_empbarcode set emp_code5=emp_rec.emp_code,emp_name5=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 6 then
                  update alldo_gh_iot_empbarcode set emp_code6=emp_rec.emp_code,emp_name6=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 7 then
                  update alldo_gh_iot_empbarcode set emp_code7=emp_rec.emp_code,emp_name7=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 8 then
                  update alldo_gh_iot_empbarcode set emp_code8=emp_rec.emp_code,emp_name8=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 9 then
                  update alldo_gh_iot_empbarcode set emp_code9=emp_rec.emp_code,emp_name9=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 10 then
                  update alldo_gh_iot_empbarcode set emp_code10=emp_rec.emp_code,emp_name10=emp_rec.name where id = mymaxid ;
               end if ;
               myitem = myitem + 1 ;
               if myitem > 10 then
                  myitem = 1 ;
               end if ;
             end loop ;
             close emp_cur ;  
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genequipstatusbarcode(wizid int) cascade""")
        self.env.cr.execute("""create or replace function genequipstatusbarcode(wizid int) returns void as $BODY$
           DECLARE
             equip_cur refcursor ;
             equip_rec record ;
             myprintnum int ;
             myitem int = 1 ;
             mymaxid int ;
             mymaxid1 int ;
             mynowdate date ;
             mynum int = 1 ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select print_num into myprintnum from alldo_gh_iot_equipstatus_barcode_wizard where id = wizid ;
             select now()::DATE into mynowdate ;
             delete from alldo_gh_iot_equipstatusinfo ;
             insert into alldo_gh_iot_equipstatusinfo(print_num,create_date) values (myprintnum,mynowdatetime) ;
             select max(id) into mymaxid1 from alldo_gh_iot_equipstatusinfo ;
             loop
                 exit when mynum > myprintnum ;
                 myitem = 1 ;
                 open equip_cur for select * from maintenance_equipment_status order by sequence,id ;
                 loop
                   fetch equip_cur into equip_rec ;
                   exit when not found ;
                   if myitem = 1 then
                      insert into alldo_gh_iot_equipstatusbarcode(barcode_id,status_code1,status_name1) values (mymaxid1,equip_rec.status_code,equip_rec.status_name) ;
                      select max(id) into mymaxid from alldo_gh_iot_equipstatusbarcode ;
                   end if ;
                   if myitem = 2 then
                      update alldo_gh_iot_equipstatusbarcode set status_code2=equip_rec.status_code,status_name2=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 3 then
                      update alldo_gh_iot_equipstatusbarcode set status_code3=equip_rec.status_code,status_name3=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 4 then
                      update alldo_gh_iot_equipstatusbarcode set status_code4=equip_rec.status_code,status_name4=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 5 then
                      update alldo_gh_iot_equipstatusbarcode set status_code5=equip_rec.status_code,status_name5=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 6 then
                      update alldo_gh_iot_equipstatusbarcode set status_code6=equip_rec.status_code,status_name6=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 7 then
                      update alldo_gh_iot_equipstatusbarcode set status_code7=equip_rec.status_code,status_name7=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 8 then
                      update alldo_gh_iot_equipstatusbarcode set status_code8=equip_rec.status_code,status_name8=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 9 then
                      update alldo_gh_iot_equipstatusbarcode set status_code9=equip_rec.status_code,status_name9=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 10 then
                      update alldo_gh_iot_equipstatusbarcode set status_code10=equip_rec.status_code,status_name10=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   myitem = myitem + 1 ;
                   if myitem > 10 then
                      myitem = 1 ;
                   end if ;
                 end loop ;
                 close equip_cur ;  
                 mynum = mynum + 1 ;
             end loop ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcusprod(cusid int) cascade""")
        self.env.cr.execute("""create or replace function getcusprod(cusid int) returns setof INT as $BODY$
           DECLARE
             prod_cur refcursor ;
             prod_rec record ;
             myprodid int ;
           BEGIN
             open prod_cur for select id,cus_no from product_template where cus_no=cusid ;
             loop
                fetch prod_cur into prod_rec ;
                exit when not found ;
                select id into myprodid from product_product where product_tmpl_id=prod_rec.id ;
                return next myprodid ;
             end loop ;
             close prod_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmomoldcavity(mono varchar) cascade""")
        self.env.cr.execute("""create or replace function getmomoldcavity(mono varchar) returns Integer as $BODY$
           DECLARE
             myprodid int ;
             myprodtmplid int ;
             myengtype varchar ;
             myres integer ;
           BEGIN
             select product_no,eng_type into myprodid,myengtype from alldo_gh_iot_workorder where name = mono ;
             if myprodid is not null and myengtype is not null then
                select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
                select coalesce(mold_cavity,1) into myres from alldo_gh_iot_eng_order where 
                    prod_id=myprodtmplid and eng_type=myengtype ;    
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")



        self.env.cr.execute("""drop function if exists getnodelastmoid(nodename varchar) cascade""")
        self.env.cr.execute("""create or replace function getnodelastmoid(nodename varchar) returns INT as $BODY$
          DECLARE
            myres int ;
            equipid int ;
            wkorderid int ;
            mymaxid int ;
          BEGIN
            select id,mo_no into equipid,myres from maintenance_equipment where equipment_no=nodename ;
            if myres is null then
                select max(id) into mymaxid from alldo_gh_iot_workorder_lastwork where equipment_id = equipid and workorder_id is not null ;
                select workorder_id into myres from alldo_gh_iot_workorder_lastwork where id = mymaxid ;
            end if ;    
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getnodelastmono(nodename varchar) cascade""")
        self.env.cr.execute("""create or replace function getnodelastmono(nodename varchar) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            equipid int ;
            wkorderid int ;
            mymaxid int ;
            mystatus char ;
            outoffid int ;
            outstatusid int ;
            outstatustype char ;
            mylastmoid int ;
          BEGIN
            select id,mo_no into equipid,mylastmoid from maintenance_equipment where equipment_no = nodename ;
            select name into myres from alldo_gh_iot_workorder where id = mylastmoid ;
            if myres is null then
                select max(id) into mymaxid from alldo_gh_iot_workorder_lastwork where equipment_id = equipid and workorder_id is not null ;
                select workorder_id into mylastmoid from alldo_gh_iot_workorder_lastwork where id = mymaxid ;
                select name into myres from alldo_gh_iot_workorder where id = mylastmoid ;
            end if ;  
            if myres is null then
               myres = ' ' ;
            end if ; 
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists runcncreplaceline(nodename varchar,empno varchar,wkorder varchar) cascade""")
        self.env.cr.execute("""create or replace function runcncreplaceline(nodename varchar,empno varchar,wkorder varchar) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
             mynodeid int ;
             myempid int ;
             mywkorderid int ;
             ncount1 int ;
             statusid int ;
           BEGIN
             select max(id) into statusid from maintenance_equipment_status where status_type='2' ;
             select current_timestamp  into mynowdatetime ;
             select id into mynodeid from maintenance_equipment where equipment_no=nodename ;
             select id into myempid from hr_employee where emp_code=empno ;
             select id into mywkorderid from alldo_gh_iot_workorder where name = wkorder ;
             update maintenance_equipment set mo_no=mywkorderid where id = mynodeid ;
             select count(*) into ncount from alldo_gh_iot_wkorder_replaceline where replace_end_datetime is null 
                 and equipment_id=mynodeid ;
             if ncount = 0 and mynodeid is not null and  myempid is not null  and mywkorderid is not null then
                insert into alldo_gh_iot_wkorder_replaceline(order_id,replace_owner,equipment_id,replace_start_datetime,create_date)
                  values (mywkorderid,myempid,mynodeid,mynowdatetime,mynowdatetime) ;
             end if ;
             select count(*) into ncount1 from alldo_gh_iot_equipment_outofforder_status where iot_id=mynodeid and end_datetime is null ;
             if ncount1 = 0 and mynodeid is not null and mywkorderid is not null then
                insert into alldo_gh_iot_equipment_outofforder_status(iot_id,status_id,iot_workorder,start_datetime,create_date,outoff_owner) values 
                  (mynodeid,statusid,mywkorderid,mynowdatetime,mynowdatetime,myempid) ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists runcnccompleteline(nodename varchar) cascade""")
        self.env.cr.execute("""create or replace function runcnccompleteline(nodename varchar) returns void as $BODY$
           DECLARE
             myrepid int ;
             myoutoffid int ; 
             myequipid int ;
             mynowdatetime timestamp ;
             myrepstartdatetime timestamp ;
             repdurmin float ;
             repdurhour float ;
             repdurday float ;
             repdurmin1 float ;
             statusid int ;
             outoffid int ;
             outoffdatetime timestamp ;
             offdurmin float ;
             offdurhour float ;
             offdurday float ;
             offdurmin1 float ;
             mywkorderid int ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select id into myequipid from maintenance_equipment where equipment_no=nodename ;
             select id,replace_start_datetime into myrepid,myrepstartdatetime from alldo_gh_iot_wkorder_replaceline where equipment_id=myequipid 
                 and replace_end_datetime is null;
             if myrepid is not null then
                  select order_id into mywkorderid from alldo_gh_iot_wkorder_replaceline where id = myrepid ;
                  select extract(minute from (select age(mynowdatetime,myrepstartdatetime))) into repdurmin ;
                  select extract(hours from (select age(mynowdatetime,myrepstartdatetime))) into repdurhour ;  
                  select extract(days from (select age(mynowdatetime,myrepstartdatetime))) into repdurday ;
                  repdurmin1 = repdurmin + (repdurhour * 60) + (repdurday * 24 * 60) ;
                  update alldo_gh_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime,write_date=mynowdatetime,replace_duration=coalesce(repdurmin1,0) 
                   where id = myrepid ;
                  insert into alldo_gh_iot_workorder_lastwork(work_datetime,equipment_id,workorder_id) values (mynowdatetime,myequipid,mywkorderid) ; 
             end if ;    
             select id,start_datetime into outoffid,outoffdatetime from alldo_gh_iot_equipment_outofforder_status where iot_id=myequipid 
                 and end_datetime is null;
             if outoffid is not null then
                  select extract(minute from (select age(mynowdatetime,outoffdatetime))) into offdurmin ;
                  select extract(hours from (select age(mynowdatetime,outoffdatetime))) into offdurhour ;  
                  select extract(days from (select age(mynowdatetime,outoffdatetime))) into offdurday ;
                  offdurmin1 = offdurmin + (offdurhour * 60) + (offdurday * 24 * 60) ;
                  update alldo_gh_iot_equipment_outofforder_status set end_datetime=mynowdatetime,write_date=mynowdatetime,outoff_duration=coalesce(offdurmin1,0) 
                   where id = outoffid ;
             end if ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists runcncstopline(cncerrcode varchar,empno varchar,nodename varchar) cascade""")
        self.env.cr.execute("""create or replace function runcncstopline(cncerrcode varchar,empno varchar,nodename varchar) returns void as $BODY$ 
           DECLARE
             statusid int ;
             mynowdatetime timestamp ;
             myequipid int ;
             myempid int ;
             ncount int ;
             mywkorderid int ;
           BEGIN
             select id into statusid from maintenance_equipment_status where status_code = cncerrcode ;
             select id into myempid from hr_employee where emp_code = empno ;
             select current_timestamp  into mynowdatetime ;
             select id into myequipid from maintenance_equipment where equipment_no = nodename ;
             select count(*) into ncount from alldo_gh_iot_equipment_outofforder_status where iot_id=myequipid and
                end_datetime is null ;
             if ncount = 0 and statusid is not null and myequipid is not null and myempid is not null then
                select getnodelastmoid(nodename) into mywkorderid ;
                insert into alldo_gh_iot_equipment_outofforder_status(iot_id,status_id,iot_workorder,start_datetime,outoff_owner,create_date) values
                 (myequipid,statusid,mywkorderid,mynowdatetime,myempid,mynowdatetime) ;
             end if ;   
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists getpartnerprod(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getpartnerprod(partnerid int) returns setof INT as $BODY$
           DECLARE
             myres int ;
             prod_cur refcursor ;
             prod_rec record ;
           BEGIN
             open prod_cur for select id,cus_no,is_blank from product_template where cus_no=partnerid and is_blank != True  ;
             loop
               fetch prod_cur into prod_rec ;
               exit when not found ;
               select id into myres from product_product where product_tmpl_id=prod_rec.id ;
               return next myres ;
             end loop ;
             close prod_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoutpartner(partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,outretdate date,moveid int) cascade""")
        self.env.cr.execute("""drop function if exists genoutpartner(partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,moveid int) cascade""")
        self.env.cr.execute("""create or replace function genoutpartner(partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,moveid int) returns void as $BODY$
           DECLARE
             mynowdatetime timestamp ;
             myretdate date ;
           BEGIN
             select current_timestamp - interval '8 hours' into mynowdatetime ;
             select (current_timestamp - interval '8 hours')::DATE into myretdate ;
             insert into alldo_gh_iot_partner_prodout(partner_id,prodout_datetime,product_no,out_good_num,out_owner,out_loc,out_memo,picking_no,out_return_date) values 
               (partnerid,mynowdatetime,prodid,prodnum,ownerid,coalesce(outdesc,' '),coalesce(outmemo,' '),moveid,myretdate) ;
             execute gennewoutsourcingno(partnerid) ; 
           END;$BODY$
           LANGUAGE plpgsql;""")



        self.env.cr.execute("""drop function if exists geninpartner(partnerid int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar,pickingid int) cascade""")
        self.env.cr.execute("""drop function if exists geninpartner(partnerid int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar,pickingid int,lossnum int) cascade""")
        self.env.cr.execute("""create or replace function geninpartner(partnerid int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar,pickingid int,lossnum int) returns void as $BODY$
           DECLARE
              mynowdatetime timestamp ;
           BEGIN
              select current_timestamp into mynowdatetime ;
              insert into alldo_gh_iot_partner_prodin(partner_id,prodin_datetime,product_no,in_good_num,in_ng_num,in_owner,in_loc,picking_no,loss_num) values 
                (partnerid,mynowdatetime,prodid,prodnum,ngnum,ownerid,coalesce(indesc,' '),pickingid,lossnum) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcusmo(cusid int) cascade""")
        self.env.cr.execute("""drop function if exists getcusmo(cusid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getcusmo(cusid int,prodid int) returns setof INT as $BODY$
           DECLARE
             mo_cur refcursor ;
             mo_rec record ;
             mgpid int ;
             ncount int ;
           BEGIN
             open mo_cur for select id,cus_name,state,eng_order,blank_no from alldo_gh_iot_workorder where cus_name=cusid and 
             (state != '4')  and blank_no=prodid order by id ;
             loop
               fetch mo_cur into mo_rec ;
               exit when not found ;
               select mo_group_id into mgpid from alldo_gh_iot_workorder where id = mo_rec.id ;
               select count(*) into ncount from alldo_gh_iot_workorder where mo_group_id=mgpid ;
               if ncount > 1 then
                  if mo_rec.eng_order='1' then
                     return next mo_rec.id ;
                  end if ;
               else
                  if mo_rec.eng_order='1' or mo_rec.eng_order='3' then
                     return next mo_rec.id ;
                  end if ;
               end if ;
             end loop ;
             close mo_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodmo(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodmo(prodid int) returns setof INT as $BODY$
           DECLARE
             mog_cur refcursor ;
             mog_rec record ; 
             mo_cur refcursor ;
             mo_rec record ;
             maxmoid int ;
           BEGIN
             open mog_cur for select distinct mo_group_id from alldo_gh_iot_workorder where state != '4' and
               product_no=prodid ;
             loop 
                 fetch mog_cur into mog_rec ;
                 exit when not found ;
                 open mo_cur for select id,cus_name,state,eng_order,product_no from alldo_gh_iot_workorder where 
                 id = (select max(id) from alldo_gh_iot_workorder where mo_group_id=mog_rec.mo_group_id and eng_order != '4')  ;
                 loop
                   fetch mo_cur into mo_rec ;
                   exit when not found ;
                   return next mo_rec.id ;
                 end loop ;
                 close mo_cur ;
             end loop ;
             close mog_cur ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getoutsourcingprodmo(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getoutsourcingprodmo(prodid int) returns setof INT as $BODY$
           DECLARE
             mo_cur refcursor ;
             mo_rec record ;
           BEGIN
             open mo_cur for select id,cus_name,state,eng_order,product_no from alldo_gh_iot_workorder where 
             state != '4'  and blank_no=prodid order by id ;
             loop
               fetch mo_cur into mo_rec ;
               exit when not found ;
               return next mo_rec.id ;
             end loop ;
             close mo_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcusmoprod(cusid int) cascade""")
        self.env.cr.execute("""create or replace function getcusmoprod(cusid int) returns setof INT as $BODY$
           DECLARE
             mo_cur refcursor ;
             mo_rec record ;
           BEGIN
             open mo_cur for select id,cus_name,state,eng_order,blank_no from alldo_gh_iot_workorder where cus_name=cusid and 
             (state != '4')  order by id ;
             loop
               fetch mo_cur into mo_rec ;
               exit when not found ;
               return next mo_rec.blank_no ;
             end loop ;
             close mo_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmoprod(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmoprod(moid int) returns int as $BODY$
           DECLARE
             ncount int ;
             myres int ;
           BEGIN
             select count(*) into ncount from alldo_gh_iot_workorder where id=moid ;
             if ncount > 0 then
                select coalesce(blank_no,0) into myres from alldo_gh_iot_workorder where id=moid ;
                if myres = 0 then
                    select coalesce(product_no,0) into myres from alldo_gh_iot_workorder where id=moid ;
                end if ;
             else
                myres = 0 ;   
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists getmoprod1(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmoprod1(moid int) returns int as $BODY$
           DECLARE
             ncount int ;
             myres int ;
           BEGIN
             select count(*) into ncount from alldo_gh_iot_workorder where id=moid ;
             if ncount > 0 then   
                select coalesce(product_no,0) into myres from alldo_gh_iot_workorder where id=moid ;
             else
                myres = 0 ;   
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists genblankstockin1(moid int,blanknum float,inowner int) cascade""")
        self.env.cr.execute("""create or replace function genblankstockin1(moid int,blanknum float,inowner int) returns void as $BODY$
           DECLARE
             myprodtmplid int ;
             isoutsourcing Boolean ;
             myoutsourcingid int ;
             mywkorderid int ;
             myname varchar ;
             mynowblanknum float ;
             mynowwkordernum float ;
             mysalenum float ;
             ncount int ;
             mysalelineid int ;
             mypickingid int ;
             mynowdatetime timestamp ;
             prodid int ;
             mycusid int ;
             mogrpid int ;
             powkid int ;
           BEGIN
             select product_no,cus_name,mo_group_id,po_no1 into prodid,mycusid,mogrpid,powkid from alldo_gh_iot_workorder where id = moid ;
             select name into myname from res_partner where id = mycusid ;
             select current_timestamp into mynowdatetime ;  
             insert into alldo_gh_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_loc,in_owner,in_type,create_date) values
               (moid,mynowdatetime,prodid,blanknum,myname,inowner,'1',mynowdatetime) ; 
             update alldo_gh_iot_workorder set write_date = mynowdatetime where  id = moid ;  
             if mycusid=35 then
                update alldo_gh_iot_workorder set blank_num = coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id = moid ; 
             else
                update alldo_gh_iot_workorder set blank_num = coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where mo_group_id = mogrpid ; 
             end if ;    
             if powkid is not null then
                update alldo_gh_iot_po_wkorder set blank_num = coalesce(blank_num,0) + blanknum where id = powkid ;
             end if ; 
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setallmoclose(moid int) cascade""")
        self.env.cr.execute("""create or replace function setallmoclose(moid int) returns void as $BODY$
           DECLARE
             mogroupid int ;
             mo_cur refcursor ;
             mo_rec record ;
             ncount int ;
             poid int ;
           BEGIN
             select count(*) into ncount from alldo_gh_iot_po_wkorder_line where wkorder_id= moid ;
             if ncount > 0 then
                select max(po_id) into poid from alldo_gh_iot_po_wkorder_line where wkorder_id= moid ;
                update alldo_gh_iot_po_wkorder set state='3' where id = poid ;
                update alldo_gh_iot_po_wkorder set state='3' where id in (select po_id from powkorder_iotwkorder_rel where wk_id=moid) ; 
             end if ;
             select mo_group_id into mogroupid from alldo_gh_iot_workorder where id = moid ;
             update alldo_gh_iot_workorder set state='4' where mo_group_id=mogroupid and (not_close is null or not_close=False) ;
             open mo_cur for select id,mo_group_id from alldo_gh_iot_workorder where mo_group_id=mogroupid order by id ;
             loop
               fetch mo_cur into mo_rec ;
               exit when not found ;
               execute genmoperformance(mo_rec.id) ;
             end loop ;
             close mo_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists runmoadd(moid int,prodnum numeric) cascade""")
        self.env.cr.execute("""create or replace function runmoadd(moid int,prodnum numeric) returns void as $BODY$
          DECLARE
            mygroupid int ;
            mypickid int ;
            myprodid int ;
          BEGIN
            select mo_group_id,product_no,prodout_picking into mygroupid,myprodid,mypickid  from alldo_gh_iot_workorder where id = moid ;
            if mygroupid is not null then
              /* update alldo_gh_iot_workorder set order_num=coalesce(order_num,0) + prodnum where mo_group_id=mygroupid ;*/
              /* select id into mypickid from stock_picking where mo_group_id = mygroupid and picking_type_id=2  ; */
               if mypickid is not null then
                  update stock_move set product_qty=coalesce(product_qty,0)+prodnum,product_uom_qty=coalesce(product_uom_qty,0)+prodnum 
                         where picking_id=mypickid and product_id=myprodid ;  
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmooriginnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmooriginnum(moid int) returns float as $BODY$
          DECLARE
            myres float ;
          BEGIN
            select order_num into myres from alldo_gh_iot_workorder where id = moid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists candelwkorder(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function candelwkorder(wkorderid int) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
            ncount1 int ;
            mygroupid int;
            myprodid int ;
            moproductnum float ;
          BEGIN
            select mo_group_id,product_no into mygroupid,myprodid from alldo_gh_iot_workorder where id = wkorderid ;
            select count(*) into ncount1 from alldo_gh_iot_workorder where mo_group_id = mygroupid and mo_production_num > 0 ;
            if ncount1 > 0 then
               myres = 0 ;
            else
                select count(*) into ncount from alldo_gh_iot_workorder where mo_group_id = mygroupid and (state='3' or state='4') ;
                if ncount = 0 then
                   myres = mygroupid ;
                else
                   myres = 0 ;
                end if ;
            end if ;    
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckshipping(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function ckshipping(partnerid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from stock_picking where picking_type_id=2 and (report_no is null or report_no='') and state= 'done' 
                and partner_id=partnerid  ;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewshipping(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gennewshipping(partnerid int) returns void as $BODY$
          DECLARE
            pick_cur refcursor ;
            pick_rec record ;
            ml_cur refcursor ;
            ml_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            currentdate date ;
            myreplineid int ;
            repmemo varchar ;
            reportdate date ;
            jhreportno varchar ;
            mylinememo varchar ;
            mynowdate date ;
            myid int ;
            numbernext int ;
            numbernext1 varchar ;
            acmereportno varchar ;
            myyear varchar;
            mymonth varchar;
            myday varchar;
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
             /*     */
            select current_timestamp::DATE into mynowdate ;
            select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
            select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
            select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
            select id,number_next into myid,numbernext from ir_sequence where code='alldo_gh_iot.shipping' ;
            numbernext1 = numbernext::TEXT ;
            jhreportno = concat('S',myyear,mymonth,myday,lpad(numbernext1,3,'0')) ;
            update ir_sequence set number_next=number_next+1 where id = myid ;
            /*     */
            select max(id) into myreportid from alldo_gh_iot_stockpicking_report where partner_id=partnerid ;
            update alldo_gh_iot_stockpicking_report set name=jhreportno where id = myreportid ;
            select coalesce(report_date,currentdate) into reportdate from alldo_gh_iot_stockpicking_report where id = myreportid ;
            nitem = 1 ;
            open pick_cur for select * from stock_picking where picking_type_id=2 and partner_id=partnerid and report_no is null  ;
            loop
               fetch pick_cur into pick_rec ;
               exit when not found ;
               repmemo = concat(coalesce(repmemo,''),'/',pick_rec.report_memo) ;
               open ml_cur for select * from stock_move_line where picking_id = pick_rec.id ;
               loop
                  fetch ml_cur into ml_rec ;
                  exit when not found ;
                  select description_picking into mylinememo from stock_move where id = ml_rec.move_id ;
                  if ml_rec.qty_done > 0 then
                      if nitem = 1 then
                         insert into alldo_gh_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,line_memo) values 
                          (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',0,mylinememo) ;
                         select max(id) into myreplineid from alldo_gh_iot_stockpicking_report_line where rep_id=myreportid ; 
                      elsif nitem = 2 then
                         update alldo_gh_iot_stockpicking_report_line set item1=nitem,prod_no1=ml_rec.product_id,prod_num1=ml_rec.qty_done,prod_uom1='PCS',
                            prod_price1=0,line_memo1=mylinememo where id = myreplineid ;
                      elsif nitem = 3 then
                         update alldo_gh_iot_stockpicking_report_line set item2=nitem,prod_no2=ml_rec.product_id,prod_num2=ml_rec.qty_done,prod_uom2='PCS',
                            prod_price2=0,line_memo2=mylinememo where id = myreplineid ;
                      elsif nitem= 4 then
                         update alldo_gh_iot_stockpicking_report_line set item3=nitem,prod_no3=ml_rec.product_id,prod_num3=ml_rec.qty_done,prod_uom3='PCS',
                            prod_price3=0,line_memo3=mylinememo where id = myreplineid ;
                      elsif nitem = 5 then
                         update alldo_gh_iot_stockpicking_report_line set item4=nitem,prod_no4=ml_rec.product_id,prod_num4=ml_rec.qty_done,prod_uom4='PCS',
                            prod_price4=0,line_memo4=mylinememo where id = myreplineid ;
                         nitem = 0 ;
                      end if ;
                      nitem = nitem + 1 ;
                  end if ;    
               end loop ;
               close ml_cur ;
               update stock_picking set date_done=reportdate,report_no=jhreportno where id = pick_rec.id ;
            end loop ;
            close pick_cur ;
            update alldo_gh_iot_stockpicking_report set report_memo=repmemo,report_date=currentdate where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldshipping(reportno varchar) cascade""")
        self.env.cr.execute("""create or replace function genoldshipping(reportno varchar) returns void as $BODY$
          DECLARE
            pick_cur refcursor ;
            pick_rec record ;
            ml_cur refcursor ;
            ml_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            reportdate date ;
            myreplineid int ;
            repmemo varchar ;
            mypartnerid int ;
            mylinememo varchar ;
          BEGIN
            select max(date_done) into reportdate from stock_picking where report_no=reportno ; 
            select max(partner_id) into mypartnerid from stock_picking where report_no=reportno ; 
            insert into alldo_gh_iot_stockpicking_report(name,report_date) values (reportno,reportdate) ;
            select max(id) into myreportid from alldo_gh_iot_stockpicking_report where name=reportno ;
            nitem = 1 ;
            open pick_cur for select * from stock_picking where report_no = reportno and picking_type_id = 2 ;
            loop
               fetch pick_cur into pick_rec ;
               exit when not found ;
               if pick_rec.report_memo is not null then
                  if repmemo is null then
                     repmemo = pick_rec.report_memo ;
                  else
                     repmemo = concat(coalesce(repmemo,''),'/',pick_rec.report_memo) ;
                  end if ;   
               end if ;   
               open ml_cur for select * from stock_move_line where picking_id = pick_rec.id and state='done' ; 
               loop
                  fetch ml_cur into ml_rec ;
                  exit when not found ;
                  select description_picking into mylinememo from stock_move where id = ml_rec.move_id ;
                if nitem = 1 then 
                     insert into alldo_gh_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,line_memo) values 
                      (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',0,mylinememo) ;
                     select max(id) into myreplineid from alldo_gh_iot_stockpicking_report_line where rep_id=myreportid ; 
                elsif nitem = 2 then
                     update alldo_gh_iot_stockpicking_report_line set item1=nitem,prod_no1=ml_rec.product_id,prod_num1=ml_rec.qty_done,prod_uom1='PCS',
                        prod_price1=0,line_memo1=mylinememo where id = myreplineid ;
                  elsif nitem = 3 then
                     update alldo_gh_iot_stockpicking_report_line set item2=nitem,prod_no2=ml_rec.product_id,prod_num2=ml_rec.qty_done,prod_uom2='PCS',
                        prod_price2=0,line_memo2=mylinememo where id = myreplineid ;
                  elsif nitem= 4 then
                     update alldo_gh_iot_stockpicking_report_line set item3=nitem,prod_no3=ml_rec.product_id,prod_num3=ml_rec.qty_done,prod_uom3='PCS',
                        prod_price3=0,line_memo3=mylinememo where id = myreplineid ;
                  elsif nitem = 5 then
                     update alldo_gh_iot_stockpicking_report_line set item4=nitem,prod_no4=ml_rec.product_id,prod_num4=ml_rec.qty_done,prod_uom4='PCS',
                        prod_price4=0,line_memo4=mylinememo where id = myreplineid ;
                     nitem = 0 ;
                  end if ; 
                  nitem = nitem + 1 ;
               end loop ;
               close ml_cur ;
            end loop ;
            close pick_cur ;
            update alldo_gh_iot_stockpicking_report set report_memo=repmemo,report_date=reportdate,partner_id=mypartnerid where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckngreturn(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function ckngreturn(partnerid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_gh_iot_workorder where id in 
              (select order_id from alldo_gh_iot_workorder_qc where (report_no is null or report_no='') 
                 and (material_ng_num > 0 or processing_ng_num > 0 or loss_num > 0))
              and cus_name = partnerid ;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;  
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewngreturn(reportno varchar) cascade""")
        self.env.cr.execute("""drop function if exists gennewngreturn() cascade""")
        self.env.cr.execute("""create or replace function gennewngreturn(reportno varchar) returns void as $BODY$
          DECLARE
            ng_cur refcursor ;
            ng_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            currentdate date ;
            reportdate date ;
            jhngreturnno varchar ;
            mylinememo varchar ;
            mymngnum float ; 
            mypngnum float ;
            myreplineid int ;
            ncount1 int ;
            ncount2 int ;
            ncount3 int ;
            ncount4 int ;
            ncount5 int ;
            myid int ;
            myselectid int ;
            partnerid int ;
            myreportno varchar ;
          BEGIN
            select max(id),max(partner_id) into myselectid,partnerid from alldo_gh_iot_ngreturn_select ;
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into myreportid from alldo_gh_iot_ngreturn_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhngreturnno from alldo_gh_iot_ngreturn_report where id = myreportid ;
            nitem = 1 ; 
            open ng_cur for select * from alldo_gh_iot_ngreturn_selectitem where select_id=myselectid and selectyn=True;    
            loop
               fetch ng_cur into ng_rec ;
               exit when not found ;
               /*if ng_rec.report_no is not null then
                  update alldo_gh_iot_ngreturn_report set name=ng_rec.report_no where id = myreportid ;
               end if ;*/
               update alldo_gh_iot_ngreturn_selectitem set report_no=jhngreturnno where id = ng_rec.id ;
               select count(*) into ncount1 from alldo_gh_iot_ngreturn_report_line where prod_no=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount2 from alldo_gh_iot_ngreturn_report_line where prod_no1=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount3 from alldo_gh_iot_ngreturn_report_line where prod_no2=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount4 from alldo_gh_iot_ngreturn_report_line where prod_no3=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount5 from alldo_gh_iot_ngreturn_report_line where prod_no4=ng_rec.product_no and rep_id=myreportid ;
               if ncount1 > 0 or ncount2 >0 or ncount3 > 0 or ncount4 > 0 or ncount5 > 0 then 
                  if ncount1 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num = coalesce(m_ng_num,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num = coalesce(p_ng_num,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num = coalesce(m_loss_num,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount2 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no1 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num1 = coalesce(m_ng_num1,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num1 = coalesce(p_ng_num1,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num1 = coalesce(m_loss_num1,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount3 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no2 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num2 = coalesce(m_ng_num2,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num2 = coalesce(p_ng_num2,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num2 = coalesce(m_loss_num2,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount4 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no3 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num3 = coalesce(m_ng_num3,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num3 = coalesce(p_ng_num3,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num3 = coalesce(m_loss_num3,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount5 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no4 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num4 = coalesce(m_ng_num4,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num4 = coalesce(p_ng_num4,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num4 = coalesce(m_loss_num4,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  end if ;           
               else
                   if nitem = 1 then
                      insert into alldo_gh_iot_ngreturn_report_line(rep_id,item,prod_no,m_ng_num,p_ng_num,prod_uom,line_memo,m_loss_num) values 
                      (myreportid,nitem,ng_rec.product_no,coalesce(ng_rec.material_ng_num,0),coalesce(ng_rec.processing_ng_num,0),'PCS',ng_rec.line_memo,coalesce(ng_rec.loss_num,0)) ;
                     select max(id) into myreplineid from alldo_gh_iot_ngreturn_report_line where rep_id=myreportid ; 
                   elsif nitem = 2 then
                      update alldo_gh_iot_ngreturn_report_line set item1=nitem,prod_no1=ng_rec.product_no,m_ng_num1=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num1=coalesce(ng_rec.processing_ng_num,0),prod_uom1='PCS',line_memo1=ng_rec.line_memo,m_loss_num1=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem = 3 then
                      update alldo_gh_iot_ngreturn_report_line set item2=nitem,prod_no2=ng_rec.product_no,m_ng_num2=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num2=coalesce(ng_rec.processing_ng_num,0),prod_uom2='PCS',line_memo2=ng_rec.line_memo,m_loss_num2=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem= 4 then
                      update alldo_gh_iot_ngreturn_report_line set item3=nitem,prod_no3=ng_rec.product_no,m_ng_num3=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num3=coalesce(ng_rec.processing_ng_num,0),prod_uom3='PCS',line_memo3=ng_rec.line_memo,m_loss_num3=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem = 5 then
                      update alldo_gh_iot_ngreturn_report_line set item4=nitem,prod_no4=ng_rec.product_no,m_ng_num4=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num4=coalesce(ng_rec.processing_ng_num,0),prod_uom4='PCS',line_memo4=ng_rec.line_memo,m_loss_num4=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                      nitem = 0 ;
                   end if ;
                   nitem = nitem + 1 ;
               end if ;    
               update alldo_gh_iot_workorder_qc set report_date=reportdate,report_no=reportno where id = ng_rec.qcid ;   
            end loop ;
            close ng_cur ;
            update alldo_gh_iot_ngreturn_report set report_date=currentdate where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldngreturn(ngreturnno varchar) cascade""")
        self.env.cr.execute("""create or replace function genoldngreturn(ngreturnno varchar) returns void as $BODY$
          DECLARE
            ng_cur refcursor ;
            ng_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            currentdate date ;
            reportdate date ;
            jhngreturnno varchar ;
            partnerid int ;
            myreplineid int ;
            mymaxid int ;
            ncount1 int ;
            ncount2 int ;
            ncount3 int ;
            ncount4 int ;
            ncount5 int ;
            myid int ;
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into mymaxid from alldo_gh_iot_workorder_qc where report_no = ngreturnno ; 
            select cus_name,report_no,report_date into partnerid,jhngreturnno,reportdate from alldo_gh_iot_workorder_qc 
               where id = mymaxid ;
            insert into alldo_gh_iot_ngreturn_report(partner_id,name,report_date) values (partnerid,jhngreturnno,reportdate) ;
            select max(id) into myreportid from alldo_gh_iot_ngreturn_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhngreturnno from alldo_gh_iot_ngreturn_report where id = myreportid ;
            nitem = 1 ; 
            open ng_cur for select * from alldo_gh_iot_workorder_qc where report_no=ngreturnno ;
            loop
               fetch ng_cur into ng_rec ;
               exit when not found ;
               /*            */
               select count(*) into ncount1 from alldo_gh_iot_ngreturn_report_line where prod_no=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount2 from alldo_gh_iot_ngreturn_report_line where prod_no1=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount3 from alldo_gh_iot_ngreturn_report_line where prod_no2=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount4 from alldo_gh_iot_ngreturn_report_line where prod_no3=ng_rec.product_no and rep_id=myreportid ;
               select count(*) into ncount5 from alldo_gh_iot_ngreturn_report_line where prod_no4=ng_rec.product_no and rep_id=myreportid ;
               if ncount1 > 0 or ncount2 >0 or ncount3 > 0 or ncount4 > 0 or ncount5 > 0 then 
                  if ncount1 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num = coalesce(m_ng_num,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num = coalesce(p_ng_num,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num = coalesce(m_loss_num,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount2 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no1 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num1 = coalesce(m_ng_num1,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num1 = coalesce(p_ng_num1,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num1 = coalesce(m_loss_num1,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount3 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no2 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num2 = coalesce(m_ng_num2,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num2 = coalesce(p_ng_num2,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num2 = coalesce(m_loss_num2,0) + ng_rec.loss_num where id = myid ;
                  elsif ncount4 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no3 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num3 = coalesce(m_ng_num3,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num3 = coalesce(p_ng_num3,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num3 = coalesce(m_loss_num3,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  elsif ncount5 > 0 then
                      select id into myid from alldo_gh_iot_ngreturn_report_line where prod_no4 = ng_rec.product_no and rep_id = myreportid ;
                      update alldo_gh_iot_ngreturn_report_line set m_ng_num4 = coalesce(m_ng_num4,0) + coalesce(ng_rec.material_ng_num,0),p_ng_num4 = coalesce(p_ng_num4,0) + coalesce(ng_rec.processing_ng_num,0),
                             m_loss_num4 = coalesce(m_loss_num4,0) + coalesce(ng_rec.loss_num,0) where id = myid ;
                  end if ;           
               else
               /*            */
                   if nitem = 1 then
                      insert into alldo_gh_iot_ngreturn_report_line(rep_id,item,prod_no,m_ng_num,p_ng_num,prod_uom,line_memo,m_loss_num) values 
                      (myreportid,nitem,ng_rec.product_no,coalesce(ng_rec.material_ng_num,0),coalesce(ng_rec.processing_ng_num,0),'PCS',coalesce(ng_rec.line_memo,' '),coalesce(ng_rec.loss_num,0)) ;
                     select max(id) into myreplineid from alldo_gh_iot_ngreturn_report_line where rep_id=myreportid ; 
                   elsif nitem = 2 then
                      update alldo_gh_iot_ngreturn_report_line set item1=nitem,prod_no1=ng_rec.product_no,m_ng_num1=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num1=coalesce(ng_rec.processing_ng_num,0),prod_uom1='PCS',line_memo1=coalesce(ng_rec.line_memo,' '),m_loss_num1=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem = 3 then
                      update alldo_gh_iot_ngreturn_report_line set item2=nitem,prod_no2=ng_rec.product_no,m_ng_num2=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num2=coalesce(ng_rec.processing_ng_num,0),prod_uom2='PCS',line_memo2=coalesce(ng_rec.line_memo,' '),m_loss_num2=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem= 4 then
                      update alldo_gh_iot_ngreturn_report_line set item3=nitem,prod_no3=ng_rec.product_no,m_ng_num3=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num3=coalesce(ng_rec.processing_ng_num,0),prod_uom3='PCS',line_memo3=coalesce(ng_rec.line_memo,' '),m_loss_num3=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                   elsif nitem = 5 then
                      update alldo_gh_iot_ngreturn_report_line set item4=nitem,prod_no4=ng_rec.product_no,m_ng_num4=coalesce(ng_rec.material_ng_num,0),
                        p_ng_num4=coalesce(ng_rec.processing_ng_num,0),prod_uom4='PCS',line_memo4=coalesce(ng_rec.line_memo,' '),m_loss_num4=coalesce(ng_rec.loss_num,0) where id = myreplineid ;
                      nitem = 0 ;
                   end if ;
                   nitem = nitem + 1 ;
               end if ;    
               update alldo_gh_iot_workorder_qc set report_date=reportdate,report_no=jhngreturnno where id = ng_rec.id ;   
            end loop ;
            close ng_cur ;
            update alldo_gh_iot_ngreturn_report set report_date=currentdate where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckoutsourcing(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function ckoutsourcing(partnerid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_gh_iot_partner_prodout where partner_id = partnerid
               and (report_no is null or report_no='') and out_good_num > 0 ;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;  
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewoutsourcing(partnerid int) cascade""")
        self.env.cr.execute("""drop function if exists gennewoutsourcing(partnerid int,reportid int) cascade""")
        self.env.cr.execute("""create or replace function gennewoutsourcing(partnerid int,reportid int) returns void as $BODY$
          DECLARE
            os_cur refcursor ;
            os_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            currentdate date ;
            reportdate date ;
            jhoutsourcingno varchar ;
            mylinememo varchar ;
            mymngnum float ; 
            mypngnum float ;
            myreplineid int ;
            par_cur refcursor ;
            par_rec record ;
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into myreportid from alldo_gh_iot_outsourcing_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_gh_iot_outsourcing_report where id = myreportid ;
            nitem = 1 ; 
            open os_cur for select * from alldo_gh_iot_partner_prodout where out_good_num > 0  
                and partner_id=partnerid and (report_no is null or report_no='') ;
            loop
               fetch os_cur into os_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_gh_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                  (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                  select max(id) into myreplineid from alldo_gh_iot_outsourcing_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_gh_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                    prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_gh_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                    prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_gh_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                    prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_gh_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                    prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_gh_iot_partner_prodout set report_date=reportdate,report_no=jhoutsourcingno where id = os_rec.id ;   
            end loop ;
            close os_cur ;
            open par_cur for select * from alldo_gh_iot_outsourcing_report_wizard_res_partner_rel where 
                alldo_gh_iot_outsourcing_report_wizard_id=reportid ;
            loop
                fetch par_cur into par_rec;
                exit when not found ;
                insert into alldo_gh_iot_outsourcing_report(partner_id,name,report_date) values (par_rec.res_partner_id,jhoutsourcingno,reportdate) ;
                select max(id) into myreportid from alldo_gh_iot_outsourcing_report where partner_id=par_rec.res_partner_id ;
                select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_gh_iot_outsourcing_report where id = myreportid ;
                nitem = 1 ; 
                open os_cur for select * from alldo_gh_iot_partner_prodout where out_good_num > 0  
                    and report_no = jhoutsourcingno ;
                loop
                   fetch os_cur into os_rec ;
                   exit when not found ;
                   if nitem = 1 then
                      insert into alldo_gh_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                      (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                      select max(id) into myreplineid from alldo_gh_iot_outsourcing_report_line where rep_id=myreportid ; 
                   elsif nitem = 2 then
                      update alldo_gh_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                        prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem = 3 then
                      update alldo_gh_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                        prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem= 4 then
                      update alldo_gh_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                        prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem = 5 then
                      update alldo_gh_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                        prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                      nitem = 0 ;
                   end if ;
                   nitem = nitem + 1 ; 
                end loop ;
                close os_cur ;
            end loop ;
            close par_cur ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldoutsourcing(outsourcingno varchar) cascade""")
        self.env.cr.execute("""drop function if exists genoldoutsourcing(outsourcingno varchar,reportid int) cascade""")
        self.env.cr.execute("""create or replace function genoldoutsourcing(outsourcingno varchar,reportid int) returns void as $BODY$
          DECLARE
            os_cur refcursor ;
            os_rec record ;
            nitem int ;
            myreportid int ;
            currentdatetime timestamp ;
            currentdate date ;
            reportdate date ;
            jhoutsourcingno varchar ;
            mylinememo varchar ;
            mymngnum float ; 
            mypngnum float ;
            myreplineid int ;
            mymaxid int ;
            partnerid int ;
            par_cur refcursor ;
            par_rec record ;
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into mymaxid from alldo_gh_iot_partner_prodout where report_no = outsourcingno ; 
            select partner_id,report_no,report_date into partnerid,jhoutsourcingno,reportdate from alldo_gh_iot_partner_prodout 
               where id = mymaxid ;
            insert into alldo_gh_iot_outsourcing_report(partner_id,name,report_date) values (partnerid,jhoutsourcingno,reportdate) ;
            select max(id) into myreportid from alldo_gh_iot_outsourcing_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_gh_iot_outsourcing_report where id = myreportid ;
            nitem = 1 ; 
            open os_cur for select * from alldo_gh_iot_partner_prodout where out_good_num > 0  
                and report_no = outsourcingno ;
            loop
               fetch os_cur into os_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_gh_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                  (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                  select max(id) into myreplineid from alldo_gh_iot_outsourcing_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_gh_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                    prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_gh_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                    prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_gh_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                    prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_gh_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                    prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_gh_iot_partner_prodout set report_date=reportdate,report_no=jhoutsourcingno where id = os_rec.id ;   
            end loop ;
            close os_cur ;
            open par_cur for select * from alldo_gh_iot_outsourcing_report_wizard_res_partner_rel where 
                alldo_gh_iot_outsourcing_report_wizard_id=reportid ;
            loop
                fetch par_cur into par_rec;
                exit when not found ;
                insert into alldo_gh_iot_outsourcing_report(partner_id,name,report_date) values (par_rec.res_partner_id,jhoutsourcingno,reportdate) ;
                select max(id) into myreportid from alldo_gh_iot_outsourcing_report where partner_id=par_rec.res_partner_id ;
                select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_gh_iot_outsourcing_report where id = myreportid ;
                nitem = 1 ; 
                open os_cur for select * from alldo_gh_iot_partner_prodout where out_good_num > 0  
                    and report_no = outsourcingno ;
                loop
                   fetch os_cur into os_rec ;
                   exit when not found ;
                   if nitem = 1 then
                      insert into alldo_gh_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                      (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                      select max(id) into myreplineid from alldo_gh_iot_outsourcing_report_line where rep_id=myreportid ; 
                   elsif nitem = 2 then
                      update alldo_gh_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                        prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem = 3 then
                      update alldo_gh_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                        prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem= 4 then
                      update alldo_gh_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                        prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
                   elsif nitem = 5 then
                      update alldo_gh_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                        prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                      nitem = 0 ;
                   end if ;
                   nitem = nitem + 1 ; 
                end loop ;
                close os_cur ;
            end loop ;
            close par_cur ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        # self.env.cr.execute("""drop function if exists getwkiotnode(wkorderid int) cascade""")
        # self.env.cr.execute("""create or replace function getwkiotnode(wkorderid int) returns setof INT as $BODY$
        #    DECLARE
        #      node_cur refcursor ;
        #      node_rec record ;
        #    BEGIN
        #      open node_cur for select distinct iot_node from alldo_gh_iot_workorder_iot_data where order_id = wkorderid ;
        #      loop
        #        fetch node_cur into node_rec ;
        #        exit when not found ;
        #        return next node_rec.iot_node ;
        #      end loop ;
        #      close node_cur ;
        #    END;$BODY$
        #    LANGUAGE plpgsql;""")
        #
        # self.env.cr.execute("""drop function if exists getwkiotowner(wkorderid int) cascade""")
        # self.env.cr.execute("""create or replace function getwkiotowner(wkorderid int) returns setof INT as $BODY$
        #    DECLARE
        #      owner_cur refcursor ;
        #      owner_rec record ;
        #    BEGIN
        #      open owner_cur for select distinct iot_node from alldo_gh_iot_workorder_iot_data where order_id = wkorderid ;
        #      loop
        #        fetch owner_cur into owner_rec ;
        #        exit when not found ;
        #        return next node_rec.iot_owner ;
        #      end loop ;
        #      close owner_cur ;
        #    END;$BODY$
        #    LANGUAGE plpgsql;""")
        #
        self.env.cr.execute("""drop function if exists getwkiotnum(wkid int,nodeid int,ownerid int) cascade""")
        self.env.cr.execute("""create or replace function getwkiotnum(wkid int,nodeid int,ownerid int) returns INT as $BODY$
           DECLARE
             myres int ;
           BEGIN
             select sum(iot_num) into myres from alldo_gh_iot_workorder_iot_data where order_id=wkid and iot_node=nodeid and iot_owner=ownerid ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwkiotduration(wkid int,nodeid int,ownerid int) cascade""")
        self.env.cr.execute("""create or replace function getwkiotduration(wkid int,nodeid int,ownerid int) returns INT as $BODY$
           DECLARE
             myres int ;
           BEGIN
             select sum(iot_duration) into myres from alldo_gh_iot_workorder_iot_data where order_id=wkid and iot_node=nodeid and iot_owner=ownerid ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwkstdduration(wkid int,nodeid int,ownerid int) cascade""")
        self.env.cr.execute("""create or replace function getwkstdduration(wkid int,nodeid int,ownerid int) returns INT as $BODY$
           DECLARE
             myres int ;
           BEGIN
             select sum(std_duration) into myres from alldo_gh_iot_workorder_iot_data where order_id=wkid and iot_node=nodeid and iot_owner=ownerid ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")



        self.env.cr.execute("""drop function if exists genmoperformance(woid int) cascade""")
        self.env.cr.execute("""create or replace function genmoperformance(woid int) returns void as $BODY$
          DECLARE
              mo_cur refcursor ;
              mo_rec record ;
              nsumtottime float ;
              nsumnum float ;
              ncount int ;
              proddate date ;
              prodid int ;
              prodtmplid int ;
              engtype varchar ;
              stdnum int ;
              realstdnum int ;
              perf Float ;
              mynowdate date ;
          BEGIN
              select current_timestamp::DATE into mynowdate ;
              open mo_cur for select distinct iot_owner from alldo_gh_iot_workorder_iot_data where order_id = woid ;
              loop
                 fetch mo_cur into mo_rec ;
                 exit when not found ;
                 select sum(coalesce(iot_duration,0)),sum(coalesce(iot_num,0)) into nsumtottime,nsumnum from alldo_gh_iot_workorder_iot_data
                   where order_id = woid and iot_owner=mo_rec.iot_owner ;
                 select coalesce(max(iot_date::DATE),mynowdate) into proddate from alldo_gh_iot_workorder_iot_data where order_id = woid and iot_owner=mo_rec.iot_owner ; 
                 select product_no,eng_type into prodid,engtype from alldo_gh_iot_workorder where id = woid ;
                 select product_tmpl_id into prodtmplid from product_product where id = prodid ;
                 select coalesce(standard_num,0) into stdnum from alldo_gh_iot_eng_order where prod_id = prodtmplid and eng_type=engtype ;
                 if stdnum is null or nsumtottime is null then
                    realstdnum = 0 ;
                 else   
                    realstdnum = round(stdnum * (nsumtottime::numeric/60),0) ;
                 end if ;   
                 if realstdnum=0 then
                    perf = 0 ;
                 else
                    perf = round((nsumnum::numeric/realstdnum::numeric),2) ;
                 end if ;
                 select count(*) into ncount from alldo_gh_iot_man_performance where order_id = woid and prod_owner=mo_rec.iot_owner ;
                 if ncount = 0 then
                    insert into alldo_gh_iot_man_performance(order_id,prod_date,prod_duration,std_duration,prod_performance,prod_owner,prod_num) values
                     (woid,proddate,nsumtottime,realstdnum,perf,mo_rec.iot_owner,nsumnum) ;
                 else    
                    update alldo_gh_iot_man_performance set prod_date=proddate,prod_duration=nsumtottime,std_durtion=realstdnum,prod_performance=perf,
                       prod_num=nsumnum where prod_owner=mo_rec.iot_owner and order_id=woid ;
                 end if ;
              end loop ;
              close mo_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genattendance1(attstart DATE,attend DATE) cascade""")
        self.env.cr.execute("""create or replace function genattendance1(attstart DATE,attend DATE) returns void as $BODY$
          DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            att_cur refcursor ;
            att_rec record ;
            ncount int ;
            chour varchar ;
            cmin varchar ;
            csecond varchar ;
            mytime varchar ;
            mydate date ;
            mydate1 varchar ;
            ondutydatetime timestamp ;
            offdutydatetime timestamp ;
            list_cur refcursor ;
            list_rec record ;
            listmin float ;
            listhour float ;
            listmin1 float ;
            listhour1 float ;
            listmin2 float ;
            listhour2 float ;
            listmin3 float ;
            listhour3 float ;
            listtot float ;
            listtot1 float ;
            listtot2 float ;
            listtot3 float ;
            mytime1 timestamp ;
            mytime2 timestamp ;
            mynowdate varchar ;
            mydate2 date ;
            ncount1 int ;
            otattstime1 timestamp ;
            otattstime2 timestamp ;
            otattstimes timestamp ;
            ot_release float ;
          BEGIN
            delete from alldo_gh_iot_emp_attendance_list ;
            open emp_cur for select * from hr_employee where active=True order by emp_code ;
            loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               mydate2 = attstart::DATE ;
               loop
                 exit when mydate2::DATE > attend::DATE ;
                 insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1) values (emp_rec.id,mydate2::DATE,mydate2::TEXT) ;
                 select mydate2::DATE + interval '1 days' into mydate2 ;   
               end loop ;
               open att_cur for select * from alldo_gh_iot_emp_attendance where attendance_id=emp_rec.id and 
                  (attendance_date + interval '8 hours')::DATE >= attstart::DATE and 
                  (attendance_date + interval '8 hours')::DATE <= attend::DATE order by attendance_date;
               loop
                  fetch att_cur into att_rec ;
                  exit when not found ;
                  select (att_rec.attendance_date + interval '8 hours')::DATE into mydate ;
                  mydate1 = mydate::TEXT ;
                  select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=emp_rec.id and
                       attend_date1 = mydate1 ;
                  select lpad(date_part('hour',att_rec.attendance_date + interval '8 hours')::TEXT,2,'0') into chour ;
                  select lpad(date_part('minute',att_rec.attendance_date)::TEXT,2,'0') into cmin ;
                  select lpad(date_part('second',att_rec.attendance_date)::TEXT,2,'0') into csecond ;
                  /* mytime = concat(chour,':',cmin,':',csecond) ;   */
                  mytime = concat(chour,':',cmin) ;  
                  if ncount = 0 then
                   if att_rec.attendance_type='1' then   
                        insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_start,att_start_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='2' then
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_end,att_end_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='3' then   
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,otattendance_start,otatt_start_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='4' then   
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,otattendance_end,otatt_end_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;   
                     end if ;
                   else 
                      if att_rec.attendance_type='1' then
                        execute writeattendlist(emp_rec.id,att_rec.attendance_date,'1') ;
                      elsif att_rec.attendance_type='2' then
                        execute writeattendlist(emp_rec.id,att_rec.attendance_date,'2') ;
                      elsif att_rec.attendance_type='3' then 
                          execute writeattendlist(emp_rec.id,att_rec.attendance_date,'3') ;
                      elsif att_rec.attendance_type='4' then 
                         execute writeattendlist(emp_rec.id,att_rec.attendance_date,'4') ;                       
                     end if ;
                  end if ;     
               end loop ;
               close att_cur ;   
            end loop ;
            close emp_cur ;
             open list_cur for select * from alldo_gh_iot_emp_attendance_list ;
               loop
                  fetch list_cur into list_rec ;
                  exit when not found ;
                  select abs(extract(minute from (select age(list_rec.att_end_date,list_rec.att_start_date)))) into listmin ;
                  select abs(extract(hours from (select age(list_rec.att_end_date,list_rec.att_start_date)))) into listhour ; 
                  listtot = listhour::numeric + round((listmin::numeric/60::numeric),2) ;
                  if (substring(list_rec.attendance_end,1,2))::INT <= 9 then
                     if listtot >= 8 then
                            listtot = 8 ;
                     end if ;
                  else
                      if listtot > 5 then
                         listtot = listtot - 1 ;
                         if listtot >= 8 then
                            listtot = 8 ;
                         end if ;
                      end if ;
                  end if ;   
                  listmin1 = 0 ;
                  listhour1 = 0 ;
                  listtot1 = 0 ;
                  if list_rec.att_start_date1 is not null and list_rec.att_end_date1 is not null then
                     select abs(extract(minute from (select age(list_rec.att_end_date1,list_rec.att_start_date1)))) into listmin1 ;
                     select abs(extract(hours from (select age(list_rec.att_end_date1,list_rec.att_start_date1)))) into listhour1 ; 
                      listtot1 = listhour1::numeric + round((listmin1::numeric/60::numeric),2) ;
                      if (substring(list_rec.attendance_end1,1,2))::INT <= 9 then
                         if listtot1 >= 8 then
                                listtot1 = 8 ;
                         end if ;
                      else
                          if listtot1 > 5 then
                             listtot1 = listtot1 - 1 ;
                             if listtot1 >= 8 then
                                listtot1 = 8 ;
                             end if ;
                          end if ;
                      end if ;   
                  end if ;
                  listmin2 = 0 ;
                  listhour2 = 0 ;
                  listtot2 = 0 ;
                  if list_rec.att_start_date2 is not null and list_rec.att_end_date2 is not null then
                     select abs(extract(minute from (select age(list_rec.att_end_date2,list_rec.att_start_date2)))) into listmin2 ;
                     select abs(extract(hours from (select age(list_rec.att_end_date2,list_rec.att_start_date2)))) into listhour2 ; 
                      listtot2 = listhour2::numeric + round((listmin2::numeric/60::numeric),2) ;
                      if (substring(list_rec.attendance_end2,1,2))::INT < 9 then
                         if listtot2 >= 8 then
                                listtot2 = 8 ;
                         end if ;
                      else
                          if listtot2 > 5 then
                             listtot2 = listtot2 - 1 ;
                             if listtot2 >= 8 then
                                listtot2 = 8 ;
                             end if ;
                          end if ;
                      end if ;   
                  end if ;
                  update alldo_gh_iot_emp_attendance_list set att_duration=listtot where id = list_rec.id ;
                  if listtot1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att1_duration=listtot1 where id = list_rec.id ;
                  end if ;
                  if listtot2 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att2_duration=listtot2 where id = list_rec.id ;
                  end if ;
                  if list_rec.otatt_start_date is not null and list_rec.otatt_end_date is not null then
                     select extract(minute from (select age(list_rec.otatt_end_date,list_rec.otatt_start_date))) into listmin3 ;
                     select extract(hours from (select age(list_rec.otatt_end_date,list_rec.otatt_start_date))) into listhour3 ;  
                     select concat(list_rec.otatt_start_date::DATE::TEXT,' 09:00:00')::timestamp into otattstime1 ;
                     select concat(list_rec.otatt_start_date::DATE::TEXT,' 09:30:00')::timestamp into otattstime2 ;
                      
                     listtot3 = listhour3::numeric + round((listmin3::numeric/60::numeric),2) ;   
                     if list_rec.otatt_start_date between otattstime1 and otattstime2 then
                        if listtot3 >= 1.5 then
                           select extract(minute from (select age(list_rec.otatt_end_date,otattstime2))) into listmin3 ;
                           select extract(hours from (select age(list_rec.otatt_end_date,otattstime2))) into listhour3 ;
                           listtot3 = listhour3::numeric + round((listmin3::numeric/60::numeric),2) ;
                        end if ;
                     end if ;      
                     
                     update alldo_gh_iot_emp_attendance_list set otatt_duration=listtot3 where id = list_rec.id ;
                  end if ;
               end loop ;
           close list_cur ;  
           execute check_attendance(); 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists writeattendlist(myempno int,mydatetime timestamp,mytype char) cascade""")
        self.env.cr.execute("""create or replace function writeattendlist(myempno int,mydatetime timestamp,mytype char) returns void as $BODY$
          DECLARE
            ncount int ;
            ncount1 int ;
            ncount2 int ;
            mydate date ;
            mydate1 varchar ;
            chour varchar;
            cmin varchar ;
            csecond varchar ;
            mytime varchar ;
          BEGIN
            select (mydatetime + interval '8 hours')::DATE into mydate ;
            mydate1 = mydate::TEXT ;
            select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=myempno and
               attend_date1 = mydate1 ;
            select lpad(date_part('hour',mydatetime + interval '8 hours')::TEXT,2,'0') into chour ;
            select lpad(date_part('minute',mydatetime)::TEXT,2,'0') into cmin ;
            select lpad(date_part('second',mydatetime)::TEXT,2,'0') into csecond ;
            mytime = concat(chour,':',cmin,':',csecond) ; 
            if mytype = '1' then
               select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_start is null ;
               if ncount > 0 then
                  update alldo_gh_iot_emp_attendance_list set att_start_date=mydatetime,attendance_start=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_start is null ;
               else
                  select count(*) into ncount1 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_start1 is null ;
                  if ncount1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att_start_date1=mydatetime,attendance_start1=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_start1 is null ;
                  else
                     select count(*) into ncount2 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_start2 is null ;
                     if ncount2 > 0 then
                        update alldo_gh_iot_emp_attendance_list set att_start_date2=mydatetime,attendance_start2=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_start2 is null ;
                     end if ;
                  end if ;
               end if ;
            elsif mytype = '2' then
               if substring(mytime,1,2)::INT < 6 then
                    select ((mydate::DATE - interval '1 days'))::DATE::TEXT into mydate1 ; 
               end if ;             
              select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_end is null ;
               if ncount > 0 then
                  update alldo_gh_iot_emp_attendance_list set att_end_date=mydatetime,attendance_end=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_end is null ;
               else
                  select count(*) into ncount1 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_end1 is null ;
                  if ncount1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att_end_date1=mydatetime,attendance_end1=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_end1 is null ;
                  else
                     select count(*) into ncount2 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and attendance_end2 is null ;
                     if ncount2 > 0 then
                        update alldo_gh_iot_emp_attendance_list set att_end_date2=mydatetime,attendance_end2=mytime where emp_no=myempno and attend_date1=mydate1 and attendance_end2 is null ;
                     end if ;
                  end if ;
               end if ;
            elsif mytype = '3' then
              select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date::DATE = (mydatetime + interval '8 hours')::DATE and otattendance_start is null ;
               if ncount > 0 then
                  update alldo_gh_iot_emp_attendance_list set otatt_start_date=mydatetime,otattendance_start=mytime where emp_no=myempno and attend_date::DATE=(mydatetime + interval '8 hours')::DATE and otattendance_start is null ;
               else
                  select count(*) into ncount1 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date::DATE=mydatetime::DATE and otattendance_start1 is null ;
                  if ncount1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set otatt_start_date1=mydatetime,otattendance_start1=mytime where emp_no=myempno and attend_date::DATE=mydatetime::DATE and attendance_start1 is null ;
                  end if ;
               end if ;
            else
               if substring(mytime,1,2)::INT < 6 then
                    select ((mydate::DATE - interval '1 days'))::DATE::TEXT into mydate1 ; 
               end if ;     
               select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date1=mydate1 and otattendance_end is null ;
               if ncount > 0 then
                  update alldo_gh_iot_emp_attendance_list set otatt_end_date=mydatetime,otattendance_end=mytime where emp_no=myempno and attend_date1=mydate1 and otattendance_end is null ;
               else
                  select count(*) into ncount1 from alldo_gh_iot_emp_attendance_list where emp_no=myempno and attend_date::DATE=mydatetime::DATE and otattendance_end1 is null ;
                  if ncount1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set otatt_end_date1=mydatetime,otattendance_end1=mytime where emp_no=myempno and attend_date::DATE=mydatetime::DATE and attendance_end1 is null ;
                  end if ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genattendance2(empno int,attstart DATE,attend DATE) cascade""")
        self.env.cr.execute("""create or replace function genattendance2(empno int,attstart DATE,attend DATE) returns void as $BODY$
           DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            att_cur refcursor ;
            att_rec record ;
            ncount int ;
            chour varchar ;
            cmin varchar ;
            csecond varchar ;
            mytime varchar ;
            mydate date ;
            mydate1 varchar ;
            ondutydatetime timestamp ;
            offdutydatetime timestamp ;
            list_cur refcursor ;
            list_rec record ;
            listmin float ;
            listhour float ;
            listmin1 float ;
            listhour1 float ;
            listmin2 float ;
            listhour2 float ;
            listmin3 float ;
            listhour3 float ;
            listtot float ;
           
            listtot1 float ;
            listtot2 float ;
            listtot3 float ;
            mytime1 timestamp ;
            mytime2 timestamp ;
            mynowdate varchar ;
            mydate2 date ;
            ncount1 int ;
          BEGIN
            delete from alldo_gh_iot_emp_attendance_list ;
            open emp_cur for select * from hr_employee where id=empno ;
            loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               mydate2 = attstart::DATE ;
               loop
                 exit when mydate2::DATE > attend::DATE ;
                 insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1) values (emp_rec.id,mydate2::DATE,mydate2::TEXT) ;
                 select mydate2::DATE + interval '1 days' into mydate2 ;   
               end loop ;
               open att_cur for select * from alldo_gh_iot_emp_attendance where attendance_id=emp_rec.id and 
                  (attendance_date + interval '8 hours')::DATE >= attstart::DATE and 
                  (attendance_date + interval '8 hours')::DATE <= attend::DATE order by attendance_date;
               loop
                  fetch att_cur into att_rec ;
                  exit when not found ;
                  select (att_rec.attendance_date + interval '8 hours')::DATE into mydate ;
                  mydate1 = mydate::TEXT ;
                  select count(*) into ncount from alldo_gh_iot_emp_attendance_list where emp_no=emp_rec.id and
                       attend_date1 = mydate1 ;
                  select lpad(date_part('hour',att_rec.attendance_date + interval '8 hours')::TEXT,2,'0') into chour ;
                  select lpad(date_part('minute',att_rec.attendance_date)::TEXT,2,'0') into cmin ;
                  select lpad(date_part('second',att_rec.attendance_date)::TEXT,2,'0') into csecond ;
                  mytime = concat(chour,':',cmin,':',csecond) ;     
                  if ncount = 0 then
                   if att_rec.attendance_type='1' then   
                        insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_start,att_start_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='2' then
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_end,att_end_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='3' then   
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,otattendance_start,otatt_start_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;
                     elsif att_rec.attendance_type='4' then   
                       insert into alldo_gh_iot_emp_attendance_list(emp_no,attend_date,attend_date1,otattendance_end,otatt_end_date) values 
                        (emp_rec.id,mydate,mydate1,mytime,att_rec.attendance_date) ;   
                     end if ;
                   else 
                      if att_rec.attendance_type='1' then
                        execute writeattendlist(emp_rec.id,att_rec.attendance_date,'1') ;
                      elsif att_rec.attendance_type='2' then
                        execute writeattendlist(emp_rec.id,att_rec.attendance_date,'2') ;
                      elsif att_rec.attendance_type='3' then 
                          execute writeattendlist(emp_rec.id,att_rec.attendance_date,'3') ;
                      elsif att_rec.attendance_type='4' then 
                         execute writeattendlist(emp_rec.id,att_rec.attendance_date,'4') ;                       
                     end if ;
                  end if ;     
               end loop ;
               close att_cur ;   
            end loop ;
            close emp_cur ;
             open list_cur for select * from alldo_gh_iot_emp_attendance_list ;
               loop
                  fetch list_cur into list_rec ;
                  exit when not found ;
                  select abs(extract(minute from (select age(list_rec.att_end_date,list_rec.att_start_date)))) into listmin ;
                  select abs(extract(hours from (select age(list_rec.att_end_date,list_rec.att_start_date)))) into listhour ; 
                  listtot = listhour::numeric + round((listmin::numeric/60::numeric),2) ;
                  if (substring(list_rec.attendance_end,1,2))::INT <= 9 then
                     if listtot >= 8 then
                            listtot = 8 ;
                     end if ;
                  else
                      if listtot > 5 then
                         listtot = listtot - 1 ;
                         if listtot >= 8 then
                            listtot = 8 ;
                         end if ;
                      end if ;
                  end if ;   
                  listmin1 = 0 ;
                  listhour1 = 0 ;
                  listtot1 = 0 ;
                  if list_rec.att_start_date1 is not null and list_rec.att_end_date1 is not null then
                     select abs(extract(minute from (select age(list_rec.att_end_date1,list_rec.att_start_date1)))) into listmin1 ;
                     select abs(extract(hours from (select age(list_rec.att_end_date1,list_rec.att_start_date1)))) into listhour1 ; 
                      listtot1 = listhour1::numeric + round((listmin1::numeric/60::numeric),2) ;
                      if (substring(list_rec.attendance_end1,1,2))::INT <= 9 then
                         if listtot1 >= 8 then
                                listtot1 = 8 ;
                         end if ;
                      else
                          if listtot1 > 5 then
                             listtot1 = listtot1 - 1 ;
                             if listtot1 >= 8 then
                                listtot1 = 8 ;
                             end if ;
                          end if ;
                      end if ;   
                  end if ;
                  listmin2 = 0 ;
                  listhour2 = 0 ;
                  listtot2 = 0 ;
                  if list_rec.att_start_date2 is not null and list_rec.att_end_date2 is not null then
                     select abs(extract(minute from (select age(list_rec.att_end_date2,list_rec.att_start_date2)))) into listmin2 ;
                     select abs(extract(hours from (select age(list_rec.att_end_date2,list_rec.att_start_date2)))) into listhour2 ; 
                      listtot2 = listhour2::numeric + round((listmin2::numeric/60::numeric),2) ;
                      if (substring(list_rec.attendance_end2,1,2))::INT <= 9 then
                         if listtot2 >= 8 then
                                listtot2 = 8 ;
                         end if ;
                      else
                          if listtot2 > 5 then
                             listtot2 = listtot2 - 1 ;
                             if listtot2 >= 8 then
                                listtot2 = 8 ;
                             end if ;
                          end if ;
                      end if ;   
                  end if ;
                  update alldo_gh_iot_emp_attendance_list set att_duration=listtot where id = list_rec.id ;
                  if listtot1 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att1_duration=listtot1 where id = list_rec.id ;
                  end if ;
                  if listtot2 > 0 then
                     update alldo_gh_iot_emp_attendance_list set att2_duration=listtot2 where id = list_rec.id ;
                  end if ;
                  if list_rec.otatt_start_date is not null and list_rec.otatt_end_date is not null then
                     select extract(minute from (select age(list_rec.otatt_end_date,list_rec.otatt_start_date))) into listmin3 ;
                     select extract(hours from (select age(list_rec.otatt_end_date,list_rec.otatt_start_date))) into listhour3 ; 
                     listtot3 = listhour3::numeric + round((listmin3::numeric/60::numeric),2) ;
                     update alldo_gh_iot_emp_attendance_list set otatt_duration=listtot3 where id = list_rec.id ;
                  end if ;
               end loop ;
           close list_cur ;  
           execute check_attendance(); 
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists genoutsourcinginout(partnerid int,prodid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genoutsourcinginout(partnerid int,prodid int,startdate date,enddate date) returns void as $BODY$
          DECLARE
            out_cur refcursor ;
            out_rec record ;
            in_cur refcursor ;
            in_rec record ;
            list_cur refcursor ;
            list_rec record ;
            nowbalance float ;
            mydate varchar ;
            ncount int ;
            resourceid int ;
            empid int ;
          BEGIN
            delete from alldo_gh_iot_inout_prod_list ;
            if prodid = 0 then
               open out_cur for select * from alldo_gh_iot_partner_prodout where partner_id=partnerid and
                   prodout_datetime::DATE >= startdate::DATE and prodout_datetime::DATE <= enddate::DATE  ;
            else
               open out_cur for select * from alldo_gh_iot_partner_prodout where partner_id=partnerid and
               product_no=prodid and prodout_datetime::DATE >= startdate::DATE and prodout_datetime::DATE <= enddate::DATE ;
            end if ;
            loop
                fetch out_cur into out_rec ;
                exit when not found ;
                select out_rec.prodout_datetime::DATE::TEXT into mydate ;
                select id into resourceid from resource_resource where user_id = out_rec.out_owner ;
                select id into empid from hr_employee where resource_id=resourceid ;
                if out_rec.out_owner is null then
                   insert into alldo_gh_iot_inout_prod_list(inout_date1,product_id,out_num,inout_partner) values
                      (mydate,out_rec.product_no,out_rec.out_good_num,partnerid) ;
                else
                   insert into alldo_gh_iot_inout_prod_list(inout_date1,product_id,out_num,out_owner,inout_partner) values
                      (mydate,out_rec.product_no,out_rec.out_good_num,empid,partnerid) ;
                end if ;
                
            end loop ;
            close out_cur ;   
            open in_cur for select * from alldo_gh_iot_partner_prodin where partner_id=partnerid and
               product_no=prodid and prodin_datetime::DATE >= startdate::DATE and prodin_datetime::DATE <= enddate::DATE ;
            loop
                fetch in_cur into in_rec ;
                exit when not found ;
                select in_rec.prodin_datetime::DATE::TEXT into mydate ;
                 select id into resourceid from resource_resource where user_id = in_rec.in_owner ;
                select id into empid from hr_employee where resource_id=resourceid ;
                if in_rec.in_owner is null then
                   insert into alldo_gh_iot_inout_prod_list(inout_date1,product_id,in_good_num,in_ng_num,inout_partner) values
                       (mydate,in_rec.product_no,in_rec.in_good_num,in_rec.in_ng_num,partnerid) ;
                else
                    insert into alldo_gh_iot_inout_prod_list(inout_date1,product_id,in_good_num,in_ng_num,in_owner,inout_partner) values
                       (mydate,in_rec.product_no,in_rec.in_good_num,in_rec.in_ng_num,empid,partnerid) ;
                end if ;
            end loop ;
            close in_cur ;  
            nowbalance = 0 ;
            open list_cur for select * from alldo_gh_iot_inout_prod_list order by inout_date ; 
            loop
              fetch list_cur into list_rec ;
              exit when not found ;
              nowbalance = nowbalance + coalesce(list_rec.out_num,0) - coalesce(list_rec.in_good_num,0) - coalesce(list_rec.in_ng_num,0) ;
              update alldo_gh_iot_inout_prod_list set balance_num=nowbalance where id = list_rec.id ;
            end loop ;
            close list_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW stock_picking_move_line_view AS
          SELECT SP.id,SP.name,SP.report_no,SP.partner_id,SP.origin,SP.date_done,SP.picking_type_id,SP.state,SML.location_id,
             SML.product_id,SML.qty_done,SML.picking_id from stock_picking SP left join stock_move_line SML on SP.id = SML.picking_id 
             where SP.state='done' and SP.picking_type_id=2 ;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW stock_picking_move_return_line_view AS
                  SELECT SP.id,SP.name,SP.report_no,SP.partner_id,SP.origin,SP.date_done,SP.picking_type_id,SP.state,SML.location_id,
                     SML.product_id,SML.qty_done,SML.picking_id from stock_picking SP left join stock_move_line SML on SP.id = SML.picking_id 
                     where SP.state='done' and SP.picking_type_id=1 and origin like '%退回%' ;""")

        self.env.cr.execute("""drop function if exists genshippingexcel(partnerid int,prodid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genshippingexcel(partnerid int,prodid int,startdate date,enddate date) returns void as $BODY$
          DECLARE
            mv_cur refcursor ;
            mv_rec record ; 
            mv1_cur refcursor ;
            mv1_rec record ;
            mydate varchar ;
          BEGIN
            delete from alldo_gh_iot_shipping_list ;
            if prodid = 0 then
               open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid  
               order by date_done,name ;
            else
              open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid and  
               product_id=prodid order by date_done,name ;
            end if ;
            loop
              fetch mv_cur into mv_rec ;
              exit when not found ;
              select mv_rec.date_done::TEXT into mydate ;
              insert into alldo_gh_iot_shipping_list(name,report_no,location_id,partner_id,shipping_date,shipping_date1,product_id,qty_done,origin) values
                (mv_rec.name,mv_rec.report_no,mv_rec.location_id,mv_rec.partner_id,mv_rec.date_done,mydate,mv_rec.product_id,mv_rec.qty_done,mv_rec.origin) ;
            end loop ;
            close mv_cur ;  
             if prodid = 0 then
               open mv1_cur for select * from stock_picking_move_return_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid  
               order by date_done,name ;
            else
              open mv1_cur for select * from stock_picking_move_return_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid and  
               product_id=prodid order by date_done,name ;
            end if ; 
             loop
              fetch mv1_cur into mv1_rec ;
              exit when not found ;
              select mv1_rec.date_done::TEXT into mydate ;
              insert into alldo_gh_iot_shipping_list(name,report_no,location_id,partner_id,shipping_date,shipping_date1,product_id,qty_done,origin) values
                (mv1_rec.name,mv1_rec.report_no,mv1_rec.location_id,mv1_rec.partner_id,mv1_rec.date_done,mydate,mv1_rec.product_id,(mv1_rec.qty_done * -1),mv1_rec.origin) ;
            end loop ;
            close mv1_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop view if exists alldo_gh_iot_ngreturn_view cascade""")
        self.env.cr.execute("""CREATE OR REPLACE VIEW alldo_gh_iot_ngreturn_view AS
                         SELECT QC.id as qid,QC.order_id,QC.qc_date,QC.material_ng_num,QC.processing_ng_num,QC.loss_num,QC.report_no,QC.iot_node,QC.line_memo,WK.cus_name,WK.name,WK.product_no,WK.blank_no
                         from alldo_gh_iot_workorder_qc QC left join alldo_gh_iot_workorder WK on QC.order_id = WK.id where QC.material_ng_num > 0 or
                         QC.processing_ng_num > 0 or QC.loss_num > 0  """)

        self.env.cr.execute("""drop function if exists genngreturnexcel(partnerid int,prodid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genngreturnexcel(partnerid int,prodid int,startdate date,enddate date) returns void as $BODY$
         DECLARE
           ng_cur refcursor ;
           ng_rec record ; 
           outng_cur refcursor ;
           outng_rec record ;
           mydate varchar ;
           mytype char ;
         BEGIN
           delete from alldo_gh_iot_ngreturn_list ;
           if prodid = 0 then
              open ng_cur for select * from alldo_gh_iot_ngreturn_view where qc_date >= startdate and qc_date <= enddate and cus_name=partnerid  
              order by qc_date,name ;
           else
             open ng_cur for select * from alldo_gh_iot_ngreturn_view where qc_date >= startdate and qc_date <= enddate and cus_name=partnerid and  
              (product_no=prodid or blank_no=prodid) order by qc_date,name ;
           end if ;
           loop
             fetch ng_cur into ng_rec ;
             exit when not found ;
             select ng_rec.qc_date::TEXT into mydate ;
             if ng_rec.iot_node is null then
                mytype = '2' ;
             else
                mytype = '1' ;
             end if ;
             insert into alldo_gh_iot_ngreturn_list(name,report_no,partner_id,ngreturn_date,ngreturn_date1,product_id,material_ng_num,processing_ng_num,loss_num,ngreturn_type) values
               (ng_rec.name,ng_rec.report_no,ng_rec.cus_name,ng_rec.qc_date,mydate,ng_rec.product_no,ng_rec.material_ng_num,ng_rec.processing_ng_num,ng_rec.loss_num,mytype) ;
           end loop ;
           close ng_cur ;  
         END;$BODY$
         LANGUAGE plpgsql;""")



        self.env.cr.execute("""drop function if exists empotonduty(empno varchar) cascade""")
        self.env.cr.execute("""create or replace function empotonduty(empno varchar) returns varchar as $BODY$
           DECLARE
             myid int ;
             mynowdate DATE;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             ncount int ;
             myname varchar ;
             mydutytime varchar ;
             mydate varchar ;
             mytime varchar ;
             myres varchar ;
           BEGIN
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp  into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select mynowdatetime1::DATE::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno and active=True ;
             if myid is not null then
               insert into alldo_gh_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'3',mynowdatetime) ;
               update hr_employee set duty_type='3',duty_datetime=mynowdatetime,write_date=mynowdatetime where id=myid ;
               myres = concat(myname,'-',mydutytime);
               return myres ;       
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists empotoffduty(empno varchar) cascade""")
        self.env.cr.execute("""create or replace function empotoffduty(empno varchar) returns varchar as $BODY$
           DECLARE
             myid int ;
             mynowdate DATE;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             ncount int ;
             myname varchar ;
             mydutytime varchar ;
             mydate varchar ;
             mytime varchar ;
             myres varchar ;
           BEGIN
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp  into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select mynowdatetime1::DATE::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno and active=True;
             if myid is not null then
               insert into alldo_gh_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'4',mynowdatetime) ;
               update hr_employee set duty_type='4',duty_datetime=mynowdatetime,write_date=mynowdatetime where id=myid ;
               myres = concat(myname,'-',mydutytime);
               return myres ;       
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmonotodaynum(equipid int,monoid int) cascade""")
        self.env.cr.execute("""create or replace function getmonotodaynum(equipid int,monoid int) returns INT as $BODY$
           DECLARE
             myres int ;
           BEGIN
             select coalesce(sum(iot_num),0) into myres from alldo_gh_iot_equipment_iot_data where iot_id=equipid and iot_workorder=monoid 
                 and iot_datetime::DATE = (now() + interval '2 hours')::DATE ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genequipmentdaily() cascade""")
        self.env.cr.execute("""create or replace function genequipmentdaily() returns void as $BODY$
           DECLARE
             equ_cur refcursor ;
             equ_rec record ;
             myres int ;
             mynowdatetime timestamp ;
             mystartdatetime timestamp ;
             mynowdate date ;
             prodid int ;
             prodtmplid int ;
             engtype varchar ;
             standardnum int ;
             opentimem int ;
             opentimeh int ;
             opentime int ;
             stdminnum int ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select current_timestamp::DATE into mynowdate ;
             mystartdatetime = (concat(mynowdate::TEXT,' 00:00:00'))::timestamp ;
             select date_part('hours',age(mynowdatetime,mystartdatetime))::INTEGER into opentimeh ;
             if opentimeh >= 5 then
                opentimeh = opentimeh - 1 ;    /* 中午午休 不算 */ 
             end if ;   
             select date_part('minutes',age(mynowdatetime,mystartdatetime))::INTEGER into opentimem ;
             opentime = (opentimeh * 60) + opentimem ;
             open equ_cur for select * from maintenance_equipment order by equipment_no ;
             loop
                fetch equ_cur into equ_rec ;
                exit when not found ;
                /* select sum(coalesce(iot_num,0)) into myres from alldo_gh_iot_equipment_iot_data where iot_id=equ_rec.id and iot_workorder=equ_rec.mo_no
                 and iot_datetime::DATE = (now() + interval '2 hours')::DATE ;*/
                 select sum(coalesce(iot_num,0)) into myres from alldo_gh_iot_equipment_iot_data where iot_id=equ_rec.id and iot_workorder=equ_rec.mo_no
                 and (iot_datetime + interval '8 hours')::DATE = (now() + interval '8 hours')::DATE ;
                select product_no,eng_type into prodid,engtype from alldo_gh_iot_workorder where id = equ_rec.mo_no ;
                select product_tmpl_id into prodtmplid from product_product where id = prodid ;
                select max(standard_num) into standardnum from alldo_gh_iot_eng_order where prod_id=prodtmplid and TRIM(eng_type) like TRIM(engtype) ;
                select round((standardnum::numeric/60::numeric)*opentime::numeric,0) into stdminnum;
                update maintenance_equipment set mono_today_num=myres,std_today_num=stdminnum where id = equ_rec.id ;
                update alldo_gh_iot_workorder set state='3' where id = equ_rec.mo_no and (state='2' or state='1') ;
             end loop ;
             close equ_cur ; 
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmostdduration(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmostdduration(moid int) returns INT as $BODY$
           DECLARE
             myres int ;
             prodid int ;
             prodtmplid int ;
             engtype varchar ;
             stdnum int ;
           BEGIN
             select product_no,eng_type into prodid,engtype from alldo_gh_iot_workorder where id = moid ;
             select product_tmpl_id into prodtmplid from product_product where id = prodid ;
             select coalesce(standard_num,0) into stdnum from alldo_gh_iot_eng_order where prod_id=prodtmplid and eng_type=engtype ;
             if stdnum = 0 then
                myres = 0 ;
             else
                myres = round((3600::numeric / stdnum::numeric),0) ;
             end if ;   
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;  """)

        self.env.cr.execute("""CREATE OR REPLACE VIEW alldo_gh_iot_workorder_view AS
                 select WK.id as wkid,WK.name,WK.product_no,WK.eng_type,WK.po_no,WK.cus_name,WK.order_num,WK.prod_num,WK.shipping_num,WK.prod_duration,
                 DT.id as dtid,DT.order_id,DT,iot_date,DT.iot_node,DT.iot_owner,DT.iot_num,DT.iot_duration,DT.std_duration 
                 from alldo_gh_iot_workorder_iot_data DT left join alldo_gh_iot_workorder WK on WK.id= DT.order_id where WK.state in ('3','4') """)


        self.env.cr.execute("""drop function if exists genwkperformance(startdate date,enddate date,prodid int,empid int,equipid int) cascade""")
        self.env.cr.execute("""drop function if exists genwkperformance(startdate date,enddate date,prodid int,engtype char,empid int,equipid int) cascade""")
        self.env.cr.execute("""create or replace function genwkperformance(startdate date,enddate date,prodid int,engtype char,empid int,equipid int) returns void as $BODY$
          DECLARE
            iot_cur refcursor ;
            iot_rec record ; 
            mywkid int ;
            myiotnum int ;
            myiotduration float ;
            mystdduration float ;
            mygoodnum int ;
            myngnum int ;
            myperfrate float ;
            myprodid int ;
            myengtype varchar ;
            myempid int ;
            mynodeid int ;
            startdate1 varchar ;
            enddate1 varchar ;
          BEGIN
            mywkid = 0 ; 
            myiotnum = 0 ;
            myiotduration = 0 ;
            mystdduration = 0 ;
            mynodeid = 0 ;
            myempid = 0 ;
            if engtype='1' then
               myengtype='一' ;
            elsif engtype='2' then
               myengtype='二' ;
            elsif engtype='3' then
               myengtype='三' ;   
            elsif engtype='4' then
               myengtype='四' ;
            elsif engtype='5' then
               myengtype='五' ;
            elsif engtype='6' then
               myengtype='六' ;
            elsif engtype='7' then
               myengtype='七' ;
            else
               myengtype='八' ; 
            end if ; 
            delete from alldo_gh_iot_workorder_performance_list1 ;
            if prodid = 0 and empid = 0 and equipid > 0 then
                open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid = 0 and empid > 0 and equipid = 0 then
                open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid > 0 and empid = 0 and equipid = 0 then
                if engtype='0' then
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid order by wkorder_id,iot_node,iot_owner ;
                else                    
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid 
                        and eng_type like '%'|| myengtype||'%'  order by wkorder_id,iot_node,iot_owner ;
                end if ;        
            elsif prodid = 0 and empid > 0 and equipid > 0 then
                open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                    (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid > 0 and empid = 0 and equipid > 0 then
                if engtype='0' then
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
                else
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid and iot_node = equipid 
                        and eng_type like '%'|| myengtype||'%'   order by wkorder_id,iot_node,iot_owner ;
                end if ;        
            elsif prodid > 0 and empid > 0 and equipid = 0 then
                if engtype='0' then
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date between startdate and enddate) and iot_owner = empid and product_no = prodid order by wkorder_id,iot_node,iot_owner ; 
                else
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                        (iot_date between startdate and enddate) and iot_owner = empid and product_no = prodid 
                        and eng_type like '%'|| myengtype||'%'  order by wkorder_id,iot_node,iot_owner ; 
                end if ;        
            elsif prodid = 0 and empid = 0 and equipid = 0 then
                open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                   (iot_date::DATE between startdate::DATE and enddate::DATE) order by wkorder_id,iot_node,iot_owner ;
            else
                if engtype='0' then
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                       (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid and product_no = prodid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
                else
                    open iot_cur for select * from alldo_gh_iot_cnc_performance_report where 
                       (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid and product_no = prodid and iot_node = equipid 
                       and eng_type like '%'|| myengtype||'%'  order by wkorder_id,iot_node,iot_owner ;
                end if ;       
            end if ;
           loop
              fetch iot_cur into iot_rec ;
              exit when not found ;
              select to_char(iot_rec.iot_start,'YYYY-MM-DD HH:MM:SS') into startdate1 ; 
              select to_char(iot_rec.iot_end,'YYYY-MM-DD HH:MM:SS') into enddate1 ; 
              insert into alldo_gh_iot_workorder_performance_list1(wkorder_id,iot_date,iot_owner,iot_node,iot_start,iot_end,product_no,eng_type,total_amount_num,material_ng_num,
              processing_ng_num,std_num,performance_rate,iot_duration,product_num,iot_start1,iot_end1) values (iot_rec.wkorder_id,iot_rec.iot_date::TEXT,iot_rec.iot_owner,iot_rec.iot_node,startdate1,
              enddate1,iot_rec.product_no,iot_rec.eng_type,iot_rec.total_amount_num,iot_rec.material_ng_num,iot_rec.processing_ng_num,iot_rec.std_num,round((iot_rec.performance_rate::numeric * 100::numeric),2),
              iot_rec.iot_duration,iot_rec.product_num,iot_rec.iot_start,iot_rec.iot_end) ;
            end loop ;
            close iot_cur ;       
          END;$BODY$
          LANGUAGE plpgsql;""")



        self.env.cr.execute("""drop function if exists genwkperformance1(startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genwkperformance1(startdate date,enddate date) returns void as $BODY$
           DECLARE
             iotwk_cur refcursor ;
             iotwk_rec record ; 
             mywkid int ;
             myiotnum int ;
             myiotduration float ;
             mystdduration float ;
             mygoodnum int ;
             myngnum int ;
             myperfrate float ;
             myprodid int ;
             myengtype varchar ;
           BEGIN
             mywkid = 0 ; 
             myiotnum = 0 ;
             myiotduration = 0 ;
             mystdduration = 0 ;
             delete from alldo_gh_iot_workorder_performance_list ;
             open iotwk_cur for select * from alldo_gh_iot_workorder_iot_data where (iot_date::timestamp + interval '8 hours')::DATE 
                  between startdate::DATE and enddate::DATE  order by order_id ;
             loop
               fetch iotwk_cur into iotwk_rec ;
               exit when not found ;

               if mywkid != iotwk_rec.order_id then
                  if myiotnum != 0 then
                     select sum(coalesce(processing_ng_num,0)) into myngnum from alldo_gh_iot_workorder_qc
                        where order_id=iotwk_rec.order_id ;
                     mygoodnum = myiotnum - myngnum ;   
                     myperfrate = coalesce(round(mystdduration::numeric/myiotduration::numeric,2),0);   
                     select product_no,eng_type into myprodid,myengtype from alldo_gh_iot_workorder where id = iotwk_rec.order_id ;
                     insert into alldo_gh_iot_workorder_performance_list(order_id,iot_date,iot_node,iot_owner,good_num,ng_num,iot_duration,std_duration,owner_perfrate,product_no,eng_type)
                       values (iotwk_rec.order_id,iotwk_rec.iot_date::DATE::TEXT,iotwk_rec.iot_node,iotwk_rec.iot_owner,mygoodnum,myngnum,myiotduration,mystdduration,myperfrate,myprodid,myengtype) ;     
                  end if ;
                  myiotnum = iotwk_rec.iot_num ;
                  myiotduration = coalesce(round((iotwk_rec.iot_duration::numeric/60::numeric),2),0) ;
                  mystdduration = coalesce(round((iotwk_rec.std_duration::numeric/60::numeric),2),0) ;
                  mywkid = iotwk_rec.order_id ; 
               else   
                  myiotnum = myiotnum + coalesce(iotwk_rec.iot_num,0) ;
                  myiotduration = myiotduration + coalesce(round((iotwk_rec.iot_duration::numeric/60::numeric),2),0) ;
                  mystdduration = mystdduration + coalesce(round((iotwk_rec.std_duration::numeric/60::numeric),2),0) ;
               end if ;
             end loop ;
             close iotwk_cur ;     
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkperformance2(startdate date,enddate date,empid int) cascade""")
        self.env.cr.execute("""create or replace function genwkperformance2(startdate date,enddate date,empid int) returns void as $BODY$
           DECLARE
             iotwk_cur refcursor ;
             iotwk_rec record ; 
             mywkid int ;
             myiotnum int ;
             myiotduration float ;
             mystdduration float ;
             mygoodnum int ;
             myngnum int ;
             myperfrate float ;
             myprodid int ;
             myengtype varchar ;
           BEGIN
             mywkid = 0 ; 
             myiotnum = 0 ;
             myiotduration = 0 ;
             mystdduration = 0 ;
             delete from alldo_gh_iot_workorder_performance_list ;
             open iotwk_cur for select * from alldo_gh_iot_workorder_iot_data where (iot_date::timestamp + interval '8 hours')::DATE 
                  between startdate::DATE and enddate::DATE and iot_owner = empid order by order_id ;
             loop
               fetch iotwk_cur into iotwk_rec ;
               exit when not found ;

               if mywkid != iotwk_rec.order_id then
                  if myiotnum != 0 then
                     select sum(coalesce(processing_ng_num,0)) into myngnum from alldo_gh_iot_workorder_qc
                        where order_id=iotwk_rec.order_id ;
                     mygoodnum = myiotnum - myngnum ;   
                     myperfrate = coalesce(round(mystdduration::numeric/myiotduration::numeric,2),2);  
                      select product_no,eng_type into myprodid,myengtype from alldo_gh_iot_workorder where id = iotwk_rec.order_id ; 
                     insert into alldo_gh_iot_workorder_performance_list(order_id,iot_date,iot_node,iot_owner,good_num,ng_num,iot_duration,std_duration,owner_perfrate,product_no,eng_type)
                       values (iotwk_rec.order_id,iotwk_rec.iot_date::DATE::TEXT,iotwk_rec.iot_node,iotwk_rec.iot_owner,mygoodnum,myngnum,myiotduration,mystdduration,myperfrate,myprodid,myengtype) ;     
                  end if ;
                  myiotnum = iotwk_rec.iot_num ;
                  myiotduration = coalesce(round((iotwk_rec.iot_duration::numeric/60::numeric),2),0) ;
                  mystdduration = coalesce(round((iotwk_rec.std_duration::numeric/60::numeric),2),0) ;
                  mywkid = iotwk_rec.order_id ; 
               else   
                  myiotnum = myiotnum + coalesce(iotwk_rec.iot_num,0) ;
                  myiotduration = myiotduration + coalesce(round((iotwk_rec.iot_duration::numeric/60::numeric),2),0) ;
                  mystdduration = mystdduration + coalesce(round((iotwk_rec.std_duration::numeric/60::numeric),2),0) ;
               end if ;
             end loop ;
             close iotwk_cur ;     
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists genreplaceline1(repsdate date,repedate date) cascade""")
        self.env.cr.execute("""create or replace function genreplaceline1(repsdate date,repedate date) returns void as $BODY$
           DECLARE
             rep_cur refcursor ;
             rep_rec record ;
             prodid int ;
             engtype varchar ;
             cusname int ;
             mysdatetime varchar ;
             myedatetime varchar ; 
           BEGIN
             delete from alldo_gh_iot_replaceline_list ;
             open rep_cur for select * from alldo_gh_iot_wkorder_replaceline where replace_start_datetime::DATE between
                repsdate::DATE and repedate::DATE order by order_id ;
             loop   
               fetch rep_cur into rep_rec ;
               exit when not found ;
               select (rep_rec.replace_start_datetime + interval '8 hours')::TEXT into mysdatetime ;
               select (rep_rec.replace_end_datetime + interval '8 hours')::TEXT into myedatetime ;
               select product_no,eng_type,cus_name into prodid,engtype,cusname from alldo_gh_iot_workorder where id = rep_rec.order_id ;
                insert into alldo_gh_iot_replaceline_list(order_id,product_no,eng_type,replace_owner,equipment_id,replace_start_datetime,
                replace_end_datetime,replace_duration,partner_id) values (rep_rec.order_id,prodid,engtype,rep_rec.replace_owner,rep_rec.equipment_id,
                mysdatetime,myedatetime,rep_rec.replace_duration,cusname) ;
             end loop ;
             close rep_cur ;   
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genreplaceline2(repsdate date,repedate date,empid int) cascade""")
        self.env.cr.execute("""create or replace function genreplaceline2(repsdate date,repedate date,empid int) returns void as $BODY$
           DECLARE
             rep_cur refcursor ;
             rep_rec record ;
             prodid int ;
             engtype varchar ;
             cusname int ;
             mysdatetime varchar ;
             myedatetime varchar ;
           BEGIN
             delete from alldo_gh_iot_replaceline_list ;
             open rep_cur for select * from alldo_gh_iot_wkorder_replaceline where replace_start_datetime::DATE between
                repsdate::DATE and repedate::DATE and replace_owner = empid order by order_id ;
             loop   
               fetch rep_cur into rep_rec ;
               exit when not found ;
               select (rep_rec.replace_start_datetime + interval '8 hours')::TEXT into mysdatetime ;
               select (rep_rec.replace_end_datetime + interval '8 hours')::TEXT into myedatetime ;
               select product_no,eng_type,cus_name into prodid,engtype,cusname from alldo_gh_iot_workorder where id = rep_rec.order_id ;
                insert into alldo_gh_iot_replaceline_list(order_id,product_no,eng_type,replace_owner,equipment_id,replace_start_datetime,
                replace_end_datetime,replace_duration,partner_id) values (rep_rec.order_id,prodid,engtype,rep_rec.replace_owner,rep_rec.equipment_id,
                mysdatetime,myedatetime,rep_rec.replace_duration,cusname) ;
             end loop ;
             close rep_cur ;   
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatemoprodin(moid int,innum int) cascade""")
        self.env.cr.execute("""create or replace function updatemoprodin(moid int,innum int) returns void as $BODY$
           DECLARE
              ncount int ;
              mogrpid int ;
           BEGIN
              select count(*) into ncount from alldo_gh_iot_workorder where id = moid ;
              if ncount > 0 and innum > 0 then
                 select mo_group_id into mogrpid from alldo_gh_iot_workorder where id = moid ;
                 update alldo_gh_iot_workorder set prodin_num = coalesce(prodin_num,0) + innum where mo_group_id = mogrpid ;
              end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updateshippingwkorder(pickingid int) cascade""")
        self.env.cr.execute("""create or replace function updateshippingwkorder(pickingid int) returns void as $BODY$
           DECLARE
             ncount int ;
             mogroupid int ;
             qtynum float ;
             mybackorderid int ;
             mynowpickingid int;
             myworkorderid int;
             myordernum int;
             myshippingnum int ;
             pono1 int ;
             ncount1 int ;
             pickingdate date ;
             pickingtypeid int ;
             prodqty float ;
             prodid int ;
             po_cur refcursor ;
             po_rec record ;
           BEGIN
             qtynum = 0 ;
             select coalesce(mo_group_id,0),picking_type_id,date_done::DATE into mogroupid,pickingtypeid,pickingdate
                  from stock_picking where id = pickingid  ;
             select sum(coalesce(qty_done,0)) into qtynum from stock_move_line where picking_id in
               (select id from stock_picking where mo_group_id=mogroupid and picking_type_id=2) ;
             if mogroupid > 0 then
                if qtynum > 0 then
                    update alldo_gh_iot_workorder set shipping_num = qtynum where mo_group_id = mogroupid ;
                end if ; 
                select max(id),max(po_no1) into myworkorderid,pono1 from alldo_gh_iot_workorder where mo_group_id = mogroupid ;
                 select order_num,shipping_num into myordernum,myshippingnum from alldo_gh_iot_workorder where id = myworkorderid ;
                 if myordernum > myshippingnum then
                    update alldo_gh_iot_workorder set uncomplete_shipping=True where mo_group_id = mogroupid ;
                 else
                    update alldo_gh_iot_workorder set uncomplete_shipping=False where mo_group_id = mogroupid ;   
                 end if ;
                 select coalesce(prodout_picking,0) into mynowpickingid from alldo_gh_iot_workorder where id = myworkorderid ;
                 if mynowpickingid > 0 then
                    select max(id) into mybackorderid from stock_picking where backorder_id = mynowpickingid ; 
                    if mybackorderid > 0 then
                       update alldo_gh_iot_workorder set prodout_picking=mybackorderid where mo_group_id = mogroupid ;
                    end if ;   
                 end if ;   
               
             end if ;
             
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updateshippingwkorder1(pickingid int) cascade""")
        self.env.cr.execute("""create or replace function updateshippingwkorder1(pickingid int) returns void as $BODY$
           DECLARE
             qtynum float ;
             unqtynum float ;
             move_cur refcursor ;
             move_rec record ;
             po_cur refcursor ;
             po_rec record ;
             poid int ;
             ncount int ;
             prodid int ;
             prodno int ;
             mypickingtypeid int ;
             mynowdate date ;
             pocount int ;
             mogroupid int ;
           BEGIN
             select picking_type_id,coalesce(mo_group_id,0) into mypickingtypeid,mogroupid from stock_picking where id = pickingid ;
             if mogroupid = 0 then
                 select now()::DATE into mynowdate ;
                 open move_cur for select id,picking_id,product_id from stock_move_line where picking_id=pickingid ;
                 loop
                   fetch move_cur into move_rec ;
                   exit when not found ;
                   select count(*) into ncount from ghiot_moveline_powk_rel where move_id = move_rec.id ;
                   if ncount > 1 then
                       select sum(coalesce(qty_done,0)) into qtynum from stock_move_line where id = move_rec.id ;
                       open po_cur for select * from ghiot_moveline_powk_rel where move_id = move_rec.id ;
                       loop
                         fetch po_cur into po_rec ;
                         exit when not found ;            
                         select (coalesce(po_num,0) - coalesce(shipping_num,0)),product_no into unqtynum,prodno from alldo_gh_iot_po_wkorder where id = po_rec.po_id ; 
                         if move_rec.product_id = prodno and qtynum >= unqtynum then
                            update alldo_gh_iot_po_wkorder set shipping_num=coalesce(shipping_num,0) + unqtynum where id = po_rec.po_id ;
                            qtynum = coalesce(qtynum,0) - unqtynum ;
                           /* insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_num,picking_type_id,picking_date) values (po_rec.po_id,pickingid,unqtynum,mypickingtypeid,mynowdate) ; */
                         elsif move_rec.product_id = prodno and qtynum < unqtynum then
                            update alldo_gh_iot_po_wkorder set shipping_num=coalesce(shipping_num,0) + qtynum where id = po_rec.po_id ;
                           /*  insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_num,picking_type_id,picking_date) values (po_rec.po_id,pickingid,qtynum,mypickingtypeid,mynowdate) ; */
                            qtynum = 0 ;
                         end if ;   
                       end loop ;
                       close po_cur ;
                   elsif ncount = 1 then
                       select po_id into poid from ghiot_moveline_powk_rel where move_id = move_rec.id ;
                       select sum(coalesce(qty_done,0)) into qtynum from stock_move_line where id=move_rec.id ;  
                       update alldo_gh_iot_po_wkorder set shipping_num=qtynum where id = poid ;    
                      /* insert into alldo_gh_iot_picking_line(po_id,picking_id,picking_num,picking_type_id,picking_date) values (poid,pickingid,qtynum,mypickingtypeid,mynowdate) ; */
                   end if ;    
                 end loop ;
                 close move_cur ;
             end if ;    
           END;$BODY$
           LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists getlastmo(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getlastmo(partnerid int) returns INT as $BODY$
          DECLARE
            mogid int ;
            maxid int ;
            myres int ;
          BEGIN
            myres = 0 ;
            select max(id) into maxid from alldo_gh_iot_workorder where cus_name=partnerid ;
            select mo_group_id into mogid from alldo_gh_iot_workorder where id = maxid ;
            select min(id) into myres from alldo_gh_iot_workorder where mo_group_id=mogid and eng_order != '4';
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatemomemo(partnerid int,mydesc varchar) cascade""")
        self.env.cr.execute("""drop function if exists updatemomemo(partnerid int,mydesc varchar,stockinid int,shippingid int) cascade""")
        self.env.cr.execute("""create or replace function updatemomemo(partnerid int,mydesc varchar,stockinid int,shippingid int) returns void as $BODY$
          DECLARE
            mogid int ;
            maxid int ;
            myid int ;
            mymaxid int ;
          BEGIN
            select max(id) into maxid from alldo_gh_iot_workorder where cus_name=partnerid ;
            select mo_group_id into mogid from alldo_gh_iot_workorder where id = maxid ;
            select min(id),max(id) into myid,mymaxid from alldo_gh_iot_workorder where mo_group_id=mogid ;
            update alldo_gh_iot_workorder set workorder_memo=mydesc where mo_group_id=mogid 
                   and (workorder_memo = ' ' or workorder_memo is null) ;
            if stockinid > 0 then
               update alldo_gh_iot_workorder set blankin_picking=stockinid where mo_group_id=mogid ;
            end if ;
            if shippingid > 0 then
               update alldo_gh_iot_workorder set prodout_picking=shippingid where mo_group_id=mogid ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodblank(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodblank(prodid int) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
            myprodtmplid int ;
          BEGIN
            myres = 0 ;
            select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
            select coalesce(blank_no,0) into myres from product_template where id = myprodtmplid ;
            if myres = 0 then
               myres = prodid ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # self.env.cr.execute("""drop function if exists getmogoodnum(monoid int) cascade""")
        # self.env.cr.execute("""create or replace function getmogoodnum(monoid int) returns float as $BODY$
        #   DECLARE
        #     myres float ;
        #     prodinnum float ;
        #     goodnum float ;
        #     ordernum float ;
        #   BEGIN
        #     myres = 0 ;
        #     select coalesce(prodin_num,0),coalesce(order_num,0) into prodinnum,ordernum from alldo_gh_iot_workorder where id = monoid ;
        #     select sum(coalesce(qc_good_num,0)) into goodnum from alldo_gh_iot_workorder_qc where order_id=monoid ;
        #     if goodnum > 0 then
        #        myres = goodnum - prodinnum ;
        #     else
        #        myres = ordernum - prodinnum ;
        #     end if ;
        #     if myres < 0 then
        #        myres = 0 ;
        #     end if ;
        #     return myres ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmongnum(monoid int) cascade""")
        self.env.cr.execute("""create or replace function getmongnum(monoid int) returns float as $BODY$
          DECLARE
            myres float ;
            mogroupid int ;
          BEGIN
            myres = 0 ;
            select mo_group_id into mogroupid from alldo_gh_iot_workorder where id = monoid ;
            select sum(coalesce(material_ng_num,0) + coalesce(processing_ng_num,0) + coalesce(loss_num,0)) into myres from alldo_gh_iot_workorder_qc 
               where order_id in (select id from alldo_gh_iot_workorder where mo_group_id=mogroupid) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmolossnum(monoid int) cascade""")
        self.env.cr.execute("""create or replace function getmolossnum(monoid int) returns float as $BODY$
          DECLARE
            myres float ;
          BEGIN
            myres = 0 ;
            select sum(coalesce(loss_num,0)) into myres from alldo_gh_iot_workorder_qc where order_id=monoid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists chkmoprodinnum(monoid int,prodinnum float) cascade""")
        self.env.cr.execute("""create or replace function chkmoprodinnum(monoid int,prodinnum float) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            prodinnum1 float ;
            cncprodnum float ;
            ordernum float ;
          BEGIN
            select sum(coalesce(total_amount_num,0)) into cncprodnum from alldo_gh_iot_workorder_qc where order_id=monoid ;
            select coalesce(prodin_num,0),coalesce(order_num,0) into prodinnum1,ordernum from alldo_gh_iot_workorder where id = monoid ;
            if cncprodnum > 0 then
               if prodinnum > (cncprodnum - prodinnum1) then
                  myres = False ;
               else
                  myres = True ;
               end if ;
            else
               if prodinnum > (ordernum - prodinnum1) then
                  myres = False ;
               else
                  myres = True ;
               end if ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmogoodnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmogoodnum(moid int) returns void as $BODY$
          DECLARE
            myres int ;
          BEGIN
            select sum(coalesce(total_amount_num,0) - coalesce(material_ng_num,0) - coalesce(processing_ng_num,0) - coalesce(loss_num,0))::INT into myres from
               alldo_gh_iot_workorder_qc where order_id = moid ;
            if myres is null then
               myres = 0 ;
            end if ;   
            update alldo_gh_iot_workorder set mo_production_num=myres where id = moid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop view if exists alldo_outofforder_view""")
        self.env.cr.execute("""create or replace view alldo_outofforder_view AS select A.iot_id,A.status_id,A.iot_workorder,A.start_datetime,
          A.end_datetime,A.outoff_duration,A.outoff_owner,B.product_no,B.eng_type from alldo_gh_iot_equipment_outofforder_status A left join
           alldo_gh_iot_workorder B on A.iot_workorder = B.id where status_id=9 ;""")

        self.env.cr.execute("""drop function if exists genreplineperformance(startdate date,enddate date,prodid int,empid int,equipid int) cascade""")
        self.env.cr.execute("""create or replace function genreplineperformance(startdate date,enddate date,prodid int,empid int,equipid int) returns void as $BODY$
          DECLARE
            rep_cur refcursor ;
            rep_rec record ;
            emp_cur refcursor ;
            emp_rec record ;
            hour_duration float ;
            ncount int ;
            timeh int ;
            timem int ;
          BEGIN
            delete from alldo_gh_iot_replaceline_list ;
            if prodid = 0 and empid = 0 and equipid = 0 then
               open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                    between startdate::DATE and enddate::DATE ;
            else
                if prodid = 0 and empid = 0 and equipid > 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and iot_id = equipid order by iot_id,iot_workorder,product_no ;
                 
                elsif prodid = 0 and empid > 0 and equipid = 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and outoff_owner = empid order by iot_id,iot_workorder,product_no ; 
                   
                elsif prodid > 0 and empid = 0 and equipid = 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and product_no = prodid order by iot_id,iot_workorder,product_no ;  
                   
                elsif prodid = 0 and empid > 0 and equipid > 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and iot_id = prodid and outoff_owner = empid order by iot_id,iot_workorder,product_no ;  
                   
                elsif prodid > 0 and empid = 0 and equipid > 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and product_no = prodid and iot_id = equipid order by iot_id,iot_workorder,product_no ; 
                      
                elsif prodid > 0 and empid > 0 and equipid = 0 then
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and product_no = prodid and outoff_owner=empid order by iot_id,iot_workorder,product_no ;      
                             
                else
                    open rep_cur for select * from alldo_outofforder_view where (start_datetime::timestamp + interval '8 hours')::DATE 
                        between startdate::DATE and enddate::DATE and product_no = prodid and outoff_owner=empid and iot_id=equipid  order by iot_id,iot_workorder,product_no ; 
                      
                end if ; 
            end if ;    
             loop
                 fetch rep_cur into rep_rec ;
                 exit when not found ;
                 /* hour_duration = round((rep_rec.outoff_duration::numeric/60::numeric),1) ; */
                 select date_part('hours',age(rep_rec.end_datetime,rep_rec.start_datetime))::INTEGER into timeh ;
                 select date_part('minutes',age(rep_rec.end_datetime,rep_rec.start_datetime))::INTEGER into timem ;
                 hour_duration = timeh + round((timem::numeric/60::numeric),1) ;
                 insert into alldo_gh_iot_replaceline_list(equipment_id,order_id,product_no,eng_type,replace_start_datetime,replace_end_datetime,replace_duration,replace_owner) values
                     (rep_rec.iot_id,rep_rec.iot_workorder,rep_rec.product_no,rep_rec.eng_type,substring((rep_rec.start_datetime::timestamp + interval '8 hours')::TEXT,1,16),
                     substring((rep_rec.end_datetime::timestamp + interval '8 hours')::TEXT,1,16),hour_duration,rep_rec.outoff_owner) ;
             end loop ;
             close rep_cur ;        
                                         
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcustomerloc(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getcustomerloc(partnerid int) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            select coalesce(property_stock_customer,0) into myres from res_partner where id = partnerid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;  """)

        self.env.cr.execute("""drop function if exists getsupplierloc(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getsupplierloc(partnerid int) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            select coalesce(property_stock_supplier,0) into myres from res_partner where id = partnerid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;  """)

        self.env.cr.execute("""drop function if exists getmogpseq() cascade""")
        self.env.cr.execute("""create or replace function getmogpseq() returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_gh_iot_mo_group_seq ;
            if ncount=0 then
               myres = 100001 ;
               insert into alldo_gh_iot_mo_group_seq(seqnum) values (100002) ;
            else
               select coalesce(seqnum,100001) into myres from alldo_gh_iot_mo_group_seq  ;
               update alldo_gh_iot_mo_group_seq set seqnum = seqnum + 1 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodcus(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodcus(prodid int) returns INT as $BODY$
          DECLARE
             myres int ;
             ncount int ;
             prodtmplid int ;
          BEGIN
             select product_tmpl_id into prodtmplid from product_product where id = prodid ;
             select coalesce(cus_no,0) into myres from product_template where id = prodtmplid ;
             return myres ;
          END;$BODY$
          LANGUAGE plpgsql;   """)

        self.env.cr.execute("""CREATE OR REPLACE VIEW ghiot_prodstock_view AS
           select A.company_id,A.product_id,A.location_id,A.quantity,B.name as loc_desc,B.active,B.usage, 
           (select getprodcus(A.product_id)) as cus_no from stock_quant A left join stock_location B
           on A.location_id = B.id where B.active=True and B.usage = 'internal' and A.company_id=1 """)

        self.env.cr.execute("""drop function if exists genprodstock(prodid int) cascade""")
        self.env.cr.execute("""create or replace function genprodstock(prodid int) returns void as $BODY$
          DECLARE
            st_cur refcursor ;
            st_rec record ;
            defcode varchar ;
            prodlocid int ;
            pbookinglocid int ;
          BEGIN
            delete from alldo_gh_iot_prod_stock_list ;
            select max(prod_loc) into prodlocid from alldo_gh_iot_company_stockloc ;
            select distinct pbooking_loc into pbookinglocid from alldo_gh_iot_company_stockloc ;
            if prodid = 0 then
               open st_cur for select * from ghiot_prodstock_view order by product_id and location_id=prodlocid  ;
            else
               open st_cur for select * from ghiot_prodstock_view where product_id=prodid and location_id=prodlocid  ;
            end if ;
            loop
               fetch st_cur into st_rec ;
               exit when not found ;
               insert into alldo_gh_iot_prod_stock_list(product_no,stock_location,prod_num) values (st_rec.product_id,st_rec.location_id,st_rec.quantity) ;
              /* if st_rec.location_id=prodlocid or st_rec.location_id=pbookinglocid then
                  insert into alldo_gh_iot_prod_stock_list(product_no,stock_location,prod_num) values (st_rec.product_id,st_rec.location_id,st_rec.quantity) ;
               else
                  insert into alldo_gh_iot_prod_stock_list(product_no,stock_location,blank_num) values (st_rec.product_id,st_rec.location_id,st_rec.quantity) ;
               end if ; */  
            end loop ;
            close st_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genworkorderqcloss(workorderid int,lossnum float,iotowner int) cascade""")
        self.env.cr.execute("""create or replace function genworkorderqcloss(workorderid int,lossnum float,iotowner int) returns void as $BODY$ 
          DECLARE
            ncount int ;
            mynowdatetime timestamp ;
            cusid int ;
            prodid int ;
          BEGIN
            select cus_name,product_no into cusid,prodid from alldo_gh_iot_workorder where id=workorderid ;
            select current_timestamp - interval '8 hours' into mynowdatetime ;
            select count(*) into ncount from alldo_gh_iot_workorder_qc where order_id=workorderid and qc_date::DATE=mynowdatetime::DATE  ;
            if ncount > 0 then
               update alldo_gh_iot_workorder_qc set loss_num = coalesce(loss_num,0) + lossnum,iot_owner=iotowner,write_date=mynowdatetime,
               cus_name = cusid,product_no=prodid  where order_id=workorderid and qc_date::DATE=qcdate::DATE  ;
            else  
               insert into alldo_gh_iot_workorder_qc(order_id,qc_date,loss_num,iot_owner,create_date,cus_name,product_no) values
                 (workorderid,mynowdatetime::DATE,lossnum,iotowner,mynowdatetime,cusid,prodid) ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;
       """)

        self.env.cr.execute("""drop function if exists resetqcowner() cascade""")
        self.env.cr.execute("""create or replace function resetqcowner() returns void as $BODY$
          DECLARE
            qc_cur refcursor ;
            qc_rec record ;
            ncount int ;
          BEGIN
            open qc_cur for select * from alldo_gh_iot_workorder_qc ;
            loop
              fetch qc_cur into qc_rec ;
              exit when not found ;
              select count(*) into ncount from hr_employee where id = qc_rec.iot_owner ;
              if ncount > 0 then
                 update alldo_gh_iot_workorder_qc set iot_owner1=qc_rec.iot_owner where id = qc_rec.id ;
              end if ;
            end loop ;
            close qc_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists blankgetprod(blankid int) cascade""")
        self.env.cr.execute("""create or replace function blankgetprod(blankid int) returns setof INT as $BODY$
          DECLARE
            prod_cur refcursor ;
            prod_rec record ;
            prodid int ;
          BEGIN
            
            open prod_cur for select id,blank_no from product_template where blank_no = blankid and active=True  ;
            loop
              fetch prod_cur into prod_rec ;
              exit when not found ;
              select id into prodid from product_product where product_tmpl_id = prod_rec.id ;
              return next prodid ;
            end loop ;
            close prod_cur ;
            
          END;$BODY$
          LANGUAGE plpgsql;
          """)

        self.env.cr.execute("""drop function if exists genblankengorder(prodtmplid int) cascade""")
        self.env.cr.execute("""create or replace function genblankengorder(prodtmplid int) returns void as $BODY$
          DECLARE
            eng_cur refcursor ;
            eng_rec record ;
            ins_cur refcursor ;
            ins_rec record ;
            ncount int ;
            blankid int ;
            blanktmplid int ;
          BEGIN
            select blank_no into blankid from product_template where id = prodtmplid ;
            select product_tmpl_id into blanktmplid from product_product where id = blankid ;
            if prodtmplid != blanktmplid then
                open eng_cur for select * from alldo_gh_iot_eng_order where prod_id = prodtmplid ;
                loop
                  fetch eng_cur into eng_rec ;
                  exit when not found ;
                  select count(*) into ncount from alldo_gh_iot_eng_order where prod_id=blanktmplid and eng_order=eng_rec.eng_order ;
                  if ncount = 0 then
                     insert into alldo_gh_iot_eng_order(sequence,prod_id,eng_type,is_outsourcing,partner_id,eng_order,cnc_prog,clamping_power,standard_num,mold_cavity)
                        values (eng_rec.sequence,blanktmplid,eng_rec.eng_type,coalesce(eng_rec.is_outsourcing,False),eng_rec.partner_id,eng_rec.eng_order,
                        coalesce(eng_rec.cnc_prog,' '),coalesce(eng_rec.clamping_power,' '),coalesce(eng_rec.standard_num,0),coalesce(eng_rec.mold_cavity,1)) ;
                  end if ;
                end loop ;
                close eng_cur ;
                open ins_cur for select * from alldo_gh_iot_workorder_inspect where product_id = prodtmplid ;
                loop
                  fetch ins_cur into ins_rec ;
                  exit when not found ;
                  select count(*) into ncount from alldo_gh_iot_workorder_inspect where product_id = blanktmplid and inspect_name = ins_rec.inspect_name and eng_type=ins_rec.eng_type;
                  if ncount = 0 then
                     insert into alldo_gh_iot_workorder_inspect(sequence,eng_type,product_id,inspect_name,inspect_size,drawing_tolerance,real_work_size,
                      correct_no,inspect_point,inspect_tool) values (ins_rec.sequence,ins_rec.eng_type,blanktmplid,coalesce(ins_rec.inspect_name,' '),
                      coalesce(ins_rec.inspect_size,' '),coalesce(ins_rec.drawing_tolerance,' '),coalesce(ins_rec.real_work_size,' '),coalesce(ins_rec.correct_no,' '),
                      coalesce(ins_rec.inspect_point,' '),ins_rec.inspect_tool) ;
                  end if ;
                end loop ;
                close ins_cur ;
            end if ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genallblankengorder() cascade""")
        self.env.cr.execute("""create or replace function genallblankengorder() returns void as $BODY$
          DECLARE
            prod_cur refcursor ;
            prod_rec record ;
          BEGIN
            open prod_cur for select id from product_template where blank_no is not null ;
            loop
              fetch prod_cur into prod_rec ;
              exit when not found ;
              execute genblankengorder(prod_rec.id) ;
            end loop ;
            close prod_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genqcinfo() cascade""")
        self.env.cr.execute("""create or replace function genqcinfo() returns void as $BODY$
          DECLARE
            qc_cur refcursor ;
            qc_rec record ;
            mycusnameno int ;
            myproductno int ;
          BEGIN
            open qc_cur for select * from alldo_gh_iot_workorder_qc ;
            loop
               fetch qc_cur into qc_rec ;
               exit when not found ;
               select product_no,cus_name into myproductno,mycusnameno from alldo_gh_iot_workorder where id = qc_rec.order_id ;
               update alldo_gh_iot_workorder_qc set product_no=myproductno,cus_name=mycusnameno where id = qc_rec.id ;
            end loop ;
            close qc_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists gennewqcngno(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gennewqcngno(partnerid int) returns void as $BODY$
          DECLARE
           have_new Boolean ;
           mynowdate date ;
           myyear varchar ;
           mymonth varchar ;
           myday varchar ;
           numbernext int ;
           numbernext1 varchar ;
           myid int ;
           myngno varchar ;
          BEGIN
           select ckngreturn(partnerid) into have_new ;
           if have_new = True then   /* 有NG退料單 */
              select current_timestamp::DATE into mynowdate ;
              select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
              select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
              select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
              select id,number_next into myid,numbernext from ir_sequence where code='alldo_gh_iot.return_ng' ;
              numbernext1 = numbernext::TEXT ;
              myngno = concat('R',myyear,mymonth,myday,lpad(numbernext1,2,'0')) ;
              update alldo_gh_iot_workorder_qc set report_no=myngno where (report_no is null or report_no='') 
                 and (material_ng_num > 0 or processing_ng_num > 0 or loss_num > 0) ;
              update ir_sequence set number_next=number_next+1 where id = myid ;
           end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getblankonhand(blanknoid int) cascade""")
        self.env.cr.execute("""create or replace function getblankonhand(blanknoid int) returns Float as $BODY$
          DECLARE
            myres float ;
            blankloc int ;
          BEGIN
            select min(blank_loc) into blankloc from alldo_gh_iot_company_stockloc ;
            select sum(quantity) into myres from stock_quant where company_id=1 and location_id=blankloc and product_id=blanknoid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodonhand(prodid int) returns Float as $BODY$
          DECLARE
            myres float ;
            prodloc int ;
          BEGIN
            select min(prod_loc) into prodloc from alldo_gh_iot_company_stockloc ;
            select sum(quantity) into myres from stock_quant where company_id=1 and location_id=prodloc and product_id=prodid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getsemiprodonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getsemiprodonhand(prodid int) returns Float as $BODY$
          DECLARE
            myres float ;
            semiprodloc int ;
          BEGIN
            select min(semi_prod_loc) into semiprodloc from alldo_gh_iot_company_stockloc ;
            select sum(quantity) into myres from stock_quant where company_id=1 and location_id=semiprodloc and product_id=prodid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpdbkonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpdbkonhand(prodid int) returns float as $BODY$
          DECLARE
            myres float ;
            prodtmplid int ;
            blankno int ;
            blankloc int ;
          BEGIN
            select product_tmpl_id into prodtmplid from product_product where id = prodid ;
            select blank_no into blankno from product_template where id = prodtmplid ;
            if blankno is null then
               blankno = prodid ;
            end if ;
            select min(blank_loc) into blankloc from alldo_gh_iot_company_stockloc ;
            select sum(quantity) into myres from stock_quant where company_id=1 and location_id=blankloc and product_id=blankno ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpdonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpdonhand(prodid int) returns float as $BODY$
         DECLARE
           myres float ;
           prodtmplid int ;
           prodloc int ;
         BEGIN
           select min(prod_loc) into prodloc from alldo_gh_iot_company_stockloc ;
           select sum(quantity) into myres from stock_quant where company_id=1 and location_id=prodloc and product_id=prodid ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpartnerbkonhand(partnerlocid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpartnerbkonhand(partnerlocid int,prodid int) returns float as $BODY$
          DECLARE
             myres float ;
          BEGIN
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=partnerlocid and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpartnerprodonhand(partnerlocid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpartnerprodonhand(partnerlocid int,prodid int) returns float as $BODY$
          DECLARE
             myres float ;
          BEGIN
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=partnerlocid and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpartnersemiprodonhand(partnerlocid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpartnersemiprodonhand(partnerlocid int,prodid int) returns float as $BODY$
          DECLARE
             myres float ;
          BEGIN
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=partnerlocid and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwhbkonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getwhbkonhand(prodid int) returns float as $BODY$
          DECLARE
             myres float ;
             blankloc int ;
          BEGIN
             select min(blank_loc) into blankloc from alldo_gh_iot_company_stockloc ;
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=blankloc and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwhprodonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getwhprodonhand(prodid int) returns float as $BODY$
          DECLARE
             myres float ;
             prodloc int ;
          BEGIN
             select min(prod_loc) into prodloc from alldo_gh_iot_company_stockloc ;
             select sum(coalesce(quantity,0)) into myres from stock_quant where company_id=1 and location_id=prodloc and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getwhsemiprodonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getwhsemiprodonhand(prodid int) returns float as $BODY$
          DECLARE
             myres float ;
             semiprodloc int ;
          BEGIN
             select min(semi_prod_loc) into semiprodloc from alldo_gh_iot_company_stockloc ;
             select sum(coalesce(quantity,0)) into myres from stock_quant where company_id=1 and location_id=semiprodloc and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewshippingno(pickingid int) cascade""")
        self.env.cr.execute("""create or replace function gennewshippingno(pickingid int) returns varchar as $BODY$
          DECLARE
           have_new Boolean ;
           mynowdate date ;
           myyear varchar ;
           mymonth varchar ;
           myday varchar ;
           numbernext int ;
           numbernext1 varchar ;
           myid int ;
           myshippingno varchar ;
           reportno varchar ;
           myres varchar ;
           ncount int ;
           mycurrenttime timestamp ;
           mypartnerid int ;
          BEGIN
           select coalesce(report_no,' '),partner_id into reportno,mypartnerid from stock_picking where id = pickingid ; 
           if reportno = ' ' then   /* 要產出新單號 */
              select current_timestamp::timestamp + interval '2 hours' into mycurrenttime ;
              select (current_timestamp::timestamp + interval '2 hours')::DATE into mynowdate ;
              select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
              select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
              select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
              select count(*) into ncount from ir_sequence where code='alldo_gh_iot.shipping' and write_date::DATE = mynowdate ;
              if ncount > 0 then
                 select id,number_next into myid,numbernext from ir_sequence where code='alldo_gh_iot.shipping' and write_date::DATE = mynowdate ;
                 update ir_sequence set number_next=number_next+1,write_date=mycurrenttime where id = myid ;
              else
                 select id into myid from ir_sequence where code='alldo_gh_iot.shipping' ;
                 numbernext = 1 ;
                 update ir_sequence set number_next=2,write_date=mycurrenttime where id = myid ;
              end if ;   
              numbernext1 = numbernext::TEXT ;
              myshippingno = concat('S',myyear,mymonth,myday,lpad(numbernext1,3,'0')) ;
              myres = myshippingno ;
              update stock_picking set report_no=myshippingno,date_done=mynowdate where (report_no is null or report_no='') and partner_id=mypartnerid and state='done' and picking_type_id=2 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewoutsourcingno(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gennewoutsourcingno(partnerid int) returns void as $BODY$
          DECLARE
           have_new Boolean ;
           mynowdate date ;
           myyear varchar ;
           mymonth varchar ;
           myday varchar ;
           numbernext int ;
           numbernext1 varchar ;
           myid int ;
           myoutsourcingno varchar ;
           reportno varchar ;
           ncount int ;
          BEGIN
           select count(*) into ncount from alldo_gh_iot_partner_prodout where partner_id = partnerid and report_no is null ;
           if ncount > 0 then   /* 要產出新單號 */
              select current_timestamp::DATE into mynowdate ;
              select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
              select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
              select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
              select id,number_next into myid,numbernext from ir_sequence where code='alldo_gh_iot.outsourcing_out' ;
              numbernext1 = numbernext::TEXT ;
              myoutsourcingno = concat('O',myyear,mymonth,myday,lpad(numbernext1,2,'0')) ;
              update alldo_gh_iot_partner_prodout set report_no=myoutsourcingno where (report_no is null or report_no='') and partner_id = partnerid  ;
              update ir_sequence set number_next=number_next+1 where id = myid ;
           end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodsupplier(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodsupplier(prodid int) returns setof INT as $BODY$
          DECLARE
            out_cur refcursor ;
            out_rec record ;
          BEGIN
            open out_cur for select distinct partner_id from alldo_gh_iot_partner_prodout where product_no=prodid ;
            loop
              fetch out_cur into out_rec ;
              exit when not found ;
              return next out_rec.partner_id ;
            end loop ;
            close out_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatenotclosemo(moid int,partnerlocid int) cascade;""")
        self.env.cr.execute("""create or replace function updatenotclosemo(moid int,partnerlocid int) returns void as $BODY$
          DECLARE
            notclose Boolean ;
            blankid int ;
            blanknum Float;
          BEGIN
            select not_close,blank_no into notclose,blankid from alldo_gh_iot_workorder where id = moid ;
            select sum(quantity) into blanknum from stock_quant where company_id=1 and location_id=partnerlocid and product_id=blankid ;
            if notclose=True then
               update alldo_gh_iot_workorder set blank_num=blanknum where id = moid ;
            end if ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists alloutsourcingstockin(moid int,ngnum float,lossnum float) cascade""")
        self.env.cr.execute("""drop function if exists alloutsourcingstockin(moid int,prodnum float,ngnum float,lossnum float) cascade""")
        self.env.cr.execute("""create or replace function alloutsourcingstockin(moid int,prodnum float,ngnum float,lossnum float) returns void as $BODY$
          DECLARE
            motype char ;
            mynowdate date ;
            totnum float ;
          BEGIN
            totnum = prodnum + ngnum + lossnum ;
            select current_timestamp::DATE into mynowdate ;
            select state into motype from alldo_gh_iot_workorder where id = moid ;
            if motype = '5' then   /* 全委外 */
               if ngnum > 0 or lossnum > 0 then 
                  insert into alldo_gh_iot_workorder_qc (order_id,qc_date,total_amount_num,processing_ng_num,loss_num,line_memo) values
                     (moid,mynowdate,totnum,ngnum,lossnum,'託工NG回廠') ;
               else
                  insert into alldo_gh_iot_workorder_qc (order_id,qc_date,total_amount_num,processing_ng_num,loss_num,line_memo) values
                     (moid,mynowdate,totnum,ngnum,lossnum,'託工回廠') ;   
               end if ;      
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genngreturnselectitem(mytype char,partnerid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genngreturnselectitem(mytype char,partnerid int,startdate date,enddate date) returns void as $BODY$
          DECLARE
            ng_cur refcursor ;
            ng_rec record ;
            reportno varchar ;
            mynowdate date ;
            mymaxid int ;
            linememo varchar ;
          BEGIN
            select current_timestamp::DATE into mynowdate ;
            delete from alldo_gh_iot_ngreturn_selectitem ;
            delete from alldo_gh_iot_ngreturn_select ;
            insert into alldo_gh_iot_ngreturn_select(report_date,partner_id) values (mynowdate,partnerid) ;
            select max(id) into mymaxid from alldo_gh_iot_ngreturn_select ;
           /* if mytype='1' then
               open ng_cur for select * from alldo_gh_iot_ngreturn_view where report_no is null and cus_name = partnerid and 
                 qc_date::DATE between startdate::DATE and enddate::DATE order by qc_date DESC ; 
            else
               open ng_cur for select * from alldo_gh_iot_ngreturn_view where report_no is not null and cus_name = partnerid and 
                 qc_date::DATE between startdate::DATE and enddate::DATE order by qc_date DESC ; 
            end if ; */
            open ng_cur for select * from alldo_gh_iot_ngreturn_view where cus_name = partnerid and 
                 qc_date::DATE between startdate::DATE and enddate::DATE order by qc_date DESC ; 
            loop
              fetch ng_cur into ng_rec ;
              exit when not found ;
              if ng_rec.report_no is null then
                 reportno = ' ' ;
              else
                 reportno = ng_rec.report_no ;
              end if ;
              insert into alldo_gh_iot_ngreturn_selectitem(select_id,name,product_no,cus_name,report_no,material_ng_num,processing_ng_num,loss_num,qc_date,line_memo,qcid) values 
               (mymaxid,ng_rec.name,ng_rec.product_no,ng_rec.cus_name,reportno,ng_rec.material_ng_num,ng_rec.processing_ng_num,ng_rec.loss_num,ng_rec.qc_date,coalesce(ng_rec.line_memo,' '),ng_rec.qid) ;
            end loop ;
            close ng_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkorderprocessing(moid int) cascade""")
        self.env.cr.execute("""create or replace function genwkorderprocessing(moid int) returns void as $BODY$
          DECLARE
            wk_cur refcursor ;
            wk_rec record ;
            prodid int ;
            shippingnum float ;
            mymaxid int ;
            cdate date ;
            goodnum float ;
            mngnum float ;
            pngnum float ;
            lossnum float ;
            gnum float ;
          BEGIN
            delete from alldo_gh_iot_processing_view_line ;
            delete from alldo_gh_iot_processing_view ;
            select product_no,coalesce(shipping_num,0) into prodid,shippingnum from alldo_gh_iot_workorder where id = moid ;
            insert into alldo_gh_iot_processing_view(mo_no,product_no,shipping_num) values (moid,prodid,shippingnum) ;
            select max(id) into mymaxid from alldo_gh_iot_processing_view ;
            goodnum = 0 ;
            gnum = 0 ;
            mngnum = 0 ;
            pngnum = 0 ;
            lossnum = 0 ;
            open wk_cur for select * from alldo_gh_iot_workorder_qc where order_id=moid ;
            loop
              fetch wk_cur into wk_rec ;
              exit when not found ;
              cdate = wk_rec.create_date ;
              gnum = coalesce(wk_rec.total_amount_num,0) - coalesce(wk_rec.material_ng_num,0) - coalesce(wk_rec.processing_ng_num,0) - coalesce(wk_rec.loss_num,0) ;
              goodnum = goodnum + coalesce(gnum,0) ;
              mngnum = mngnum + coalesce(wk_rec.material_ng_num,0) ;
              pngnum = pngnum + coalesce(wk_rec.processing_ng_num,0) ;
              lossnum = lossnum + coalesce(wk_rec.loss_num,0) ;
              insert into alldo_gh_iot_processing_view_line(processing_id,qc_date,qc_good_num,material_ng_num,processing_ng_num,loss_num,iot_owner1)
                values (mymaxid,coalesce(wk_rec.qc_date,cdate),gnum,wk_rec.material_ng_num,wk_rec.processing_ng_num,wk_rec.loss_num,wk_rec.iot_owner1) ;
            end loop ;
            close wk_cur ;
            update alldo_gh_iot_processing_view set good_num=goodnum,material_ng_num=mngnum,processing_ng_num=pngnum,loss_num=lossnum where id = mymaxid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists resetbells() cascade""")
        self.env.cr.execute("""create or replace function resetbells() returns void as $BODY$
          DECLARE
            bell_cur refcursor ;
            bell_rec record ;
            mynowdate date ;
            mycurrenttime timestamp ;
            myhms varchar ;
            mycdate varchar ;
            mydatetime timestamp ;
          BEGIN
            select current_timestamp into mycurrenttime ;
            select current_timestamp::DATE into mynowdate ;
            open bell_cur for select * from alldo_gh_iot_bells_line ;
            loop
              fetch bell_cur into bell_rec ;
              exit when not found ;
              mycdate = concat(mynowdate::DATE::TEXT,' ',bell_rec.bells_time) ;
              mydatetime  = mycdate::timestamp - interval '8 hours' ;
              if mydatetime < mycurrenttime then
                 mycdate = concat((mynowdate + interval '1 days')::DATE::TEXT,' ',bell_rec.bells_time) ;
                 mydatetime  = mycdate::timestamp - interval '8 hours' ; 
                 update alldo_gh_iot_bells_line set next_run_bells= mydatetime where id = bell_rec.id ;
              else
                 update alldo_gh_iot_bells_line set next_run_bells= mydatetime where id = bell_rec.id ;
              end if ;
            end loop ;
            close bell_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genbells() cascade""")
        self.env.cr.execute("""create or replace function genbells() returns varchar as $BODY$
          DECLARE
            mycurrenttime timestamp ;
            mycurrenttime1 timestamp ;
            mynextbelltime timestamp ;
            myid int ;
            myres varchar ;
            ncount int ;
            bells_cur refcursor ;
            bells_rec record ;
          BEGIN
            select current_timestamp::timestamp into mycurrenttime ;
            select current_timestamp::timestamp + interval '30 seconds' into mycurrenttime1 ; 
            /* select count(*) into ncount from alldo_gh_iot_bells_line where next_run_bells between mycurrenttime and mycurrenttime1 ; */
            select count(*) into ncount from alldo_gh_iot_bells_line where next_run_bells::timestamp < mycurrenttime1::timestamp ;
            if ncount > 0 then
               /* select id into myid from alldo_gh_iot_bells_line where next_run_bells between mycurrenttime and mycurrenttime1 ; */
               open bells_cur for select id,next_run_bells from alldo_gh_iot_bells_line where next_run_bells::timestamp < mycurrenttime1::timestamp ;
               loop
                  fetch bells_cur into bells_rec ;
                  exit when not found ;
                  select bells_file_name into myres from alldo_gh_iot_bells_line where id = bells_rec.id ;
                  select next_run_bells into mynextbelltime from alldo_gh_iot_bells_line where id = bells_rec.id ;
                  mynextbelltime = mynextbelltime + interval '1 days' ;
                  update alldo_gh_iot_bells_line set next_run_bells=mynextbelltime where id = bells_rec.id ;
               end loop ;
               close bells_cur ;
            end if ;
            if myres is null then
               myres = 'NO' ;
            end if ;
            return myres ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getgroupmo(mywkid int) cascade""")
        self.env.cr.execute("""create or replace function getgroupmo(mywkid int) returns setof INT as $BODY$
          DECLARE
            mo_cur refcursor ;
            mo_rec record ;
            mogid int ;
          BEGIN
            select mo_group_id into mogid from alldo_gh_iot_workorder where id = mywkid ;
            open mo_cur for select id from alldo_gh_iot_workorder 
               where mo_group_id = mogid and eng_order != '4' order by id ;
            loop
              fetch mo_cur into mo_rec ;
              exit when not found ;
              return next mo_rec.id ;
            end loop ;
            close mo_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkequipment(startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genwkequipment(startdate date,enddate date) returns void as $BODY$
          DECLARE
            equ_cur refcursor ;
            equ_rec record ;
            iotdur float ;
            iotdurh float ;
            iotdurmin float ;
            iotdurh1 float ;
          BEGIN
            delete from alldo_gh_iot_equipment_performance_list ;
            open equ_cur for select id from maintenance_equipment ;
            loop
              fetch equ_cur into equ_rec ;
              exit when not found ; 
              iotdur = 0 ;
              iotdurmin = 0 ;
              iotdurh1 = 0 ;
              select sum(coalesce(iot_duration,0)) into iotdur from alldo_gh_iot_workorder_iot_data where iot_node = equ_rec.id and 
                 iot_date::DATE >= startdate::DATE and iot_date::DATE <= enddate::DATE ;
              select sum(coalesce(replace_duration,0)) into iotdurmin from alldo_gh_iot_wkorder_replaceline where equipment_id=equ_rec.id and 
                 replace_start_datetime::DATE >= startdate::DATE and replace_start_datetime::DATE <= enddate::DATE ;   
              iotdurh1 = round((iotdurmin::numeric/60::numeric),2) ;    
              iotdurh = round((iotdur::numeric/3600::numeric),2) + coalesce(iotdurh1,0) ;
              insert into alldo_gh_iot_equipment_performance_list(equip_no,equipment_duration) values (equ_rec.id,iotdurh) ;
            end loop ;
            close equ_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkmanperformance(startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genwkmanperformance(startdate date,enddate date) returns void as $BODY$
             DECLARE
               man_cur refcursor ;
               man_rec record ;
               temp_cur refcursor ;
               temp_rec record ;
               perf_rate float ;
               amounttot float ;
               numtot float ;
               avgtot float ;
             BEGIN
               delete from alldo_gh_iot_man_performance_list ;
               delete from alldo_gh_iot_man_performance_temp ;
               execute genwkperformance(startdate,enddate,0,'0',0,0) ;
               open temp_cur for select iot_owner,performance_rate,total_amount_num from alldo_gh_iot_workorder_performance_list1 where performance_rate > 0 ;
              /* open temp_cur for select id,iot_owner1,qc_date from alldo_gh_iot_workorder_qc where qc_date::DATE between startdate::DATE and enddate::DATE ; */
               loop
                 fetch temp_cur into temp_rec ;
                 exit when not found ;
                 /* select getperformance(temp_rec.id) into perf_rate ; */
                 insert into alldo_gh_iot_man_performance_temp(prod_owner,prod_performance,prod_num) values (temp_rec.iot_owner,temp_rec.performance_rate,temp_rec.total_amount_num) ;
               end loop ;
               close temp_cur ;
              open man_cur for select distinct iot_owner from alldo_gh_iot_workorder_performance_list1 ;
               loop
                 fetch man_cur into man_rec ;
                 exit when not found ;
                 insert into  alldo_gh_iot_man_performance_list(prod_owner) values (man_rec.iot_owner) ;    
               end loop ;
               close man_cur ;
               open man_cur for select * from alldo_gh_iot_man_performance_list ;
               loop
                  fetch man_cur into man_rec ;
                  exit when not found ;
                  select round(avg(T.prod_performance)::numeric,2) into avgtot from alldo_gh_iot_man_performance_temp T where T.prod_owner=man_rec.prod_owner and T.prod_performance > 0 and T.prod_num > 30 ; 
                  /* select sum(coalesce(T.prod_performance,0) * coalesce(T.prod_num,0)) into amounttot from alldo_gh_iot_man_performance_temp T where T.prod_owner=man_rec.prod_owner ;
                  select sum(coalesce(T.prod_num,0)) into numtot from alldo_gh_iot_man_performance_temp T where T.prod_owner=man_rec.prod_owner ;
                  if numtot = 0 or numtot is null then
                     avgtot = 0 ;
                  else
                     avgtot = round((amounttot::numeric/numtot::numeric),2) ;
                  end if ;*/
                  update alldo_gh_iot_man_performance_list set prod_performance=avgtot where id = man_rec.id ;
               end loop ;
               close man_cur ;
               delete from alldo_gh_iot_man_performance_list where prod_performance = 0 or prod_owner is null or prod_performance is null ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmoid(mogid int) cascade""")
        self._cr.execute("""drop function if exists getmoid(repno varchar) cascade""")
        self._cr.execute("""drop function if exists getmoid(repno varchar,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getmoid(repno varchar,prodid int) returns int as $BODY$
          DECLARE
            pickid int ;
            myres int ;
          BEGIN
            select max(id) into pickid from stock_picking where report_no=repno and id in (select picking_id from stock_move where product_id=prodid) ;
            select id into myres from alldo_gh_iot_workorder where prodout_picking=pickid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpono1(mogid int) cascade""")
        self.env.cr.execute("""create or replace function getpono1(mogid int) returns int as $BODY$
          DECLARE
            myres int ;
          BEGIN
            if mogid is null then
               myres = null ;
            else
               select po_no1 into myres from alldo_gh_iot_workorder where mo_group_id=mogid ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpono(mogid int) cascade""")
        self.env.cr.execute("""create or replace function getpono(mogid int) returns varchar as $BODY$
          DECLARE
            po_cur refcursor ;
            po_rec record ;
            pono varchar ;
            maxid int ;
            myres varchar ;
            powkid int ;
          BEGIN 
            if mogid is null then
               myres = '' ;
            else
               select max(id) into maxid from alldo_gh_iot_workorder where mo_group_id=mogid ;
               open po_cur for select * from powkorder_iotwkorder_rel where wk_id=maxid ;
               loop
                 fetch po_cur into po_rec ;
                 exit when not found ;
                 select po_no into pono from alldo_gh_iot_po_wkorder where id = po_rec.po_id ;
                 if myres ='' then
                    myres = pono ;
                 else
                    myres = concat(myres,'/',pono) ;
                 end if ;
               end loop ;
               close po_cur ;
            end if ;
            if myres is null then
               myres = ' ' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpoloc(mogid int) cascade""")
        self.env.cr.execute("""create or replace function getpoloc(mogid int) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            powkid int ;
          BEGIN 
            if mogid is null then
               myres = ' ' ;
            else
               select po_no1 into powkid from alldo_gh_iot_workorder where mo_group_id=mogid ;
               select po_location into myres from alldo_gh_iot_po_wkorder where id = powkid ;
            end if ;
            if myres is null then
               myres = ' ' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcussystem(mogid int) cascade""")
        self.env.cr.execute("""create or replace function getcussystem(mogid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            powkid int ;
          BEGIN 
            if mogid is null then
               myres = False ;
            else
               select po_no1 into powkid from alldo_gh_iot_workorder where mo_group_id=mogid ;
               select custom_system into myres from alldo_gh_iot_po_wkorder where id = powkid ;
            end if ;
            if myres is null then
               myres = False ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpono2(mvid int,prodid int) cascade""")
        self._cr.execute("""drop function if exists getpono2(mvlid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getpono2(mvlid int,prodid int) returns varchar as $BODY$
         DECLARE
           powk_cur refcursor ;
           powk_rec record ;
           pono varchar ;
           myres varchar ;
           ncount int ;
         BEGIN
           /*select max(id) into mvlid from stock_move_line where move_id=mvid  ;*/
           open powk_cur for select * from ghiot_moveline_powk_rel where move_id=mvlid ;
           loop
             fetch powk_cur into powk_rec ;
             exit when not found ;
             select count(*) into ncount from alldo_gh_iot_po_wkorder where id=powk_rec.po_id and product_no=prodid ;
             if ncount > 0 then
                 select po_no into pono from alldo_gh_iot_po_wkorder where id=powk_rec.po_id  ;
                 if myres=null then
                    myres = pono ;
                 else
                    myres = concat(myres,'/',pono) ;
                 end if ;
             end if ;    
           end loop ;
           close powk_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # self.env.cr.execute("""drop view if exists ghiot_stockmovelist""")
        # self.env.cr.execute("""CREATE OR REPLACE VIEW ghiot_stockmovelist AS
        #     select A.id,A.date,A.product_id,A.product_qty,A.product_uom,A.state,A.picking_id,B.origin,A.reference,B.partner_id,A.picking_type_id,B.mo_group_id,(select getpono1(B.mo_group_id) as po_no1),(select getmoid(B.report_no,A.product_id) as moid),
        #         (select getpono2(A.id,A.product_id) as po_no),(select getpoloc(B.mo_group_id) as po_location),(select getcussystem(B.mo_group_id) as custom_system),B.report_no from stock_move A left join stock_picking B on A.picking_id = B.id
        #           where A.picking_type_id in (1,2) and A.state='done' and (B.location_id=5 or B.location_id=8 or B.location_dest_id=5 or B.location_dest_id=8)""")

        self.env.cr.execute("""drop view if exists ghiot_stockmovelist""")
        self.env.cr.execute("""CREATE OR REPLACE VIEW ghiot_stockmovelist AS
            select C.id,C.date,C.product_id,C.qty_done,A.product_uom,A.state,A.picking_id,B.origin,A.reference,B.partner_id,A.picking_type_id,B.mo_group_id,(select getpono1(B.mo_group_id) as po_no1),(select getmoid(B.report_no,A.product_id) as moid),
                (select getpono2(C.id,C.product_id) as po_no),(select getpoloc(B.mo_group_id) as po_location),(select getcussystem(B.mo_group_id) as custom_system),B.report_no from stock_move_line C left join stock_move A on C.move_id=A.id and C.product_id=A.product_id left join stock_picking B on A.picking_id = B.id
                  where A.picking_type_id in (1,2) and A.state='done' and (B.location_id=5 or B.location_id=8 or B.location_dest_id=5 or B.location_dest_id=8)""")


        self.env.cr.execute("""drop function if exists genstockmovemixsearch(startdate date,enddate date,partnerid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function genstockmovemixsearch(startdate date,enddate date,partnerid int,prodid int) returns void as $BODY$
          DECLARE
            mv_cur refcursor ;
            mv_rec record ;
            mypartnerid int ;
            myprodid int ;
            ncount int ;
            totqty float ;
            nitem int ;
            ncount1 int ;
            ncount2 int ;
            pono varchar ;
            pono1 varchar ;
            po_cur refcursor ;
            po_rec record ;
          BEGIN
            delete from alldo_gh_iot_stock_move_list ;
            mypartnerid = 0 ;
            myprodid = 0 ;
            ncount = 0 ;
            totqty = 0 ;
            nitem = 0 ;
            if partnerid = 0 then
               open mv_cur for select * from ghiot_stockmovelist where (date::DATE between startdate::DATE and enddate::DATE)  and product_id=prodid 
                  order by partner_id,product_id ;
            elsif prodid = 0 then
               open mv_cur for select * from ghiot_stockmovelist where (date::DATE between startdate::DATE and enddate::DATE) and  partner_id=partnerid 
                   order by product_id ;
            else
               open mv_cur for select * from ghiot_stockmovelist where  (date::DATE between startdate::DATE and enddate::DATE) and  partner_id=partnerid
                  and product_id=prodid  order by product_id;
            end if ;
            loop
              fetch mv_cur into mv_rec ;
              exit when not found ;
              if mv_rec.product_id = myprodid then
                 nitem = nitem + 1 ;
              end if ;   
              ncount = ncount + 1 ;
              /* if mv_rec.mo_group_id is not null then
                select count(*) into ncount from alldo_gh_iot_stock_move_list where mo_group_id=mv_rec.mo_group_id ;
                 if ncount = 0 then */
                if mv_rec.picking_type_id=1 and mv_rec.origin like '%退回%' then
                   select count(*) into ncount2 from alldo_gh_iot_stock_move_list where origin=mv_rec.reference ;
                   if ncount2 = 0 then
                       insert into alldo_gh_iot_stock_move_list(date,product_id,product_qty,product_uom,partner_id,origin,po_no,po_location,custom_system,mo_group_id,report_no,mo_no) values
                         (mv_rec.date,mv_rec.product_id,(mv_rec.qty_done * -1),mv_rec.product_uom,mv_rec.partner_id,concat(mv_rec.reference,' (',mv_rec.origin,')'),mv_rec.po_no,coalesce(mv_rec.po_location,' '),mv_rec.custom_system,mv_rec.mo_group_id,coalesce(mv_rec.report_no,' '),mv_rec.moid) ;
                   end if ;  
                elsif mv_rec.picking_type_id=2 then
                    select count(*) into ncount2 from alldo_gh_iot_stock_move_list where origin=mv_rec.reference ;
                    if ncount2 = 0 then
                       insert into alldo_gh_iot_stock_move_list(date,product_id,product_qty,product_uom,partner_id,origin,po_no,po_location,custom_system,mo_group_id,report_no,mo_no) values
                         (mv_rec.date,mv_rec.product_id,mv_rec.qty_done,mv_rec.product_uom,mv_rec.partner_id,mv_rec.reference,mv_rec.po_no,coalesce(mv_rec.po_location,' '),mv_rec.custom_system,mv_rec.mo_group_id,coalesce(mv_rec.report_no,' '),mv_rec.moid) ;
                    end if ; 
                end if ;
                /* else
                   update alldo_gh_iot_stock_move_list set product_qty=coalesce(product_qty,0)+coalesce(mv_rec.product_qty,0) where mo_group_id=mv_rec.mo_group_id ;
                 end if ; 
              else
                 select count(*) into ncount from alldo_gh_iot_stock_move_list where partner_id=mv_rec.partner_id and product_id=mv_rec.product_id ;
                 if ncount = 0 then
                    insert into alldo_gh_iot_stock_move_list(date,product_id,product_qty,product_uom,partner_id,origin,po_no,po_location,custom_system,mo_group_id,report_no) values
                   (mv_rec.date,mv_rec.product_id,mv_rec.product_qty,mv_rec.product_uom,mv_rec.partner_id,mv_rec.origin,coalesce(mv_rec.po_no,' '),coalesce(mv_rec.po_location,' '),mv_rec.custom_system,mv_rec.mo_group_id,coalesce(mv_rec.report_no,' ')) ;
                 else
                   update alldo_gh_iot_stock_move_list set product_qty=coalesce(product_qty,0)+coalesce(mv_rec.product_qty,0) where partner_id=mv_rec.partner_id and product_id=mv_rec.product_id ;
                 end if ;
              end if ; */
            end loop ;
            close mv_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genzeroiotduration() cascade""")
        self.env.cr.execute("""create or replace function genzeroiotduration() returns void as $BODY$
          DECLARE
             iotdursecond int ;
             iotdurmin int ;
             iotdurhour int ;
             iotdurday int ;
             iotdurmin1 int ;
             wk_cur refcursor ;
             wk_rec record ;
             iot_cur refcursor ;
             iot_rec record ;
             mylastworktime timestamp ;
             mynowdatetime timestamp ;
             iotduration int ;
          BEGIN
             open wk_cur for select id from alldo_gh_iot_workorder ;
             loop
                fetch wk_cur into wk_rec ;
                exit when not found ;
                open iot_cur for select * from alldo_gh_iot_workorder_iot_data where order_id = wk_rec.id order by iot_date asc;
                loop
                   fetch iot_cur into iot_rec ;
                   exit when not found ;
                   if mylastworktime is null then
                      mylastworktime=iot_rec.iot_date ;
                   end if ;
                   mynowdatetime = iot_rec.iot_date ;
                   select round(extract(second from (select age(mynowdatetime,mylastworktime)))::numeric,0) into iotdursecond ;
                   select extract(minute from (select age(mynowdatetime,mylastworktime))) into iotdurmin ;
                   select extract(hours from (select age(mynowdatetime,mylastworktime))) into iotdurhour ;  
                   select extract(days from (select age(mynowdatetime,mylastworktime))) into iotdurday ;
                   iotdurmin1 = iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60) ;
                   iotduration = iotdurmin1 * 60 + iotdursecond ;
                   if iotduration < 3600 then
                      update alldo_gh_iot_workorder_iot_data set iot_duration = iotduration where id = iot_rec.id  ;
                   else
                      update alldo_gh_iot_workorder_iot_data set iot_duration = 0 where id = iot_rec.id  ;   
                   end if ;   
                   mylastworktime=iot_rec.iot_date ;
                end loop ;
                close iot_cur ;
             end loop ;
             close wk_cur ;
             update alldo_gh_iot_workorder_iot_data set iot_duration = 0 where iot_duration < 0 ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genmindashboard() cascade""")
        self.env.cr.execute("""create or replace function genmindashboard() returns void as $BODY$
          DECLARE
            ncount INTEGER := 0;
            iot_cur refcursor ;
            iot_rec record ;
            nitem INTEGER := 0;
            iotstatus char ;
            iotstatus1 varchar ;
            ordernum integer ;
            prodnum integer ;
            tprodnum integer ;
            standardnum integer ;
            opentime float ;
            wkorderid int ;
            wkorder varchar ;
            prodid int ;
            prodtmplid int ;
            prodname varchar ;
            engtype varchar ;
            stdminnum int ;
            nodestatus varchar ;
            mynowdate date ;
            mynowdatetime timestamp ;
            mystartdatetime timestamp ;
            opentimeh int ;
            opentimem int ;
            mymaxid int ;
            empid int ;
            empname varchar ;
            ncount1 int ;
            wkorderid1 int ;
            mymaxid1 int ;
            lastduration float ;
            iotdursecond float ;
            iotdurmin float ;
            iotdurhour float ;
            iotdurday float ;
            mylastdatetime timestamp ;
          BEGIN
            select current_timestamp into mynowdatetime ;
            select current_timestamp::DATE into mynowdate ;
            mystartdatetime = (concat(mynowdate::TEXT,' 00:00:00'))::timestamp ;
            open iot_cur for select * from maintenance_equipment order by sequence,id ;
            loop
              fetch iot_cur into iot_rec ;
              exit when not found ;
              if iot_rec.iot_status='1' or iot_rec.iot_status='4' then
                 iotstatus = '3' ;
              elsif iot_rec.iot_status='2' then
                 iotstatus = '1' ;
              else
                 iotstatus = '2' ;
              end if ;   
              /*  判斷是否架機階段  */   
              select max(id) into mymaxid1 from alldo_gh_iot_wkorder_replaceline where equipment_id=iot_rec.id ;            
              select count(*) into ncount1 from alldo_gh_iot_wkorder_replaceline where equipment_id=iot_rec.id and 
                     id = mymaxid1 and replace_end_datetime is null ;
              if ncount1 > 0 and iot_rec.iot_status='4' then
                  select order_id,replace_owner into wkorderid,empid from alldo_gh_iot_wkorder_replaceline where id = mymaxid1 ;
                  select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_gh_iot_workorder where id = wkorderid ; 
                  iotstatus = '2' ;
              else        
                  select iot_workorder into wkorderid from alldo_gh_iot_equipment_iot_data where 
                      id = (select max(id) from alldo_gh_iot_equipment_iot_data where iot_id=iot_rec.id);
                  select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_gh_iot_workorder where id = wkorderid ;   
                  select max(id) into mymaxid from alldo_gh_iot_workorder_iot_data where order_id=wkorderid and iot_node=iot_rec.id ;
                  select iot_owner into empid from alldo_gh_iot_workorder_iot_data where id = mymaxid ; 
                  if iot_rec.iot_status='1' or iot_rec.iot_status='4' then
                     iotstatus = '3' ;
                  else
                     iotstatus = '1' ;
                  end if ;   
              end if ;         
              select sum(iot_num) into prodnum from alldo_gh_iot_equipment_iot_data where iot_id=iot_rec.id and iot_workorder=wkorderid ;
              select max(id) into mymaxid from alldo_gh_iot_workorder_lastwork where equipment_id = iot_rec.id and workorder_id = wkorderid ;
              if mymaxid is not null then
                 select work_datetime into mylastdatetime from alldo_gh_iot_workorder_lastwork where id = mymaxid ;
                 select round(extract(second from (select age(mynowdatetime,mylastdatetime)))::numeric,0) into iotdursecond ;
                 select extract(minute from (select age(mynowdatetime,mylastdatetime))) into iotdurmin ;
                 select extract(hours from (select age(mynowdatetime,mylastdatetime))) into iotdurhour ;  
                 select extract(days from (select age(mynowdatetime,mylastdatetime))) into iotdurday ;
                 lastduration = iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60) ;
              else
                 lastduration = 0 ;
              end if ;   
              select count(*) into ncount from alldo_gh_iot_dashboard where equipment_no=iot_rec.id ;
              if iotstatus = '1' then
                 iotstatus1 = '生產中' ;
              elsif iotstatus = '2' then
                 iotstatus1 = '換線中' ;
              else
                 iotstatus1 = '準備中' ;
              end if ;      
              if ncount = 0 then
                 insert into alldo_gh_iot_dashboard(equipment_no,iot_status1,wkorder_no,order_num,prod_num,product_id,eng_type,emp_no,last_duration) values
                  (iot_rec.id,iotstatus1,wkorderid,ordernum,prodnum,prodid,engtype,empid,lastduration) ;
              else
                 update alldo_gh_iot_dashboard set iot_status1=iotstatus1,wkorder_no=wkorderid,order_num=ordernum,prod_num=prodnum,product_id=prodid,eng_type=engtype,
                    emp_no=empid,last_duration=lastduration where id = iot_rec.id ;
              end if ;
            end loop ;
            close iot_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists processwkorderng(wkid int) cascade""")
        self.env.cr.execute("""create or replace function processwkorderng(wkid int) returns void as $BODY$
          DECLARE
            mogroupid int ;
            totnum float ;
            totngnum float ;
            totout float ;
            totin float ;
            oldngnum float ;
            ngcomplete Boolean ;
            nowngnum float ;
            engseq int ;
            currentngnum float ;
            blanknum float ;
            maxoutid int ;
            maxinid int ;
            wknextid int ;
          BEGIN
             select sum(coalesce(in_good_num,0)) into blanknum from alldo_gh_iot_wkorder_prodin where order_id = wkid ;
             update alldo_gh_iot_workorder set blank_num = coalesce(blanknum,0) where id = wkid ;
             select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)+coalesce(loss_num,0)),sum(coalesce(total_amount_num,0)) into totngnum,totnum from alldo_gh_iot_workorder_qc
                    where order_id=wkid ;
             totnum = totnum - totngnum ;       
             select sum(coalesce(out_good_num,0)) into totout from alldo_gh_iot_wkorder_prodout where order_id = wkid ;    
             if totnum != totout then
                 select max(id) into maxoutid from alldo_gh_iot_wkorder_prodout where order_id = wkid ;
                 update alldo_gh_iot_wkorder_prodout set out_good_num=coalesce(out_good_num,0) - (totout - totnum) where id = maxoutid ;
                 select mo_group_id,eng_seq into mogroupid,engseq from alldo_gh_iot_workorder where id = wkid ;
                 select id into wknextid from alldo_gh_iot_workorder where mo_group_id=mogroupid and eng_seq=(engseq + 1) ;
                 if wknextid is not null then
                    select sum(coalesce(in_good_num,0)) into totin from alldo_gh_iot_wkorder_prodin where order_id = wknextid ;
                    if totnum != totin then
                       select max(id) into maxinid from alldo_gh_iot_wkorder_prodin where order_id = wknextid ; 
                       update alldo_gh_iot_wkorder_prodin set in_good_num=coalesce(in_good_num,0) - (totin - totnum) where id = maxinid ; 
                       select sum(coalesce(in_good_num,0)) into totin from alldo_gh_iot_wkorder_prodin where order_id = wknextid ;
                       update alldo_gh_iot_workorder set blank_num=totin where id = wknextid ;
                    end if ;
                 end if ;
             end if ;      
             
          END;$BODY$
          LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists iotresettime() cascade""")
        self.env.cr.execute("""create or replace function iotresettime() returns void as $BODY$
          DECLARE
            mynowdate date ;
            mynextdate date ;
            mycurrenttime timestamp ;
            mynextrestarttime timestamp ;
            myhms varchar ;
            mycdate varchar ;
            mycdate1 varchar ;
            mydatetime timestamp ;
            restartfreq int ;
          BEGIN
            select current_timestamp into mycurrenttime ;
            select current_timestamp::DATE into mynowdate ;
            select restart_time,restart_freq,next_run_restart into mycdate1,restartfreq,mynextrestarttime from alldo_gh_iot_restartiot_setting;
            /* if restartfreq is not null then
               select (mynowdate::DATE + restartfreq) into mynextdate ;
            else
               mynextdate = mynowdate + interval '1 days' ;   
            end if ;
            mycdate = concat(mynextdate::DATE::TEXT,' ',mycdate1) ;
            mydatetime  = mycdate::timestamp - interval '8 hours' ;
            if mydatetime < mycurrenttime then
                 mycdate = concat(mynextdate::TEXT,' ',mycdate1) ;
                 mydatetime  = mycdate::timestamp - interval '8 hours' ; 
            end if ; */
            mynextrestarttime = mynextrestarttime + '1 days' ;
            update alldo_gh_iot_restartiot_setting set next_run_restart = mynextrestarttime  ;
            
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists geniotrestart() cascade""")
        self.env.cr.execute("""create or replace function geniotrestart() returns varchar as $BODY$
          DECLARE
            mycurrenttime timestamp ;
            mycurrenttime1 timestamp ;
            mynextrestarttime timestamp ;
            myrestartfreq int ;
            mynowdate date ;
            mynextdate date ;
            mycdate varchar ;
            mydatetime timestamp ;
            mycdate1 varchar ;
            myid int ;
            myres varchar ;
            ncount int ;
            bells_cur refcursor ;
            bells_rec record ;
            enablestart boolean ;
          BEGIN
            select current_timestamp::timestamp into mycurrenttime ;
            select current_timestamp::DATE into mynowdate ;
            select current_timestamp::timestamp + interval '30 seconds' into mycurrenttime1 ; 
            select count(*) into ncount from alldo_gh_iot_restartiot_setting where next_run_restart::timestamp < mycurrenttime1::timestamp ;
            if ncount > 0 then
              select next_run_restart,restart_freq,restart_time,enable_start into mynextrestarttime,myrestartfreq,mycdate1,enablestart from alldo_gh_iot_restartiot_setting ;
              /* if myrestartfreq is not null then
                 select (mynextrestarttime::DATE + myrestartfreq) into mynextdate ;
              else 
                 mynextdate = mynextrestarttime::DATE + interval '1 days' ;
              end if ;  */
              mynextrestarttime = mynextrestarttime::timestamp + '1 days' ; 
             /* mycdate = concat(mynextdate::TEXT,' ',mycdate1) ;
              mydatetime  = mycdate::timestamp - interval '8 hours' ; 
              update alldo_gh_iot_restartiot_setting set next_run_restart=mydatetime ; */
              update alldo_gh_iot_restartiot_setting set next_run_restart=mynextrestarttime ;
              if enablestart is null or enablestart=False then
                 myres = 'NO' ;
              else   
                 myres = 'YES' ;
              end if ;   
            end if ;
            if myres is null then
               myres = 'NO' ;
            end if ;
            return myres ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genprocessngnum() cascade""")
        self.env.cr.execute("""create or replace function genprocessngnum() returns void as $BODY$
          DECLARE
            totngnum float ;
            wk_cur refcursor ;
            wk_rec record ;
          BEGIN
            open wk_cur for select id from alldo_gh_iot_workorder ;
            loop
              fetch wk_cur into wk_rec ;
              exit when not found ;
              select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)+coalesce(loss_num,0)) into totngnum from alldo_gh_iot_workorder_qc
                    where order_id=wk_rec.id  ;
              update alldo_gh_iot_workorder set process_ng_num=totngnum where id = wk_rec.id ;  
            end loop ;
            close wk_cur ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genprodgoodng(startdate date,enddate date,prodid int,nodeid int) cascade""")
        self.env.cr.execute("""create or replace function genprodgoodng(startdate date,enddate date,prodid int,nodeid int) returns void as $BODY$
         DECLARE
           totamount float ;
           goodnum float ;
           ngnum float ;
           mng float ;
           png float ;
           ngratio float ;
           mngratio float ;
           pngratio float ;
           goodratio float ;
           qc_cur refcursor ;
           qc_rec record ;
           prod_cur refcursor ;
           prod_rec record ;
           wk_cur refcursor ;
           wk_rec record ;
         BEGIN
           delete from alldo_gh_iot_prod_goodng_list ; 
           if prodid = 0 then
              open wk_cur for select * from alldo_gh_iot_workorder where id in (select order_id from alldo_gh_iot_workorder_qc where qc_date::DATE between startdate::DATE and enddate::DATE);
           else
              open wk_cur for select * from alldo_gh_iot_workorder where id in (select order_id from alldo_gh_iot_workorder_qc where qc_date::DATE between startdate::DATE and enddate::DATE)
                 and product_no = prodid ;
           end if ;   
          loop
            fetch wk_cur into wk_rec ;
            exit when not found ;
            select sum(coalesce(material_ng_num,0)),sum(coalesce(processing_ng_num,0)) into mng,png from alldo_gh_iot_workorder_qc where order_id=wk_rec.id ;
            if wk_rec.blank_num = 0 then
               mngratio = 0 ;
               pngratio = 0 ;
            else   
               mngratio = round((mng::numeric/wk_rec.blank_num::numeric)*100,1) ;
               pngratio = round((png::numeric/wk_rec.blank_num::numeric)*100,1) ;
            end if ;   
            if mngratio > 0 or pngratio > 0 then
               insert into alldo_gh_iot_prod_goodng_list(product_id,mo_no,blank_num,prod_num,m_ng,p_ng,mng_ratio,png_ratio,eng_type) values
                      (wk_rec.product_no,wk_rec.id,wk_rec.blank_num,wk_rec.prodin_num,mng,png,mngratio,pngratio,wk_rec.eng_type) ;
            end if ; 
          end loop ;
          close wk_cur ;
           delete from alldo_gh_iot_prod_goodng_list where product_id is null  ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genprodrealnum() cascade""")
        self.env.cr.execute("""create or replace function genprodrealnum() returns void as $BODY$
         DECLARE
           currentdate1 date ;
           currentdate2 date;
           currentdate3 date ;
           wk_cur refcursor ;
           wk_rec record ;
           real_cur refcursor ;
           real_rec record ;
           prodtmplid int ;
           engtype varchar ;
           wkid int ;
           prodid int ;
           prodid1 int ;
           myid int ;
           myhour int ;
           realprod int ;
           moldcavity int ;
           mystate char ;
           mystdnum int ;
           mystdnum1 int ;
           mychkdate date ;
           ncount int ;
           eng_cur refcursor ;
           eng_rec record ;
         BEGIN
           delete from alldo_gh_iot_production_real ;
           select current_date::DATE into currentdate1 ;
           select (current_date - interval '1 month')::DATE into currentdate2 ;
          /* open wk_cur for select * from alldo_gh_iot_workorder_iot_data where iot_date::DATE between
               currentdate2::DATE and currentdate1::DATE and order_id not in (select id from alldo_gh_iot_workorder where eng_order='4');
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             select product_no,eng_type,state into prodid,engtype,mystate from alldo_gh_iot_workorder where id = wk_rec.order_id ;
             select product_tmpl_id into prodtmplid from product_product where id = prodid ;
             select id into myid from alldo_gh_iot_production_real where prod_id=prodtmplid and eng_type like '%'|| engtype ||'%' ;
             if mystate != '5' then
                 if myid is not null then
                    update alldo_gh_iot_production_real set prod_num = coalesce(prod_num,0) + coalesce(wk_rec.iot_num,0),
                       prod_time = coalesce(prod_time,0) + coalesce(wk_rec.iot_duration,0) where id = myid ;
                 else
                    insert into alldo_gh_iot_production_real(prod_id,eng_type,prod_num,prod_time) values (prodtmplid,engtype,coalesce(wk_rec.iot_num,0),coalesce(wk_rec.iot_duration,0)) ;
                 end if ;
             end if ;    
           end loop ;
           close wk_cur ;    
           
           open real_cur for select * from alldo_gh_iot_production_real ;
           loop
             fetch real_cur into real_rec ;
             exit when not found ;
             myhour = round((real_rec.prod_time::numeric/3600::numeric),2) ;
             if myhour = 0 then
                realprod = 0 ;
             else   
                realprod = round((real_rec.prod_num::numeric/myhour::numeric),0) ;
             end if ;   
             select id,coalesce(mold_cavity,1) into myid,moldcavity from alldo_gh_iot_eng_order where prod_id = real_rec.prod_id and eng_type like '%'|| real_rec.eng_type||'%' ;
             if moldcavity = 0 then
                realprod = 0 ;
             else
                realprod = round((realprod::numeric/moldcavity::numeric),0) ;
             end if ;
             update alldo_gh_iot_eng_order set prod_real_num = realprod where id = myid ;
           end loop ;
           close real_cur ; */
           open eng_cur for select * from alldo_gh_iot_eng_order where prod_id not in (select id from product_template where is_blank=True);
           loop
              fetch eng_cur into eng_rec ;
              exit when not found ;
              select id into prodid from product_product where product_tmpl_id = eng_rec.prod_id ;
              select avg(product_num)::INT into realprod from alldo_gh_iot_cnc_performance_report where 
                 product_no=prodid and iot_date::DATE <= currentdate1::DATE and iot_date::DATE >= currentdate2::DATE
                  and eng_type like '%'|| eng_rec.eng_type ||'%';
              update alldo_gh_iot_eng_order set prod_real_num = realprod where id = eng_rec.id ;  
           end loop ;
           close eng_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkamountnum(wkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkamountnum(wkid int) returns void as $BODY$
         DECLARE
           ncount int ;
           blanknum float ;
           prodgoodnum float ;
         BEGIN
           select sum(coalesce(in_good_num,0)) into blanknum from alldo_gh_iot_wkorder_prodin where order_id = wkid ;
           select sum(coalesce(total_amount_num,0) - coalesce(loss_num,0) - coalesce(material_ng_num,0) - coalesce(processing_ng_num,0))
                  into prodgoodnum from alldo_gh_iot_workorder_qc where order_id = wkid ;
           if blanknum is null then
              blanknum = 0 ;
           end if ;    
           if prodgoodnum is null then
              prodgoodnum = 0 ;
           end if ;   
           update alldo_gh_iot_workorder set blank_num=blanknum,mo_production_num=prodgoodnum where id = wkid ;       
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkngratio(wkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkngratio(wkid int) returns void as $BODY$
         DECLARE
           ncount int ;
           wkpngnum float ;
           wkmngnum float ;
           wklngnum float ;
           wktotnum float ;
           wkgoodnum float ;
           ngratio float ;
         BEGIN
           select sum(coalesce(processing_ng_num,0)),sum(coalesce(material_ng_num,0)),sum(coalesce(loss_num,0)),sum(coalesce(total_amount_num,0)) into
              wkpngnum,wkmngnum,wklngnum,wktotnum from alldo_gh_iot_workorder_qc where order_id = wkid ;
           if wkpngnum is null then
              wkpngnum = 0 ;
           end if ;
           if wkmngnum is null then
              wkmngnum = 0 ;
           end if ;    
           if wklngnum is null then
              wklngnum = 0 ;
           end if ;  
           if wktotnum is null then
              wktotnum = 0 ;
           end if ;
           wkgoodnum = wktotnum - wkpngnum - wkmngnum - wklngnum ;
           if wktotnum = 0 then
              ngratio = 0.0 ;
           else
              ngratio = round(((wkpngnum + wkmngnum)::numeric / (wktotnum - wklngnum)::numeric) * 100::numeric,1) ;
           end if ;
           select count(*) into ncount from alldo_gh_iot_wkorder_ngratio where order_id = wkid ;
           if ncount = 0 then
              insert into alldo_gh_iot_wkorder_ngratio(order_id,wk_good_num,wk_ng_num,material_ng_num,wk_loss_num,ng_ratio)
                values (wkid,wkgoodnum,wkpngnum,wkmngnum,wklngnum,ngratio) ;
           else
              update alldo_gh_iot_wkorder_ngratio set wk_good_num=wkgoodnum,wk_ng_num=wkpngnum,material_ng_num=wkmngnum,wk_loss_num=wklngnum,ng_ratio=ngratio
                 where order_id=wkid ;
           end if ;      
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getbookingnum(pickid int) cascade""")
        self.env.cr.execute("""create or replace function getbookingnum(pickid int) returns float as $BODY$
         DECLARE
           myres float ;
         BEGIN
           select sum(coalesce(product_qty,0)) into myres from stock_move where picking_id = pickid ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists genpobooking(pono varchar,cusid int,prodno int,odate date,poloc varchar,polock Boolean,sdate date,ponum float,ppickid int,bpickid int,poowner int,cussystem Boolean) cascade""")
        self.env.cr.execute("""drop function if exists genpobooking(pono varchar,cusid int,prodno int,odate date,poloc varchar,polock Boolean,sdate date,ponum float,ppickid int,bpickid int,poowner int,cussystem Boolean,lockdesc varchar) cascade""")
        self.env.cr.execute("""create or replace function genpobooking(pono varchar,cusid int,prodno int,odate date,poloc varchar,polock Boolean,sdate date,ponum float,ppickid int,bpickid int,poowner int,cussystem Boolean,lockdesc varchar) returns void as $BODY$
         DECLARE
           blankno int ;
           ponhand float ;
           bonhand float ;
           pomemo varchar ;
           prodtmplid int ;
           maxpowkid int ;
           maxbookingid int ;
           p_num float ;
           b_num float ;
         BEGIN
           select product_tmpl_id into prodtmplid from product_product where id = prodno ;
           select coalesce(description,' ') into pomemo from product_template where id = prodtmplid ; 
           select getprodblank(prodno) into blankno ;
           select getprodonhand(prodno) into ponhand ;
           select getblankonhand(blankno) into bonhand ;
           insert into alldo_gh_iot_po_wkorder(po_no,cus_name,product_no,order_date,po_location,po_memo,po_lock,shipping_date,po_num,is_closed,is_open,state,active,custom_system) values
            (pono,cusid,prodno,odate::DATE,poloc,pomemo,polock,sdate::DATE,ponum,False,False,'1',True,cussystem) ;
            select max(id) into maxpowkid from alldo_gh_iot_po_wkorder ;
           if polock=True and ponum > 0 then
              insert into alldo_gh_iot_prod_booking(po_id,booking_custom,booking_prod,prod_onhand,booking_blank,blank_onhand,booking_num,booking_date,booking_type,booking_owner,booking_desc) values
               (maxpowkid,cusid,prodno,ponhand,blankno,bonhand,ponum,odate,'1',poowner,lockdesc) ;
              select max(id) into maxbookingid from alldo_gh_iot_prod_booking ;
              update alldo_gh_iot_prod_booking set booking_prod_num=0,booking_blank_num=0,release_prod_num=0,release_blank_num=0 where id = maxbookingid ;
              if ppickid > 0 then
                 select getbookingnum(ppickid) into p_num ;
                 update alldo_gh_iot_prod_booking set booking_p_picking=ppickid,booking_prod_num=p_num where id = maxbookingid ;         
              end if ;
              if bpickid > 0 then
                 select getbookingnum(bpickid) into b_num ;
                 update alldo_gh_iot_prod_booking set booking_b_picking=bpickid,booking_blank_num=b_num where id = maxbookingid ;
              end if ;
           end if ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists calreplacewknum() cascade""")
        self.env.cr.execute("""create or replace function calreplacewknum() returns void as $BODY$
         DECLARE
           rep_cur refcursor ;
           rep_rec record ;
           repdate1 timestamp ;
           repdate2 timestamp ;
           wksdt timestamp ;
           wkedt timestamp ;
           wksdtt varchar ;
           wkedtt varchar ;
           wknum float ;
           ncount int ;
           ncount1 int ;
           minid int ;
           maxid int ;
         BEGIN
           open rep_cur for select * from alldo_gh_iot_replaceline_list ;
           loop
              fetch rep_cur into rep_rec ;
              exit when not found ;
              repdate1 = rep_rec.replace_start_datetime::timestamp ;
              repdate2 = rep_rec.replace_end_datetime::timestamp ;
              select count(*) into ncount from alldo_gh_iot_workorder_iot_data where order_id=rep_rec.order_id and iot_owner=rep_rec.replace_owner
                and iot_node=rep_rec.equipment_id and iot_date::DATE = repdate2::DATE ;
              if ncount > 0 then
                 select min(iot_date),max(iot_date) into wksdt,wkedt from alldo_gh_iot_workorder_iot_data where order_id=rep_rec.order_id and iot_owner=rep_rec.replace_owner
                       and iot_node=rep_rec.equipment_id and iot_date::DATE = repdate2::DATE ; 
                 select sum(coalesce(iot_num,0)) into wknum from alldo_gh_iot_workorder_iot_data where order_id=rep_rec.order_id and iot_owner=rep_rec.replace_owner
                       and iot_node=rep_rec.equipment_id and iot_date::DATE = repdate2::DATE ;   
                 wksdt = wksdt::timestamp + interval '8 hours' ;
                 wkedt = wkedt::timestamp + interval '8 hours' ;      
                 wksdtt = substring(wksdt::TEXT,1,16) ;
                 wkedtt = substring(wkedt::TEXT,1,16) ;         
              else
                 wksdtt = ' ' ;
                 wkedtt = ' ' ;
                 wknum = 0 ;
              end if ; 
              update alldo_gh_iot_replaceline_list set wk_start_datetime=wksdtt,wk_end_datetime=wkedtt,wk_num=coalesce(wknum,0) where id = rep_rec.id ;
           end loop ;
           close rep_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""update product_template set is_blank=True where substring(default_code,1,2)='R-' ;""")
        self.env.cr.execute("""update product_template set is_blank=False where substring(default_code,1,2)!='R-' ;""")

        self.env.cr.execute("""drop function if exists setpowkorderclose(pono varchar) cascade""")
        self.env.cr.execute("""create or replace function setpowkorderclose(pono varchar) returns void as $BODY$
         DECLARE
           ncount int ;
           maxid int ;
         BEGIN
           select count(*) into ncount from alldo_gh_iot_po_wkorder where po_no=pono ;
           if ncount > 0 then
              select max(id) into maxid from alldo_gh_iot_po_wkorder where po_no=pono ;
              update alldo_gh_iot_po_wkorder set state='3' where id = maxid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genbookingpb() cascade""")
        self.env.cr.execute("""create or replace function genbookingpb() returns void as $BODY$
         DECLARE
           booking_cur refcursor ;
           booking_rec record ;
           p_num float ;
           b_num float ;
         BEGIN
           open booking_cur for select * from alldo_gh_iot_prod_booking ;
           loop
              fetch booking_cur into booking_rec ;
              exit when not found ;
              if booking_rec.booking_p_picking is not null then
                 select getbookingnum(booking_rec.booking_p_picking) into p_num ;
              else
                 p_num = 0 ;
              end if ;
              if booking_rec.booking_b_picking is not null then
                 select getbookingnum(booking_rec.booking_b_picking) into b_num ;
              else
                 b_num = 0 ;
              end if ;    
              update alldo_gh_iot_prod_booking set booking_prod_num=p_num,booking_blank_num=b_num,release_prod_num=0,release_blank_num=0 where id = booking_rec.id ;  
           end loop ;
           close booking_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpackagemo() cascade""")
        self.env.cr.execute("""create or replace function getpackagemo() returns setof INT as $BODY$
         DECLARE
           mo_cur refcursor ;
           mo_rec record ;
           engorder char ;
           prodid int ;
           engtype varchar ;
         BEGIN
           open mo_cur for select * from alldo_gh_iot_workorder where state = '1' ;
           loop
             fetch mo_cur into mo_rec ;
             exit when not found ;
             select getprodengorder(mo_rec.product_no,mo_rec.eng_type) into engorder ;
             if engorder='4' then
                return next mo_rec.id ;
             end if ;   
           end loop ;
           close mo_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpackagemodata(powner int,moid int,startdt timestamp,enddt timestamp,pnum float,moclose Boolean) cascade""")
        self.env.cr.execute("""create or replace function genpackagemodata(powner int,moid int,startdt timestamp,enddt timestamp,pnum float,moclose Boolean) returns void as $BODY$
         DECLARE
           empid int ;
           resourceid int ;
           iotserial varchar ;
           ptime1 Float;
           ptime2 Float;
           ptime3 Float ;
           pdate date ;
           prodid int ;
         BEGIN
           select product_no into prodid from alldo_gh_iot_workorder where id = moid ;
           select id into resourceid from resource_resource where user_id = powner ;
           select id into empid from hr_employee where resource_id=resourceid ;
           select current_timestamp::TEXT into iotserial ;
           insert into alldo_gh_iot_workorder_iot_data(order_id,iot_date,iot_owner,iot_num,iot_duration,std_duration,iot_serial) values
            (moid,startdt,empid,0,0,0,iotserial) ;
           select extract(minute from (select age(enddt,startdt))) into ptime1 ;
           select extract(hours from (select age(enddt,startdt))) into ptime2 ;
           ptime3 = (ptime1 * 60) + (ptime2 * 60 * 60) ;
           select current_timestamp::TEXT into iotserial ;
           insert into alldo_gh_iot_workorder_iot_data(order_id,iot_date,iot_owner,iot_num,iot_duration,std_duration,iot_serial) values
            (moid,enddt,empid,pnum,ptime3,0,iotserial) ;
           select enddt::DATE into pdate ;
           insert into alldo_gh_iot_workorder_qc(order_id,qc_date,total_amount_num,complete_date,iot_owner1,product_no) values 
              (moid,pdate,pnum,pdate,empid,prodid) ; 
           if moclose = True then
              update alldo_gh_iot_workorder set state='4' where id = moid ;
           end if ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gensupplierloc(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gensupplierloc(partnerid int) returns void as $BODY$
         DECLARE
           partnername varchar ;
           locid int ;
           resid varchar ;
           valreference varchar ;
           parentpath varchar ;
           completename varchar ;
         BEGIN
           select name into partnername from res_partner where id = partnerid ;
           partnername = concat(partnername,'(委外倉)') ;
           select id into locid from stock_location where name = partnername ;
           if locid is null then
              insert into stock_location(name,location_id,usage,active) values (partnername,7,'internal',true) ;
              select max(id) into locid from stock_location ;
           end if ; 
           parentpath = concat('1/7/',locid::TEXT) ;
           completename = concat('WH/',partnername) ;
           update stock_location set parent_path=parentpath,complete_name=completename where id = locid ;
           resid = concat('res.partner',',',partnerid::TEXT) ;
           valreference = concat('stock.location',',',locid::TEXT) ;
           insert into ir_property(name,res_id,company_id,fields_id,value_reference,type,create_uid,create_date)
             values (partnername,resid,1,6128,valreference,'many2one',2,current_date) ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gethasprodlock(wkid int) cascade""")
        self.env.cr.execute("""create or replace function gethasprodlock(wkid int) returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           poid int ;
         BEGIN
           select coalesce(po_no1,0) into poid from alldo_gh_iot_workorder where id = wkid ;
           if poid > 0 then
              select coalesce(po_lock,False) into myres from alldo_gh_iot_po_wkorder where id = poid ;
           else
              myres = False ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodlocknum(wkid int) cascade""")
        self.env.cr.execute("""create or replace function getprodlocknum(wkid int) returns Float as $BODY$
         DECLARE
           poid int ;
           bookingnum float ;
           releasenum float ;
           myres float ;
         BEGIN
            select coalesce(po_no1,0) into poid from alldo_gh_iot_workorder where id = wkid ;
           if poid > 0 then
              select sum(coalesce(booking_num,0)) into bookingnum from alldo_gh_iot_prod_booking
                 where po_id = poid ;
              select sum(coalesce(release_num,0)) into releasenum from alldo_gh_iot_prod_booking_release
                 where po_id = poid ;   
            
              myres = bookingnum - releasenum ;   
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getbbookingnum(blankno int) cascade""")
        self.env.cr.execute("""create or replace function getbbookingnum(blankno int) returns Float as $BODY$
        DECLARE
          bbookingloc int ;
          myres Float ;
        BEGIN
            select min(bbooking_loc) into bbookingloc from alldo_gh_iot_company_stockloc ;
            select sum(coalesce(quantity,0)) into myres from stock_quant where company_id=1 and location_id=bbookingloc and product_id=blankno ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpoprodlocknum(poid int) cascade""")
        self.env.cr.execute("""create or replace function getpoprodlocknum(poid int) returns int as $BODY$
         DECLARE
           myres int ;
           ncount int ;
         BEGIN
           select count(*) into ncount from alldo_gh_iot_prod_booking where po_id = poid ;
           if ncount > 0 then
              select sum(coalesce(booking_prod_num::INTEGER,0)) into myres from 
                     alldo_gh_iot_prod_booking where po_id = poid ;
           else
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpounreleasenum(poid int) cascade""")
        self.env.cr.execute("""create or replace function getpounreleasenum(poid int) returns int as $BODY$
         DECLARE
           bookingnum int ;
           releasenum int ;
           myres int ;
           ncount int ;
         BEGIN
          
          select sum(coalesce(booking_num,0))::INTEGER into bookingnum from 
                 alldo_gh_iot_prod_booking where po_id = poid ;
          if bookingnum is null then
             bookingnum = 0 ;
          end if ;       
          select sum(coalesce(release_num,0))::INTEGER into releasenum from 
                 alldo_gh_iot_prod_booking_release where po_id = poid ;   
          if releasenum is null then
             releasenum = 0 ;
          end if ;    
          myres = bookingnum - releasenum ;         
          if myres is null then
            myres = 0 ;
          end if ;  
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getshippingqty(pickid int,prodid int) cascade""")
        self.env.cr.execute("""create or replace function getshippingqty(pickid int,prodid int) returns float as $BODY$
         DECLARE
           myres float ;
           mv_cur refcursor ;
           mv_rec record ;
           mynum float ;
         BEGIN
           myres = 0 ;
           open mv_cur for select * from stock_move where picking_id=pickid and picking_type_id=2 and product_id=prodid ;
           loop
             fetch mv_cur into mv_rec ;
             exit when not found ;
             select sum(coalesce(qty_done,0)) into mynum from stock_move_line where move_id = mv_rec.id ;
             myres = myres + mynum ;
           end loop ;
           close mv_cur ;
           return myres ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists checkcanshipping(pickid int) cascade""")
        self.env.cr.execute("""create or replace function checkcanshipping(pickid int) returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           shippingnum int ;
           polock Boolean ;
           prodid int ;
           onhandqty int ;
           picktype int ;
           mogid int ;
           poid int ;
         BEGIN
           select picking_type_id,mo_group_id into picktype,mogid from stock_picking where id = pickid ;
           if picktype = 2 then
              select max(po_no1),max(product_no) into poid,prodid from alldo_gh_iot_workorder where mo_group_id = mogid ;
              if poid is not null then
                  select po_lock into polock from alldo_gh_iot_po_wkorder where id = poid ;
                  if polock = True then
                     select getshippingqty(pickid,prodid)::INTEGER into shippingnum ;
                     select getprodonhand(prodid)::INTEGER into onhandqty ;
                     if onhandqty::numeric < shippingnum::numeric then
                        myres = False ;
                     else
                        myres = True ;
                     end if ;
                  else
                     myres = True ;
                  end if ;
              else
                  myres = True ;
              end if ;    
           else
              myres = True ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpostockin(wkid int,pickid int,picknum float) cascade""")
        self.env.cr.execute("""drop function if exists genpostockin(wkid int,pickid int,picknum float,locid int,destlocid int) cascade""")
        self.env.cr.execute("""create or replace function genpostockin(wkid int,pickid int,picknum float,locid int,destlocid int) returns void as $BODY$
         DECLARE
           poid int ;
           po_cur refcursor ;
           po_rec record ;
         BEGIN
           select coalesce(po_no1,0) into poid from alldo_gh_iot_workorder where id = wkid ;
           if poid is null then
              poid = 0 ;
           end if ;
           if poid > 0 and pickid > 0 and picknum > 0 then
              insert into alldo_gh_iot_stock_line(po_id,picking_id,picking_num,picking_type_id,picking_date,location_id,dest_location_id) values
               (poid,pickid,picknum,5,current_date,locid,destlocid) ;
           end if ;
           open po_cur for select * from powkorder_iotwkorder_rel where wk_id = wkid ;
           loop
             fetch po_cur into po_rec ;
             exit when not found ;
             if po_rec.po_id != poid then 
                 insert into alldo_gh_iot_stock_line(po_id,picking_id,picking_num,picking_type_id,picking_date,location_id,dest_location_id) values
                   (po_rec.po_id,pickid,picknum,5,current_date,locid,destlocid) ;
             end if ;      
           end loop ;
           close po_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpackageprod() cascade""")
        self.env.cr.execute("""create or replace function getpackageprod() returns INT as $BODY$
         DECLARE
           myres int ;
         BEGIN
           select id into myres from product_product where default_code='SERVICE_WORK' ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists resetstockpicking(repid int) cascade""")
        self.env.cr.execute("""create or replace function resetstockpicking(repid int) returns void as $BODY$
         DECLARE
           rep_cur refcursor ;
           rep_rec record ;
         BEGIN
           open rep_cur for select * from alldo_gh_iot_stockpicking_report_line where rep_id = repid ;
           loop
             fetch rep_cur into rep_rec ;
             exit when not found ;
             if rep_rec.item is null or rep_rec.prod_no is null then
                if rep_rec.prod_no1 is not null or rep_rec.prod_no1 != ' ' then
                   update alldo_gh_iot_stockpicking_report_line set item=1,prod_no=rep_rec.prod_no1,prod_num=rep_rec.prod_num1,prod_uom=rep_rec.prod_uom1,prod_price=rep_rec.prod_price1,line_memo=rep_rec.line_memo1 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no2 is not null or rep_rec.prod_no2 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item1=2,prod_no1=rep_rec.prod_no2,prod_num1=rep_rec.prod_num2,prod_uom1=rep_rec.prod_uom2,prod_price1=rep_rec.prod_price2,line_memo1=rep_rec.line_memo2 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no3 is not null or rep_rec.prod_no3 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item2=3,prod_no2=rep_rec.prod_no3,prod_num2=rep_rec.prod_num3,prod_uom2=rep_rec.prod_uom3,prod_price2=rep_rec.prod_price3,line_memo2=rep_rec.line_memo3 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no4 is not null or rep_rec.prod_no4 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item3=4,prod_no3=rep_rec.prod_no4,prod_num3=rep_rec.prod_num4,prod_uom3=rep_rec.prod_uom4,prod_price3=rep_rec.prod_price4,line_memo3=rep_rec.line_memo4 where id = rep_rec.id ;
                end if ;   
                if rep_rec.prod_no5 is not null or rep_rec.prod_no5 != ' ' then 
                   update alldo_gh_iot_stockpicking_report_line set item4=5,prod_no4=rep_rec.prod_no5,prod_num4=rep_rec.prod_num5,prod_uom4=rep_rec.prod_uom5,prod_price4=rep_rec.prod_price5,line_memo4=rep_rec.line_memo5 where id = rep_rec.id ;
                end if ;   
             elsif rep_rec.item1 is null or rep_rec.prod_no1 is null then   
                if rep_rec.prod_no2 is not null or rep_rec.prod_no2 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item1=2,prod_no1=rep_rec.prod_no2,prod_num1=rep_rec.prod_num2,prod_uom1=rep_rec.prod_uom2,prod_price1=rep_rec.prod_price2,line_memo1=rep_rec.line_memo2 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no3 is not null or rep_rec.prod_no3 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item2=3,prod_no2=rep_rec.prod_no3,prod_num2=rep_rec.prod_num3,prod_uom2=rep_rec.prod_uom3,prod_price2=rep_rec.prod_price3,line_memo2=rep_rec.line_memo3 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no4 is not null or rep_rec.prod_no4 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item3=4,prod_no3=rep_rec.prod_no4,prod_num3=rep_rec.prod_num4,prod_uom3=rep_rec.prod_uom4,prod_price3=rep_rec.prod_price4,line_memo3=rep_rec.line_memo4 where id = rep_rec.id ;
                end if ;   
                if rep_rec.prod_no5 is not null or rep_rec.prod_no5 != ' ' then 
                   update alldo_gh_iot_stockpicking_report_line set item4=5,prod_no4=rep_rec.prod_no5,prod_num4=rep_rec.prod_num5,prod_uom4=rep_rec.prod_uom5,prod_price4=rep_rec.prod_price5,line_memo4=rep_rec.line_memo5 where id = rep_rec.id ;
                end if ;   
             elsif rep_rec.item2 is null or rep_rec.prod_no2 is null then   
                if rep_rec.prod_no3 is not null or rep_rec.prod_no3 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item2=3,prod_no2=rep_rec.prod_no3,prod_num2=rep_rec.prod_num3,prod_uom2=rep_rec.prod_uom3,prod_price2=rep_rec.prod_price3,line_memo2=rep_rec.line_memo3 where id = rep_rec.id ;
                end if ;
                if rep_rec.prod_no4 is not null or rep_rec.prod_no4 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item3=4,prod_no3=rep_rec.prod_no4,prod_num3=rep_rec.prod_num4,prod_uom3=rep_rec.prod_uom4,prod_price3=rep_rec.prod_price4,line_memo3=rep_rec.line_memo4 where id = rep_rec.id ;
                end if ;   
                if rep_rec.prod_no5 is not null or rep_rec.prod_no5 != ' ' then 
                   update alldo_gh_iot_stockpicking_report_line set item4=5,prod_no4=rep_rec.prod_no5,prod_num4=rep_rec.prod_num5,prod_uom4=rep_rec.prod_uom5,prod_price4=rep_rec.prod_price5,line_memo4=rep_rec.line_memo5 where id = rep_rec.id ;
                end if ;    
             elsif rep_rec.item3 is null or rep_rec.prod_no3 is null then   
                if rep_rec.prod_no4 is not null or rep_rec.prod_no4 != ' ' then   
                   update alldo_gh_iot_stockpicking_report_line set item3=4,prod_no3=rep_rec.prod_no4,prod_num3=rep_rec.prod_num4,prod_uom3=rep_rec.prod_uom4,prod_price3=rep_rec.prod_price4,line_memo3=rep_rec.line_memo4 where id = rep_rec.id ;
                end if ;   
                if rep_rec.prod_no5 is not null or rep_rec.prod_no5 != ' ' then 
                   update alldo_gh_iot_stockpicking_report_line set item4=5,prod_no4=rep_rec.prod_no5,prod_num4=rep_rec.prod_num5,prod_uom4=rep_rec.prod_uom5,prod_price4=rep_rec.prod_price5,line_memo4=rep_rec.line_memo5 where id = rep_rec.id ;
                end if ;    
             elsif rep_rec.item4 is null or rep_rec.prod_no4 is null then   
                if rep_rec.prod_no5 is not null or rep_rec.prod_no5 != ' ' then 
                   update alldo_gh_iot_stockpicking_report_line set item4=5,prod_no4=rep_rec.prod_no5,prod_num4=rep_rec.prod_num5,prod_uom4=rep_rec.prod_uom5,prod_price4=rep_rec.prod_price5,line_memo4=rep_rec.line_memo5 where id = rep_rec.id ;
                end if ; 
             end if ;   
           end loop ;
           close rep_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpowkorderdata(puid int) cascade""")
        self.env.cr.execute("""create or replace function genpowkorderdata(puid int) returns void as $BODY$
         DECLARE
           pol_cur refcursor ;
           pol_rec record ;
           ncount int ;
           mystate varchar ;
         BEGIN
           select state into mystate from purchase_order where id = puid ;
           if mystate != 'cancel' then
              open pol_cur for select * from purchase_order_line where order_id = puid ;
              loop
                fetch pol_cur into pol_rec ;
                exit when not found ;
                select count(*) into ncount from alldo_gh_iot_po_wkorder where product_no=pol_rec.product_id and id=pol_rec.po_wkorder_id ;
                if ncount > 0 then
                   if pol_rec.po_wkorder_id is not null then
                      update alldo_gh_iot_po_wkorder set po_id=puid,booking_blank=True,booking_blank_num=pol_rec.product_uom_qty where id=pol_rec.po_wkorder_id ;
                   end if ;
                   /* if pol_rec.qty_received > 0 and pol_rec.po_wkorder_id is not null then
                      update alldo_gh_iot_po_wkorder set stockin_blank=True,stockin_blank_num=pol_rec.qty_received
                       where id = pol_rec.po_wkorder_id ;
                   end if ; */
                end if ;
              end loop ;
              close pol_cur ;
           end if ;
           
          
         END;$BODY$
         LANGUAGE plpgsql;""")


        self.env.cr.execute("""drop function if exists genwkorderpodata(wkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkorderpodata(wkid int) returns void as $BODY$
         DECLARE
           po_cur refcursor ;
           po_rec record ;
         BEGIN
           update alldo_gh_iot_po_wkorder set wk_id=null,open_wkorder=False where wk_id=wkid ;
           open po_cur for select * from powkorder_iotwkorder_rel where wk_id = wkid ;
           loop
             fetch po_cur into po_rec ;
             exit when not found ;
             update alldo_gh_iot_po_wkorder set wk_id=wkid,open_wkorder=True,is_open=True where id=po_rec.po_id  ;
           end loop ;
           close po_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpurchasedata() cascade""")
        self.env.cr.execute("""create or replace function genpurchasedata() returns void as $BODY$
         DECLARE
           pu_cur refcursor ;
           pu_rec record ;
           ncount int ;
         BEGIN
           select count(*) into ncount from purchase_order where change_ids is null or change_ids=False ;
           if ncount > 0 then
              open pu_cur for select id from purchase_order where change_ids is null or change_ids=False ;
              loop
                fetch pu_cur into pu_rec ;
                exit when not found ;
                execute genpowkorderdata(pu_rec.id) ;
                update purchase_order set change_ids=True where id=pu_rec.id ;
              end loop ;
              close pu_cur ;
              
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genopenpowkorder(wizid int,wkid int) cascade""")
        self.env.cr.execute("""create or replace function genopenpowkorder(wizid int,wkid int) returns void as $BODY$
          DECLARE
            wiz_cur refcursor ;
            wiz_rec record ;
            ponoid int ;
            ncount int ;
            ncount1 int ;
            engtype varchar ;
            engseq int ;
            engorder char ;
          BEGIN
            select coalesce(po_no1,0),eng_type,eng_seq,eng_order into ponoid,engtype,engseq,engorder from alldo_gh_iot_workorder where id = wkid ;
            open wiz_cur for select * from po_wkorder_wizard_rel where wiz_id=wizid ;
            loop
              fetch wiz_cur into wiz_rec ;
              exit when not found ;
              insert into powkorder_iotwkorder_rel(wk_id,po_id) values (wkid,wiz_rec.po_id) ;
              update alldo_gh_iot_po_wkorder set open_wkorder=True,wk_id=wkid where id=wiz_rec.po_id ;
              select count(*) into ncount1 from alldo_gh_iot_po_wkorder_line where po_id=wiz_rec.po_id and wkorder_id=wkid ;
              if ncount1 = 0 then
                  insert into alldo_gh_iot_po_wkorder_line(po_id,wkorder_id,eng_type,eng_seq,eng_order,complete_num,ng_num) values
                   (wiz_rec.po_id,wkid,engtype,engseq,engorder,0,0) ;
              end if ;     
            end loop ;
            close wiz_cur ;
            if ponoid > 0 then
               select count(*) into ncount from powkorder_iotwkorder_rel where wk_id=wkid and po_id = ponoid ;
               if ncount = 0 then
                  insert into powkorder_iotwkorder_rel(wk_id,po_id) values (wkid,ponoid) ;
                  update alldo_gh_iot_po_wkorder set open_wkorder=True,wk_id=wkid where id=ponoid ;
                  select count(*) into ncount1 from alldo_gh_iot_po_wkorder_line where po_id=ponoid and wkorder_id=wkid ;
                  if ncount1 = 0 then
                     insert into alldo_gh_iot_po_wkorder_line(po_id,wkorder_id,eng_type,eng_seq,eng_order,complete_num,ng_num) values
                        (ponoid,wkid,engtype,engseq,engorder,0,0) ;
                  end if ;      
               end if ;
            end if ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpowkorderlist(prodid int) cascade""")
        self.env.cr.execute("""create or replace function genpowkorderlist(prodid int) returns void as $BODY$
         DECLARE
           po_cur refcursor ;
           po_rec record ;
           pquant_cur refcursor ;
           pquant_rec record ;
           bquant_cur refcursor ;
           bquant_rec record ;
           ncount int ;
           ncount1 int ;
           myid int ;
           blankid int ;
         BEGIN
           delete from alldo_gh_iot_powkorder_list ; 
           select getprodblank(prodid) into blankid ; 
           open po_cur for select * from alldo_gh_iot_po_wkorder where product_no=prodid and state in ('1','2') ;
           loop
             fetch po_cur into po_rec ;
             exit when not found ;
             insert into alldo_gh_iot_powkorder_list(po_no,cus_name,product_no,order_date,shipping_date,response_shipping_date,custom_system,open_wkorder,booking_blank,stockin_blank,po_id,po_num) values
              (po_rec.po_no,po_rec.cus_name,po_rec.product_no,po_rec.order_date,po_rec.shipping_date,po_rec.response_shipping_date,po_rec.custom_system,po_rec.open_wkorder,po_rec.booking_blank,po_rec.stockin_blank,po_rec.po_id,po_rec.po_num) ;
             select max(id) into myid from  alldo_gh_iot_powkorder_list ;
             
             open pquant_cur for select * from stock_quant where product_id=prodid and location_id in 
                (select id from stock_location where active=True and usage='internal' and scrap_location=False) ;
             loop
               fetch pquant_cur into pquant_rec ;
               exit when not found ;
               select count(*) into ncount from alldo_gh_iot_powkorder_line where line_id=myid and
                    product_no=prodid and location_id=pquant_rec.location_id ;
               if ncount = 0 then
                  insert into alldo_gh_iot_powkorder_line(line_id,product_no,location_id,qty) values (myid,prodid,pquant_rec.location_id,pquant_rec.quantity) ;
               else
                  update alldo_gh_iot_powkorder_line set qty=coalesce(qty,0)+ pquant_rec.quantity where product_no=prodid and location_id=pquant_rec.location_id and line_id=myid ;
               end if ;     
             end loop ;
             close pquant_cur ; 
             
             open bquant_cur for select * from stock_quant where product_id=blankid and location_id in 
                (select id from stock_location where active=True and usage='internal' and scrap_location=False) ;
             loop
               fetch bquant_cur into bquant_rec ;
               exit when not found ;
               select count(*) into ncount1 from alldo_gh_iot_powkorder_line where line_id=myid and
                    product_no=blankid and location_id=bquant_rec.location_id ;
               if ncount1 = 0 then
                  insert into alldo_gh_iot_powkorder_line1(line_id,product_no,location_id,qty) values (myid,bquant_rec.product_id,bquant_rec.location_id,bquant_rec.quantity) ;
               else
                  update alldo_gh_iot_powkorder_line1 set qty=coalesce(qty,0)+ bquant_rec.quantity where product_no=blankid and location_id=bquant_rec.location_id and line_id=myid;
               end if ;     
             end loop ;
             close bquant_cur ;     
           end loop ;
           close po_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpounstockinnum(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpounstockinnum(prodid int) returns float as $BODY$
         DECLARE
           pur_cur refcursor ;
           pur_rec record ;
           picking_cur refcursor ;
           picking_rec record ;
           orderid int ;
           poname varchar ;
           qty1 float ;
           qty2 float ;
           qty3 float ;
           qty4 float ;
           myres float ;
         BEGIN
           myres = 0 ;
           open pur_cur for select * from purchase_order_line where state='purchase' and product_id=prodid ;
           loop
             fetch pur_cur into pur_rec ;
             exit when not found ;
             select name into poname from purchase_order where id=pur_rec.order_id ;
             qty1 = 0 ;
             qty2 = 0 ;
             open picking_cur for select * from stock_picking where origin=poname and picking_type_id=1 ;
             loop
               fetch picking_cur into picking_rec ;
               exit when not found ;
               qty3 = 0 ;
               qty4 = 0 ;
               select sum(coalesce(product_uom_qty,0)) into qty3 from stock_move where picking_id=picking_rec.id and product_id=prodid ;
               qty1 = qty1 + qty3 ;
               select sum(coalesce(done_qty,0)) into qty4 from stock_move_line where picking_id=picking_rec.id and product_id=prodid ;
               qty2 = qty2 + qty4 ;
             end loop ;
             close picking_cur ;
           end loop ;
           close pur_cur ;
           myres = qty1 - qty2 ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists shippingreport(mypartnerid int) cascade""")
        self.env.cr.execute("""create or replace function shippingreport(mypartnerid int) returns varchar as $BODY$
          DECLARE
            myres varchar ;
          BEGIN
            if mypartnerid = 0 then
               select max(report_no) into myres from stock_picking ;
            else
               select max(report_no) into myres from stock_picking where partner_id=mypartnerid ;
            end if ;
            if myres is null then
               myres = ' ' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprodpo(prodid int) cascade""")
        self._cr.execute("""create or replace function getprodpo(prodid int) returns setof int as $BODY$
         DECLARE
           myres int ;
           po_cur refcursor ;
           po_rec record ;
         BEGIN
           open po_cur for select id,active,order_date from alldo_gh_iot_po_wkorder where active=True and product_no=prodid
              order by order_date desc ;
           loop
             fetch po_cur into po_rec ;
             exit when not found ;
             return next po_rec.id ;
           end loop ;
           close po_cur ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists autoarchwkorder() cascade""")
        self._cr.execute("""create or replace function autoarchwkorder() returns void as $BODY$
          DECLARE
            archivedate date ;
          BEGIN
            select (current_timestamp::DATE - interval '1 days')::DATE into archivedate ;
            update alldo_gh_iot_workorder set active=False where eng_order='4' and create_date::DATE <= archivedate::DATE and active=True ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkpowkorder(pickingid int) cascade""")
        self._cr.execute("""create or replace function checkpowkorder(pickingid int) returns void as $BODY$
          DECLARE
            myorigin varchar ;
            mypicktypeid int ;
            ncount int ;
            poid int ;
          BEGIN
            select picking_type_id into mypicktypeid from stock_picking where id = pickingid ;
            if mypicktypeid = 1 then
               select coalesce(origin,' ') into myorigin from stock_picking where id = pickingid ;
               select count(*) into ncount from purchase_order where name = myorigin ;
               if ncount > 0 then
                  select id into poid from purchase_order where name = myorigin ;
                  execute genpowkorderdata(poid) ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")



        self._cr.execute("""create or replace function change_po_qty_received() returns trigger as $BODY$
            DECLARE
              ncount int ;
              qty1 float ;
              qty2 float ;
              iscomplete Boolean ;
            BEGIN
                select count(*) into ncount from alldo_gh_iot_po_wkorder where product_no=NEW.product_id and id = NEW.po_wkorder_id ;
                if OLD.qty_received <> NEW.qty_received then
                   /* if NEW.po_wkorder_id is not null and ncount > 0  then
                      update alldo_gh_iot_po_wkorder set stockin_blank=True,stockin_blank_num=NEW.qty_received where id = NEW.po_wkorder_id ;  
                   end if ; */  
                   execute checkpurcomplete(OLD.order_id) ;
                end if ;
                return NEW ;
            END;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists po_line_qty_received_change on purchase_order_line;""")
        self._cr.execute("""create trigger po_line_qty_received_change after update on purchase_order_line
                   for each row execute procedure change_po_qty_received();""")

        self._cr.execute("""create or replace function change_purchase_stockloc() returns trigger as $BODY$
          DECLARE
            poname varchar ;
            pickingid int ;
            prodlocid int ;
            mv_cur refcursor ;
            mv_rec record ;
          BEGIN
            if NEW.state <> OLD.state and NEW.state='purchase' then
               select name into poname from purchase_order where id = OLD.id ;
               select id into pickingid from stock_picking where origin=poname ;
               if pickingid is not null then
                  update stock_picking set location_id=4 where id = pickingid ;
               end if ;   
               if OLD.change_prodloc = True and pickingid is not null then    
                 select max(prod_loc) into prodlocid from alldo_gh_iot_company_stockloc ;
                 if prodlocid > 0 then
                    update stock_picking set location_dest_id=prodlocid where id = pickingid ;
                    update stock_move set location_dest_id=prodlocid where picking_id = pickingid ;
                 end if ;
               end if ; 
            end if ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists purchase_inloc_change on purchase_order;""")
        self._cr.execute("""create trigger purchase_inloc_change after update on purchase_order
                          for each row execute procedure change_purchase_stockloc();""")

        self._cr.execute("""update purchase_order set stockin_state='1' where stockin_state is null""")

        self._cr.execute("""drop function if exists checkpurcomplete(pid int) cascade""")
        self._cr.execute("""create or replace function checkpurcomplete(pid int) returns void as $BODY$
         DECLARE
           myres Boolean ;
           ncount int ;
           purno varchar ;
           mv_cur refcursor ;
           mv_rec record ;
         BEGIN
           select count(*) into ncount from purchase_order_line where order_id=pid and product_qty != qty_received ;
           if ncount > 0 then
              update purchase_order set stockin_state='2' where id = pid ;
           else
              update purchase_order set stockin_state='3' where id = pid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getblankbycus(cusid int) cascade""")
        self._cr.execute("""create or replace function getblankbycus(cusid int) returns setof int as $BODY$
         DECLARE
          p_cur refcursor ;
          p_rec record ;
          prodid int ;
         BEGIN
           if cusid=35 then
              open p_cur for select id from product_template where cus_no=cusid ;
           else
              open p_cur for select id from product_template where cus_no=cusid and is_blank=True ;
           end if ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select id into prodid from product_product where product_tmpl_id = p_rec.id ;
             return next prodid ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkequipment2(startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genwkequipment2(startdate date,enddate date) returns void as $BODY$
          DECLARE
            totmach int ;
            ncount int ;
            ncount1 int ;
            ncount2 int ;
            nweek int ;
            time1 varchar ;
            time2 varchar ;
            time3 varchar ;
            time4 varchar ;
            time5 varchar ;
            time6 varchar ;
            mydate date ;
            mydt1 timestamp ;
            mydt2 timestamp ;
            mydt3 timestamp ;
            mydt4 timestamp ;
            mydt5 timestamp ;
            mydt6 timestamp ;
            per float ;
            per1 float ;
            per2 float ;
            avg float ;
            avg1 float ;
            avg2 float ;
            per_avg float ;
            per_avg1 float ;
            per_avg2 float ;
          BEGIN
            select count(*) into totmach from maintenance_equipment where category_id in (1,2,3) and active=True ;
            time1 = ' 08:00:00' ;
            time2 = ' 17:00:00' ;
            time3 = ' 16:30:00' ;
            time4 = ' 24:00:00' ;
            time5 = ' 00:30:00' ;
            time6 = ' 09:00:00' ;
            delete from alldo_gh_iot_workorder_performance_list2 ;
            mydate = startdate ;
            loop
              exit when mydate > enddate ;
              select (extract(DOW FROM cast(mydate as DATE)))::INT into nweek ;
              select concat(mydate,time1)::timestamp into mydt1 ;
              select concat(mydate,time2)::timestamp into mydt2 ;
              select concat(mydate,time3)::timestamp into mydt3 ;
              select concat(mydate,time4)::timestamp into mydt4 ;
              select concat(mydate,time5)::timestamp into mydt5 ;
              select concat(mydate,time6)::timestamp into mydt6 ;
              select count(distinct iot_id) into ncount from alldo_gh_iot_equipment_iot_data where 
                (iot_datetime + interval '8 hours') >= mydt1 and (iot_datetime + interval '8 hours') <= mydt2 and iot_num=0 ;
              select count(distinct iot_id) into ncount1 from alldo_gh_iot_equipment_iot_data where 
                (iot_datetime + interval '8 hours') >= mydt3 and (iot_datetime + interval '8 hours') <= mydt4 and iot_num=0 ;  
              select count(distinct iot_id) into ncount2 from alldo_gh_iot_equipment_iot_data where 
                (iot_datetime + interval '8 hours') >= mydt5 and (iot_datetime + interval '8 hours') <= mydt6 and iot_num=0 ; 
                if coalesce(totmach,0)=0 then
                   per = 0.0 ;
                   per1 = 0.0 ;
                   per2 = 0.0 ;
                else
                   per = round((coalesce(ncount,0)::numeric/totmach::numeric),2) * 100 ;
                   per1 = round((coalesce(ncount1,0)::numeric/totmach::numeric),2) * 100 ;
                   per2 = round((coalesce(ncount2,0)::numeric/totmach::numeric),2) * 100 ;
                end if ;
               if nweek != 0 or nweek != 6 then  
                  insert into alldo_gh_iot_workorder_performance_list2(iot_date,iot_week,timesheet1,timesheet2,timesheet3,timesheet1_per,timesheet2_per,timesheet3_per) values
                      (mydate::TEXT,nweek,coalesce(ncount,0),coalesce(ncount1,0),coalesce(ncount2,0),per,per1,per2) ;   
               end if ;
               mydate = mydate + interval '1 days' ;
            end loop ;
            select avg(timesheet1),avg(timesheet2),avg(timesheet3),avg(timesheet1_per),avg(timesheet2_per),avg(timesheet3_per) 
               into avg,avg1,avg2,per_avg,per_avg1,per_avg2 from alldo_gh_iot_workorder_performance_list2 ;
             insert into alldo_gh_iot_workorder_performance_list2(iot_date,timesheet1,timesheet2,timesheet3,timesheet1_per,timesheet2_per,timesheet3_per) values
              ('總平均',avg,avg1,avg2,per_avg,per_avg1,per_avg2) ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getoldesc(olid int) cascade""")
        self._cr.execute("""create or replace function getoldesc(olid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           oid int ;
           minid int ;
           ncount int ;
         BEGIN
           select order_id into oid from purchase_order_line where id = olid ;
           select min(id) into minid from purchase_order_line where id > olid and order_id=oid ;
           select count(*) into ncount from purchase_order_line where id=minid and product_id is null ;
           if ncount > 0 then
              select coalesce(name,' ') into myres from purchase_order_line where id=minid and product_id is null ;
           else
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")





        # self.env.cr.execute("""drop index if exists equipment_iotdata_index1 cascade""")
        # self.env.cr.execute("""create index equipment_iotdata_index1 on alldo_gh_iot_equipment_iot_data(iot_serial)""")

        # self.env.cr.execute("""drop index if exists equipment_iotdata_index2 cascade""")
        # self.env.cr.execute("""create index equipment_iotdata_index2 on alldo_gh_iot_equipment_iot_data(iot_id,iot_workorder,iot_datetime)""")

        # self.env.cr.execute("""drop index if exists iot_workorder_index1 cascade""")
        # self.env.cr.execute("""create index iot_workorder_index1 on alldo_gh_iot_workorder(name)""")
        # self.env.cr.execute("""drop index if exists iot_workorder_index3 cascade""")
        # self.env.cr.execute("""create index iot_workorder_index3 on alldo_gh_iot_workorder(mo_group_id)""")
        # self.env.cr.execute("""drop index if exists iot_workorder_index2 cascade""")
        # self.env.cr.execute("""create index iot_workorder_index2 on alldo_gh_iot_workorder(name,state)""")
        # self.env.cr.execute("""drop index if exists maintenance_equipment_index1 cascade""")
        # self.env.cr.execute("""create index maintenance_equipment_index1 on maintenance_equipment(equipment_no)""")
        # self.env.cr.execute("""drop index if exists maintenance_equipment_index2 cascade""")
        # self.env.cr.execute("""create index maintenance_equipment_index2 on maintenance_equipment(iot_ip)""")
        # self.env.cr.execute("""drop index if exists hr_employee_index1 cascade""")
        # self.env.cr.execute("""create index hr_employee_index1 on hr_employee(emp_code)""")
        # self.env.cr.execute("""drop index if exists workorder_lastwork_index1 cascade""")
        # self.env.cr.execute("""create index workorder_lastwork_index1 on alldo_gh_iot_workorder_lastwork(work_datetime)""")
        # self.env.cr.execute("""drop index if exists node_status_index1 cascade""")
        # self.env.cr.execute("""create index node_status_index1 on alldo_gh_iot_node_change_status(node_datetime)""")
        # self.env.cr.execute("""drop index if exists emp_attendance_index1 cascade""")
        # self.env.cr.execute("""create index emp_attendance_index1 on alldo_gh_iot_emp_attendance(attendance_id,attendance_date,attendance_type) """)
        # self.env.cr.execute("""drop index if exists qcdate_index cascade""")
        # self.env.cr.execute("""create index qcdate_index on alldo_gh_iot_workorder_qc(qc_date)""")
        # self.env.cr.execute("""drop index if exists iotowner1_index cascade""")
        # self.env.cr.execute("""create index iotowner1_index on alldo_gh_iot_workorder_qc(iot_owner1)""")
        # self.env.cr.execute("""drop index if exists iotdata1_index cascade""")
        # self.env.cr.execute("""create index iotdata1_index on alldo_gh_iot_workorder_iot_data(iot_owner)""")
        # self.env.cr.execute("""drop index if exists iotdata2_index cascade""")
        # self.env.cr.execute("""create index iotdata2_index on alldo_gh_iot_workorder_iot_data(iot_date)""")
        # self.env.cr.execute("""update res_partner set active=False where id=40""")
        # self.env.cr.execute("""update res_partner set active=True where id=34""")
        # self.env.cr.execute("""update alldo_gh_iot_po_wkorder set cus_name=34 where cus_name=40""")
        # self.env.cr.execute("""update alldo_gh_iot_workorder set cus_name=34 where cus_name=40""")
        # self.env.cr.execute("""update alldo_gh_iot_workorder_qc set cus_name=34 where cus_name=40""")
        # self.env.cr.execute("""update alldo_gh_iot_partner_prodin set partner_id=34 where partner_id=40""")
        # self.env.cr.execute("""update stock_picking set partner_id=34 where partner_id=40""")


