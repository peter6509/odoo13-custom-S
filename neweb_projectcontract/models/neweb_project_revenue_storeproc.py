# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class newebprojectrevenuestoreproc(models.Model):
      _name = "neweb_projectcontract.store_proc"


      @api.model
      def init(self):
          self._cr.execute("""drop function if exists gencontractanalysis(contractid int) cascade;""")
          self._cr.execute("""create or replace function gencontractanalysis(contractid int) returns void as $BODY$
            DECLARE
              con_cur cursor is select * from neweb_contract_contract where id=contractid ;
              con_row record;
              pur_cur refcursor ;
              pur_rec record ;
              curtime timestamp := now();
              myid INTEGER ;
              sub_main_date DATE ;
              sub_start_date DATE ;
              sub_end_date DATE ;
              myyear CHAR(4);
              mymonth CHAR(2) ;
              mymainym VARCHAR ;
              myday INTEGER ;
              myday1 int ;
              projectid INTEGER ;
              monthcount INTEGER ;
              proj_man_rev_amount FLOAT ;
              proj_manpower_rev_amount FLOAT ;
              proj_man_cost_amount FLOAT ;
              proj_manpower_cost_amount FLOAT ;
              month_rev_amount FLOAT ;
              month_cost_amount FLOAT ;
              mycount INTEGER ;
              maintype INTEGER ;
              mybalance1 FLOAT ;
              mybalance2 FLOAT ;
              mymaxid1 int ;
              mymaxid2 int ;
              mycontractname varchar ;
            BEGIN
              
              select name into mycontractname from neweb_contract_contract where id = contractid ; 
              delete from neweb_projectcontract_revenue_cost_analysis where contract_no like mycontractname ;
              open con_cur;
              loop
                FETCH con_cur into con_row;
                exit when not found;
                maintype := con_row.routine_maintenance_new ;
                select id into projectid from neweb_project where name=con_row.project_no ;
                execute genprojconstracttemp(projectid) ;
                select coalesce(sum(analysis_revenue),0) into proj_man_rev_amount from neweb_projanalysis where analysis_id=projectid and (analysis_costtype=4 or analysis_costtype=9);
                select coalesce(sum(analysis_revenue),0) into proj_manpower_rev_amount from neweb_projanalysis where analysis_id=projectid and analysis_costtype=5 ;
                select coalesce(sum(analysis_cost),0) into proj_man_cost_amount from neweb_projanalysis where analysis_id=projectid and (analysis_costtype=4 or analysis_costtype=5 or analysis_costtype=9) ;
                select count(*) into mycount from neweb_projsaleitem where saleitem_id=projectid and cost_type=5 ;
                if mycount > 0 then
                   select sum(coalesce(prod_num,0) * coalesce(prod_price,0)) into proj_manpower_cost_amount FROM neweb_projsaleitem where saleitem_id=projectid and cost_type=5 ;
                end if;
                insert into neweb_projectcontract_revenue_cost_analysis(sales_id,contract_no,project_no,customer_name,start_date,end_date,create_date,create_uid)
                    values (con_row.sales,con_row.name,con_row.project_no,con_row.customer_name,con_row.maintenance_start_date,con_row.maintenance_end_date,curtime,1) ;
                select id into myid from neweb_projectcontract_revenue_cost_analysis where contract_no like con_row.contract_no ;
                select extract (day from con_row.maintenance_start_date) into myday ;
                select extract (day from con_row.maintenance_end_date) into myday1 ;
                if myday <= 15 and myday1 <= 15 THEN
                   select date_trunc('month',con_row.maintenance_start_date)::DATE into sub_start_date ;
                   /*select date_trunc('month',con_row.maintenance_end_date)::DATE into sub_end_date;*/
                   select date_trunc('month',con_row.maintenance_end_date - interval '1 month')::DATE into sub_end_date ;
                elsif myday <= 15 and myday1 > 15 then 
                   select date_trunc('month',con_row.maintenance_start_date)::DATE into sub_start_date ;
                   /*select date_trunc('month',con_row.maintenance_end_date)::DATE into sub_end_date;*/
                   select date_trunc('month',con_row.maintenance_end_date)::DATE into sub_end_date ;
                elsif myday > 15 and myday1 <= 15 then 
                   select date_trunc('month',con_row.maintenance_start_date + interval '1 month')::DATE into sub_start_date ;
                   /*select date_trunc('month',con_row.maintenance_end_date)::DATE into sub_end_date;*/
                   select date_trunc('month',con_row.maintenance_end_date - interval '1 month')::DATE into sub_end_date ;
                else
                   select date_trunc('month',con_row.maintenance_start_date + interval '1 month')::DATE into sub_start_date ;
                   select date_trunc('month',con_row.maintenance_end_date)::DATE into sub_end_date ;
                end if;
                sub_main_date := sub_start_date ;
                monthcount := 0 ;
                loop
                  exit when sub_main_date > sub_end_date ;
                  select to_char(extract (year from sub_main_date),'FM0000') into myyear;
                  select to_char(extract (month from sub_main_date),'FM00') into mymonth;
                  mymainym := concat(myyear , '-' , mymonth);
                  insert into neweb_projectcontract_revenue_analysis(revenue_id,revenue_date,itemnum) values (myid,sub_main_date,monthcount+1) ;
                  open pur_cur for select * from neweb_projectcontract_costtemp ;
                  loop
                     fetch pur_cur into pur_rec ;
                     exit when not found ;
                     insert into neweb_projectcontract_cost_analysis(cost_id,cost_date,itemnum,vendor_no,purchase_no,cost_type) values (myid,sub_main_date,monthcount+1,pur_rec.vendor_no,pur_rec.purchase_no,pur_rec.cost_type);
                  end loop ;
                  close pur_cur ;
                  select sub_main_date + interval '1 month' into sub_main_date ;
                  monthcount := monthcount +1 ;
                end loop;
                month_rev_amount := round((coalesce(proj_man_rev_amount,0)+ coalesce(proj_manpower_rev_amount,0)) / monthcount) ;
                month_cost_amount := round((coalesce(proj_man_cost_amount,0) + coalesce(proj_manpower_cost_amount,0)) / monthcount) ;
                mybalance1 := round(coalesce(proj_man_rev_amount,0) - coalesce((month_rev_amount * monthcount),0)) ;
                mybalance2 := round(coalesce(proj_man_cost_amount,0) + coalesce(proj_manpower_cost_amount,0) - coalesce((month_cost_amount   * monthcount),0)) ;
                update neweb_projectcontract_revenue_analysis set revenue_amount=month_rev_amount where revenue_id=myid ;
                /*update neweb_projectcontract_cost_analysis set cost_amount=month_cost_amount where cost_id=myid;*/
              end loop;
              close con_cur;
              if maintype is null then 
                update neweb_projectcontract_revenue_cost_analysis set project_rev_amount=coalesce(proj_man_rev_amount,0)+coalesce(proj_manpower_rev_amount,0),
                    project_cost_amount=coalesce(proj_man_cost_amount,0)  where id = myid ;
              else 
                update neweb_projectcontract_revenue_cost_analysis set project_rev_amount=coalesce(proj_man_rev_amount,0)+coalesce(proj_manpower_rev_amount,0),
                    project_cost_amount=coalesce(proj_man_cost_amount,0),main_type=maintype  where id = myid ;
              end if ;
              select max(id) into mymaxid1 from neweb_projectcontract_revenue_analysis where revenue_id = myid ;
              update neweb_projectcontract_revenue_analysis set revenue_amount= coalesce(revenue_amount,0) + mybalance1 where id = mymaxid1 ;
               open pur_cur for select * from neweb_projectcontract_costtemp ;
               loop
                 fetch pur_cur into pur_rec ;
                 exit when not found ;
                 month_cost_amount := round(coalesce(pur_rec.total_amount,0) / monthcount) ;
                 mybalance2 := round(coalesce(pur_rec.total_amount,0)  - coalesce((month_cost_amount   * monthcount),0)) ; 
                 select max(id) into mymaxid2 from neweb_projectcontract_cost_analysis where cost_id = myid and cost_type = pur_rec.cost_type and purchase_no = pur_rec.purchase_no ;
                 update neweb_projectcontract_cost_analysis set cost_amount= coalesce(month_cost_amount,0) where cost_id = myid and cost_type = pur_rec.cost_type and purchase_no = pur_rec.purchase_no ; 
                 update neweb_projectcontract_cost_analysis set cost_amount= coalesce(month_cost_amount,0) + mybalance2 where id = mymaxid2 ;
               end loop;
               close pur_cur ;
              update neweb_contract_contract set revenue_analysis_mark=TRUE where id=contractid ;
            END;$BODY$
            LANGUAGE plpgsql;
             """)

          self._cr.execute("""drop function if exists getcontractid(myname varchar) cascade;""")
          self._cr.execute("""create or replace function getcontractid(myname varchar) returns int as $BODY$
            DECLARE 
              ncount int ;
              mycontractid int ;
            BEGIN 
              select count(*) into ncount from neweb_contract_contract where name like myname ;
              if ncount > 0 then 
                 select id into mycontractid from neweb_contract_contract where name like myname ;
              else 
                  mycontractid := 0 ;
              end if ;
              return mycontractid ;
            END;$BODY$
            LANGUAGE plpgsql ;""")

          self._cr.execute("""drop function if exists contracthasproject(mycontractid int) cascade;""")
          self._cr.execute("""create or replace function contracthasproject(mycontractid int) returns Boolean as $BODY$
            DECLARE 
              ncount int ;
              myres Boolean ;
              myprojno varchar ;
            BEGIN 
              select coalesce(project_no,' ') into myprojno from neweb_contract_contract where id = mycontractid ;
              if myprojno = ' ' then 
                  myres := FALSE ;
              else
                  select count(*) into ncount from neweb_project where name like myprojno ;
                  if ncount > 0 then 
                     myres := TRUE ;
                  else 
                     myres := FALSE ;
                  end if ;
              end if ;    
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

          self._cr.execute("""drop function if exists genprojconstracttemp(projectid int) cascade;""")
          self._cr.execute("""create or replace function genprojconstracttemp(projectid int) returns void as $BODY$
            DECLARE 
              proj_cur refcursor ;
              proj_rec record ; 
              myvendorid int;
              mycosttypeid int ;
              mytotamount FLOAT ;
              myorderid int ;
            BEGIN 
              delete from neweb_projectcontract_costtemp ;
              open proj_cur for select distinct purchase_no from neweb_projsaleitem where saleitem_id = projectid and purchase_no is not null ;
              loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                select sum(coalesce(prod_num,0) * coalesce(prod_price,0)) into mytotamount from neweb_projsaleitem where saleitem_id = projectid and purchase_no = proj_rec.purchase_no ;
                select id,partner_id,cost_type into myorderid,myvendorid,mycosttypeid from purchase_order where name = proj_rec.purchase_no ;
                if myorderid is not null and myvendorid is not null and mycosttypeid is not null then
                   insert into neweb_projectcontract_costtemp(vendor_no,purchase_no,cost_type,total_amount) values (myvendorid,myorderid,mycosttypeid,mytotamount) ;
                end if ;   
              end loop ;
              close proj_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")




