# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class crmteam_storeproc(models.Model):
    _name = "neweb_sale_analysis.crmteam_storeproc"

    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS crmteam_genline(targetid int) cascade;""")
        self._cr.execute("""create or replace function crmteam_genline(targetid int) returns void as $BODY$
         DECLARE 
            saleteam_cur refcursor;
            saleteam_rec record ;
            ncount int;
            targetgpid int;
            teamid int;
            myresourceid int;
            myempid int;
         BEGIN 
            select team_id into teamid from neweb_sale_analysis_team_targetgp where id = targetid ;
            open saleteam_cur for select id from res_users where sale_team_id=teamid and active=TRUE ; 
            loop
               fetch saleteam_cur into saleteam_rec ;
               exit when not found ;
               select id into myresourceid from resource_resource where user_id=saleteam_rec.id ;
               select id into myempid from hr_employee where resource_id=myresourceid ;
               select count(*) into ncount from neweb_sale_analysis_teammember_targetgp where sales_id=saleteam_rec.id and team_line_id = targetid  ;
               if ncount = 0 THEN 
                  insert into neweb_sale_analysis_teammember_targetgp(team_line_id,sales_id,salesempid) values 
                        (targetid,saleteam_rec.id,myempid) ;
                  insert into neweb_sale_analysis_teammember_utargetgp(team_line_id,sales_id,salesempid) values 
                        (targetid,saleteam_rec.id,myempid) ;      
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'1',myempid);     
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'2',myempid);    
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'3',myempid);   
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                         (targetid,saleteam_rec.id,'4',myempid);       
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'5',myempid);   
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'6',myempid);  
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'7',myempid);  
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'8',myempid);    
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'9',myempid);   
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'10',myempid);  
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'11',myempid); 
                  insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'12',myempid); 
                  insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'Q1',myempid);  
                  insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'Q2',myempid);        
                  insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'Q3',myempid); 
                  insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter,salesempid) VALUES 
                        (targetid,saleteam_rec.id,'Q4',myempid);                                                               
               END if ;        
            end loop;
            close saleteam_cur ; 
            update neweb_sale_analysis_team_targetgp set is_generation=True where id=targetid ;
         END ; $BODY$
         LANGUAGE plpgsql; 
             """)

        self._cr.execute("""DROP FUNCTION IF EXISTS getemp(userid int) cascade;""")
        self._cr.execute("""create or replace function getemp(userid int) returns INTEGER as $BODY$
         DECLARE 
            ncount INTEGER ;
            resourceid INTEGER ;
            empid INTEGER ;
         BEGIN 
         empid := 1;
            select count(*) into ncount from resource_resource where user_id=userid;
            if ncount > 0 THEN
               select id into resourceid from resource_resource where user_id=userid;
               select id into empid from hr_employee where resource_id=resourceid;   
            END if;
            return empid;
         END ;$BODY$
         LANGUAGE plpgsql;
          """)

        self._cr.execute("""DROP FUNCTION IF EXISTS getuserdept(userid int) cascade;""")
        self._cr.execute("""create or replace function getuserdept(userid int) returns INTEGER as $BODY$
         DECLARE 
            ncount INTEGER ;
            resourceid INTEGER ;
            empid INTEGER ;
            deptid int ;
         BEGIN 
         empid := 1;
            select count(*) into ncount from resource_resource where user_id=userid;
            if ncount > 0 THEN
               select id into resourceid from resource_resource where user_id=userid;
               select id,department_id into empid,deptid from hr_employee where resource_id=resourceid ;  
            END if;
            return deptid;
         END ;$BODY$
         LANGUAGE plpgsql;
          """)

        self._cr.execute("""drop function if exists computeday(travelid int) cascade;""")
        self._cr.execute("""create or replace function computeday(travelid int) returns void as $BODY$
          DECLARE 
             nday INTEGER ;
          BEGIN 
             select (travel_end_date - travel_start_date) + 1 into nday from 
                 neweb_sale_analysis_travel_report where id=travelid;
             update neweb_sale_analysis_travel_report set travel_day=nday where id=travelid;
          END ;$BODY$
          LANGUAGE plpgsql;
                """)


        self._cr.execute("""drop function if exists getofficialdate(officialid int) cascade;""")
        self._cr.execute("""create or replace function getofficialdate(officialid int) returns void as $BODY$
          DECLARE 
             ncount INTEGER ;
             mydate VARCHAR ;
             myyear VARCHAR ;
             mymonth VARCHAR ;
             myday VARCHAR ; 
          BEGIN 
             select count(*) into ncount from neweb_sale_analysis_official_doc where id=officialid and doc_date is not null;
             if ncount > 0 THEN 
                select to_char(doc_date,'YYYYMMDD') into mydate from neweb_sale_analysis_official_doc where id = officialid;
                myyear := substr(to_char((to_number(substr(mydate,1,4),'9999') - 1911),'999'),2,3);
                mymonth := substr(mydate,5,2);
                myday := substr(mydate,7,2);
                update neweb_sale_analysis_official_doc set doc_date_y=myyear,doc_date_m=mymonth,doc_date_d=myday
                       where id=officialid ;
             end if;   
          END ; $BODY$
          LANGUAGE plpgsql; 
               """)


        self._cr.execute("""drop function if exists runsaleanalysis(mysaleteam int,mystartdate varchar,myenddate varchar,mysalequarter CHAR) cascade""")
        self._cr.execute("""create or replace function runsaleanalysis(mysaleteam int,mystartdate varchar,myenddate varchar,mysalequarter CHAR) returns void as $BODY$
         DECLARE 
             ncount INTEGER ;
             ncount1 INTEGER ;
             ncount2 INTEGER ;
             project_cur refcursor;
             project_rec record;
             rev_cur refcursor ;
             rev_rec record ;
             myresourceid INTEGER ;
             empid INTEGER ;
             startdate DATE ;
             enddate DATE ;
             projid INTEGER ;
             projsale INTEGER ;
             projname varchar;
             myuserid INTEGER ;
             nmonth INTEGER ;
             nday INTEGER ;
             mymonth varchar;
             myday varchar ;
             mymonthday varchar;
             cusid INTEGER ;
             cusname varchar ;
             targetgpid INTEGER ;
             nyear FLOAT ;
             cyear varchar ;
             sirevenue FLOAT ;
             siprofit FLOAT ;
             siprofitrate FLOAT ;
             servicerevenue FLOAT ;
             serviceprofit FLOAT ;
             servicecost FLOAT ;
             serviceprofitrate FLOAT ;
             servicerevenue1 FLOAT ;
             servicerevenue1ratio FLOAT ;
             serviceprofit1 FLOAT ;
             servicecost1 FLOAT ;
             serviceprofitrate1 FLOAT ;
             prodspec VARCHAR ;
             myid INTEGER ;
             invoicedate DATE ;
             mydivnum1 FLOAT ;
             mydivnum2 FLOAT ;
             mysalesteamid int;
         BEGIN 
             select to_date(mystartdate,'YYYY-MM-DD') into startdate ;
             select to_date(myenddate,'YYYY-MM-DD') into enddate ;
             select EXTRACT(YEAR FROM startdate) into nyear ;
             select to_char(nyear,'FM0000') into cyear ;
             select id into targetgpid from neweb_sale_analysis_team_targetgp where team_id=mysaleteam and team_target_year=cyear ;
             /*update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                       oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                       where  sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
             update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                       oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                       where sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ;     
             update neweb_sale_analysis_teammember_targetgp set teammember_total_q1_gp=0,teammember_total_q2_gp=0,teammember_total_q3_gp=0,teammember_total_q4_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ;     
             update neweb_sale_analysis_team_targetgp set team_total_q1_gp=0,team_total_q2_gp=0,team_total_q3_gp=0,team_total_q4_gp=0 where id=targetgpid ;   */         
                            
           
             open project_cur for select * from neweb_project where create_date::date >= mystartdate::date and create_date::date <= myenddate::date 
                  and proj_sale in (select salesempid from neweb_sale_analysis_teammember_targetgp where team_line_id=targetgpid);
             loop
                fetch project_cur into project_rec ;
                exit when not found ;
                select EXTRACT(MONTH FROM project_rec.create_date) into nmonth ;
                select to_char(nmonth,'FM00') into mymonth ; 
                select EXTRACT(DAY FROM project_rec.create_date) into nday ;
                select to_char(nday,'FM00') into myday ;
                select concat(mymonth,myday) into mymonthday;
                select resource_id into myresourceid from hr_employee where id=project_rec.proj_sale;
                select user_id into myuserid from resource_resource where id = myresourceid ;
                select sale_team_id into mysalesteamid from res_users where id=myuserid ;
                select count(*) into ncount from res_users where sale_team_id=mysaleteam and id=myuserid ;
                select application_date into invoicedate from neweb_invoice_invoiceopen where project_no=project_rec.id ;
                select count(*) into ncount1 from neweb_invoice_invoiceopen where project_no=project_rec.id ;
                select prod_desc into prodspec from neweb_projsaleitem where saleitem_id=project_rec.id and 
                     id = (select min(id) from neweb_projsaleitem where saleitem_id=project_rec.id);
               
                select sum(analysis_revenue),sum(analysis_cost),sum(analysis_profit) into servicerevenue,servicecost,serviceprofit
                     from neweb_projanalysis where analysis_id=project_rec.id and analysis_costtype in (3,4,5);
                select sum(analysis_revenue),sum(analysis_cost),sum(analysis_profit),sum(analysis_revenue * (select getrevenueratio(project_rec.id))) into servicerevenue1,servicecost1,serviceprofit1,servicerevenue1ratio
                     from neweb_projanalysis where analysis_id=project_rec.id and analysis_costtype = 9 ;     
                select count(*) into ncount2 from neweb_sale_analysis_sale_revenuel where 
                         salel_line_id=targetgpid and project_no like project_rec.name and monthday = mymonthday ;  
                if ncount2 > 0 then 
                   if mysaleteam = mysalesteamid then
                       update neweb_sale_analysis_sale_revenuel set oldma_revenue=servicerevenue,oldma_cost=servicecost,oldma_profit=serviceprofit,newma_revenue=servicerevenue1,newma_cost=servicecost1,newma_profit=serviceprofit1,newma_revenue1=servicerevenue1ratio
                         where project_no ilike project_rec.name and salel_line_id=targetgpid and monthday=mymonthday ;   
                   end if ;      
                else 
                   if mysaleteam = mysalesteamid then
                       insert into neweb_sale_analysis_sale_revenuel(salel_line_id,sales_id,monthday,cus_name,prod_name,invoice_date,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_cost,newma_profit,project_no,salesempid,newma_revenue1) VALUES 
                         (targetgpid,myuserid,mymonthday,project_rec.comp_sname,prodspec,project_rec.write_date::date,servicerevenue,servicecost,serviceprofit,servicerevenue1,servicecost1,serviceprofit1,project_rec.name,project_rec.proj_sale,servicerevenue1ratio) ;
                   end if ;      
                end if ;        
           
                select sum(analysis_revenue),sum(analysis_profit) into sirevenue,siprofit from neweb_projanalysis where 
                     analysis_id=project_rec.id and analysis_costtype not in (3,4,5,9);
                if sirevenue = 0 then
                   siprofitrate := 0 ;
                else
                   siprofitrate := (siprofit / sirevenue) ;
                end if ;       
                select count(*) into ncount2 from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and project_no ilike project_rec.name and monthday = mymonthday ;   
                if ncount2 > 0 then
                   if mysaleteam = mysalesteamid then
                       update neweb_sale_analysis_sale_revenuel set si_revenue=sirevenue,si_profit=siprofit,si_profitrate=siprofitrate
                            where project_no ilike project_rec.name and salel_line_id=targetgpid and monthday = mymonthday ;
                   end if ;         
                else 
                   if mysaleteam = mysalesteamid then
                       insert into neweb_sale_analysis_sale_revenuel(salel_line_id,sales_id,monthday,cus_name,prod_name,invoice_date,si_revenue,si_profit,si_profitrate,project_no,salesempid) VALUES 
                            (targetgpid,myuserid,mymonthday,project_rec.comp_sname,prodspec,invoicedate,sirevenue,siprofit,siprofitrate,project_rec.name,project_rec.proj_sale) ;
                   end if ;         
                end if ;       
             end loop;
             close project_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")



        self._cr.execute("""drop function if exists getempnum(userid int) cascade""")
        self._cr.execute("""create or replace function getempnum(userid int) returns VARCHAR as $BODY$
         DECLARE 
             ncount INTEGER ;
             myresourceid int ;
             myempnum VARCHAR ;
         BEGIN 
             select id into myresourceid from resource_resource where user_id=userid ;
             select COALESCE(employee_num,'NO NUM') into myempnum from hr_employee where resource_id=myresourceid ;
             return myempnum ;
         END ;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists calsaleanalysis(mysaleteam int,mystartdate varchar,myenddate varchar,mysalequarter CHAR)""")
        self._cr.execute("""create or replace function calsaleanalysis(mysaleteam int,mystartdate varchar,myenddate varchar,mysalequarter CHAR) returns void as $BODY$
            DECLARE 
               team_cur refcursor ;
               team_rec record ;
               targetgpid INT ;
               mymonth VARCHAR ;
               myquarter VARCHAR ;
               month1revenue FLOAT ;
               month2revenue FLOAT ;
               month3revenue FLOAT ;
               quarterrevenue FLOAT ;
               month1profit FLOAT ;
               month2profit FLOAT ;
               month3profit FLOAT ;
               quarterprofit FLOAT ;
               month1servicerevenue FLOAT ;
               month2servicerevenue FLOAT ;
               month3servicerevenue FLOAT ;
               month3serviceprofit FLOAT ;
               month1serviceprofit FLOAT ;
               month2serviceprofit FLOAT ;
               month1oldmarevenue FLOAT ;
               month2oldmarevenue FLOAT ;
               month3oldmarevenue FLOAT ;
               month1oldmacost FLOAT ;
               month2oldmacost FLOAT ;
               month3oldmacost FLOAT ;
               month1oldmaprofit FLOAT ;
               month2oldmaprofit FLOAT ;
               month3oldmaprofit FLOAT ;
               month1newmarevenue FLOAT ;
               month2newmarevenue FLOAT ;
               month3newmarevenue FLOAT ;
               month1newmarevenue1 FLOAT ;
               month2newmarevenue1 FLOAT ;
               month3newmarevenue1 FLOAT ;
               month1newmacost FLOAT ;
               month2newmacost FLOAT ;
               month3newmacost FLOAT ;
               month1newmaprofit FLOAT ;
               month2newmaprofit FLOAT ;
               month3newmaprofit FLOAT ;
               salesq1gp FLOAT;
               salesq2gp FLOAT;
               salesq3gp FLOAT;
               salesq4gp FLOAT;
               salesyeargp FLOAT ;
               teamq1gp FLOAT;
               teamq2gp FLOAT;
               teamq3gp FLOAT;
               teamq4gp FLOAT;
               teamyeargp FLOAT;
               startdate DATE ;
               enddate DATE ;
               nyear FLOAT ;
               cyear VARCHAR ;
            BEGIN 
               salesq1gp := 0 ;
               salesq2gp := 0 ;
               salesq3gp := 0 ;
               salesq4gp := 0 ;
               salesyeargp := 0 ;
               teamq1gp := 0 ;
               teamq2gp := 0 ;
               teamq3gp := 0 ;
               teamq4gp := 0 ;
               teamyeargp := 0 ;
               myquarter := concat('Q',mysalequarter) ;
               select to_date(mystartdate,'YYYY-MM-DD') into startdate ;
               select to_date(myenddate,'YYYY-MM-DD') into enddate ;
               select EXTRACT(YEAR FROM startdate) into nyear ;
               select to_char(nyear,'FM0000') into cyear ;
               select id into targetgpid from neweb_sale_analysis_team_targetgp where team_id=mysaleteam and team_target_year=cyear ;
               open team_cur for select id from res_users where sale_team_id=mysaleteam ;
               loop
                  fetch team_cur into team_rec ;
                  exit when not found ;
                  if mysalequarter='1' then
                     
                     select coalesce(sum(si_revenue),0) into month1revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(si_revenue),0) into month2revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(si_revenue),0) into month3revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(si_profit),0) into month1profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(si_profit),0) into month2profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(si_profit),0) into month3profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(service_revenue),0) into month1servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(service_revenue),0) into month2servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(service_revenue),0) into month3servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(service_profit),0) into month1serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(service_profit),0) into month2serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(service_profit),0) into month3serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(oldma_revenue),0) into month1oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(oldma_revenue),0) into month2oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(oldma_revenue),0) into month3oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(oldma_cost),0) into month1oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(oldma_cost),0) into month2oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(oldma_cost),0) into month3oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(oldma_profit),0) into month1oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(oldma_profit),0) into month2oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(oldma_profit),0) into month3oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month1newmarevenue,month1newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month2newmarevenue,month2newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month3newmarevenue,month3newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(newma_cost),0) into month1newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(newma_cost),0) into month2newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(newma_cost),0) into month3newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     select coalesce(sum(newma_profit),0) into month1newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='01' ;
                     select coalesce(sum(newma_profit),0) into month2newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='02' ;
                     select coalesce(sum(newma_profit),0) into month3newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='03' ;
                     salesq1gp := month1profit+month2profit+month3profit+month1serviceprofit+month2serviceprofit+month3serviceprofit+month1oldmaprofit+month2oldmaprofit+month3oldmaprofit+
                           month1newmaprofit+month2newmaprofit+month3newmaprofit ;
                     update neweb_sale_analysis_teammember_targetgp set teammember_total_q1_gp=salesq1gp where team_line_id=targetgpid and sales_id=team_rec.id ;      
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month1revenue,si_profit=month1profit,service_revenue=month1servicerevenue,service_profit=month1serviceprofit,
                            oldma_revenue=month1oldmarevenue,oldma_cost=month1oldmacost,oldma_profit=month1oldmaprofit,newma_revenue=month1newmarevenue,newma_revenue1=month1newmarevenue1,newma_cost=month1newmacost,newma_profit=
                            month1newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='1' ;
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month2revenue,si_profit=month2profit,service_revenue=month2servicerevenue,service_profit=month2serviceprofit,
                            oldma_revenue=month2oldmarevenue,oldma_cost=month2oldmacost,oldma_profit=month2oldmaprofit,newma_revenue=month2newmarevenue,newma_revenue1=month2newmarevenue1,newma_cost=month2newmacost,newma_profit=
                            month2newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='2' ;   
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month3revenue,si_profit=month3profit,service_revenue=month3servicerevenue,service_profit=month3serviceprofit,
                            oldma_revenue=month3oldmarevenue,oldma_cost=month3oldmacost,oldma_profit=month3oldmaprofit,newma_revenue=month3newmarevenue,newma_revenue1=month3newmarevenue1,newma_cost=month3newmacost,newma_profit=
                            month3newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='3' ;
                     update neweb_sale_analysis_sale_revenueq set si_revenue=month1revenue+month2revenue+month3revenue,
                            si_profit=month1profit+month2profit+month3profit,service_revenue=month1servicerevenue+month2servicerevenue+month3servicerevenue,
                            service_profit=month1serviceprofit+month2serviceprofit+month3serviceprofit,oldma_revenue=month1oldmarevenue+month2oldmarevenue+month3oldmarevenue,
                            oldma_cost=month1oldmacost+month2oldmacost+month3oldmacost,oldma_profit=month1oldmaprofit+month2oldmaprofit+month3oldmaprofit,
                            newma_revenue=month1newmarevenue+month2newmarevenue+month3newmarevenue,newma_revenue1=month1newmarevenue1+month2newmarevenue1+month3newmarevenue1,newma_cost=month1newmacost+month2newmacost+month3newmacost,
                            newma_profit=month1newmaprofit+month2newmaprofit+month3newmaprofit where 
                            saleq_line_id=targetgpid and sales_id=team_rec.id and sale_quarter='Q1' ;  
                  elsif mysalequarter='2' then
                     select coalesce(sum(si_revenue),0) into month1revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(si_revenue),0) into month2revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(si_revenue),0) into month3revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(si_profit),0) into month1profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(si_profit),0) into month2profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(si_profit),0) into month3profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(service_revenue),0) into month1servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(service_revenue),0) into month2servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(service_revenue),0) into month3servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(service_profit),0) into month1serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(service_profit),0) into month2serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(service_profit),0) into month3serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(oldma_revenue),0) into month1oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(oldma_revenue),0) into month2oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(oldma_revenue),0) into month3oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(oldma_cost),0) into month1oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(oldma_cost),0) into month2oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(oldma_cost),0) into month3oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(oldma_profit),0) into month1oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(oldma_profit),0) into month2oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(oldma_profit),0) into month3oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month1newmarevenue,month1newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month2newmarevenue,month2newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month3newmarevenue,month3newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(newma_cost),0) into month1newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(newma_cost),0) into month2newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(newma_cost),0) into month3newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     select coalesce(sum(newma_profit),0) into month1newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='04' ;
                     select coalesce(sum(newma_profit),0) into month2newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='05' ;
                     select coalesce(sum(newma_profit),0) into month3newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='06' ;
                     salesq2gp := month1profit+month2profit+month3profit+month1serviceprofit+month2serviceprofit+month3serviceprofit+month1oldmaprofit+month2oldmaprofit+month3oldmaprofit+
                           month1newmaprofit+month2newmaprofit+month3newmaprofit ;
                     update neweb_sale_analysis_teammember_targetgp set teammember_total_q2_gp=salesq2gp where team_line_id=targetgpid and sales_id=team_rec.id ;      
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month1revenue,si_profit=month1profit,service_revenue=month1servicerevenue,service_profit=month1serviceprofit,
                            oldma_revenue=month1oldmarevenue,oldma_cost=month1oldmacost,oldma_profit=month1oldmaprofit,newma_revenue=month1newmarevenue,newma_revenue1=month1newmarevenue1,newma_cost=month1newmacost,newma_profit=
                            month1newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='4' ;
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month2revenue,si_profit=month2profit,service_revenue=month2servicerevenue,service_profit=month2serviceprofit,
                            oldma_revenue=month2oldmarevenue,oldma_cost=month2oldmacost,oldma_profit=month2oldmaprofit,newma_revenue=month2newmarevenue,newma_revenue1=month2newmarevenue1,newma_cost=month2newmacost,newma_profit=
                            month2newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='5' ;   
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month3revenue,si_profit=month3profit,service_revenue=month3servicerevenue,service_profit=month3serviceprofit,
                            oldma_revenue=month3oldmarevenue,oldma_cost=month3oldmacost,oldma_profit=month3oldmaprofit,newma_revenue=month3newmarevenue,newma_revenue1=month3newmarevenue1,newma_cost=month3newmacost,newma_profit=
                            month3newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='6' ;
                     update neweb_sale_analysis_sale_revenueq set si_revenue=month1revenue+month2revenue+month3revenue,
                            si_profit=month1profit+month2profit+month3profit,service_revenue=month1servicerevenue+month2servicerevenue+month3servicerevenue,
                            service_profit=month1serviceprofit+month2serviceprofit+month3serviceprofit,oldma_revenue=month1oldmarevenue+month2oldmarevenue+month3oldmarevenue,
                            oldma_cost=month1oldmacost+month2oldmacost+month3oldmacost,oldma_profit=month1oldmaprofit+month2oldmaprofit+month3oldmaprofit,
                            newma_revenue=month1newmarevenue+month2newmarevenue+month3newmarevenue,newma_revenue1=month1newmarevenue1+month2newmarevenue1+month3newmarevenue1,newma_cost=month1newmacost+month2newmacost+month3newmacost,
                            newma_profit=month1newmaprofit+month2newmaprofit+month3newmaprofit where 
                            saleq_line_id=targetgpid and sales_id=team_rec.id and sale_quarter='Q2' ;
                  elsif mysalequarter='3' then
                     select coalesce(sum(si_revenue),0) into month1revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(si_revenue),0) into month2revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(si_revenue),0) into month3revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(si_profit),0) into month1profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(si_profit),0) into month2profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(si_profit),0) into month3profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(service_revenue),0) into month1servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(service_revenue),0) into month2servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(service_revenue),0) into month3servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(service_profit),0) into month1serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(service_profit),0) into month2serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(service_profit),0) into month3serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(oldma_revenue),0) into month1oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(oldma_revenue),0) into month2oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(oldma_revenue),0) into month3oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(oldma_cost),0) into month1oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(oldma_cost),0) into month2oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(oldma_cost),0) into month3oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(oldma_profit),0) into month1oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(oldma_profit),0) into month2oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(oldma_profit),0) into month3oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month1newmarevenue,month1newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month2newmarevenue,month2newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month3newmarevenue,month3newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(newma_cost),0) into month1newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(newma_cost),0) into month2newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(newma_cost),0) into month3newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     select coalesce(sum(newma_profit),0) into month1newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='07' ;
                     select coalesce(sum(newma_profit),0) into month2newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='08' ;
                     select coalesce(sum(newma_profit),0) into month3newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='09' ;
                     salesq3gp := month1profit+month2profit+month3profit+month1serviceprofit+month2serviceprofit+month3serviceprofit+month1oldmaprofit+month2oldmaprofit+month3oldmaprofit+
                           month1newmaprofit+month2newmaprofit+month3newmaprofit ;
                     update neweb_sale_analysis_teammember_targetgp set teammember_total_q3_gp=salesq3gp where team_line_id=targetgpid and sales_id=team_rec.id ;      
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month1revenue,si_profit=month1profit,service_revenue=month1servicerevenue,service_profit=month1serviceprofit,
                            oldma_revenue=month1oldmarevenue,oldma_cost=month1oldmacost,oldma_profit=month1oldmaprofit,newma_revenue=month1newmarevenue,newma_revenue1=month1newmarevenue1,newma_cost=month1newmacost,newma_profit=
                            month1newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='7' ;
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month2revenue,si_profit=month2profit,service_revenue=month2servicerevenue,service_profit=month2serviceprofit,
                            oldma_revenue=month2oldmarevenue,oldma_cost=month2oldmacost,oldma_profit=month2oldmaprofit,newma_revenue=month2newmarevenue,newma_revenue1=month2newmarevenue1,newma_cost=month2newmacost,newma_profit=
                            month2newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='8' ;   
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month3revenue,si_profit=month3profit,service_revenue=month3servicerevenue,service_profit=month3serviceprofit,
                            oldma_revenue=month3oldmarevenue,oldma_cost=month3oldmacost,oldma_profit=month3oldmaprofit,newma_revenue=month3newmarevenue,newma_revenue1=month3newmarevenue1,newma_cost=month3newmacost,newma_profit=
                            month3newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='9' ;
                     update neweb_sale_analysis_sale_revenueq set si_revenue=month1revenue+month2revenue+month3revenue,
                            si_profit=month1profit+month2profit+month3profit,service_revenue=month1servicerevenue+month2servicerevenue+month3servicerevenue,
                            service_profit=month1serviceprofit+month2serviceprofit+month3serviceprofit,oldma_revenue=month1oldmarevenue+month2oldmarevenue+month3oldmarevenue,
                            oldma_cost=month1oldmacost+month2oldmacost+month3oldmacost,oldma_profit=month1oldmaprofit+month2oldmaprofit+month3oldmaprofit,
                            newma_revenue=month1newmarevenue+month2newmarevenue+month3newmarevenue,newma_revenue1=month1newmarevenue1+month2newmarevenue1+month3newmarevenue1,newma_cost=month1newmacost+month2newmacost+month3newmacost,
                            newma_profit=month1newmaprofit+month2newmaprofit+month3newmaprofit where 
                            saleq_line_id=targetgpid and sales_id=team_rec.id and sale_quarter='Q3' ;  
                  elsif mysalequarter='4' then
                     select coalesce(sum(si_revenue),0) into month1revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(si_revenue),0) into month2revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(si_revenue),0) into month3revenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(si_profit),0) into month1profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(si_profit),0) into month2profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(si_profit),0) into month3profit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(service_revenue),0) into month1servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(service_revenue),0) into month2servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(service_revenue),0) into month3servicerevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(service_profit),0) into month1serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(service_profit),0) into month2serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(service_profit),0) into month3serviceprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(oldma_revenue),0) into month1oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(oldma_revenue),0) into month2oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(oldma_revenue),0) into month3oldmarevenue from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(oldma_cost),0) into month1oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(oldma_cost),0) into month2oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(oldma_cost),0) into month3oldmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(oldma_profit),0) into month1oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(oldma_profit),0) into month2oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(oldma_profit),0) into month3oldmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month1newmarevenue,month1newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month2newmarevenue,month2newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(newma_revenue),0),coalesce(sum(newma_revenue1),0) into month3newmarevenue,month3newmarevenue1 from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(newma_cost),0) into month1newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(newma_cost),0) into month2newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(newma_cost),0) into month3newmacost from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     select coalesce(sum(newma_profit),0) into month1newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='10' ;
                     select coalesce(sum(newma_profit),0) into month2newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='11' ;
                     select coalesce(sum(newma_profit),0) into month3newmaprofit from neweb_sale_analysis_sale_revenuel where sales_id=team_rec.id and substr(monthday,1,2)='12' ;
                     salesq4gp := month1profit+month2profit+month3profit+month1serviceprofit+month2serviceprofit+month3serviceprofit+month1oldmaprofit+month2oldmaprofit+month3oldmaprofit+
                           month1newmaprofit+month2newmaprofit+month3newmaprofit ;
                     update neweb_sale_analysis_teammember_targetgp set teammember_total_q4_gp=salesq4gp where team_line_id=targetgpid and sales_id=team_rec.id ;      
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month1revenue,si_profit=month1profit,service_revenue=month1servicerevenue,service_profit=month1serviceprofit,
                            oldma_revenue=month1oldmarevenue,oldma_cost=month1oldmacost,oldma_profit=month1oldmaprofit,newma_revenue=month1newmarevenue,newma_revenue1=month1newmarevenue1,newma_cost=month1newmacost,newma_profit=
                            month1newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='10' ;
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month2revenue,si_profit=month2profit,service_revenue=month2servicerevenue,service_profit=month2serviceprofit,
                            oldma_revenue=month2oldmarevenue,oldma_cost=month2oldmacost,oldma_profit=month2oldmaprofit,newma_revenue=month2newmarevenue,newma_revenue1=month2newmarevenue1,newma_cost=month2newmacost,newma_profit=
                            month2newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='11' ;   
                     update neweb_sale_analysis_sale_revenuem set si_revenue=month3revenue,si_profit=month3profit,service_revenue=month3servicerevenue,service_profit=month3serviceprofit,
                            oldma_revenue=month3oldmarevenue,oldma_cost=month3oldmacost,oldma_profit=month3oldmaprofit,newma_revenue=month3newmarevenue,newma_revenue1=month3newmarevenue1,newma_cost=month3newmacost,newma_profit=
                            month3newmaprofit where sales_id=team_rec.id and salem_line_id=targetgpid and sale_month='12' ;
                     update neweb_sale_analysis_sale_revenueq set si_revenue=month1revenue+month2revenue+month3revenue,
                            si_profit=month1profit+month2profit+month3profit,service_revenue=month1servicerevenue+month2servicerevenue+month3servicerevenue,
                            service_profit=month1serviceprofit+month2serviceprofit+month3serviceprofit,oldma_revenue=month1oldmarevenue+month2oldmarevenue+month3oldmarevenue,
                            oldma_cost=month1oldmacost+month2oldmacost+month3oldmacost,oldma_profit=month1oldmaprofit+month2oldmaprofit+month3oldmaprofit,
                            newma_revenue=month1newmarevenue+month2newmarevenue+month3newmarevenue,newma_revenue1=month1newmarevenue1+month2newmarevenue1+month3newmarevenue1,newma_cost=month1newmacost+month2newmacost+month3newmacost,
                            newma_profit=month1newmaprofit+month2newmaprofit+month3newmaprofit where 
                            saleq_line_id=targetgpid and sales_id=team_rec.id and sale_quarter='Q4' ;    
                  end if ;   
                  update neweb_sale_analysis_sale_revenuem set si_profitrate=(case when si_revenue=0 then 0 else (si_profit/si_revenue) end),
                         service_profitrate=(case when service_revenue=0 then 0 else (service_profit/service_revenue) end) where sales_id=team_rec.id and salem_line_id = targetgpid ;
                  update neweb_sale_analysis_sale_revenueq set si_profitrate=(case when si_revenue=0 then 0 else (si_profit/si_revenue) end),
                         service_profitrate=(case when service_revenue=0 then 0 else (service_profit/service_revenue) end) where sales_id=team_rec.id and saleq_line_id=targetgpid ;       
                  update neweb_sale_analysis_teammember_targetgp set teammember_total_year_gp=teammember_total_q1_gp+teammember_total_q2_gp+teammember_total_q3_gp+teammember_total_q4_gp
                         where team_line_id=targetgpid and sales_id=team_rec.id ;                              
               end loop ;
               close team_cur ;          
               select sum(teammember_total_q1_gp),sum(teammember_total_q2_gp),sum(teammember_total_q3_gp),sum(teammember_total_q4_gp) into
                   teamq1gp,teamq2gp,teamq3gp,teamq4gp from neweb_sale_analysis_teammember_targetgp where team_line_id=targetgpid ;
               teamyeargp := coalesce(teamq1gp,0) + coalesce(teamq2gp,0) + coalesce(teamq3gp,0) + coalesce(teamq4gp,0) ;    
               update neweb_sale_analysis_team_targetgp set team_total_q1_gp=teamq1gp,
                   team_total_q2_gp=teamq2gp,team_total_q3_gp=teamq3gp,team_total_q4_gp=teamq4gp where id=targetgpid ;  
               update neweb_sale_analysis_team_targetgp set team_total_year_gp=teamyeargp
                   where id=targetgpid ;                               
            END;$BODY$
            LANGUAGE plpgsql;   
               """)


        self._cr.execute("""drop function if exists cleansaleteamtarget(mysaleteam int,mystartdate varchar) cascade;""")
        self._cr.execute("""create or replace function cleansaleteamtarget(mysaleteam int,mystartdate varchar) returns void as $BODY$
          DECLARE 
             startdate DATE ;
             enddate DATE ;
             nyear FLOAT ;
             cyear varchar ;
             targetgpid int ;
          BEGIN 
             select to_date(mystartdate,'YYYY-MM-DD') into startdate ;
            
            select EXTRACT(YEAR FROM startdate) into nyear ;
             select to_char(nyear,'FM0000') into cyear ;
             select id into targetgpid from neweb_sale_analysis_team_targetgp where team_id=mysaleteam and team_target_year=cyear ;
            delete from neweb_sale_analysis_sale_revenuel where salel_line_id = targetgpid ; 
              update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                       oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                       where  sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
             update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                       oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                       where sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ;     
             update neweb_sale_analysis_teammember_targetgp set teammember_total_q1_gp=0,teammember_total_q2_gp=0,teammember_total_q3_gp=0,teammember_total_q4_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ;     
             update neweb_sale_analysis_team_targetgp set team_total_q1_gp=0,team_total_q2_gp=0,team_total_q3_gp=0,team_total_q4_gp=0 where id=targetgpid ;            
          END;$BODY$
          language plpgsql;""")

        self._cr.execute("""drop function if exists getrevenueratio(projid int) cascade""")
        self._cr.execute("""create or replace function getrevenueratio(projid int) returns float as $BODY$
          DECLARE 
            myres float ;
          BEGIN 
            select revenue_ratio into myres from neweb_project where id = projid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists resortexpense(expid int) cascade""")
        self._cr.execute("""create or replace function resortexpense(expid int) returns void as $BODY$
         DECLARE 
            exp_cur refcursor ;
            exp_rec record ;
            myitem int ;
         BEGIN 
            myitem = 1 ;
            open exp_cur for select * from neweb_sale_analysis_expense_line where exp_id=expid order by id ;
            loop
              fetch exp_cur into exp_rec ;
              exit when not found ;
              update neweb_sale_analysis_expense_line set seq_item=myitem,nitem=myitem where id = exp_rec.id ;
              myitem = myitem + 1 ;
            end loop ; 
            close exp_cur ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists resortexpense1(expid int) cascade""")
        self._cr.execute("""create or replace function resortexpense1(expid int) returns void as $BODY$
         DECLARE 
            exp_cur refcursor ;
            exp_rec record ;
            myitem int ;
            ncount1 int ;
         BEGIN 
            myitem = 1 ;
            select count(*) into ncount1 from neweb_sale_analysis_expense_line where exp_id=expid and seq_item=0 ;
            if ncount1 > 0 then
                open exp_cur for select * from neweb_sale_analysis_expense_line where exp_id=expid order by id ;
                loop
                  fetch exp_cur into exp_rec ;
                  exit when not found ;
                  update neweb_sale_analysis_expense_line set seq_item=myitem,nitem=myitem where id = exp_rec.id ;
                  myitem = myitem + 1 ;
                end loop ; 
                close exp_cur ;    
            end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists sortallexpense() cascade""")
        self._cr.execute("""create or replace function sortallexpense() returns void as $BODY$
         DECLARE 
          exp_cur refcursor ;
          exp_rec record ;
          expl_cur refcursor ;
          expl_rec record ;
          myitem int ;
         BEGIN 
          open exp_cur for select id from neweb_sale_analysis_expense_report ;
          loop
            fetch exp_cur into exp_rec ;
            exit when not found ;
            myitem = 1 ;
            open expl_cur for select id from neweb_sale_analysis_expense_line where exp_id=exp_rec.id order by 
               sequence,exp_date1,id ;
            loop
               fetch expl_cur into expl_rec ;
               exit when not found ;
               update neweb_sale_analysis_expense_line set sequence=20,nitem=myitem where id=expl_rec.id ;
               myitem = myitem + 1 ;
            end loop ;
            close expl_cur ;   
          end loop ;
          close exp_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setallsequence1() cascade""")
        self._cr.execute("""create or replace function setallsequence1() returns void as $BODY$
           DECLARE
           BEGIN
             update neweb_sale_analysis_expenseevent set sequence=20 where sequence is null ;
             update neweb_sale_analysis_expensedoc set sequence=20 where sequence is null ;
             update neweb_sale_analysis_expenseitem set sequence=20 where sequence is null ;
           END;$BODY$
           LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists genutargetgp() cascade""")
        self._cr.execute("""create or replace function genutargetgp() returns void as $BODY$
           DECLARE
             tar_cur refcursor ;
             tar_rec record ;
             ncount int ;
           BEGIN
             open tar_cur for select team_line_id,sales_id,salesempid from neweb_sale_analysis_teammember_targetgp ;
             loop
               fetch tar_cur into tar_rec ;
               exit when not found ;
               select count(*) into ncount from neweb_sale_analysis_teammember_utargetgp where team_line_id=tar_rec.team_line_id and
                  sales_id=tar_rec.sales_id ;
               if ncount = 0 then
                  insert into neweb_sale_analysis_teammember_utargetgp(team_line_id,sales_id,salesempid) values 
                     (tar_rec.team_line_id,tar_rec.sales_id,tar_rec.salesempid) ;
               end if ;   
             end loop ;
             close tar_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentargetgp(targetid int) cascade""")
        self._cr.execute("""create or replace function gentargetgp(targetid int) returns void as $BODY$
           DECLARE
             ncount int ;
             tar_cur refcursor ;
             tar_rec record ;
             tyeargp float ;
             tq1gp float ;
             tq1magp float ;
             tq1sigp float ;
             tq2gp float ;
             tq2magp float ;
             tq2sigp float ;
             tq3gp float ;
             tq3magp float ;
             tq3sigp float ;
             tq4gp float ;
             tq4magp float ;
             tq4sigp float ;
           BEGIN
             open tar_cur for select * from neweb_sale_analysis_teammember_utargetgp where team_line_id = targetid ;
             loop
               fetch tar_cur into tar_rec;
               exit when not found ;
               update neweb_sale_analysis_teammember_utargetgp set teammember_target_q1_gp = 
                  coalesce(tar_rec.teammember_target_q1_magp,0) + coalesce(tar_rec.teammember_target_q1_sigp,0)
                   where id = tar_rec.id and coalesce(teammember_target_q1_gp,0) = 0 ;
               update neweb_sale_analysis_teammember_utargetgp set teammember_target_q2_gp = 
                  coalesce(tar_rec.teammember_target_q2_magp,0) + coalesce(tar_rec.teammember_target_q2_sigp,0)
                   where id = tar_rec.id and coalesce(teammember_target_q2_gp,0) = 0 ;   
               update neweb_sale_analysis_teammember_utargetgp set teammember_target_q3_gp = 
                  coalesce(tar_rec.teammember_target_q3_magp,0) + coalesce(tar_rec.teammember_target_q3_sigp,0)
                   where id = tar_rec.id and coalesce(teammember_target_q3_gp,0) = 0 ;   
               update neweb_sale_analysis_teammember_utargetgp set teammember_target_q4_gp = 
                  coalesce(tar_rec.teammember_target_q4_magp,0) + coalesce(tar_rec.teammember_target_q4_sigp,0)
                   where id = tar_rec.id and coalesce(teammember_target_q4_gp,0) = 0 ;     
             end loop ;
             close tar_cur ;
             open tar_cur for select * from neweb_sale_analysis_teammember_utargetgp where team_line_id = targetid ;
             loop
               fetch tar_cur into tar_rec;
               exit when not found ;
               update neweb_sale_analysis_teammember_utargetgp set teammember_target_year_gp = 
                  coalesce(tar_rec.teammember_target_q1_gp,0) + coalesce(tar_rec.teammember_target_q2_gp,0) +
                  coalesce(tar_rec.teammember_target_q3_gp,0) + coalesce(tar_rec.teammember_target_q4_gp,0)
                   where id = tar_rec.id and coalesce(teammember_target_year_gp,0) = 0 ;
             end loop ;
             close tar_cur ;
             select sum(coalesce(teammember_target_q1_magp,0)),sum(coalesce(teammember_target_q1_sigp,0)),
                    sum(coalesce(teammember_target_q2_magp,0)),sum(coalesce(teammember_target_q2_sigp,0)),
                    sum(coalesce(teammember_target_q3_magp,0)),sum(coalesce(teammember_target_q3_sigp,0)),
                    sum(coalesce(teammember_target_q4_magp,0)),sum(coalesce(teammember_target_q4_sigp,0)) 
                    into tq1magp,tq1sigp,tq2magp,tq2sigp,tq3magp,tq3sigp,tq4magp,tq4sigp
                   from neweb_sale_analysis_teammember_utargetgp where team_line_id = targetid ;
             update neweb_sale_analysis_team_targetgp set team_target_q1_magp=tq1magp,
                   team_target_q1_sigp=tq1sigp,team_target_q2_magp=tq2magp,team_target_q2_sigp=tq2sigp,
                   team_target_q3_magp=tq3magp,team_target_q3_sigp=tq3sigp,team_target_q4_magp=tq4magp,
                   team_target_q4_sigp=tq4sigp where id = targetid ;  
             update neweb_sale_analysis_team_targetgp set team_target_q1_gp = coalesce(team_target_q1_magp,0) + coalesce(team_target_q1_sigp,0)
                  where id = targetid and coalesce(team_target_q1_gp,0) = 0 ; 
             update neweb_sale_analysis_team_targetgp set team_target_q2_gp = coalesce(team_target_q2_magp,0) + coalesce(team_target_q2_sigp,0)
                  where id = targetid and coalesce(team_target_q2_gp,0) = 0 ;   
             update neweb_sale_analysis_team_targetgp set team_target_q3_gp = coalesce(team_target_q3_magp,0) + coalesce(team_target_q3_sigp,0)
                  where id = targetid and coalesce(team_target_q3_gp,0) = 0 ;  
             update neweb_sale_analysis_team_targetgp set team_target_q4_gp = coalesce(team_target_q4_magp,0) + coalesce(team_target_q4_sigp,0)
                  where id = targetid and coalesce(team_target_q4_gp,0) = 0 ;  
             update neweb_sale_analysis_team_targetgp set team_target_year_gp = coalesce(team_target_q1_gp,0) + coalesce(team_target_q2_gp,0) +
                  coalesce(team_target_q3_gp,0) + coalesce(team_target_q4_gp,0) where id = targetid and coalesce(team_target_year_gp,0) = 0 ; 
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runcfsumline(expid int) cascade""")
        self._cr.execute("""create or replace function runcfsumline(expid int) returns void as $BODY$
           DECLARE
             exp_cur refcursor ;
             exp_rec record ;
             ncount int ;
           BEGIN 
             delete from neweb_sale_analysis_cf_sumline where exp_id=expid;
             update neweb_sale_analysis_cf_sumline set exp_update=False where exp_id=expid ;
             open exp_cur for select * from  neweb_sale_analysis_expense_line where exp_id = expid ;
             loop
               fetch exp_cur into exp_rec ;
               exit when not found ;
               select count(*) into ncount from neweb_sale_analysis_cf_sumline where exp_id=expid and 
                   sumline_exp_item = exp_rec.exp_item ;
               if ncount = 0 then
                  insert into neweb_sale_analysis_cf_sumline(exp_id,sumline_exp_item,sum_tot) values 
                      (expid,exp_rec.exp_item,exp_rec.exp_money) ; 
               else    
                  update neweb_sale_analysis_cf_sumline set sum_tot=coalesce(sum_tot,0)+exp_rec.exp_money
                     where exp_id=expid and sumline_exp_item = exp_rec.exp_item ;
               end if ;      
             end loop ;
             close exp_cur ;
              
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentravelperm(travelid int) cascade""")
        self._cr.execute("""create or replace function gentravelperm(travelid int) returns void as $BODY$
           DECLARE
             opid int ;
             gmember_cur refcursor ;
             gmember_rec record ;
             empid int ;
             ncount int ;
             ncount1 int ;
             userid int ;
             resourceid int ;
           BEGIN
             select user_id into userid from neweb_sale_analysis_travel_report where id = travelid ;
             select id into resourceid from resource_resource where user_id=userid ;
             select id into empid from hr_employee where resource_id = resourceid ;
             select id into opid from neweb_sale_analysis_op_program where op_name='TRAVEL' ;
             open gmember_cur for select id,op_id,leader_man from neweb_sale_analysis_group_member where op_id=opid ;
             loop
                fetch gmember_cur into gmember_rec ;
                exit when not found ;
                select count(*) into ncount from group_member_hr_employee_rel where emp_id=empid and gmember_id=gmember_rec.id ;
                if ncount > 0 then
                   select count(*) into ncount1 from hr_employee_travel_report_rel where emp_id=gmember_rec.leader_man and travel_id=travelid ;
                   if ncount1 = 0 then
                      insert into hr_employee_travel_report_rel(travel_id,emp_id) values (travelid,gmember_rec.leader_man) ;
                   end if ;
                end if ;
             end loop ;
             close gmember_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genexpperm(expid int) cascade""")
        self._cr.execute("""create or replace function genexpperm(expid int) returns void as $BODY$
           DECLARE
             opid int ;
             gmember_cur refcursor ;
             gmember_rec record ;
             empid int ;
             ncount int ;
             ncount1 int ;
           BEGIN
             select emp_no into empid from neweb_sale_analysis_expense_report where id = expid ;
             select id into opid from neweb_sale_analysis_op_program where op_name='EXP' ;
             open gmember_cur for select id,op_id,leader_man from neweb_sale_analysis_group_member where op_id=opid ;
             loop
                fetch gmember_cur into gmember_rec ;
                exit when not found ;
                select count(*) into ncount from group_member_hr_employee_rel where emp_id=empid and gmember_id=gmember_rec.id ;
                if ncount > 0 then
                   select count(*) into ncount1 from hr_employee_expense_report_rel where emp_id=gmember_rec.leader_man and exp_id=expid ;
                   if ncount1 = 0 then
                      insert into hr_employee_expense_report_rel(exp_id,emp_id) values (expid,gmember_rec.leader_man) ;
                   end if ;
                end if ;
             end loop ;
             close gmember_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genexpenseflowman(expid int) cascade""")
        self._cr.execute("""create or replace function genexpenseflowman(expid int) returns void as $BODY$
          DECLARE
            resid int ;
            empid int ;
            userid int;
            flowman1 int ;
            flowman2 int ;
            flowman3 int ;
            flowman4 int ;
            flowman5 int ;
          BEGIN
            select emp_no into empid from neweb_sale_analysis_expense_report where id = expid ;            
           if empid is not null then
              update neweb_sale_analysis_expense_report set flow_owner=empid where id = expid ;
              select flow_man1,flow_man2,flow_man3,flow_man4,flow_man5 into flowman1,flowman2,flowman3,flowman4,flowman5 from hr_employee_postype where emp_id=empid ;
              if flowman1 is not null then
                 update neweb_sale_analysis_expense_report set flow_man1=flowman1,has_man1=1,flow_man5=flowman5 where id = expid ;
              end if ;
              if flowman2 is not null then
                 update neweb_sale_analysis_expense_report set flow_man2=flowman2,has_man2=1,flow_man5=flowman5 where id = expid ;
              end if ;
              if flowman3 is not null then
                 update neweb_sale_analysis_expense_report set flow_man3=flowman3,has_man3=1,flow_man5=flowman5 where id = expid ;
              end if ;
              if flowman4 is not null then
                 update neweb_sale_analysis_expense_report set flow_man4=flowman4,has_man4=1,flow_man5=flowman5 where id = expid ;
              end if ;
           end if ;
          
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentravelflowman(travelid int) cascade""")
        self._cr.execute("""create or replace function gentravelflowman(travelid int) returns void as $BODY$
          DECLARE
            resid int ;
            empid int ;
            userid int;
            flowman1 int ;
            flowman2 int ;
            flowman3 int ;
            flowman4 int ;
            flowman5 int ;
          BEGIN
            select user_id into userid from neweb_sale_analysis_travel_report where id = travelid ;
            select getemp(userid) into empid ;
            
            /* select emp_id into empid from neweb_sale_analysis_travel_report where id = travelid ; */
           if empid is not null then
              update neweb_sale_analysis_travel_report set flow_owner=empid where id = travelid ;
              select flow_man1,flow_man2,flow_man3,flow_man4,flow_man5 into flowman1,flowman2,flowman3,flowman4,flowman5 from hr_employee_postype where emp_id=empid ;
              if flowman1 is not null then
                 update neweb_sale_analysis_travel_report set flow_man1=flowman1,has_man1=1,flow_man5=flowman5 where id = travelid ;
              end if ;
              if flowman2 is not null then
                 update neweb_sale_analysis_travel_report set flow_man2=flowman2,has_man2=1,flow_man5=flowman5 where id = travelid ;
              end if ;
              if flowman3 is not null then
                 update neweb_sale_analysis_travel_report set flow_man3=flowman3,has_man3=1,flow_man5=flowman5 where id = travelid ;
              end if ;
              if flowman4 is not null then
                 update neweb_sale_analysis_travel_report set flow_man4=flowman4,has_man4=1,flow_man5=flowman5 where id = travelid ;
              end if ;
              update neweb_sale_analysis_travel_report set emp_id=empid,flow_owner=empid,flow_man5=flowman5 where id = travelid ;
           end if ;

          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genalltravelflowman() cascade""")
        self._cr.execute("""create or replace function genalltravelflowman() returns void as $BODY$
         DECLARE
           t_cur refcursor ;
           t_rec record ;
         BEGIN
           open t_cur for select * from neweb_sale_analysis_travel_report ;
           loop
             fetch t_cur into t_rec ;
             exit when not found ;
             execute gentravelflowman(t_rec.id) ;
           end loop ;
           close t_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists explineitem(expid int) cascade;""")
        self._cr.execute("""create or replace function explineitem(expid int) returns void as $BODY$
           DECLARE 
             ncount int;
             expline_cur refcursor ;
             expline_rec record ;
             myitem int ;
           BEGIN
                myitem = 1 ; 
                open expline_cur for select id,exp_id,sequence from neweb_sale_analysis_expense_line where exp_id = expid order by seq_item ;
                loop
                  fetch expline_cur into expline_rec ;
                  exit when not found ;
                  update neweb_sale_analysis_expense_line set seq_item=myitem::numeric,nitem=myitem where id = expline_rec.id ;
                  myitem = myitem + 1 ;
                end loop ;
                close expline_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists explineitem1(expid int) cascade;""")
        self._cr.execute("""create or replace function explineitem1(expid int) returns void as $BODY$
           DECLARE 
             ncount int;
             expline_cur refcursor ;
             expline_rec record ;
             myitem int ;
           BEGIN
                myitem = 1 ; 
                open expline_cur for select id,exp_id,sequence from neweb_sale_analysis_expense_line where exp_id = expid order by sequence,id ;
                loop
                  fetch expline_cur into expline_rec ;
                  exit when not found ;
                  update neweb_sale_analysis_expense_line set seq_item=myitem::numeric,nitem=myitem where id = expline_rec.id ;
                  myitem = myitem + 1 ;
                end loop ;
                close expline_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallseqitem() cascade""")
        self._cr.execute("""create or replace function genallseqitem() returns void as $BODY$
          DECLARE
            exp_cur refcursor ;
            exp_rec record ;
          BEGIN
            open exp_cur for select id from neweb_sale_analysis_expense_report ;
            loop
              fetch exp_cur into exp_rec ;
              exit when not found ;
              execute explineitem1(exp_rec.id) ;
            end loop ;
            close exp_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentravelcoman() cascade""")
        self._cr.execute("""create or replace function gentravelcoman() returns void as $BODY$
         DECLARE
           t_cur refcursor ;
           t_rec record ;
           e_cur refcursor ;
           e_rec record ;
           nnum int ;
         BEGIN
           open t_cur for select id from neweb_sale_analysis_travel_report ;
           loop
             fetch t_cur into t_rec ;
             exit when not found ;
             update neweb_sale_analysis_travel_report set co_man1=null,co_man2=null,co_man3=null,co_man4=null,co_man5=null where id=t_rec.id ;
             nnum=1 ;
             open e_cur for select * from hr_employee_neweb_sale_analysis_travel_report_rel where neweb_sale_analysis_travel_report_id=t_rec.id ;
             loop
                fetch e_cur into e_rec ;
                exit when not found ;
                if nnum=1 then
                   update neweb_sale_analysis_travel_report set co_man1=e_rec.hr_employee_id where id=t_rec.id  ;
                elsif nnum=2 then
                   update neweb_sale_analysis_travel_report set co_man2=e_rec.hr_employee_id where id=t_rec.id ;
                elsif nnum=3 then
                   update neweb_sale_analysis_travel_report set co_man3=e_rec.hr_employee_id where id=t_rec.id ;
                elsif nnum=4 then
                   update neweb_sale_analysis_travel_report set co_man4=e_rec.hr_employee_id where id=t_rec.id  ;
                else
                   update neweb_sale_analysis_travel_report set co_man5=e_rec.hr_employee_id where id=t_rec.id  ;
                end if ;
                nnum = nnum + 1 ;
             end loop ;
             close e_cur ;
           end loop ;
           close t_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""update neweb_sale_analysis_travel_report set flow_man5=1322 ;""")
        self._cr.execute("""update neweb_sale_analysis_expense_report set flow_man5=1322 ;""")



