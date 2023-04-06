# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class newebrepairstoreproc(models.Model):
    _name = "neweb_repair.storeproc"


    @api.model
    def init(self):

        self._cr.execute("""DROP FUNCTION IF EXISTS get_carecalldate(contractid int) cascade;""")
        self._cr.execute("""create or replace function get_carecalldate(contractid int) returns void as $BODY$
         declare
           mycarecalldate neweb_repair_repair.care_call_date%type;
           myid INTEGER ;
           mycount INTEGER ;
         begin
           select count(*) into mycount from neweb_repair_repair_care_call_log where repair_id=contractid;
           if mycount >0 then
              select max(id) into myid from neweb_repair_repair_care_call_log where repair_id=contractid;
              select care_call_date into mycarecalldate from neweb_repair_repair_care_call_log
                     where id=myid;
              update neweb_repair_repair set care_call_date=mycarecalldate where id=contractid;
           end if;
         end;$BODY$
         LANGUAGE plpgsql;
           """)


        self._cr.execute("""drop function if exists get_contact_person(contractid int) cascade;""")
        self._cr.execute("""create or replace function get_contact_person(contractid int) returns VARCHAR as $BODY$
            DECLARE 
                contactinfo VARCHAR ;
                myphone VARCHAR ;
                mymobile VARCHAR ;
                myname VARCHAR ;
                partnerid int;
                ncount int ;
            BEGIN 
                select contact_person into partnerid from neweb_contract_contract where id=contractid ;
                select count(*) into ncount from res_partner where id=partnerid ;
                if ncount > 0 THEN 
                   select name,phone,mobile into myname,myphone,mymobile from res_partner where id=partnerid ;
                   if myname is null THEN 
                      myname := 'NO NAME' ;
                   end if;
                   if myphone is null THEN 
                      myphone := 'NO PHONE';
                   end if ;
                   if mymobile is null THEN 
                      mymobile := 'NO MOBILE' ;
                   end if ;
                   contactinfo := myname || ' / ' || myphone || ' / ' || mymobile ;
                ELSE 
                   contactinfo := 'NO CONTACT INFO' ;
                end if ;
                return contactinfo ;
            END; $BODY$
            LANGUAGE plpgsql ;   
                   """)

        self._cr.execute("""drop function if exists get_contract_enduser(contractid int) cascade;""")
        self._cr.execute("""create or replace function get_contract_enduser(contractid int) returns INTEGER as $BODY$
            DECLARE 
               ncount int;
               myendcustomer int;
            BEGIN 
               select end_customer into myendcustomer from neweb_contract_contract where id=contractid ;
               if myendcustomer is not null THEN
                  return myendcustomer ;
               ELSE 
                  return 0 ;      
               end if ; 
            END ; $BODY$
            LANGUAGE plpgsql; """)

        self._cr.execute("""drop function if exists checkrepairparts(repairid int) cascade;""")
        self._cr.execute("""create or replace function checkrepairparts(repairid int) returns Boolean as $BODY$
            DECLARE 
               ncount int ;
               myres Boolean ;
            BEGIN 
               select count(*) into ncount from neweb_repair_repair_part where repair_line_id in 
                 (select id from neweb_repair_repair_line where repair_id=repairid) and prod is null ;
               if ncount > 0 then 
                  myres := FALSE ;
               else 
                  myres := TRUE ; 
               end if; 
               return myres ;
            END ;$BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists trackingparts(prodid int) cascade;""")
        self._cr.execute("""create or replace function trackingparts(prodid int) returns setof character varying  as $BODY$
            DECLARE 
               repair_cur refcursor ;
               repair_rec record ;
            BEGIN
               open repair_cur for select distinct id from neweb_repair_repair where id in 
                  (select repair_id from neweb_repair_repair_line where id in 
                    (select repair_line_id from neweb_repair_repair_part where prod = prodid)) ;
               loop
                 fetch repair_cur into repair_rec ;
                 exit when not found ;
                 return next repair_rec.id ;
               end loop;
               close repair_cur ;      
            END ;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists change_parts(repairid int,oprodid int,cprodid int) cascade;""")
        self._cr.execute("""drop function if exists changeparts(repairid int,oprodid int,cprodid int) cascade;""")
        self._cr.execute("""create or replace function changeparts(repairid int,oprodid int,cprodid int) returns void as $BODY$
            DECLARE 
              ncount int ;
            BEGIN 
              select count(*) into ncount from neweb_repair_repair_part where repair_line_id in 
               (select id from neweb_repair_repair_line where repair_id=repairid) and prod = oprodid ;
              if ncount > 0 then 
                 update neweb_repair_repair_part set prod=cprodid where repair_line_id in 
               (select id from neweb_repair_repair_line where repair_id=repairid) and prod = oprodid ;
              end if ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getcontractlineid(serialno varchar) cascade""")
        self._cr.execute("""create or replace function getcontractlineid(serialno varchar) returns int as $BODY$
            DECLARE 
              ncount int ;
              myres int ;
              mynowdate date ;
              mylen int ;
            BEGIN 
              if length(coalesce(trim(serialno),''))=0 then 
                  myres = 0 ;
              else
                  select now()::date into mynowdate ; 
                  select count(*) into ncount from neweb_contract_contract_line where machine_serial_no ilike '%'|| serialno ||'%' 
                     and mynowdate between contract_start_date::date and contract_end_date::date ;
                  if ncount > 0 then
                      select id into myres from neweb_contract_contract_line where machine_serial_no ilike '%'|| serialno ||'%' 
                          and mynowdate between contract_start_date::date and contract_end_date::date ;
                  else   
                      myres := 0 ;       
                  end if ;
              end if ;    
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmachineserialno(conlineid int) cascade""")
        self._cr.execute("""create or replace function getmachineserialno(conlineid int) returns varchar as $BODY$
           DECLARE
             ncount int ;
             myres varchar ;
           BEGIN
             if conlineid is null then
                myres = '' ;
             else
                select concat(coalesce(machine_serial_no,'No Contract Now'),' (',prod_modeltype,')') into myres from 
                       neweb_contract_contract_line where id = conlineid ;
             end if ;   
             return myres ; 
           END;$BODY$
           LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists runrepeatcall(startdate date,enddate date,repeatnum int) cascade""")
        self._cr.execute("""create or replace function runrepeatcall(startdate date,enddate date,repeatnum int) returns void as $BODY$
           DECLARE
              rep_cur refcursor ;
              rep_rec record ;
              rep1_cur refcursor ;
              rep1_rec record ;
              pb_cur refcursor ;
              pb_rec record ;
              pr_cur refcursor ;
              pr_rec record ;
              ncount int ;
              mypbdesc varchar ;
              myprdesc varchar ;
              myprodmodeltype varchar ;
           BEGIN
              delete from neweb_repair_repeat_call_report ;
              open rep_cur for select distinct prod_serial_no from neweb_repair_repair_product_serial_no_report where 
                 (repair_datetime + interval '8 hours')::DATE between startdate::DATE and enddate::DATE ;
              loop
                 fetch rep_cur into rep_rec ;
                 exit when not found ;
                 
                 select sum(device_amount) into ncount from neweb_repair_repair_product_serial_no_report where 
                    prod_serial_no = rep_rec.prod_serial_no 
                    and (repair_datetime::DATE between startdate::DATE and enddate::DATE);
                 if ncount >= repeatnum then
                    open rep1_cur for select * from neweb_repair_repair_product_serial_no_report where prod_serial_no = rep_rec.prod_serial_no 
                    and (repair_datetime::DATE between startdate::DATE and enddate::DATE);
                    loop
                       fetch rep1_cur into rep1_rec ;
                       exit when not found ;
                       mypbdesc='' ;
                       open pb_cur for select id,repair_id,problem_desc from neweb_repair_repair_line where repair_id=rep1_rec.id ;
                         loop
                           fetch pb_cur into pb_rec ;
                           exit when not found ;
                           if mypbdesc ='' then
                              mypbdesc = coalesce(pb_rec.problem_desc,' ') ;
                           else
                              mypbdesc = concat(mypbdesc,' /',coalesce(pb_rec.problem_desc,' ')) ;
                           end if ;   
                         end loop ;
                         close pb_cur ;
                         myprdesc='' ;
                         open pr_cur for select id,repair_id,work_log from neweb_repair_repair_work_log where repair_id=rep1_rec.id ;
                         loop
                           fetch pr_cur into pr_rec ;
                           exit when not found ;
                           if myprdesc ='' then
                              myprdesc = coalesce(pr_rec.work_log,' ') ;
                           else
                              myprdesc = concat(myprdesc,' /',coalesce(pr_rec.work_log,' ')) ;
                           end if ;   
                         end loop ;
                         close pr_cur ;
                         select getprodmodeltype(rep1_rec.prod_serial_no) into myprodmodeltype ;
                       insert into neweb_repair_repeat_call_report(name,repair_datetime,end_customer,ae_id,prod_serial_no,
                         prod_serial,device_amount,tot_amount,problem_desc,process_desc) values (rep1_rec.name,rep1_rec.repair_datetime,
                         rep1_rec.end_customer,rep1_rec.ae_id,rep1_rec.prod_serial_no,myprodmodeltype,rep1_rec.device_amount,ncount,
                         mypbdesc,myprdesc) ; 
                    end loop ;
                    close rep1_cur ;
                 end if ; 
              end loop ;
              close rep_cur ;   
           END;$BODY$
           LANGUAGE plpgsql""")

        self._cr.execute("""drop function if exists getprodmodeltype(serialno varchar) cascade""")
        self._cr.execute("""create or replace function getprodmodeltype(serialno varchar) returns varchar as $BODY$
           DECLARE
             myres varchar ;
             ncount int ;
             maxid int ;
           BEGIN
             select max(id) into maxid from neweb_contract_contract_line where machine_serial_no = serialno and prod_modeltype is not null ;
             if maxid is not null then
                select prod_modeltype into myres from neweb_contract_contract_line where id = maxid ;
             else
                myres = ' ' ;
             end if ; 
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getserialrepcall(serialno varchar) cascade""")
        self._cr.execute("""create or replace function getserialrepcall(serialno varchar) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
            mynowdate date ;
            bdate date ;
          BEGIN
            select current_date::DATE into mynowdate ;
            select mynowdate::DATE - interval '3 months' into bdate ;
            select count(*) into myres from neweb_repair_repair_product_serial_no_report where prod_serial_no = serialno
            and repair_datetime::DATE >= bdate::DATE ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getcarecalllist(startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function getcarecalllist(startdate date,enddate date) returns setof int as $BODY$
         DECLARE
           myres int ;
           care_cur refcursor ;
           care_rec record ;
         BEGIN
           open care_cur for select distinct repair_id from neweb_repair_repair_care_call_log where care_call_date::DATE between startdate::DATE and enddate::DATE ;
           loop
             fetch care_cur into care_rec ;
             exit when not found ;
             return next care_rec.repair_id ;
           end loop ;
           close care_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getaetotmatime(repid int) cascade""")
        self._cr.execute("""create or replace function getaetotmatime(repid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           onsitedt timestamp ;
           completedt timestamp ;
           nday int ;
           nhours int ;
           nmin int ;
         BEGIN
           select ae_on_site_datetime,ae_complete_datetime into onsitedt,completedt from neweb_repair_repair where id = repid ;
           if onsitedt is not null and completedt is not null then
              select date_part('day',age(completedt,onsitedt)) into nday ;
              select date_part('hour',age(completedt,onsitedt)) into nhours ;
              select date_part('minute',age(completedt,onsitedt)) into nmin ;
           end if ;
           myres = ' ' ;
           if nday > 0 then
              myres = concat(nday::TEXT,' 天 ') ;
           end if ;
           if nhours > 0 then
              myres = concat(myres,nhours::TEXT,' 小時 ') ;
           end if ;
           if nmin > 0 then
              myres = concat(myres,nmin::TEXT,' 分') ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chksladelay(repid int) cascade""")
        self._cr.execute("""create or replace function chksladelay(repid int) returns Boolean as $BODY$
          DECLARE
            slaid int ;
            contractid int ;
            repdt timestamp ;  /* 報修時間 */
            resdt timestamp ;  /* 回應時間 */
            onsdt timestamp ;  /* 到場時間 */
            comdt timestamp ;  /* 完修時間 */
            nh int ;
            nm int ;
            myres Boolean ;
            rept float ;       /* sla 回應時 */
            onsitet float ;    /* sla 到場時 */
            maint float ;      /* sla 維修時 */
            rept1 float ;       /*  回應時 */
            onsitet1 float ;    /*  到場時 */
            maint1 float ;      /*  維修時 */
          BEGIN
            myres = False ; 
            select repair_datetime,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,contract_id into 
                   repdt,resdt,onsdt,comdt,contractid from neweb_repair_repair where id = repid ;
            rept = 0 ;
            onsitet = 0 ;
            maint = 0 ;       
            if contractid is not null then
                select sla into slaid from neweb_contract_contract where id = contractid ;
                select response_time,onsite_time,maintenance_time into rept,onsitet,maint from neweb_base_sla where id = slaid ;
                select date_part('hour',age(resdt,repdt))::INT into nh ;
                select date_part('minute',age(resdt,repdt))::INT into nm ;
                rept1 = nh+round((nm::numeric/60::numeric),2) ;  /* 報修 -> 回應 時間 */
                select date_part('hour',age(onsdt,repdt))::INT into nh ;
                select date_part('minute',age(onsdt,repdt))::INT into nm ;
                onsitet1 = nh+round((nm::numeric/60::numeric),2) ;  /* 報修 -> 到場 時間 */
                select date_part('hour',age(comdt,repdt))::INT into nh ;
                select date_part('minute',age(comdt,repdt))::INT into nm ;
                maint1 = nh+round((nm::numeric/60::numeric),2) ;  /* 報修 -> 回應 時間 */
            end if ;
            if rept > 0 or onsitet > 0 or maint > 0 then
               if rept1 > rept or onsitet1 > onsitet or maint1 > maint then
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

        self._cr.execute("""drop function if exists genmachserno() cascade""")
        self._cr.execute("""create or replace function genmachserno() returns void as $BODY$
         DECLARE
           rl_cur refcursor ;
           rl_rec record ;
           machserno varchar ; 
         BEGIN
           open rl_cur for select id,contract_line from neweb_repair_repair_line where contract_line is not null ;
           loop
             fetch rl_cur into rl_rec ;
             exit when not found ;
             select getmachineserialno(rl_rec.contract_line) into machserno ;
             if machserno != '' then
                update neweb_repair_repair_line set machine_serial_no1=machserno,machine_serial_no=machserno where id = rl_rec.id ;
             end if ;   
           end loop ;
           close rl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gettimesheetcount(conid int) cascade""")
        self._cr.execute("""create or replace function gettimesheetcount(conid int) returns INT as $BODY$
          DECLARE
            conname varchar ;
            myres int ;
          BEGIN
            select name into conname from neweb_contract_contract where id = conid ;
            if conname is not null then
               select sum(duration)::NUMERIC::INT into myres from neweb_emp_timesheet_timesheet_calendar_line where timesheet_origin=conname ; 
            end if ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentimesheetrec(conid int) cascade""")
        self._cr.execute("""create or replace function gentimesheetrec(conid int) returns setof INT as $BODY$
          DECLARE
            conname varchar ;
            ts_cur refcursor ;
            ts_rec record ;
          BEGIN
            select name into conname from neweb_contract_contract where id = conid ;
            open ts_cur for select id from neweb_emp_timesheet_timesheet_calendar_line where timesheet_origin=conname ;
            loop
              fetch ts_cur into ts_rec ;
              exit when not found ;
              return next ts_rec.id ;
            end loop ;
            close ts_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


