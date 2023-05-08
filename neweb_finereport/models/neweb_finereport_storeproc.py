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


        tools.drop_view_if_exists(self.env.cr, 'neweb_finrreport_sima_view')
        self.env.cr.execute("""CREATE or REPLACE VIEW neweb_finereport_sima_view as (select (select getprojyear(A.id)) as proj_year,B.name as proj_sale,(select getsinum(A.id)) as si_num,(select getmanum(A.id)) as ma_num,(select getsimatot(A.id)) as simatot from neweb_project A 
            left join hr_employee B on A.proj_sale = B.id)""")