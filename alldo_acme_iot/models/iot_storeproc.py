# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError


class alldoiotstoreproc(models.Model):
    _name = "alldo_acme_iot.storeproc"

    @api.model
    def init(self):
        # return 'E'=> 員工 ; 'W' => 工單號 ; 'N' => Nothin  'X' => 故障  'Y' => 換線   'Z' => 機台復歸
        self.env.cr.execute("""drop function if exists getcodetype(mycode varchar,iotnode varchar) cascade""")
        self.env.cr.execute("""create or replace function getcodetype(mycode varchar,iotnode varchar) returns char as $BODY$
         DECLARE
           myres char ;
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           equipstatusid int ; 
           ncountq int ;
           equipid int ;
           mynowdatetime timestamp ;
           outofforderid int ;
           mymaxid int ;
           mystatustype char ;
           islotno Boolean ;
           isproductno Boolean ;
         BEGIN
           select id into equipid from maintenance_equipment where equipment_no = iotnode ;   
           if mycode in ('CAST_PREP','CAST_LOAD','CAST_BAKE') then 
              myres = 'Y' ;     /* 換線,烘模 */
           elsif mycode = 'CAST_END' then
              myres = 'Z' ;     /* 復歸 */ 
           elsif upper(substring(mycode,1,7)) = 'FURNACE' then
              myres = 'F' ;     /* 熔爐 */   
           else
               select count(*) into ncount from hr_employee where emp_code = mycode ;
               if ncount > 0 then     /* 員工代碼 return 'E' */
                  myres = 'E' ;
               else
                  select count(*) into ncount1 from alldo_acme_iot_workorder where name = mycode  ;
                  if ncount1 > 0 then   /*  工單號碼 return 'W' */    
                     myres = 'W' ;
                  else
                     select getislotno(mycode) into islotno ;
                     if islotno = True then
                        myres = 'L' ;      /* 批次號 */
                     else
                        select getisprodno(mycode) into isproductno ;
                        if isproductno = True then
                            myres = 'P' ;     /*  物料料號  */
                        else    
                            myres = 'N' ;     /*  都不是 return 'N' */ 
                        end if ;    
                     end if ;
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
                select max(id) into mymaxid from alldo_acme_iot_equipment_outofforder_status where 
                   iot_id=equipid ;
                update alldo_acme_iot_equipment_outofforder_status set end_datetime=mynowdatetime,write_date=mynowdatetime where 
                   id = mymaxid and end_datetime is null ;      
             end if ;
          END;$BODY$
          LANGUAGE plpgsql ;""")

        self.env.cr.execute(
            """drop function if exists genworkorderqcline(workorderid int,qcdate date,iotnode int,prodnum float,iotowner int) cascade""")
        self.env.cr.execute("""create or replace function genworkorderqcline(workorderid int,qcdate date,iotnode int,prodnum float,iotowner int) returns void as $BODY$ 
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
             prodid int ;
           BEGIN
            select current_timestamp into mynowdatetime ;
            select product_no into prodid from alldo_acme_iot_workorder where id = workorderid ;
             select count(*) into ncount from alldo_acme_iot_workorder_qc where order_id=workorderid and qc_date::DATE=qcdate::DATE and iot_node=iotnode ;
             if ncount > 0 then
                update alldo_acme_iot_workorder_qc set qc_good_num = coalesce(qc_good_num,0) + prodnum,iot_owner1=iotowner,write_date=mynowdatetime,
                product_no=prodid  where order_id=workorderid and qc_date::DATE=qcdate::DATE and iot_node=iotnode ;
             else  
                insert into alldo_acme_iot_workorder_qc(order_id,qc_date,iot_node,qc_good_num,iot_owner1,create_date,product_no) values
                  (workorderid,qcdate::DATE,iotnode,prodnum,iotowner,mynowdatetime,prodid) ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;
        """)

        # iotstate => '1' 代表啟動   '2' 代表開工   '3' 代表暫停  '4' 代表停止
        self.env.cr.execute(
            """drop function if exists setiotstatus(workorder varchar,iotnode varchar,iotstate char) cascade""")
        self.env.cr.execute("""create or replace function setiotstatus(workorder varchar,iotnode varchar,iotstate char) returns void as $BODY$
          DECLARE
            ncount int ;
            iotnodeid int ;
            mynowdatetime timestamp ;
            myworkorderid int ;
            mylastid int ;
          BEGIN
            if workorder != 'ALLDO' and iotstate != '1' then
               select id into myworkorderid from alldo_acme_iot_workorder where name = workorder ; 
            else
               myworkorderid = 0 ;   
            end if ;   
            select id into iotnodeid from maintenance_equipment where equipment_no = iotnode ;
            select current_timestamp into mynowdatetime ; 
            if iotnodeid is not null and myworkorderid is not null then  
               update maintenance_equipment set iot_status=iotstate where id = iotnodeid ;
               if myworkorderid > 0 then
                   insert into alldo_acme_iot_equipment_iot_status (iot_id,iot_datetime,iot_workorder,iot_status,create_date) values
                    (iotnodeid,mynowdatetime,myworkorderid,iotstate,mynowdatetime) ;
                   insert into alldo_acme_iot_node_change_status (order_id,node_status,iot_node,node_datetime,create_date) values 
                     (myworkorderid,iotstate,iotnodeid,mynowdatetime,mynowdatetime) ; 
               end if ;      
            end if ;
            if iotstate='2' or iotstate='3' then
               update maintenance_equipment set mo_no=myworkorderid where id = iotnodeid ;
               if iotstate='2' then
                  execute ckoutoffstatus(iotnode) ; 
                  execute runcnccompleteline(iotnode,workorder) ;
               end if ;
            else
               update maintenance_equipment set write_date=mynowdatetime where id = iotnodeid ;  
            end if ;
            if iotstate='2' and myworkorderid is not null and iotnodeid is not null then
                select id into mylastid from alldo_acme_iot_workorder_lastwork where work_datetime::DATE = mynowdatetime::DATE and 
                   equipment_id=iotnodeid and workorder_id=myworkorderid ;
                if mylastid is not null then
                   update alldo_acme_iot_workorder_lastwork set work_datetime = mynowdatetime,write_date=mynowdatetime where id = mylastid ;
                else
                   insert into alldo_acme_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date) values 
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

        self.env.cr.execute(
            """drop function if exists geniotdata(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar)""")
        self.env.cr.execute("""create or replace function geniotdata(nodename varchar,workorderno varchar,empno varchar,prodnum float,iotserial varchar) returns void 
           as $BODY$
           DECLARE
              myworkorderid int;
              mynodeid int ;
              myempid int ;
              myempid1 int ;
              myempid2 int ;
              mynowdatetime timestamp ;
              mylastworktime timestamp ;
              iotdurmin float ;
              iotdurhour float ;
              iotdurday float ;
              iotdurmin1 float ;
              mylastid int ;
              ncount int ;
              mymoldcavity int ;
              mymaxid int ;
              prodid int ;
              prodtmplid int ;
              mymoldwkman int ;
           BEGIN
              /*   確認 geniotdata 是否有重複    */
              select count(*) into ncount from alldo_acme_iot_equipment_iot_data where iot_serial=iotserial ;
              select current_timestamp into mynowdatetime ;
              select getmomoldcavity(workorderno) into mymoldcavity ;
              select getmomoldwkman(workorderno) into mymoldwkman ;
              prodnum = (prodnum * mymoldcavity) ;
              if ncount = 0 then
                  select id into myworkorderid from alldo_acme_iot_workorder where name = workorderno ;
                  select id into mynodeid from maintenance_equipment where equipment_no = nodename ;
                  select id into myempid from hr_employee where emp_code = empno ;   
                  select work_datetime,id into mylastworktime,mylastid from alldo_acme_iot_workorder_lastwork where work_datetime::DATE = mynowdatetime::DATE
                    and equipment_id=mynodeid and workorder_id=myworkorderid ;
                  if mymoldwkman > 1 then
                      select id into myworkorderid from alldo_acme_iot_workorder where name = workorderno ;
                      select max(id) into mymaxid from alldo_acme_iot_workorder_lastwork where 
                        equipment_id=mynodeid and workorder_id=myworkorderid ;
                      select iot_owner,iot_owner1 into myempid1,myempid2 from alldo_acme_iot_workorder_lastwork where 
                        id = mymaxid ;
                  end if ;      
                  
                  if mylastworktime is not null then  
                      select extract(minute from (select age(mynowdatetime,mylastworktime))) into iotdurmin ;
                      select extract(hours from (select age(mynowdatetime,mylastworktime))) into iotdurhour ;  
                      select extract(days from (select age(mynowdatetime,mylastworktime))) into iotdurday ;
                      iotdurmin1 = iotdurmin + (iotdurhour * 60) + (iotdurday * 24 * 60) ;
                      update alldo_acme_iot_workorder_lastwork set work_datetime=mynowdatetime,write_date=mynowdatetime where id = mylastid ;
                  else
                      iotdurmin1 = 0 ;
                      if mymoldwkman > 1 then
                         insert into alldo_acme_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date,iot_owner,iot_owner1) values (mynowdatetime,mynodeid,myworkorderid,mynowdatetime,myempid1,myempid2) ;
                      else
                         insert into alldo_acme_iot_workorder_lastwork (work_datetime,equipment_id,workorder_id,create_date) values (mynowdatetime,mynodeid,myworkorderid,mynowdatetime) ;
                      end if ;   
                  end if ;    
                  if myworkorderid is not null and mynodeid is not null and myempid is not null then  
                     if mymoldwkman > 1 then
                        insert into alldo_acme_iot_workorder_iot_data(order_id,iot_date,iot_node,iot_owner,iot_owner1,iot_num,iot_duration,iot_serial,create_date) values
                           (myworkorderid,mynowdatetime,mynodeid,myempid1,myempid2,prodnum,iotdurmin1,iotserial,mynowdatetime) ;
                        insert into alldo_acme_iot_equipment_iot_data(iot_id,iot_datetime,iot_owner,iot_owner1,iot_workorder,iot_num,iot_serial,create_date) values
                            (mynodeid,mynowdatetime,myempid1,myempid2,myworkorderid,prodnum,iotserial,mynowdatetime) ;
                     else
                        insert into alldo_acme_iot_workorder_iot_data(order_id,iot_date,iot_node,iot_owner,iot_num,iot_duration,iot_serial,create_date) values
                           (myworkorderid,mynowdatetime,mynodeid,myempid,prodnum,iotdurmin1,iotserial,mynowdatetime) ;
                        
                        insert into alldo_acme_iot_equipment_iot_data(iot_id,iot_datetime,iot_owner,iot_workorder,iot_num,iot_serial,create_date) values
                            (mynodeid,mynowdatetime,myempid,myworkorderid,prodnum,iotserial,mynowdatetime) ;
                     end if ; 
                     update alldo_acme_iot_workorder set prod_duration=coalesce(prod_duration,0)+iotdurmin1,prod_num=coalesce(prod_num,0)+prodnum,write_date=mynowdatetime 
                         where id = myworkorderid ;
                     update alldo_acme_iot_workorder set prod_date=mynowdatetime,state='3' where id = myworkorderid ;
                     update maintenance_equipment set iot_status='2',write_date=mynowdatetime where id = mynodeid ;
                     update maintenance_equipment set iot_start_datetime=mynowdatetime where iot_start_datetime is null and id = mynodeid ;  
                     execute genworkorderqcline(myworkorderid,mynowdatetime::DATE,mynodeid,prodnum,myempid) ;
                     execute wkorderwip(myworkorderid,prodnum) ;
                     execute genpowkorder(myworkorderid,prodnum) ;
                     execute genmoldtimes(myworkorderid) ;   /* 模具使用次數加 1  */
                     execute genwkngratio(myworkorderid) ;
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
             select count(*) into myres from maintenance_equipment where category_id=2 ;
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
                select iot_workorder into mywkorderid from alldo_acme_iot_equipment_iot_status where 
                id = (select max(id) from alldo_acme_iot_equipment_iot_status where iot_id=myequipid and iot_datetime::DATE = now()::DATE)  ;
                select name,product_no,eng_type into myname,myprodid,myengtype from alldo_acme_iot_workorder where id = mywkorderid ;
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
             select order_num into myres from alldo_acme_iot_workorder where name=mywkorderno ;
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
             select order_num into myres from alldo_acme_iot_workorder where name=mywkorderno ;
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
             open ins_cur for select eng_type from alldo_acme_iot_workorder_inspect where product_id=myprodid ;
             loop
                fetch ins_cur into ins_rec ;
                exit when not found ;
                select count(*) into ncount from alldo_acme_iot_eng_order AA where TRIM(AA.eng_type) like TRIM(ins_rec.eng_type) and
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
             update alldo_acme_iot_workorder set state='4',write_date=mynowdatetime where id = wkorderid ;
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
             select count(*) into wkloop from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and node_status in ('2','3') ;
             if wkloop > 0 then  
                 stopflag := False ;
                 open wk_cur for select * from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
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
                 update alldo_acme_iot_workorder set stop_duration=mywkstopdur where id = mywkorderid ;
             end if ;   
             /* 分機台計算 */
             select count(*) into wkloop from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and iot_node=mynodeid and node_status in ('2','3') ;
             if wkloop > 0 then  
                 stopflag := False ;
                 open wk_cur for select * from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
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
             select count(*) into wkloop from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and node_status = '1' ;
             if wkloop > 0 then  
                 startflag := False ;
                 open wk_cur for select * from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
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
                 update alldo_acme_iot_workorder set start_duration=mywkstartdur where id = mywkorderid ;
             end if ;   
             /* 分機台計算 */
             select count(*) into wkloop from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
                 order_id = mywkorderid and iot_node=mynodeid and node_status='1' ;
             if wkloop > 0 then  
                 startflag := False ;
                 open wk_cur for select * from alldo_acme_iot_node_change_status where node_datetime::DATE = mynowdatetime::DATE and
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
             delete from alldo_acme_iot_wkorder_selectitem ;
             select current_timestamp into mynowdatetime ;
             insert into alldo_acme_iot_wkorder_selectitem(report_owner,report_date,create_date) values (myuid,mynowdatetime::DATE,mynowdatetime) ;
             select max(id) into myid from alldo_acme_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_acme_iot_workorder where state='1' ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_acme_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               insert into alldo_acme_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,create_date) values
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
             delete from alldo_acme_iot_wkorder_selectitem ;
             select current_timestamp into mynowdatetime ;
             insert into alldo_acme_iot_wkorder_selectitem(report_owner,report_date,create_date) values (myuid,mynowdatetime::DATE,mynowdatetime) ;
             select max(id) into myid from alldo_acme_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_acme_iot_workorder where id in (select wkorder_id from alldo_workorder_newreport_rel where wizard_id = mywizid) ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               select coalesce(cnc_prog,' ') into cncprog from alldo_acme_iot_eng_order where prod_id=myprodtmplid and TRIM(eng_type) like TRIM(wk_rec.eng_type) ;
               insert into alldo_acme_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,cnc_prog,po_no,order_num,blank_num,shipping_date,create_date) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,cncprog,wk_rec.po_no,wk_rec.order_num,wk_rec.blank_num,wk_rec.shipping_date,mynowdatetime) ; 
             end loop ;
             close wk_cur ;
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
           BEGIN
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
               select iot_workorder into wkorderid from alldo_acme_iot_equipment_iot_data where 
                   id = (select max(id) from alldo_acme_iot_equipment_iot_data where iot_id=iot_rec.id);
               select name,product_no,order_num,eng_type into wkorder,prodid,ordernum,engtype from alldo_acme_iot_workorder where id = wkorderid ;   
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select name into prodname from product_template where id = prodtmplid ;
               if prodname is null then
                  prodname = ' ' ;
               end if ;
               /* wkorder = concat(wkorder,'-',prodname) ; */
               select sum(iot_num) into prodnum from alldo_acme_iot_equipment_iot_data where iot_id=iot_rec.id and iot_workorder=wkorderid ;
               select sum(iot_num) into tprodnum from alldo_acme_iot_equipment_iot_data where iot_id=iot_rec.id and iot_workorder=wkorderid 
                 and iot_datetime::DATE = now()::DATE ;
               nodestatus = 'OK' ;  
               /*   計算開工時間 及 停機時間   */
               execute genstartduration(wkorderid,iot_rec.id) ;
               execute genstopduration(wkorderid,iot_rec.id) ;
               /* **********************   */ 
               opentime = coalesce(iot_rec.start_duration,0) - coalesce(iot_rec.stop_duration,0) ;
               select standard_num into standardnum from alldo_acme_iot_eng_order where prod_id=prodtmplid and TRIM(eng_type) like TRIM(engtype) ;
               select round((standardnum::INTEGER/60)*opentime::INTEGER,0) into stdminnum;
               myres := ARRAY[]::TEXT[] ;
               if iotstatus = '3' then
                  wkorder = null ;
                  ordernum = null ;
                  prodnum = null ;
                  stdminnum = null ;
                  tprodnum = null ;
                  nodestatus = null ;
               end if ;
               myres = array_append(myres,iot_rec.equipment_no::TEXT) ;
               myres = array_append(myres,iotstatus::TEXT) ;
               myres = array_append(myres,coalesce(wkorder::TEXT,'')) ;
               myres = array_append(myres,coalesce(ordernum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(prodnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(stdminnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(tprodnum::TEXT,'0')) ;
               myres = array_append(myres,coalesce(nodestatus::TEXT,'')) ; 
               myres = array_append(myres,coalesce(prodname::TEXT,'')) ;
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
             open eng_cur for select * from alldo_acme_iot_eng_order where prod_id = prodid  order by sequence,id;
             loop
               fetch eng_cur into eng_rec ;
               exit when not found ;
               update alldo_acme_iot_eng_order set eng_order=nitem,write_date=mynowdatetime where id = eng_rec.id ;
               nitem = nitem + 1 ;
             end loop ;
             close eng_cur ;
             delete from alldo_acme_iot_eng_order where (eng_type is null or eng_type=' ') and prod_id = prodid ;
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
           BEGIN
             select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
             select count(*) into myengcount from alldo_acme_iot_eng_order where prod_id = myprodtmplid ;
             select max(eng_order) into mymaxid from alldo_acme_iot_eng_order where prod_id = myprodtmplid ;
             select eng_order into myengorder from alldo_acme_iot_eng_order where prod_id= myprodtmplid and 
                TRIM(eng_type) like TRIM(engtype) ;
             if myengorder = 1 then
                if myengcount = 1 then
                   myres = '4' ;
                else   
                   myres = '1' ;
                end if ;   
             elsif myengorder = mymaxid then
                if myengcount = 1 then
                   myres = '4' ;
                else   
                   myres = '3' ;
                end if ;   
             else
                myres = '2' ;
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
            select max(eng_order) into mymaxid from alldo_acme_iot_eng_order where prod_id = myprodtmplid ;
            select eng_order into myres from alldo_acme_iot_eng_order where prod_id= myprodtmplid and 
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
           BEGIN
             select po_no,eng_seq,eng_order,product_no into mypono,engseq,engorder,prodid from alldo_acme_iot_workorder 
                    where id = wkorderid ;
             if engorder != '3' then
                select id into myres from alldo_acme_iot_workorder where po_no=mypono and product_no=prodid and eng_seq = engseq + 1 ;
             else
                myres := 0 ;
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
             select po_no,eng_seq,eng_order,product_no into mypono,engseq,engorder,prodid from alldo_acme_iot_workorder 
                    where id = wkorderid ;
             if engorder != '1' then
                select id into myres from alldo_acme_iot_workorder where po_no=mypono and product_no=prodid and eng_seq = engseq - 1 ;
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
             select is_outsourcing into myres from alldo_acme_iot_eng_order where prod_id = prodtmplid and eng_order=engseq ;
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
             mynowdatetime timestamp ;
             mynowdate date ;
           BEGIN
             /*  先處理自己工單 wkorder_prodin 的已使用來料 */
             select current_timestamp into mynowdatetime ;
             select mynowdatetime::DATE into mynowdate ;
             select id into myprodinid from alldo_acme_iot_wkorder_prodin where order_id = wkorderid and prodin_datetime::DATE = mynowdate;
             select name,product_no,eng_order,po_no,eng_seq into mywkorderno,myprodid,myengorder,mypono,myengseq from alldo_acme_iot_workorder 
                 where id = wkorderid ;
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;    
             if myprodinid is null then
                 if myengorder='1' then  /* 首工序 */
                    myinloc := mypono ;
                    myintype := '1' ;
                 else
                    select getlastwkorder(wkorderid) into mylastwkid ;
                    select name into myinloc from alldo_acme_iot_workorder where id = mylastwkid ;
                    myintype := '2' ;
                 end if ;
                 insert into alldo_acme_iot_wkorder_prodin(order_id,prodin_datetime,product_no,process_num,in_type,in_loc,create_date) values
                      (wkorderid,current_timestamp,myprodid,prodnum,myintype,myinloc,mynowdatetime) ;
             else
                 update alldo_acme_iot_wkorder_prodin set process_num = coalesce(process_num,0) + prodnum,write_date=mynowdatetime where id = myprodinid ;
             end if ;
             /*  處理 自己工單 的 wkorder_prodout 轉出加工料件 */
             select id into myprodoutid from alldo_acme_iot_wkorder_prodout where order_id = wkorderid and prodout_datetime::DATE = mynowdate ;
             if myprodoutid is null then
                if myengorder='3' then  /* 完工序 */
                    myoutloc := mypono ;
                    myouttype := '1' ;
                 else
                    select getnextwkorder(wkorderid) into mynextwkid ;
                    select name into myoutloc from alldo_acme_iot_workorder where id = mynextwkid ;
                    myouttype := '2' ;
                 end if ;
                insert into alldo_acme_iot_wkorder_prodout(order_id,prodout_datetime,product_no,out_type,out_good_num,out_loc,create_date) values
                  (wkorderid,current_timestamp,myprodid,myouttype,prodnum,myoutloc,mynowdatetime) ;
             else
                update alldo_acme_iot_wkorder_prodout set out_good_num = coalesce(out_good_num,0) + prodnum,write_date=mynowdatetime where id = myprodoutid ;
             end if ;
             execute genwkamountnum(wkorderid) ;
             /* 處理 下一工序 wkorder_prodin 轉入投料 */
             select ckisoutsourcing(myprodtmplid,myengseq+1) into isoutsourcing ;
             if myengorder != '3' and isoutsourcing = False then  /*  如果不是完工序且非委外加工單 即執行 */
                 select getnextwkorder(wkorderid) into mynextwkid ;
                 select id into myprodinid from alldo_acme_iot_wkorder_prodin where order_id = mynextwkid ;
                 if myprodoutid is null then
                   select getlastwkorder(wkorderid) into mylastwkid ;
                   select name into myinloc from alldo_acme_iot_workorder where id = mylastwkid ;
                   myintype := '2' ;
                   myinloc := mywkorderno ;
                    insert into alldo_acme_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_type,in_loc,create_date) values
                          (mynextwkid,current_timestamp,myprodid,prodnum,myintype,myinloc,mynowdatetime) ;
                 else
                    update alldo_acme_iot_wkorder_prodin set in_good_num = coalesce(in_good_num,0) + prodnum,write_date=mynowdatetime where id = myprodinid ;
                 end if ;
             end if ;    
             execute genwkamountnum(wkorderid) ;
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
             select order_id,iot_owner into mywkorderid,myempid from alldo_acme_iot_wkorder_iot_data where 
                     id = (select max(id) from alldo_acme_iot_workorder_iot_data where iot_node=nodeid) ;
             select coalesce(name,' ') into mywkordername from alldo_acme_iot_workorder where id = mywkorderid ;
             select coalesce(emp_code,' ') into myempcode from hr_employee where id = myempid ;        
             myres = concat(mywkordername,'-',myempcode) ;
             return myres ;  
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists createpowkorder(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function createpowkorder(wkorderid int) returns void as $BODY$
           DECLARE
             mypono varchar ;
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
             select po_no,so_no,cus_name,product_no,order_num,blank_num,eng_order,eng_seq,eng_type,shipping_date into 
                mypono,mysono,mycusno,myprodid,myponum,myblanknum,myengorder,myengseq,myengtype,myshipdate
                  from alldo_acme_iot_workorder where id = wkorderid ;
             select id into mypoid from alldo_acme_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             if mypoid is null then
                insert into alldo_acme_iot_po_wkorder(po_no,so_no,cus_name,product_no,po_num,blank_num,shipping_date,state,create_date) values 
                   (mypono,mysono,mycusno,myprodid,myponum,myblanknum,myshipdate,'1',mynowdatetime) ;
                select id into mypoid from alldo_acme_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             end if ;
             insert into alldo_acme_iot_po_wkorder_line(po_id,wkorder_id,eng_seq,eng_order,eng_type,create_date) values  
                 (mypoid,wkorderid,myengseq,myengorder,myengtype,mynowdatetime) ; 
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpowkorder(wkorderid int,prodnum float) cascade""")
        self.env.cr.execute("""create or replace function genpowkorder(wkorderid int,prodnum float) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ; 
             select count(*) into ncount from alldo_acme_iot_po_wkorder_line where wkorder_id=wkorderid ;
             if ncount > 0 then
                update alldo_acme_iot_po_wkorder_line set complete_num=coalesce(complete_num,0)+prodnum,write_date=mynowdatetime where wkorder_id=wkorderid ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpoprod(poid int) cascade""")
        self.env.cr.execute("""create or replace function getpoprod(poid int) returns int as $BODY$
            DECLARE
             ncount int ;
             myres int ;
           BEGIN
             select count(*) into ncount from alldo_acme_iot_po_wkorder where id=poid ;
             if ncount > 0 then
                select product_no into myres from alldo_acme_iot_po_wkorder where id=poid ;
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
             select (coalesce(complete_num,0) - coalesce(ng_num,0)) into myres from alldo_acme_iot_po_wkorder_line where po_id=poid
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
             myprodinnum float ;
             myamounttot float ;
             qc_cur refcursor ;
             qc_rec record ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into myngnum from alldo_acme_iot_workorder_qc
                where order_id=wkorderid ;
             update alldo_acme_iot_po_wkorder_line set ng_num=myngnum,write_date=mynowdatetime where wkorder_id=wkorderid ;  
             select sum(coalesce(qc_good_num,0) - coalesce(material_ng_num,0) - coalesce(processing_ng_num,0)) into myprodinnum from 
                 alldo_acme_iot_workorder_qc where order_id=wkorderid ;
             /* 切割工序GOOD數量 */    
             /*select sum(coalesce(out_good_num,0) - coalesce(out_ng_num,0)) into myprodinnum from alldo_acme_iot_wkorder_prodout where
                 order_id = wkorderid ;   */ 
             select sum(coalesce(qc_good_num,0)) into myamounttot from  alldo_acme_iot_workorder_qc where order_id=wkorderid ;   
             /* update alldo_acme_iot_workorder set prodin_num=myprodinnum,mo_production_num=myamounttot where id = wkorderid ; */
            
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
             myproductname varchar ;
             myprodblank varchar ;
             mynewrecid int ;
             nitem int := 1 ;
             myclamppower varchar ;
             mystandardnum int ;
             myinscode varchar ;
             workordermemo varchar ;
             prodblank1 int ;
           BEGIN
             delete from alldo_acme_iot_wkorder_printsheet ;
             open sel_cur for select * from alldo_acme_iot_wkorder_selectitem_line ;
             loop
               fetch sel_cur into sel_rec ;
               exit when not found ;
               select workorder_memo into workordermemo from alldo_acme_iot_workorder where name=sel_rec.name ;
               select product_tmpl_id into myprodtmplid from product_product where id = sel_rec.product_no ;
               select default_code,name,product_blank1 into myprodcode,myproductname,prodblank1 from product_template where id = myprodtmplid ;
               myprodcode = concat('[',myprodcode,']',myproductname) ;
               insert into alldo_acme_iot_wkorder_printsheet (name,product_no,cus_name,order_num,eng_type,shipping_date,
               workorder_memo,product_blank1) values (sel_rec.name,myprodcode,sel_rec.cus_name,sel_rec.order_num::NUMERIC,
               sel_rec.eng_type,sel_rec.shipping_date,workordermemo,prodblank1) ;
                 select max(id) into mynewrecid from alldo_acme_iot_wkorder_printsheet ;
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
           BEGIN
             /* delete from alldo_acme_iot_wkorder_selectitem ; */
             select current_timestamp  into mynowdatetime ; 
             insert into alldo_acme_iot_wkorder_selectitem(report_owner,report_date) values (myuid,mynowdatetime::DATE) ;
             select max(id) into myid from alldo_acme_iot_wkorder_selectitem ;
             open wk_cur for select * from alldo_acme_iot_workorder where id=mywkid ;
             loop
               fetch wk_cur into wk_rec ;
               exit when not found ;
               select product_tmpl_id into myprodtmplid from product_product where id = wk_rec.product_no ;
               insert into alldo_acme_iot_wkorder_selectitem_line(item_id,name,cus_name,product_no,eng_type,order_num,shipping_date,select_yn) values
                (myid,wk_rec.name,wk_rec.cus_name,wk_rec.product_no,wk_rec.eng_type,wk_rec.order_num,wk_rec.shipping_date,True) ; 
               select max(id) into mymaxid from  alldo_acme_iot_wkorder_selectitem_line ;
              
             end loop ;
             close wk_cur ;
             update alldo_acme_iot_workorder set state='2' where id=mywkid and state = '1' ;
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
             select id into myid from alldo_acme_iot_so_sequence where so_prefixcode=prefixcode and so_year=myyear ;
             if myid is null then
                myres = concat(prefixcode,myyear1,'001') ;
                insert into alldo_acme_iot_so_sequence(so_prefixcode,so_year,so_seq) values (prefixcode,myyear,2) ;
             else
                select coalesce(so_seq,0) into myseq from alldo_acme_iot_so_sequence where id = myid ;
                myres = concat(prefixcode,myyear1,LPAD((myseq+1)::TEXT,3,'0')) ;
                update alldo_acme_iot_so_sequence set so_seq=coalesce(so_seq,0) + 1 where id = myid;
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
             mypono varchar ;
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
             select po_no,so_no,cus_name,product_no,order_num,blank_num,eng_order,eng_seq,eng_type,shipping_date into 
                mypono,mysono,mycusno,myprodid,myponum,myblanknum,myengorder,myengseq,myengtype,myshipdate
                  from alldo_acme_iot_outsuborder where id = outsuborderid ;
             select id into mypoid from alldo_acme_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             if mypoid is null then
                insert into alldo_acme_iot_po_wkorder(po_no,so_no,cus_name,product_no,po_num,blank_num,shipping_date,state,create_date) values 
                   (mypono,mysono,mycusno,myprodid,myponum,myblanknum,myshipdate,'1',mynowdatetime) ;
                select id into mypoid from alldo_acme_iot_po_wkorder where TRIM(po_no)=TRIM(mypono) ;
             end if ;
             insert into alldo_acme_iot_po_suborder_line(po_id,outsourcing_id,eng_seq,eng_order,eng_type,create_date) values  
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
             update alldo_acme_iot_outsuborder set state='3',write_date=mynowdatetime where id = outsuborderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genpooutsuborderngnum(outsuborderid int) cascade""")
        self.env.cr.execute("""create or replace function genpooutsuborderngnum(outsuborderid int) returns void as $BODY$
           DECLARE
             myngnum float ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into myngnum from alldo_acme_iot_outsuborder_qc
                where order_id=outsuborderid ;
             update alldo_acme_iot_po_suborder_line set ng_num=myngnum,write_date=mynowdatetime where outsourcing_id=outsuborderid ;  
           END;$BODY$
           LANGUAGE plpgsql""")

        self.env.cr.execute(
            """drop function if exists genoutsourcingout(outid1 int ,outid int,outownerid int,outnum int) cascade""")
        self.env.cr.execute(
            """drop function if exists genoutsourcingout(outid1 int ,outid int,outownerid int,outnum int,datesupply date,datedue date) cascade""")
        self.env.cr.execute("""create or replace function genoutsourcingout(outid1 int,outid int,outownerid int,outnum int,datesupply date,datedue date) returns void as $BODY$
           DECLARE
              mynowdatetime timestamp ;
              myprodid int ;
              cusid int ;
              cusname varchar ;
           BEGIN
              if outid1 = 0 then
                 cusname = 'ACME供料' ;
              else   
                  select cus_name into cusid from  alldo_acme_iot_outsuborder where id=outid1 ;
                  select name into cusname from res_partner where id = cusid ;
              end if ;    
              select product_no into myprodid from alldo_acme_iot_outsuborder where id=outid ; 
              select current_timestamp into mynowdatetime ;
              insert into alldo_acme_iot_outsuborder_prodout(order_id,prodout_datetime,product_no,out_good_num,out_owner,create_date,out_loc,date_supply,date_due)
                 values (outid,mynowdatetime,myprodid,outnum,outownerid,mynowdatetime,cusname,datesupply,datedue) ;
              update alldo_acme_iot_outsuborder set blank_num=coalesce(blank_num,0) + outnum,state='2',write_date=mynowdatetime where id = outid ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists genoutsourcingin(suborderid int,suborderid1 int,inownerid int,ingoodnum int,inngnum int) cascade""")
        self.env.cr.execute(
            """drop function if exists genoutsourcingin(suborderid int,suborderid1 int,inownerid int,ingoodnum int,inngnum int,datedelivery date) cascade""")
        self.env.cr.execute("""create or replace function genoutsourcingin(suborderid int,suborderid1 int,inownerid int,ingoodnum int,inngnum int,datedelivery date) returns void as $BODY$
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
             mrpprodid int ;
             cusid int ;
             cusname varchar ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select product_no,so_no,eng_order,eng_seq,name,mrp_prod_id into myprodid,sono,myengorder,myengseq,myname,mrpprodid from alldo_acme_iot_outsuborder where id = suborderid ;
             if suborderid1=0 then
                cusname = '移轉回ACME入庫' ;
             else
                select cus_name into cusid from alldo_acme_iot_outsuborder where id = suborderid1;
                select name into cusname from res_partner where id = cusid ;
             end if ;   
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
             insert into alldo_acme_iot_outsuborder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_ng_num,in_owner,create_date,in_loc,date_delivery) values 
                 (suborderid,mynowdatetime,myprodid,ingoodnum,inngnum,inownerid,mynowdatetime,cusname,datedelivery) ;
             update alldo_acme_iot_outsuborder set prod_num=coalesce(prod_num,0)+ingoodnum+inngnum,write_date=mynowdatetime where id=suborderid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setpowkordercomplete(powkorderid int) cascade""")
        self.env.cr.execute("""create or replace function setpowkordercomplete(powkorderid int) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             update alldo_acme_iot_po_wkorder set state='3',write_date=mynowdatetime where id = powkorderid ;
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
             select max(eng_order) into maxengseq from alldo_acme_iot_eng_order where prod_id=myprodtmplid ;
             select is_outsourcing into isoutsourcing from alldo_acme_iot_eng_order where prod_id=myprodtmplid and
                 eng_order=maxengseq ; 
             if isoutsourcing = True then   /* 如果為委外加工    */
                select id into myoutsourcingid from alldo_acme_iot_outsuborder where so_no=sonoid and product_no=prodid
                  and eng_seq=maxengseq ;
                select sum(coalesce(in_good_num,0) - coalesce(in_stock_num,0)) into myres from alldo_acme_iot_outsuborder_prodin  
                   where order_id = myoutsourcingid ;
             else                           /* 如果為一般工單    */
                 select id into mywkorderid from alldo_acme_iot_workorder where so_no=sonoid and product_no=prodid
                     and eng_seq=maxengseq ; 
                 select sum(coalesce(out_good_num,0) - coalesce(out_stock_num,0)) into myres from alldo_acme_iot_wkorder_prodout                                where order_id = mywkorderid ;
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
            select max(eng_order) into maxengseq from alldo_acme_iot_eng_order where prod_id=myprodtmplid ;
            select is_outsourcing into isoutsourcing from alldo_acme_iot_eng_order where prod_id=myprodtmplid and
                eng_order=maxengseq ; 
            if isoutsourcing = True then   /* 如果為委外加工    */
               select name into myres from alldo_acme_iot_outsuborder where so_no=sonoid and product_no=prodid
                and eng_seq=maxengseq ; 
            else                           /* 如果為一般工單    */
                select name into myres from alldo_acme_iot_workorder where so_no=sonoid and product_no=prodid
                    and eng_seq=maxengseq ; 
            end if ;
            if myres is null then
               myres := ' ' ;
            end if ;
            return myres ;    
          END;$BODY$
          LANGUAGE plpgsql;
       """)

        self.env.cr.execute(
            """drop function if exists genblankstockin(sonoid int,prodid int,blanknum float,outowner int) cascade""")
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
             nowday date ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             select current_timestamp::DATE into nowday ;
             select name into myname from sale_order where id = sonoid ;
             select product_tmpl_id into myprodtmplid from product_product where id = prodid ;
             select is_outsourcing into isoutsourcing from alldo_acme_iot_eng_order where prod_id=myprodtmplid and eng_order=1 ;
             if isoutsourcing = True then     /* 第一工序為委外加工單 */
                select id into myoutsourcingid from alldo_acme_iot_outsuborder where so_no=sonoid and eng_seq=1 and
                   product_no=prodid ;
                insert into alldo_acme_iot_outsuborder_prodout(order_id,product_no,out_good_num,out_loc,out_owner,prodout_datetime,create_date,date_supply,date_due) values
                  (myoutsourcingid,prodid,blanknum,myname,outowner,mynowdatetime,mynowdatetime,nowday,nowday) ;   
                update alldo_acme_iot_outsuborder set blank_num=coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id =myoutsourcingid ;
                select blank_num into mynowblanknum from alldo_acme_iot_outsuborder where id = myoutsourcingid ;
                select id,product_uom_qty into mysalelineid,mysalenum from sale_order_line where order_id=sonoid 
                    and product_id=prodid ;
                if mynowblanknum > mysalenum then
                   update sale_order_line set product_uom_qty=mynowblanknum,write_date=mynowdatetime where id = mysalelineid ;
                   select id into mypickingid from stock_picking where origin=myname ;
                   update stock_move set product_uom_qty=mynowblanknum,write_date=mynowdatetime where picking_id=mypickingid and product_id=prodid ;
                end if ;
             else                             /* 第一工序為一般工單   */
                 select id into mywkorderid from alldo_acme_iot_workorder where so_no=sonoid and eng_seq=1 and
                   product_no=prodid ;    
                 insert into alldo_acme_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_loc,in_owner,in_type,create_date) values
                   (mywkorderid,mynowdatetime,prodid,blanknum,myname,outowner,'1',mynowdatetime) ; 
                 update alldo_acme_iot_workorder set blank_num = coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id = mywkorderid ;
                 select blank_num into mynowblanknum from alldo_acme_iot_workorder where id = mywkorderid ;
                 select id,product_uom_qty into mysalelineid,mysalenum from sale_order_line where order_id=sonoid 
                    and product_id=prodid ;
                 if mynowblanknum > mysalenum then
                   update alldo_acme_iot_workorder set order_num=mynowblanknum,write_date=mynowdatetime where id = mywkorderid ;
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
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno ;
             if myid is not null then
               insert into alldo_acme_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'1',mynowdatetime) ;
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
             ncount int ;
             mydate varchar ;
             mytime varchar ;
             mydutytime varchar ;
             myres varchar ;
             myname varchar ;
           BEGIN
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp  into mynowdatetime ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             mydutytime = concat(mydate,' ',mytime) ;
             select id,name into myid,myname from hr_employee where emp_code = empno ;
             if myid is not null then
               insert into alldo_acme_iot_emp_attendance (attendance_id,attendance_date,attendance_type,create_date) values (myid,mynowdatetime,'2',mynowdatetime) ;
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
             delete from alldo_acme_iot_empinfo ;
             insert into alldo_acme_iot_empinfo (empinfo_date) values (mynowdate) ;
             select max(id) into mymaxid1 from alldo_acme_iot_empinfo ;
             open emp_cur for select id,emp_code,name from hr_employee where id in 
               (select emp_id from alldo_acme_iot_empbarcode_rel where wizard_id=wizid)
               and active=true order by emp_code ;
             loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               if myitem = 1 then
                  insert into alldo_acme_iot_empbarcode (barcode_id,emp_code1,emp_name1) values (mymaxid1,emp_rec.emp_code,emp_rec.name) ;
                  select max(id) into mymaxid from alldo_acme_iot_empbarcode ;
               end if ;
               if myitem = 2 then
                  update alldo_acme_iot_empbarcode set emp_code2=emp_rec.emp_code,emp_name2=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 3 then
                  update alldo_acme_iot_empbarcode set emp_code3=emp_rec.emp_code,emp_name3=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 4 then
                  update alldo_acme_iot_empbarcode set emp_code4=emp_rec.emp_code,emp_name4=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 5 then
                  update alldo_acme_iot_empbarcode set emp_code5=emp_rec.emp_code,emp_name5=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 6 then
                  update alldo_acme_iot_empbarcode set emp_code6=emp_rec.emp_code,emp_name6=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 7 then
                  update alldo_acme_iot_empbarcode set emp_code7=emp_rec.emp_code,emp_name7=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 8 then
                  update alldo_acme_iot_empbarcode set emp_code8=emp_rec.emp_code,emp_name8=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 9 then
                  update alldo_acme_iot_empbarcode set emp_code9=emp_rec.emp_code,emp_name9=emp_rec.name where id = mymaxid ;
               end if ;
               if myitem = 10 then
                  update alldo_acme_iot_empbarcode set emp_code10=emp_rec.emp_code,emp_name10=emp_rec.name where id = mymaxid ;
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
             select print_num into myprintnum from alldo_acme_iot_equipstatus_barcode_wizard where id = wizid ;
             select now()::DATE into mynowdate ;
             delete from alldo_acme_iot_equipstatusinfo ;
             insert into alldo_acme_iot_equipstatusinfo(print_num,create_date) values (myprintnum,mynowdatetime) ;
             select max(id) into mymaxid1 from alldo_acme_iot_equipstatusinfo ;
             loop
                 exit when mynum > myprintnum ;
                 myitem = 1 ;
                 open equip_cur for select * from maintenance_equipment_status order by sequence,id ;
                 loop
                   fetch equip_cur into equip_rec ;
                   exit when not found ;
                   if myitem = 1 then
                      insert into alldo_acme_iot_equipstatusbarcode(barcode_id,status_code1,status_name1) values (mymaxid1,equip_rec.status_code,equip_rec.status_name) ;
                      select max(id) into mymaxid from alldo_acme_iot_equipstatusbarcode ;
                   end if ;
                   if myitem = 2 then
                      update alldo_acme_iot_equipstatusbarcode set status_code2=equip_rec.status_code,status_name2=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 3 then
                      update alldo_acme_iot_equipstatusbarcode set status_code3=equip_rec.status_code,status_name3=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 4 then
                      update alldo_acme_iot_equipstatusbarcode set status_code4=equip_rec.status_code,status_name4=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 5 then
                      update alldo_acme_iot_equipstatusbarcode set status_code5=equip_rec.status_code,status_name5=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 6 then
                      update alldo_acme_iot_equipstatusbarcode set status_code6=equip_rec.status_code,status_name6=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 7 then
                      update alldo_acme_iot_equipstatusbarcode set status_code7=equip_rec.status_code,status_name7=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 8 then
                      update alldo_acme_iot_equipstatusbarcode set status_code8=equip_rec.status_code,status_name8=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 9 then
                      update alldo_acme_iot_equipstatusbarcode set status_code9=equip_rec.status_code,status_name9=equip_rec.status_name where id = mymaxid ;
                   end if ;
                   if myitem = 10 then
                      update alldo_acme_iot_equipstatusbarcode set status_code10=equip_rec.status_code,status_name10=equip_rec.status_name where id = mymaxid ;
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
             moldid int ;
             myengtype varchar ;
             myres integer ;
           BEGIN
             select product_no,eng_type into myprodid,myengtype from alldo_acme_iot_workorder where name = mono ;
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
             select mold_id into moldid from alldo_acme_iot_product_mold where product_id = myprodtmplid and active = True ;
             if moldid is not null then
                select coalesce(mold_cavity,1) into myres from alldo_acme_iot_acme_mold where id = moldid ;
             else
                myres = 1 ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmomoldwkman(mono varchar) cascade""")
        self.env.cr.execute("""create or replace function getmomoldwkman(mono varchar) returns Integer as $BODY$
           DECLARE
             myprodid int ;
             myprodtmplid int ;
             moldid int ;
             myengtype varchar ;
             myres integer ;
           BEGIN
             select product_no,eng_type into myprodid,myengtype from alldo_acme_iot_workorder where name = mono ;
             select product_tmpl_id into myprodtmplid from product_product where id = myprodid ;
             select mold_id into moldid from alldo_acme_iot_product_mold where product_id = myprodtmplid and active = True ;
             if moldid is not null then
                select coalesce(work_man,1) into myres from alldo_acme_iot_acme_mold where id = moldid ;
             else
                myres = 1 ;
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
                select max(id) into mymaxid from alldo_acme_iot_workorder_lastwork where equipment_id = equipid and workorder_id is not null ;
                select workorder_id into myres from alldo_acme_iot_workorder_lastwork where id = mymaxid ;
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
            prodtmplid int ;
            prodid int ;
            moldid int ;
            workman int ;
            cworkman char ;
          BEGIN
            select id,mo_no into equipid,mylastmoid from maintenance_equipment where equipment_no = nodename ;
            select name,product_no into myres,prodid from alldo_acme_iot_workorder where id = mylastmoid ;
            if myres is null then
                select max(id) into mymaxid from alldo_acme_iot_workorder_lastwork where equipment_id = equipid and workorder_id is not null ;
                select workorder_id into mylastmoid from alldo_acme_iot_workorder_lastwork where id = mymaxid ;
                select name,product_no into myres,prodid from alldo_acme_iot_workorder where id = mylastmoid ;
            end if ;  
            select product_tmpl_id into prodtmplid from product_product where id = prodid ;
            select mold_id into moldid from product_template where id = prodtmplid ;
            select coalesce(work_man,1) into workman from alldo_acme_iot_acme_mold where id = moldid ;
            if workman is null then
               cworkman = '1' ;
            else
               cworkman = workman::TEXT ;
            end if ;
            if myres is null then
               myres = ' ' ;
            else
              myres = concat(myres,cworkman) ;   
            end if ; 
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists runcncreplaceline(nodename varchar,empno varchar,wkorder varchar) cascade""")
        self.env.cr.execute(
            """drop function if exists runcncreplaceline(nodename varchar,empno varchar,wkorder varchar,reptype varchar) cascade""")
        self.env.cr.execute("""create or replace function runcncreplaceline(nodename varchar,empno varchar,wkorder varchar,reptype varchar) returns void as $BODY$
           DECLARE
             ncount int ;
             mynowdatetime timestamp ;
             mynodeid int ;
             myempid int ;
             mywkorderid int ;
             ncount1 int ;
             statusid int ;
             typecode char ;
             prep_count int ;
             bake_count int ;
             load_count int ;
             myrepid int ;
           BEGIN
             if reptype='CAST_PREP' then   /* 備模 */
                typecode = 'P' ;
             elsif reptype='CAST_LOAD' then  /* 架模 */
                typecode = 'L' ;
             elsif reptype='CAST_BAKE' then  /* 烘模 */
                typecode = 'B' ;
             elsif reptype='CAST_END' then  /* 結束 */
                typecode = 'E' ;   
             end if ; 
             select id into mywkorderid from alldo_acme_iot_workorder where name=wkorder ;     
             select max(id) into statusid from maintenance_equipment_status where status_type='2' ;
             select current_timestamp  into mynowdatetime ;
             ncount = 0 ;
             if nodename is not null or nodename != '' then
                 select id into mynodeid from maintenance_equipment where equipment_no=nodename ;
                 update maintenance_equipment set mo_no=mywkorderid where id = mynodeid ;
                 if typecode='L' then
                    update maintenance_equipment set iot_status='1' where id = mynodeid ;
                 elsif typecode='B' then
                    update maintenance_equipment set iot_status='3' where id = mynodeid ; 
                 end if ;   
             end if ;    
             if empno is not null or empno != '' then
                 select id into myempid from hr_employee where emp_code=empno ;
                 update maintenance_equipment set iot_owner=myempid where id = mynodeid ;
             end if ;    
             if typecode='P' then
                select count(*) into prep_count from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='P' and order_id=mywkorderid ;
                if prep_count > 0 then
                   select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline  where replace_end_datetime is null and replace_type='P' and order_id=mywkorderid ;
                   update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid  ;
                   /* execute recalreplinetime(myrepid) ; */
                end if ;
                insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,replace_start_datetime,create_date,replace_type)
                     values (mywkorderid,myempid,mynowdatetime,mynowdatetime,typecode) ;
             elsif typecode='L' then
                 select count(*) into load_count from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and equipment_id=mynodeid and order_id=mywkorderid;
                if load_count > 0 then
                   select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and equipment_id=mynodeid and order_id=mywkorderid;
                   update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                   /* execute recalreplinetime(myrepid) ; */
                end if ;
                insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,equipment_id,replace_start_datetime,create_date,replace_type)
                  values (mywkorderid,myempid,mynodeid,mynowdatetime,mynowdatetime,typecode) ;
             elsif typecode='B' then
                select count(*) into bake_count from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='B' and order_id=mywkorderid and order_id=mywkorderid ;
                if bake_count > 0 then
                   select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='B' and equipment_id=mynodeid and order_id=mywkorderid;
                   update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                   /* execute recalreplinetime(myrepid) ; */
                end if ;
                insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,equipment_id,replace_start_datetime,create_date,replace_type)
                  values (mywkorderid,myempid,mynodeid,mynowdatetime,mynowdatetime,typecode) ;
             elsif typecode='E' then     
                if mywkorderid is not null then
                   update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where replace_end_datetime is null and order_id=mywkorderid ;
                end if ;   
             end if ;
           
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists runcnccompleteline(nodename varchar) cascade""")
        self.env.cr.execute("""drop function if exists runcnccompleteline(nodename varchar,wkorder varchar) cascade""")
        self.env.cr.execute("""create or replace function runcnccompleteline(nodename varchar,wkorder varchar) returns void as $BODY$
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
             mywkorderid1 int ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             if nodename is not null or nodename != '' then
                select id,mo_no into myequipid,mywkorderid from maintenance_equipment where equipment_no=nodename ;
                 select id,replace_start_datetime into myrepid,myrepstartdatetime from alldo_acme_iot_wkorder_replaceline where order_id=mywkorderid 
                 and replace_end_datetime is null;
             else
                 select id into mywkorderid from alldo_acme_iot_workorder where name = wkorder ;
                 select id,replace_start_datetime into myrepid,myrepstartdatetime from alldo_acme_iot_wkorder_replaceline where order_id=mywkorderid
                 and replace_end_datetime is null;   
             end if ;   
             
             if myrepid is not null then
                  select order_id into mywkorderid1 from alldo_acme_iot_wkorder_replaceline where id = myrepid ; 
                  select extract(minute from (select age(mynowdatetime,myrepstartdatetime))) into repdurmin ;
                  select extract(hours from (select age(mynowdatetime,myrepstartdatetime))) into repdurhour ;  
                  select extract(days from (select age(mynowdatetime,myrepstartdatetime))) into repdurday ;
                  repdurmin1 = repdurmin + (repdurhour * 60) + (repdurday * 24 * 60) ;
                  update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime,write_date=mynowdatetime,replace_duration=coalesce(repdurmin1,0) 
                   where id = myrepid ;
                  /* execute recalreplinetime(myrepid) ; */
                  if mywkorderid1 is null then 
                     insert into alldo_acme_iot_workorder_lastwork(work_datetime,equipment_id,workorder_id) values (mynowdatetime,myequipid,mywkorderid) ; 
                  else
                     insert into alldo_acme_iot_workorder_lastwork(work_datetime,equipment_id,workorder_id) values (mynowdatetime,myequipid,mywkorderid1) ;
                  end if ;   
             end if ;    
          
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genallreplinedur() cascade""")
        self.env.cr.execute("""create or replace function genallreplinedur() returns void as $BODY$
          DECLARE
            rep_cur refcursor ;
            rep_rec record ;
          BEGIN
            open rep_cur for select id from alldo_acme_iot_wkorder_replaceline where (complete_tag is null or complete_tag = False)
               and replace_end_datetime is not null ;
            loop
               fetch rep_cur into rep_rec ;
               exit when not found ;
               execute recalreplinetime(rep_rec.id) ; 
               update alldo_acme_iot_wkorder_replaceline set complete_tag=True where id = rep_rec.id  ;
            end loop ;
            close rep_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists recalreplinetime(repid int) cascade""")
        self.env.cr.execute("""create or replace function recalreplinetime(repid int) returns void as $BODY$
          DECLARE
            ncount int ;
            repdurmin int ;
            repdurhour int ;
            repdurday int ;
            repdurmin1 int ;
            myrepstartdatetime timestamp ;
            myrependdatetime timestamp ;
          BEGIN
            select replace_start_datetime,replace_end_datetime into myrepstartdatetime,myrependdatetime from alldo_acme_iot_wkorder_replaceline
                  where id = repid ;
            select extract(minute from (select age(myrependdatetime,myrepstartdatetime))) into repdurmin ;
            select extract(hours from (select age(myrependdatetime,myrepstartdatetime))) into repdurhour ;  
            select extract(days from (select age(myrependdatetime,myrepstartdatetime))) into repdurday ;
            repdurmin1 = repdurmin + (repdurhour * 60) + (repdurday * 24 * 60) ;
            update alldo_acme_iot_wkorder_replaceline set replace_duration=repdurmin1 where id = repid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists runcncstopline(cncerrcode varchar,empno varchar,nodename varchar) cascade""")
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
             select count(*) into ncount from alldo_acme_iot_equipment_outofforder_status where iot_id=myequipid and
                end_datetime is null ;
             if ncount = 0 and statusid is not null and myequipid is not null and myempid is not null then
                select getnodelastmoid(nodename) into mywkorderid ;
                insert into alldo_acme_iot_equipment_outofforder_status(iot_id,status_id,iot_workorder,start_datetime,outoff_owner,create_date) values
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
             open prod_cur for select id,cus_no from product_template where cus_no=partnerid ;
             loop
               fetch prod_cur into prod_rec ;
               exit when not found ;
               select id into myres from product_product where product_tmpl_id=prod_rec.id ;
               return next myres ;
             end loop ;
             close prod_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists genoutpartner(partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,outretdate date) cascade""")
        self.env.cr.execute(
            """drop function if exists genoutpartner(partnerid1 int,partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,outretdate date) cascade""")
        self.env.cr.execute("""create or replace function genoutpartner(partnerid1 int,partnerid int,prodid int,ownerid int,prodnum int,outdesc varchar,outmemo varchar,outretdate date) returns void as $BODY$
           DECLARE
             mynowdatetime timestamp ;
             cusname varchar ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             if partnerid1=0 then
                cusname = 'ACME供料' ;
             else
                select name into cusname from res_partner where id = partnerid1 ;
             end if ;   
             insert into alldo_acme_iot_partner_prodout(partner_id,prodout_datetime,product_no,out_good_num,out_owner,out_loc,out_memo,out_return_date) values 
              (partnerid,mynowdatetime,prodid,prodnum,ownerid,cusname,outmemo,outretdate::DATE) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists geninpartner(partnerid int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar) cascade""")
        self.env.cr.execute(
            """drop function if exists geninpartner(partnerid int,partnerid1 int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar) cascade""")
        self.env.cr.execute("""create or replace function geninpartner(partnerid int,partnerid1 int,prodid int,ownerid int,prodnum int,ngnum int,indesc varchar) returns void as $BODY$
           DECLARE
             mynowdatetime timestamp ;
             cusname varchar ;
           BEGIN
             select current_timestamp into mynowdatetime ;
             if partnerid1 = 0 then
                cusname = '移轉回ACME入庫' ;
             else
                select name into cusname from res_partner where id = partnerid1 ;
             end if ;   
             insert into alldo_acme_iot_partner_prodin(partner_id,prodin_datetime,product_no,in_good_num,in_ng_num,in_owner,in_loc) values 
              (partnerid,mynowdatetime,prodid,prodnum,ngnum,ownerid,cusname) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getcusmo(cusid int) cascade""")
        self.env.cr.execute("""create or replace function getcusmo(cusid int) returns setof INT as $BODY$
           DECLARE
             mo_cur refcursor ;
             mo_rec record ;
           BEGIN
             open mo_cur for select id,cus_name,state,eng_order from alldo_acme_iot_workorder where cus_name=cusid and 
             (state != '4' or state != '5') and (eng_order='1' or eng_order='4') order by id ;
             loop
               fetch mo_cur into mo_rec ;
               exit when not found ;
               return next mo_rec.id ;
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
             select count(*) into ncount from mrp_production where id=moid ;
             if ncount > 0 then
                select product_id into myres from mrp_production where id=moid ;
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
           BEGIN
             select product_no,cus_name into prodid,mycusid from alldo_acme_iot_workorder where id = moid ;
             select name into myname from res_partner where id = mycusid ;
             select current_timestamp into mynowdatetime ;  
             insert into alldo_acme_iot_wkorder_prodin(order_id,prodin_datetime,product_no,in_good_num,in_loc,in_owner,in_type,create_date) values
               (moid,mynowdatetime,prodid,blanknum,myname,inowner,'1',mynowdatetime) ; 
             update alldo_acme_iot_workorder set blank_num = coalesce(blank_num,0) + blanknum,write_date=mynowdatetime where id = moid ;
             select blank_num into mynowblanknum from alldo_acme_iot_workorder where id = moid ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setallmoclose(moid int) cascade""")
        self.env.cr.execute("""create or replace function setallmoclose(moid int) returns void as $BODY$
           DECLARE
             mogroupid int ;
             mo_cur refcursor ;
             mo_rec record ;
           BEGIN
             select mo_group_id into mogroupid from alldo_acme_iot_workorder where id = moid ;
             update alldo_acme_iot_workorder set state='4' where mo_group_id=mogroupid ;
             open mo_cur for select id,mo_group_id from alldo_acme_iot_workorder where mo_group_id=mogroupid order by id ;
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
            bom_cur refcursor ;
            bom_rec record ;
            pack_cur refcursor ;
            pack_rec record ;
            prodtmplid int ;
            bomid int ;
            prodqty float ;
            blanktmplid int ;
            blankprodid int ;
            mixprodid int ;
            onhandqty float ;
            blankprodqty float ;
            needqty float ;
            moqty float ;
            msetqty float ;
            csetqty float ;
          BEGIN
            update mrp_production set product_qty=coalesce(product_qty,0) + prodnum where id = moid ;
            update alldo_acme_iot_workorder set order_num = coalesce(order_num,0)+prodnum where mrp_prod_id = moid ;
            update alldo_acme_iot_outsuborder set order_num = coalesce(order_num,0) + prodnum where mrp_prod_id = moid ;
            select product_id,product_qty into myprodid,moqty from mrp_production where id = moid ; 
            select product_tmpl_id into prodtmplid from product_product where id = myprodid ;
            select id,product_qty into bomid,prodqty from mrp_bom where product_tmpl_id=prodtmplid and type='normal' ;
            select product_blank1 into blanktmplid from product_template where id = prodtmplid ;
            select id into blankprodid from product_product where product_tmpl_id = blanktmplid ;
            select furnace_prod_id into mixprodid from alldo_acme_iot_company_stockloc ;
            if bomid is not null then
               open bom_cur for select * from mrp_bom_line where bom_id=bomid ;
               loop
                 fetch bom_cur into bom_rec ;
                 exit when not found ;
                  update stock_move set product_uom_qty = coalesce(product_uom_qty,0) + round((bom_rec.product_qty::numeric/prodqty::numeric) * prodnum::numeric,2) 
                         where raw_material_production_id = moid and product_id=bom_rec.product_id ;
               end loop ;
               close bom_cur ;
               select round((product_uom_qty::numeric * 0.7),2) into blankprodqty from stock_move where raw_material_production_id = moid and
                   product_id = mixprodid ;
               open pack_cur for select * from alldo_acme_iot_materialline where mrp_prod_id = moid ;
               loop
                 fetch pack_cur into pack_rec ;
                 exit when not found ;
                 select getmaterialonhand(pack_rec.product_no) into onhandqty ;
                 if pack_rec.product_no = blankprodid then
                    if onhandqty > blankprodqty then
                       needqty = 0 ;
                    else
                       needqty = onhandqty - blankprodqty ;
                    end if ;
                    update alldo_acme_iot_materialline set product_qty=blankprodqty,onhand_qty=onhandqty,need_qty=needqty where id = pack_rec.id ;
                 else
                    msetqty = 0 ;
                    csetqty = 0 ;
                    select m_set_qty,c_set_qty into msetqty,csetqty from alldo_acme_iot_packaging_line where bom_id=bomid and 
                        product_id=pack_rec.product_no ;
                    if msetqty > 0 and csetqty > 0 and moqty > 0 then
                       if (moqty::numeric % msetqty::numeric) > 0 then
                           blankprodqty = ((moqty::numeric/msetqty::numeric)::INTEGER + 1) * csetqty ; 
                       else
                           blankprodqty = (moqty::numeric/msetqty::numeric)::INTEGER * csetqty ; 
                       end if ;  
                       if onhandqty > blankprodqty then
                          needqty = 0 ;
                       else
                          needqty = onhandqty - blankprodqty ;
                       end if ;  
                       update alldo_acme_iot_materialline set product_qty=blankprodqty,onhand_qty=onhandqty,need_qty=needqty
                          where id = pack_rec.id ;
                    end if ;    
                 end if ;
               end loop ;
               close pack_cur ;             
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmooriginnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmooriginnum(moid int) returns float as $BODY$
          DECLARE
            myres float ;
          BEGIN
            select product_qty into myres from mrp_production where id = moid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists candelwkorder(wkorderid int) cascade""")
        self.env.cr.execute("""create or replace function candelwkorder(wkorderid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
            mygroupid int;
            myprodid int ;
            engtype varchar ;
          BEGIN
            select mo_group_id,product_no,eng_type into mygroupid,myprodid,engtype from alldo_acme_iot_workorder where id = wkorderid ;
            select count(*) into ncount from alldo_acme_iot_workorder where mo_group_id= mygroupid and state in ('3','4') ;
            if ncount = 0 and mygroupid is not null then
               delete from alldo_acme_iot_workorder where mo_group_id = mygroupid and state in ('1','2','5') ;
               myres = True ;
               if mygroupid is not null  then
                  delete from stock_picking where mo_group_id = mygroupid ;
               end if ;
            else
               if engtype='N/A' then
                  delete from alldo_acme_iot_workorder where id = wkorderid ;
                  myres = True ;
               else
                  myres = False ;
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
           mypi varchar ;
          BEGIN
           select coalesce(report_no,' ') into reportno from stock_picking where id = pickingid ; 
           myres = ' ' ;
           if reportno = ' ' then   /* 要產出新單號 */
              select current_timestamp::DATE into mynowdate ;
              select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
              select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
              select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
              select id,number_next into myid,numbernext from ir_sequence where code='alldo_acme_iot.shipping' ;
              numbernext1 = numbernext::TEXT ;
              myshippingno = concat('S',myyear,mymonth,myday,lpad(numbernext1,3,'0')) ;
              myres = myshippingno ;
              update stock_picking set report_no=myshippingno where (report_no is null or report_no='') and id = pickingid and picking_type_id=2 ;
              update ir_sequence set number_next=number_next+1 where id = myid ;
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
            acmereportno varchar ;
            mylinememo varchar ;
            mynowdate date ;
            myyear varchar ;
            mymonth varchar ;
            myday varchar ;
            myid int ;
            numbernext int ;
            numbernext1 varchar ;
            taiinv varchar ;
            saleid int ;
            priceunit float ;
            reporttype char ;
            ispackagemat Boolean ;
            pricelistid int ;
          BEGIN
            select current_timestamp into currentdatetime ;
            /*     */
            select current_timestamp::DATE into mynowdate ;
            select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
            select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
            select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
            select id,number_next into myid,numbernext from ir_sequence where code='alldo_acme_iot.shipping' ;
            numbernext1 = numbernext::TEXT ;
            acmereportno = concat('S',myyear,mymonth,myday,lpad(numbernext1,3,'0')) ;
            update ir_sequence set number_next=number_next+1 where id = myid ;
            /*     */
            select current_timestamp::DATE into currentdate ; 
            select max(id) into myreportid from alldo_acme_iot_stockpicking_report where partner_id=partnerid ;
            update alldo_acme_iot_stockpicking_report set name=acmereportno where id = myreportid ;
            select coalesce(report_date,currentdate),coalesce(report_type,'1') into reportdate,reporttype from alldo_acme_iot_stockpicking_report where id = myreportid ;
            nitem = 1 ;
            open pick_cur for select * from stock_picking where picking_type_id=2 and partner_id=partnerid and report_no is null  ;
            loop
               fetch pick_cur into pick_rec ;
               exit when not found ;
               select coalesce(id,0),pricelist_id into saleid,pricelistid from sale_order where name=pick_rec.origin ;
               select gettaiinv(pick_rec.origin) into taiinv ;
               update alldo_acme_iot_stockpicking_report set taiwan_receipt=taiinv where id = myreportid ;
               if repmemo is null then
                  repmemo = pick_rec.report_memo ;
               else   
                  repmemo = concat(coalesce(repmemo,''),'/',pick_rec.report_memo) ;
               end if ;
               select coalesce(so_pi,' ') into mylinememo from sale_order where name=pick_rec.origin ;   
               open ml_cur for select * from stock_move_line where picking_id = pick_rec.id and reference != 'do_not_print' ;
               loop
                  fetch ml_cur into ml_rec ;
                  exit when not found ;
                  select getispackagemat(ml_rec.product_id) into ispackagemat ;
                  if ispackagemat = False then
                      /* select description_picking into mylinememo from stock_move where id = ml_rec.move_id ;*/
                      if ml_rec.qty_done > 0 then
                          if saleid > 0 then
                             select price_unit into priceunit from sale_order_line where order_id = saleid and product_id = ml_rec.product_id ;
                          else
                             priceunit = 0 ;   
                          end if ;
                          if reporttype='1' then
                             insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo) values 
                                 (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',0,0,mylinememo) ;
                          else
                              if pricelistid=140 then
                                 insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo) values 
                                    (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',priceunit,round(ml_rec.qty_done::numeric * priceunit::numeric),mylinememo) ;
                              else
                                 insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo) values 
                                    (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',priceunit,round((ml_rec.qty_done::numeric * priceunit::numeric),2),mylinememo) ;
                              end if ;
                              
                          end if ;   
                          select max(id) into myreplineid from alldo_acme_iot_stockpicking_report_line where rep_id=myreportid ; 
                          /* update stock_picking set date_done=reportdate,report_no=acmereportno where id = pick_rec.id ; */
                          nitem = nitem + 1 ;
                      end if ;    
                  end if ;    
               end loop ;
               close ml_cur ;
               update stock_picking set report_no=acmereportno where  id = pick_rec.id ;
            end loop ;
            close pick_cur ;
            update alldo_acme_iot_stockpicking_report set report_memo=repmemo,report_date=currentdate where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldshipping(reportno varchar) cascade""")
        self.env.cr.execute("""drop function if exists genoldshipping(reportno varchar,reporttype char) cascade""")
        self.env.cr.execute("""create or replace function genoldshipping(reportno varchar,reporttype char) returns void as $BODY$
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
            myorigin varchar ;
            saleid int ;
            priceunit float ;
            ispackagemat boolean ;
            orderlineid int ;
            taxid int ;
            taxamount float ;
            sono varchar ;
            pricelistid int ;
          BEGIN
            select max(date_done) into reportdate from stock_picking where report_no=reportno ; 
            select max(partner_id) into mypartnerid from stock_picking where report_no=reportno ; 
            insert into alldo_acme_iot_stockpicking_report(name,report_date) values (reportno,reportdate) ;
            select max(id) into myreportid from alldo_acme_iot_stockpicking_report where name=reportno ;
            nitem = 1 ;
            open pick_cur for select * from stock_picking where report_no = reportno ;
            loop
               fetch pick_cur into pick_rec ;
               exit when not found ;
               select coalesce(id,0),pricelist_id into saleid,pricelistid from sale_order where name=pick_rec.origin ;
               if pick_rec.report_memo is not null then
                  if repmemo is null then
                     repmemo = pick_rec.report_memo ;
                  else
                     repmemo = concat(coalesce(repmemo,''),'/',pick_rec.report_memo) ;
                  end if ;   
               end if ;   
               select coalesce(so_pi,' ') into mylinememo from sale_order where name=pick_rec.origin ;
               open ml_cur for select * from stock_move_line where picking_id = pick_rec.id and state='done' and reference != 'do_not_print'  ; 
               loop
                  fetch ml_cur into ml_rec ;
                  exit when not found ;
                  select getispackagemat(ml_rec.product_id) into ispackagemat ;
                  if ispackagemat = False then
                      /* select description_picking into mylinememo from stock_move where id = ml_rec.move_id ;*/
                      if ml_rec.qty_done > 0 then
                          if saleid > 0 then
                             select id,price_unit into orderlineid,priceunit from sale_order_line where order_id = saleid and product_id = ml_rec.product_id ;
                             select distinct account_tax_id into taxid from account_tax_sale_order_line_rel where sale_order_line_id=orderlineid ;
                             if taxid is not null then
                                select amount into taxamount from account_tax where id = taxid ;
                             else
                                taxamount = 0 ;
                             end if ;
                          else
                             priceunit = 0 ;   
                             taxamount = 0 ;
                          end if ;
                          if reporttype='1' then
                             insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo,tax_amount) values 
                                  (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',0,0,mylinememo,taxamount) ;
                          else
                              if pricelistid=140 then
                                  insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo,tax_amount) values 
                                      (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',priceunit,round(ml_rec.qty_done::numeric * priceunit::numeric),mylinememo,taxamount) ;
                              else
                                  insert into alldo_acme_iot_stockpicking_report_line(rep_id,item,prod_no,prod_num,prod_uom,prod_price,sum_price,line_memo,tax_amount) values 
                                      (myreportid,nitem,ml_rec.product_id,ml_rec.qty_done,'PCS',priceunit,round((ml_rec.qty_done::numeric * priceunit::numeric),2),mylinememo,taxamount) ;
                              end if ;        
                          end if ;        
                          select max(id) into myreplineid from alldo_acme_iot_stockpicking_report_line where rep_id=myreportid ; 
                          nitem = nitem + 1 ;
                      end if ;    
                  end if ;    
               end loop ;
               close ml_cur ;
            end loop ;
            close pick_cur ;
            update alldo_acme_iot_stockpicking_report set report_memo=repmemo,report_date=reportdate,partner_id=mypartnerid,report_type=reporttype where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckngreturn(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function ckngreturn(partnerid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_acme_iot_workorder where id in 
              (select order_id from alldo_acme_iot_workorder_qc where (report_no is null or report_no='') 
                 and (material_ng_num > 0 or processing_ng_num > 0))
              and cus_name = partnerid ;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;  
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gennewngreturn(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gennewngreturn(partnerid int) returns void as $BODY$
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
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into myreportid from alldo_acme_iot_ngreturn_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhngreturnno from alldo_acme_iot_ngreturn_report where id = myreportid ;
            nitem = 1 ; 
            open ng_cur for select * from alldo_acme_iot_workorder_qc where (material_ng_num > 0 or processing_ng_num > 0) 
                and (report_no is null or report_no='') and cus_name=partnerid ;
            loop
               fetch ng_cur into ng_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_acme_iot_ngreturn_report_line(rep_id,item,prod_no,m_ng_num,p_ng_num,prod_uom,line_memo) values 
                  (myreportid,nitem,ng_rec.product_no,ng_rec.material_ng_num,ng_rec.processing_ng_num,'PCS',ng_rec.line_memo) ;
                 select max(id) into myreplineid from alldo_acme_iot_ngreturn_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_acme_iot_ngreturn_report_line set item1=nitem,prod_no1=ng_rec.product_no,m_ng_num1=ng_rec.material_ng_num,
                    p_ng_num1=ng_rec.processing_ng_num,prod_uom1='PCS',line_memo1=ng_rec.line_memo where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_acme_iot_ngreturn_report_line set item2=nitem,prod_no2=ng_rec.product_no,m_ng_num2=ng_rec.material_ng_num,
                    p_ng_num2=ng_rec.processing_ng_num,prod_uom2='PCS',line_memo2=ng_rec.line_memo where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_acme_iot_ngreturn_report_line set item3=nitem,prod_no3=ng_rec.product_no,m_ng_num3=ng_rec.material_ng_num,
                    p_ng_num3=ng_rec.processing_ng_num,prod_uom3='PCS',line_memo3=ng_rec.line_memo where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_acme_iot_ngreturn_report_line set item4=nitem,prod_no4=ng_rec.product_no,m_ng_num4=ng_rec.material_ng_num,
                    p_ng_num4=ng_rec.processing_ng_num,prod_uom4='PCS',line_memo4=ng_rec.line_memo where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_acme_iot_workorder_qc set report_date=reportdate,report_no=jhngreturnno where id = ng_rec.id ;   
            end loop ;
            close ng_cur ;
            update alldo_acme_iot_ngreturn_report set report_date=currentdate where id = myreportid ;
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
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into mymaxid from alldo_acme_iot_workorder_qc where report_no = ngreturnno ; 
            select cus_name,report_no,report_date into partnerid,jhngreturnno,reportdate from alldo_acme_iot_workorder_qc 
               where id = mymaxid ;
            insert into alldo_acme_iot_ngreturn_report(partner_id,name,report_date) values (partnerid,jhngreturnno,reportdate) ;
            select max(id) into myreportid from alldo_acme_iot_ngreturn_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhngreturnno from alldo_acme_iot_ngreturn_report where id = myreportid ;
            nitem = 1 ; 
            open ng_cur for select * from alldo_acme_iot_workorder_qc where report_no=ngreturnno ;
            loop
               fetch ng_cur into ng_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_acme_iot_ngreturn_report_line(rep_id,item,prod_no,m_ng_num,p_ng_num,prod_uom,line_memo) values 
                  (myreportid,nitem,ng_rec.product_no,ng_rec.material_ng_num,ng_rec.processing_ng_num,'PCS',ng_rec.line_memo) ;
                 select max(id) into myreplineid from alldo_acme_iot_ngreturn_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_acme_iot_ngreturn_report_line set item1=nitem,prod_no1=ng_rec.product_no,m_ng_num1=ng_rec.material_ng_num,
                    p_ng_num1=ng_rec.processing_ng_num,prod_uom1='PCS',line_memo1=ng_rec.line_memo where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_acme_iot_ngreturn_report_line set item2=nitem,prod_no2=ng_rec.product_no,m_ng_num2=ng_rec.material_ng_num,
                    p_ng_num2=ng_rec.processing_ng_num,prod_uom2='PCS',line_memo2=ng_rec.line_memo where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_acme_iot_ngreturn_report_line set item3=nitem,prod_no3=ng_rec.product_no,m_ng_num3=ng_rec.material_ng_num,
                    p_ng_num3=ng_rec.processing_ng_num,prod_uom3='PCS',line_memo3=ng_rec.line_memo where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_acme_iot_ngreturn_report_line set item4=nitem,prod_no4=ng_rec.product_no,m_ng_num4=ng_rec.material_ng_num,
                    p_ng_num4=ng_rec.processing_ng_num,prod_uom4='PCS',line_memo4=ng_rec.line_memo where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_acme_iot_workorder_qc set report_date=reportdate,report_no=jhngreturnno where id = ng_rec.id ;   
            end loop ;
            close ng_cur ;
            update alldo_acme_iot_ngreturn_report set report_date=currentdate where id = myreportid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists ckoutsourcing(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function ckoutsourcing(partnerid int) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_acme_iot_partner_prodout where partner_id = partnerid
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
        self.env.cr.execute("""create or replace function gennewoutsourcing(partnerid int) returns void as $BODY$
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
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into myreportid from alldo_acme_iot_outsourcing_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_acme_iot_outsourcing_report where id = myreportid ;
            nitem = 1 ; 
            open os_cur for select * from alldo_acme_iot_partner_prodout where out_good_num > 0  
                and partner_id=partnerid and (report_no is null or report_no='') ;
            loop
               fetch os_cur into os_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_acme_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                  (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                  select max(id) into myreplineid from alldo_acme_iot_outsourcing_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_acme_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                    prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_acme_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                    prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_acme_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                    prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_acme_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                    prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_acme_iot_partner_prodout set report_date=reportdate,report_no=jhoutsourcingno where id = os_rec.id ;   
            end loop ;
            close os_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genoldoutsourcing(outsourcingno varchar) cascade""")
        self.env.cr.execute("""create or replace function genoldoutsourcing(outsourcingno varchar) returns void as $BODY$
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
          BEGIN
            select current_timestamp into currentdatetime ;
            select current_timestamp::DATE into currentdate ; 
            select max(id) into mymaxid from alldo_acme_iot_partner_prodout where report_no = outsourcingno ; 
            select partner_id,report_no,report_date into partnerid,jhoutsourcingno,reportdate from alldo_acme_iot_partner_prodout 
               where id = mymaxid ;
            insert into alldo_acme_iot_outsourcing_report(partner_id,name,report_date) values (partnerid,jhoutsourcingno,reportdate) ;
            select max(id) into myreportid from alldo_acme_iot_outsourcing_report where partner_id=partnerid ;
            select coalesce(report_date,currentdate),name into reportdate,jhoutsourcingno from alldo_acme_iot_outsourcing_report where id = myreportid ;
            nitem = 1 ; 
            open os_cur for select * from alldo_acme_iot_partner_prodout where out_good_num > 0  
                and report_no = outsourcingno ;
            loop
               fetch os_cur into os_rec ;
               exit when not found ;
               if nitem = 1 then
                  insert into alldo_acme_iot_outsourcing_report_line(rep_id,item,prod_no,prod_num,prod_uom,line_memo,out_return_date) values 
                  (myreportid,nitem,os_rec.product_no,os_rec.out_good_num,'PCS',os_rec.out_loc,os_rec.out_return_date) ;
                  select max(id) into myreplineid from alldo_acme_iot_outsourcing_report_line where rep_id=myreportid ; 
               elsif nitem = 2 then
                  update alldo_acme_iot_outsourcing_report_line set item1=nitem,prod_no1=os_rec.product_no,prod_num1=os_rec.out_good_num,
                    prod_uom1='PCS',line_memo1=os_rec.out_loc,out_return_date1=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 3 then
                  update alldo_acme_iot_outsourcing_report_line set item2=nitem,prod_no2=os_rec.product_no,prod_num2=os_rec.out_good_num,
                    prod_uom2='PCS',line_memo2=os_rec.out_loc,out_return_date2=os_rec.out_return_date where id = myreplineid ;
               elsif nitem= 4 then
                  update alldo_acme_iot_outsourcing_report_line set item3=nitem,prod_no3=os_rec.product_no,prod_num3=os_rec.out_good_num,
                    prod_uom3='PCS',line_memo3=os_rec.out_loc,out_return_date3=os_rec.out_return_date where id = myreplineid ;
               elsif nitem = 5 then
                  update alldo_acme_iot_outsourcing_report_line set item4=nitem,prod_no4=os_rec.product_no,prod_num4=os_rec.out_good_num,
                    prod_uom4='PCS',line_memo4=os_rec.out_loc,out_return_date4=os_rec.out_return_date where id = myreplineid ;
                  nitem = 0 ;
               end if ;
               nitem = nitem + 1 ;
               update alldo_acme_iot_partner_prodout set report_date=reportdate,report_no=jhoutsourcingno where id = os_rec.id ;   
            end loop ;
            close os_cur ;
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
              open mo_cur for select distinct iot_owner from alldo_acme_iot_workorder_iot_data where order_id = woid ;
              loop
                 fetch mo_cur into mo_rec ;
                 exit when not found ;
                 select sum(coalesce(iot_duration,0)),sum(coalesce(iot_num,0)) into nsumtottime,nsumnum from alldo_acme_iot_workorder_iot_data
                   where order_id = woid and iot_owner=mo_rec.iot_owner ;
                 select coalesce(max(iot_date::DATE),mynowdate) into proddate from alldo_acme_iot_workorder_iot_data where order_id = woid and iot_owner=mo_rec.iot_owner ; 
                 select product_no,eng_type into prodid,engtype from alldo_acme_iot_workorder where id = woid ;
                 select product_tmpl_id into prodtmplid from product_product where id = prodid ;
                 select coalesce(standard_num,0) into stdnum from alldo_acme_iot_eng_order where prod_id = prodtmplid and eng_type=engtype ;
                 realstdnum = round(stdnum::numeric * (nsumtottime::numeric/60),0) ;
                 if realstdnum=0 then
                    perf = 0 ;
                 else
                    perf = round((nsumnum::numeric/realstdnum::numeric),2) ;
                 end if ;
                 select count(*) into ncount from alldo_acme_iot_man_performance where order_id = woid and prod_owner=mo_rec.iot_owner ;
                 if ncount = 0 then
                    insert into alldo_acme_iot_man_performance(order_id,prod_date,prod_duration,std_duration,prod_performance,prod_owner,prod_num) values
                     (woid,proddate,nsumtottime,realstdnum,perf,mo_rec.iot_owner,nsumnum) ;
                 else    
                    update alldo_acme_iot_man_performance set prod_date=proddate,prod_duration=nsumtottime,std_durtion=realstdnum,prod_performance=perf,
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
          BEGIN
            delete from alldo_acme_iot_emp_attendance_list ;
            open emp_cur for select * from hr_employee where active=True order by emp_code ;
            loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               open att_cur for select * from alldo_acme_iot_emp_attendance where attendance_id=emp_rec.id and 
                  (attendance_date + interval '8 hours')::DATE >= attstart::DATE and 
                  (attendance_date + interval '8 hours')::DATE <= attend::DATE order by attendance_date;
               loop
                  fetch att_cur into att_rec ;
                  exit when not found ;
                  select (att_rec.attendance_date + interval '8 hours')::DATE into mydate ;
                  mydate1 = mydate::TEXT ;
                  select count(*) into ncount from alldo_acme_iot_emp_attendance_list where emp_no=emp_rec.id and
                       attend_date1 = mydate1 ;
                  select lpad(date_part('hour',att_rec.attendance_date + interval '8 hours')::TEXT,2,'0') into chour ;
                  select lpad(date_part('minute',att_rec.attendance_date)::TEXT,2,'0') into cmin ;
                  select lpad(date_part('second',att_rec.attendance_date)::TEXT,2,'0') into csecond ;
                  mytime = concat(chour,':',cmin,':',csecond) ;     
                  if ncount = 0 then
                     if att_rec.attendance_type='1' then
                        insert into alldo_acme_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_start) values 
                        (att_rec.attendance_id,mydate,mydate1,mytime) ;
                     else
                       insert into alldo_acme_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_end) values 
                        (att_rec.attendance_id,mydate,mydate1,mytime) ;
                     end if ;
                  else 
                     if att_rec.attendance_type='1' then
                        update alldo_acme_iot_emp_attendance_list set attendance_start=mytime where emp_no=emp_rec.id and
                               attend_date1 = mydate1 and  attendance_start is null ;
                     else
                        update alldo_acme_iot_emp_attendance_list set attendance_end=mytime where emp_no=emp_rec.id and
                               attend_date1 = mydate1 and  attendance_end is null;
                     end if ;
                  end if ;     
               end loop ;
               close att_cur ;   
            end loop ;
            close emp_cur ;
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
            list_cur refcursor ;
            list_rec record ;
            mynowdatetime timestamp ;
            listmin float ;
            listhour float ;
            listtot float ;
            mytime1 timestamp ;
            mytime2 timestamp ;
            mynowdate varchar ;
          BEGIN
            delete from alldo_acme_iot_emp_attendance_list ;
            select now()::DATE::TEXT into mynowdate ;
            select concat(mynowdate,' 12:00:00')::timestamp into mytime1 ;
            select concat(mynowdate,' 13:00:00')::timestamp into mytime2 ;
            open att_cur for select * from alldo_acme_iot_emp_attendance where attendance_id=empno and 
                 (attendance_date + interval '8 hours')::DATE >= attstart::DATE and 
                 (attendance_date + interval '8 hours')::DATE <= attend::DATE order by attendance_date ;
            loop
              fetch att_cur into att_rec ;
              exit when not found ;
              select (att_rec.attendance_date + interval '8 hours')::DATE into mydate ;
              mydate1 = mydate::TEXT ;
              select count(*) into ncount from alldo_acme_iot_emp_attendance_list where emp_no=empno and
                   attend_date1 = mydate1 ;
              select lpad(date_part('hour',att_rec.attendance_date + interval '8 hours')::TEXT,2,'0') into chour ;
              select lpad(date_part('minute',att_rec.attendance_date)::TEXT,2,'0') into cmin ;
              select lpad(date_part('second',att_rec.attendance_date)::TEXT,2,'0') into csecond ;
              mytime = concat(chour,':',cmin,':',csecond) ;    
               
              if ncount = 0 then
                 if att_rec.attendance_type='1' then
                    insert into alldo_acme_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_start,att_start_date) values 
                    (empno,mydate,mydate1,mytime,att_rec.attendance_date) ;
                 else
                   insert into alldo_acme_iot_emp_attendance_list(emp_no,attend_date,attend_date1,attendance_end,att_end_date) values 
                    (empno,mydate,mydate1,mytime,att_rec.attendance_date) ;
                 end if ;
              else 
                 if att_rec.attendance_type='1' then
                    update alldo_acme_iot_emp_attendance_list set attendance_start=mytime,att_start_date=att_rec.attendance_date where emp_no=empno and
                           attend_date1=mydate1 and  attendance_start is null ;
                 else
                    update alldo_acme_iot_emp_attendance_list set attendance_end=mytime,att_end_date=att_rec.attendance_date where emp_no=empno and
                           attend_date1=mydate1 and  attendance_end is null;
                 end if ;
              end if ;     
           end loop ;
           close att_cur ;  
           open list_cur for select * from alldo_acme_iot_emp_attendance_list ;
           loop
              fetch list_cur into list_rec ;
              exit when not found ;
              select extract(minute from (select age(list_rec.att_end_date,list_rec.att_start_date))) into listmin ;
              select extract(hours from (select age(list_rec.att_end_date,list_rec.att_start_date))) into listhour ; 
              listtot = listhour::numeric + round((listmin::numeric/60::numeric),2) ;
              /*if list_rec.att_start_date <= mytime1 and list_rec.att_end_date >= mytime2 then */
              if listtot > 5 then
                 listtot = listtot - 1 ;
              end if ;
              update alldo_acme_iot_emp_attendance_list set att_duration=listtot where id = list_rec.id ;
           end loop ;
           close list_cur ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists genoutsourcinginout(partnerid int,prodid int,startdate date,enddate date) cascade""")
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
            delete from alldo_acme_iot_inout_prod_list ;
            open out_cur for select * from alldo_acme_iot_partner_prodout where partner_id=partnerid and
               product_no=prodid and prodout_datetime::DATE >= startdate::DATE and prodout_datetime::DATE <= enddate::DATE ;
            loop
                fetch out_cur into out_rec ;
                exit when not found ;
                select out_rec.prodout_datetime::DATE::TEXT into mydate ;
                select id into resourceid from resource_resource where user_id = out_rec.out_owner ;
                select id into empid from hr_employee where resource_id=resourceid ;
                if out_rec.out_owner is null then
                   insert into alldo_acme_iot_inout_prod_list(inout_date1,product_id,out_num) values
                      (mydate,out_rec.product_no,out_rec.out_good_num) ;
                else
                   insert into alldo_acme_iot_inout_prod_list(inout_date1,product_id,out_num,out_owner) values
                      (mydate,out_rec.product_no,out_rec.out_good_num,empid) ;
                end if ;
                
            end loop ;
            close out_cur ;   
            open in_cur for select * from alldo_acme_iot_partner_prodin where partner_id=partnerid and
               product_no=prodid and prodin_datetime::DATE >= startdate::DATE and prodin_datetime::DATE <= enddate::DATE ;
            loop
                fetch in_cur into in_rec ;
                exit when not found ;
                select in_rec.prodin_datetime::DATE::TEXT into mydate ;
                 select id into resourceid from resource_resource where user_id = in_rec.in_owner ;
                select id into empid from hr_employee where resource_id=resourceid ;
                if in_rec.in_owner is null then
                   insert into alldo_acme_iot_inout_prod_list(inout_date1,product_id,in_good_num,in_ng_num) values
                       (mydate,in_rec.product_no,in_rec.in_good_num,in_rec.in_ng_num) ;
                else
                    insert into alldo_acme_iot_inout_prod_list(inout_date1,product_id,in_good_num,in_ng_num,in_owner) values
                       (mydate,in_rec.product_no,in_rec.in_good_num,in_rec.in_ng_num,empid) ;
                end if ;
            end loop ;
            close in_cur ;  
            nowbalance = 0 ;
            open list_cur for select * from alldo_acme_iot_inout_prod_list order by inout_date ; 
            loop
              fetch list_cur into list_rec ;
              exit when not found ;
              nowbalance = nowbalance + coalesce(list_rec.out_num,0) - coalesce(list_rec.in_good_num,0) - coalesce(list_rec.in_ng_num,0) ;
              update alldo_acme_iot_inout_prod_list set balance_num=nowbalance where id = list_rec.id ;
            end loop ;
            close list_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW stock_picking_move_line_view AS
          SELECT SP.id,SP.name,SP.report_no,SP.partner_id,SP.origin,SP.date_done,SP.picking_type_id,SP.state,SML.location_id,
             SML.product_id,SML.qty_done,SML.picking_id from stock_picking SP left join stock_move_line SML on SP.id = SML.picking_id 
             where SP.state='done' and SP.picking_type_id=2 ;""")

        self.env.cr.execute(
            """drop function if exists genshippingexcel(partnerid int,prodid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genshippingexcel(partnerid int,prodid int,startdate date,enddate date) returns void as $BODY$
          DECLARE
            mv_cur refcursor ;
            mv_rec record ; 
            mydate varchar ;
          BEGIN
            delete from alldo_acme_iot_shipping_list ;
            if prodid = 0 and partnerid = 0 then
                open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate 
                order by date_done,name ;
            elsif prodid = 0 and partnerid != 0 then 
               open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid   
                order by date_done,name ;
            elsif prodid != 0 and partnerid = 0 then
               open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate and   
               product_id=prodid order by date_done,name ;
            else
               open mv_cur for select * from stock_picking_move_line_view where date_done >= startdate and date_done <= enddate and partner_id=partnerid and  
               product_id=prodid order by date_done,name ;    
            end if ;
            loop
              fetch mv_cur into mv_rec ;
              exit when not found ;
              select mv_rec.date_done::TEXT into mydate ;
              insert into alldo_acme_iot_shipping_list(name,report_no,location_id,partner_id,shipping_date,shipping_date1,product_id,qty_done,origin) values
                (mv_rec.name,mv_rec.report_no,mv_rec.location_id,mv_rec.partner_id,mv_rec.date_done,mydate,mv_rec.product_id,mv_rec.qty_done,mv_rec.origin) ;
            end loop ;
            close mv_cur ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW alldo_acme_iot_workorder_view AS
             select WK.id as wkid,WK.name,WK.product_no,WK.eng_type,WK.po_no,WK.cus_name,WK.order_num,WK.prod_num,WK.shipping_num,WK.prod_duration,
             DT.id as dtid,DT.order_id,DT,iot_date,DT.iot_node,DT.iot_owner,DT.iot_num,DT.iot_duration,DT.std_duration 
             from alldo_acme_iot_workorder_iot_data DT left join alldo_acme_iot_workorder WK on WK.id= DT.order_id where WK.state in ('3','4') """)

        self.env.cr.execute(
            """drop function if exists genwkperformance(startdate date,enddate date,prodid int,engtype char,empid int,equipid int) cascade""")
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
            delete from alldo_acme_iot_workorder_performance_list1 ;
            if prodid = 0 and empid = 0 and equipid > 0 then
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid = 0 and empid > 0 and equipid = 0 then
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid > 0 and empid = 0 and equipid = 0 then
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                    (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid order by wkorder_id,iot_node,iot_owner ; 
            elsif prodid = 0 and empid > 0 and equipid > 0 then
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                    (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid > 0 and empid = 0 and equipid > 0 then 
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                    (iot_date::DATE between startdate::DATE and enddate::DATE) and product_no = prodid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            elsif prodid > 0 and empid > 0 and equipid = 0 then          
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                    (iot_date between startdate and enddate) and iot_owner = empid and product_no = prodid order by wkorder_id,iot_node,iot_owner ; 
            elsif prodid = 0 and empid = 0 and equipid = 0 then
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                   (iot_date::DATE between startdate::DATE and enddate::DATE) order by wkorder_id,iot_node,iot_owner ;
            else
                open iot_cur for select * from alldo_acme_iot_cnc_performance_report where 
                   (iot_date::DATE between startdate::DATE and enddate::DATE) and iot_owner = empid and product_no = prodid and iot_node = equipid order by wkorder_id,iot_node,iot_owner ;
            end if ;
           loop
              fetch iot_cur into iot_rec ;
              exit when not found ;
              select to_char(iot_rec.iot_start,'YYYY-MM-DD HH:MM:SS') into startdate1 ; 
              select to_char(iot_rec.iot_end,'YYYY-MM-DD HH:MM:SS') into enddate1 ; 
              insert into alldo_acme_iot_workorder_performance_list1(wkorder_id,iot_date,iot_owner,iot_node,iot_start,iot_end,product_no,eng_type,total_amount_num,material_ng_num,
              processing_ng_num,std_num,performance_rate,iot_duration,product_num) values (iot_rec.wkorder_id,iot_rec.iot_date::TEXT,iot_rec.iot_owner,iot_rec.iot_node,startdate1,
              enddate1,iot_rec.product_no,iot_rec.eng_type,iot_rec.total_amount_num,iot_rec.material_ng_num,iot_rec.processing_ng_num,iot_rec.std_num,(iot_rec.performance_rate::numeric * 100),
              iot_rec.iot_duration,iot_rec.product_num) ;
            end loop ;
            close iot_cur ;       
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""create or replace view alldo_replaceline_view AS select A.order_id,A.replace_owner,A.equipment_id,A.replace_type,
           A.replace_start_datetime,A.replace_end_datetime,A.replace_duration,B.product_no,B.eng_type from alldo_acme_iot_wkorder_replaceline A left join
           alldo_acme_iot_workorder B on A.order_id = B.id ;""")

        self.env.cr.execute(
            """drop function if exists genreplineperformance(startdate date,enddate date,prodid int,empid int,equipid int) cascade""")
        self.env.cr.execute(
            """drop function if exists genreplineperformance(startdate date,enddate date,prodid int,empid int,equipid int,reptype char) cascade""")
        self.env.cr.execute("""create or replace function genreplineperformance(startdate date,enddate date,prodid int,empid int,equipid int,reptype char) returns void as $BODY$
              DECLARE
                rep_cur refcursor ;
                rep_rec record ;
              BEGIN
                delete from alldo_acme_iot_replaceline_list ;
                if prodid = 0 and empid = 0 and equipid > 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and equipment_id = equipid order by replace_start_datetime,equipment_id,order_id ;
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and equipment_id = equipid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id;
                    end if ;        
                elsif prodid = 0 and empid > 0 and equipid = 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and replace_owner = empid order by replace_start_datetime,equipment_id,order_id; 
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and replace_owner = empid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ; 
                    end if ;        
                elsif prodid > 0 and empid = 0 and equipid = 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid order by replace_start_datetime,equipment_id,order_id;  
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ;
                    end if ;        
                elsif prodid = 0 and empid > 0 and equipid > 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and equipment_id = equipid and replace_owner = empid order by replace_start_datetime,equipment_id,order_id ;  
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and equipment_id = equipid and replace_owner = empid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ;
                    end if ;        
                elsif prodid > 0 and empid = 0 and equipid > 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and equipment_id = equipid order by replace_start_datetime,equipment_id,order_id ; 
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and equipment_id = equipid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ;
                    end if ;        
                elsif prodid > 0 and empid > 0 and equipid = 0 then
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and replace_owner=empid order by replace_start_datetime,equipment_id,order_id ;     
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and replace_owner=empid and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ;  
                    end if ;             
                else
                    if reptype='0' then
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and replace_owner=empid and equipment_id=equipid  order by replace_start_datetime,equipment_id,order_id ;   
                    else
                        open rep_cur for select * from alldo_replaceline_view where (replace_start_datetime::timestamp + interval '8 hours')::DATE 
                            between startdate::DATE and enddate::DATE and product_no = prodid and replace_owner=empid and equipment_id=equipid  and replace_type=reptype order by replace_start_datetime,equipment_id,order_id ; 
                    end if ;          
                end if ; 
                loop
                  fetch rep_cur into rep_rec ;
                  exit when not found ;
                    insert into alldo_acme_iot_replaceline_list(equipment_id,order_id,product_no,eng_type,replace_start_datetime,replace_end_datetime,replace_duration,replace_owner,replace_type) values
                     (rep_rec.equipment_id,rep_rec.order_id,rep_rec.product_no,rep_rec.eng_type,(rep_rec.replace_start_datetime + interval '8 hours'),(rep_rec.replace_end_datetime + interval '8 hours'),rep_rec.replace_duration,
                     rep_rec.replace_owner,rep_rec.replace_type) ;
                end loop ;
                close rep_cur ;                                    
              END;$BODY$
              LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmogpseq() cascade""")
        self.env.cr.execute("""create or replace function getmogpseq() returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_acme_iot_mo_group_seq ;
            if ncount=0 then
               myres = 1 ;
               insert into alldo_acme_iot_mo_group_seq(seqnum) values (2) ;
            else
               select coalesce(seqnum,1) into myres from alldo_acme_iot_mo_group_seq  ;
               update alldo_acme_iot_mo_group_seq set seqnum = coalesce(seqnum,1) + 1 ;
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

        self.env.cr.execute("""CREATE OR REPLACE VIEW acmeiot_prodstock_view AS
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
          BEGIN
            delete from alldo_acme_iot_prod_stock_list ;
            select distinct prod_loc into prodlocid from alldo_acme_iot_company_stockloc ;
            if prodid = 0 then
               open st_cur for select * from acmeiot_prodstock_view order by product_id ;
            else
               open st_cur for select * from acmeiot_prodstock_view where product_id=prodid ;
            end if ;
            loop
               fetch st_cur into st_rec ;
               exit when not found ;
               if st_rec.location_id=prodlocid then
                  insert into alldo_acme_iot_prod_stock_list(product_no,stock_location,prod_num) values (st_rec.product_id,st_rec.location_id,st_rec.quantity) ;
               else
                  insert into alldo_acme_iot_prod_stock_list(product_no,stock_location,blank_num) values (st_rec.product_id,st_rec.location_id,st_rec.quantity) ;
               end if ;   
            end loop ;
            close st_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genfurnaceloc(locid int) cascade""")
        self.env.cr.execute("""create or replace function genfurnaceloc(locid int) returns void as $BODY$
          DECLARE
            ncount int ;
            myid int ;
          BEGIN
            select count(*) into ncount from  alldo_acme_iot_casting_furnace ;
            if ncount = 0 then
               if locid > 0 then
                  insert into alldo_acme_iot_casting_furnace(furnace_loc) values (locid) ;
               end if ;   
            else
               if locid > 0 then
                  select min(id) into myid from alldo_acme_iot_casting_furnace ;
                  update alldo_acme_iot_casting_furnace set furnace_loc=locid ;
                  delete from alldo_acme_iot_casting_furnace where id != myid ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genlotid(prodid int) cascade""")
        self.env.cr.execute("""create or replace function genlotid(prodid int) returns setof INT as $BODY$
          DECLARE
            lot_cur refcursor ;
            lot_rec record ;
            productid int ;
          BEGIN
            select id into productid from product_product where product_tmpl_id = prodid ;
            open lot_cur for select id,product_id,company_id,quantity from stock_quant where product_id=productid and 
                company_id=1 and lot_id is not null and location_id=19 and quantity > 0 ;
            loop
               fetch lot_cur into lot_rec ;
               exit when not found ;
               return next lot_rec.id ;
            end loop ;
            close lot_cur ;     
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genalllotid() cascade""")
        self.env.cr.execute("""create or replace function genalllotid() returns setof INT as $BODY$
          DECLARE
            lot_cur refcursor ;
            lot_rec record ;
            productid int ;
          BEGIN
            open lot_cur for select id,product_id,company_id,quantity from stock_quant where  
                company_id=1 and lot_id is not null and location_id=19 and quantity > 0 ;
            loop
               fetch lot_cur into lot_rec ;
               exit when not found ;
               return next lot_rec.id ;
            end loop ;
            close lot_cur ;     
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getfurnace() cascade""")
        self.env.cr.execute("""create or replace function getfurnace() returns setof INT as $BODY$
          DECLARE
             equ_cur refcursor ;
             equ_rec record ;
             categid int ;
          BEGIN
             select min(id) into categid from maintenance_equipment_category where name = 'furnace' ;
             open equ_cur for select id,category_id from maintenance_equipment where category_id = categid ;
             loop
               fetch equ_cur into equ_rec ;
               exit when not found ;
               return next equ_rec.id ;
             end loop ;
             close equ_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmosaleno(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmosaleno(moid int) returns INT as $BODY$
          DECLARE
            myorigin varchar ;
            myres int ;
          BEGIN
            select origin into myorigin from mrp_production where id = moid ;
            select id into myres from sale_order where name = myorigin ;
            if myres is null then
               myres = 0 ;         
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmoqty(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmoqty(moid int) returns Float as $BODY$
          DECLARE
            myres Float ;
          BEGIN
            select product_qty into myres from mrp_production where id=moid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmodeadline(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmodeadline(moid int) returns timestamp as $BODY$
          DECLARE
             myres timestamp ;
          BEGIN
             select date_deadline into myres from mrp_production where id=moid ;
             if myres is null then
                select current_timestamp + interval '30 Days' into myres ;
             end if ;   
             return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getfurnaceqty(bomid int) cascade""")
        self.env.cr.execute("""create or replace function getfurnaceqty(bomid int) returns void as $BODY$
          DECLARE
            myres float ;
            prodtmplid int ;
            moldid int ;
            moldcavity int ;
            blankweight float ;
            furnaceprodid int ;
            ncount int ;
          BEGIN
            moldcavity = 0 ;
            select min(furnace_prod_id) into furnaceprodid from alldo_acme_iot_company_stockloc ;
            select product_tmpl_id into prodtmplid from mrp_bom where id = bomid ;
            select min(mold_id) into moldid from alldo_acme_iot_product_mold where product_id=prodtmplid and active=True ;
            select coalesce(mold_cavity,1) into moldcavity from alldo_acme_iot_acme_mold where id = moldid ;
            select blank_weight into blankweight from product_template where id = prodtmplid ;
            if moldcavity = 0 then
               myres = 0 ;
            else   
               myres = round((blankweight::numeric/moldcavity::numeric),3)::numeric ;
            end if ;   
            select count(*) into ncount from mrp_bom_line where bom_id=bomid and product_id=furnaceprodid ;
            if ncount = 0 then
               if blankweight > 0 then
                  insert into mrp_bom_line(bom_id,product_id,product_qty,product_uom_id) values (bomid,furnaceprodid,myres,3) ;
               end if ;   
            else
               if blankweight > 0 then
                  update mrp_bom_line set product_qty=myres where bom_id=bomid and product_id=furnaceprodid ;
               end if ;   
            end if ;   
          END;$BODY$
          LANGUAGE plpgsql;  """)

        self.env.cr.execute("""drop function if exists chfurnaceloc(mpid int) cascade""")
        self.env.cr.execute("""create or replace function chfurnaceloc(mpid int) returns void as $BODY$
          DECLARE
            furnacelocid int ;
            furnaceprodid int ;
            mympname varchar ;
          BEGIN
            select min(furnace_loc),min(furnace_prod_id) into furnacelocid,furnaceprodid from alldo_acme_iot_company_stockloc ;
            select name into mympname from mrp_production where id = mpid ;
            update stock_move set location_id=furnacelocid where reference=mympname and product_id=furnaceprodid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpartnertype(typename varchar) cascade""")
        self.env.cr.execute("""create or replace function getpartnertype(typename varchar) returns INT as $BODY$
          DECLARE
             ncount int ;
             myres int ;
          BEGIN
             select count(*) into ncount from res_partner_category where name like typename ;
             if ncount > 0 then
                select id into myres from res_partner_category where name like typename ;
             else
                insert into res_partner_category(name,active) values (typename,True) ;
                select max(id) into myres from res_partner_category ;
             end if ;
             return myres ;
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists setprodmold(prodtmplid int,moldid int) cascade""")
        self.env.cr.execute("""create or replace function setprodmold(prodtmplid int,moldid int) returns void as $BODY$
          DECLARE
            ncount int ;
            ncount1 int ;
            myengtype varchar ;
            myminid int ;
          BEGIN
            myengtype='1' ; 
            select count(*) into ncount from alldo_acme_iot_eng_order where prod_id=prodtmplid  ;
            if ncount = 0 then
               insert into alldo_acme_iot_eng_order(prod_id,eng_type,eng_desc) values (prodtmplid,myengtype,'鑄造') ;
            else
               select min(id) into myminid from alldo_acme_iot_eng_order where prod_id=prodtmplid ; 
               select eng_type into myengtype from  alldo_acme_iot_eng_order where id = myminid ; 
            end if ;
            select count(*) into ncount1 from alldo_acme_iot_product_mold where product_id=prodtmplid  ;
            if ncount1 = 0 then
               insert into alldo_acme_iot_product_mold(product_id,eng_type,mold_id,active) values (prodtmplid,myengtype,moldid,True) ;
            else
               select min(id) into myminid from alldo_acme_iot_product_mold where product_id=prodtmplid ; 
               update alldo_acme_iot_product_mold set mold_id=moldid where id = myminid ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists mrpproductionupdate(wono varchar) cascade""")
        self.env.cr.execute("""create or replace function mrpproductionupdate(wono varchar) returns void as $BODY$
          DECLARE
            materiallocid int ;
            prodlocid int ;
            blanklocid int ;
            molocid int ;
            furnacelocid int ;
            furnaceprodid int ;
            uncompletelocid int ;
            woname varchar ;
            mv_cur refcursor ;
            mv_rec record ;
            prodid int ;
            sopi varchar ;
            myorigin varchar ;
            moid int ;
          BEGIN
            select origin,id into myorigin,moid from mrp_production where name=wono ;
            select so_pi into sopi from sale_order where name = myorigin ;
            update mrp_production set so_pi=sopi where id = moid ;
            update alldo_acme_iot_workorder set so_pi=sopi where mrp_prod_id = moid ;
            update alldo_acme_iot_outsuborder set so_pi=sopi where mrp_prod_id = moid ;
            select material_loc,prod_loc,blank_loc,mo_loc,furnace_loc,furnace_prod_id,uncomplete_loc into 
              materiallocid,prodlocid,blanklocid,molocid,furnacelocid,furnaceprodid,uncompletelocid from alldo_acme_iot_company_stockloc ;
            open mv_cur for select id,reference,bom_line_id,picking_type_id from stock_move where reference=wono and picking_type_id = 8 ;
            loop
              fetch mv_cur into mv_rec ;
              exit when not found ;
              if mv_rec.bom_line_id is not null then
                 select product_id into prodid from mrp_bom_line where id = mv_rec.bom_line_id ;
                 if prodid = furnaceprodid then
                    update stock_move set location_id=furnacelocid,location_dest_id=molocid where id = mv_rec.id ;
                    update stock_move_line set location_id=furnacelocid,location_dest_id=molocid where move_id = mv_rec.id ;
                 else
                    update stock_move set location_id=materiallocid,location_dest_id=molocid where id = mv_rec.id ;
                    update stock_move_line set location_id=materiallocid,location_dest_id=molocid where move_id = mv_rec.id ;
                 end if ;
              else
                 update stock_move set location_id=molocid,location_dest_id=uncompletelocid where id = mv_rec.id ;
                 update stock_move_line set location_id=molocid,location_dest_id=uncompletelocid where move_id = mv_rec.id ;
              end if ;   
            end loop ;
            close mv_cur ;  
            update mrp_production set location_src_id=materiallocid,location_dest_id=uncompletelocid where name = wono ; 
            update mrp_production set state='draft' where state is null and name = wono ; 
          /*  delete from stock_move where name=wono and product_qty is null and reference is null ; */
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getproduom(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getproduom(prodid int) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
            prodtmplid int ;
          BEGIN
            select product_tmpl_id into prodtmplid from product_product where id = prodid ;
            select coalesce(uom_id,1) into myres from product_template where id = prodtmplid ;
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql ;""")

        self.env.cr.execute("""drop function if exists getmocusid(sono varchar) cascade""")
        self.env.cr.execute("""create or replace function getmocusid(sono varchar) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            ncount = 0 ;
          
            select count(*) into ncount from sale_order where name = sono ;
            if ncount > 0 then
               select coalesce(partner_id,0) into myres from sale_order where name = sono ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmosaleorderid(sono varchar) cascade""")
        self.env.cr.execute("""create or replace function getmosaleorderid(sono varchar) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            ncount = 0 ;
          
            select count(*) into ncount from sale_order where name = sono ;
            if ncount > 0 then
               select id into myres from sale_order where name = sono ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists autogencastingeng(prodtmplid int) cascade""")
        self.env.cr.execute("""create or replace function autogencastingeng(prodtmplid int) returns void as $BODY$
          DECLARE
            ncount int ;
            ncount1 int ;
            moldid int ;
          BEGIN
            select count(*) into ncount from alldo_acme_iot_eng_order where prod_id=prodtmplid and eng_type='1' ;
            if ncount = 0 then
               insert into alldo_acme_iot_eng_order(prod_id,eng_type,eng_order,eng_desc) values (prodtmplid,'1',1,'鑄件工程') ;
            end if ;
            select count(*) into ncount1 from alldo_acme_iot_product_mold where product_id=prodtmplid and eng_type='1' ;
            select coalesce(mold_id,0) into moldid from product_template where id = prodtmplid ;
            if ncount1 = 0 then
               if moldid > 0 then
                  insert into alldo_acme_iot_product_mold(product_id,eng_type,mold_id,active) values (prodtmplid,'1',moldid,True) ;
               else
                  insert into alldo_acme_iot_product_mold(product_id,eng_type,active) values (prodtmplid,'1',True) ;
               end if ;
            else
               if moldid > 0 then
                  update alldo_acme_iot_product_mold set mold_id=moldid where product_id=prodtmplid and eng_type='1' ;
               end if ;   
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genstocklocproperty() cascade""")
        self.env.cr.execute("""create or replace function genstocklocproperty() returns void as $BODY$
          DECLARE
            par_cur refcursor ;
            par_rec record ;
            myfieldsid int ;
            ncount int ;
            myresid varchar;
            myparentlocpath varchar ;
            myparentlocpath1 varchar ;
            mymaxlocid int ;
            mylocname varchar ;
            mywhlocid int ;
            myloccompletename varchar ;
            myvaluereference varchar ;
          BEGIN
            select id,parent_path into mywhlocid,myparentlocpath from stock_location where name='WH' ;
            select id into myfieldsid from ir_model_fields where name='property_stock_supplier' and model='res.partner' ;
            open par_cur for select id,name from res_partner where is_company=True and supplier_rank = 1 ;
            loop
               fetch par_cur into par_rec ;
               exit when not found ;
               myresid = concat('res.partner,',par_rec.id::TEXT) ;
               update stock_location set parent_path=myparentlocpath1 where id = mymaxlocid ; 
               myvaluereference = 'stock.location,4' ; 
               update ir_property set value_reference=myvaluereference where name='property_stock_supplier' and res_id=myresid 
                  and fields_id=myfieldsid ;
               execute gensuploc(par_rec.id) ;   
            end loop ;
            close par_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gensuploc(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function gensuploc(partnerid int) returns void as $BODY$
          DECLARE
            par_cur refcursor ;
            par_rec record ;
            myfieldsid int ;
            ncount int ;
            myresid varchar;
            myparentlocpath varchar ;
            myparentlocpath1 varchar ;
            mymaxlocid int ;
            mylocname varchar ;
            mywhlocid int ;
            myloccompletename varchar ;
            myvaluereference varchar ;
            supplierrank int ;
          BEGIN
            select supplier_rank into supplierrank from res_partner where id = partnerid ;
            if supplierrank = 1 then   /* 判斷是供應商才執行 */
                select id,parent_path into mywhlocid,myparentlocpath from stock_location where name='WH' ;
                open par_cur for select id,name from res_partner where is_company=True and supplier_rank = 1 ;
                loop
                   fetch par_cur into par_rec ;
                   exit when not found ;
                   mylocname = concat(par_rec.name,'(委外倉)') ;
                   myloccompletename = concat('WH/',par_rec.name,'(委外倉)') ;
                   select count(*) into ncount from stock_location where complete_name like myloccompletename ;
                   if ncount = 0 then   /* 如無記錄自動生成 ir_property */
                      /* 先建立 stock.location 記錄 */ 
                      insert into stock_location(name,complete_name,active,usage,location_id,company_id) values 
                        (mylocname,myloccompletename,True,'internal',mywhlocid,1) ;
                      select max(id) into mymaxlocid from stock_location ;
                      myparentlocpath1 = concat(myparentlocpath,par_rec.id::TEXT,'/') ;
                      update stock_location set parent_path=myparentlocpath1 where id = mymaxlocid ; 
                   else
                      select id into mymaxlocid from stock_location where complete_name like myloccompletename ;
                   end if ;
                   update res_partner set blank_stock_supplier=mymaxlocid where id = par_rec.id ;
                end loop ;
                close par_cur ;
            end if ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpurno(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getpurno(prodid int) returns setof INT as $BODY$
          DECLARE
            pur_cur refcursor ;
            pur_rec record ;
          BEGIN
            open pur_cur for select id,name from purchase_order where id in 
              (select order_id from purchase_order_line where product_id=prodid)
              and state='purchase' order by name desc;
            loop
              fetch pur_cur into pur_rec ;
              exit when not found ;
              return next pur_rec.id ;
            end loop ;
            close pur_cur ;  
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists setmrpprodloc(prodid int,prodqty float) cascade""")
        self.env.cr.execute("""create or replace function setmrpprodloc(prodid int,prodqty float) returns void as $BODY$
          DECLARE
            myid int ;
            uncompletelocid int ;
          BEGIN
          select uncomplete_loc into uncompletelocid from alldo_acme_iot_company_stockloc ;
            select max(id) into myid from stock_quant where product_id=prodid and quantity=prodqty ;
            update stock_quant set location_id=uncompletelocid,reserved_quantity=0 where id = myid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmcategprod() cascade""")
        self.env.cr.execute("""create or replace function getmcategprod() returns setof INT as $BODY$
          DECLARE
            mymcategid int ;
            prod_cur refcursor ;
            prod_rec record ;
          BEGIN
            select m_categ into mymcategid from alldo_acme_iot_company_stockloc ;
            open prod_cur for select A.id,A.product_tmpl_id,B.categ_id from product_product A,product_template B 
              where A.product_tmpl_id = B.id and B.categ_id=mymcategid ;
            loop
               fetch prod_cur into prod_rec ;
               exit when not found ;
               return next prod_rec.id ;
            end loop ;
            close prod_cur ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmaterialonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getmaterialonhand(prodid int) returns float as $BODY$
          DECLARE
             myres float ;
             materialloc int ;
          BEGIN
             select min(material_loc) into materialloc from alldo_acme_iot_company_stockloc ;
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=materialloc and product_id=prodid ;
             if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getprodonhand(prodid int) cascade""")
        self.env.cr.execute("""create or replace function getprodonhand(prodid int) returns float as $BODY$
          DECLARE
             myres float ;
             prodloc int ;
          BEGIN
             select min(prod_loc) into prodloc from alldo_acme_iot_company_stockloc ;
             select sum(quantity) into myres from stock_quant where company_id=1 and location_id=prodloc and product_id=prodid ;
             if myres is null then
                myres = 0 ;
             end if ;
           return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gen_mrp_materialline(moid int) cascade""")
        self.env.cr.execute("""create or replace function gen_mrp_materialline(moid int) returns void as $BODY$
          DECLARE
            m_cur refcursor ;
            m_rec record ;
            bom_cur refcursor ;
            bom_rec record ;
            mixprodid int ;
            m1_cur refcursor ;
            m1_rec record ;
            materialloc int ;
            prodid int ;
            prodtmplid int ;
            blanktmplid int ;
            blankprodid int ;
            blankprodqty float ;
            onhandqty float ;
            needqty float ;
            bomid int ;
            productqty float ;
            setnum int ;
            modnum int ;
            packagingqty int ;
          BEGIN
            delete from alldo_acme_iot_materialline where mrp_prod_id = moid ;
            select product_id,product_qty into prodid,productqty from mrp_production where id = moid ;
            select product_tmpl_id into prodtmplid from product_product where id = prodid ;
            select product_blank1 into blanktmplid from product_template where id = prodtmplid ;
            select id into blankprodid from product_product where product_tmpl_id=blanktmplid ;
            select furnace_prod_id,material_loc into mixprodid,materialloc from alldo_acme_iot_company_stockloc ;
            open m_cur for select * from stock_move where raw_material_production_id = moid ;
            loop
               fetch m_cur into m_rec ;
               exit when not found ;
               if m_rec.product_id = mixprodid then
                  select getmaterialonhand(blankprodid) into onhandqty ;
                  blankprodqty = m_rec.product_uom_qty::numeric * 0.7 ;
                  if onhandqty > blankprodqty then
                     needqty = 0 ;
                  else
                     needqty = onhandqty - blankprodqty ;
                  end if ;
                  insert into alldo_acme_iot_materialline(mrp_prod_id,product_no,product_qty,prod_uom_id,onhand_qty,need_qty) values
                   (moid,blankprodid,blankprodqty,m_rec.product_uom,onhandqty,needqty) ;
               else
                  select getmaterialonhand(m_rec.product_id) into onhandqty ;
                  if onhandqty > m_rec.product_uom_qty then
                     needqty = 0 ;
                  else
                     needqty = onhandqty - m_rec.product_uom_qty ;
                  end if ;
                  insert into alldo_acme_iot_materialline(mrp_prod_id,product_no,product_qty,prod_uom_id,onhand_qty,need_qty) values
                   (moid,m_rec.product_id,m_rec.product_uom_qty,m_rec.product_uom,onhandqty,needqty) ;
               end if ;
            end loop ;
            close m_cur ;
            select id into bomid from mrp_bom where product_tmpl_id = prodtmplid ;
            open bom_cur for select * from alldo_acme_iot_packaging_line where bom_id=bomid ;
            loop
               fetch bom_cur into bom_rec ;
               exit when not found ;
               modnum = (productqty::numeric % bom_rec.m_set_qty::numeric)::INTEGER ;
               setnum = (productqty::numeric/bom_rec.m_set_qty::numeric)::INTEGER ;
               if modnum > 0 then
                  setnum = setnum + 1 ;
               end if ;
               packagingqty = setnum * bom_rec.c_set_qty ;
               select getmaterialonhand(bom_rec.product_id) into onhandqty ;
                  if onhandqty > packagingqty then
                     needqty = 0 ;
                  else
                     needqty = onhandqty - packagingqty ;
                  end if ;
               insert into alldo_acme_iot_materialline(mrp_prod_id,product_no,product_qty,prod_uom_id,onhand_qty,need_qty) values
                (moid,bom_rec.product_id,packagingqty,bom_rec.product_uom_id,onhandqty,needqty) ;
            end loop ;
            close bom_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genmoldtimes(workorderid int) cascade""")
        self.env.cr.execute("""create or replace function genmoldtimes(workorderid int) returns void as $BODY$
          DECLARE
            prodid int ;
            prodtmplid int ;
            moldid int ;
          BEGIN
            select product_no into prodid from alldo_acme_iot_workorder where id = workorderid ;
            select product_tmpl_id into prodtmplid from product_product where id = prodid ;
            select mold_id into moldid from alldo_acme_iot_product_mold where product_id=prodtmplid ;
            update alldo_acme_iot_acme_mold set current_times=coalesce(current_times,0) + 1 where id = moldid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists mo_produce_in(productno varchar,lotno varchar,equipno varchar,scaleweight float,scaleowner varchar)""")
        self.env.cr.execute("""create or replace function mo_produce_in(productno varchar,lotno varchar,equipno varchar,scaleweight float,scaleowner varchar) returns Boolean as $BODY$
          DECLARE
            prodid int ;
            lotid int ;
            quantid int ;
            equipid int ; 
            userid int ;
            ncount int ;  /* product_no */
            ncount1 int ; /* lot_no */
            ncount2 int ; /* maintenance_equipment */
            ncount3 int ; /* emp_no */
            ncount4 int ; /* tracking -> lot */
            myres Boolean ;
            materiallocid int ;
            empid int ;
            prodtmplid int ;
            uomid int ;
            mynowdatetime timestamp ;
            maxid int ;
          BEGIN
            select current_timestamp into mynowdatetime ;
            ncount = 0 ;
            ncount1 = 0 ;
            ncount2 = 0 ;
            ncount3 = 0 ;
            ncount4 = 0 ;
            select count(*) into ncount from product_product where default_code = productno ;
            if ncount > 0 then
               select min(id) into prodid from product_product where default_code = productno ;
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select uom_id into uomid from product_template where id= prodtmplid ;
            end if ;
            if lotno ='' or lotno = ' ' then
               ncount1 = 0 ;
            else
                select count(*) into ncount1 from stock_production_lot where name = lotno ;
                if ncount1 > 0 then
                   select max(id) into lotid from stock_production_lot where name = lotno ;
                   select min(material_loc) into materiallocid from alldo_acme_iot_company_stockloc ;
                   select id into quantid from stock_quant where lot_id = lotid and location_id=materiallocid 
                      and quantity > 0 ;
                end if ;
            end if ;
            select count(*) into ncount2 from maintenance_equipment where equipment_no=equipno and category_id=3 and active=True ;
            if ncount2 > 0 then
               select min(id) into equipid from maintenance_equipment where equipment_no=equipno and category_id=3 and active=True ;
            end if ;
            select count(*) into ncount3 from hr_employee where emp_code=scaleowner and active=True ;
            if ncount3 > 0 then
               select user_id into userid from hr_employee where emp_code=scaleowner and active=True ;
            end if ; 
            if ncount > 0 and ncount1 > 0 and ncount2 > 0 and ncount3 > 0 then
               insert into alldo_acme_iot_electronic_scale(product_no,need_lotno,lot_no,scale_weight,equipment_no,uom_id,scale_owner,scale_type,is_posting,scale_datetime) values
                      (prodid,True,quantid,scaleweight,equipid,uomid,userid,'1','1',mynowdatetime) ;
               myres = True ;       
            elsif ncount > 0 and ncount1 = 0  and ncount2 > 0 and ncount3 > 0 then        
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select count(*) into ncount4 from product_template where id = prodtmplid and tracking='lot' ;
               if ncount4 > 0 then  
                   insert into alldo_acme_iot_electronic_scale(product_no,need_lotno,scale_weight,equipment_no,uom_id,scale_owner,scale_type,is_posting,scale_datetime) values
                          (prodid,True,scaleweight,equipid,uomid,userid,'1','1',mynowdatetime) ;
               else
                    insert into alldo_acme_iot_electronic_scale(product_no,need_lotno,scale_weight,equipment_no,uom_id,scale_owner,scale_type,is_posting,scale_datetime) values
                          (prodid,False,scaleweight,equipid,uomid,userid,'1','1',mynowdatetime) ;
               end if ;
               myres = True ;
            else
               myres = False ;
            end if ;
            select max(id) into maxid from alldo_acme_iot_electronic_scale ;
            execute gendayscale(maxid) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists mo_stock_in(productno varchar,scaleweight float,scaleowner varchar)""")
        self.env.cr.execute("""create or replace function mo_stock_in(productno varchar,scaleweight float,scaleowner varchar) returns Boolean as $BODY$
         DECLARE
           prodid int ;
           ncount int ;
           ncount1 int ;
           prodtmplid int ;
           uomid int ;
           userid int ;
           myres Boolean ;
           mynowdatetime timestamp ;
         BEGIN
            select current_timestamp into mynowdatetime ;
            select count(*) into ncount from product_product where default_code = productno ;
            if ncount > 0 then  /* 料號 */
               select min(id) into prodid from product_product where default_code = productno ;
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select uom_id into uomid from product_template where id= prodtmplid ;
            end if ;
            select count(*) into ncount1 from hr_employee where emp_code=scaleowner and active=True ;
            if ncount1 > 0 then  /* 人員 */
               select user_id into userid from hr_employee where emp_code=scaleowner and active=True ;
            end if ; 
            if ncount > 0 and ncount1 > 0 then
               insert into alldo_acme_iot_electronic_scale(product_no,scale_weight,uom_id,scale_owner,scale_type,is_posting,scale_datetime) values
                 (prodid,scaleweight,uomid,userid,'2','1',mynowdatetime) ;
               myres = True ;  
            elsif ncount > 0 and ncount1 = 0 then
               insert into alldo_acme_iot_electronic_scale(product_no,scale_weight,uom_id,scale_type,is_posting,scale_datetime) values
                 (prodid,scaleweight,uomid,'2','1',mynowdatetime) ;
               myres = True ;  
            else
               myres = False ;
            end if ;
            return myres ;
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
           BEGIN
             qtynum = 0 ;
             select coalesce(mo_group_id,0) into mogroupid  from stock_picking where id = pickingid  ;
             select sum(coalesce(qty_done,0)) into qtynum from stock_move_line where picking_id in
               (select id from stock_picking where mo_group_id=mogroupid and picking_type_id=2) ;
             if mogroupid > 0 then
                if qtynum > 0 then
                    update alldo_acme_iot_workorder set shipping_num = qtynum where mo_group_id = mogroupid ;
                end if ;    
             end if ;
             select max(id) into myworkorderid from alldo_acme_iot_workorder where mo_group_id = mogroupid ;
             select order_num,shipping_num into myordernum,myshippingnum from alldo_acme_iot_workorder where id = myworkorderid ;
             if myordernum > myshippingnum then
                update alldo_acme_iot_workorder set uncomplete_shipping=True where mo_group_id = mogroupid ;
             else
                update alldo_acme_iot_workorder set uncomplete_shipping=False where mo_group_id = mogroupid ;   
             end if ;
             select coalesce(prodout_picking,0) into mynowpickingid from alldo_acme_iot_workorder where id = myworkorderid ;
             if mynowpickingid > 0 then
                select max(id) into mybackorderid from stock_picking where backorder_id = mynowpickingid ; 
                if mybackorderid > 0 then
                   update alldo_acme_iot_workorder set prodout_picking=mybackorderid where mo_group_id = mogroupid ;
                end if ;   
             end if ;   
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatemoldline(nitem int,moldcode varchar) cascade""")
        self.env.cr.execute("""create or replace function updatemoldline(nitem int,moldcode varchar) returns void as $BODY$
           DECLARE
             myid int ;
             ncount int ;
           BEGIN
             select max(id) into myid from alldo_acme_iot_mold_report ;
             if nitem=2 then
                update alldo_acme_iot_mold_report_line set mold_code2=moldcode where mold_id=myid ;
             elsif nitem=3 then
                update alldo_acme_iot_mold_report_line set mold_code3=moldcode where mold_id=myid ;
             elsif nitem=4 then
                update alldo_acme_iot_mold_report_line set mold_code4=moldcode where mold_id=myid ;
             elsif nitem=5 then
                update alldo_acme_iot_mold_report_line set mold_code5=moldcode where mold_id=myid ;
             elsif nitem=6 then
                update alldo_acme_iot_mold_report_line set mold_code6=moldcode where mold_id=myid ;
             elsif nitem=7 then
                update alldo_acme_iot_mold_report_line set mold_code7=moldcode where mold_id=myid ;
             elsif nitem=8 then
                update alldo_acme_iot_mold_report_line set mold_code8=moldcode where mold_id=myid ;
             elsif nitem=9 then
                update alldo_acme_iot_mold_report_line set mold_code9=moldcode where mold_id=myid ;
             elsif nitem=10 then
                update alldo_acme_iot_mold_report_line set mold_code10=moldcode where mold_id=myid ;
             elsif nitem=11 then
                update alldo_acme_iot_mold_report_line set mold_code11=moldcode where mold_id=myid ;
             elsif nitem=12 then
                update alldo_acme_iot_mold_report_line set mold_code12=moldcode where mold_id=myid ;
             elsif nitem=13 then
                update alldo_acme_iot_mold_report_line set mold_code13=moldcode where mold_id=myid ;
             elsif nitem=14 then
                update alldo_acme_iot_mold_report_line set mold_code14=moldcode where mold_id=myid ;
             elsif nitem=15 then
                update alldo_acme_iot_mold_report_line set mold_code15=moldcode where mold_id=myid ;
             elsif nitem=16 then
                update alldo_acme_iot_mold_report_line set mold_code16=moldcode where mold_id=myid ;
             elsif nitem=17 then
                update alldo_acme_iot_mold_report_line set mold_code17=moldcode where mold_id=myid ;
             elsif nitem=18 then
                update alldo_acme_iot_mold_report_line set mold_code18=moldcode where mold_id=myid ;
             elsif nitem=19 then
                update alldo_acme_iot_mold_report_line set mold_code19=moldcode where mold_id=myid ;
             elsif nitem=20 then
                update alldo_acme_iot_mold_report_line set mold_code20=moldcode where mold_id=myid ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists addmoldline(moldcode varchar) cascade""")
        self.env.cr.execute("""create or replace function addmoldline(moldcode varchar) returns void as $BODY$
           DECLARE
             myid int ;
           BEGIN
             select max(id) into myid from alldo_acme_iot_mold_report ;
             insert into alldo_acme_iot_mold_report_line(mold_id,mold_code1) values (myid,moldcode) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatequantline(nitem int,lotcode varchar) cascade""")
        self.env.cr.execute("""create or replace function updatequantline(nitem int,lotcode varchar) returns void as $BODY$
           DECLARE
             myid int ;
             ncount int ;
           BEGIN
             select max(id) into myid from alldo_acme_iot_quant_report ;
             if nitem=2 then
                update alldo_acme_iot_quant_report_line set lot_code2=lotcode where quant_id=myid ;
             elsif nitem=3 then
                update alldo_acme_iot_quant_report_line set lot_code3=lotcode where quant_id=myid ;
             elsif nitem=4 then
                update alldo_acme_iot_quant_report_line set lot_code4=lotcode where quant_id=myid ;
             elsif nitem=5 then
                update alldo_acme_iot_quant_report_line set lot_code5=lotcode where quant_id=myid ;
             elsif nitem=6 then
                update alldo_acme_iot_quant_report_line set lot_code6=lotcode where quant_id=myid ;
             elsif nitem=7 then
                update alldo_acme_iot_quant_report_line set lot_code7=lotcode where quant_id=myid ;
             elsif nitem=8 then
                update alldo_acme_iot_quant_report_line set lot_code8=lotcode where quant_id=myid ;
             elsif nitem=9 then
                update alldo_acme_iot_quant_report_line set lot_code9=lotcode where quant_id=myid ;
             elsif nitem=10 then
                update alldo_acme_iot_quant_report_line set lot_code10=lotcode where quant_id=myid ;
             elsif nitem=11 then
                update alldo_acme_iot_quant_report_line set lot_code11=lotcode where quant_id=myid ;
             elsif nitem=12 then
                update alldo_acme_iot_quant_report_line set lot_code12=lotcode where quant_id=myid ;
             elsif nitem=13 then
                update alldo_acme_iot_quant_report_line set lot_code13=lotcode where quant_id=myid ;
             elsif nitem=14 then
                update alldo_acme_iot_quant_report_line set lot_code14=lotcode where quant_id=myid ;
             elsif nitem=15 then
                update alldo_acme_iot_quant_report_line set lot_code15=lotcode where quant_id=myid ;
             elsif nitem=16 then
                update alldo_acme_iot_quant_report_line set lot_code16=lotcode where quant_id=myid ;
             elsif nitem=17 then
                update alldo_acme_iot_quant_report_line set lot_code17=lotcode where quant_id=myid ;
             elsif nitem=18 then
                update alldo_acme_iot_quant_report_line set lot_code18=lotcode where quant_id=myid ;
             elsif nitem=19 then
                update alldo_acme_iot_quant_report_line set lot_code19=lotcode where quant_id=myid ;
             elsif nitem=20 then
                update alldo_acme_iot_quant_report_line set lot_code20=lotcode where quant_id=myid ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists addquantline(lotcode varchar) cascade""")
        self.env.cr.execute("""create or replace function addquantline(lotcode varchar) returns void as $BODY$
           DECLARE
             myid int ;
           BEGIN
             select max(id) into myid from alldo_acme_iot_quant_report ;
             insert into alldo_acme_iot_quant_report_line(quant_id,lot_code1) values (myid,lotcode) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists chkhaveprod(defcode varchar) cascade""")
        self.env.cr.execute("""create or replace function chkhaveprod(defcode varchar) returns Boolean as $BODY$
           DECLARE
             myres Boolean ;
             ncount int ;
           BEGIN
             select count(*) into ncount from product_product where default_code=defcode ;
             if ncount > 0 then
                myres = True ;
             else
                myres = False ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists genpackagingbom(mypackagingno varchar,myprodno varchar,prodset int,childset int) cascade""")
        self.env.cr.execute("""create or replace function genpackagingbom(mypackagingno varchar,myprodno varchar,prodset int,childset int) returns void as $BODY$
          DECLARE
            ncount int ;
            ncount1 int;
            packagingid int ;
            prodid int ;
            ncount2 int ;
            bomid int;
            prodtmplid int;
          BEGIN
            select count(*) into ncount from product_product where trim(default_code)=trim(mypackagingno);
            if ncount > 0 then
               select id into packagingid from product_product where trim(default_code)=trim(mypackagingno);
            end if ;
            select count(*) into ncount1 from product_product where trim(default_code)=trim(myprodno);
            if ncount1 > 0 then
               select id into prodid from product_product where trim(default_code)=trim(myprodno);
            end if ;
            if ncount > 0 and ncount1 > 0 then
               select product_tmpl_id into prodtmplid from product_product where id = prodid ;
               select id into bomid from mrp_bom where product_tmpl_id = prodtmplid ;
               select count(*) into ncount2 from alldo_acme_iot_packaging_line where bom_id=bomid and 
                   product_id = packagingid ;
               if ncount2 = 0 then
                  insert into alldo_acme_iot_packaging_line(bom_id,product_id,product_uom_id,m_set_qty,c_set_qty) 
                      values (bomid,packagingid,1,prodset,childset) ;
               else
                  update alldo_acme_iot_packaging_line set m_set_qty=prodset,c_set_qty=childset where bom_id=bomid and 
                     product_id = packagingid ;
               end if ;    
            end if ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getislotno(mycode varchar) cascade""")
        self.env.cr.execute("""create or replace function getislotno(mycode varchar) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
            mylotid int ;
            ncount1 int ;
          BEGIN
            select count(*) into ncount from stock_production_lot where name=mycode ;
            if ncount > 0 then
               myres = True ;               
            else
               myres = False ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getisprodno(mycode varchar) cascade""")
        self.env.cr.execute("""create or replace function getisprodno(mycode varchar) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
          BEGIN
            select count(*) into ncount from product_product where default_code = mycode and active=True;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getsupplierprod(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getsupplierprod(partnerid int) returns setof INT as $BODY$
          DECLARE
            ncount int ;
            out_cur refcursor ;
            out_rec record ;
          BEGIN
            open out_cur for select distinct product_no from alldo_acme_iot_partner_prodout where partner_id=partnerid ;
            loop
              fetch out_cur into out_rec ;
              exit when not found ;
              return next out_rec.product_no ;
            end loop ;
            close out_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop view if exists alldo_acme_iot_ngreturn_view cascade ;""")

        self.env.cr.execute("""CREATE OR REPLACE VIEW alldo_acme_iot_ngreturn_view AS
            SELECT QC.order_id,QC.prodin_datetime,QC.in_ng_num,QC.in_good_num,SUB.cus_name,SUB.name,SUB.product_no
            from alldo_acme_iot_outsuborder_prodin QC left join alldo_acme_iot_outsuborder SUB
             on QC.order_id = SUB.id where (coalesce(QC.in_ng_num,0) > 0 or coalesce(QC.in_good_num,0) > 0) order by prodin_datetime::DATE,name""")

        self.env.cr.execute(
            """drop function if exists genngreturnexcel(partnerid int,prodid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function genngreturnexcel(partnerid int,prodid int,startdate date,enddate date) returns void as $BODY$
         DECLARE
           ng_cur refcursor ;
           ng_rec record ; 
           outng_cur refcursor ;
           outng_rec record ;
           mydate varchar ;
           mytype char ;
         BEGIN
           delete from alldo_acme_iot_ngreturn_list ;
           if prodid = 0 then
              open ng_cur for select * from alldo_acme_iot_ngreturn_view where prodin_datetime::DATE >= startdate and prodin_datetime::DATE <= enddate and cus_name=partnerid   ;
           else
             open ng_cur for select * from alldo_acme_iot_ngreturn_view where prodin_datetime::DATE >= startdate and prodin_datetime::DATE <= enddate and cus_name=partnerid and  
              (product_no=prodid) ;
           end if ;
           loop
             fetch ng_cur into ng_rec ;
             exit when not found ;
             select ng_rec.prodin_datetime::DATE::TEXT into mydate ;
             mytype = '2' ;   /* 托工NG */
             insert into alldo_acme_iot_ngreturn_list(name,partner_id,ngreturn_date,ngreturn_date1,product_id,processing_ng_num,ngreturn_type,return_good_num) values
               (ng_rec.name,ng_rec.cus_name,ng_rec.prodin_datetime::DATE,mydate,ng_rec.product_no,ng_rec.in_ng_num,mytype,ng_rec.in_good_num) ;
           end loop ;
           close ng_cur ;  
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists gen_accountmove(partnerid int,startdate date,enddate date) cascade""")
        self.env.cr.execute("""create or replace function gen_accountmove(partnerid int,startdate date,enddate date) returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
           invl_cur refcursor ;
           invl_rec record ;
           mynowdate date ;
           mynowdate1 varchar ;
           myreportid int ;
           prodtmplid int ;
           proddesc varchar ;
           sedate varchar ;
         BEGIN
           select (current_timestamp + interval '8 hours')::DATE into mynowdate ;
           select mynowdate::TEXT into mynowdate1 ;
           /*  delete from alldo_acme_iot_accountmove_selectitem_line ; */
           delete from alldo_acme_iot_accountmove_selectitem ;
           sedate = concat(startdate::TEXT,' ~ ',enddate::TEXT) ;
           insert into alldo_acme_iot_accountmove_selectitem(report_date,partner_id,report_date1,startenddate) values (mynowdate,partnerid,mynowdate1,sedate) ;
           select max(id) into myreportid from alldo_acme_iot_accountmove_selectitem ;
           open inv_cur for select * from account_move where partner_id=partnerid and state='posted' and report_no is null and amount_residual_signed > 0 and type='out_invoice' 
              and date::DATE between startdate::DATE and enddate::DATE ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             open invl_cur for select * from account_move_line where move_id = inv_rec.id and product_id is not null;
             loop
                fetch invl_cur into invl_rec ;
                exit when not found ;
                select product_tmpl_id into prodtmplid from product_product where id = invl_rec.product_id ;
                proddesc = ' ' ;
                select name into proddesc from product_template where id = prodtmplid ;
                insert into alldo_acme_iot_accountmove_selectitem_line(move_id,account_date,ref,sales_no,prod_no,prod_desc,uom_id,prod_num,prod_price,tax_type,amount_untax_num,amount_tax_num,account_move_line_id) values
                 (myreportid,inv_rec.date,inv_rec.name,inv_rec.invoice_origin,invl_rec.product_id,proddesc,invl_rec.product_uom_id,invl_rec.quantity,invl_rec.price_unit,invl_rec.tax_line_id,invl_rec.price_subtotal,invl_rec.price_total,invl_rec.id) ;
             end loop ;
             close invl_cur ;
           end loop ;
           close inv_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gen_accountmove1(partnerid int,reportno varchar) cascade""")
        self.env.cr.execute("""create or replace function gen_accountmove1(partnerid int,reportno varchar) returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
           invl_cur refcursor ;
           invl_rec record ;
           mynowdate date ;
           mynowdate1 varchar ;
           myreportid int ;
           prodtmplid int ;
           proddesc varchar ;
           untaxamounttot float ;
           taxtot float ;
           taxamounttot float ;
           startdate date ;
           enddate date ;
           sedate varchar ;
         BEGIN
           select (current_timestamp + interval '8 hours')::DATE into mynowdate ;
           select mynowdate::TEXT into mynowdate1 ;
           delete from alldo_acme_iot_accountmove_selectitem ;
           insert into alldo_acme_iot_accountmove_selectitem(report_date,partner_id,report_date1) values (mynowdate,partnerid,mynowdate1) ;
           select max(id) into myreportid from alldo_acme_iot_accountmove_selectitem ;
           untaxamounttot = 0 ;
           taxtot = 0 ;
           taxamounttot = 0 ;
           select min(date),max(date) into startdate,enddate from account_move where partner_id=partnerid and report_no=reportno;
           open inv_cur for select * from account_move where partner_id=partnerid and report_no=reportno;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             sedate = concat(startdate::DATE::TEXT,' ~ ',enddate::DATE::TEXT) ;
             open invl_cur for select * from account_move_line where move_id = inv_rec.id and product_id is not null;
             loop
                fetch invl_cur into invl_rec ;
                exit when not found ;
                select product_tmpl_id into prodtmplid from product_product where id = invl_rec.product_id ;
                proddesc = ' ' ;
                select name into proddesc from product_template where id = prodtmplid ;
                untaxamounttot = untaxamounttot + coalesce((invl_rec.price_subtotal),0) ;
                taxamounttot = taxamounttot + coalesce(invl_rec.price_total,0) ;
                insert into alldo_acme_iot_accountmove_selectitem_line(move_id,account_date,ref,sales_no,prod_no,prod_desc,uom_id,prod_num,prod_price,tax_type,amount_untax_num,amount_tax_num,account_move_line_id,selectyn) values
                 (myreportid,inv_rec.date,inv_rec.name,inv_rec.invoice_origin,invl_rec.product_id,proddesc,invl_rec.product_uom_id,invl_rec.quantity,invl_rec.price_unit,invl_rec.tax_line_id,invl_rec.price_subtotal,invl_rec.price_total,invl_rec.id,True) ;
             end loop ;
             close invl_cur ;
           end loop ;
           close inv_cur ;
           taxtot = taxamounttot - untaxamounttot ;
           update alldo_acme_iot_accountmove_selectitem set amount_untax_total=untaxamounttot,amount_tax_total=taxamounttot,
               amount_tax=taxtot,name=reportno,startenddate=sedate where id = myreportid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getaccountseq(mytype varchar) cascade""")
        self.env.cr.execute("""create or replace function getaccountseq(mytype varchar) returns varchar as $BODY$
         DECLARE
           ncount int ;
           mynowdate date ;
           myyear varchar ;
           mymonth varchar ;
           myday varchar ;
           mynum int ;
           cnum varchar ;
           myid int ;
           myres varchar ;
         BEGIN
           select current_timestamp::DATE into mynowdate ;
           select lpad(substring(date_part('year',mynowdate)::TEXT,3,2),2,'0') into myyear ;
           select lpad(date_part('month',mynowdate)::TEXT,2,'0') into mymonth ;
           select lpad(date_part('day',mynowdate)::TEXT,2,'0') into myday ;
           select count(*) into ncount from alldo_acme_iot_account_seq where seq_type=mytype and seq_date=mynowdate ;
           if ncount = 0 then
              insert into alldo_acme_iot_account_seq(seq_type,seq_date,seq_num) values (mytype,mynowdate,2) ;
              myres = concat(mytype,myyear,mymonth,myday,'01') ;
           else
              select id,seq_num into myid,mynum from alldo_acme_iot_account_seq where seq_type=mytype and seq_date=mynowdate ;
              cnum = lpad(mynum::TEXT,2,'0') ;
              myres = concat(mytype,myyear,mymonth,myday,cnum) ;
              update alldo_acme_iot_account_seq set seq_num=seq_num + 1 where id = myid ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genaccountarno() cascade""")
        self.env.cr.execute("""drop function if exists genaccountarno(reportno varchar) cascade""")
        self.env.cr.execute("""create or replace function genaccountarno(reportno varchar) returns void as $BODY$
         DECLARE
           myarno varchar ;
           ar_cur refcursor ;
           ar_rec record ;
           accmoveid int ;
         BEGIN
           /* select max(name) into myarno from alldo_acme_iot_accountmove_selectitem ; */
           open ar_cur for select * from alldo_acme_iot_accountmove_selectitem_line where selectyn=True ;
           loop
             fetch ar_cur into ar_rec ;
             exit when not found ;
             select move_id into accmoveid from account_move_line where id = ar_rec.account_move_line_id ;
             update account_move set report_no=reportno where id = accmoveid ;
           end loop ;
           close ar_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getpartnerresidual(partnerid int) cascade""")
        self.env.cr.execute("""create or replace function getpartnerresidual(partnerid int) returns float as $BODY$
         DECLARE
          myres float ;
         BEGIN
          select sum(coalesce(amount_residual_signed,0)) into myres from account_move where partner_id=partnerid and type='out_invoice'
             and state='posted' ;
          if myres is null then
             myres = 0 ;
          end if ;   
          return myres ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatetaiwanreceipt(itemid int) cascade""")
        self.env.cr.execute("""create or replace function updatetaiwanreceipt(itemid int) returns void as $BODY$
         DECLARE
           sel_cur refcursor ;
           sel_rec record ;
           taiwanreceipt varchar ;
           moveid int ;
         BEGIN
           select taiwan_receipt into taiwanreceipt from alldo_acme_iot_accountmove_selectitem where id = itemid ;
           open sel_cur for select * from alldo_acme_iot_accountmove_selectitem_line where move_id=itemid and selectyn = True ;
           loop
             fetch sel_cur into sel_rec ;
             exit when not found ;
             if taiwanreceipt is not null then 
                select move_id into moveid from account_move_line where id = sel_rec.account_move_line_id ;
                update account_move set taiwan_receipt = taiwanreceipt where id = moveid ;
             end if ;   
           end loop ;
           close sel_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmaterialno() cascade""")
        self.env.cr.execute("""create or replace function getmaterialno() returns setof INT as $BODY$
         DECLARE
           mcateg int ;
           rcateg int ;
           pt_cur refcursor ;
           pt_rec record ;
           prodid int ;
         BEGIN
           select max(m_categ),max(r_categ) into mcateg,rcateg from alldo_acme_iot_company_stockloc ;
           open pt_cur for select id,categ_id from product_template where categ_id = mcateg or categ_id = rcateg ;
           loop
              fetch pt_cur into pt_rec ;
              exit when not found ;
              select id into prodid from product_product where product_tmpl_id = pt_rec.id ;
              return next prodid ;
           end loop ;
           close pt_cur ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self.env.cr.execute(
            """drop function if exists genscalemovemixsearch(startdate date,enddate date,prodid int) cascade""")
        self.env.cr.execute(
            """drop function if exists genscalemovemixsearch(startdate date,enddate date,prodid int,scaletype char) cascade""")
        self.env.cr.execute("""create or replace function genscalemovemixsearch(startdate date,enddate date,prodid int,scaletype char) returns void as $BODY$
         DECLARE
           sca_cur refcursor ;
           sca_rec record ;
           ncount int ;
         BEGIN
            delete from alldo_acme_iot_mixsearch_scalemovelist ;
           if prodid = 0 and scaletype='0' then
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE and is_posting='2';
           elsif prodid = 0 and scaletype='1' then
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE 
                   and is_posting='2' and scale_type='1' ;
           elsif prodid = 0 and scaletype='2' then
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE 
                   and is_posting='2' and scale_type='2' ;
           elsif prodid > 0 and scaletype='0' then
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE and product_no=prodid 
                   and is_posting='2' ;
           elsif prodid > 0 and scaletype='1' then
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE and product_no=prodid 
                   and is_posting='2' and scale_type='1' ;
           elsif prodid > 0 and scaletype='2' then   
              open sca_cur for select * from alldo_acme_iot_electronic_scale where scale_datetime::DATE between startdate::DATE and enddate::DATE and product_no=prodid 
                   and is_posting='2' and scale_type='2' ;
           end if ;
           loop
             fetch sca_cur into sca_rec ;
             exit when not found ;
             insert into alldo_acme_iot_mixsearch_scalemovelist(scale_type,product_no,need_lotno,lot_no,scale_weight,equipment_no,uom_id,scale_owner,picking_no,scale_datetime) values
              (sca_rec.scale_type,sca_rec.product_no,sca_rec.need_lotno,sca_rec.lot_no,sca_rec.scale_weight,sca_rec.equipment_no,sca_rec.uom_id,sca_rec.scale_owner,sca_rec.picking_no,sca_rec.scale_datetime) ;
           end loop ;
           close sca_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatemomarkupratio(saleid int) cascade""")
        self.env.cr.execute("""drop function if exists updatemomarkupratio() cascade""")
        self.env.cr.execute("""create or replace function updatemomarkupratio(saleid int) returns void as $BODY$
         DECLARE
           saleno varchar ;
           sa_cur refcursor ;
           sa_rec record ;
           sal_cur refcursor ;
           sal_rec record ;
           markupratio float ;
           mymoid int ;
           mynowqty float ;
           mymoname varchar ;
           prodtmplid int ;
           prodonhand float ;
         BEGIN
           select name into saleno from sale_order where id = saleid ;
           open sal_cur for select * from sale_order_line where order_id = saleid ;
           loop
             fetch sal_cur into sal_rec ;
             exit when not found ;
             select product_tmpl_id into prodtmplid from product_product where id = sal_rec.product_id ;
             select ng_ratio::INT into markupratio from product_template where id = prodtmplid ;
             mynowqty = sal_rec.product_uom_qty + (sal_rec.product_uom_qty::INT * markupratio::INT / 100)::INT ;
             select id into mymoid from mrp_production where product_id=sal_rec.product_id and origin=saleno  ;
             if mymoid is not null then
                select getprodonhand(sal_rec.product_id) into prodonhand ;
                update mrp_production set product_qty = (mynowqty - prodonhand) where id = mymoid ;
                execute resetproductionnum(mymoid) ;
                execute gen_mrp_materialline(mymoid) ;
             end if ;
           end loop ;
           close sal_cur ;
           update sale_order set is_update_markup=True where id = saleid ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists resetproductionnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function resetproductionnum(moid int) returns void as $BODY$
         DECLARE
           boml_cur refcursor ;
           boml_rec record ;
           bomid int ;
           prodqty float ;
           prodmaterialnum float ;
           rawmaterialnum float ;
           bomlprodid int ;
           bomlprodqty float ;
           moldcavity int ;
           moldid int ;
           prodtmplid int ;
           prodid int ;
           furnaceprodid int ;
         BEGIN
           select max(furnace_prod_id) into furnaceprodid from alldo_acme_iot_company_stockloc ;
           select bom_id,product_qty,product_id into bomid,prodqty,prodid from mrp_production where id = moid ;
           open boml_cur for select * from mrp_bom_line where bom_id = bomid ;
           loop
             fetch boml_cur into boml_rec ;
             exit when not found ;
             select product_tmpl_id into prodtmplid from product_product where id = prodid ;
             prodmaterialnum = boml_rec.product_qty::numeric * prodqty::numeric ;
             if boml_rec.product_id = furnaceprodid then
                rawmaterialnum = round((prodmaterialnum::numeric * 0.7),2) ;
             else
                rawmaterialnum = prodmaterialnum ;
             end if ;   
             update stock_move set product_uom_qty=prodmaterialnum where raw_material_production_id=moid and product_id=boml_rec.product_id  ;
             update alldo_acme_iot_materialline set product_qty=rawmaterialnum where mrp_prod_id=moid and product_no=boml_rec.product_id  ;
           end loop ;
           close boml_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updatetodaynum() cascade""")
        self.env.cr.execute("""create or replace function updatetodaynum() returns void as $BODY$
         DECLARE
           equ_cur refcursor ;
           equ_rec record ;
           todaynum int ;
           mynowtoday date ;
         BEGIN
           select current_timestamp::DATE into mynowtoday ;
           open equ_cur for select id,category_id from maintenance_equipment where category_id=2 ;
           loop
              fetch equ_cur into equ_rec ;
              exit when not found ;
              select sum(coalesce(iot_num,0))::INT into todaynum from alldo_acme_iot_equipment_iot_data where iot_id = 
                 equ_rec.id and (iot_datetime + interval '8 hours')::DATE  = mynowtoday ;
              update maintenance_equipment set today_prodnum=todaynum where id = equ_rec.id ;   
           end loop ;
           close equ_cur ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getmopreprodnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function getmopreprodnum(moid int) returns INT as $BODY$
         DECLARE
           iot_cur refcursor ;
           iot_rec record ;
           ncount int ;
           myres int ;
         BEGIN
           update alldo_acme_iot_workorder_iot_data set is_select=False where is_select=True and order_id = moid ;
           select count(*) into ncount from alldo_acme_iot_workorder_iot_data where (is_posting is null or is_posting=False) 
              and order_id = moid ;
           if ncount > 0 then
              update alldo_acme_iot_workorder_iot_data set is_select=True where (is_posting is null or is_posting=False) and order_id = moid ;
              select sum(coalesce(iot_num,0)) into myres from alldo_acme_iot_workorder_iot_data where (is_posting is null or is_posting=False) and 
                is_select = True and order_id = moid ;
           else
               myres = 0 ;  
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists completepreprodnum(moid int) cascade""")
        self.env.cr.execute("""create or replace function completepreprodnum(moid int) returns void as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_workorder_iot_data where is_select=True and order_id=moid ;
           if ncount > 0 then
              update alldo_acme_iot_workorder_iot_data set is_posting=True where order_id=moid and is_select=True ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkorderqcrecord(moid int,ngnum float) cascade""")
        self.env.cr.execute("""create or replace function genwkorderqcrecord(moid int,ngnum float) returns void as $BODY$
          DECLARE
             qcdate date ;
             myqclineid int ;
             totamount float ;
             qcngnum float ;
             qcgoodnum float ;
             mynowngnum float ;
             mynowgoodnum float ;
             prodoutid int ;
          BEGIN
             select ((current_timestamp + interval '8 hours')::DATE - interval '1 days') into qcdate ; 
             select max(id) into myqclineid from alldo_acme_iot_workorder_qc where order_id=moid and qc_date::DATE = qcdate::DATE ;
             if myqclineid is null then
                select max(id) into myqclineid from alldo_acme_iot_workorder_qc where order_id=moid ;
             end if ;
             select coalesce(processing_ng_num,0),coalesce(qc_good_num,0) into qcngnum,qcgoodnum from alldo_acme_iot_workorder_qc where id = myqclineid ;
             mynowngnum = qcngnum + ngnum ;
             totamount = qcgoodnum - mynowngnum ;
             update alldo_acme_iot_workorder_qc set processing_ng_num=mynowngnum where id = myqclineid ;
             select max(id) into prodoutid from alldo_acme_iot_wkorder_prodout where order_id=moid and prodout_datetime::DATE = qcdate::DATE ;
             if prodoutid is null then
                 select max(id) into prodoutid from alldo_acme_iot_wkorder_prodout where order_id=moid ;
             end if ;
             update alldo_acme_iot_wkorder_prodout set out_good_num=totamount where id = prodoutid ;
          END;$BODY$
          LANGUAGE plpgsql ;""")

        self.env.cr.execute(
            """drop function if exists updatesuborderframe(subid int,outframe1 int,outframe2 int,outpallet int) cascade""")
        self.env.cr.execute("""create or replace function updatesuborderframe(subid int,outframe1 int,outframe2 int,outpallet int) returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update alldo_acme_iot_outsuborder set out_plastic_frame1 = coalesce(out_plastic_frame1,0) + coalesce(outframe1,0),out_plastic_frame2 = coalesce(out_plastic_frame2,0) + coalesce(outframe2,0),
                 out_pallet = coalesce(out_pallet,0) + coalesce(outpallet,0) where id = subid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists updatesuborderframe1(subid int,inframe1 int,inframe2 int,inpallet int) cascade""")
        self.env.cr.execute("""create or replace function updatesuborderframe1(subid int,inframe1 int,inframe2 int,inpallet int) returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update alldo_acme_iot_outsuborder set in_plastic_frame1 = coalesce(in_plastic_frame1,0) + coalesce(inframe1,0),in_plastic_frame2 = coalesce(in_plastic_frame2,0) + coalesce(inframe2,0),
                 in_pallet = coalesce(in_pallet,0) + coalesce(inpallet,0) where id = subid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists updatesuborderframe2(subid1 int,subid2 int,tframe1 int,tframe2 int,tpallet int) cascade""")
        self.env.cr.execute("""create or replace function updatesuborderframe2(subid1 int,subid2 int,tframe1 int,tframe2 int,tpallet int) returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update alldo_acme_iot_outsuborder set in_plastic_frame1 = coalesce(in_plastic_frame1,0) + coalesce(tframe1,0),in_plastic_frame2 = coalesce(in_plastic_frame2,0) + coalesce(tframe2,0),
                 in_pallet = coalesce(in_pallet,0) + coalesce(tpallet,0) where id = subid1 ;
            update alldo_acme_iot_outsuborder set out_plastic_frame1 = coalesce(out_plastic_frame1,0) + coalesce(tframe1,0),out_plastic_frame2 = coalesce(out_plastic_frame2,0) + coalesce(tframe2,0),
                 out_pallet = coalesce(out_pallet,0) + coalesce(tpallet,0) where id = subid2 ;     
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genqcngnum(ngtype char,noid int,ngnum float) cascade""")
        self.env.cr.execute(
            """drop function if exists genqcngnum(ngtype char,noid int,ngnum float,ngmemo varchar,inowner int) cascade""")
        self.env.cr.execute("""create or replace function genqcngnum(ngtype char,noid int,ngnum float,ngmemo varchar,inowner int) returns void as $BODY$
         DECLARE
           ncount int ;
           currentdatetime timestamp ;
           prodid int ;
           empid int ;
           nowday date ;
         BEGIN
           select current_timestamp into currentdatetime ;
           select current_timestamp::DATE into nowday ;
           if ngtype='2' then
              select count(*) into ncount from alldo_acme_iot_outsuborder where id = noid ;
              if ncount > 0 then
                 select product_no into prodid from alldo_acme_iot_outsuborder where id = noid ;
                 insert into alldo_acme_iot_outsuborder_prodin(order_id,prodin_datetime,in_good_num,in_ng_num,in_loc,product_no,in_owner,date_delivery) values
                   (noid,currentdatetime::DATE,0,ngnum,ngmemo,prodid,inowner,nowday) ;
              end if ;
           else
              select count(*) into ncount from alldo_acme_iot_workorder where id = noid ;
              if ncount > 0 then
                 select product_no into prodid from alldo_acme_iot_workorder where id = noid ;
                 select id into empid from hr_employee where user_id=inowner ;
                 insert into alldo_acme_iot_workorder_qc(order_id,qc_date,qc_good_num,processing_ng_num,line_memo,product_no,iot_owner1) values
                   (noid,currentdatetime::DATE,0,ngnum,ngmemo,prodid,empid) ;
              end if ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists updatemowkman(nodename varchar,wkorder varchar,empno1 varchar,empno2 varchar) cascade""")
        self.env.cr.execute("""create or replace function updatemowkman(nodename varchar,wkorder varchar,empno1 varchar,empno2 varchar) returns void as $BODY$
         DECLARE
           ncount int ;
           nodeid int ;
           wkorderid int ;
           wkdatetime timestamp ;
           empid1 int ;
           empid2 int ;
         BEGIN
           select current_timestamp into wkdatetime ;
           select id into nodeid from maintenance_equipment where equipment_no = nodename ;
           select id into wkorderid from alldo_acme_iot_workorder where name=wkorder ;
           select count(*) into ncount from alldo_acme_iot_workorder_lastwork where equipment_id=nodeid and workorder_id=wkorderid ;
           select id into empid1 from hr_employee where emp_code=empno1 ;
           select id into empid2 from hr_employee where emp_code=empno2 ;
           if ncount > 0 then
              update alldo_acme_iot_workorder_lastwork set work_datetime=wkdatetime,iot_owner=empid1,iot_owner1=empid2 where equipment_id=nodeid and workorder_id=wkorderid ;
           else
              insert into alldo_acme_workorder_lastwork(work_datetime,equipment_id,workorder_id,iot_owner,iot_owner1) values
                (wkdatetime,nodeid,wkorderid,empid1,empid2) ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getsuborderprod(prodid int,engtype varchar) cascade""")
        self.env.cr.execute("""create or replace function getsuborderprod(prodid int,engtype varchar) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           mydcode varchar ;
           mydcode1 varchar ;
           myengdesc varchar ;
           myprodtmplid int ;
           myprodtmplid1 int ;
         BEGIN
           select product_tmpl_id,default_code into myprodtmplid,mydcode from product_product where id = prodid ;
           select product_blank1 into myprodtmplid1 from product_template where id = myprodtmplid ;
           select default_code into mydcode1 from product_template where id = myprodtmplid1 ;
           select eng_desc into myengdesc from alldo_acme_iot_eng_order where prod_id = myprodtmplid and substring(eng_type,1,1)=substring(engtype,1,1) ;
           myres = concat('[',mydcode,'] ',mydcode1,'-(',myengdesc,')') ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genlastoutsuborder(subid int) cascade""")
        self.env.cr.execute("""create or replace function genlastoutsuborder(subid int) returns void as $BODY$
         DECLARE
           lastdate date ;
           outdatetime timestamp ;
           lastnum int ;
           prodno int ;
         BEGIN
           update alldo_acme_iot_outsuborder_prodout set last_record = False where order_id = subid ;
           select max(prodout_datetime) into outdatetime from alldo_acme_iot_outsuborder_prodout where order_id = subid ;
           lastdate = outdatetime::DATE ;
           update alldo_acme_iot_outsuborder_prodout set last_record = True where order_id = subid and prodout_datetime::DATE = lastdate::DATE ;
           select sum(coalesce(out_good_num,0))::INT into lastnum from alldo_acme_iot_outsuborder_prodout where last_record = True and order_id=subid ;
           update alldo_acme_iot_outsuborder set last_blank_num=lastnum where id = subid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists iotresettime() cascade""")
        self.env.cr.execute("""create or replace function iotresettime() returns void as $BODY$
          DECLARE
            mynowdate date ;
            mynextdate date ;
            mycurrenttime timestamp ;
            myhms varchar ;
            mycdate varchar ;
            mycdate1 varchar ;
            mydatetime timestamp ;
            restartfreq int ;
            mynextrestarttime timestamp ;
          BEGIN
            select current_timestamp into mycurrenttime ;
            select current_timestamp::DATE + interval '1 days' into mynowdate ;
            select restart_time,restart_freq,next_run_restart into mycdate1,restartfreq,mynextrestarttime from alldo_acme_iot_restartiot_setting;
            mynextrestarttime = mynextrestarttime::timestamp + '1 days' ;
            mynextrestarttime = concat(mynextrestarttime::DATE::TEXT,' ',mycdate1)::timestamp - interval '8 hours' ;
            update alldo_acme_iot_restartiot_setting set next_run_restart = mynextrestarttime  ;
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
          BEGIN
            select current_timestamp::timestamp into mycurrenttime ;
            select current_timestamp::DATE into mynowdate ;
            select current_timestamp::timestamp + interval '30 seconds' into mycurrenttime1 ; 
            select count(*) into ncount from alldo_acme_iot_restartiot_setting where next_run_restart::timestamp < mycurrenttime1::timestamp ;
            if ncount > 0 then
              execute iotresettime() ;
              myres = 'YES' ;
            end if ;
            if myres is null then
               myres = 'NO' ;
            end if ;
            return myres ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gencastprepstart(mono varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastprepstart(mono varchar,empno varchar) returns varchar as $BODY$
          DECLARE
            CAST_PREP_START varchar ;
            CAST_PREP_END varchar ;
            CAST_BAKE_START varchar ;
            CAST_BAKE_END varchar ;
            mynowdate date ;
            mynowdatetime timestamp ;
            mynowdatetime1 timestamp ;
            mytime varchar ;
            myworktime varchar ;
            ncount int ;
            mywkid int ;
            myempid int ;
            myrepid int ;
            mydate varchar ;
             myres varchar ;
          BEGIN
             select id into mywkid from alldo_acme_iot_workorder where name=mono ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='P' and order_id=mywkid ;
             if ncount > 0 then
                select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='P' and order_id=mywkid ;
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                 execute recalreplinetime(myrepid) ;
             end if ;
             insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,replace_start_datetime,create_date,replace_type)
                 values (mywkid,myempid,mynowdatetime,mynowdatetime,'P') ;
             return myworktime ;    
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists gencastprepend(mono varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastprepend(mono varchar,empno varchar) returns varchar as $BODY$
          DECLARE
            mynowdate date ;
            mynowdatetime timestamp ;
            mynowdatetime1 timestamp ;
            mytime varchar ;
            myworktime varchar ;
            ncount int ;
            mywkid int ;
            myempid int ;
            myrepid int ;
            mydate varchar ;
            myres varchar ; 
          BEGIN
             select id into mywkid from alldo_acme_iot_workorder where name=mono ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='P' and order_id=mywkid ;
             if ncount > 0 then
                select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='P' and order_id=mywkid ;
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                myres = myworktime ;
                execute recalreplinetime(myrepid) ; 
             else
                myres = ' ' ;   
             end if ;
             return myres;  
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists gencastbakestart(nodeno varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastbakestart(nodeno varchar,empno varchar) returns varchar as $BODY$
          DECLARE
             mynowdate date ;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             mytime varchar ;
             myworktime varchar ;
             ncount int ;
             mywkid int ;
             myempid int ;
             mynodeid int ;
             mydate varchar ;
             myres varchar ;
             myrepid int ;
          BEGIN
             select id,mo_no into mynodeid,mywkid from maintenance_equipment where equipment_no = nodeno ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='B' and order_id=mywkid ;
             if ncount > 0 then
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where replace_end_datetime is null and replace_type='B' and order_id=mywkid  ;
             end if ;
             insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,replace_start_datetime,create_date,replace_type)
                 values (mywkid,myempid,mynowdatetime,mynowdatetime,'B') ;
             update maintenance_equipment set iot_status='3' where id = mynodeid ;    
             return myworktime ;  
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists gencastbakeend(nodeno varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastbakeend(nodeno varchar,empno varchar) returns varchar as $BODY$
          DECLARE
             mynowdate date ;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             mytime varchar ;
             myworktime varchar ;
             ncount int ;
             mywkid int ;
             myempid int ;
             mynodeid int ;
             mydate varchar ;
             myres varchar ;
             myrepid int ;
          BEGIN
             select id,mo_no into mynodeid,mywkid from maintenance_equipment where equipment_no = nodeno ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='B' and order_id=mywkid ;
              if ncount > 0 then
                select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='B' and order_id=mywkid ;
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                myres = myworktime ;
                execute recalreplinetime(myrepid) ; 
                update maintenance_equipment set iot_status='4' where id = mynodeid ; 
             else
                myres = ' ' ;   
             end if ;
             return myres;    
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute(
            """drop function if exists gencastloadstart(nodeno varchar,mono varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastloadstart(nodeno varchar,mono varchar,empno varchar) returns varchar as $BODY$
          DECLARE
             mynowdate date ;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             mytime varchar ;
             myworktime varchar ;
             ncount int ;
             mywkid int ;
             myempid int ;
             mynodeid int ;
             myrepid int ;
             mydate varchar ;
             myres varchar ;
          BEGIN
             select id into mywkid from alldo_acme_iot_workorder where name=mono ;
             select id,mo_no into mynodeid,mywkid from maintenance_equipment where equipment_no = nodeno ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and order_id=mywkid ;
             if ncount > 0 then
                select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and order_id=mywkid ;
                 execute recalreplinetime(myrepid) ; 
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
             end if ;
             insert into alldo_acme_iot_wkorder_replaceline(order_id,replace_owner,equipment_id,replace_start_datetime,create_date,replace_type)
                 values (mywkid,myempid,mynodeid,mynowdatetime,mynowdatetime,'L') ;
             update maintenance_equipment set mo_no=mywkid where id = mynodeid ;    
             return myworktime ;  
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute(
            """drop function if exists gencastloadend(nodeno varchar,mono varchar,empno varchar) cascade""")
        self.env.cr.execute("""create or replace function gencastloadeend(nodeno varchar,mono varchar,empno varchar) returns varchar as $BODY$
          DECLARE
             mynowdate date ;
             mynowdatetime timestamp ;
             mynowdatetime1 timestamp ;
             mytime varchar ;
             myworktime varchar ;
             ncount int ;
             mywkid int ;
             myempid int ;
             mynodeid int ;
             myrepid int ;
             mydate varchar ;
             myres varchar ;
          BEGIN
             select id into mywkid from alldo_acme_iot_workorder where name=mono ;
             select id,mo_no into mynodeid,mywkid from maintenance_equipment where equipment_no = nodeno ;
             select id into myempid from hr_employee where emp_code=empno ;
             select (now()::timestamp)::DATE  into mynowdate ;
             select current_timestamp into mynowdatetime ;
             select current_timestamp + interval '8 hours' into mynowdatetime1 ;
             select current_date::TEXT into mydate ;
             select substring((current_time + interval '8 hours')::TEXT,1,8) into mytime ;
             myworktime = concat(mydate,' ',mytime) ;
             select count(*) into ncount from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and order_id=mywkid ;
              if ncount > 0 then
                select max(id) into myrepid from alldo_acme_iot_wkorder_replaceline where replace_end_datetime is null and replace_type='L' and order_id=mywkid ;
                update alldo_acme_iot_wkorder_replaceline set replace_end_datetime=mynowdatetime where id = myrepid ;
                myres = myworktime ;
                execute recalreplinetime(myrepid) ; 
                update maintenance_equipment set iot_status='4' where id = mynodeid ; 
             else
                myres = ' ' ;   
             end if ;
             return myres;    
          END;$BODY$
          LANGUAGE plpgsql""")

        self.env.cr.execute("""drop function if exists postockinqcline(moid int,prodnum float,ngnum float) cascade""")
        self.env.cr.execute("""create or replace function postockinqcline(moid int,prodnum float,ngnum float) returns void as $BODY$
          DECLARE
            mymaxid int ;
            ncount int ;
          BEGIN
            select count(*) into ncount from alldo_acme_iot_workorder_qc where order_id = moid ;
            if ncount > 0 then
               select max(id) into mymaxid from alldo_acme_iot_workorder_qc where order_id = moid ;
               update alldo_acme_iot_workorder_qc set qc_good_num=prodnum,processing_ng_num=ngnum where id =mymaxid ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genprodrealnum() cascade""")
        self.env.cr.execute("""create or replace function genprodrealnum() returns void as $BODY$
         DECLARE
           currentdate1 date ;
           currentdate2 date;
           wk_cur refcursor ;
           wk_rec record ;
           real_cur refcursor ;
           real_rec record ;
           prodtmplid int ;
           engtype varchar ;
           wkid int ;
           prodid int ;
           myid int ;
           myhour int ;
           realprod int ;
           moldcavity int ;
           mystate char ;
           mymoldid int ;
         BEGIN
           delete from alldo_acme_iot_production_real ;
           select current_date::DATE into currentdate1 ;
           select (current_date - interval '3 month')::DATE into currentdate2 ;
           open wk_cur for select * from alldo_acme_iot_workorder_iot_data where iot_date::DATE between currentdate2::DATE and currentdate1::DATE ;
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             select product_no,eng_type into prodid,engtype from alldo_acme_iot_workorder where id = wk_rec.order_id ;
             select product_tmpl_id into prodtmplid from product_product where id = prodid ;
             select mold_id into mymoldid from product_template where id = prodtmplid ;
             select mold_cavity into moldcavity from alldo_acme_iot_acme_mold where id = mymoldid ;
             select id into myid from alldo_acme_iot_production_real where prod_id=prodtmplid and eng_type='1' ;
             if myid is not null then
                update alldo_acme_iot_production_real set prod_num = coalesce(prod_num,0) + coalesce(wk_rec.iot_num,0),
                   prod_time = coalesce(prod_time,0) + coalesce(wk_rec.iot_duration,0) where id = myid ;
             else
                insert into alldo_acme_iot_production_real(prod_id,eng_type,prod_num,prod_time) values (prodtmplid,'1',coalesce(wk_rec.iot_num,0),coalesce(wk_rec.iot_duration,0)) ;
             end if ;
            
           end loop ;
           close wk_cur ;    
           open real_cur for select * from alldo_acme_iot_production_real ;
           loop
             fetch real_cur into real_rec ;
             exit when not found ;
             myhour = round((real_rec.prod_time::numeric/60::numeric),2) ;
             if myhour = 0 then
                realprod = 0 ;
             else   
                realprod = round((real_rec.prod_num::numeric/myhour::numeric),0) ;
             end if ;   
             select id,coalesce(mold_cavity,1) into myid,moldcavity from alldo_acme_iot_eng_order where prod_id = real_rec.prod_id and eng_type = real_rec.eng_type ;
             /* realprod = round((realprod::numeric/moldcavity::numeric),0) ;*/
             update alldo_acme_iot_eng_order set prod_real_num = realprod where id = myid ;
           end loop ;
           close real_cur ;
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
           delete from alldo_acme_iot_equipment_performance_list ;
           open equ_cur for select id from maintenance_equipment where category_id=2 and active=True;
           loop
             fetch equ_cur into equ_rec ;
             exit when not found ;
             select sum(coalesce(iot_duration,0)) into iotdur from alldo_acme_iot_workorder_iot_data where iot_node = equ_rec.id and 
                iot_date::DATE between startdate::DATE and enddate::DATE ;
             select sum(coalesce(replace_duration,0)) into iotdurmin from alldo_acme_iot_wkorder_replaceline where equipment_id=equ_rec.id and 
                replace_start_datetime::DATE between startdate::DATE and enddate::DATE ;   
             iotdurh1 = round((iotdurmin::numeric/60),2) ;    
             iotdurh = round((iotdur::numeric/60),2) ;
             insert into alldo_acme_iot_equipment_performance_list(equip_no,equipment_duration) values (equ_rec.id,iotdurh) ;
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
             BEGIN
               delete from alldo_acme_iot_man_performance_list ;
               delete from alldo_acme_iot_man_performance_temp ;
               open temp_cur for select id,iot_owner1,qc_date from alldo_acme_iot_workorder_qc where qc_date::DATE between startdate::DATE and enddate::DATE ;
               loop
                 fetch temp_cur into temp_rec ;
                 exit when not found ;
                 select getperformance(temp_rec.id) into perf_rate ;
                 insert into alldo_acme_iot_man_performance_temp(prod_owner,prod_performance) values (temp_rec.iot_owner1,perf_rate) ;
               end loop ;
               close temp_cur ;
              open man_cur for select distinct iot_owner1 from alldo_acme_iot_workorder_qc where qc_date::DATE between startdate::DATE and enddate::DATE ;
               loop
                 fetch man_cur into man_rec ;
                 exit when not found ;
                 insert into  alldo_acme_iot_man_performance_list(prod_owner) values (man_rec.iot_owner1) ;    
               end loop ;
               close man_cur ;
               open man_cur for select * from alldo_acme_iot_man_performance_list ;
               loop
                  fetch man_cur into man_rec ;
                  exit when not found ;
                  select round(avg(T.prod_performance)::numeric * 100,2) into perf_rate from alldo_acme_iot_man_performance_temp T where T.prod_owner=man_rec.prod_owner ;
                  update alldo_acme_iot_man_performance_list set prod_performance=perf_rate where id = man_rec.id ;
               end loop ;
               close man_cur ;
               delete from alldo_acme_iot_man_performance_list where prod_performance = 0 or prod_owner is null or prod_performance is null ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """drop function if exists genprodgoodng(startdate date,enddate date,prodid int,nodeid int) cascade""")
        self.env.cr.execute("""create or replace function genprodgoodng(startdate date,enddate date,prodid int,nodeid int) returns void as $BODY$
        DECLARE
          totamount float ;
          goodnum float ;
          ngnum float ;
          ngratio float ;
          goodratio float ;
          qc_cur refcursor ;
          qc_rec record ;
          prod_cur refcursor ;
          prod_rec record ;
          prodno int ;
          mywkid int ;
        BEGIN
          delete from alldo_acme_iot_prod_goodng_list ; 
          if prodid = 0 then
             if nodeid = 0 then
                open prod_cur for select distinct product_no from alldo_acme_iot_workorder_qc where qc_date::DATE between
                    startdate::DATE and enddate::DATE ;
                loop
                   fetch prod_cur into prod_rec ;
                   exit when not found ;
                   select sum(coalesce(total_amount_num,0)),sum(coalesce(qc_good_num,0)),sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into goodnum,totamount,ngnum 
                       from alldo_acme_iot_workorder_qc where product_no=prod_rec.product_no and qc_date::DATE between startdate::DATE and enddate::DATE; 
                       
                    goodnum = totamount - ngnum ;
                   goodratio = round((goodnum::numeric / totamount::numeric) * 100 ,2) ;
                   ngratio =  round((ngnum::numeric / totamount::numeric) * 100 ,2) ; 
               
                   insert into alldo_acme_iot_prod_goodng_list(product_id,good_ratio,ng_ratio) values (prod_rec.product_no,goodratio,ngratio) ;
                end loop ;
                close prod_cur ;    
             else
                open prod_cur for select distinct product_no from alldo_acme_iot_workorder_qc where qc_date::DATE between
                    startdate::DATE and enddate::DATE and iot_node = nodeid ;
                loop
                   fetch prod_cur into prod_rec ;
                   exit when not found ;
                   select sum(coalesce(total_amount_num,0)),sum(coalesce(qc_good_num,0)),sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into totamount,goodnum,ngnum 
                       from alldo_acme_iot_workorder_qc where product_no=prod_rec.product_no and iot_node=nodeid and qc_date::DATE between
                       startdate::DATE and enddate::DATE; 
                   goodnum = totamount - ngnum ;    
                   goodratio = round((goodnum::numeric / totamount::numeric) * 100 ,2) ;
                   ngratio =  round((ngnum::numeric / totamount::numeric) * 100 ,2) ; 
                   insert into alldo_acme_iot_prod_goodng_list(product_id,good_ratio,ng_ratio) values (prod_rec.product_no,goodratio,ngratio) ;
                end loop ;
                close prod_cur ;   
             end if ; 
          else
              if nodeid = 0 then
                 select sum(coalesce(total_amount_num,0)),sum(coalesce(qc_good_num,0)),sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into totamount,goodnum,ngnum 
                    from alldo_acme_iot_workorder_qc where product_no=prodid and qc_date::DATE between startdate::DATE and enddate::DATE; 
              else
                 select sum(coalesce(total_amount_num,0)),sum(coalesce(qc_good_num,0)),sum(coalesce(material_ng_num,0)+coalesce(processing_ng_num,0)) into totamount,goodnum,ngnum 
                    from alldo_acme_iot_workorder_qc where product_no=prodid and iot_node=nodeid and qc_date::DATE between startdate::DATE and enddate::DATE;      
              end if ;
              goodnum = totamount - ngnum ;
              goodratio = round((goodnum::numeric / totamount::numeric) * 100 ,2) ;
              ngratio =  round((ngnum::numeric / totamount::numeric) * 100 ,2) ;
              insert into alldo_acme_iot_prod_goodng_list(product_id,good_ratio,ng_ratio) values (prodid,goodratio,ngratio) ; 
          end if ;
          delete from alldo_acme_iot_prod_goodng_list where product_id is null ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genqcprod() cascade""")
        self.env.cr.execute("""create or replace function genqcprod() returns void as $BODY$
         DECLARE
           wk_cur refcursor ;
           wk_rec record ;
         BEGIN
           open wk_cur for select id,product_no from alldo_acme_iot_workorder ;
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             update alldo_acme_iot_workorder_qc set product_no=wk_rec.product_no where order_id=wk_rec.id ;
           end loop ;
           close wk_cur ;
           update alldo_acme_iot_workorder_qc set iot_owner1=iot_owner ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genprodout(subid int) cascade""")
        self.env.cr.execute("""create or replace function genprodout(subid int) returns void as $BODY$
         DECLARE
           outl_cur refcursor ;
           outl_rec record ;
           ncount int ;
           mymaxid int ;
           mymaxid1 int ;
           mysubid int ;
           mycurrenttime timestamp ;
           myowner int ;
           mypartnerid int ;
           mycurrentdate date ;
         BEGIN
           select current_timestamp into mycurrenttime ;
           select (current_timestamp + interval '8 hours')::DATE into mycurrentdate ;
           select prodout_owner,partner_id into myowner,mypartnerid from alldo_acme_iot_prodout where id = subid ;
           open outl_cur for select * from alldo_acme_iot_prodout_line where prodout_id = subid ;
           loop 
             fetch outl_cur into outl_rec;
             exit when not found ;
             select count(*) into ncount from alldo_acme_iot_outsuborder where id = outl_rec.prodout_no and product_no = outl_rec.product_no ;
             if ncount > 0 then
                insert into alldo_acme_iot_outsuborder_prodout(order_id,prodout_datetime,product_no,out_good_num,out_loc,out_owner,date_supply,date_due) values
                       (outl_rec.prodout_no,mycurrenttime,outl_rec.product_no,outl_rec.out_good_num,'ACME委外供料',myowner,mycurrentdate,outl_rec.date_due) ;
                execute updatesuborderframe(outl_rec.prodout_no,outl_rec.out_plastic_frame1,outl_rec.out_plastic_frame2,outl_rec.out_pallet) ; 
                update alldo_acme_iot_outsuborder set blank_num = coalesce(blank_num,0) + outl_rec.out_good_num where id = outl_rec.prodout_no and product_no = outl_rec.product_no ;    
             end if ;
             select max(id) into mymaxid from alldo_acme_iot_outsuborder_prodout where order_id=outl_rec.prodout_no ;
             insert into alldo_acme_iot_partner_prodout(partner_id,prodout_datetime,product_no,out_good_num,out_loc,out_owner) values
               (mypartnerid,mycurrenttime,outl_rec.product_no,outl_rec.out_good_num,'ACME委外供料',myowner) ;
             select max(id) into mymaxid1 from alldo_acme_iot_partner_prodout where partner_id = mypartnerid ;  
             update alldo_acme_iot_prodout_line set outsuborderlineid=mymaxid,outpartnerlineid=mymaxid1 where id = outl_rec.id ; 
           end loop ;
           close outl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists syncoldprodout(subid int) cascade""")
        self.env.cr.execute("""create or replace function syncoldprodout(subid int) returns void as $BODY$
         DECLARE
           ncount int ;
           myprodoutno int ;
           mygoodnum float ;   
           outl_cur refcursor ;
           outl_rec record ;
         BEGIN
           open outl_cur for select * from alldo_acme_iot_prodout_line where prodout_id = subid ;
           loop
              fetch outl_cur into outl_rec ;
              exit when not found ;
              select order_id into subid from alldo_acme_iot_outsuborder_prodout where id = outl_rec.outsuborderlineid ;
              select sum(coalesce(out_good_num,0)) into mygoodnum from alldo_acme_iot_outsuborder_prodout where order_id=subid ;
              /* mygoodnum = coalesce(outl_rec.out_good_num,0) - coalesce(outl_rec.old_good_num,0) ; */
              update alldo_acme_iot_outsuborder set blank_num = mygoodnum where id = outl_rec.prodout_no ;
              update alldo_acme_iot_prodout_line set old_good_num=coalesce(out_good_num,0),old_plastic_frame1=coalesce(out_plastic_frame1,0),
                  old_plastic_frame2=coalesce(out_plastic_frame2,0),old_pallet=coalesce(out_pallet,0),date_due=outl_rec.date_due where id = outl_rec.id ;
           end loop ;
           close outl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists delprodoutline(outlid int) cascade""")
        self.env.cr.execute("""create or replace function delprodoutline(outlid int) returns void as $BODY$
         DECLARE
           oldgoodnum float;
           oldpframe1 float ;
           oldpframe2 float ;
           oldpallet float ;
           sublineid int ;
           partnerlineid int ;
           subid int ;
         BEGIN
           select outsuborderlineid,outpartnerlineid,old_good_num,old_plastic_frame1,old_plastic_frame2,old_pallet 
              into sublineid,partnerlineid,oldgoodnum,oldpframe1,oldpframe2,oldpallet from alldo_acme_iot_prodout_line where id = outlid ;
              select order_id into subid from alldo_acme_iot_outsuborder_prodout where id = sublineid ;
           update alldo_acme_iot_outsuborder set blank_num=coalesce(blank_num,0) - oldgoodnum,out_plastic_frame1=coalesce(out_plastic_frame1,0) - oldpframe1,
             out_plastic_frame2=coalesce(out_plastic_frame2,0) - oldpframe2,out_pallet=coalesce(out_pallet,0) - oldpallet where id = subid ;
           delete from alldo_acme_iot_outsuborder_prodout where id = sublineid ;
           delete from alldo_acme_iot_partner_prodout where id = partnerlineid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists updateprodoutline(outlid int) cascade""")
        self.env.cr.execute("""create or replace function updateprodoutline(outlid int) returns void as $BODY$
         DECLARE
           oldgoodnum float;
           oldpframe1 float ;
           oldpframe2 float ;
           oldpallet float ;
           outgoodnum float;
           outpframe1 float ;
           outpframe2 float ;
           outpallet float ;
           sublineid int ;
           partnerlineid int ;
           subid int ;
         BEGIN
           select outsuborderlineid,outpartnerlineid,old_good_num,old_plastic_frame1,old_plastic_frame2,old_pallet,out_good_num,out_plastic_frame1,out_plastic_frame2,out_pallet 
              into sublineid,partnerlineid,oldgoodnum,oldpframe1,oldpframe2,oldpallet, outgoodnum,outpframe1,outpframe2,outpallet from alldo_acme_iot_prodout_line where id = outlid ;
              select order_id into subid from alldo_acme_iot_outsuborder_prodout where id = sublineid ;
           oldgoodnum = coalesce(oldgoodnum,0) - coalesce(outgoodnum,0) ;
           oldpframe1 = coalesce(oldpframe1,0) - coalesce(outpframe1,0) ;
           oldpframe2 = coalesce(oldpframe2,0) - coalesce(outpframe2,0) ;
           oldpallet = coalesce(oldpallet,0) - coalesce(outpallet,0) ;   
           update alldo_acme_iot_outsuborder set blank_num=coalesce(blank_num,0) - oldgoodnum,out_plastic_frame1=coalesce(out_plastic_frame1,0) - oldpframe1,
             out_plastic_frame2=coalesce(out_plastic_frame2,0) - oldpframe2,out_pallet=coalesce(out_pallet,0) - oldpallet where id = subid ;
           update alldo_acme_iot_outsuborder_prodout set out_good_num=coalesce(outgoodnum,0) where id = sublineid ;
           update alldo_acme_iot_partner_prodout set out_good_num=coalesce(oldgoodnum,0) where id = partnerlineid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkamountnum(wkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkamountnum(wkid int) returns void as $BODY$
         DECLARE
           ncount int ;
           blanknum float ;
           prodgoodnum float ;
           mynowdate date ;
         BEGIN
           select current_timestamp::DATE into mynowdate ;
           select sum(coalesce(in_good_num,0)) into blanknum from alldo_acme_iot_wkorder_prodin where order_id = wkid ;         
           /*select sum(coalesce(qc_good_num,0) - coalesce(material_ng_num,0) - coalesce(processing_ng_num,0))
                  into prodgoodnum from alldo_acme_iot_workorder_qc where order_id = wkid ; */
           select sum(coalesce(qc_good_num,0)) into prodgoodnum  from alldo_acme_iot_workorder_qc where order_id = wkid ;     
           if blanknum is null then
              blanknum = 0 ;
           end if ;    
           if prodgoodnum is null then
              prodgoodnum = 0 ;
           end if ;   
           /* update alldo_acme_iot_workorder set mo_production_num=prodgoodnum where id = wkid ; */      
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkngratio(wkid int) cascade""")
        self.env.cr.execute("""create or replace function genwkngratio(wkid int) returns void as $BODY$
         DECLARE
           ncount int ;
           wkngnum float ;
           wkgoodnum float ;
           cutngnum float ;
           cutgoodnum float ;
           ngratio float ;
         BEGIN
           select sum(coalesce(processing_ng_num,0)),sum(coalesce(qc_good_num,0) - coalesce(processing_ng_num,0)) into
              wkngnum,wkgoodnum from alldo_acme_iot_workorder_qc where order_id = wkid ;
           select sum(coalesce(out_ng_num,0)),sum(coalesce(out_good_num,0)) into cutngnum,cutgoodnum from alldo_acme_iot_wkorder_prodout
              where order_id = wkid ;
           if wkngnum is null then
              wkngnum = 0 ;
           end if ;
           if wkgoodnum is null then
              wkgoodnum = 0 ;
           end if ;    
           if cutngnum is null then
              cutngnum = 0 ;
           end if ;  
           if cutgoodnum is null then
              cutgoodnum = 0 ;
           end if ;
           if wkngnum + wkgoodnum = 0 then
              ngratio = 0.0 ;
           else
              ngratio = round(((wkngnum + cutngnum)::numeric / (wkngnum + wkgoodnum)::numeric) * 100::numeric,1) ;
           end if ;
           select count(*) into ncount from alldo_acme_iot_wkorder_ngratio where order_id = wkid ;
           if ncount = 0 then
              insert into alldo_acme_iot_wkorder_ngratio(order_id,wk_good_num,wk_ng_num,cut_ng_num,ng_ratio)
                values (wkid,wkgoodnum,wkngnum,cutngnum,ngratio) ;
           else
              update alldo_acme_iot_wkorder_ngratio set wk_good_num=wkgoodnum,wk_ng_num=wkngnum,cut_ng_num=cutngnum,ng_ratio=ngratio
                 where order_id=wkid ;
           end if ;      
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gensubngratio(subid int) cascade""")
        self.env.cr.execute("""create or replace function gensubngratio(subid int) returns void as $BODY$
         DECLARE
           ncount int ;
           subgoodnum float ;
           subngnum float ;
           subngratio float ;
         BEGIN
           select sum(coalesce(in_good_num,0)),sum(coalesce(in_ng_num,0)) into subgoodnum,subngnum from alldo_acme_iot_outsuborder_prodin
             where order_id=subid ;
           if subgoodnum + subngnum = 0 then
              subngratio = 0.0 ;
           else
              subngratio = round((subngnum::numeric/(subgoodnum::numeric + subngnum::numeric))* 100::numeric,1) ;
           end if ;  
           select count(*) into ncount from alldo_acme_iot_outsuborder_ngratio where order_id = subid ;
           if ncount = 0 then
              insert into alldo_acme_iot_outsuborder_ngratio(order_id,sub_good_num,sub_ng_num,sub_ratio) values (subid,subgoodnum,subngnum,subngratio) ;
           else
              update alldo_acme_iot_outsuborder_ngratio set sub_good_num=subgoodnum,sub_ng_num=subngnum,sub_ratio=subngratio where order_id=subid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getislowsafe() cascade""")
        self.env.cr.execute("""create or replace function getislowsafe() returns void as $BODY$
         DECLARE
           sf_cur refcursor ;
           sf_rec record ;
           prodid int ;
           monhand float ;
           islowsafe Boolean ;
         BEGIN
           open sf_cur for select id,safe_num from product_template where safe_num > 0 ;
           loop
             fetch sf_cur into sf_rec ;
             exit when not found ;
             select id into prodid from product_product where product_tmpl_id = sf_rec.id ;
             select getmaterialonhand(prodid) into monhand ;
             if monhand < sf_rec.safe_num then
                islowsafe = True ;
             else
                islowsafe = False ;
             end if ;
             update product_template set material_onhand=monhand,is_lowsafe=islowsafe where id = sf_rec.id ;
           end loop ;
           close sf_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genwkordergoodnum() cascade""")
        self.env.cr.execute("""create or replace function genwkordergoodnum() returns void as $BODY$
         DECLARE
           wk_cur refcursor ;
           wk_rec record ;
           goodnum float ;
         BEGIN
           open wk_cur for select id,mo_production_num from alldo_acme_iot_workorder where coalesce(mo_production_num,0) = 0 ;
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             select sum(coalesce(qc_good_num,0) - coalesce(processing_ng_num,0)) into goodnum from alldo_acme_iot_workorder_qc where order_id = wk_rec.id ;
            /* update alldo_acme_iot_workorder set mo_production_num=goodnum where id = wk_rec.id ; */
           end loop ;
           close wk_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gendayscale(scaleid int) cascade""")
        self.env.cr.execute("""create or replace function gendayscale(scaleid int) returns void as $BODY$
         DECLARE
           prodgpid int ;
           prodid int ;
           scaletype char;
           scaleweight float ;
           scaletot float ;
           scaleratio float ;
           uomid int ;
           scaledate date ;
           ncount int ;
           ncount1 int ;
           maxid int ;
           itemseq int ;
           sratio float ;
           scale_cur refcursor ;
           scale_rec record ;
           equipid int ;
         BEGIN
           /* select count(*) into ncount from alldo_acme_iot_electronic_scale where id = scaleid and scale_type='1' and is_posting='2' ; */
           select count(*) into ncount from alldo_acme_iot_electronic_scale where id = scaleid and scale_type='1' ;
           if ncount > 0 then
              select product_no,scale_weight,uom_id,scale_datetime::DATE,equipment_no into prodid,scaleweight,uomid,scaledate,equipid from 
                     alldo_acme_iot_electronic_scale where id = scaleid ;
              select product_gpid,item_seq into prodgpid,itemseq from alldo_acme_iot_scalegroup_setting where product_no=prodid ;
              select count(*) into ncount1 from alldo_acme_iot_day_scale where product_no=prodid and scale_date=scaledate  ;
              if ncount1 = 0 then
                 insert into alldo_acme_iot_day_scale(product_no,scale_weight,product_gpid,item_seq,uom_id,scale_date,scale_complete,equipment_no) values
                   (prodid,scaleweight,prodgpid,itemseq,uomid,scaledate,False,equipid) ;
              else
                 update alldo_acme_iot_day_scale set scale_weight=coalesce(scale_weight,0)+scaleweight
                        where product_no=prodid and scale_date=scaledate ;     
              end if ;      
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 此 function genscalenoncomplete 有問題要修正
        self.env.cr.execute("""drop function if exists genscalenoncomplete() cascade""")
        self.env.cr.execute("""create or replace function genscalenoncomplete() returns void as $BODY$
         DECLARE
           scale_cur refcursor ;
           scale_rec record ;
           mynowdate date ;
           mynum float ;
           totnum float ;
           sratio float ;
         BEGIN
           select current_date into mynowdate ;
           open scale_cur for select * from alldo_acme_iot_day_scale where scale_date=mynowdate or scale_complete=False or scale_complete is null ;
           loop
             fetch scale_cur into scale_rec ;
             exit when not found ;
             select sum(coalesce(scale_weight,0)) into mynum from alldo_acme_iot_day_scale where scale_date=scale_rec.scale_date and product_no = scale_rec.product_no and equipment_no=scale_rec.equipment_no ;
             select sum(coalesce(scale_weight,0)) into totnum from alldo_acme_iot_day_scale where scale_date=scale_rec.scale_date and product_gpid = scale_rec.product_gpid and equipment_no=scale_rec.equipment_no ;
             if totnum is null or totnum = 0 then
                sratio = 0 ;
             else    
                sratio = round((mynum::numeric/totnum::numeric)*100,2) ;
             end if ;   
             update alldo_acme_iot_day_scale set scale_total=totnum,scale_ratio=sratio,scale_complete=True where id = scale_rec.id ;
           end loop ;
           close scale_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 修正版 genscalenoncomplete1
        self.env.cr.execute("""drop function if exists genscalenoncomplete1() cascade""")
        self.env.cr.execute("""create or replace function genscalenoncomplete1() returns void as $BODY$
         DECLARE
           s1_cur refcursor ;
           s1_rec record ;
           m_cur refcursor ;
           m_rec record ;
           s2_cur refcursor ;
           s2_rec record ;
           scale_cur refcursor ;
           scale_rec record ;
           mynowdate date ;
           mynum float ;
           totnum float ;
           sratio float ;
           ncount int ;
         BEGIN
           open s1_cur for select distinct scale_date from alldo_acme_iot_day_scale where scale_complete=False ;
           loop
             fetch s1_cur into s1_rec ;
             exit when not found ;
             open s2_cur for select distinct product_gpid from alldo_acme_iot_day_scale where  scale_date=s1_rec.scale_date ;
               loop
                 fetch s2_cur into s2_rec ;
                 exit when not found ;
                 select sum(coalesce(scale_weight,0)) into totnum from alldo_acme_iot_day_scale where scale_date=s1_rec.scale_date and  product_gpid=s2_rec.product_gpid ;
                 update alldo_acme_iot_day_scale set scale_total=totnum where scale_date=s1_rec.scale_date and  product_gpid=s2_rec.product_gpid ;
             end loop ;
             close s2_cur ; 
           end loop ;
           close s1_cur ;
           open s1_cur for select * from alldo_acme_iot_day_scale where scale_complete=False or scale_complete is null ;
           loop
               fetch s1_cur into s1_rec ;
               exit when not found ;
               if s1_rec.scale_total=0 or s1_rec.scale_total is null then
                  sratio = 0 ;
               else
                  sratio = round((s1_rec.scale_weight::numeric/s1_rec.scale_total::numeric)*100,2) ;
               end if ;             
               update alldo_acme_iot_day_scale set scale_ratio=sratio,scale_complete=True where id = s1_rec.id ;
           end loop ;
           close s1_cur ;  
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genalldayscale() cascade""")
        self.env.cr.execute("""create or replace function genalldayscale() returns void as $BODY$
         DECLARE
          scale_cur refcursor ;
          scale_rec record ;
          scaletot float ;
          sratio float ;
         BEGIN
           delete from  alldo_acme_iot_day_scale ;
           open scale_cur for select id from alldo_acme_iot_electronic_scale where scale_type='1' ;
           loop
             fetch scale_cur into scale_rec ;
             exit when not found ;
             execute gendayscale(scale_rec.id) ;
           end loop ;
           close scale_cur ; 
           execute genscalenoncomplete1() ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getlotdata() cascade""")
        self.env.cr.execute("""create or replace function getlotdata() returns setof INT as $BODY$
         DECLARE
           quant_cur refcursor ;
           quant_rec record ;
           mlocid int ;
         BEGIN
           select max(material_loc) into mlocid from alldo_acme_iot_company_stockloc ;
           open quant_cur for select id from stock_quant where lot_id is not null and quantity != 0 and location_id=mlocid ;
           loop
             fetch quant_cur into quant_rec ;
             exit when not found ;
             return next quant_rec.id ;
           end loop ;
           close quant_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists getquantlotnum(quantid int) cascade""")
        self.env.cr.execute("""create or replace function getquantlotnum(quantid int) returns float as $BODY$
         DECLARE
           myres float ;
         BEGIN
           select coalesce(quantity,0) into myres from stock_quant where id = quantid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists genallwkordergoodng() cascade""")
        self.env.cr.execute("""create or replace function genallwkordergoodng() returns void as $BODY$
         DECLARE
           wk_cur refcursor ;
           wk_rec record ;
           qc_cur refcursor ;
           qc_rec record ;
           ncount int ;
         BEGIN
           open wk_cur for select id from alldo_acme_iot_workorder ;
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             open qc_cur for select * from alldo_acme_iot_workorder_qc where order_id = wk_rec.id ;
             loop
               fetch qc_cur into qc_rec ;
               exit when not found ;
               select count(*) into ncount from alldo_acme_iot_wkorder_prodout where order_id = wk_rec.id
                  and prodout_datetime::DATE = qc_rec.qc_date::DATE ;
               if ncount > 0 then
                  update alldo_acme_iot_wkorder_prodout set 
                    out_good_num=(coalesce(qc_rec.qc_good_num,0) - coalesce(qc_rec.processing_ng_num,0))
                    where order_id = wk_rec.id and prodout_datetime::DATE = qc_rec.qc_date::DATE ;
               else
                  insert into alldo_acme_iot_wkorder_prodout(order_id,prodout_datetime,product_no,is_cutting,out_type,out_good_num,out_ng_num,out_owner) values
                   (qc_rec.order_id,qc_rec.qc_date,qc_rec.product_no,True,'2',(coalesce(qc_rec.qc_good_num,0) - coalesce(qc_rec.processing_ng_num,0)),0,qc_rec.iot_owner) ;
               end if ;   
             end loop ;
             close qc_cur ;
             execute genpowkorderngnum(wk_rec.id) ;
           end loop ;
           close wk_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists delmailmessage() cascade""")
        self.env.cr.execute("""create or replace function delmailmessage() returns void as $BODY$
         DECLARE
         BEGIN
           delete from mail_message ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists gendaylastman(startdate date,enddate date) cascade""")
        self.env.cr.execute("""drop function if exists gendaylastman() cascade""")
        self.env.cr.execute("""create or replace function gendaylastman() returns void as $BODY$
         DECLARE
           emp_cur refcursor ;
           emp_rec record ;
           last_cur refcursor ;
           last_rec record ;
           lastdatetime timestamp ;
           lastdatetime1 varchar ;
           lastdate1 varchar ;
           lastdate2 date ;
           empname varchar ;
           nitem int ;
           ncount int ;
         BEGIN
           nitem = 1 ; 
           delete from alldo_acme_iot_daylast_manlist ;
           delete from alldo_acme_iot_daylast_sum_list ;
           open emp_cur for select distinct iot_owner from alldo_acme_iot_daylast_list order by iot_owner;
           loop
             fetch emp_cur into emp_rec ;
             exit when not found ;
             select name into empname from hr_employee where id=emp_rec.iot_owner ; 
             insert into alldo_acme_iot_daylast_manlist(item_id,emp_id,emp_name) values (nitem,emp_rec.iot_owner,empname) ;
             open last_cur for select distinct last_date2 from alldo_acme_iot_daylast_list where iot_owner=emp_rec.iot_owner order by last_date2 ;
             loop
               fetch last_cur into last_rec ;
               exit when not found ;
               select max(iot_datetime) into lastdatetime from alldo_acme_iot_daylast_list where last_date2=last_rec.last_date2 
                  and iot_owner=emp_rec.iot_owner ;
               select substring((lastdatetime + interval '8 hours')::TEXT,12,5) into lastdatetime1 ;   
               select (lastdatetime + interval '8 hours')::DATE::TEXT into lastdate1 ;
               select (lastdatetime + interval '8 hours')::DATE into lastdate2 ;   
               select count(*) into ncount from alldo_acme_iot_daylast_sum_list where last_date2=last_rec.last_date2 ;
               if ncount = 0 then
                  if nitem = 1 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime1,cdatetime1) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 2 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime2,cdatetime2) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 3 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime3,cdatetime3) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 4 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime4,cdatetime4) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 5 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime5,cdatetime5) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 6 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime6,cdatetime6) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 7 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime7,cdatetime7) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 8 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime8,cdatetime8) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  elsif nitem = 9 then
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime9,cdatetime9) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  else
                     insert into alldo_acme_iot_daylast_sum_list(last_date1,last_date2,iot_datetime10,cdatetime10) values (lastdate1,lastdate2,lastdatetime,lastdatetime1) ;
                  end if ;   
               else
                  if nitem = 1 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime1=lastdatetime,cdatetime1=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 2 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime2=lastdatetime,cdatetime2=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 3 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime3=lastdatetime,cdatetime3=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 4 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime4=lastdatetime,cdatetime4=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 5 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime5=lastdatetime,cdatetime5=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 6 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime6=lastdatetime,cdatetime6=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 7 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime7=lastdatetime,cdatetime7=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 8 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime8=lastdatetime,cdatetime8=lastdatetime1 where last_date2=lastdate2 ;
                  elsif nitem = 9 then
                     update alldo_acme_iot_daylast_sum_list set iot_datetime9=lastdatetime,cdatetime9=lastdatetime1 where last_date2=lastdate2 ;
                  else
                     update alldo_acme_iot_daylast_sum_list set iot_datetime10=lastdatetime,cdatetime10=lastdatetime1 where last_date2=lastdate2 ;
                  end if ;
               end if ;             
             end loop ;
             close last_cur ;
             nitem = nitem + 1 ; 
           end loop ; 
           close emp_cur ;  
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self.env.cr.execute("""drop function if exists gendaylasttime(startdate date,enddate date)""")
        self.env.cr.execute("""create or replace function gendaylasttime(startdate date,enddate date) returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           iot_cur refcursor ;
           iot_rec record ;
           lastdate1 varchar ;
           lastdate2 date ;
           lastdatetime timestamp ;
           myid int ;
         BEGIN
           delete from alldo_acme_iot_daylast_list ;
           open iot_cur for select id,iot_owner,iot_owner1,iot_datetime,iot_id from alldo_acme_iot_equipment_iot_data where
                (iot_datetime + interval '8 hours')::DATE >= startdate and (iot_datetime + interval '8 hours')::DATE <= enddate ;
           loop
             fetch iot_cur into iot_rec ;
             exit when not found ;
             /* iot_owner */
             select count(*) into ncount from alldo_acme_iot_daylast_list where iot_id=iot_rec.iot_id and last_date2=(iot_rec.iot_datetime + interval '8 hours')::DATE
                and iot_owner=iot_rec.iot_owner ;
             if ncount > 0 then
                myid = 0 ;
                select id,iot_datetime into myid,lastdatetime from alldo_acme_iot_daylast_list where iot_id=iot_rec.iot_id and last_date2=(iot_rec.iot_datetime + interval '8 hours')::DATE
                and iot_owner=iot_rec.iot_owner ;
                if myid > 0 and iot_rec.iot_datetime > lastdatetime then
                   update alldo_acme_iot_daylast_list set iot_datetime=iot_rec.iot_datetime where id = myid ;
                end if ;    
             else
                select (iot_rec.iot_datetime + interval '8 hours')::TEXT into lastdate1 ;
                select (iot_rec.iot_datetime + interval '8 hours')::DATE into lastdate2 ;
                if iot_rec.iot_owner is not null then
                   insert into alldo_acme_iot_daylast_list(iot_id,last_date1,last_date2,iot_datetime,iot_owner) values
                      (iot_rec.iot_id,lastdate1,lastdate2,iot_rec.iot_datetime,iot_rec.iot_owner) ;   
                end if ;      
             end if ;  
             /*  iot_owner1 */
             select count(*) into ncount from alldo_acme_iot_daylast_list where iot_id=iot_rec.iot_id and last_date2=(iot_rec.iot_datetime + interval '8 hours')::DATE
                and iot_owner=iot_rec.iot_owner1 ;
             if ncount > 0 then
                myid = 0 ;
                select id,iot_datetime into myid,lastdatetime from alldo_acme_iot_daylast_list where iot_id=iot_rec.iot_id and last_date2=(iot_rec.iot_datetime + interval '8 hours')::DATE
                       and iot_owner=iot_rec.iot_owner1 ;
                if myid > 0 and iot_rec.iot_datetime > lastdatetime then
                   update alldo_acme_iot_daylast_list set iot_datetime=iot_rec.iot_datetime where id = myid ;
                end if ;    
             else
                select (iot_rec.iot_datetime + interval '8 hours')::TEXT into lastdate1 ;
                select (iot_rec.iot_datetime + interval '8 hours')::DATE into lastdate2 ;
                if iot_rec.iot_owner1 is not null then
                   insert into alldo_acme_iot_daylast_list(iot_id,last_date1,last_date2,iot_datetime,iot_owner) values
                       (iot_rec.iot_id,lastdate1,lastdate2,iot_rec.iot_datetime,iot_rec.iot_owner1) ; 
                end if ;         
             end if ;  
           end loop ;
           close iot_cur ;  
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

        self.env.cr.execute("""drop view if exists acmeiot_stockmovelist""")
        self.env.cr.execute("""CREATE OR REPLACE VIEW acmeiot_stockmovelist AS
                    select A.id,A.date,A.product_id,A.product_qty,A.product_uom,A.state,A.picking_id,B.partner_id,A.picking_type_id,
                        B.report_no,B.origin from stock_move A left join stock_picking B on A.picking_id = B.id
                         where A.picking_type_id=2 and A.state='done' and substring(B.report_no,1,1)='S' """)

        self.env.cr.execute(
            """drop function if exists genstockmovemixsearch(startdate date,enddate date,partnerid int,prodid int) cascade""")
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
         BEGIN
           delete from alldo_acme_iot_stock_move_list ;
           mypartnerid = 0 ;
           myprodid = 0 ;
           ncount = 0 ;
           totqty = 0 ;
           nitem = 0 ;
           if partnerid = 0 then
              open mv_cur for select * from acmeiot_stockmovelist where (date::DATE between startdate::DATE and enddate::DATE)  and product_id=prodid 
                 order by partner_id,product_id ;
           elsif prodid = 0 then
              open mv_cur for select * from acmeiot_stockmovelist where (date::DATE between startdate::DATE and enddate::DATE) and  partner_id=partnerid 
                  order by product_id ;
           else
              open mv_cur for select * from acmeiot_stockmovelist where  (date::DATE between startdate::DATE and enddate::DATE) and  partner_id=partnerid 
                 and product_id=prodid  order by product_id;
           end if ;
           loop
             fetch mv_cur into mv_rec ;
             exit when not found ;
            
            insert into alldo_acme_iot_stock_move_list(date,product_id,product_qty,product_uom,partner_id,so_no,report_no) values
              (mv_rec.date,mv_rec.product_id,mv_rec.product_qty,mv_rec.product_uom,mv_rec.partner_id,mv_rec.origin,coalesce(mv_rec.report_no,' ')) ;
           
           end loop ;
           close mv_cur ;
          
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensaleshipping(saleid int) cascade""")
        self._cr.execute("""create or replace function gensaleshipping(saleid int) returns void as $BODY$
         DECLARE
           mypartnerid int ;
           myname varchar ;
           mynote varchar ;
           mynowdate date ;
           myprodid int ;
           myqty float ;
           myuom int ;
           myprice float ;
           mymemo varchar ; 
           line_cur refcursor ;
           line_rec record ;
           ncount int ;
           mymaxid int ;
           myitem int ;
           mysumtot float ;
           commitdate date ;
           paymentid int ;
           paymentterm varchar ;
           myproduom varchar ;
           saleno varchar ;
           taiinv varchar ;
         BEGIN
           delete from alldo_acme_iot_stockpicking_report1 ;
           select count(*) into ncount from sale_order where id=saleid ;
           myitem = 1 ;
           if ncount > 0 then
               select name,partner_id,name,coalesce(so_pi,' '),commitment_date::DATE,payment_term_id into saleno,mypartnerid,myname,mynote,commitdate,paymentid from sale_order where id = saleid ;
               select gettaiinv(saleno) into taiinv ;
               if paymentid is not null then
                  select name into paymentterm from account_payment_term where id = paymentid ;
               end if ;
               if mynote != ' ' then
                  mynote = concat('PI:',mynote) ;
               end if ;   
               insert into alldo_acme_iot_stockpicking_report1(partner_id,name,report_memo,report_date,taiwan_receipt) values (mypartnerid,myname,mynote,commitdate,taiinv) ;
               select max(id) into mymaxid from alldo_acme_iot_stockpicking_report1 ;
               open line_cur for select * from sale_order_line where order_id=saleid and product_uom_qty > 0 ;
               loop
                 fetch line_cur into line_rec ;
                 exit when not found ;
                 select name into myproduom from uom_uom where id = line_rec.product_uom ;
                /* insert into alldo_acme_iot_stockpicking_report_line1(rep_id,item,prod_no,prod_num,prod_uom,prod_price,price_tax,sum_price,line_memo) values
                  (mymaxid,myitem,line_rec.product_id,line_rec.product_uom_qty,myproduom,line_rec.price_unit,line_rec.price_tax,line_rec.price_subtotal,line_rec.name) ; */
                  insert into alldo_acme_iot_stockpicking_report_line1(rep_id,item,prod_no,prod_num,prod_uom,prod_price,price_tax,sum_price,line_memo) values
                  (mymaxid,myitem,line_rec.product_id,line_rec.qty_delivered,myproduom,line_rec.price_unit,line_rec.price_tax,(line_rec.product_uom_qty * line_rec.price_unit),line_rec.name) ;
                 myitem = myitem + 1 ; 
               end loop ;
               close line_cur ;
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gettaiinv(saleno varchar) cascade""")
        self._cr.execute("""create or replace function gettaiinv(saleno varchar) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            ncount int ;
            maxid int ;
          BEGIN
            select count(*) into ncount from account_move where invoice_origin=saleno and taiwan_receipt is not null ;
            if ncount > 0 then
               select max(id) into maxid from account_move where invoice_origin=saleno and taiwan_receipt is not null  ;
               select taiwan_receipt into myres from account_move where id = maxid ;
            else
               myres = ' ' ;   
            end if ;   
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensaleproddesc(soid int) cascade""")
        self._cr.execute("""create or replace function gensaleproddesc(soid int) returns void as $BODY$
          DECLARE
            proddesc varchar ;
            ncount int ;
            so_cur refcursor ;
            so_rec record ;
            defcode varchar ;
          BEGIN
            ncount = 0 ; 
            proddesc = '' ;
            open so_cur for select * from sale_order_line where order_id=soid ;
            loop
              fetch so_cur into so_rec ;
              exit when not found ;
              select default_code into defcode from product_product where id = so_rec.product_id ;
              if proddesc = '' then
                 proddesc = defcode ;
              else
                 if ncount <= 2 then
                    proddesc = concat(proddesc,' / ',defcode) ;
                 end if ;
              end if ;
              ncount = ncount + 1 ;
            end loop ;
            close so_cur ;
            update sale_order set prod_desc=proddesc where id = soid ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallsoproddesc() cascade""")
        self._cr.execute("""create or replace function genallsoproddesc() returns void as $BODY$
         DECLARE
          sale_cur refcursor ;
          sale_rec record ;
         BEGIN
           open sale_cur for select * from sale_order ;
           loop
             fetch sale_cur into sale_rec ;
             exit when not found ;
             execute gensaleproddesc(sale_rec.id) ;
           end loop ;
           close sale_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getispackagemat(prodid int) cascade""")
        self._cr.execute("""create or replace function getispackagemat(prodid int) returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           prodtmplid int ;
           ncount int ;
         BEGIN
           select coalesce(product_tmpl_id,0) into prodtmplid from product_product where id = prodid ;
           if prodtmplid > 0 then
              select count(*) into ncount from product_template where id=prodtmplid and categ_id=4 ;
              if ncount > 0 then
                 myres = True ;
              else
                 myres = False ;
              end if ;
           else
              myres = False ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genparoutloc(partnerid int) cascade""")
        self._cr.execute("""create or replace function genparoutloc(partnerid int) returns void as $BODY$
          DECLARE
            myname varchar ;
            myname1 varchar ;
            ncount int ;
            myparoutloc int ;
            myparentpath varchar ;
            mycompletename varchar ;   
          BEGIN
            select name into myname from res_partner where id = partnerid and is_company=True ;
            if myname is not null then
               myname1 = concat(myname,'(委外倉)') ;
               mycompletename = concat('WH/',myname1) ;
               select id into myparoutloc from stock_location where complete_name = mycompletename ;
               if myparoutloc is null then
                  insert into stock_location(name,complete_name,usage,location_id,active) values (myname1,mycompletename,'internal',7,True) ;
                  select max(id) into myparoutloc from stock_location ;
                  myparentpath = concat('1/7/',myparoutloc::TEXT,'/') ;
                  update stock_location set parent_path=myparentpath where id = myparoutloc ;
               end if ;
               update res_partner set blank_stock_supplier=myparoutloc where is_company=True and blank_stock_supplier is null and id = partnerid ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genalloutloc() cascade""")
        self._cr.execute("""create or replace function genalloutloc() returns void as $BODY$
          DECLARE
            par_cur refcursor ;
            par_rec record ;
          BEGIN
            open par_cur for select id,active,is_company from res_partner where active=True and is_company = True and blank_stock_supplier is null ;
            loop
              fetch par_cur into par_rec ;
              exit when not found ;
              execute genparoutloc(par_rec.id) ;
            end loop ;
            close par_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""create or replace function change_purchase_stockloc() returns trigger as $BODY$
         DECLARE
           poname varchar ;
           pickingid int ;
           blanklocid int ;
           mv_cur refcursor ;
           mv_rec record ;
           moveid int ;
           mvl_cur refcursor ;
           mvl_rec record ;
         BEGIN
           if NEW.state <> OLD.state and NEW.state='purchase' and OLD.is_blank_stockin=True then
              select name into poname from purchase_order where id = OLD.id ;
              select id into pickingid from stock_picking where origin=poname ;
              if OLD.is_blank_stockin=True and pickingid is not null then    
                select max(blank_loc) into blanklocid from alldo_acme_iot_company_stockloc ;
                if blanklocid > 0 then
                   update stock_picking set location_dest_id=blanklocid where id = pickingid ;
                   
                   open mvl_cur for select * from stock_move where picking_id = pickingid ;
                   loop
                     fetch mvl_cur into mvl_rec ;
                     exit when not found ;
                     update stock_move set location_dest_id=blanklocid where id = mvl_rec.id ;
                     update stock_move_line set location_dest_id=blanklocid where move_id=mvl_rec.id ;
                   end loop ;
                   close mvl_cur ;
                end if ;
              end if ; 
           end if ;
           return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists purchase_inloc_change on purchase_order;""")
        # self._cr.execute("""create trigger purchase_inloc_change after update on purchase_order
        #                          for each row execute procedure change_purchase_stockloc();""")

        self._cr.execute("""drop function if exists purchase_change_loc() cascade""")
        self._cr.execute("""create or replace function purchase_change_loc() returns void as $BODY$
          DECLARE
            po_cur refcursor ;
            po_rec record ;
            mvl_cur refcursor ;
            mvl_rec record ;
            ncount int ;
            blanklocid int ;
            pickingid int ;
          BEGIN
            select max(blank_loc) into blanklocid from alldo_acme_iot_company_stockloc ;
            open po_cur for select id,name from purchase_order where coalesce(is_blank_stockin,False)=True and coalesce(update_loc,False)=False ;
            loop
              fetch po_cur into po_rec ;
              exit when not found ;
              select count(*) into ncount from stock_picking where origin = po_rec.name ;
              if ncount > 0 then
                 select id into pickingid from stock_picking where origin=po_rec.name ;
                 update stock_picking set location_dest_id=blanklocid where id = pickingid ;
                 open mvl_cur for select * from stock_move where picking_id = pickingid ;
                   loop
                     fetch mvl_cur into mvl_rec ;
                     exit when not found ;
                     update stock_move set location_dest_id=blanklocid where id = mvl_rec.id ;
                     update stock_move_line set location_dest_id=blanklocid where move_id=mvl_rec.id ;
                   end loop ;
                   close mvl_cur ;
                 update purchase_order set update_loc=True where id = po_rec.id ;
              end if ;   
            end loop ;
            close po_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists changequant(saleid int) cascade""")
        self._cr.execute("""create or replace function changequant(saleid int) returns void as $BODY$
         DECLARE
           nqty float ;
           sl_cur refcursor ;
           sl_rec record ;
           q_cur refcursor ;
           q_rec record ;
         BEGIN
           open sl_cur for select product_id from sale_order_line where order_id=saleid ;
           loop
             fetch sl_cur into sl_rec ;
             exit when not found ;
             open q_cur for select id,quantity from stock_quant where product_id=sl_rec.product_id and location_id=8 and coalesce(quantity,0) > 0 and (temp_change=False or temp_change is null);
             loop
               fetch q_cur into q_rec ;
               exit when not found ;
               update stock_quant set temp_qty=coalesce(q_rec.quantity,0),temp_change=True where id = q_rec.id ;
               update stock_quant set quantity=1.1 where id = q_rec.id ;
             end loop ;
             close q_cur ;
           end loop ;
           close sl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists returnquant() cascade""")
        self._cr.execute("""create or replace function returnquant() returns void as $BODY$
         DECLARE
           q_cur refcursor ;
           q_rec record ;
         BEGIN
           open q_cur for select id,temp_qty from stock_quant where temp_change=True and location_id=8 and temp_qty > 0 ;
           loop
             fetch q_cur into q_rec ;
             exit when not found ;
             update stock_quant set quantity=coalesce(q_rec.temp_qty,0),temp_qty=0,temp_change=False where id = q_rec.id  ;
           end loop ;
           close q_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists changequant1(productionid int) cascade""")
        self._cr.execute("""create or replace function changequant1(productionid int) returns void as $BODY$
         DECLARE
           nqty float ;
           prodid int ;
           q_cur refcursor ;
           q_rec record ;
         BEGIN
             select product_id into prodid from mrp_production where id = productionid ;
             open q_cur for select id,quantity from stock_quant where product_id=prodid and location_id=8 and coalesce(quantity,0) > 0 and (temp_change=False or temp_change is null);
             loop
               fetch q_cur into q_rec ;
               exit when not found ;
               update stock_quant set temp_qty=coalesce(q_rec.quantity,0),temp_change=True where id = q_rec.id ;
               update stock_quant set quantity=1.1 where id = q_rec.id ;
             end loop ;
             close q_cur ;
          
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delsaleorder(saleid int) cascade""")
        self._cr.execute("""create or replace function delsaleorder(saleid int) returns void as $BODY$
         DECLARE
           mogroupid int ;
           saleno varchar ;
         BEGIN
           select name into saleno from sale_order where id = saleid ;
           select mo_group_id into mogroupid from mrp_production where origin=saleno ;
           if mogroupid is not null then
              delete from alldo_acme_iot_workorder where mo_group_id = mogroupid ;
              delete from alldo_acme_iot_outsuborder where mo_group_id = mogroupid ;
              delete from mrp_production where mo_group_id = mogroupid ;
              
           end if ;
           delete from sale_order where id = saleid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # self._cr.execute("""update alldo_acme_iot_outsuborder_prodout set date_supply=prodout_datetime::DATE""")
        # self._cr.execute("""update alldo_acme_iot_outsuborder_prodin set date_delivery=prodin_datetime::DATE""")

        self._cr.execute("""drop function if exists genoutsuborderkpi(partnerid int,sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function genoutsuborderkpi(partnerid int,sdate date,edate date) returns void as $BODY$
         DECLARE
           out_cur refcursor ;
           out_rec record ;
           po_cur refcursor ; /* product out */
           po_rec record ;
           pi_cur refcursor ; /* product in */
           pi_rec record ;
           maxid int ;
           dnum float ;
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           maxdatesupply date ;
           maxdatedelivery date ;
         BEGIN
           delete from alldo_acme_iot_outsuborder_kpi_line ;
           delete from alldo_acme_iot_outsuborder_kpi_line1 ;
           delete from alldo_acme_iot_outsuborder_kpi ;
           if partnerid = 0 then  /* 全部委外加工商 */
              open out_cur for select * from alldo_acme_iot_outsuborder where prod_date::DATE between sdate::DATE and edate::DATE ;
           else                   /* 單一委外加工商 */
              open out_cur for select * from alldo_acme_iot_outsuborder where (prod_date::DATE between sdate::DATE and edate::DATE) and cus_name=partnerid ;
           end if ;
           loop
              fetch out_cur into out_rec ;
              exit when not found ;
              select count(*) into ncount from alldo_acme_iot_outsuborder_kpi where outsub_id = out_rec.id ;
              if ncount = 0 then
                 insert into alldo_acme_iot_outsuborder_kpi(partner_id,outsub_id,product_no,outsub_num) values (out_rec.cus_name,out_rec.id,out_rec.product_no,coalesce(out_rec.order_num,0)) ;
              end if ;
              select max(id) into maxid from alldo_acme_iot_outsuborder_kpi ;
              open po_cur for select * from alldo_acme_iot_outsuborder_prodout where order_id=out_rec.id ;
              loop
                fetch po_cur into po_rec ;
                exit when not found ;
                /* 匯總供料明細 */
                select count(*) into ncount1 from alldo_acme_iot_outsuborder_kpi_line1 where supply_id=maxid ;
                if ncount1 = 0 then
                   insert into alldo_acme_iot_outsuborder_kpi_line1(supply_id,supply_num,date_due) values (maxid,po_rec.out_good_num,po_rec.date_due) ;   
                else 
                   update alldo_acme_iot_outsuborder_kpi_line1 set supply_num=coalesce(supply_num,0)+po_rec.out_good_num,date_due=po_rec.date_due where supply_id=maxid ;
                end if ;   
                update alldo_acme_iot_outsuborder_kpi set outsub_num=coalesce(po_rec.out_good_num,0) where id = maxid ; 
              end loop ;
              close po_cur ;
              select max(date_supply) into maxdatesupply from alldo_acme_iot_outsuborder_prodout where order_id=out_rec.id ;
              update alldo_acme_iot_outsuborder_kpi_line1 set date_supply=maxdatesupply where supply_id=maxid ;
              
              open pi_cur for select * from alldo_acme_iot_outsuborder_prodin where order_id=out_rec.id ;
              loop
                fetch pi_cur into pi_rec ;
                exit when not found ;
                dnum = coalesce(pi_rec.in_good_num,0) + coalesce(pi_rec.in_ng_num,0) ;
                select count(*) into ncount2 from alldo_acme_iot_outsuborder_kpi_line where delivery_id=maxid ;
                if ncount2 = 0 then
                   insert into alldo_acme_iot_outsuborder_kpi_line(delivery_id,date_delivery,delivery_num,good_num,ng_num) values 
                      (maxid,pi_rec.prodin_datetime::DATE,dnum,coalesce(pi_rec.in_good_num,0),coalesce(pi_rec.in_ng_num,0)) ;
                else
                   update alldo_acme_iot_outsuborder_kpi_line set delivery_num=coalesce(delivery_num,0)+dnum,
                       good_num=coalesce(good_num,0)+coalesce(pi_rec.in_good_num,0),
                       ng_num=coalesce(ng_num,0)+coalesce(pi_rec.in_ng_num,0) where delivery_id=maxid ;
                end if ;      
              end loop ;
              close pi_cur ;
              select max(date_delivery) into maxdatedelivery from alldo_acme_iot_outsuborder_prodin where order_id=out_rec.id ;
              update alldo_acme_iot_outsuborder_kpi_line set date_delivery=maxdatedelivery where delivery_id=maxid ;
           end loop ;
           close out_cur ;
           
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genkpiquant() cascade""")
        self._cr.execute("""create or replace function genkpiquant() returns void as $BODY$
         DECLARE
           kpi_cur refcursor ;
           kpi_rec record ;
           sup_cur refcursor ;
           sup_rec record ;
           del_cur refcursor ;
           del_rec record ;
           quant_cur refcursor ;
           quant_rec record ;
           nseq int ;
           nseq1 int ;
           nowseq int ;
           nitem int ;
           supnum float ;
           delnum float ;
           duedate date ;
           kpir float ;
           nextdate date ;
           deday int ;
           deratio float ;
           avgratio float ;
           sumde float ;
           ncount int ;
           maxdatedue date ;
           maxdeliverydate date ;
           deliverynum float ;
           maxdatelast date ;
           date_dur int ;
         BEGIN
           nseq = 10 ;
           delete from alldo_acme_iot_outsuborder_kpi_quant ;
           open kpi_cur for select * from alldo_acme_iot_outsuborder_kpi ;
           loop
              fetch kpi_cur into kpi_rec ;
              exit when not found ;
              /* 委外供貨明細 */
              open sup_cur for select * from alldo_acme_iot_outsuborder_kpi_line1 where supply_id=kpi_rec.id order by id ;
              loop
                fetch sup_cur into sup_rec ;
                exit when not found ;
                    insert into alldo_acme_iot_outsuborder_kpi_quant(quant_id,quant_seq,supply_num,date_supply,date_due,is_complete) values
                        (kpi_rec.id,nseq,sup_rec.supply_num,sup_rec.date_supply,sup_rec.date_due,False) ; 
                nseq = nseq + 10 ;    
              end loop ;
              close sup_cur ;
              /* 委外交貨明細  */
              select max(date_due) into maxdatedue from alldo_acme_iot_outsuborder_kpi_quant where quant_id=kpi_rec.id ;
              select max(date_delivery) into maxdeliverydate from alldo_acme_iot_outsuborder_kpi_line 
                    where delivery_id = kpi_rec.id and date_delivery <= maxdatedue ;
              select sum(delivery_num) into deliverynum from alldo_acme_iot_outsuborder_kpi_line where delivery_id = kpi_rec.id ;
              select max(date_delivery) into maxdatelast from alldo_acme_iot_outsuborder_kpi_line where delivery_id=kpi_rec.id ;
              if maxdeliverydate = maxdatelast then
                 update alldo_acme_iot_outsuborder_kpi_quant set date_delivery=maxdeliverydate,delivery_num=deliverynum,date_duration=0 where quant_id=kpi_rec.id ;
              else
                 select date_part('day',age(maxdatelast,maxdeliverydate))::INT into date_dur ;
                 update alldo_acme_iot_outsuborder_kpi_quant set date_delivery=maxdeliverydate,delivery_num=deliverynum,date_last=maxdatelast,date_duration=date_dur where quant_id=kpi_rec.id ;
              end if ;
           end loop ;
           close kpi_cur ;
           /* 滾算 quant 達成率 & 扣點 */
           open quant_cur for select * from alldo_acme_iot_outsuborder_kpi_quant where date_due is not null and date_delivery is not null  ;
           loop
             fetch quant_cur into quant_rec ;
             exit when not found ;
             kpir = round((quant_rec.delivery_num / quant_rec.supply_num),2) ;
             if kpir > 1 then
                kpir = 1.0 ;
             end if ;
             if quant_rec.delivery_num < quant_rec.supply_num then /* 要計算扣點 */
                deratio = round(quant_rec.date_duration * 0.5,1) ;    
             end if ;
             update alldo_acme_iot_outsuborder_kpi_quant set kpi_ratio=kpir,kpi_deduction=deratio where id=quant_rec.id ;
           end loop ;
           close quant_cur ;
           open kpi_cur for select id from alldo_acme_iot_outsuborder_kpi ;
           loop
             fetch kpi_cur into kpi_rec ;
             exit when not found ;
             select avg(kpi_ratio) into avgratio from alldo_acme_iot_outsuborder_kpi_quant where quant_id=kpi_rec.id and date_due is not null ;
             select sum(kpi_deduction) into sumde from alldo_acme_iot_outsuborder_kpi_quant where quant_id=kpi_rec.id and date_due is not null ;
             update alldo_acme_iot_outsuborder_kpi set kpi_ratio=avgratio,kpi_deduction=sumde where id = kpi_rec.id ;
           end loop ;
           close kpi_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensocompleted() cascade""")
        self._cr.execute("""create or replace function gensocompleted() returns void as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           update sale_order_line set is_completed=TRUE where qty_delivered >= product_uom_qty ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genfristchecklist(wid int,uid int) cascade""")
        self._cr.execute("""create or replace function genfristchecklist(wid int,uid int) returns void as $BODY$
        DECLARE 
          prodid int ;
          prodtmplid int ;
          chk_cur refcursor ;
          chk_rec record ;
          ncount int ;
          mynowdate date ;
        BEGIN
          mynowdate = now()::DATE ;
          select product_no into prodid from alldo_acme_iot_workorder where id=wid ;
          select product_tmpl_id into prodtmplid from product_product where id=prodid ;
          open chk_cur for select * from alldo_acme_iot_frist_prod_checklist where checklist_id=prodtmplid order by checklist_seq ;  
          loop
            fetch chk_cur into chk_rec ;
            exit when not found ;
            select count(*) into ncount from alldo_acme_iot_wkfrist_checklist where checklist_id=wid and checklist_item=chk_rec.checklist_item and checklist_date::DATE = chk_rec.checklist_date::DATE ;    
            if ncount = 0 then
               insert into alldo_acme_iot_wkfrist_checklist(checklist_id,checklist_item,checklist_value,checklist_date,checklist_user,checklist_status) values
                (wid,chk_rec.checklist_item,chk_rec.checklist_value,mynowdate,uid,'ok') ;
            end if ;
          end loop ;
          close chk_cur ;
        END ;$BODY$
        LANGUAGE plpgsql;""")

        #
        # self.env.cr.execute("""drop index if exists equipment_iotdata_index1 cascade""")
        # self.env.cr.execute("""create index equipment_iotdata_index1 on alldo_acme_iot_equipment_iot_data(iot_serial)""")
        # self.env.cr.execute("""drop index if exists iot_workorder_index1 cascade""")
        # self.env.cr.execute("""create index iot_workorder_index1 on alldo_acme_iot_workorder(name)""")
        # self.env.cr.execute("""drop index if exists iot_workorder_index2 cascade""")
        # self.env.cr.execute("""create index iot_workorder_index2 on alldo_acme_iot_workorder(name,state)""")
        # self.env.cr.execute("""drop index if exists maintenance_equipment_index1 cascade""")
        # self.env.cr.execute("""create index maintenance_equipment_index1 on maintenance_equipment(equipment_no)""")
        # self.env.cr.execute("""drop index if exists maintenance_equipment_index2 cascade""")
        # self.env.cr.execute("""create index maintenance_equipment_index2 on maintenance_equipment(iot_ip)""")
        # self.env.cr.execute("""drop index if exists hr_employee_index1 cascade""")
        # self.env.cr.execute("""create index hr_employee_index1 on hr_employee(emp_code)""")
        # self.env.cr.execute("""drop index if exists workorder_lastwork_index1 cascade""")
        # self.env.cr.execute("""create index workorder_lastwork_index1 on alldo_acme_iot_workorder_lastwork(work_datetime)""")
        # self.env.cr.execute("""drop index if exists node_status_index1 cascade""")
        # self.env.cr.execute("""create index node_status_index1 on alldo_acme_iot_node_change_status(node_datetime)""")
        # self.env.cr.execute("""drop index if exists emp_attendance_index1 cascade""")
        # self.env.cr.execute("""create index emp_attendance_index1 on alldo_acme_iot_emp_attendance(attendance_id,attendance_date,attendance_type) """)
        # self.env.cr.execute("""drop index if exists qcdate_index cascade""")
        # self.env.cr.execute("""create index qcdate_index on alldo_acme_iot_workorder_qc(qc_date)""")
        # self.env.cr.execute("""drop index if exists iotowner1_index cascade""")
        # self.env.cr.execute("""create index iotowner1_index on alldo_acme_iot_workorder_qc(iot_owner1)""")
        # self.env.cr.execute("""drop index if exists iotdata1_index cascade""")
        # self.env.cr.execute("""create index iotdata1_index on alldo_acme_iot_workorder_iot_data(iot_owner)""")
        # self.env.cr.execute("""drop index if exists iotdata2_index cascade""")
        # self.env.cr.execute("""create index iotdata2_index on alldo_acme_iot_workorder_iot_data(iot_date)""")
        #
