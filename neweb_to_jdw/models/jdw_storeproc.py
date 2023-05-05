# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class newebjdwstoreproc(models.Model):
    _name = "neweb_to_jdw.storeproc"


    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getjdwexportcus(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function getjdwexportcus(sdate date,edate date) returns set of INT as $$
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
        self._cr.execute("""create or replace function getjdwcontact(partnerid int) returns set of varchar as $$
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
        self._cr.execute("""create or replace function getjdwexportdev(sdate date,edate date) returns set of INT as $$
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
