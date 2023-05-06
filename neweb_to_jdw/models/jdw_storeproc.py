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
          open cus_cur for select id from res_partner where  active = true and write_date between sdate and edate ;
          loop
            fetch cus_cur into cus_rec ;
            exit when not found ;
            myres := cus_rec.id ;
            return next myres ;
          end loop ;
          close cus_cur ;
          open cus_cur for select id from res_partner where  active = true and write_date is null and create_date between sdate and edate ;
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
                select count(*) into ncount from hr_employee where employee_id = rel_rec.hr_employee_id and active = true ;
                if ncount > 0 then
                   select name into myres from hr_employee where employee_id = rel_rec.hr_employee_id and active = true ; 
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
            select max(id) into projid from neweb_project where cus_name = partnerid and active = true ;
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
         begin
            select max(id) into projid from neweb_project where cus_name = partnerid and active = true ;
            select contact_name into myres from neweb_projcontact where contact_type=11 and contact_id=projid ;
            if myres is null then
               select max(id) into contactid from neweb_projcontact where  contact_id=projid ;
               select contact_name into myres from neweb_projcontact where id=contactid ;
               return next myres ;
               select contact_phone into myres from neweb_projcontact where id=contactid ;
                return next myres ;
               select contact_email into myres from neweb_projcontact where id=contactid ;
                return next myres ; 
            else
                return next myres ;
                select contact_phone into myres from neweb_projcontact where contact_type=11 and contact_id=projid ;
                return next myres ;
                select contact_email into myres from neweb_projcontact where contact_type=11 and contact_id=projid ;
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
          open con_cur for select id from neweb_contract_contract_line where active = true and write_date between sdate and edate order by contract_id,id ;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.id ;
            return next myres ;
          end loop ;
          close con_cur ;
          open con_cur for select id from neweb_contract_contract_line where  active = true and write_date is null and create_date between sdate and edate order by contract_id,id;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            myres := con_rec.id ;
            return next myres ;
          end loop ;
          close con_cur ;
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
                    cbackup = 'Y' ;
               else
                    cbackup = '-' ;
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
