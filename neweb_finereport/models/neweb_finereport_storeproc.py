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


        tools.drop_view_if_exists(self.env.cr, 'neweb_finrreport_sima_view')
        self.env.cr.execute("""CREATE or REPLACE VIEW neweb_finereport_sima_view as (select (select getprojyear(A.id)) as proj_year,B.name as proj_sale,(select getsinum(A.id)) as si_num,(select getmanum(A.id)) as ma_num,(select getsimatot(A.id)) as simatot from neweb_project A 
            left join hr_employee B on A.proj_sale = B.id)""")

        tools.drop_view_if_exists(self._cr, 'neweb_acceptance_acc_list_view')
        self._cr.execute("""create or replace view neweb_acceptance_acc_list_view as (
            select B.name as salename,A.project_no,E.name as projectno1,F.date_approve as purdate,A.purchase_no,A.proj_sale,
            C.name as stockoutno,D.name as partnername,A.cus_project,A.prod_modeltype,A.prod_desc,A.prod_num,
            A.supplier,E.shipping_date,F.date_planned::DATE,A.acceptanced_date1,A.stockin_date,A.stockout_date,A.acceptanced_date2,
            (select getprojyear(A.project_no)) as proj_year,(select getprojym(A.project_no)) as proj_ym,(select getpurym(A.purchase_no)) as pur_ym
            from neweb_acceptance_acc_list A left join hr_employee B on A.proj_sale = B.id 
            left join stock_picking C on A.stockout_no = C.id left join res_partner D on A.cus_name = D.id
            left join neweb_project E on A.project_no = E.id left join purchase_order F on A.purchase_no = F.name)""")