# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class newebcontractstoreproc(models.Model):
    _name = "neweb_contract.store_proc"


    @api.model
    def init(self):
        # self._cr.execute("""DROP FUNCTION IF EXISTS gen_contract_list(contractid int,inspectionmode int) cascade;""")
        # self._cr.execute("""create or replace function gen_contract_list(contractid int,inspectionmode int) returns void as $BODY$
        #  declare
        #    start_date neweb_contract_contract.maintenance_start_date%type;
        #    end_date neweb_contract_contract.maintenance_start_date%type;
        #    start_main_date neweb_contract_contract.maintenance_start_date%type;
        #    sub_main_date neweb_contract_contract.maintenance_start_date%type;
        #    createdate neweb_contract_contract.maintenance_start_date%type;
        #    mycount int;
        #    mysubyear neweb_contract_inspection_list.subscribe_year%type ;
        #    myroutinemaintenancenew int ;
        #  BEGIN
        #    select routine_maintenance_new into myroutinemaintenancenew from neweb_contract_contract where id=contractid ;
        #    if myroutinemaintenancenew = 1 then
        #    elsif myroutinemaintenancenew = 2 then
        #    elsif myroutinemaintenancenew = 3 then
        #    elsif myroutinemaintenancenew = 4 then
        #    end if ;
        #    select maintenance_start_date,maintenance_end_date into start_date,end_date from neweb_contract_contract
        #           where id = contractid ;
        #    mycount := 1;
        #    select now() into createdate ;
        #    select start_date + interval '15 days' into start_main_date ;
        #    select to_char(EXTRACT(year from start_main_date),'FM9999') into mysubyear ;
        #    insert into neweb_contract_inspection_list(inspection_id,subscribe_date,create_date,subscribe_year) values (contractid,start_main_date,createdate,mysubyear);
        #    LOOP
        #     if myroutinemaintenancenew = 1 then
        #       select start_main_date + interval '1 month' into sub_main_date;
        #     elsif myroutinemaintenancenew = 3 then
        #       select start_main_date + interval '2 month' into sub_main_date;
        #     elsif myroutinemaintenancenew = 2 then
        #       select start_main_date + interval '3 month' into sub_main_date;
        #     elsif myroutinemaintenancenew = 4 then
        #       select start_main_date + interval '6 month' into sub_main_date;
        #     end if;
        #     exit when sub_main_date > end_date ;
        #     select to_char(EXTRACT(year from sub_main_date),'FM9999') into mysubyear ;
        #     insert into neweb_contract_inspection_list(inspection_id,subscribe_date,create_date,subscribe_year) values (contractid,sub_main_date,createdate,mysubyear);
        #     mycount := mycount + 1 ;
        #     start_main_date := sub_main_date;
        #   END LOOP;
        #  end; $BODY$
        #  LANGUAGE plpgsql;""")


        self._cr.execute("""DROP FUNCTION IF EXISTS gen_projtocontract(contractid int,projid int) cascade;""")
        self._cr.execute("""create or replace function gen_projtocontract(contractid int,projid int) returns void as $BODY$
          declare
            projname neweb_project.name%type;
            cusname neweb_project.cus_name%type;
            maincusname neweb_project.cus_name%type;
            projsale neweb_project.proj_sale%type;
            mainstartdate neweb_project.main_start_date%type;
            mainenddate neweb_project.main_end_date%type;
            prodmodeltype neweb_projsaleitem.prod_modeltype%type;
            mainrevenue neweb_projanalysis.analysis_revenue%type;
            mainpowerrevenue neweb_projanalysis.analysis_revenue%type;
            refprojcur refcursor ;
            refprojrow record;
            myroutinetype int ;
            myservicetype int ;
            prodnum int ;
            cusproj varchar ;
          begin
            select name,cus_name,main_cus_name,proj_sale,main_start_date,main_end_date,routine_maintenance_new,main_service_rule_new,cus_project into
               projname,cusname,maincusname,projsale,mainstartdate,mainenddate,myroutinetype,myservicetype,cusproj from neweb_project where id=projid;
            select sum(analysis_revenue) into mainrevenue from neweb_projanalysis where analysis_id=projid and analysis_costtype=4 ;
            select sum(analysis_revenue) into mainpowerrevenue from neweb_projanalysis where analysis_id=projid and analysis_costtype=5 ;
            update neweb_contract_contract set project_no=projname,customer_name=cusname,maintenance_start_date=mainstartdate,maintenance_end_date=mainenddate,
                   end_customer=maincusname,sales=projsale,main_cost=mainrevenue,main_manpower_cost=mainpowerrevenue,
                   routine_maintenance_new=myroutinetype,main_service_rule_new=myservicetype,cus_project=cusproj where id=contractid;
            open refprojcur for select * from neweb_projsaleitem where saleitem_id=projid;
            LOOP
              fetch refprojcur into refprojrow;
              exit when not found;
              mainstartdate = refprojrow.neweb_start_date::DATE ;
              mainenddate = refprojrow.neweb_end_date::DATE ;
              prodnum = 1 ;
              loop
                  exit when prodnum > coalesce(refprojrow.prod_num,0) ;
                  insert into neweb_contract_contract_line(contract_id,prod_modeltype,machine_serial_no,contract_start_date,contract_end_date,prod_set,prod_brand,memo,prod_modeltype1)
                  values (contractid,refprojrow.prod_modeltype,refprojrow.prod_serial,mainstartdate,mainenddate,refprojrow.prod_set,refprojrow.prod_brand,refprojrow.prod_desc,refprojrow.prod_modeltype1);
                  prodnum = prodnum + 1 ;
              end loop ;    
            END LOOP;
            close refprojcur;
            end;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS gen_prodsla(contractid int,sla int) cascade;""")
        self._cr.execute("""create or replace function gen_prodsla(contractid int,slaid int) returns void as $BODY$
         declare
            refslacur refcursor;
            refslarow record;
         begin
            open refslacur for select id from neweb_contract_contract_line where contract_id=contractid and prod_sla is null;
            loop
              fetch refslacur into refslarow;
              exit when not found;
              update neweb_contract_contract_line set prod_sla=slaid where id=refslarow.id;
            end loop;
            close refslacur;
         end;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists check_inspection_warn() cascade;""")
        self._cr.execute("""create or replace function check_inspection_warn() returns setof character varying as $BODY$
         DECLARE
           mycurrent_year int;
           mycurrent_month int;
           mycurrent_day int;
           inspection_ref refcursor;
           inspection_row record;
           warn_day int;
         begin
           select date_part('year',current_date) into mycurrent_year;
           select date_part('month',current_date) into mycurrent_month;
           select date_part('day',current_date) into mycurrent_day;
           open inspection_ref for select inspection_id,subscribe_date,actual_date
                from neweb_contract_inspection_list where
                 date_part('year',subscribe_date)=mycurrent_year AND
                 date_part('month',subscribe_date)=mycurrent_month AND
                 inspection_id in (select id from neweb_contract_contract WHERE
                 maintenance_start_date <= current_date and maintenance_end_date >= current_date
                 and inspection_warn=true) and actual_date is null ;
           loop
             fetch inspection_ref into inspection_row;
             exit when not found;
              select inspection_warn_days into warn_day from neweb_contract_contract where id=inspection_row.inspection_id;
              if date_part('day',inspection_row.subscribe_date)=mycurrent_day+warn_day then
               return next inspection_row.inspection_id;
              end if ;
           end loop;
           close inspection_ref;
         end;$BODY$
         LANGUAGE plpgsql;
           """)

        self._cr.execute("""DROP FUNCTION IF EXISTS check_inspection(inspectionid int) cascade;""")
        self._cr.execute("""create or replace function check_inspection(inspectionid int) returns void as $BODY$
          DECLARE
            ncount int;
          begin
            select count(*) into ncount from neweb_contract_inspection_list where inspection_id=inspectionid;
            if ncount = 0 THEN
               update neweb_contract_contract set subscribe_build=FALSE where id=inspectionid;
            ELSE
               update neweb_contract_contract set subscribe_build=TRUE where id=inspectionid;
            end if;
          end;$BODY$
          LANGUAGE plpgsql;
          """)


        self._cr.execute("""drop function if exists getcontractcus() cascade;""")
        self._cr.execute("""create or replace function getcontractcus() returns setof CHARACTER VARYING as $BODY$
              DECLARE 
                 contractcus_cur refcursor;
                 contractcus_rec record;
                 nowtime TIMESTAMP ;
              BEGIN 
                 nowtime := now();
                 open contractcus_cur for select id,end_customer,customer_name from neweb_contract_contract where maintenance_start_date <= nowtime and 
                       maintenance_end_date >= nowtime ;
                 loop
                    fetch contractcus_cur into contractcus_rec ;
                    exit when not found ;
                    return next contractcus_rec.end_customer ; 
                 end loop;
                 close contractcus_cur ; 
              END ;$BODY$
              LANGUAGE plpgsql;        """)

        self._cr.execute("""drop function if exists gen_contract_custom_data(mainduedate Date,contractsales int) cascade;""")
        self._cr.execute("""create or replace function gen_contract_custom_data(mainduedate Date,contractsales int) returns void as $BODY$
              DECLARE 
                 cus_cur refcursor ;
                 cus_rec record ;
                 endcus_cur refcursor ;
                 endcus_rec record ;
                 ncount int;
                 ncount1 int;
                 ncount2 int ;
                 mycontact1 VARCHAR ;
                 mycontact2 DATE ;
                 mycontact3 INTEGER ;
                 mycontact4 INTEGER ;
                 mycontact5 VARCHAR ;
                 mycontact6 VARCHAR ;
                 mycontact7 VARCHAR ;
                 mycontact8 INTEGER ;
                 mycontact12 char ;
                 mycontact13 char ;
                 mywizardid int ;
                 ncount3 int ;
              BEGIN 
                 
                 select max(id) into mywizardid from neweb_contract_excel_export_wizard ;
                 select count(*) into ncount3 from neweb_contract1_hr_employee_rel where wid = mywizardid ;
                /* delete from neweb_contract_custom_excel_data ; */
                 if contractsales=0 THEN 
                    if ncount3 > 0 then
                        insert into neweb_contract_custom_excel_data(contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact12)
                            select A.name,A.maintenance_end_date,A.customer_name,A.sales,
                            B.name as bname,B.email as bemail,B.phone as bphone,A.end_customer,(select getsurveymark(B.survey_mark) as bmark) from neweb_contract_contract A
                            FULL OUTER JOIN res_partner B on A.customer_name=B.parent_id 
                            where   A.maintenance_end_date >= mainduedate and B.active=TRUE and
                            A.id in (select neweb_contract_contract_id from hr_employee_neweb_contract_contract_rel where hr_employee_id in (select eid from neweb_contract1_hr_employee_rel where wid=mywizardid))
                            order by name,bname  ;
                    else 
                        insert into neweb_contract_custom_excel_data(contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact12)
                            select A.name,A.maintenance_end_date,A.customer_name,A.sales,
                            B.name as bname,B.email as bemail,B.phone as bphone,A.end_customer,(select getsurveymark(B.survey_mark) as bmark) from neweb_contract_contract A
                            FULL OUTER JOIN res_partner B on A.customer_name=B.parent_id 
                            where   A.maintenance_end_date >= mainduedate and B.active=TRUE 
                            order by name,bname  ;
                    end if ;       
                 ELSE 
                    if ncount3 > 0 then
                        insert into neweb_contract_custom_excel_data(contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact12)
                            select A.name,A.maintenance_end_date,A.customer_name,A.sales,
                            B.name as bname,B.email as bemail,B.phone as bphone,A.end_customer,(select getsurveymark(B.survey_mark) as bmark) from neweb_contract_contract A
                            FULL OUTER JOIN res_partner B on A.customer_name=B.parent_id 
                            where   A.maintenance_end_date >= mainduedate and B.active=TRUE and
                            A.id in (select neweb_contract_contract_id from hr_employee_neweb_contract_contract_rel where hr_employee_id in (select eid from neweb_contract1_hr_employee_rel where wid=mywizardid))
                            and A.sales=contractsales order by name,bname  ;
                    else 
                         insert into neweb_contract_custom_excel_data(contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact12)
                            select A.name,A.maintenance_end_date,A.customer_name,A.sales,
                            B.name as bname,B.email as bemail,B.phone as bphone,A.end_customer,(select getsurveymark(B.survey_mark) as bmark) from neweb_contract_contract A
                            FULL OUTER JOIN res_partner B on A.customer_name=B.parent_id 
                            where   A.maintenance_end_date >= mainduedate and B.active=TRUE 
                            and A.sales=contractsales order by name,bname  ;
                    end if ;       
                 end if ;
                     
                 open cus_cur for select distinct id from neweb_contract_custom_excel_data where contact3 != contact8 ;
                 loop
                   fetch cus_cur into cus_rec ;
                   exit when not found ;
                   select contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact12 INTO 
                     mycontact1,mycontact2,mycontact3,mycontact4,mycontact5,mycontact6,mycontact7,mycontact8,mycontact12 from 
                     neweb_contract_custom_excel_data where id=cus_rec.id ; 
                   select count(*) into ncount from neweb_contract_custom_excel_data where contact1=mycontact1 and contact3=mycontact3 ;
                   select count(*) into ncount1 from res_partner where parent_id=mycontact8 ;
                   open endcus_cur for select name,email,phone,survey_mark from res_partner where parent_id=mycontact8 ;
                   loop
                     fetch endcus_cur into endcus_rec ;
                     exit when not found ;
                     if endcus_rec.survey_mark=True then 
                           mycontact13 := '*' ;
                        else 
                           mycontact13 := ' ' ;
                        end if ;
                     if ncount > ncount1 THEN
                        
                        update neweb_contract_custom_excel_data set contact9=endcus_rec.name,
                           contact10=endcus_rec.email,contact11=endcus_rec.phone,contact13=mycontact13 where id=
                           (select min(id) from neweb_contract_custom_excel_data where 
                           contact1=mycontact1 and contact9 is null) ;
                     ELSE 
                        select count(*) into ncount2 from neweb_contract_custom_excel_data where contact1=mycontact1 and contact9 is null ;
                        if ncount2=0 THEN 
                           insert into neweb_contract_custom_excel_data (contact1,contact2,contact3,contact4,contact5,contact6,contact7,contact8,contact9,contact10,contact11,contact12)
                           values (mycontact1,mycontact2,mycontact3,mycontact4,mycontact5,mycontact6,mycontact7,mycontact8,endcus_rec.name,endcus_rec.email,endcus_rec.phone,mycontact12)  ;
                        ELSE 
                           update neweb_contract_custom_excel_data set contact9=endcus_rec.name,
                           contact10=endcus_rec.email,contact11=endcus_rec.phone,contact13=mycontact13 where id=
                           (select min(id) from neweb_contract_custom_excel_data where 
                           contact1=mycontact1 and contact9 is null) ;
                        end if ;  
                     end if ;
                   end loop ;
                   close endcus_cur ;
                 end loop;
                 close cus_cur ; 
                 
              END ;$BODY$
              LANGUAGE plpgsql; 
                          """)

        self._cr.execute("""drop function if exists getsurveymark(mysurvey boolean) cascade;""")
        self._cr.execute("""create or replace function getsurveymark(mysurvey boolean) returns char as $BODY$
          DECLARE 
          myres char ;
          BEGIN 
            if mysurvey = TRUE then 
               myres := '*' ;
            else 
               myres := ' ' ;
            end if ;
            return myres ;
          END ;$BODY$
          LANGUAGE plpgsql ;""")

        #self._cr.execute("""alter table neweb_contract_contract_line drop CONSTRAINT neweb_contract_contract_line_contract_machine_serial_no_uniq ;""")


        self._cr.execute("""drop function if exists contractisactive(lineid int) cascade;""")
        self._cr.execute("""create or replace function contractisactive(lineid int) returns Boolean as $BODY$
           DECLARE 
              ncount int ;
              myenddate DATE ;
              mynowdate DATE ;
              myres Boolean ;
           BEGIN 
              select contract_end_date::DATE into myenddate from neweb_contract_contract_line where id = lineid ;
              select now()::DATE into mynowdate ;
              if myenddate >= mynowdate then 
                 myres := TRUE ;
              else 
                 myres := FALSE ;
              end if ;
              return myres ;    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractmainline() cascade""")
        self._cr.execute("""drop function if exists gencontractmainline(contractid int) cascade""")
        self._cr.execute("""create or replace function gencontractmainline(contractid int) returns void as $BODY$
          DECLARE
            con_cur refcursor ;
            con_rec record ;
            nowdate date ;
            ncount int ;
            aename1 varchar ;
            aename varchar ;
            myvat varchar ;
            ae_cur refcursor ;
            ae_rec record ;
          BEGIN
            select now()::DATE into nowdate ;
            delete from neweb_contract_mainline ;
            if contractid = 0 then
                open con_cur for select B.id as conid,B.project_no,B.name,B.customer_name,A.prod_set,A.prod_brand,A.prod_modeltype,A.prod_modeltype1,A.machine_serial_no,A.memo,A.contract_start_date,A.contract_end_date,
                   B.sales,B.is_maintenance_contract,A.contract_id,A.machine_loc,A.prod_sla,B.main_service_rule_new from neweb_contract_contract_line A left join neweb_contract_contract B 
                     on A.contract_id=B.id where nowdate::DATE >= A.contract_start_date::DATE and nowdate::DATE <= A.contract_end_date::DATE
                     order by A.contract_id,A.id ;
            else
                open con_cur for select B.id as conid,B.project_no,B.name,B.customer_name,A.prod_set,A.prod_brand,A.prod_modeltype,A.prod_modeltype1,A.machine_serial_no,A.memo,A.contract_start_date,A.contract_end_date,
                   B.sales,B.is_maintenance_contract,A.contract_id,A.machine_loc,A.prod_sla,B.main_service_rule_new from neweb_contract_contract_line A left join neweb_contract_contract B 
                     on A.contract_id=B.id where  B.id=contractid
                     order by A.contract_id,A.id ;
            end if ;         
            loop
              fetch con_cur into con_rec ;
              exit when not found ;
              aename = ' ';
              select count(*) into ncount from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=con_rec.conid ;
              if ncount > 0 then
                 open ae_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=con_rec.conid ;
                 loop
                    fetch ae_cur into ae_rec ;
                    exit when not found ;
                    select name into aename1 from hr_employee where id=ae_rec.hr_employee_id ;
                    if aename=' ' then
                       aename=aename1 ;
                    else
                       aename=concat(aename,',',aename1) ;
                    end if ;    
                 end loop ;
                 close ae_cur ;
              end if ;
              select coalesce(vat,' ') into myvat from res_partner where id = con_rec.customer_name ;
              insert into neweb_contract_mainline(project_no,contract_no,customer_name,prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,memo,contract_start_date,contract_end_date,sales,ae1,machine_loc,prod_sla,main_service_rule_new,vat) values
                (con_rec.project_no,con_rec.name,con_rec.customer_name,con_rec.prod_set,con_rec.prod_brand,con_rec.prod_modeltype,con_rec.prod_modeltype1,con_rec.machine_serial_no,con_rec.memo,con_rec.contract_start_date,
                 con_rec.contract_end_date,con_rec.sales,aename,con_rec.machine_loc,con_rec.prod_sla,con_rec.main_service_rule_new,myvat) ;
            end loop ;
            close con_cur ;     
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmodeltype1(mt1 varchar) cascade""")
        self._cr.execute("""create or replace function genmodeltype1(mt1 varchar) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
         BEGIN
           myres = 0 ;
           if mt1 != ' ' then
              select count(*) into ncount from neweb_sitem_modeltype1 where name = mt1  and active=True ;
              if ncount > 0 then
                 select max(id) into myres from neweb_sitem_modeltype1 where name = mt1  and active=True ;
              else
                 insert into neweb_sitem_modeltype1(name,active) values (mt1,TRUE) ;
                 select max(id) into myres from neweb_sitem_modeltype1 where name = mt1 and active=True  ;
              end if ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists update_contract_modeltype1(mysn varchar,mymt varchar,mypt varchar,mybd varchar,mymtc varchar,mymemo varchar) cascade""")
        self._cr.execute("""drop function if exists update_contract_modeltype1(mysn varchar,mymt varchar,mypt varchar,mybd varchar,mymtc varchar,mymemo varchar,mymachineloc varchar,myid int) cascade""")
        self._cr.execute("""create or replace function update_contract_modeltype1(mysn varchar,mymt varchar,mypt varchar,mybd varchar,mymtc varchar,mymemo varchar,mymachineloc varchar,myid int) returns void as $BODY$
         DECLARE
           ncount int;
           mymt1 int ;
           myid int ;
           mypt1 int ;
           mybd1 int ; 
         BEGIN
           if mysn != ' '  then
              if mymt != ' ' then
                 select genmodeltype1(mymt) into mymt1 ;
                 if mymt1 > 0 then
                    update neweb_contract_contract_line set prod_modeltype1=mymt1 where machine_serial_no=mysn ;
                 end if ;
              end if ;
              if mypt != ' ' then
                 select id into mypt1 from neweb_prodset where name1=mypt ;
                 if mypt1 is not null then
                    update neweb_contract_contract_line set prod_set=mypt1 where machine_serial_no=mysn ;
                 end if ;
              end if ;
              if mybd != ' ' then
                 select id into mybd1 from neweb_prodbrand where name=mybd and active=TRUE ;
                     if mybd1 is not null then
                        update neweb_contract_contract_line set prod_brand=mybd1 where machine_serial_no=mysn ;
                     end if ;
              end if ;
              if mymtc != ' '  then
                     update neweb_contract_contract_line set prod_modeltype=mymtc where machine_serial_no=mysn ;
              end if ;
              if mymachineloc != ' ' then
                 update neweb_contract_contract_line set machine_loc=mymachineloc where id=myid ;
              end if ;
           end if ;
           
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_sitem_modeltype1() cascade""")
        self._cr.execute("""create or replace function chk_sitem_modeltype1() returns void as $BODY$
         DECLARE
           maxid int ;
           ncount int ;
           m_cur refcursor ;
           m_rec record ;
         BEGIN
           open m_cur for select distinct name from neweb_sitem_modeltype1 where active=TRUE ;
           loop
             fetch m_cur into m_rec ;
             exit when not found ;
             select count(*) into ncount from neweb_sitem_modeltype1 where active=TRUE ;
             if ncount > 1 then
                select max(id) into maxid from neweb_sitem_modeltype1 where name=m_rec.name and active=TRUE ;
                update neweb_sitem_modeltype1 set active=FALSE where name=m_rec.name and id != maxid and active=TRUE ;
             end if ;   
           end loop ;
           close m_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmachineloc() cascade""")
        self._cr.execute("""create or replace function genmachineloc() returns void as $BODY$
         DECLARE
           c_cur refcursor ;
           c_rec record ;
           mystreet varchar ;
         BEGIN
           open c_cur for select id,end_customer from neweb_contract_contract ;
           loop
             fetch c_cur into c_rec ;
             exit when not found ;
             select coalesce(street,' ') into mystreet from res_partner where id = c_rec.end_customer ;
             update neweb_contract_contract_line set machine_loc=mystreet where contract_id=c_rec.id and machine_loc is null ;
           end loop ;
           close c_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gennewcontractline1() cascade""")
        self._cr.execute("""create or replace function gennewcontractline1() returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
         BEGIN
           open l_cur for select * from neweb_contract_contract_line ;
           loop
             fetch l_cur into l_rec;
             exit when not found ;
             insert into neweb_contract_contract_line1(contract_id,prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,rack_loc,warranty_duedate,prod_line_os,contract_line_id) values
              (l_rec.contract_id,l_rec.prod_set,l_rec.prod_brand,l_rec.prod_modeltype,l_rec.prod_modeltype1,l_rec.machine_serial_no,l_rec.rack_loc,l_rec.warranty_duedate,l_rec.prod_line_os,l_rec.id) ;
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")









