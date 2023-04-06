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
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'1');     
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'2');    
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'3');   
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                 (targetid,saleteam_rec.id,'4');       
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'5');   
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'6');  
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'7');  
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'8');    
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'9');   
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'10');  
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'11'); 
                          insert into neweb_sale_analysis_sale_revenuem(salem_line_id,sales_id,sale_month) VALUES 
                                (targetid,saleteam_rec.id,'12'); 
                          insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter) VALUES 
                                (targetid,saleteam_rec.id,'Q1');  
                          insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter) VALUES 
                                (targetid,saleteam_rec.id,'Q2');        
                          insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter) VALUES 
                                (targetid,saleteam_rec.id,'Q3'); 
                          insert into neweb_sale_analysis_sale_revenueq(saleq_line_id,sales_id,sale_quarter) VALUES 
                                (targetid,saleteam_rec.id,'Q4');                                                               
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
                       select id into empid from hr_emplayee where resource_id=resourceid;   
                    END if;
                    return empid;
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
                     if mysalequarter='1' then
                        update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_month in ('1','2','3') and sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
                        update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_quarter='Q1' and sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ;  
                        update neweb_sale_analysis_teammember_targetgp set teammember_total_q1_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ;     
                        update neweb_sale_analysis_team_targetgp set team_total_q1_gp=0 where id=targetgpid ;      
                     elsif mysalequarter ='2' then 
                        update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_month in ('4','5','6') and sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
                        update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_quarter='Q2' and sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ;    
                        update neweb_sale_analysis_teammember_targetgp set teammember_total_q2_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ; 
                        update neweb_sale_analysis_team_targetgp set team_total_q2_gp=0 where id=targetgpid ;              
                     elsif mysalequarter = '3' then 
                        update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_month in ('7','8','9') and sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
                        update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_quarter='Q3' and sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ;  
                        update neweb_sale_analysis_teammember_targetgp set teammember_total_q3_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ;
                        update neweb_sale_analysis_team_targetgp set team_total_q3_gp=0 where id=targetgpid ;          
                     elsif mysalequarter = '4' then
                        update neweb_sale_analysis_sale_revenuem set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_month in ('10','11','12') and sales_id in (select id from res_users where sale_team_id=mysaleteam) and salem_line_id=targetgpid ;
                        update neweb_sale_analysis_sale_revenueq set si_revenue=0,si_profit=0,si_profitrate=0,service_revenue=0,service_profit=0,service_profitrate=0,
                               oldma_revenue=0,oldma_cost=0,oldma_profit=0,newma_revenue=0,newma_cost=0,newma_profit=0 
                               where sale_quarter='Q4' and sales_id in (select id from res_users where sale_team_id=mysaleteam) and saleq_line_id=targetgpid ; 
                        update neweb_sale_analysis_teammember_targetgp set teammember_total_q4_gp=0 where team_line_id=targetgpid and sales_id in (select id from res_users where sale_team_id=mysaleteam) ;   
                        update neweb_sale_analysis_team_targetgp set team_total_q4_gp=0 where id=targetgpid ;               
                     end if ;
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
                             from neweb_projanalysis where analysis_id=project_rec.id and analysis_costtype in (3,4,5,9);
                        select count(*) into ncount2 from neweb_sale_analysis_sale_revenuel where 
                                 salel_line_id=targetgpid and project_no like project_rec.name and monthday = mymonthday ;  
                        if ncount2 > 0 then 
                           if mysaleteam = mysalesteamid then
                               update neweb_sale_analysis_sale_revenuel set oldma_revenue=servicerevenue,oldma_cost=servicecost,oldma_profit=serviceprofit
                                 where project_no ilike project_rec.name and salel_line_id=targetgpid and monthday=mymonthday ;   
                           end if ;      
                        else 
                           if mysaleteam = mysalesteamid then
                               insert into neweb_sale_analysis_sale_revenuel(salel_line_id,sales_id,monthday,cus_name,prod_name,invoice_date,oldma_revenue,oldma_cost,oldma_profit,project_no) VALUES 
                                 (targetgpid,myuserid,mymonthday,project_rec.comp_sname,prodspec,project_rec.write_date::date,servicerevenue,servicecost,serviceprofit,project_rec.name) ;
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
                               insert into neweb_sale_analysis_sale_revenuel(salel_line_id,sales_id,monthday,cus_name,prod_name,invoice_date,si_revenue,si_profit,si_profitrate,project_no) VALUES 
                                    (targetgpid,myuserid,mymonthday,project_rec.comp_sname,prodspec,invoicedate,sirevenue,siprofit,siprofitrate,project_rec.name) ;
                           end if ;         
                        end if ;       
                     end loop;
                     close project_cur ;
                     if mysalequarter='1' then
                        open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0101' and monthday <= '0331' ;
                        loop
                          fetch rev_cur into rev_rec;
                          exit when not found ;
                          if substr(rev_rec.monthday,1,2)='01' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                    oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='1' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                                   
                          end if ;
                          if substr(rev_rec.monthday,1,2)='02' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                    oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='2' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='03' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                    oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='3' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          update neweb_sale_analysis_sale_revenueq set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                              oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.cost,oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                              newma_cost=newma_cost+rev_rec.newma_cost,newma_profit=newma_profit+rev_rec.newma_profit 
                              where saleq_line_id=rev_rec.salel_line_id
                               and sale_quarter='Q1' and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_teammember_targetgp set teammember_total_q1_gp=teammember_total_q1_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where team_line_id=rev_rec.salel_line_id and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_team_targetgp set team_total_q1_gp=team_total_q1_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where id=rev_rec.salel_line_id ;  
                          update neweb_sale_analysis_sale_revenuel set si_profitrate = (si_profit / si_revenue) where id = rev_rec.id and si_revenue > 0 ;
                          update neweb_sale_analysis_sale_revenuel set service_profitrate = (service_profit/service_revenue) where id = rev_rec.id and service_revenue > 0 ;
                        end loop ;
                        close rev_cur ;
                        update neweb_sale_analysis_sale_revenuem set si_profitrate=(si_profit/si_revenue) where sale_month in ('1','2','3') and salem_line_id=rev_rec.salel_line_id and si_revenue > 0 ;
                        update neweb_sale_analysis_sale_revenuem set service_profitrate=(service_profit/service_revenue) where sale_month in ('1','2','3') and salem_line_id=rev_rec.salel_line_id and service_revenue > 0 ;
                        update neweb_sale_analysis_sale_revenueq set si_profitrate=(si_profit/si_revenue) where sale_quarter='Q1' and saleq_line_id = rev_rec.salel_line_id and si_revenue > 0 ;
                        update neweb_sale_analysis_sale_revenueq set service_profitrate=(service_profit/service_revenue) where sale_quarter='Q1' and saleq_line_id = rev_rec.salel_line_id ;
                     elsif mysalequarter='2' then 
                        open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0401' and monthday <= '0630' ;
                        loop
                          fetch rev_cur into rev_rec ;
                          exit when not found ;
                          if substr(rev_rec.monthday,1,2)='04' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='4' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='05' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='5' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='06' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                    oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='6' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          update neweb_sale_analysis_sale_revenueq set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                 oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.cost,oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                                 newma_cost=newma_cost+rev_rec.newma_cost,newma_profit=newma_profit+rev_rec.newma_profit 
                                 where saleq_line_id=rev_rec.salel_line_id and sale_quarter='Q2' and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_teammember_targetgp set teammember_total_q2_gp=teammember_total_q2_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where team_line_id=rev_rec.salel_line_id and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_team_targetgp set team_total_q2_gp=team_total_q2_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where id=rev_rec.salel_line_id ;  
                          update neweb_sale_analysis_sale_revenuel set si_profitrate = (si_profit / si_revenue) where id = rev_rec.id and si_revenue > 0;
                          update neweb_sale_analysis_sale_revenuel set service_profitrate = (service_profit/service_revenue) where id = rev_rec.id and service_revenue > 0 ;
                        end loop;
                        close rev_cur;
                        update neweb_sale_analysis_sale_revenuem set si_profitrate=(si_profit/si_revenue) where sale_month in ('4','5','6') and salem_line_id=targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenuem set service_profitrate=(service_profit/service_revenue) where sale_month in ('4','5','6') and salem_line_id=targetgpid and service_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set si_profitrate=(si_profit/si_revenue) where sale_quarter='Q2' and saleq_line_id = targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set service_profitrate=(service_profit/service_revenue) where sale_quarter='Q2' and saleq_line_id = targetgpid and service_revenue > 0 ;
                     elsif mysalequarter='3' then 
                        open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0701' and monthday <= '0930' ;
                         loop
                          fetch rev_cur into rev_rec;
                          exit when not found ;
                          if substr(rev_rec.monthday,1,2)='07' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='7' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='08' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='8' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='09' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='9' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          update neweb_sale_analysis_sale_revenueq set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                 oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.cost,oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                                 newma_cost=newma_cost+rev_rec.newma_cost,newma_profit=newma_profit+rev_rec.newma_profit
                                 where saleq_line_id=rev_rec.salel_line_id and sale_quarter='Q3' and sales_id=rev_rec.sales_id ;
       
                          update neweb_sale_analysis_teammember_targetgp set teammember_total_q3_gp=teammember_total_q3_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where
                                team_line_id=rev_rec.salel_line_id and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_team_targetgp set team_total_q3_gp=team_total_q3_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit where
                                id=rev_rec.salel_line_id  ; 
                         update neweb_sale_analysis_sale_revenuel set si_profitrate = (si_profit / si_revenue) where id = rev_rec.id and si_revenue > 0 ;
                         update neweb_sale_analysis_sale_revenuel set service_profitrate = (service_profit/service_revenue) where id = rev_rec.id and service_revenue > 0 ;        
                        end loop;
                        close rev_cur;
                        update neweb_sale_analysis_sale_revenuem set si_profitrate=(si_profit/si_revenue) where sale_month in ('7','8','9') and salem_line_id=targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenuem set service_profitrate=(service_profit/service_revenue) where sale_month in ('7','8','9') and salem_line_id=targetgpid and service_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set si_profitrate=(si_profit/si_revenue) where sale_quarter='Q3' and saleq_line_id = targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set service_profitrate=(service_profit/service_revenue) where sale_quarter='Q3' and saleq_line_id = targetgpid and service_revenue > 0;
                     else
                        open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '1001' and monthday <= '1231' ;
                         loop
                          fetch rev_cur into rev_rec;
                          exit when not found ;
                          if substr(rev_rec.monthday,1,2)='10' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='10' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='11' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='11' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          if substr(rev_rec.monthday,1,2)='12' then
                             update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                    service_profit=rev_rec.service_profit,oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+
                                    rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit where sale_month='12' and sales_id=rev_rec.sales_id and salem_line_id=targetgpid ;
                          end if ;
                          update neweb_sale_analysis_sale_revenueq set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,service_revenue=service_revenue+rev_rec.service_revenue,
                                 oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                                 newma_profit=newma_profit+rev_rec.newma_profit,newma_cost=newma_cost+rev_rec.newma_cost
                                 where saleq_line_id=rev_rec.salel_line_id and sale_quarter='Q4' and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_teammember_targetgp set teammember_total_q4_gp=teammember_total_q4_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit+rev_rec.newma_profit where
                                team_line_id=rev_rec.salel_line_id and sales_id=rev_rec.sales_id ;
                          update neweb_sale_analysis_team_targetgp set team_total_q4_gp=team_total_q4_gp+rev_rec.si_profit+rev_rec.service_profit+rev_rec.oldma_profit+rev_rec.newma_profit where id=rev_rec.salel_line_id  ; 
                          update neweb_sale_analysis_sale_revenuel set si_profitrate = (si_profit / si_revenue) where id = rev_rec.id and si_revenue > 0;
                          update neweb_sale_analysis_sale_revenuel set service_profitrate = (service_profit/service_revenue) where id = rev_rec.id and service_revenue > 0 ;
                        end loop;
                        close rev_cur ;
                        update neweb_sale_analysis_sale_revenuem set si_profitrate=(si_profit/si_revenue) where sale_month in ('10','11','12') and salem_line_id=targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenuem set service_profitrate=(service_profit/service_revenue) where sale_month in ('10','11','12') and salem_line_id=targetgpid and service_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set si_profitrate=(si_profit/si_revenue) where sale_quarter='Q4' and saleq_line_id = targetgpid and si_revenue > 0;
                        update neweb_sale_analysis_sale_revenueq set service_profitrate=(service_profit/service_revenue) where sale_quarter='Q4' and saleq_line_id = targetgpid and service_revenue > 0;
                    end if ;
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
                           rev_cur refcursor ;
                           rev_rec record ;
                           startdate DATE ;
                           enddate DATE ;
                           nyear FLOAT ;
                           cyear VARCHAR ;
                           targetgpid INT ;
                           mymonth VARCHAR ;
                           myquarter VARCHAR ;
                        BEGIN
                           select to_date(mystartdate,'YYYY-MM-DD') into startdate ;
                           select to_date(myenddate,'YYYY-MM-DD') into enddate ;
                           select EXTRACT(YEAR FROM startdate) into nyear ;
                           select to_char(nyear,'FM0000') into cyear ;
                           select id into targetgpid from neweb_sale_analysis_team_targetgp where team_id=mysaleteam and team_target_year=cyear ;
                           if mysalequarter = '1' THEN 
                              open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0101' and monthday <= '0331' ;
                           elsif mysalequarter = '2' THEN 
                              open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0401' and monthday <= '0630' ;
                           elsif mysalequarter = '3' THEN 
                              open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '0701' and monthday <= '0930' ;
                           elsif mysalequarter = '4' THEN 
                              open rev_cur for select * from neweb_sale_analysis_sale_revenuel where salel_line_id=targetgpid and monthday >= '1001' and monthday <= '1231' ;
                           end if ;
                           loop
                              fetch rev_cur into rev_rec ;
                              exit when not found ;
                              mymonth := substr(rev_rec.monthday,1,2) ;
                              if substr(mymonth,1,1) = '0' THEN 
                                 mymonth = substr(rev_rec.monthday,2,1);
                              end if ;   
                              myquarter = concat('Q',mysalequarter) ;
                              update neweb_sale_analysis_sale_revenuem set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,
                                     service_revenue=service_revenue+rev_rec.service_revenue,service_profit=service_profit+rev_rec.service_profit,
                                     oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                     oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                                     newma_cost=newma_cost+rev_rec.newma_cost,newma_profit=newma_profit+rev_rec.newma_profit where sales_id=rev_rec.sales_id AND 
                                     sale_month like mymonth and salem_line_id=targetgpid ;
                              update neweb_sale_analysis_sale_revenueq set si_revenue=si_revenue+rev_rec.si_revenue,si_profit=si_profit+rev_rec.si_profit,
                                     service_revenue=service_revenue+rev_rec.service_revenue,service_profit=service_profit+rev_rec.service_profit,
                                     oldma_revenue=oldma_revenue+rev_rec.oldma_revenue,oldma_cost=oldma_cost+rev_rec.oldma_cost,
                                     oldma_profit=oldma_profit+rev_rec.oldma_profit,newma_revenue=newma_revenue+rev_rec.newma_revenue,
                                     newma_cost=newma_cost+rev_rec.newma_cost,newma_profit=newma_profit+rev_rec.newma_profit where sales_id=rev_rec.sales_id AND 
                                     sale_quarter like myquarter and saleq_line_id=targetgpid ;   
                              if mysalequarter='1' THEN 
                                     update neweb_sale_analysis_teammember_targetgp set teammember_total_year_gp=teammember_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            teammember_total_q1_gp=teammember_total_q1_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue 
                                            where team_line_id = targetgpid and sales_id = rev_rec.sales_id ;
                                     update neweb_sale_analysis_team_targetgp set team_total_year_gp=team_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            team_total_q1_gp = team_total_q1_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue  
                                             where team_id=targetgpid ;       
                              elsif mysalequarter='2' THEN 
                                     update neweb_sale_analysis_teammember_targetgp set teammember_total_year_gp=teammember_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            teammember_total_q2_gp=teammember_total_q2_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue 
                                            where team_line_id = targetgpid and sales_id = rev_rec.sales_id ;
                                      update neweb_sale_analysis_team_targetgp set team_total_year_gp=team_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            team_total_q2_gp = team_total_q2_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue  
                                             where team_id=targetgpid ;       
                              elsif mysalequarter='3' THEN 
                                     update neweb_sale_analysis_teammember_targetgp set teammember_total_year_gp=teammember_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            teammember_total_q3_gp=teammember_total_q3_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue 
                                            where team_line_id = targetgpid and sales_id = rev_rec.sales_id ;
                                      update neweb_sale_analysis_team_targetgp set team_total_year_gp=team_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            team_total_q3_gp = team_total_q3_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue  
                                             where team_id=targetgpid ;       
                              elsif mysalequarter='4' then 
                                     update neweb_sale_analysis_teammember_targetgp set teammember_total_year_gp=teammember_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            teammember_total_q4_gp=teammember_total_q4_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue 
                                            where team_line_id = targetgpid and sales_id = rev_rec.sales_id ;
                                      update neweb_sale_analysis_team_targetgp set team_total_year_gp=team_total_year_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue,
                                            team_total_q4_gp = team_total_q4_gp + rev_rec.si_revenue + rev_rec.service_revenue + rev_rec.oldma_revenue + rev_rec.newma_revenue  
                                             where team_id=targetgpid ;       
                              end if ;                        
                           end loop ;
                           close rev_cur ;
                        END;$BODY$
                        LANGUAGE plpgsql;   
                           """)

