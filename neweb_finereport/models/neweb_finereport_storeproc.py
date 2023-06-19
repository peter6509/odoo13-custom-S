# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,tools
from odoo.exceptions import UserError

class newebsalesima(models.Model):
    _name = "neweb_finereport.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getprojyear(projid int) cascade""")
        self._cr.execute("""create or replace function getprojyear(projid int) returns varchar as $$
        declare
          myyear varchar;
          projdate date ;
        begin
          select create_date into projdate from neweb_project where id = projid;
          select date_part('year',projdate)::TEXT into myyear;
          return myyear ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getsinum(projid int) cascade""")
        self._cr.execute("""create or replace function getsinum(projid int) returns INT as $$
        declare
            mynum int;
            ncount int;
            ncount1 int;
            sinum int ;
            manum int ;
        begin
            select count(*) into ncount from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7); /* 買賣,建置,租賃,專案合作*/
            select count(*) into ncount1 from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9); /* 維護舊約,維護新約 */
            if ncount >0 and ncount1 = 0 then
               mynum = 1 ;
            elsif ncount > 0 and ncount1 > 0 then
               select sum(analysis_revenue) into sinum from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7); /* 買賣,建置,租賃,專案合作*/
               select sum(analysis_revenue) into manum from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9); /* 維護舊約,維護新約 */
               if sinum > manum then
                 mynum = 1 ;
               else
                 mynum = 0 ;      
               end if ;
            else
                mynum = 0 ;
            end if ;   
            return mynum ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getmanum(projid int) cascade""")
        self._cr.execute("""create or replace function getmanum(projid int) returns INT as $$
        declare
            mynum int;
            ncount int;
            ncount1 int;
            sinum int ;
            manum int ;
        begin
            select count(*) into ncount from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7); /* 買賣,建置,租賃,專案合作*/
            select count(*) into ncount1 from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9); /* 維護舊約,維護新約 */
            if ncount = 0 and ncount1 > 0 then
               mynum = 1 ;
            elsif ncount > 0 and ncount1 > 0 then
               select sum(analysis_revenue) into sinum from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7); /* 買賣,建置,租賃,專案合作*/
               select sum(analysis_revenue) into manum from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9); /* 維護舊約,維護新約 */
               if manum > sinum then
                 mynum = 1 ;
               else
                 mynum = 0 ;      
               end if ;
            else
                mynum = 0 ;
            end if ;   
            return mynum ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getsimatot(projid int) cascade""")
        self._cr.execute("""create or replace function getsimatot(projid int) returns INT as $$
        declare
           ncount int ;
           mynum int ;
        begin 
           select count(*) into ncount from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,4,7,9) ; 
           if ncount is null then
              mynum = 0 ;
           else
              mynum = 1 ;
           end if ;
           return mynum ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getprojym(projid int) cascade""")
        self._cr.execute("""create or replace function getprojym(projid int) returns varchar as $$
        declare
            myym varchar;
            myy varchar;
            mym varchar;
            projdate date ;
        begin   
            if projid is not null then
                select create_date into projdate from neweb_project where id = projid;
                select date_part('year',projdate)::TEXT into myy;
                select lpad(date_part('month',projdate)::TEXT,2,'0') into mym;
                myym = concat(myy,'-',mym);
            else
                myym = ' ' ;
            end if ;    
            return myym ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getpurym(purno varchar) cascade""")
        self._cr.execute("""drop function if exists getpurym(purid int) cascade""")
        self._cr.execute("""create or replace function getpurym(purno varchar) returns varchar as $$
        declare
            myym varchar;
            myy varchar;
            mym varchar;
            purdate date ;
            purid int ;
        begin   
            if purno is not null then
                select id into purid from purchase_order where name = purno;                                            
                select create_date into purdate from purchase_order where id = purid;
                select date_part('year',purdate)::TEXT into myy;
                select lpad(date_part('month',purdate)::TEXT,2,'0') into mym;
                myym = concat(myy,'-',mym);
            else
                myym = ' ' ;
            end if ;    
            return myym ;
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getpurfromto(purid int) cascade""")
        self._cr.execute("""create or replace function getpurfromto(purid int) returns varchar as $$
         declare
           myres varchar ;
           myfrom varchar ;
           myto varchar ;
         begin
           select coalesce(deliver_date::TEXT,''),coalesce(deliver_date1::TEXT,'') into myfrom,myto from purchase_order where id = purid ;
           if myfrom is not null and myto is not null then
              myres = concat(myfrom,'~',myto);
           else
             myres = ' ' ;
           end if ;
           return myres ;
         end; $$ language plpgsql;""")

        # self._cr.execute("""drop function if exists getprojtopur(projid int) cascade""")
        # self._cr.execute("""create ort replace function getprojtopur(projid int) returns varchar as $$
        # declare
        #   myres varchar ;
        #   ncount int ;
        # begin
        #   select count(*) into ncount from neweb_projsaleitem where saleitem_id = projid and purchase_no is not null;
        #   if ncount > 0 then /* 已有採購 */
        # end; $$ language plpgsql;""")


        tools.drop_view_if_exists(self.env.cr, 'neweb_finrreport_sima_view')
        self.env.cr.execute("""CREATE or REPLACE VIEW neweb_finereport_sima_view as (select (select getprojyear(A.id)) as proj_year,B.name as proj_sale,
        (select getsinum(A.id)) as si_num,(select getmanum(A.id)) as ma_num,(select getsimatot(A.id)) as simatot,A.proj_sale as projsaleid,B.department_id from neweb_project A 
            left join hr_employee B on A.proj_sale = B.id)""")

        tools.drop_view_if_exists(self._cr, 'neweb_acceptance_acc_list_view')
        self._cr.execute("""create or replace view neweb_acceptance_acc_list_view as (
            select B.name as salename,A.project_no,E.name as projectno1,F.date_approve::DATE as purdate,A.purchase_no,A.proj_sale,
            C.name as stockoutno,D.name as partnername,A.cus_project,A.prod_modeltype,A.prod_desc,A.prod_num,
            A.supplier,E.shipping_date,F.date_planned::DATE,A.acceptanced_date1,A.stockin_date,A.stockout_date,A.acceptanced_date2,
            (select getprojyear(A.project_no)) as proj_year,(select getprojym(A.project_no)) as proj_ym,(select getpurym(A.purchase_no)) as pur_ym,
            (select getpurfromto(F.id)) as pur_fromto,B.department_id
            from neweb_acceptance_acc_list A left join hr_employee B on A.proj_sale = B.id 
            left join stock_picking C on A.stockout_no = C.id left join res_partner D on A.cus_name = D.id
            left join neweb_project E on A.project_no = E.id left join purchase_order F on A.purchase_no = F.name)""")

        # 銷貨收入
        self._cr.execute("""drop function if exists get_cost1_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost1_rev(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,7,6,8) ;
          end if ;
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 銷貨毛利
        self._cr.execute("""drop function if exists get_cost1_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost1_pro(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,7,6,8) ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 建置收入
        self._cr.execute("""drop function if exists get_cost2_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost2_rev(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=3 ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 建置毛利
        self._cr.execute("""drop function if exists get_cost2_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost2_pro(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=3  ;
          end if ;  
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維運人力收入
        self._cr.execute("""drop function if exists get_cost3_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost3_rev(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=5 ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維運人力毛利
        self._cr.execute("""drop function if exists get_cost3_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost3_pro(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=5  ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維護舊約收入
        self._cr.execute("""drop function if exists get_cost4_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost4_rev(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=4 ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維護舊約毛利
        self._cr.execute("""drop function if exists get_cost4_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost4_pro(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then 
             select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=4  ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維護新約收入
        self._cr.execute("""drop function if exists get_cost5_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost5_rev(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype in (9,12) ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 維護新約毛利
        self._cr.execute("""drop function if exists get_cost5_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost5_pro(projid int) returns float as $$
        declare
          myres float ;
        begin
          if projid is not null then
             select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype in (9,12) ;
          end if ;   
          if myres is null then
              myres = 0 ;
          end if ;
          return myres ;
        end ; $$ language plpgsql;""")

        # 保固維護收入
        self._cr.execute("""drop function if exists get_cost6_rev(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost6_rev(projid int) returns float as $$
           declare
             myres float ;
           begin
             if projid is not null then
                select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=12 ;
             end if ;   
             if myres is null then
                 myres = 0 ;
             end if ;
             return myres ;
           end ; $$ language plpgsql;""")

        # 保固維護毛利
        self._cr.execute("""drop function if exists get_cost6_pro(projid int) cascade""")
        self._cr.execute("""create or replace function get_cost6_pro(projid int) returns float as $$
           declare
             myres float ;
           begin
             if projid is not null then
                select sum(coalesce(analysis_revenue,0) - coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid and analysis_costtype=12 ;
             end if ;   
             if myres is null then
                 myres = 0 ;
             end if ;
             return myres ;
           end ; $$ language plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'neweb_projanalysis_costtype_view')
        self._cr.execute("""create or replace view neweb_projanalysis_costtype_view as (
        select A.name,(select getprojyear(A.id)) as proj_year,B.name as salename,C.name as partnername,A.proj_sale,A.cus_name,B.department_id,
         (select get_cost1_rev(A.id)) as cost1rev,(select get_cost1_pro(A.id)) as cost1pro,
          (select get_cost2_rev(A.id)) as cost2rev,(select get_cost2_pro(A.id)) as cost2pro,
          (select get_cost3_rev(A.id)) as cost3rev,(select get_cost3_pro(A.id)) as cost3pro,
          (select get_cost4_rev(A.id)) as cost4rev,(select get_cost4_pro(A.id)) as cost4pro,
          (select get_cost5_rev(A.id)) as cost5rev,(select get_cost5_pro(A.id)) as cost5pro,
          (select get_cost6_rev(A.id)) as cost6rev,(select get_cost6_pro(A.id)) as cost6pro    
          from neweb_project A left join hr_employee B on A.proj_sale = B.id 
          left join res_partner C on A.cus_name = C.id
          where A.name is not null and A.cus_name is not null and A.proj_sale is not null)""")

        self._cr.execute("""drop function if exists get_si_count(projid int) cascade""")
        self._cr.execute("""create or replace function get_si_count(projid int) returns int as $$
        declare
          myres int ;
          sirev float ;
          marev float ;
        begin
          if projid is not null then
                select sum(coalesce(analysis_revenue,0)) into sirev from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7);
                select sum(coalesce(analysis_revenue,0)) into marev from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9);
          end if ;
          if sirev is null then
              sirev = 0 ;
          end if ;
          if marev is null then
              marev = 0 ;
          end if ;
          if sirev > marev then
             myres = 1 ;
          else
              myres = 0 ;
          end if ; 
          return myres ;  
        end; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists get_ma_count(projid int) cascade""")
        self._cr.execute("""create or replace function get_ma_count(projid int) returns int as $$
        declare
          myres int ;
          sirev float ;
          marev float ;
        begin
          if projid is not null then
                select sum(coalesce(analysis_revenue,0)) into sirev from neweb_projanalysis where analysis_id = projid and analysis_costtype in (1,2,3,7);
                select sum(coalesce(analysis_revenue,0)) into marev from neweb_projanalysis where analysis_id = projid and analysis_costtype in (4,9);
          end if ;
          if sirev is null then
              sirev = 0 ;
          end if ;
          if marev is null then
              marev = 0 ;
          end if ;
          if marev > sirev then
             myres = 1 ;
          else
              myres = 0 ;
          end if ; 
          return myres ;  
        end; $$ language plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'neweb_proj_salecount_view')
        self._cr.execute("""create or replace view neweb_proj_salecount_view as (select A.proj_sale,B.name as salename,(select getprojyear(A.id)) as proj_year,
         (select get_si_count(A.id)) as sicount,(select get_ma_count(A.id)) as macount,B.department_id  from neweb_project A left join hr_employee B on A.proj_sale = B.id 
         where A.name is not null and A.cus_name is not null and A.proj_sale is not null)""")





