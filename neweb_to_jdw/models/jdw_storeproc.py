# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class newebjdwstoreproc(models.Model):
    _name = "neweb_to_jdw.storeproc"


    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getjdwexportcus(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportcus(sdate date,edate date) returns setof INT as $$
        declare
          myres int ;
          cus_cur refcursor ;
          cus_rec record ;
        begin
          open cus_cur for select id from res_partner where  active = true and write_date >= sdate and write_date <= edate and is_company = true ;
          loop
            fetch cus_cur into cus_rec ;
            exit when not found ;
            myres := cus_rec.id ;
            return next myres ;
          end loop ;
          close cus_cur ;
          open cus_cur for select id from res_partner where  active = true and write_date is null and create_date >= sdate and create_date <= edate and is_company = true ;
          loop
            fetch cus_cur into cus_rec ;
            exit when not found ;
            myres := cus_rec.id ;
            return next myres ;
          end loop ;
          close cus_cur ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getcussale(partnerid int) cascade""")
        self._cr.execute("""create or replace function getcussale(partnerid int) returns varchar as $$
        declare
          myres varchar ;
          rel_cur refcursor ;
          rel_rec record ;
          ncount int ;
        begin
           open rel_cur for select hr_employee_id from hr_employee_res_partner_rel where res_partner_id = partnerid ;
           loop
                fetch rel_cur into rel_rec ;
                exit when not found ;
                select count(*) into ncount from hr_employee where id = rel_rec.hr_employee_id and active = true ;
                if ncount > 0 then
                   select name into myres from hr_employee where id = rel_rec.hr_employee_id and active = true ; 
                end if ;
           end loop ;
           close rel_cur ;
           return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getcusinvaddr(partnerid int) cascade""")
        self._cr.execute("""create or replace function getcusinvaddr(partnerid int) returns varchar as $$
        declare
            myres varchar ;
            projid int ;
        begin   
            select max(id) into projid from neweb_project where cus_name = partnerid  ;
            select cus_address into myres from neweb_projcustom where cus_id=projid and cus_type='5' ;
            if myres is null then
               select street into myres from res_partner where id = partnerid ;
            end if ;
            return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwcontact(partnerid int) cascade""")
        self._cr.execute("""create or replace function getjdwcontact(partnerid int) returns setof varchar as $$
         declare
            myres varchar ;
            projid int ;
            contactid int ;
            partnerid1 int ;
         begin
            select max(id) into projid from neweb_project where cus_name = partnerid ;
            select contact_name into partnerid1 from neweb_projcontact where contact_type=11 and contact_id=projid ;
            if partnerid1 is null then
               select max(id) into contactid from neweb_projcontact where contact_id=projid ;
               select contact_name into partnerid1 from neweb_projcontact where id = contactid ;
               select name into myres from res_partner where id = partnerid1 ;
               return next myres ;
               select contact_phone into myres from neweb_projcontact where id = contactid ;
                return next myres ;
               select contact_email into myres from neweb_projcontact where id = contactid ;
                return next myres ; 
            else
                select name into myres from res_partner where id = partnerid1 ;
                return next myres ;
                select max(id) into contactid from neweb_projcontact where contact_id=projid ;
                select contact_phone into myres from neweb_projcontact where id = contactid ;
                return next myres ;
                select contact_email into myres from neweb_projcontact where id = contactid;
                return next myres ;
            end if ;
         end;$$
         language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportdev(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportdev(sdate date,edate date) returns setof INT as $$
        declare
          myres int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          open con_cur for select contract_line_id from neweb_contract_contract_line_change where change_date >= sdate and change_date <= edate order by contract_line_id ;
          loop
             fetch con_cur into con_rec ;
             exit when not found ;
                myres := con_rec.contract_line_id ;
                return next myres ;
          end loop ;
          close con_cur ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportdevall(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportdevall(sdate date,edate date) returns setof INT as $$
        declare
          myres int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          open con_cur for select id from neweb_contract_contract_line where 
             contract_id in 
             (select id from neweb_contract_contract where maintenance_start_date >= sdate and maintenance_start_date <= edate) 
             order by id ;
          loop
             fetch con_cur into con_rec ;
             exit when not found ;
                myres := con_rec.id ;
                return next myres ;
          end loop ;
          close con_cur ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportdev1(contractno varchar) cascade""")
        self._cr.execute("""create or replace function getjdwexportdev1(contractno varchar) returns setof INT as $$
        declare
          myres int ;
          myres1 int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          select id into myres from neweb_contract_contract where name = contractno ;
          if myres is not null then
             open con_cur for select * from neweb_contract_contract_line_change where contract_id = myres ;
             loop
                fetch con_cur into con_rec ;
                exit when not found ;
                myres1 := con_rec.contract_line_id ;
                return next myres1 ;
             end loop ;
             close con_cur ;
          end if ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportdevall1(contractno varchar) cascade""")
        self._cr.execute("""create or replace function getjdwexportdevall1(contractno varchar) returns setof INT as $$
        declare
          myres int ;
          myres1 int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          select id into myres from neweb_contract_contract where name = contractno ;
          if myres is not null then
             open con_cur for select * from neweb_contract_contract_line where contract_id = myres ;
             loop
                fetch con_cur into con_rec ;
                exit when not found ;
                myres1 := con_rec.id ;
                return next myres1 ;
             end loop ;
             close con_cur ;
          end if ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getslabrief(slaid int) cascade""")
        self._cr.execute("""create or replace function getslabrief(slaid int) returns varchar as $$
        declare
          myres varchar ;
          restime varchar ;
          onsitetime varchar ;
          maintime varchar ;
          havebackup Boolean ;
          cbackup varchar ;
          begin 
            select response_time::INT::TEXT,onsite_time::INT::TEXT,maintenance_time::INT::TEXT,backup_equipment into restime,onsitetime,maintime,havebackup from neweb_base_sla where id = slaid and active=true;
            if restime is not null then
               if havebackup = true then
                    cbackup = '備機' ;
               else
                    cbackup = '無' ;
               end if ;
                  myres = concat(restime,'/',onsitetime,'/',maintime,'/',cbackup) ;
            else
                myres = ' ' ;
            end if ;
            return myres ;
          end;$$
          language plpgsql;""")

        self._cr.execute("""drop function if exists getcontractae1(conid int) cascade""")
        self._cr.execute("""create or replace function getcontractae1(conid int) returns varchar as $$
        declare
          myres varchar ;
          cname varchar ;  
          empid int ;
          resourceid int ;
          userid int ;
          partnerid int ;
          rel_cur refcursor ;
          rel_rec record ;
        begin
          myres = '' ;
          open rel_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id = conid ; 
          loop
              fetch rel_cur into rel_rec ;
              exit when not found ;
                 select resource_id into resourceid from hr_employee where id=rel_rec.hr_employee_id and active = true;
                 select user_id into userid from resource_resource where id = resourceid and active = true ;
                 select partner_id into partnerid from res_users where id = userid and active = true ;
                 select name into cname from res_partner where id = partnerid and active = true ;
                 if myres = '' then
                     myres = cname ;
                 else
                     myres = concat(myres,'/',cname) ;
                 end if ;
          end loop ;
          close rel_cur ;    
          return myres ; 
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getcondepartment(conid int) cascade""")
        self._cr.execute("""create or replace function getcondepartment(conid int) returns varchar as $$
        declare
          myres varchar ;
          cdept varchar ;  
          empid int ;
          departmentid int ;
          rel_cur refcursor ;
          rel_rec record ;
        begin
          myres = '' ;
          open rel_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id = conid ; 
          loop
          fetch rel_cur into rel_rec ;
          exit when not found ;
             select department_id into departmentid from hr_employee where id=rel_rec.hr_employee_id and active = true ; 
             select name into cdept from hr_department where id = departmentid and active = true ;
             if cdept ilike '%NT%' then
                cdept = 'NT' ;
             elsif cdept ilike '%R6%' then
                   cdept = 'R6' ;
             elsif cdept ilike '%NW%' then 
                   cdept = 'NW' ;
             else 
                    cdept = '' ;      
             end if ;      
             if myres = '' then
                myres = cdept ;
             else
                myres = concat(myres,'/',cdept) ;
             end if ;
          end loop ;
          close rel_cur ;    
          return myres ; 
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportcontract(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportcontract(sdate date,edate date) returns setof INT as $$
        declare
          myres int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          open con_cur for select distinct contract_id from neweb_contract_contract_line where  write_date >= sdate and write_date <= edate order by contract_id;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.contract_id ;
            return next myres ;
          end loop ;
          close con_cur ;
          open con_cur for select id from neweb_contract_contract where  write_date >= sdate and write_date <= edate ;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.id ;
            return next myres ;
          end loop ;
          close con_cur ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportcontract1(contractno varchar) cascade""")
        self._cr.execute("""create or replace function getjdwexportcontract1(contractno varchar) returns INT as $$
            declare
              myres int ;
            begin
              select id into myres from neweb_contract_contract where name=contractno ;
              if myres is null then
                 myres = 0 ;
              end if ;
              return myres ;
            end;$$
            language plpgsql;""")

        self._cr.execute("""drop function if exists getprojrevenue(projid int) cascade""")
        self._cr.execute("""drop function if exists getprojrevenue(projno varchar) cascade""")
        self._cr.execute("""create or replace function getprojrevenue(projno varchar) returns INT as $$
        declare
            myres int ;
            projid int ;
        begin   
            select id into projid from neweb_project where name = projno ;
            select sum(analysis_revenue) into myres from neweb_projanalysis where analysis_id = projid ;
            if myres is null then
               myres = 0 ;
            end if ;
            return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportcontractline(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportcontractline(sdate date,edate date) returns setof INT as $$
        declare
          myres int ;
          con_cur refcursor ;
          con_rec record ;
        begin
          open con_cur for select distinct contract_id from neweb_contract_contract_line where write_date >= sdate and write_date <= edate order by contract_id ;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.contract_id ;
            return next myres ;
          end loop ;
          close con_cur ;
          open con_cur for select id from neweb_contract_contract where write_date >= sdate and write_date <= edate ;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.id ;
            return next myres ;
          end loop ;
          close con_cur ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getjdwexportcontractline1(contractno varchar) cascade""")
        self._cr.execute("""create or replace function getjdwexportcontractline1(contractno varchar) returns INT as $$
        declare
          myres int ;
        begin
          select id into myres from neweb_contract_contract where name=contractno ;
          if myres is null then
             myres = 0 ;
          end if ;
          return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getconsmonth(conid int) cascade""")
        self._cr.execute("""create or replace function getconsmonth(conid int) returns INT as $$
        declare
            myres int ;
        begin   
            select date_part('month',maintenance_start_date)::INT into myres from neweb_contract_contract where id = conid ;
            return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists getconsales(conid int) cascade""")
        self._cr.execute("""create or replace function getconsales(conid int) returns varchar as $$
        declare
            myres varchar ;
            resourceid int ;
            saleid int ;
            userid int ;
            partnerid int ;
        begin
            select sales into saleid from neweb_contract_contract where id = conid ;
            select resource_id into resourceid from hr_employee where id = saleid and active = true ;
            select user_id into userid from resource_resource where id = resourceid and active = true ;
            select partner_id into partnerid from res_users where id = userid and active = true ;
            select name into myres from res_partner where id = partnerid and active = true ;
            return myres ;
        end;$$
        language plpgsql;""")

        self._cr.execute("""drop function if exists genmachineloc() cascade""")
        self._cr.execute("""create or replace function genmachineloc() returns void as $$
        declare
          cstreet varchar ;
          partnerid int ;
          con_cur refcursor ;
          con_rec record ;  
          conl_cur refcursor ;
          conl_rec record ;
        begin
          open con_cur for select id,end_customer from neweb_contract_contract ;
          loop
             fetch con_cur into con_rec ;
             exit when not found ;
             select street into cstreet from res_partner where id = con_rec.end_customer ;   
             open conl_cur for select id from neweb_contract_contract_line1 where contract_id = con_rec.id ;
             loop
                fetch conl_cur into conl_rec ;
                exit when not found ;
                update neweb_contract_contract_line1 set machine_loc = cstreet where id = conl_rec.id and machine_loc is null ;
             end loop ;
             close conl_cur ;
          end loop ;
          close con_cur ;
        end ;$$
        language plpgsql;""")
