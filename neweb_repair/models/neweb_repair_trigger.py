# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebRepairTrigger(models.Model):
    _name = "neweb.repair_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genrepairaedept() cascade""")
        self._cr.execute("""create  or replace function genrepairaedept() returns trigger as $BODY$
          DECLARE
             deptid int ;
             deptname varchar ;
          BEGIN
             if NEW.ae_id is not null then
                select department_id into deptid from hr_employee where id = NEW.ae_id ;
                if deptid is not null then
                   select name into deptname from hr_department where id=deptid ; 
                   NEW.ae_dept = deptname ;
                end if ;   
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genrepairaedept1() cascade""")
        self._cr.execute("""create  or replace function genrepairaedept1() returns trigger as $BODY$
          DECLARE
             deptid int ;
             deptname varchar ;
          BEGIN
             if NEW.ae_id is not null then
                select department_id into deptid from hr_employee where id = NEW.ae_id ;
                if deptid is not null then
                   select name into deptname from hr_department where id=deptid ; 
                   NEW.ae_dept = deptname ;
                end if ;   
             end if ;
             return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists insert_on_repair on neweb_repair_repair ;""")
        self._cr.execute("""create trigger insert_on_repair before insert on neweb_repair_repair
                                 for each row execute procedure genrepairaedept();""")

        self._cr.execute("""drop trigger if exists update_on_repair on neweb_repair_repair ;""")
        self._cr.execute("""create trigger update_on_repair before update of ae_id on neweb_repair_repair
                                         for each row execute procedure genrepairaedept1();""")

        self._cr.execute("""drop function if exists genallrepairaedept() cascade""")
        self._cr.execute("""create or replace function genallrepairaedept() returns void as $BODY$
          DECLARE
            rep_cur refcursor ;
            rep_rec record ;
            deptid int ;
            deptname varchar ;
          BEGIN
            open rep_cur for select id,ae_id from neweb_repair_repair ;
            loop
              fetch rep_cur into rep_rec ;
              exit when not found ;
              if rep_rec.ae_id is not null then
                select department_id into deptid from hr_employee where id = rep_rec.ae_id ;
                if deptid is not null then
                   select name into deptname from hr_department where id=deptid ; 
                   update neweb_repair_repair set ae_dept=deptname where id = rep_rec.id ; 
                end if ;   
             end if ;
            end loop ;
            close rep_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")



