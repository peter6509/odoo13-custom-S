# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebtimesheetstoreproc(models.Model):
    _name = "neweb_emp_timesheet.store_proc"


    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS sortworktype() cascade;""")
        self._cr.execute("""create or replace function sortworktype() returns void as $BODY$
         DECLARE 
           wk_cur refcursor ;
           wk_rec record ;
           myitem int ;
         BEGIN 
           myitem = 1 ;
           open wk_cur for select id from neweb_emp_timesheet_timesheet_worktype order by sequence,worktype_code ;
           loop
             fetch wk_cur into wk_rec ;
             exit when not found ;
             update neweb_emp_timesheet_timesheet_worktype set nitem=myitem where id = wk_rec.id ;
             myitem = myitem + 1 ;
           end loop ;
           close wk_cur ;
         END;$BODY$
         LANGUAGE plpgsql""")


        self._cr.execute("""drop function if exists sorttimesheetitem(tsid int) cascade""")
        self._cr.execute("""create or replace function sorttimesheetitem(tsid int) returns void as $BODY$
            DECLARE 
              ts_cur refcursor ;
              ts_rec record ;
              myitem int ;
            BEGIN 
              myitem = 1 ;
              open ts_cur for select id from neweb_emp_timesheet_timesheet_calendar_line where line_id=tsid 
                 order by sequence,timesheet_start_date ;
              loop
                 fetch ts_cur into ts_rec ;
                 exit when not found ;
                 update neweb_emp_timesheet_timesheet_calendar_line set nitem=myitem where id = ts_rec.id ;
                 myitem = myitem + 1 ;
              end loop ;
              close ts_cur ;   
            END;$BODY$
            LANGUAGE plpgsql;""")


        # self._cr.execute("""drop function if exists gettimesheetlineid(myempid int,mystartdate timestamp) cascade""")
        self._cr.execute("""drop function if exists gettimesheetlineid(myempid int,mystartdate varchar) cascade""")
        self._cr.execute("""create or replace function gettimesheetlineid(myempid int,mystartdate varchar) returns int as $BODY$
            DECLARE 
               myres int ;
               myyear varchar ;
               mymon varchar ;
               myyearmon varchar ;
               ncount int ;
            BEGIN 
               
               myyearmon = mystartdate ;
               select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=myempid and 
                  timesheet_yearmonth = myyearmon ;
               if ncount > 0 then 
                  select id into myres from neweb_emp_timesheet_timesheet_calendar where emp_id=myempid and 
                  timesheet_yearmonth = myyearmon ;
               else 
                  insert into neweb_emp_timesheet_timesheet_calendar(emp_id,timesheet_yearmonth) values 
                           (myempid,myyearmon) ;
                   select id into myres from neweb_emp_timesheet_timesheet_calendar where emp_id=myempid and 
                  timesheet_yearmonth = myyearmon ;         
               end if ; 
               return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkemptimesheet(myempid int,myyearmonth varchar) cascade""")
        self._cr.execute("""create or replace function checkemptimesheet(myempid int,myyearmonth varchar) returns Boolean as $BODY$
               DECLARE 
                 ncount int ;
                 myres Boolean ;
               BEGIN 
                 select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=myempid and timesheet_yearmonth = myyearmonth ;
                 if ncount > 0 then 
                    myres = TRUE ;
                 else 
                    myres = FALSE ;
                 end if ;
                 return myres ;    
               END;$BODY$
               LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_inspection_timesheet(contractid int) cascade""")
        self._cr.execute("""drop function if exists update_inspection_timesheet(contractid int,userid int) cascade""")
        self._cr.execute("""create or replace function update_inspection_timesheet(contractid int,userid int) returns void as $BODY$
           DECLARE 
             ins_cur refcursor ;
             ins_rec record ;
             ncount int ;
             lockdate date ;
             myyear varchar ;
             mymonth varchar ;
             myyearmonth varchar ;
             ncount1 int ;
             mycalid int ;
             mystartdate timestamp ;
             myenddate timestamp ;
             mytimesheetorigin varchar ;
             mytimesheetcus int ;
             ismaintenance Boolean ;
             isoutsourcing Boolean ;
             myworktype int ;
             isadjowner Boolean ;
           BEGIN 
             select getadjustowner(userid) into isadjowner ;
             select name,end_customer into mytimesheetorigin,mytimesheetcus from neweb_contract_contract where id = contractid ;
             if isadjowner = False then
                select coalesce(lock_date,now()::DATE - interval '2 month') into lockdate from neweb_emp_timesheet_timesheet_lock  ;
             else
                select (now()::DATE - interval '1 year') into lockdate ;
             end if ;   
             select is_maintenance_contract,is_outsourcing_service into ismaintenance,isoutsourcing from neweb_contract_contract where id = contractid ;
             myworktype = 11 ;
             if ismaintenance = TRUE then
                select id into myworktype from neweb_emp_timesheet_timesheet_worktype where worktype_code='20' ; 
             elsif isoutsourcing = TRUE then
                select id into myworktype from neweb_emp_timesheet_timesheet_worktype where worktype_code='30' ;
             end if ;   
             open ins_cur for select * from neweb_contract_inspection_list where inspection_id = contractid 
             and actual_start_datetime is not null and actual_end_datetime is not null 
             and  actual_end_datetime::DATE > lockdate ;
             loop
                fetch ins_cur into ins_rec ;
                exit when not found ;
                select date_part('year',ins_rec.actual_end_datetime + interval '8 hours')::TEXT into myyear ;
                select date_part('month',ins_rec.actual_end_datetime + interval '8 hours')::TEXT into mymonth ;
                if length(mymonth) = 1 then
                    mymonth = concat('0',mymonth) ; 
                end if ;
                select concat(myyear,'-',mymonth) into myyearmonth ;
                select count(*) into ncount1 from neweb_emp_timesheet_timesheet_calendar where emp_id=ins_rec.emp_id and 
                   timesheet_yearmonth=myyearmonth ;
                if ncount1 = 0 then 
                   insert into neweb_emp_timesheet_timesheet_calendar (emp_id,timesheet_yearmonth)
                      values (ins_rec.emp_id,myyearmonth) ;
                end if ;
                select id into mycalid from neweb_emp_timesheet_timesheet_calendar where emp_id=ins_rec.emp_id and 
                   timesheet_yearmonth=myyearmonth ;
                select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar_line where emp_id=ins_rec.emp_id and
                      origin_id=ins_rec.id and origin_type='1' ;
                select date_trunc('minute',(ins_rec.actual_start_datetime + interval '8 hours')::TIMESTAMP) into mystartdate ;
                select date_trunc('minute',(ins_rec.actual_end_datetime + interval '8 hours')::TIMESTAMP) into myenddate ;      
                if ncount = 0 then 
                   insert into neweb_emp_timesheet_timesheet_calendar_line (line_id,emp_id,timesheet_start_date,timesheet_end_date,
                   timesheet_origin,timesheet_custom,origin_id,origin_type,timesheet_desc,timesheet_worktype) values (mycalid,ins_rec.emp_id,
                   ins_rec.actual_start_datetime,ins_rec.actual_end_datetime,mytimesheetorigin,mytimesheetcus,ins_rec.id,'1',ins_rec.inspection_memo,myworktype) ;
                          
                else 
                   update neweb_emp_timesheet_timesheet_calendar_line set timesheet_start_date=ins_rec.actual_start_datetime,
                     timesheet_end_date = ins_rec.actual_end_datetime,timesheet_custom=mytimesheetcus,timesheet_origin=mytimesheetorigin,
                     origin_id=ins_rec.id,timesheet_desc=ins_rec.inspection_memo,timesheet_worktype=myworktype where  emp_id=ins_rec.emp_id and
                      origin_id=ins_rec.id and origin_type='1' ;
                end if ;
             end loop ;
             close ins_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delinspectiontimesheet(originid int) cascade""")
        self._cr.execute("""drop function if exists delinspectiontimesheet(originid int,userid int) cascade""")
        self._cr.execute("""create or replace function delinspectiontimesheet(originid int,userid int) returns void as $BODY$
           DECLARE 
             ncount int ;
             lockdate date ;
             isadjowner Boolean ;
           BEGIN
             select getadjustowner(userid) into isadjowner ;
             if isadjowner = False then
                select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock  ;
             else
                select (now()::DATE - interval '1 year') into lockdate  ;
             end if ;   
             delete from neweb_emp_timesheet_timesheet_calendar_line where origin_id = originid and 
                origin_type = '1' and timesheet_start_date::DATE > lockdate  ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setlocktimesheetdate() cascade""")
        self._cr.execute("""create or replace function setlocktimesheetdate() returns void as $BODY$
           DECLARE 
             myyear varchar ;
             mymonth varchar ;
             myyearmonth varchar ;
             myyearmonthdate varchar ;
             myyearmonthdate1 date ;
             nyear int ;
             nmonth int ;
             mydate date ;
             ncount int ;
             
           BEGIN
             select count(*) into ncount from neweb_emp_timesheet_timesheet_lock ;
             if ncount > 0 then 
                select yearmonth into myyearmonth from neweb_emp_timesheet_timesheet_lock ;
                select substring(myyearmonth,1,4) into myyear ;
                select substring(myyearmonth,6,2) into mymonth ;
                SELECT myyear::int into nyear ;
                SELECT mymonth::int into nmonth ;
                if nmonth = 12 then
                   nyear = nyear + 1 ;
                   select nyear::text into myyear ;
                   mymonth = '01' ;
                   select concat(myyear,'-',mymonth,'-','01') into myyearmonthdate ; 
                else 
                   select (nmonth+1)::text into mymonth ;  
                   if length(mymonth)=1 then 
                      select concat('0',mymonth) into mymonth ;
                   end if ;
                   select concat(myyear,'-',mymonth,'-','01') into myyearmonthdate ;
                end if ;
                select to_date(myyearmonthdate,'YYYY-MM-DD') into myyearmonthdate1 ;
                select myyearmonthdate1 + integer '-1' into mydate ;
                update neweb_emp_timesheet_timesheet_lock set lock_date=mydate ;
                update neweb_emp_timesheet_timesheet_calendar_line set is_locked=TRUE where 
                       timesheet_end_date <= mydate ;
                update neweb_emp_timesheet_timesheet_calendar_line set is_locked=FALSE where 
                       timesheet_end_date > mydate ;   
                update neweb_emp_timesheet_timesheet_calendar set is_closed=TRUE where 
                    timesheet_yearmonth <= myyearmonth ;
                update neweb_emp_timesheet_timesheet_calendar set is_closed=FALSE where 
                    timesheet_yearmonth > myyearmonth ;           
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists update_inspection_datetime(ins_line_id int) cascade""")
        self._cr.execute("""create or replace function update_inspection_datetime(ins_line_id int) returns void
            as $BODY$ 
               DECLARE 
                 mystartdate timestamp ;
                 myenddate timestamp ;
                 ncount int ;
                 mymemo varchar ;
               BEGIN
                 select count(*) into ncount from neweb_contract_inspection_list 
                   where actual_start_datetime is not null and actual_end_datetime is not null 
                     and id = ins_line_id ;
                 if ncount > 0 then  
                     select actual_start_datetime,actual_end_datetime,inspection_memo into mystartdate,myenddate,mymemo from 
                        neweb_contract_inspection_list where id = ins_line_id ;
                     select date_trunc('minute',mystartdate::TIMESTAMP) into mystartdate ;
                     select date_trunc('minute',myenddate::TIMESTAMP) into myenddate ;
                     update neweb_contract_inspection_list set actual_start_datetime=mystartdate,
                        actual_end_datetime=myenddate where id = ins_line_id ;   
                     update neweb_emp_timesheet_inspection_calendar set inspection_complete='Y',
                     inspection_start_datetime=mystartdate,inspection_end_datetime=myenddate,inspection_memo=mymemo
                        where inspection_sequence = ins_line_id ;   
                 end if ;       
               END;$BODY$
               LANGUAGE plpgsql ;""")


        self._cr.execute("""drop function if exists update_repair_timesheet(repairid int) cascade""")
        self._cr.execute("""drop function if exists update_repair_timesheet(repairid int,userid int) cascade""")
        self._cr.execute("""create or replace function update_repair_timesheet(repairid int,userid int) returns void as $BODY$
          DECLARE 
             work_cur refcursor ;
             work_rec record ;
             ncount int ;
             lockdate date ;
             myyear varchar;
             mymonth varchar;
             myyearmonth varchar;
             ncount1 int ;
             mystartdate TIMESTAMP ;
             myenddate TIMESTAMP ;
             mytimesheetorigin varchar;
             mytimesheetcus int ;
             mycalid int ;
             mycontractid int ;
             myhour float ;
             myminute float ;
             mytime float ;
             myrepairtype varchar ;
             myworktype varchar ;
             myworktypeid int ;
             mymaxid int ;
             saleid int ;
             isadjowner Boolean ;
          BEGIN 
              select getadjustowner(userid) into isadjowner ;
              select end_customer,contract_id,repair_type,name,coalesce(sales,0) into mytimesheetcus,mycontractid,myrepairtype,mytimesheetorigin,saleid 
                  from neweb_repair_repair where id = repairid ;
              if myrepairtype='per_call' then 
                 myworktype = '10' ;
              elsif myrepairtype='warranty_maintenance' then 
                 myworktype = '41' ;
              elsif myrepairtype='warranty_software' then 
                 myworktype = '42' ;   
              elsif myrepairtype='hw_maintenance' then 
                 myworktype = '21' ;    
              elsif myrepairtype='soft_maintenance' then 
                 myworktype = '22' ;   
              elsif myrepairtype='hw_outsourcing' then 
                 myworktype = '31' ;    
              elsif myrepairtype='soft_outsourcing' then 
                 myworktype = '32' ;
              elsif myrepairtype='no_warranty_support' then 
                 myworktype = '4B' ;
              end if ;      
              select id into myworktypeid  from neweb_emp_timesheet_timesheet_worktype where 
                 worktype_code = myworktype ;     
              if isadjowner = False then
                 select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock  ;
              else
                 select (now()::DATE - interval '1 year') into lockdate  ;
              end if ;   
              open work_cur for select * from neweb_repair_repair_work_log where repair_id=repairid and 
                 work_start_datetime is not null and work_end_datetime is not null and
                   work_end_datetime::DATE > lockdate ;
              loop
                    fetch work_cur into work_rec ;
                    exit when not found ;
                    select date_part('year',work_rec.work_end_datetime + interval '8 hours')::TEXT into myyear ;
                    select date_part('month',work_rec.work_end_datetime + interval '8 hours')::TEXT into mymonth ;
                    if length(mymonth) = 1 then
                       mymonth = concat('0',mymonth) ;
                    end if ;
                    select concat(myyear,'-',mymonth) into myyearmonth ;
                    select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=work_rec.work_emp and 
                       timesheet_yearmonth=myyearmonth ;
                    if ncount = 0 then 
                       insert into neweb_emp_timesheet_timesheet_calendar (emp_id,timesheet_yearmonth)
                          values (work_rec.work_emp,myyearmonth) ;
                    end if ;
                    select id into mycalid from neweb_emp_timesheet_timesheet_calendar where emp_id=work_rec.work_emp and 
                       timesheet_yearmonth=myyearmonth ;
                     select count(*) into ncount1 from neweb_emp_timesheet_timesheet_calendar_line where emp_id=work_rec.work_emp and
                      origin_id=work_rec.id and origin_type='2' ;
                    select date_trunc('minute',(work_rec.work_start_datetime + interval '8 hours')::TIMESTAMP) into mystartdate ;
                    select date_trunc('minute',(work_rec.work_end_datetime + interval '8 hours')::TIMESTAMP) into myenddate ;    
                    select abs(date_part('hour',age(myenddate,mystartdate))) into myhour;
                    select abs(date_part('minute',age(myenddate,mystartdate))) into myminute ;
                    mytime = myhour + (myminute/60) ;  
                    if ncount1 = 0 then 
                       if saleid > 0 then
                           insert into neweb_emp_timesheet_timesheet_calendar_line (line_id,emp_id,timesheet_start_date,timesheet_end_date,
                           timesheet_origin,timesheet_custom,origin_id,origin_type,timesheet_desc,duration,timesheet_worktype,timesheet_duration,sale_id) 
                             values (mycalid,work_rec.work_emp,work_rec.work_start_datetime,work_rec.work_end_datetime,mytimesheetorigin,mytimesheetcus,
                           work_rec.id,'2',work_rec.work_log,mytime,myworktypeid,mytime,saleid) ;    
                       else
                           insert into neweb_emp_timesheet_timesheet_calendar_line (line_id,emp_id,timesheet_start_date,timesheet_end_date,
                           timesheet_origin,timesheet_custom,origin_id,origin_type,timesheet_desc,duration,timesheet_worktype,timesheet_duration) 
                             values (mycalid,work_rec.work_emp,work_rec.work_start_datetime,work_rec.work_end_datetime,mytimesheetorigin,mytimesheetcus,
                           work_rec.id,'2',work_rec.work_log,mytime,myworktypeid,mytime) ; 
                       end if ;      
                    else 
                       if saleid > 0 then
                           update neweb_emp_timesheet_timesheet_calendar_line set timesheet_start_date=work_rec.work_start_datetime,
                             timesheet_end_date = work_rec.work_end_datetime,timesheet_custom=mytimesheetcus,timesheet_origin=mytimesheetorigin,
                             origin_id=work_rec.id,timesheet_desc=work_rec.work_log,duration=mytime,timesheet_worktype=myworktypeid,timesheet_duration=mytime,
                             sale_id=saleid where  emp_id=work_rec.work_emp and origin_id=work_rec.id and origin_type='2' ;
                       else
                            update neweb_emp_timesheet_timesheet_calendar_line set timesheet_start_date=work_rec.work_start_datetime,
                         timesheet_end_date = work_rec.work_end_datetime,timesheet_custom=mytimesheetcus,timesheet_origin=mytimesheetorigin,
                         origin_id=work_rec.id,timesheet_desc=work_rec.work_log,duration=mytime,timesheet_worktype=myworktypeid,timesheet_duration=mytime 
                            where  emp_id=work_rec.work_emp and origin_id=work_rec.id and origin_type='2' ;
                       end if ;         
                    end if ;
                    select id into mymaxid from neweb_emp_timesheet_timesheet_calendar_line where emp_id=work_rec.work_emp and origin_id=work_rec.id and origin_type='2' ;  
                    execute checkcalendarline(mymaxid) ; 
              end loop ;
              close work_cur ;     
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists del_repair_timesheet(repid int) cascade""")
        self._cr.execute("""drop function if exists del_repair_timesheet(repid int,userid int) cascade""")
        self._cr.execute("""create or replace function del_repair_timesheet(repid int,userid int) returns void as $BODY$
          DECLARE 
            work_cur refcursor ;
            work_rec record ;
            lockdate date ;
            isadjowner Boolean ;
          BEGIN 
            select getadjustowner(userid) into isadjowner ;
            if isadjowner = False then
               select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock  ;
            else
               select (now()::DATE - interval '1 year') into lockdate ;
            end if ;   
            open work_cur for select * from neweb_repair_repair_work_log where repair_id=repid and 
                   work_end_datetime::DATE > lockdate ;
            loop
               fetch work_cur into work_rec ;
               exit when not found ;
               delete from neweb_emp_timesheet_timesheet_calendar_line where origin_type='2' and origin_id=work_rec.id and emp_id = work_rec.work_emp ;
            end loop ;
            close work_cur ;       
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists del_repair_work_log(originid int) cascade""")
        self._cr.execute("""drop function if exists del_repair_work_log(originid int,userid int) cascade""")
        self._cr.execute("""create or replace function del_repair_work_log(originid int,userid int) returns void as $BODY$
              DECLARE 
                 ncount int ;
                 isadjowner Boolean ;
              BEGIN 
                  select getadjustowner(userid) into isadjowner ;
                  if isadjowner = False then
                     delete from neweb_emp_timesheet_timesheet_calendar_line where origin_id = originid and 
                            origin_type = '2' and is_locked = False ;
                  else
                     delete from neweb_emp_timesheet_timesheet_calendar_line where origin_id = originid and 
                            origin_type = '2' ;
                  end if ;          
              END;$BODY$
              LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_assignline_datetime(assignlineid int) cascade""")
        self._cr.execute("""create or replace function update_assignline_datetime(assignlineid int) returns void
           as $BODY$ 
              DECLARE 
                mystartdate timestamp ;
                myenddate timestamp ;
                ncount int ;
              BEGIN
                select count(*) into ncount from neweb_assign_complete where assign_start_datetime is not null
                  and assign_end_datetime is not null and id = assignlineid ;
                if ncount > 0 then  
                    select assign_start_datetime,assign_end_datetime into mystartdate,myenddate from 
                       neweb_assign_complete where id = assignlineid ;
                    select date_trunc('minute',mystartdate::TIMESTAMP) into mystartdate ;
                    select date_trunc('minute',myenddate::TIMESTAMP) into myenddate ;
                    update neweb_assign_complete set assign_start_datetime=mystartdate,
                       assign_end_datetime=myenddate where id = assignlineid ;   
                end if ;       
              END;$BODY$
              LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists del_assingline_timesheet(assignlineid int) cascade""")
        self._cr.execute("""drop function if exists del_assingline_timesheet(assignlineid int,userid int) cascade""")
        self._cr.execute("""create or replace function del_assingline_timesheet(assignlineid int,userid int) returns void as $BODY$
                      DECLARE 
                         ncount int ;
                         isadjowner Boolean ;
                      BEGIN 
                         select getadjustowner(userid) into isadjowner ;
                         if isadjowner = False then
                            delete from neweb_emp_timesheet_timesheet_calendar_line where origin_id = assignlineid and 
                                origin_type in ('3','4') and is_locked = False ;
                         else
                            delete from neweb_emp_timesheet_timesheet_calendar_line where origin_id = assignlineid and 
                                origin_type in ('3','4') ;
                         end if ;       
                      END;$BODY$
                      LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_assign_timesheet(assignid int) cascade""")
        self._cr.execute("""drop function if exists gen_assign_timesheet(assignid int,userid int) cascade""")
        self._cr.execute("""create or replace function gen_assign_timesheet(assignid int,userid int) returns void as $BODY$
           DECLARE 
             assl_cur refcursor ;
             assl_rec record ;
             ncount int ;
             lockdate date ;
             myyear varchar ;
             mymonth varchar ;
             myyearmonth varchar ;
             ncount1 int ;
             mycalid int ;
             mystartdate timestamp ;
             myenddate timestamp ;
             mytimesheetorigin varchar ;
             mytimesheetcus int ;
             myhour float ;
             myminute float ;
             mytime float ;
             mysaleid int ;
             mymemo varchar ;
             myprojadd varchar ;
             projno int ;
             origintype char ;
             isadjowner Boolean ;
           BEGIN 
             select assign_no,proj_cus_name,proj_sale,setup_address,proj_no into mytimesheetorigin,mytimesheetcus,mysaleid,myprojadd,projno 
                from neweb_proj_eng_assign where id = assignid ;
             if projno is null then
                origintype := '3' ;
             else
                origintype := '4' ;
             end if ;
             select getadjustowner(userid) into isadjowner ;
             if isadjowner = False then
                select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate 
                      from neweb_emp_timesheet_timesheet_lock ;
             else
                select (now()::DATE - interval '1 year') into lockdate ;
             end if ;         
             open assl_cur for select * from neweb_assign_complete where complete_id = assignid and
               assign_start_datetime is not null and assign_end_datetime is not null and work_type is not null
                 and assign_end_datetime::DATE > lockdate ;
             loop
                fetch assl_cur into assl_rec ;
                exit when not found ;
                select date_part('year',assl_rec.assign_end_datetime + interval '8 hours')::TEXT into myyear ;
                select date_part('month',assl_rec.assign_end_datetime + interval '8 hours')::TEXT into mymonth ;
                if length(mymonth) = 1 then
                   mymonth = concat('0',mymonth) ;
                end if ;
                select concat(myyear,'-',mymonth) into myyearmonth ;
                select count(*) into ncount1 from neweb_emp_timesheet_timesheet_calendar where emp_id=assl_rec.emp_id and 
                   timesheet_yearmonth=myyearmonth ;
                if ncount1 = 0 then 
                   insert into neweb_emp_timesheet_timesheet_calendar (emp_id,timesheet_yearmonth)
                      values (assl_rec.emp_id,myyearmonth) ;
                end if ;
                select id into mycalid from neweb_emp_timesheet_timesheet_calendar where emp_id=assl_rec.emp_id and 
                   timesheet_yearmonth=myyearmonth ;
                select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar_line where emp_id=assl_rec.emp_id and
                      origin_id=assl_rec.id and origin_type=origintype ;
                select date_trunc('minute',(assl_rec.assign_start_datetime + interval '8 hours')::TIMESTAMP) into mystartdate ;
                select date_trunc('minute',(assl_rec.assign_end_datetime + interval '8 hours')::TIMESTAMP) into myenddate ;    
                select abs(date_part('hour',age(myenddate,mystartdate))) into myhour ;
                select abs(date_part('minute',age(myenddate,mystartdate))) into myminute ;
                mytime = myhour + (myminute/60) ;  
                if ncount = 0 then 
                   if mytimesheetcus is null then 
                     mymemo = concat('(',myprojadd,') ',assl_rec.man_memo) ;
                     insert into neweb_emp_timesheet_timesheet_calendar_line (line_id,emp_id,timesheet_start_date,timesheet_end_date,
                       timesheet_origin,sale_id,origin_id,origin_type,timesheet_desc,timesheet_worktype,duration,timesheet_duration)
                        values (mycalid,assl_rec.emp_id,assl_rec.assign_start_datetime,assl_rec.assign_end_datetime,mytimesheetorigin,
                        mysaleid,assl_rec.id,origintype,mymemo,assl_rec.work_type,mytime,mytime) ;
                   else
                     insert into neweb_emp_timesheet_timesheet_calendar_line (line_id,emp_id,timesheet_start_date,timesheet_end_date,
                     timesheet_origin,timesheet_custom,origin_id,origin_type,timesheet_desc,timesheet_worktype,duration,timesheet_duration)
                     values (mycalid,assl_rec.emp_id,assl_rec.assign_start_datetime,assl_rec.assign_end_datetime,mytimesheetorigin,
                       mytimesheetcus,assl_rec.id,origintype,assl_rec.man_memo,assl_rec.work_type,mytime,mytime) ;
                   end if ;
                else 
                   if mytimesheetcus is null then 
                       mymemo = concat('(',myprojadd,') ',assl_rec.man_memo) ;
                       update neweb_emp_timesheet_timesheet_calendar_line set timesheet_start_date=assl_rec.assign_start_datetime,
                        timesheet_end_date = assl_rec.assign_end_datetime,sale_id=mysaleid,timesheet_origin=mytimesheetorigin,
                        origin_id=assl_rec.id,timesheet_desc=mymemo,timesheet_worktype=assl_rec.work_type,duration=mytime 
                        where  emp_id=assl_rec.emp_id and origin_id=assl_rec.id and origin_type=origintype ;
                   else 
                       update neweb_emp_timesheet_timesheet_calendar_line set timesheet_start_date=assl_rec.assign_start_datetime,
                        timesheet_end_date = assl_rec.assign_end_datetime,timesheet_custom=mytimesheetcus,timesheet_origin=mytimesheetorigin,
                        origin_id=assl_rec.id,timesheet_desc=assl_rec.man_memo,timesheet_worktype=assl_rec.work_type,duration=mytime 
                        where  emp_id=assl_rec.emp_id and origin_id=assl_rec.id and origin_type=origintype ;
                   end if ;
                end if ;
             end loop ;
             close assl_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists del_assign_timesheet(assignid int) cascade""")
        self._cr.execute("""drop function if exists del_assign_timesheet(assignid int,userid int) cascade""")
        self._cr.execute("""create or replace function del_assign_timesheet(assignid int,userid int) returns void as $BODY$
         DECLARE 
           assl_cur refcursor ;
           assl_rec record ;
         BEGIN
           open assl_cur for select * from neweb_assign_complete where complete_id = assignid ;
           loop
              fetch assl_cur into assl_rec ;
              exit when not found ;
              execute del_assingline_timesheet(assl_rec.id,userid) ;
           end loop ;
           close assl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""update neweb_repair_repair set repair_type='hw_maintenance' where repair_type='maintenance'""")
        self._cr.execute("""update neweb_repair_repair set repair_type='hw_outsourcing' where repair_type='outsourcing'""")
        self._cr.execute("""update neweb_repair_repair set repair_type='hw_maintenance' where repair_type='maintenance'""")
        self._cr.execute("""update neweb_repair_repair set repair_type='warranty_maintenance' where repair_type='warranty'""")
        self._cr.execute("""update neweb_emp_timesheet_timesheet_worktype set worktype_categ='維運工時' where id=12""")
        self._cr.execute("""update neweb_emp_timesheet_timesheet_worktype set worktype_categ='維護工時' where id=22""")

        self._cr.execute("""drop function if exists checkrepairdate(replineid int) cascade""")
        self._cr.execute("""create or replace function checkrepairdate(replineid int) returns char as $BODY$
                 DECLARE 
                   ncount int ;
                   myres char ;
                   startdate TIMESTAMP ;
                   enddate TIMESTAMP ;
                 BEGIN 
                   select (work_start_datetime + interval '8 hours'),(work_end_datetime + interval '8 hours') into startdate,enddate 
                        from neweb_repair_repair_work_log where id = replineid ;
                   if startdate is null or enddate is null then 
                      myres = '1' ;
                   elsif startdate::DATE != enddate::DATE then     
                      myres = '2' ;
                   elsif startdate = enddate then 
                      myres = '3' ;  
                   end if ;  
                   return myres ;
                 END;$BODY$
                 LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS gen_contract_list(contractid int,inspectionmode int) cascade;""")
        self._cr.execute("""DROP FUNCTION IF EXISTS gen_contract_list(contractid int,inspectionmode int,userid int) cascade;""")
        self._cr.execute("""create or replace function gen_contract_list(contractid int,inspectionmode int,userid int) returns void as $BODY$
               declare
                 start_date date ;
                 end_date date ;
                 start_main_date date ;
                 sub_main_date date ;
                 createdate date ;
                 mycount int;
                 mysubyear varchar;
                 myroutinemaintenancenew int ;
                 ae1_cur refcursor ;
                 ae1_rec record ;
                 maxid int ;
               BEGIN
                 select routine_maintenance_new into myroutinemaintenancenew from neweb_contract_contract where id=contractid ;
                 /*if myroutinemaintenancenew = 1 then 
                 elsif myroutinemaintenancenew = 2 then 
                 elsif myroutinemaintenancenew = 3 then 
                 elsif myroutinemaintenancenew = 4 then 
                 end if ;*/
                 select maintenance_start_date,maintenance_end_date into start_date,end_date from neweb_contract_contract
                        where id = contractid ;
                 mycount := 1;
                 select now() into createdate ;
                 select start_date + interval '15 days' into start_main_date ;
                 select to_char(EXTRACT(year from start_main_date),'FM9999') into mysubyear ;
                 open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where 
                      neweb_contract_contract_id = contractid ;
                 loop  
                   fetch ae1_cur into ae1_rec ;
                   exit when not found ;   
                   insert into neweb_contract_inspection_list(inspection_id,subscribe_date,create_date,subscribe_year,emp_id) values 
                       (contractid,start_main_date,createdate,mysubyear,ae1_rec.hr_employee_id);
                 end loop ;
                 close ae1_cur ;
                 LOOP
                  if myroutinemaintenancenew = 1 then /* 月維護 */
                    select start_main_date + interval '1 month' into sub_main_date;
                  elsif myroutinemaintenancenew = 3 then  /* 雙月 */
                    select start_main_date + interval '2 month' into sub_main_date;
                  elsif myroutinemaintenancenew = 2 then  /* 季維護  */
                    select start_main_date + interval '3 month' into sub_main_date;
                  elsif myroutinemaintenancenew = 4 then  /* 半年 */
                    select start_main_date + interval '6 month' into sub_main_date;
                  elsif myroutinemaintenancenew = 6 then  /* 每二月 */ 
                    select start_main_date + interval '2 month' into sub_main_date;
                  elsif myroutinemaintenancenew = 7 then  /* 一年 */
                    select start_main_date + interval '12 month' into sub_main_date;  
                  end if;
                  exit when sub_main_date > end_date ;
                  select to_char(EXTRACT(year from sub_main_date),'FM9999') into mysubyear ;
                  open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where 
                      neweb_contract_contract_id = contractid ;
                  loop    
                    fetch ae1_cur into ae1_rec ;
                    exit when not found ;
                    insert into neweb_contract_inspection_list(inspection_id,subscribe_date,create_date,subscribe_year,emp_id) values 
                         (contractid,sub_main_date,createdate,mysubyear,ae1_rec.hr_employee_id) ;
                  end loop ;
                  close ae1_cur ;
                  mycount := mycount + 1 ;
                  start_main_date := sub_main_date;
                END LOOP;
                /* execute update_plan_ins_calendar(contractid,userid) ; */
               end; $BODY$
               LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkinspectiondate(inslistid int) cascade""")
        self._cr.execute("""create or replace function checkinspectiondate(inslistid int) returns char as $BODY$
                         DECLARE 
                           ncount int ;
                           myres char ;
                           startdate TIMESTAMP ;
                           enddate TIMESTAMP ;
                         BEGIN 
                           select (actual_start_datetime + interval '8 hours'),(actual_end_datetime + interval '8 hours') into
                           startdate,enddate from neweb_contract_inspection_list where id = inslistid ;
                           if startdate is null or enddate is null then 
                              myres = '1' ;
                           elsif startdate::DATE != enddate::DATE then     
                              myres = '2' ;
                           elsif startdate = enddate then 
                              myres = '3' ;  
                           end if ;  
                           return myres ;
                         END;$BODY$
                         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists updaterepaircalendar(repid int) cascade""")
        self._cr.execute("""drop function if exists updaterepaircalendar(repid int,userid int) cascade""")
        self._cr.execute("""create or replace function updaterepaircalendar(repid int,userid int) returns void as $BODY$
                 DECLARE 
                   ncount int ;
                   ncount1 int ;
                   rep_cur refcursor ;
                   rep_rec record ;
                   myempmanager int ;
                   mydeptid int ;
                   myrepairname varchar ;
                   mycusname varchar ;
                   myempname varchar ;
                   lockdate date ;
                   myresourceid int ;
                   myhour float ;
                   myminute float ;
                   mytime float ;
                   isadjowner Boolean ;
                 BEGIN 
                   select getadjustowner(userid) into isadjowner ;
                   if isadjowner = False then
                      select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock ;
                   else
                      select (now()::DATE - interval '1 year') into lockdate ;
                   end if ;   
                   open rep_cur for select * from neweb_repair_repair where id = repid and repair_datetime::DATE > lockdate;
                   loop 
                     fetch rep_cur into rep_rec ;
                     exit when not found ;
                     select coalesce(parent_id,0),coalesce(department_id,0) into myempmanager,mydeptid from hr_employee where id = rep_rec.ae_id ;
                     select coalesce(name,' ') into mycusname from res_partner where id = rep_rec.end_customer ;
                     select resource_id into myresourceid from hr_employee where id = rep_rec.ae_id ;
                     select coalesce(name,' ') into myempname from resource_resource where id = myresourceid ;
                     myrepairname = concat('[',rep_rec.name,']',mycusname,'-',myempname) ; 
                     select count(*) into ncount from neweb_emp_timesheet_repair_calendar where repair_sequence = rep_rec.id ;
                     if ncount = 0 then 
                        if myempmanager != 0 and mydeptid != 0 then 
                            insert into neweb_emp_timesheet_repair_calendar(emp_id,dept_id,cus_id,contract_no,repair_no,
                            repair_datetime,emp_manager,repair_name,repair_sequence,repair_complete) values 
                            (rep_rec.ae_id,mydeptid,rep_rec.end_customer,rep_rec.contract_id,rep_rec.id,rep_rec.repair_datetime,myempmanager,
                              myrepairname,rep_rec.id,rep_rec.state) ;
                        end if;    
                     else 
                        if myempmanager != 0 and mydeptid != 0 then
                            update neweb_emp_timesheet_repair_calendar set emp_id = rep_rec.ae_id,dept_id = mydeptid,cus_id=rep_rec.end_customer,
                              contract_no=rep_rec.contract_id,repair_no=rep_rec.id,repair_datetime=rep_rec.repair_datetime,
                              emp_manager = myempmanager,repair_name = myrepairname,repair_complete=rep_rec.state 
                               where repair_sequence = rep_rec.id ;
                        end if ;      
                     end if ;
                     select count(*) into ncount1 from neweb_emp_timesheet_todo_calendar where emp_id = rep_rec.ae_id and todo_origin='2' 
                        and todo_sequence = rep_rec.id ;
                     if ncount1 = 0 then
                       insert into neweb_emp_timesheet_todo_calendar(emp_id,todo_datetime,dept_id,cus_id,todo_origin,todo_sequence,repair_no,todo_completed)
                        values (rep_rec.ae_id,rep_rec.repair_datetime,mydeptid,rep_rec.end_customer,'2',rep_rec.id,rep_rec.id,'2') ;
                     else
                       if mydeptid != 0 then
                          update neweb_emp_timesheet_todo_calendar set todo_datetime=rep_rec.repair_datetime,dept_id=mydeptid,
                           cus_id=rep_rec.end_customer where emp_id=rep_rec.ae_id and todo_origin='2'  and todo_sequence = rep_rec.id ;
                       end if ;
                     end if ;    
                   end loop ;
                   close rep_cur ;
                 END;$BODY$
                 LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delrepaircalendar(repid int) cascade""")
        self._cr.execute("""drop function if exists delrepaircalendar(repid int,userid int) cascade""")
        self._cr.execute("""create or replace function delrepaircalendar(repid int,userid int) returns void as $BODY$
                 DECLARE 
                   ncount int ;
                   lockdate date ;
                   isadjowner Boolean ;
                 BEGIN 
                    select getadjustowner(userid) into isadjowner ;
                    if isadjowner = False then
                       select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock ;
                    else
                       select (now()::DATE - interval '1 year') into lockdate ;
                    end if ;   
                    delete from neweb_emp_timesheet_repair_calendar where repair_sequence = repid and repair_datetime::DATE > lockdate ;
                    delete from neweb_emp_timesheet_todo_calendar where todo_origin='2' and todo_sequence= repid and todo_datetime::DATE > lockdate ;
                 END;$BODY$
                 LANGUAGE plpgsql;
                 """)

        self._cr.execute("""drop function if exists runallrepcalendar() cascade""")
        self._cr.execute("""create or replace function runallrepcalendar() returns void as $BODY$
                 DECLARE 
                   rep_cur refcursor ;
                   rep_rec record ;
                 BEGIN 
                   open rep_cur for select id from neweb_repair_repair ;
                   loop
                      fetch rep_cur into rep_rec ;
                      exit when not found ;
                      execute updaterepaircalendar(rep_rec.id,1) ;
                   end loop ;
                   close rep_cur ;
                 END;$BODY$
                  LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_plan_ins_calendar(contractid int) cascade""")
        self._cr.execute("""drop function if exists update_plan_ins_calendar(contractid int,userid int) cascade""")
        self._cr.execute("""create or replace function update_plan_ins_calendar(contractid int,userid int) returns void as $BODY$
                DECLARE 
                  con_cur refcursor ;
                  con_rec record ;
                  lockdate date ;
                  mydeptid int ;
                  mycusid int ;
                  mycontractid int ;
                  myempmanager int ;
                  myinspectionname varchar ;
                  mycontractname varchar ;
                  mycusname varchar ;
                  myresourceid int ;
                  myempname varchar ;
                  ncount int ;
                  ncount1 int ;
                  iscomplete CHAR ;
                  myinswarndays int ;
                  myinswarndate DATE ;
                  mynewdate date ;
                  ncount2 int ;
                  isadjowner Boolean;
                BEGIN 
                   select getadjustowner(userid) into isadjowner ;
                   select coalesce(inspection_warn_days,0) into myinswarndays from neweb_contract_contract where id = contractid ;
                   if isadjowner = False then
                      select coalesce(lock_date::DATE,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock ;
                   else
                      select (now()::DATE - interval '1 year') into lockdate ;
                   end if ;   
                   open con_cur for select * from neweb_contract_inspection_list where inspection_id = contractid and
                        subscribe_date is not null and subscribe_date::DATE > lockdate ;
                   loop
                      fetch con_cur into con_rec ;
                      exit when not found ;
                      select holidaychange(con_rec.subscribe_date) into mynewdate ;
                      select coalesce(department_id,0),coalesce(parent_id,0),coalesce(resource_id,0) into mydeptid,myempmanager,myresourceid 
                          from hr_employee where id = con_rec.emp_id ;
                      select coalesce(name,' ') into myempname from resource_resource where id = myresourceid ;
                      select id,coalesce(end_customer,0),coalesce(name,' ') into mycontractid,mycusid,mycontractname 
                           from neweb_contract_contract where id = con_rec.inspection_id ;
                      select coalesce(name,' ') into mycusname from res_partner where id = mycusid ; 
                      select count(*) into ncount from neweb_emp_timesheet_inspection_calendar where inspection_sequence = con_rec.id ;
                      myinspectionname = concat('[',mycontractname,']',mycusname,'-',myempname) ;
                      select con_rec.subscribe_date::DATE -  myinswarndays * interval '1 days' into myinswarndate ;
                      if ncount = 0 then 
                         if mydeptid !=0 and myempmanager !=0 and mycusid !=0 then
                             
                             insert into neweb_emp_timesheet_inspection_calendar (emp_id,dept_id,cus_id,contract_no,inspection_datetime,emp_manager,
                             inspection_name,inspection_sequence,inspection_complete,alert_date1,alert_date2) values (con_rec.emp_id,mydeptid,mycusid,
                             mycontractid,mynewdate,myempmanager,myinspectionname,con_rec.id,'N',myinswarndate,mynewdate) ;
                             
                         end if ;    
                         
                      else 
                         if con_rec.actual_start_datetime is not null and con_rec.actual_end_datetime is not null then 
                            iscomplete = 'Y' ;
                         else 
                            iscomplete = 'N' ;
                         end if ;
                         if mydeptid !=0 and myempmanager !=0 and mycusid !=0 then
                             update neweb_emp_timesheet_inspection_calendar set emp_id=con_rec.emp_id,dept_id=mydeptid,cus_id=mycusid,contract_no=
                             mycontractid,inspection_datetime=mynewdate,emp_manager=myempmanager,inspection_name=myinspectionname,
                             inspection_complete=iscomplete,alert_date1=myinswarndate,alert_date2=mynewdate::DATE  
                             where inspection_sequence = con_rec.id ;
                         end if ;    
                      end if ;
                       select count(*) into ncount2 from neweb_emp_timesheet_todo_calendar where todo_origin='1' and todo_completed='2' and todo_sequence=con_rec.id ;
                       if ncount2 > 0 then
                          delete from neweb_emp_timesheet_todo_calendar where todo_origin='1' and todo_completed='2' and todo_sequence=con_rec.id ;
                       end if ;
                       select count(*) into ncount1 from neweb_emp_timesheet_todo_calendar where emp_id=con_rec.emp_id and todo_origin='1' 
                             and todo_sequence=con_rec.id ; 
                         if ncount1 = 0 then
                            insert into neweb_emp_timesheet_todo_calendar (emp_id,todo_datetime,dept_id,cus_id,todo_origin,todo_sequence,todo_completed,contract_no)
                             values (con_rec.emp_id,mynewdate,mydeptid,mycusid,'1',con_rec.id,'2',mycontractid) ;
                         else
                             if mydeptid !=0 and mycusid !=0 then
                                update neweb_emp_timesheet_todo_calendar set todo_datetime=mynewdate,dept_id=mydeptid,contract_no=mycontractid,
                                  cus_id=mycusid where emp_id=con_rec.emp_id and todo_origin='1'  and todo_sequence=con_rec.id ;
                             end if ;
                         end if ;   
                   end loop ;
                   close con_cur ;     
                END;$BODY$
                LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists del_plan_ins_calendar(inslistid int) cascade""")
        self._cr.execute("""drop function if exists del_plan_ins_calendar(inslistid int,userid int) cascade""")
        self._cr.execute("""create or replace function del_plan_ins_calendar(inslistid int,userid int) returns void as $BODY$
                   DECLARE 
                      lockdate date ;
                      ncount int ;
                      isadjowner Boolean ;
                   BEGIN 
                      select getadjustowner(userid) into isadjowner ;
                      if isadjowner = False then
                         select coalesce(lock_date,now()::DATE - interval '1 year') into lockdate from neweb_emp_timesheet_timesheet_lock ;
                      else
                         select (now()::DATE - interval '1 year') into lockdate ;
                      end if ;   
                      delete from neweb_emp_timesheet_inspection_calendar where inspection_sequence = inslistid and 
                         inspection_datetime::DATE > lockdate ;
                      delete from neweb_emp_timesheet_todo_calendar where todo_sequence = inslistid and todo_origin='1'
                         and todo_datetime::DATE > lockdate ;   
                   END;$BODY$
                   LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runallinscalendar() cascade""")
        self._cr.execute("""create or replace function runallinscalendar() returns void as $BODY$
                  DECLARE 
                     contract_cur refcursor ;
                     contract_rec record ;
                  BEGIN 
                     open contract_cur for select id from neweb_contract_contract ;
                     loop
                       fetch contract_cur into contract_rec ;
                       exit when not found ;
                       execute update_plan_ins_calendar(contract_rec.id,1) ;
                     end loop ;
                     close contract_cur ;
                  END;$BODY$
                  LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_timesheet_set(empid int,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar) cascade""")
        self._cr.execute("""drop function if exists import_timesheet_set(empno varchar,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar) cascade""")
        self._cr.execute("""create or replace function import_timesheet_set(empno varchar,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar) returns void as $BODY$
         DECLARE 
           ncount int ;
           myyearmonth varchar ;
           timesheetid int ;
           mystarttime varchar ;
           myendtime varchar ;
           mystartdatetime TIMESTAMP ;
           myenddatetime TIMESTAMP ;
           mymaxid int ;
           ncount1 int ;
           ncount2 int ;
           mycusname int ;
           myhour float ;
           myminute float ;
           mytime float ;
           myworktypeid int ;
           ncount3 int ;
           empid int ;
           hnum int ;
           mnum int ;
           hnum1 int ;
           mnum1 int ;
         BEGIN 
           select count(*) into ncount3 from hr_employee where employee_num=empno and active = True ; 
           if ncount3 > 0 then
               select id into empid from hr_employee where employee_num=empno and active = True ; 
               select substring(workdate,1,7) into myyearmonth ;
               select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=empid and 
                  timesheet_yearmonth=myyearmonth ;
               if ncount = 0 then 
                  insert into neweb_emp_timesheet_timesheet_calendar (emp_id,timesheet_yearmonth) values (empid,myyearmonth) ;
               end if ; 
               select id into timesheetid from neweb_emp_timesheet_timesheet_calendar where emp_id=empid and 
                  timesheet_yearmonth=myyearmonth ;
              if starttime::numeric::int <> starttime::numeric then
                  select FLOOR(starttime::numeric) into hnum ;
                  select (abs(starttime::numeric - hnum)*60)::INT into mnum ;
                  mystarttime = concat(lpad(hnum::TEXT,2,'0'),':',lpad(mnum::TEXT,2,'0'),':00') ;
               else
                  mystarttime = concat(lpad(starttime::numeric::int::TEXT,2,'0'),':00:00') ; 
               end if ;  
               if endtime::numeric::int <> endtime::numeric then
                  select FLOOR(endtime::numeric) into hnum1 ;
                  select (abs(endtime::numeric - hnum1) * 60)::INT into mnum1 ;
                  myendtime = concat(lpad(hnum1::TEXT,2,'0'),':',lpad(mnum1::TEXT,2,'0'),':00') ;
               else
                  myendtime = concat(lpad(endtime::numeric::int::TEXT,2,'0'),':00:00') ; 
               end if ; 
               /*mystarttime = concat(starttime,':00') ;
               myendtime = concat(endtime,':00') ;  */
               select substring(workdate,1,10) into workdate ;
               select to_timestamp(concat(workdate,' ',mystarttime),'YYYY-MM-DD HH24:MI:SS') into mystartdatetime ;
               select to_timestamp(concat(workdate,' ',myendtime),'YYYY-MM-DD HH24:MI:SS') into myenddatetime ; 
               select mystartdatetime - interval '8 hours' into mystartdatetime ;
               select myenddatetime - interval '8 hours' into myenddatetime ; 
               select abs(date_part('hour',age(myenddatetime,mystartdatetime))) into myhour ;
               select abs(date_part('minute',age(myenddatetime,mystartdatetime))) into myminute ;
               mytime = myhour + (myminute/60) ;  
                select count(*) into ncount1 from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
               if ncount1 > 0 then 
                  select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
               end if ;
               insert into neweb_emp_timesheet_timesheet_calendar_line(line_id,emp_id,timesheet_start_date,timesheet_end_date,
                 timesheet_duration,duration,timesheet_worktype,timesheet_desc) values 
                 (timesheetid,empid,mystartdatetime,myenddatetime,mytime,mytime,myworktypeid,tmemo) ;
               select max(id) into mymaxid from neweb_emp_timesheet_timesheet_calendar_line ;
               execute checkcalendarline(mymaxid) ;
               select count(*) into ncount1 from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
               if ncount1 > 0 then 
                  select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
                  update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=myworktypeid where id = mymaxid ;
               end if ;   
               if substring(worktype,1,1) = '1' and originno is not null then 
                  select count(*) into ncount2 from neweb_project where name like trim(originno) ;
                  if ncount2 > 0 then 
                      select cus_name into mycusname from neweb_project where name like trim(originno) ;
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                          is_complete='ok' where id = mymaxid ;
                  end if ;
               elsif substring(worktype,1,1) = '2' or substring(worktype,1,1) = '3' and originno is not null then 
                  select count(*) into ncount2 from neweb_contract_contract where name like trim(originno) ;
                  if ncount2 > 0 then 
                      select end_customer into mycusname from neweb_contract_contract where name like trim(originno) ;
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                          is_complete='ok' where id = mymaxid ;
                  end if ;
               elsif substring(worktype,1,1) = '4' and originno is not null then
                  select count(*) into ncount2 from neweb_proj_eng_assign where assign_no like trim(originno) ;
                  if ncount2 > 0 then 
                      select proj_cus_name into mycusname from neweb_proj_eng_assign where assign_no like trim(originno) ;
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                          is_complete='ok' where id = mymaxid ;
                  end if ;
               elsif substring(worktype,1,1) = '5' then 
                  update neweb_emp_timesheet_timesheet_calendar_line set is_complete='ok' where id = mymaxid ;
               end if ; 
            end if ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_timesheet_set1(empid int,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar,tdays int) cascade""")
        self._cr.execute("""drop function if exists import_timesheet_set1(empno varchar,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar,tdays int) cascade""")
        self._cr.execute("""create or replace function import_timesheet_set1(empno varchar,workdate varchar,starttime varchar,endtime varchar,worktype varchar,originno varchar,tmemo varchar,tdays int) returns void as $BODY$
         DECLARE 
           ncount int ;
           myyearmonth varchar ;
           timesheetid int ;
           mystarttime varchar ;
           myendtime varchar ;
           mystartdatetime TIMESTAMP ;
           myenddatetime TIMESTAMP ;
           mymaxid int ;
           ncount1 int ;
           ncount2 int ;
           mycusname int ;
           myhour float ;
           myminute float ;
           mytime float ;
           myworktypeid int ;
           mydays int ;
           empid int ;
           ncount3 int ;
           hnum int ;
           mnum int ;
           hnum1 int ;
           mnum1 int ;
         BEGIN 
           select count(*) into ncount3 from hr_employee where employee_num=empno and active = True ;
           if ncount3 > 0 and starttime is not null and endtime is not null then
               select id into empid from hr_employee where employee_num=empno and active = True ;
               select substring(workdate,1,7) into myyearmonth ;
               select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=empid and 
                  timesheet_yearmonth=myyearmonth ;
               if ncount = 0 then 
                  insert into neweb_emp_timesheet_timesheet_calendar (emp_id,timesheet_yearmonth) values (empid,myyearmonth) ;
               end if ; 
               select id into timesheetid from neweb_emp_timesheet_timesheet_calendar where emp_id=empid and 
                  timesheet_yearmonth=myyearmonth ;   
               if starttime::numeric::int <> starttime::numeric then
                  select FLOOR(starttime::numeric) into hnum ;
                  select (abs(starttime::numeric - hnum::numeric) * 60)::INT into mnum ;
                  mystarttime = concat(lpad(hnum::TEXT,2,'0'),':',lpad(mnum::TEXT,2,'0'),':00') ;
               else
                  mystarttime = concat(lpad(starttime::numeric::int::TEXT,2,'0'),':00:00') ; 
               end if ;  
               if endtime::numeric::int <> endtime::numeric then
                  select FLOOR(endtime::numeric) into hnum1 ;
                  select (abs(endtime::numeric - hnum1::numeric) * 60)::INT into mnum1 ;
                  myendtime = concat(lpad(hnum1::TEXT,2,'0'),':',lpad(mnum1::TEXT,2,'0'),':00') ;
               else
                  myendtime = concat(lpad(endtime::numeric::int::TEXT,2,'0'),':00:00') ; 
               end if ; 
               /* mystarttime = concat(starttime,':00') ;
               myendtime = concat(endtime,':00') ;  */
               select substring(workdate,1,10) into workdate ;
               select to_timestamp(concat(workdate,' ',mystarttime),'YYYY-MM-DD HH24:MI:SS') into mystartdatetime ;
               select to_timestamp(concat(workdate,' ',myendtime),'YYYY-MM-DD HH24:MI:SS') into myenddatetime ; 
               select mystartdatetime - interval '8 hours' into mystartdatetime ;
               select myenddatetime - interval '8 hours' into myenddatetime ; 
               select date_part('hour',age(myenddatetime,mystartdatetime)) into myhour ;
               select date_part('minute',age(myenddatetime,mystartdatetime)) into myminute ;
               mytime = myhour + (myminute/60) ;  
                select count(*) into ncount1 from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
               if ncount1 > 0 then 
                  select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype 
                   where worktype_code = worktype ;
               end if ;
               mydays = 1 ;
               loop
                   exit when mydays > tdays ;
                   insert into neweb_emp_timesheet_timesheet_calendar_line(line_id,emp_id,timesheet_start_date,timesheet_end_date,
                     timesheet_duration,duration,timesheet_worktype,timesheet_desc) values 
                     (timesheetid,empid,mystartdatetime,myenddatetime,mytime,mytime,myworktypeid,tmemo) ;
                   select max(id) into mymaxid from neweb_emp_timesheet_timesheet_calendar_line ;
                   execute checkcalendarline(mymaxid) ;
                   select count(*) into ncount1 from neweb_emp_timesheet_timesheet_worktype 
                       where worktype_code = worktype ;
                   if ncount1 > 0 then 
                      select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype 
                       where worktype_code = worktype ;
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=myworktypeid where id = mymaxid ;
                   end if ;   
                   if substring(worktype,1,1) = '1' and originno is not null then 
                      select count(*) into ncount2 from neweb_project where name like trim(originno) ;
                      if ncount2 > 0 then 
                          select cus_name into mycusname from neweb_project where name like trim(originno) ;
                          update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                              is_complete='ok' where id = mymaxid ;
                      end if ;
                   elsif substring(worktype,1,1) = '2' or substring(worktype,1,1) = '3' and originno is not null then 
                      select count(*) into ncount2 from neweb_contract_contract where name like trim(originno) ;
                      if ncount2 > 0 then 
                          select end_customer into mycusname from neweb_contract_contract where name like trim(originno) ;
                          update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                              is_complete='ok' where id = mymaxid ;
                      end if ;
                   elsif substring(worktype,1,1) = '4' and originno is not null then
                      select count(*) into ncount2 from neweb_proj_eng_assign where assign_no like trim(originno) ;
                      if ncount2 > 0 then 
                          select proj_cus_name into mycusname from neweb_proj_eng_assign where assign_no like trim(originno) ;
                          update neweb_emp_timesheet_timesheet_calendar_line set timesheet_origin=originno,timesheet_custom=mycusname, 
                              is_complete='ok' where id = mymaxid ;
                      end if ;
                   elsif substring(worktype,1,1) = '5' then 
                      update neweb_emp_timesheet_timesheet_calendar_line set is_complete='ok' where id = mymaxid ;
                   end if ; 
                   select mystartdatetime + interval '1 days' into mystartdatetime ;
                   select myenddatetime + interval '1 days' into myenddatetime ;
                   mydays = mydays + 1 ;
                end loop ;   
              end if ;  
         END;$BODY$
         LANGUAGE plpgsql;""")



        self._cr.execute("""drop function if exists sorttimesheetitem(timesheetid int) cascade""")
        self._cr.execute("""create or replace function sorttimesheetitem(timesheetid int) returns void as $BODY$
         DECLARE 
           line_cur refcursor ;
           line_rec record ;
           nnum int ;
         BEGIN 
           nnum = 1 ;
           open line_cur for select id,timesheet_start_date from neweb_emp_timesheet_timesheet_calendar_line where
                 line_id=timesheetid order by timesheet_start_date ;
           loop
             fetch line_cur into line_rec ;
             exit when not found ;
             update neweb_emp_timesheet_timesheet_calendar_line set nitem=nnum where id = line_rec.id ;
             nnum = nnum + 1 ;
           end loop ;  
           close line_cur ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists sorttimesheetitem1(empid int,yearmonth varchar) cascade""")
        self._cr.execute("""create or replace function sorttimesheetitem1(empid int,yearmonth varchar) returns void as $BODY$
         DECLARE 
           line_cur refcursor ;
           line_rec record ;
           nnum int ;
           timesheetid int ;
           ncount int ;
         BEGIN 
           select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=empid 
              and timesheet_yearmonth = yearmonth ;
           if ncount > 0 then  
               select id into timesheetid from neweb_emp_timesheet_timesheet_calendar where emp_id=empid 
                    and timesheet_yearmonth = yearmonth ;
               nnum = 1 ;
               open line_cur for select id,timesheet_start_date from neweb_emp_timesheet_timesheet_calendar_line where
                     line_id=timesheetid order by timesheet_start_date ;
               loop
                 fetch line_cur into line_rec ;
                 exit when not found ;
                 update neweb_emp_timesheet_timesheet_calendar_line set nitem=nnum where id = line_rec.id ;
                 nnum = nnum + 1 ;
               end loop ;
               close line_cur ; 
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists sorttimesheetitem2() cascade""")
        self._cr.execute("""create or replace function sorttimesheetitem2() returns void as $BODY$
         DECLARE 
           line_cur refcursor ;
           line_rec record ;
           nnum int ;
           timesheetid int ;
           ncount int ;
         BEGIN 
           select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=empid 
              and timesheet_yearmonth = yearmonth ;
           if ncount > 0 then  
               select id into timesheetid from neweb_emp_timesheet_timesheet_calendar where emp_id=empid 
                    and timesheet_yearmonth = yearmonth ;
               nnum = 1 ;
               open line_cur for select id,timesheet_start_date from neweb_emp_timesheet_timesheet_calendar_line where
                     line_id=timesheetid order by timesheet_start_date ;
               loop
                 fetch line_cur into line_rec ;
                 exit when not found ;
                 update neweb_emp_timesheet_timesheet_calendar_line set nitem=nnum where id = line_rec.id ;
                 nnum = nnum + 1 ;
               end loop ;
               close line_cur ; 
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkcalendarline(lineid int) cascade""")
        self._cr.execute("""create or replace function checkcalendarline(lineid int) returns void as $BODY$
         DECLARE 
              myhour float ;
              myminute float ;
              mytime float ;
              mystartdatetime timestamp ;
              myenddatetime timestamp ;
              mytimesheetworktype int ;
              mytimesheetorigin varchar ;
              myworktypelink char ;
              ncount int ;
              ncount1 int ;
              ncount2 int ;
              ncount3 int ;
              myworktypecode varchar ;
         BEGIN 
              select timesheet_start_date + interval '8 hours',timesheet_end_date + interval '8 hours',timesheet_worktype,timesheet_origin into 
               mystartdatetime,myenddatetime,mytimesheetworktype,mytimesheetorigin from 
                  neweb_emp_timesheet_timesheet_calendar_line where id = lineid ; 
              select abs(date_part('hour',age(myenddatetime,mystartdatetime))) into myhour ;
              select abs(date_part('minute',age(myenddatetime,mystartdatetime))) into myminute ;
              mytime = myhour + (myminute/60) ; 
              if trim(myworktypelink) = '1' or trim(myworktypelink) = '2' or trim(myworktypelink) = '3' then
                  select worktype_link,worktype_code into myworktypelink,myworktypecode from neweb_emp_timesheet_timesheet_worktype where 
                    id = mytimesheetworktype ;  
                  select count(*) into ncount from neweb_repair_repair where name like trim(mytimesheetorigin) and 
                          mytimesheetorigin is not null ;  
                  select count(*) into ncount1 from neweb_project where name like trim(mytimesheetorigin) and
                             mytimesheetorigin is not null  ;  
                  select count(*) into ncount2 from neweb_contract_contract where name like trim(mytimesheetorigin) and 
                          mytimesheetorigin is not null ;   
                  select count(*) into ncount3 from neweb_proj_eng_assign where assign_no like trim(mytimesheetorigin)  and 
                          mytimesheetorigin is not null ;    
                  if ncount > 0 or ncount1 > 0 or ncount2 > 0 or ncount3 > 0 or trim(myworktypelink)='4' then
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,
                        duration=mytime,is_complete='ok'  where id = lineid ;
                  else
                      update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,
                        duration=mytime,is_complete='ng'  where id = lineid ;
                  end if ;            
              else
                  update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,
                        duration=mytime,is_complete='ok'  where id = lineid ;
              end if ;             
              
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_timesheet_origin(originno varchar) cascade""")
        self._cr.execute("""create or replace function get_timesheet_origin(originno varchar) returns int as $BODY$
        DECLARE 
           ncount int ;
           myres int ;
        BEGIN 
           myres = 0 ;
           select count(*) into ncount from neweb_project where name like trim(originno) ;
           if ncount > 0 then 
              select cus_name into myres from neweb_project where name like trim(originno) ;
           end if ;
           select count(*) into ncount from neweb_contract_contract where name like trim(originno) ;
           if ncount > 0 then
              select end_customer into myres from neweb_contract_contract where name like trim(originno) ;
           end if ;
           select count(*) into ncount from neweb_proj_eng_assign where assign_no like trim(originno) ;
           if ncount > 0 then
              select proj_cus_name into myres from neweb_proj_eng_assign where assign_no like trim(originno) ;
           end if ;
           return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists run_inspection_alert_mail1() cascade""")
        self._cr.execute("""create or replace function run_inspection_alert_mail1() returns void as $BODY$
        DECLARE 
           ins_cur refcursor ;
           ins_rec record ;
        BEGIN 
           delete from neweb_emp_timesheet_inspection_alert_mail ;
           open ins_cur for select * from neweb_emp_timesheet_inspection_calendar where 
              alert_date1::DATE <= now()::DATE and inspection_alert1 = False and inspection_complete = 'N';
           loop
              fetch ins_cur into ins_rec ;
              exit when not found ;
              insert into neweb_emp_timesheet_inspection_alert_mail(emp_id,dept_id,cus_id,contract_no,
              inspection_datetime,inspection_complete,inspection_alert1,inspection_alert2,alert_date1,
              alert_date2,emp_manager,inspection_name,inspection_sequence) values (ins_rec.emp_id,ins_dept_id,
              ins_rec.cus_id,ins_rec.contract_no,ins_rec.inspection_datetime,ins_rec.inspection_complete,
              ins_rec.inspection_alert1,ins_rec.inspection_alert2,ins_rec.alert_date1,ins_rec.alert_date2,
              ins_rec.emp_manager,ins_rec.inspection_name,ins_rec.id);
           end loop ;   
           close ins_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists run_inspection_alert_mail2() cascade""")
        self._cr.execute("""create or replace function run_inspection_alert_mail2() returns void as $BODY$
        DECLARE 
           ins_cur refcursor ;
           ins_rec record ;
        BEGIN 
           delete from neweb_emp_timesheet_inspection_alert_mail ;
           open ins_cur for select * from neweb_emp_timesheet_inspection_calendar where 
              alert_date2::DATE <= now()::DATE and inspection_alert2 = False and inspection_complete = 'N';
           loop
              fetch ins_cur into ins_rec ;
              exit when not found ;
              insert into neweb_emp_timesheet_inspection_alert_mail(emp_id,dept_id,cus_id,contract_no,
              inspection_datetime,inspection_complete,inspection_alert1,inspection_alert2,alert_date1,
              alert_date2,emp_manager,inspection_name,inspection_sequence) values (ins_rec.emp_id,ins_dept_id,
              ins_rec.cus_id,ins_rec.contract_no,ins_rec.inspection_datetime,ins_rec.inspection_complete,
              ins_rec.inspection_alert1,ins_rec.inspection_alert2,ins_rec.alert_date1,ins_rec.alert_date2,
              ins_rec.emp_manager,ins_rec.inspection_name,ins_rec.id);
           end loop ;   
           close ins_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getworktype(worktypeid int) cascade""")
        self._cr.execute("""create or replace function getworktype(worktypeid int) returns varchar as $BODY$
        DECLARE 
           ncount int ;
           myres varchar;
        BEGIN 
           myres = ' ' ;
           select coalesce(worktype_code,' ') into myres from neweb_emp_timesheet_timesheet_worktype where id = worktypeid ; 
           return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checklinetimeerror(lineid int) cascade""")
        self._cr.execute("""create or replace function checklinetimeerror(lineid int) returns Boolean as $BODY$
        DECLARE 
           myyearmonth varchar ;
           mystartym varchar ;
           myendym varchar ;
           myid int ;
           mysyear FLOAT ;
           myeyear FLOAT ;
           mysmonth FLOAT ;
           myemonth FLOAT ;
           myres Boolean ; 
           mystartdate date ;
           myenddate date ;
        BEGIN 
           select line_id into myid from neweb_emp_timesheet_timesheet_calendar_line where id = lineid ;
           select timesheet_yearmonth into myyearmonth from neweb_emp_timesheet_timesheet_calendar where id = myid ;
           select date_part('year',(timesheet_start_date + interval '8 hours')::DATE),
                  date_part('year',(timesheet_end_date + interval '8 hours')::DATE),
                  date_part('month',(timesheet_start_date + interval '8 hours')::DATE),
                  date_part('month',(timesheet_end_date + interval '8 hours')::DATE) into 
                  mysyear,myeyear,mysmonth,myemonth from neweb_emp_timesheet_timesheet_calendar_line where id = lineid ;
           mystartym = concat(mysyear::TEXT,'-',mysmonth::TEXT) ;
           myendym = concat(myeyear::TEXT,'-',myemonth::TEXT) ;
           select (timesheet_start_date + interval '8 hours')::DATE,(timesheet_end_date + interval '8 hours')::DATE
             into mystartdate,myenddate from neweb_emp_timesheet_timesheet_calendar_line where id = lineid ;
           if  mystartdate != myenddate then 
              myres := TRUE ;
           else
              myres := FALSE ;
           end if ;
           return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkinspectiondate1(inscalendarid int) cascade""")
        self._cr.execute("""create or replace function checkinspectiondate1(inscalendarid int) returns char as $BODY$
            DECLARE 
              ncount int ;
              myres char ;
              startdate TIMESTAMP ;
              enddate TIMESTAMP ;
            BEGIN 
              select (inspection_start_datetime + interval '8 hours'),(inspection_end_datetime + interval '8 hours') into
              startdate,enddate from neweb_emp_timesheet_inspection_calendar where id = inscalendarid ;
              if startdate is null or enddate is null then 
                 myres = '1' ;
              elsif startdate::DATE != enddate::DATE then     
                 myres = '2' ;
              elsif startdate = enddate then 
                 myres = '3' ;  
              end if ;  
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_inscalendar_datetime(calendarid int) cascade""")
        self._cr.execute("""drop function if exists update_inscalendar_datetime(calendarid int,userid int) cascade""")
        self._cr.execute("""create or replace function update_inscalendar_datetime(calendarid int,userid int) returns void
       as $BODY$ 
          DECLARE 
            mystartdate timestamp ;
            myenddate timestamp ;
            ncount int ;
            myinspectionid int ;
            mycontractid int ;
            mymemo varchar ;
          BEGIN
            select count(*) into ncount from neweb_emp_timesheet_inspection_calendar
              where inspection_start_datetime is not null and inspection_end_datetime is not null 
                and id = calendarid ;
              if ncount > 0 then  
                select inspection_start_datetime,inspection_end_datetime,inspection_memo into 
                 mystartdate,myenddate,mymemo from neweb_emp_timesheet_inspection_calendar where id = calendarid ;
                select date_trunc('minute',mystartdate::TIMESTAMP) into mystartdate ;
                select date_trunc('minute',myenddate::TIMESTAMP) into myenddate ;
                update neweb_emp_timesheet_inspection_calendar set inspection_start_datetime=mystartdate,
                   inspection_end_datetime=myenddate where id = calendarid ;   
                select inspection_sequence into myinspectionid from neweb_emp_timesheet_inspection_calendar 
                   where id = calendarid ;  
                update neweb_contract_inspection_list set  actual_start_datetime=mystartdate,
                  actual_end_datetime=myenddate,inspection_memo=mymemo where id = myinspectionid ;   
                select inspection_id into mycontractid from neweb_contract_inspection_list where id = myinspectionid ;
                execute update_inspection_timesheet(mycontractid,userid) ;
              end if ;       
          END;$BODY$
          LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists getempidbyuserid(userid int) cascade""")
        self._cr.execute("""create or replace function getempidbyuserid(userid int) returns int as $BODY$
       DECLARE 
          myresourceid int ;
          myres int ;
          ncount int ;
       BEGIN 
          select count(*) into ncount from resource_resource where user_id=userid ;
          if ncount > 0 then 
             select id into myresourceid from resource_resource where user_id=userid ;
             select id into myres from hr_employee where resource_id=myresourceid ;
          else 
             myres = 0 ;
          end if ;
          return myres ;
       END;$BODY$
       LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmaxthcalym(empid int) cascade""")
        self._cr.execute("""create or replace function getmaxthcalym(empid int) returns varchar as $BODY$
           DECLARE
              ncount int ;
              myres varchar ;
              mymaxid int ;
           BEGIN
              select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar where emp_id=empid ;
              if ncount > 0 then
                  select max(id) into mymaxid from neweb_emp_timesheet_timesheet_calendar where emp_id=empid ;
                  select coalesce(timesheet_yearmonth,' ') into myres from neweb_emp_timesheet_timesheet_calendar
                     where id = mymaxid ;
              else
                  myres = ' ' ;
              end if ;       
              return myres ;   
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_assigntodo(assignid int) cascade""")
        self._cr.execute("""create or replace function gen_assigntodo(assignid int) returns void as $BODY$
           DECLARE
             ncount int ;
             assign_cur refcursor ;
             assign_rec record ;
             resourceid int ;
             empid int ;
             deptid int ;
             cusid int ;
             setupdate date ;
             maxid int ;
             assigncus varchar ;
             projno int ;
             todoorigin char ;
           BEGIN
             open assign_cur for select * from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id=assignid ;
             loop
                fetch assign_cur into assign_rec;
                exit when not found ;
                select id into resourceid from resource_resource where user_id=assign_rec.res_users_id ;
                select id,department_id into empid,deptid from hr_employee where resource_id=resourceid ;
                select proj_cus_name,setup_date,setup_address,proj_no into cusid,setupdate,assigncus,projno from neweb_proj_eng_assign where id = assignid ;
                if projno is null then
                   todoorigin := '3' ;
                else
                   todoorigin := '4' ;
                end if ;
                if empid is not null then
                   select count(*) into ncount from neweb_emp_timesheet_todo_calendar where todo_sequence=assignid and todo_origin=todoorigin 
                      and emp_id= empid ;
                   if ncount = 0 then
                      insert into neweb_emp_timesheet_todo_calendar(emp_id,dept_id,todo_origin,todo_sequence,assign_no,todo_completed)
                        values (empid,deptid,todoorigin,assignid,assignid,'2') ;
                      if setupdate is not null then
                         select max(id) into maxid from neweb_emp_timesheet_todo_calendar ;
                         update neweb_emp_timesheet_todo_calendar set todo_datetime=setupdate where id=maxid ;
                      end if ;  
                      if cusid is not null then 
                         select max(id) into maxid from neweb_emp_timesheet_todo_calendar ;
                         update neweb_emp_timesheet_todo_calendar set cus_id=cusid where id=maxid ;
                      else 
                         select max(id) into maxid from neweb_emp_timesheet_todo_calendar ;
                         update neweb_emp_timesheet_todo_calendar set assign_cus=assigncus where id=maxid ;
                      end if ;
                   else
                      update neweb_emp_timesheet_todo_calendar set emp_id=empid,dept_id=deptid where todo_sequence=assignid 
                        and todo_origin=todoorigin  and emp_id= empid ;
                      if setupdate is not null then
                         update neweb_emp_timesheet_todo_calendar set todo_datetime=setupdate where todo_sequence=assignid 
                        and todo_origin=todoorigin  and emp_id= empid ;
                      end if ;  
                      if cusid is not null then 
                         update neweb_emp_timesheet_todo_calendar set cus_id=cusid where todo_sequence=assignid 
                        and todo_origin=todoorigin  and emp_id= empid ;
                      else 
                         update neweb_emp_timesheet_todo_calendar set assign_cus=assigncus where todo_sequence=assignid 
                        and todo_origin=todoorigin  and emp_id= empid ;
                      end if ;
                   end if ;
                end if ;
             end loop ;
             close assign_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists del_assigntodo(assignid int) cascade""")
        self._cr.execute("""create or replace function del_assigntodo(assignid int) returns void as $BODY$
           DECLARE
             assign_cur refcursor ;
             assign_rec record ;
             resourceid int ;
             empid int ;
             projno int ;
             todoorigin char ;
           BEGIN
             open assign_cur for select * from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id=assignid ;
             loop
                fetch assign_cur into assign_rec ;
                exit when not found ;
                select proj_no into projno from neweb_proj_eng_assign where id = assignid ;
                if projno is null then
                   todoorigin := '3' ;
                else
                   todoorigin := '4' ;
                end if ;
                select id into resourceid from resource_resource where user_id=assign_rec.res_users_id ;
                select id into empid from hr_employee where resource_id=resourceid ;
                if empid is not null then
                   delete from neweb_emp_timesheet_todo_calendar where todo_sequence=assignid and todo_origin=todoorigin 
                   and emp_id= empid ;
                end if ;   
             end loop ;
             close assign_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_todocalendar(todoid int) cascade""")
        self._cr.execute("""drop function if exists update_todocalendar(todoid int,userid int) cascade""")
        self._cr.execute("""create or replace function update_todocalendar(todoid int,userid int) returns void as $BODY$
           DECLARE
             myinsid int ;
             mytodoorigin char ;
             mysdatetime timestamp ;
             myedatetime timestamp ;
             mytodoseq int ;
             myempid int ;
             mycontractid int ;
             mymemo varchar ;
             todocompleted char ;
           BEGIN
             select todo_origin,ins_start_datetime,ins_end_datetime,todo_sequence,emp_id,ins_memo,todo_completed 
                into mytodoorigin,mysdatetime,myedatetime,mytodoseq,myempid,mymemo,todocompleted 
               from neweb_emp_timesheet_todo_calendar where id = todoid ;
             if mytodoorigin = '1' and mysdatetime is not null and myedatetime is not null and mytodoseq is not null then
                update neweb_contract_inspection_list set actual_start_datetime=mysdatetime,actual_end_datetime=myedatetime,inspection_memo=mymemo,emp_id=myempid
                  where id = mytodoseq ;
                select inspection_id into mycontractid from neweb_contract_inspection_list where id = mytodoseq ;
                execute update_inspection_timesheet(mycontractid,userid) ;
             end if ;
             if todocompleted = '1' then 
                update neweb_emp_timesheet_inspection_calendar set inspection_complete ='Y',inspection_start_datetime=
                   mysdatetime,inspection_end_datetime=myedatetime,inspection_memo=mymemo
                   where inspection_sequence = mytodoseq ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checktodoinsdate(todoid int) cascade""")
        self._cr.execute("""create or replace function checktodoinsdate(todoid int) returns char as $BODY$
             DECLARE 
               ncount int ;
               myres char ;
               startdate TIMESTAMP ;
               enddate TIMESTAMP ;
               todoorg char ;
             BEGIN 
               select todo_origin into todoorg from neweb_emp_timesheet_todo_calendar where id = todoid ;
               if todoorg = '1' then
                   select (ins_start_datetime + interval '8 hours'),(ins_end_datetime + interval '8 hours') into
                   startdate,enddate from neweb_emp_timesheet_todo_calendar  where id = todoid ;
                   if startdate is null or enddate is null then 
                      myres = '1' ;
                   elsif startdate::DATE != enddate::DATE then     
                      myres = '2' ;
                   elsif startdate = enddate then 
                      myres = '3' ;  
                   end if ;  
               else 
                   myres = '0' ;
               end if ;   
               return myres ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists holidaychange(mydate timestamp) cascade""")
        self._cr.execute("""create or replace function holidaychange(mydate timestamp) returns timestamp as $BODY$
             DECLARE
               mycdate varchar ;
               myweek int ;
               myres timestamp ;
             BEGIN 
               select to_char(mydate,'YYYY-MM-DD HH24:MI:SS') into mycdate ;
               select extract(DOW FROM mycdate::timestamp ) into myweek ;
               if myweek = 0 then 
                  select mydate - interval '2 days' into myres ;
               elsif myweek = 6 then 
                  select mydate - interval '1 days' into myres ;
               else 
                  select mydate into myres ;
               end if ;
               return myres ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_holiday_line(holidayid int) cascade""")
        self._cr.execute("""create or replace function gen_holiday_line(holidayid int) returns void as $BODY$
             DECLARE 
               mycstartdate varchar;
               mycenddate varchar ;
               myyear varchar ;
               mydate date ;
               mystartdate date ;
               myenddate date ;
               myweek int ;
               mycdate varchar ;
               myitem int ;
             BEGIN 
               select hr_holiday_year into myyear from neweb_emp_timesheet_hrholiday where id = holidayid ;
               mycstartdate = concat(myyear,'-01-01') ;
               mycenddate = concat(myyear,'-12-31') ;
               select to_date(mycstartdate,'YYYY-MM-DD') into mystartdate ;
               select to_date(mycenddate,'YYYY-MM-DD') into myenddate ;
               mydate = mystartdate ;
               myitem = 1 ;
               loop
                 exit when mydate > myenddate ;
                 if myitem = 1 then 
                     insert into neweb_emp_timesheet_hrholiday_line(nitem,holiday_id,holiday_date,holiday_memo) values 
                     (myitem,holidayid,mydate,'元旦') ;
                     myitem = myitem + 1 ;
                 end if ;
                 select extract(DOW FROM mycdate::DATE) into myweek ;
                 if myweek = 6 then 
                    insert into neweb_emp_timesheet_hrholiday_line(nitem,holiday_id,holiday_date,holiday_memo) values 
                     (myitem,holidayid,mydate,'週六') ;
                     myitem = myitem + 1 ;
                 elsif myweek = 0 then 
                    insert into neweb_emp_timesheet_hrholiday_line(nitem,holiday_id,holiday_date,holiday_memo) values 
                     (myitem,holidayid,mydate,'週日') ;
                     myitem = myitem + 1 ;
                 end if ;
                 select mydate + interval '1 days' into mydate ;
                 select to_char(mydate,'YYYY-MM-DD') into mycdate ;
                 
               end loop ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists regenholidayitem(holidayid int) cascade""")
        self._cr.execute("""create or replace function regenholidayitem(holidayid int) returns void as $BODY$
             DECLARE
               ho_cur refcursor ;
               ho_rec record ; 
               myitem int ;
             BEGIN
             myitem = 1 ;
               open ho_cur for select * from neweb_emp_timesheet_hrholiday_line 
                    where holiday_id = holidayid order by holiday_date ;
               loop
                  fetch ho_cur into ho_rec ;
                  exit when not found ;
                  update neweb_emp_timesheet_hrholiday_line set nitem=myitem where id = ho_rec.id ;
                  myitem = myitem + 1 ;
               end loop ;
               close ho_cur ; 
             END;$BODY$
             LANGUAGE plpgsql;
        """)


        self._cr.execute("""drop function if exists genhototimesheet(hoyearid int) cascade""")
        self._cr.execute("""create or replace function genhototimesheet(hoyearid int) returns void as $BODY$
             DECLARE 
               ho_cur refcursor ;
               ho_rec record ;
               mycdate varchar ;
               myscdate varchar ;
               myecdate varchar ;
               mystartdate timestamp ;
               myenddate timestamp ;
               ncount int ;
               myyear varchar ;
               mymaxid int ;
               worktypeid int ;
             BEGIN 
               select id into worktypeid from neweb_emp_timesheet_timesheet_worktype where worktype_code='51' ;
              
               myscdate = concat(myyear,'-01-01') ;
               myecdate = concat(myyear,'-12-31') ;
               select to_date(myscdate,'YYYY-MM-DD') into mystartdate ;
               select to_date(myecdate,'YYYY-MM-DD') into myenddate ;
               delete from neweb_emp_timesheet_timesheet_calendar_line where emp_id is null 
                 and timesheet_origin = 'holiday_tags' and timesheet_start_date::DATE between mystartdate and myenddate ;
               open ho_cur for select * from neweb_emp_timesheet_hrholiday_line where holiday_id=hoyearid ;
               loop 
                  fetch ho_cur into ho_rec ;
                  exit when not found ;
                  select to_char(ho_rec.holiday_date::DATE,'YYYY-MM-DD') into mycdate ;
                  myscdate = concat(mycdate,' 08:30:00') ;
                  myecdate = concat(mycdate,' 17:30:00') ;
                  select to_date(myscdate,'YYYY-MM-DD HH24:MI:SS') into mystartdate ;
                  select to_date(myecdate,'YYYY-MM-DD HH24:MI:SS') into myenddate ;
                  select mystartdate + interval '30 minute' into mystartdate ;
                  select myenddate + interval '9 hours' + interval '30 minute' into myenddate ;
                  
                  insert into neweb_emp_timesheet_timesheet_calendar_line(timesheet_start_date,timesheet_end_date,
                  timesheet_worktype,timesheet_origin,timesheet_desc) values (mystartdate,myenddate,worktypeid,'holiday_tags',ho_rec.holiday_memo) ;
               end loop ;
               close ho_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delhototimesheet(hoyearid int) cascade""")
        self._cr.execute("""create or replace function delhototimesheet(hoyearid int) returns void as $BODY$
             DECLARE 
                mycdate varchar ;
                myscdate varchar ;
                myecdate varchar ;
                mystartdate timestamp ;
                myenddate timestamp ;
                myyear varchar ;
             BEGIN 
                select hr_holiday_year into myyear from neweb_emp_timesheet_hrholiday where id = hoyearid ;
               myscdate = concat(myyear,'-01-01') ;
               myecdate = concat(myyear,'-12-31') ;
               select to_date(myscdate,'YYYY-MM-DD') into mystartdate ;
               select to_date(myecdate,'YYYY-MM-DD') into myenddate ;
               delete from neweb_emp_timesheet_timesheet_calendar_line where emp_id is null 
                 and timesheet_origin = 'holiday_tags' and timesheet_start_date::DATE between mystartdate 
                 and myenddate ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delholinetotimesheet(holineid int) cascade""")
        self._cr.execute("""create or replace function delholinetotimesheet(holineid int) returns void as $BODY$
             DECLARE 
                ncount int ;
                myhodate date ;
             BEGIN 
                select holiday_date::DATE into myhodate from neweb_emp_timesheet_hrholiday_line where id = holineid ;
                delete from neweb_emp_timesheet_timesheet_calendar_line where emp_id is null 
                and timesheet_start_date::DATE = myhodate ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists inspection_ch_todo(insid int) cascade""")
        self._cr.execute("""create or replace function inspection_ch_todo(insid int) returns void as $BODY$
             DECLARE 
               seqid int ;
               myempid int ;
               myinsdt timestamp ;
               ncount int ;
             BEGIN 
               select inspection_sequence,inspection_datetime,emp_id into 
                 seqid,myinsdt,myempid  from neweb_emp_timesheet_inspection_calendar where id = insid ;
               select count(*) into ncount from neweb_emp_timesheet_todo_calendar 
                     where todo_origin = '1' and todo_sequence = seqid ;
               if ncount > 0 then 
                  update neweb_emp_timesheet_todo_calendar  set emp_id=myempid,todo_datetime=myinsdt 
                     where todo_origin = '1' and todo_sequence = seqid ;
               end if ;     
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists resettodocontractno() cascade;""")
        self._cr.execute("""create or replace function resettodocontractno() returns void as $BODY$
             DECLARE
               todo_cur refcursor ;
               todo_rec record ;
               mycontractid int ;
             BEGIN
               open todo_cur for select * from neweb_emp_timesheet_todo_calendar where todo_origin='1' ;
               loop
                  fetch todo_cur into todo_rec ;
                  exit when not found ;
                  select inspection_id into mycontractid from neweb_contract_inspection_list where id = 
                    todo_rec.todo_sequence ;
                  update neweb_emp_timesheet_todo_calendar set contract_no=mycontractid where id = todo_rec.id ;  
               end loop ;
               close todo_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists resetinspectiontimesheet() cascade;""")
        self._cr.execute("""create or replace function resetinspectiontimesheet() returns void as $BODY$
             DECLARE
               ncount int ;
             BEGIN
               update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=11 where origin_type='1' ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists timesheet_ymcheck() cascade""")
        self._cr.execute("""create or replace function timesheet_ymcheck() returns void as $BODY$
            DECLARE
              time_cur refcursor ;
              time_rec record ;
              s1  varchar ;
              s2  varchar ;
              s3 varchar ;
            BEGIN
              open time_cur for select * from neweb_emp_timesheet_timesheet_calendar ;
              loop
                fetch time_cur into time_rec ;
                exit when not found ;
                if length(time_rec.timesheet_yearmonth)=6 then
                   s1 = substring(time_rec.timesheet_yearmonth,1,5) ;
                   s2 = substring(time_rec.timesheet_yearmonth,6,1) ;
                   s3 = concat(s1,'0',s2) ;
                   update neweb_emp_timesheet_timesheet_calendar set timesheet_yearmonth=s3 where id = time_rec.id ;
                end if ;
              end loop ;
              close time_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists worktype_categ_check() cascade;""")
        self._cr.execute("""create or replace function worktype_categ_check() returns void as $BODY$
            BEGIN
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='專案工時' where substring(worktype_code,1,1)='1' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='維護工時' where substring(worktype_code,1,1)='2' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='維運工時' where substring(worktype_code,1,1)='3' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='支援工時' where substring(worktype_code,1,1)='4' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='一般工時' where substring(worktype_code,1,1)='5' ;
            END;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists get_timesheetl_cus(timesheet_line_id int) cascade;""")
        self._cr.execute("""create or replace function get_timesheetl_cus(timesheet_line_id int) returns varchar as $BODY$
            DECLARE
              ncount int ;
              myres varchar ;
              cusid int ;
            BEGIN
              select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar_line where id = timesheet_line_id and timesheet_custom is not null ;
              if ncount = 0 then
                 myres := ' ' ;
              else
                 select timesheet_custom into cusid from neweb_emp_timesheet_timesheet_calendar_line where id = timesheet_line_id ;
                 select name into myres from res_partner where id = cusid ;
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gettimesheet_sale(lineid int) cascade""")
        self._cr.execute("""create or replace function gettimesheet_sale(lineid int) returns varchar as $BODY$
            DECLARE
              ncount int ;
              ncount1 int ;
              saleid int ;
              myres varchar ;
              resourceid int ;
            BEGIN
              select count(*) into ncount from neweb_emp_timesheet_timesheet_calendar_line where id = lineid and sale_id is not null ;
              if ncount = 0 then
                 myres = 'No Setting' ;
              else
                 select sale_id into saleid from neweb_emp_timesheet_timesheet_calendar_line where id = lineid ;
                 select resource_id into resourceid from hr_employee where id = saleid ;
                 select name into myres from resource_resource where id = resourceid ;
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_emp_expense(myempid int) cascade""")
        self._cr.execute("""create or replace function get_emp_expense(myempid int) returns Float as $BODY$
            DECLARE
              myres Float ;
            BEGIN
              select coalesce(timesheet_expense,0) into myres from hr_employee where id = myempid ;
              if myres is null then
                 myres = 0 ;
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_emp_cost(myempid int) cascade""")
        self._cr.execute("""create or replace function get_emp_cost(myempid int) returns Float as $BODY$
            DECLARE
              myres Float ;
            BEGIN
              select coalesce(timesheet_cost,0) into myres from hr_employee where id = myempid ;
              if myres is null then
                 myres = 0 ;
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists recheckcalendar() cascade""")
        self._cr.execute("""create or replace function recheckcalendar() returns void as $BODY$
            DECLARE
              cal_cur refcursor ;
              cal_rec record ;
            BEGIN
              open cal_cur for select id,is_complete from neweb_emp_timesheet_timesheet_calendar_line where is_complete='ng' or is_complete is null ;
              loop
                 fetch cal_cur into cal_rec;
                 exit when not found ;
                 execute checkcalendarline(cal_rec.id) ;
              end loop ;
              close cal_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")




        self._cr.execute("""drop function if exists get_emp_hours(empid int,mydate date) cascade""")
        self._cr.execute("""create or replace function get_emp_hours(empid int,mydate date) returns Float as $BODY$
            DECLARE
               myres Float ;
            BEGIN
               select abs(coalesce(sum(duration),0)) into myres from neweb_emp_timesheet_timesheet_calendar_line where emp_id=empid and (timesheet_start_date + interval '8 hours')::DATE = mydate ;
               if myres is null then
                  myres := 0 ;
               end if ;
               myres = myres * 60 ;
               return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_mintimesheet() cascade""")
        self._cr.execute("""create or replace function get_mintimesheet() returns Float as $BODY$
            DECLARE
               myres Float ;
               mytolerance Float ;
            BEGIN
               select coalesce(tolerance_time,0) into mytolerance from neweb_emp_timesheet_tolerance_setting ;
               if mytolerance is null then
                  mytolerance := 0 ;
               end if ;
               myres := 480 - mytolerance ;
               return myres ;
             END;$BODY$
            LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists get_tolerance_num(empid int,mydate date) cascade""")
        self._cr.execute("""create or replace function get_tolerance_num(empid int,mydate date) returns INT as $BODY$
            DECLARE
               myres int ;
               myhours Float ;
               mytolerance Float ;
               minhours Float ;
            BEGIN
                select abs(coalesce(sum(duration),0)) into myhours from neweb_emp_timesheet_timesheet_calendar_line where emp_id=empid and (timesheet_start_date + interval '8 hours')::DATE = mydate::DATE ;
                if myhours is null then
                  myhours := 0 ;
                end if ;
               myhours = myhours * 60 ;
                select coalesce(tolerance_time,0) into mytolerance from neweb_emp_timesheet_tolerance_setting ;
               if mytolerance is null then
                  mytolerance := 0 ;
               end if ;
               minhours := 480 - mytolerance ;
               if myhours < minhours then
                 myres := 1 ;
               else
                 myres := 0 ;
               end if ; 
               return myres ; 
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_illegalnum(empid int,mydate date) cascade""")
        self._cr.execute("""create or replace function get_illegalnum(empid int,mydate date) returns INT as $BODY$
            DECLARE
              myres INT ;
            BEGIN
              select count(*) into myres from neweb_emp_timesheet_timesheet_calendar_line where (timesheet_start_date + interval '8 hours')::DATE = mydate::DATE 
                     and emp_id=empid and is_complete='ng' ;
              if myres is null then
                 myres := 0 ;
              end if ;   
              return myres ;  
            END;$BODY$    
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_nocompleteemp(empid int,startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function gen_nocompleteemp(empid int,startdate date,enddate date) returns void as $BODY$
            DECLARE
               ncount int ;
               myyear varchar ;
               holidayid int ;
               myhours float ;
               ncount1 int ;
               illegalnum int ;
               deptid int ;
               mynowdate DATE;
               tolerancetime Float ;
               ncount2 int ;
            BEGIN
               select tolerance_time into tolerancetime from neweb_emp_timesheet_tolerance_setting ;
               tolerancetime := 480 - tolerancetime ;
               select department_id into deptid from hr_employee where id=empid ;
               select substring(startdate::TEXT,1,4) into myyear ;
               select id into holidayid from neweb_emp_timesheet_hrholiday where hr_holiday_year=myyear ;
               mynowdate := startdate::DATE ;
               loop
                  exit when mynowdate > enddate::DATE ;
                  select count(*) into ncount from neweb_emp_timesheet_hrholiday_line where holiday_date::DATE=mynowdate::DATE and holiday_id=holidayid ;
                  if ncount = 0 then
                     select count(*) into ncount2 from neweb_emp_timesheet_timesheet_nocomplete where timesheet_date::DATE = mynowdate::DATE and emp_id=empid ;
                     if ncount2 = 0 then
                         insert into neweb_emp_timesheet_timesheet_nocomplete(timesheet_date,emp_id,dept_id,timesheet_hours,illegal_num,no_complete) values (mynowdate::DATE,empid,deptid,0,0,False) ;
                     end if ;    
                  end if ;
                  illegalnum := 0 ;
                  select count(*) into illegalnum from neweb_emp_timesheet_timesheet_calendar_line where emp_id=empid and (timesheet_start_date + interval '8 hours')::DATE = mynowdate::DATE and is_complete='ng' ;
                  if illegalnum is not null and illegalnum > 0 then
                     update  neweb_emp_timesheet_timesheet_nocomplete set illegal_num=illegalnum where emp_id=empid and timesheet_date::DATE=mynowdate::DATE ; 
                  end if ;
                  myhours := 0 ;
                  select abs(coalesce(sum(duration),0)) into myhours from neweb_emp_timesheet_timesheet_calendar_line 
                          where emp_id=empid and (timesheet_start_date + interval '8 hours')::DATE = mynowdate::DATE ;
                  if myhours is not null and myhours > 0 then        
                     update  neweb_emp_timesheet_timesheet_nocomplete set timesheet_hours=myhours where emp_id=empid and timesheet_date::DATE=mynowdate::DATE ;  
                  end if ; 
                  select mynowdate::DATE + interval '1 days' into mynowdate ;      
               end loop ;
               update neweb_emp_timesheet_timesheet_nocomplete set no_complete = True where (timesheet_hours * 60) < tolerancetime ;
            END;$BODY$
            LANGUAGE plpgsql;""")



        self._cr.execute(
            """drop function if exists gen_nocompletedept(deptid int,startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function gen_nocompletedept(deptid int,startdate date,enddate date) returns void as $BODY$
              DECLARE
                 emp_cur refcursor ;
                 emp_rec record ;
                
              BEGIN
                 open emp_cur for select * from hr_employee where resource_id not in (select id from resource_resource where active=False) and department_id=deptid ;
                 loop 
                     fetch emp_cur into emp_rec ;
                     exit when not found ;
                     execute gen_nocompleteemp(emp_rec.id,startdate,enddate) ;
                  end loop ;
                  close emp_cur ;   
              END;$BODY$
              LANGUAGE plpgsql;""")

        self._cr.execute("drop function if exists recheckduration() cascade")
        self._cr.execute("""create or replace function recheckduration() returns void as $BODY$
            DECLARE
               dur_cur refcursor ;
               dur_rec record ;
               ncount int ;
               myhours float ;
               myminutes float ;
               mytime float ;
            BEGIN
               open dur_cur for select * from neweb_emp_timesheet_timesheet_calendar_line where duration is null or timesheet_duration is null or timesheet_duration <= 0 ;
               loop
                 fetch dur_cur into dur_rec ;
                 exit when not found ;
                 select abs(date_part('hour',age(dur_rec.timesheet_end_date + interval '8 hours',dur_rec.timesheet_start_date + interval '8 hours'))) into myhours ;
                 select abs(date_part('minute',age(dur_rec.timesheet_end_date + interval '8 hours',dur_rec.timesheet_start_date + interval '8 hours'))) into myminutes ;
                 mytime := myhours + (myminutes/60) ;
                 update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,duration=mytime where id=dur_rec.id ;
               end loop ;
               close dur_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists gettimesheetsale(originno varchar) cascade""")
        self._cr.execute("""create or replace function gettimesheetsale(originno varchar) returns int as $BODY$
            DECLARE
              ncount int ;
              myres int ;
              mycontractid int ;
            BEGIN
              select count(*) into ncount from neweb_project where name = originno ;
              if ncount > 0 then
                 select proj_sale into myres from neweb_project where name = originno ;
              else
                 select count(*) into ncount from neweb_contract_contract where name = originno ;
                 if ncount > 0 then
                    select sales into myres from neweb_contract_contract where name = originno ;
                 else  
                    select count(*) into ncount from neweb_repair_repair where name = originno ;
                    if ncount > 0 then
                       select coalesce(contract_id,0) into mycontractid from neweb_repair_repair where name = originno ;
                       if mycontractid > 0 then
                          select sales into myres from neweb_contract_contract where id = mycontractid ;
                       else
                          myres := 0 ;
                       end if ;   
                    else
                       select count(*) into ncount from neweb_proj_eng_assign where name = originno ;
                       if ncount > 0 then
                          select proj_sale into myres from neweb_proj_eng_assign where name = originno ;
                       else
                          myres := 0 ;
                       end if ;
                    end if ;
                 end if ;   
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentimesheetsale() cascade""")
        self._cr.execute("""create or replace function gentimesheetsale() returns void as $BODY$
            DECLARE
              tsline_cur refcursor ;
              tsline_rec record ;
              ncount int ;
              myres int ;
            BEGIN
              open tsline_cur for select id,timesheet_origin,sale_id from neweb_emp_timesheet_timesheet_calendar_line where sale_id is null and timesheet_origin is not null ;
              loop
                 fetch tsline_cur into tsline_rec ;
                 exit when not found ;
                 select gettimesheetsale(tsline_rec.timesheet_origin) into myres ;
                 if myres > 0 then
                    update neweb_emp_timesheet_timesheet_calendar_line set sale_id=myres where id = tsline_rec.id and sale_id is null ;
                 end if ;
              end loop ;
              close tsline_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")



        self._cr.execute("""drop function if exists updateworktype() cascade""")
        self._cr.execute("""create or replace function updateworktype() returns void as $BODY$
            DECLARE
               wt_cur refcursor ;
               wt_rec record ;
               mynitem int ;
               mycat varchar ;
               mynum int ;
               myworktypeid int ;
               myworktypeid1 int ;
            BEGIN
               update neweb_emp_timesheet_timesheet_worktype set worktype_desc='定期維護' where worktype_code='40' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_desc='支援原廠保固服務' where worktype_code='41' ;
               update neweb_emp_timesheet_timesheet_worktype set worktype_categ='保固支援工時' where worktype_cat='4' ;
               insert into neweb_emp_timesheet_timesheet_worktype (sequence,worktype_code,worktype_link,worktype_desc,worktype_categ,worktype_cat) values
                 (20,'42','4','支援原廠軟體處理','保固支援工時','4') ;
               insert into neweb_emp_timesheet_timesheet_worktype (sequence,worktype_code,worktype_link,worktype_desc,worktype_categ,worktype_cat) values
                 (20,'43','4','諮詢服務','保固支援工時','4') ;  
               insert into neweb_emp_timesheet_timesheet_worktype (sequence,worktype_code,worktype_link,worktype_desc,worktype_categ,worktype_cat) values
                 (20,'44','4','測試服務','保固支援工時','4') ;  
               insert into neweb_emp_timesheet_timesheet_worktype (sequence,worktype_code,worktype_link,worktype_desc,worktype_categ,worktype_cat) values
                 (20,'4A','4','POC','保固支援工時','4') ;   
               insert into neweb_emp_timesheet_timesheet_worktype (sequence,worktype_code,worktype_link,worktype_desc,worktype_categ,worktype_cat) values
                 (20,'4B','4','非合約的人力支援','保固支援工時','4') ;  
               mynitem = 1 ;
               open wt_cur for select * from neweb_emp_timesheet_timesheet_worktype where worktype_code != '18' order by worktype_cat,worktype_code  ;
               loop
                 fetch wt_cur into wt_rec ;
                 exit when not found ;
                 update neweb_emp_timesheet_timesheet_worktype set nitem=mynitem where id = wt_rec.id ;
                 mynitem = mynitem + 1 ;
               end loop ;
               select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype where worktype_code='40' ;
               select id into myworktypeid1 from neweb_emp_timesheet_timesheet_worktype where worktype_code='4A' ;
               update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=myworktypeid1 where timesheet_worktype=myworktypeid ;
               select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype where worktype_code='41' ;
               select id into myworktypeid1 from neweb_emp_timesheet_timesheet_worktype where worktype_code='4B' ;
               update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=myworktypeid1 where timesheet_worktype=myworktypeid ;
               select id into myworktypeid from neweb_emp_timesheet_timesheet_worktype where worktype_code='18' ;
               select id into myworktypeid1 from neweb_emp_timesheet_timesheet_worktype where worktype_code='41' ;
               update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=myworktypeid1 where timesheet_worktype=myworktypeid ;
               close wt_cur ;       
            END;$BODY$
            LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists getmaintype(repairid int) cascade""")
        self._cr.execute("""create or replace function getmaintype(repairid int) returns varchar as $BODY$
            DECLARE
              myres varchar ;
              myrepairlineid int ;
              mycontractid int ;
              ismaintenancecontract Boolean ;
              isoutsourcingservice Boolean ;
              iswarrantycontract Boolean ;
              myworktype char ;
            BEGIN
              select contract_id into mycontractid from neweb_repair_repair where id = repairid ;
              select min(id) into myrepairlineid from neweb_repair_repair_line where repair_id = repairid ;
              select repair_timesheet_worktype into myworktype from neweb_repair_repair_line where id = myrepairlineid ;
              select is_warranty_contract,is_maintenance_contract,is_outsourcing_service into 
                iswarrantycontract,ismaintenancecontract,isoutsourcingservice from neweb_contract_contract where id = mycontractid ;
              if myworktype='1' then
                 if iswarrantycontract is true then
                    myres = 'warranty_maintenance' ;
                 elsif ismaintenancecontract is true then
                    myres = 'hw_maintenance' ;
                 elsif isoutsourcingservice is true then
                    myres = 'hw_outsourcing' ;
                 else
                    myres = 'per_call' ;   
                 end if ;
              else
                 if iswarrantycontract is true then
                    myres = 'warranty_software' ;
                 elsif ismaintenancecontract is true then
                    myres = 'soft_maintenance' ;
                 elsif isoutsourcingservice is true then
                    myres = 'soft_outsourcing' ;
                 else
                    myres = 'per_call' ;   
                  end if ;
              end if ; 
             
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists update_contract_type(contractno varchar) cascade""")
        self._cr.execute("""create or replace function update_contract_type(contractno varchar) returns void as $BODY$
           DECLARE
             ncount int ;
             o20 int ;
             o30 int ;
             n40 int ;
             o21 int ;
             o31 int ;
             n41 int ;
             o22 int ;
             o32 int ;
             n42 int ;
             o23 int ;
             o33 int ;
             n43 int ;
             o24 int ;
             o34 int ;
             n44 int ;
             o25 int ;
             o35 int ;
             n45 int ;
             o26 int ;
             o36 int ;
             n46 int ;
             o27 int ;
             o37 int ;
             n47 int ;
             o29 int ;
             o39 int ;
             n49 int ;
             ts_cur refcursor ;
             ts_rec record ;
           BEGIN
             select id into o20 from neweb_emp_timesheet_timesheet_worktype where worktype_code='20' ;
             select id into o21 from neweb_emp_timesheet_timesheet_worktype where worktype_code='21' ;
             select id into o22 from neweb_emp_timesheet_timesheet_worktype where worktype_code='22' ;
             select id into o23 from neweb_emp_timesheet_timesheet_worktype where worktype_code='23' ;
             select id into o24 from neweb_emp_timesheet_timesheet_worktype where worktype_code='24' ;
             select id into o25 from neweb_emp_timesheet_timesheet_worktype where worktype_code='25' ;
             select id into o26 from neweb_emp_timesheet_timesheet_worktype where worktype_code='26' ;
             select id into o27 from neweb_emp_timesheet_timesheet_worktype where worktype_code='27' ;
             select id into o29 from neweb_emp_timesheet_timesheet_worktype where worktype_code='29' ;
             
             select id into o30 from neweb_emp_timesheet_timesheet_worktype where worktype_code='30' ;
             select id into o31 from neweb_emp_timesheet_timesheet_worktype where worktype_code='31' ;
             select id into o32 from neweb_emp_timesheet_timesheet_worktype where worktype_code='32' ;
             select id into o33 from neweb_emp_timesheet_timesheet_worktype where worktype_code='33' ;
             select id into o34 from neweb_emp_timesheet_timesheet_worktype where worktype_code='34' ;
             select id into o35 from neweb_emp_timesheet_timesheet_worktype where worktype_code='35' ;
             select id into o36 from neweb_emp_timesheet_timesheet_worktype where worktype_code='36' ;
             select id into o37 from neweb_emp_timesheet_timesheet_worktype where worktype_code='37' ;
             select id into o39 from neweb_emp_timesheet_timesheet_worktype where worktype_code='39' ;
             
             select id into n40 from neweb_emp_timesheet_timesheet_worktype where worktype_code='40' ;
             select id into n41 from neweb_emp_timesheet_timesheet_worktype where worktype_code='41' ;
             select id into n42 from neweb_emp_timesheet_timesheet_worktype where worktype_code='42' ;
             select id into n43 from neweb_emp_timesheet_timesheet_worktype where worktype_code='43' ;
             select id into n44 from neweb_emp_timesheet_timesheet_worktype where worktype_code='44' ;
             select id into n45 from neweb_emp_timesheet_timesheet_worktype where worktype_code='45' ;
             select id into n46 from neweb_emp_timesheet_timesheet_worktype where worktype_code='46' ;
             select id into n47 from neweb_emp_timesheet_timesheet_worktype where worktype_code='47' ;
             select id into n49 from neweb_emp_timesheet_timesheet_worktype where worktype_code='49' ;
             
             select count(*) into ncount from neweb_contract_contract where name = contractno ;
             if ncount > 0 then
                update neweb_contract_contract set is_warranty_contract=true,is_maintenance_contract=false,is_outsourcing_service=false where name = contractno ;
                open ts_cur for select * from neweb_emp_timesheet_timesheet_calendar_line where timesheet_origin = contractno ;
                loop
                  fetch ts_cur into ts_rec ;
                  exit when not found ;
                  if ts_rec.timesheet_worktype=o20 or ts_rec.timesheet_worktype=o30 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n40 where id = ts_rec.id ;
                  elsif ts_rec.timesheet_worktype=o21 or ts_rec.timesheet_worktype=o31 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n41 where id = ts_rec.id ;   
                  elsif ts_rec.timesheet_worktype=o22 or ts_rec.timesheet_worktype=o32 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n42 where id = ts_rec.id ;   
                  elsif ts_rec.timesheet_worktype=o23 or ts_rec.timesheet_worktype=o33 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n43 where id = ts_rec.id ; 
                  elsif ts_rec.timesheet_worktype=o24 or ts_rec.timesheet_worktype=o34 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n44 where id = ts_rec.id ;  
                  elsif ts_rec.timesheet_worktype=o25 or ts_rec.timesheet_worktype=o35 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n45 where id = ts_rec.id ;   
                  elsif ts_rec.timesheet_worktype=o26 or ts_rec.timesheet_worktype=o36 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n46 where id = ts_rec.id ; 
                  elsif ts_rec.timesheet_worktype=o27 or ts_rec.timesheet_worktype=o37 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n47 where id = ts_rec.id ;    
                  elsif ts_rec.timesheet_worktype=o29 or ts_rec.timesheet_worktype=o39 then
                     update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n49 where id = ts_rec.id ; 
                  end if ;         
                end loop ;
                close ts_cur ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_contract_type1(projectno varchar) cascade""")
        self._cr.execute("""create or replace function update_contract_type1(projectno varchar) returns void as $BODY$
                   DECLARE
                     ncount int ;
                      o20 int ;
                      o30 int ;
                      n40 int ;
                      o21 int ;
                      o31 int ;
                      n41 int ;
                      o22 int ;
                      o32 int ;
                      n42 int ;
                      o23 int ;
                      o33 int ;
                      n43 int ;
                      o24 int ;
                      o34 int ;
                      n44 int ;
                      o25 int ;
                      o35 int ;
                      n45 int ;
                      o26 int ;
                      o36 int ;
                      n46 int ;
                      o27 int ;
                      o37 int ;
                      n47 int ;
                      o29 int ;
                      o39 int ;
                      n49 int ;
                     ts_cur refcursor ;
                     ts_rec record ;
                   BEGIN
                     select id into o20 from neweb_emp_timesheet_timesheet_worktype where worktype_code='20' ;
                     select id into o21 from neweb_emp_timesheet_timesheet_worktype where worktype_code='21' ;
                     select id into o22 from neweb_emp_timesheet_timesheet_worktype where worktype_code='22' ;
                     select id into o23 from neweb_emp_timesheet_timesheet_worktype where worktype_code='23' ;
                     select id into o24 from neweb_emp_timesheet_timesheet_worktype where worktype_code='24' ;
                     select id into o25 from neweb_emp_timesheet_timesheet_worktype where worktype_code='25' ;
                     select id into o26 from neweb_emp_timesheet_timesheet_worktype where worktype_code='26' ;
                     select id into o27 from neweb_emp_timesheet_timesheet_worktype where worktype_code='27' ;
                     select id into o29 from neweb_emp_timesheet_timesheet_worktype where worktype_code='29' ;
                     
                      select id into o30 from neweb_emp_timesheet_timesheet_worktype where worktype_code='30' ;
                      select id into o31 from neweb_emp_timesheet_timesheet_worktype where worktype_code='31' ;
                      select id into o32 from neweb_emp_timesheet_timesheet_worktype where worktype_code='32' ;
                      select id into o33 from neweb_emp_timesheet_timesheet_worktype where worktype_code='33' ;
                      select id into o34 from neweb_emp_timesheet_timesheet_worktype where worktype_code='34' ;
                      select id into o35 from neweb_emp_timesheet_timesheet_worktype where worktype_code='35' ;
                      select id into o36 from neweb_emp_timesheet_timesheet_worktype where worktype_code='36' ;
                      select id into o37 from neweb_emp_timesheet_timesheet_worktype where worktype_code='37' ;
                      select id into o39 from neweb_emp_timesheet_timesheet_worktype where worktype_code='39' ;
                     
                     select id into n40 from neweb_emp_timesheet_timesheet_worktype where worktype_code='40' ;
                     select id into n41 from neweb_emp_timesheet_timesheet_worktype where worktype_code='41' ;
                     select id into n42 from neweb_emp_timesheet_timesheet_worktype where worktype_code='42' ;
                     select id into n43 from neweb_emp_timesheet_timesheet_worktype where worktype_code='43' ;
                     select id into n44 from neweb_emp_timesheet_timesheet_worktype where worktype_code='44' ;
                     select id into n45 from neweb_emp_timesheet_timesheet_worktype where worktype_code='45' ;
                     select id into n46 from neweb_emp_timesheet_timesheet_worktype where worktype_code='46' ;
                     select id into n47 from neweb_emp_timesheet_timesheet_worktype where worktype_code='47' ;
                     select id into n49 from neweb_emp_timesheet_timesheet_worktype where worktype_code='49' ;

                     select count(*) into ncount from neweb_project where name = projectno ;
                     if ncount > 0 then
                        open ts_cur for select * from neweb_emp_timesheet_timesheet_calendar_line where timesheet_origin = projectno ;
                        loop
                          fetch ts_cur into ts_rec ;
                          exit when not found ;
                          if ts_rec.timesheet_worktype=o20 or ts_rec.timesheet_worktype=o30 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n40 where id = ts_rec.id ;
                          elsif ts_rec.timesheet_worktype=o21 or ts_rec.timesheet_worktype=o31 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n41 where id = ts_rec.id ;   
                          elsif ts_rec.timesheet_worktype=o22 or ts_rec.timesheet_worktype=o32 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n42 where id = ts_rec.id ;   
                          elsif ts_rec.timesheet_worktype=o23 or ts_rec.timesheet_worktype=o33 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n43 where id = ts_rec.id ; 
                          elsif ts_rec.timesheet_worktype=o24 or ts_rec.timesheet_worktype=o34 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n44 where id = ts_rec.id ;  
                          elsif ts_rec.timesheet_worktype=o25 or ts_rec.timesheet_worktype=o35 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n45 where id = ts_rec.id ;   
                          elsif ts_rec.timesheet_worktype=o26 or ts_rec.timesheet_worktype=o36 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n46 where id = ts_rec.id ; 
                          elsif ts_rec.timesheet_worktype=o27 or ts_rec.timesheet_worktype=o37 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n47 where id = ts_rec.id ;    
                          elsif ts_rec.timesheet_worktype=o29 or ts_rec.timesheet_worktype=o39 then
                             update neweb_emp_timesheet_timesheet_calendar_line set timesheet_worktype=n49 where id = ts_rec.id ; 
                          end if ;         
                        end loop ;
                        close ts_cur ;
                     end if ;
                   END;$BODY$
                   LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_nocompletealldept(startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function gen_nocompletealldept(startdate date,enddate date) returns void as $BODY$
                  DECLARE
                     emp_cur refcursor ;
                     emp_rec record ;
                     dept_cur refcursor ;
                     dept_rec record ;
                  BEGIN
                     open dept_cur for select * from hr_department where active=True and 
                        (name like '%A10%' or name like '%A20%' or name like '%A30%' or name like '%A40%') ;
                     loop
                        fetch dept_cur into dept_rec ;
                        exit when not found ;
                         open emp_cur for select * from hr_employee where resource_id not in (select id from resource_resource where active=False) and department_id = dept_rec.id ;
                         loop 
                             fetch emp_cur into emp_rec ;
                             exit when not found ;
                             execute gen_nocompleteemp(emp_rec.id,startdate,enddate) ;
                          end loop ;
                          close emp_cur ; 
                     end loop ;
                     close dept_cur ;       
                  END;$BODY$
                  LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists rechecktodoorigin() cascade""")
        self._cr.execute("""create or replace function rechecktodoorigin() returns void as $BODY$
            DECLARE
               todo_cur refcursor ;
               todo_rec record ;
               projno int;
            BEGIN
               open todo_cur for select id,todo_origin,assign_no from neweb_emp_timesheet_todo_calendar where todo_origin='3' ;
               loop
                 fetch todo_cur into todo_rec ;
                 exit when not found ;
                 select proj_no into projno from neweb_proj_eng_assign where id = todo_rec.assign_no ;
                 if projno is null then
                    update neweb_emp_timesheet_todo_calendar set todo_origin='4' where id=todo_rec.id ;
                    update neweb_emp_timesheet_timesheet_calendar_line set origin_type='4' where origin_type='3' and origin_id in (select id from neweb_assign_complete 
                        where complete_id=todo_rec.assign_no) ;
                 end if ;
               end loop ;
               close todo_cur ;
            END;$BODY$
            LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists getadjustowner(userid int) cascade""")
        self._cr.execute("""create or replace function getadjustowner(userid int) returns Boolean as $BODY$
            DECLARE
              myres Boolean ;
              ncount int ;
            BEGIN
              select count(*) into ncount from neweb_emp_timesheet_timesheet_adjustowner where 
                   timesheet_adjustowner = userid ;
              if ncount = 0 then
                 myres := False ;
              else
                 myres := True ;
              end if ;  
              return myres ;   
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delmailmessage() cascade""")
        self._cr.execute("""create or replace function delmailmessage() returns void as $BODY$
            DECLARE
               ncount int ;
            BEGIN
               delete from mail_message where date::DATE < now()::DATE - interval '7 days' ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists todosetrepairtime(todocalid int,reptype char)""")
        self._cr.execute("""create or replace function todosetrepairtime(todocalid int,reptype char) returns void as $BODY$
           DECLARE
             repno int ;
             ncount int ;
             mytime TIMESTAMP ;
           BEGIN
             select repair_no into repno from neweb_emp_timesheet_todo_calendar where id = todocalid ;
             if repno is not null then
                if reptype='1' then
                   select ae_response_datetime into mytime from neweb_emp_timesheet_todo_calendar where id = todocalid ;
                   update neweb_repair_repair set ae_response_datetime=mytime where id = repno and 
                      ae_response_datetime is null ;
                elsif reptype='2' then
                   select ae_on_site_datetime into mytime from neweb_emp_timesheet_todo_calendar where id = todocalid ;
                   update neweb_repair_repair set ae_on_site_datetime=mytime where id = repno and
                    ae_on_site_datetime is null;
                else
                   select ae_complete_datetime into mytime from neweb_emp_timesheet_todo_calendar where id = todocalid ;
                   update neweb_repair_repair set ae_complete_datetime=mytime where id = repno and
                    ae_complete_datetime is null;
                end if ;
             end if ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists todo_change_emp(oempid int,nempid int,chgdate DATE) cascade""")
        self._cr.execute("""drop function if exists todo_change_emp(oempid int,nempid int,chgdate DATE,wizid int) cascade""")
        self._cr.execute("""create or replace function todo_change_emp(oempid int,nempid int,chgdate DATE,wizid int) returns void as $BODY$
           DECLARE
             con_cur refcursor ;
             con_rec record ;
             rel_cur refcursor;
             rel_rec record ;
             mycontractid int ;
           BEGIN
              open con_cur for select distinct contract_id from timesheet_change_emp_contract_rel where wiz_id=wizid order by contract_id ;
              loop
                 fetch con_cur into con_rec ;
                 exit when not found ;
                 update neweb_emp_timesheet_todo_calendar set emp_id=nempid where emp_id=oempid and todo_datetime::DATE >= chgdate::DATE  and contract_no=con_rec.contract_id ;
                 update neweb_contract_inspection_list set emp_id=nempid where  subscribe_date::DATE > chgdate::DATE and emp_id=oempid and inspection_id=con_rec.contract_id ; 
                 open rel_cur for select * from hr_employee_neweb_contract_contract_rel where hr_employee_id=oempid and neweb_contract_contract_id = con_rec.contract_id ;
                  loop
                     fetch rel_cur into rel_rec ;
                     exit when not found ;
                       mycontractid = rel_rec.neweb_contract_contract_id ;
                       delete from hr_employee_neweb_contract_contract_rel where hr_employee_id = oempid ;
                       insert into hr_employee_neweb_contract_contract_rel(neweb_contract_contract_id,hr_employee_id) values
                          (mycontractid,nempid) ;
                  end loop ;
                  close rel_cur ;   
                  open rel_cur for select * from neweb_contract_maintenance_warn_users_rel where hr_employee_id=oempid and neweb_contract_contract_id = con_rec.contract_id ;
                  loop
                     fetch rel_cur into rel_rec ;
                     exit when not found ;
                       mycontractid = rel_rec.neweb_contract_contract_id ;
                       delete from neweb_contract_maintenance_warn_users_rel where hr_employee_id = oempid ;
                       insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id) values
                          (mycontractid,nempid) ;
                  end loop ;
                  close rel_cur ;    
              end loop ;
              close con_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getoldempcontract(empid int) cascade""")
        self._cr.execute("""create or replace function getoldempcontract(empid int) returns setof INT as $BODY$
           DECLARE
              myres int ;
              con_cur refcursor;
              con_rec record ;
           BEGIN
              delete from timesheet_change_emp_contract_rel ;
              open con_cur for select distinct neweb_contract_contract_id from hr_employee_neweb_contract_contract_rel 
                  where hr_employee_id = empid order by neweb_contract_contract_id;
              loop    
                  fetch con_cur into con_rec ;
                  exit when not found ;
                  return next con_rec.neweb_contract_contract_id ;
              end loop ;
              close con_cur ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS get_sale_dept(empid int) cascade;""")
        self._cr.execute("""create or replace function get_sale_dept(empid int) returns int as $BODY$
           declare
             ncount int ;
             deptid int;
           BEGIN
             select department_id into deptid from hr_employee where id=empid;
             if deptid is null then 
                deptid := 148 ;
             end if ;
             return deptid ;

           end; $BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gettododt(mytodotime timestamp) cascade""")
        self._cr.execute("""create or replace function gettododt(mytodotime timestamp) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           myh varchar ;
           mym varchar ;
         BEGIN
           select lpad(date_part('hour',mytodotime + interval '8 hours')::TEXT,2,'0') into myh ;
           select lpad(date_part('minute',mytodotime + interval '8 hours')::TEXT,2,'0') into mym ;
           myres = concat(myh,':',mym) ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("drop function if exists recheckallduration() cascade")
        self._cr.execute("""create or replace function recheckallduration() returns void as $BODY$
            DECLARE
               dur_cur refcursor ;
               dur_rec record ;
               ncount int ;
               myhours float ;
               myminutes float ;
               mytime float ;
            BEGIN
               open dur_cur for select * from neweb_emp_timesheet_timesheet_calendar_line  ;
               loop
                 fetch dur_cur into dur_rec ;
                 exit when not found ;
                 select abs(date_part('hour',age(dur_rec.timesheet_end_date,dur_rec.timesheet_start_date))) into myhours ;
                 select abs(date_part('minute',age(dur_rec.timesheet_end_date,dur_rec.timesheet_start_date))) into myminutes ;
                 mytime := myhours + (myminutes::numeric/60::numeric) ;
                 update neweb_emp_timesheet_timesheet_calendar_line set timesheet_duration=mytime,duration=mytime where id=dur_rec.id ;
               end loop ;
               close dur_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_startdt() cascade""")
        self._cr.execute("""create or replace function get_startdt() returns timestamp as $BODY$
         DECLARE
          myres timestamp ;
          today varchar ;
         BEGIN
          select current_timestamp::DATE::TEXT into today ;
          myres = concat(today,' 09:00:00')::timestamp ;
          return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists cal_ins_dur(startdt timestamp,enddt timestamp) cascade""")
        self._cr.execute("""create or replace function cal_ins_dur(startdt timestamp,enddt timestamp) returns Float as $BODY$
          DECLARE
            durm float ;
            durh float ;
            durh1 float ;
          BEGIN
            select date_part('hour',age(enddt::timestamp,startdt::timestamp)) into durh ;
            select date_part('minute',age(enddt::timestamp,startdt::timestamp)) into durm ;
            durh1 =  round((durm::numeric / 60::numeric),2)::numeric ;
            durh = durh + durh1 ;
            return durh ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getempno(empno varchar) cascade""")
        self._cr.execute("""create or replace function getempno(empno varchar) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            if empno is not null then
               select count(*) into ncount from hr_employee where employee_num=empno and active=True ;
               if ncount > 0 then
                  select id into myres from hr_employee where employee_num=empno and active=True ;
               end if ;
            end if ;
            return myres ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentimesheetnitem() cascade""")
        self._cr.execute("""create or replace function gentimesheetnitem() returns void as $BODY$
         DECLARE
            t_cur refcursor ;
            t_rec record ;
            nnum int ;
            empid int ;
         BEGIN
            nnum = 1 ;
            empid = 0 ;
            open t_cur for select id,nitem,emp_id,timesheet_start_date from neweb_emp_timesheet_timesheet_calendar_line where nitem is null
               order by emp_id,timesheet_start_date ;
            loop
               fetch t_cur into t_rec ;
               exit when not found ;
               if empid != t_rec.emp_id then
                  empid = t_rec.emp_id ;
                  nnum = 1 ;
               end if ;
               update neweb_emp_timesheet_timesheet_calendar_line set nitem=nnum where id = t_rec.id ;
               nnum = coalesce(nnum,0) + 1 ;
            end loop ;
            close t_cur ;   
         END;$BODY$
         LANGUAGE plpgsql;""")



