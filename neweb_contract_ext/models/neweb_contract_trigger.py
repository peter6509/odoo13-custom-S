# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class newebcontractTrigger(models.Model):
    _name = "neweb_contract.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_contract_ae1() cascade""")
        self._cr.execute("""create  or replace function insert_contract_ae1() returns trigger as $BODY$
          DECLARE
            ae1_cur refcursor ;
            ae1_rec record ;
            empname varchar ;
            empdeptid int ;
            deptname varchar ;
            myempname varchar ;
            mydeptname varchar ;
            ncount int ;
          BEGIN
             myempname='' ;
             mydeptname='' ;
             open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=NEW.neweb_contract_contract_id ;
             loop
               fetch ae1_cur into ae1_rec ;
               exit when not found ;
               select count(*) into ncount from hr_employee where id = ae1_rec.hr_employee_id and active=True ;
               if ncount > 0 then
                   select coalesce(name,' '),coalesce(department_id,0) into empname,empdeptid from hr_employee where id = ae1_rec.hr_employee_id ;
                   if myempname='' then
                      myempname = empname ;
                   else
                      myempname = concat(myempname,'/',empname) ;
                   end if ;
                   if empdeptid != 0 then
                      select name into deptname from hr_department where id = empdeptid ;
                      if mydeptname='' then
                         mydeptname = deptname ;
                      else
                         mydeptname = concat(mydeptname,'/',deptname) ;
                      end if ;
                   end if ;
               end if ;    
             end loop ;
             close ae1_cur ;
             update neweb_contract_contract set ae1_name=myempname,ae1_dept=mydeptname where id=NEW.neweb_contract_contract_id ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delete_contract_ae1() cascade""")
        self._cr.execute("""create  or replace function delete_contract_ae1() returns trigger as $BODY$
          DECLARE
            ae1_cur refcursor ;
            ae1_rec record ;
            empname varchar ;
            empdeptid int ;
            deptname varchar ;
            myempname varchar ;
            mydeptname varchar ;
          BEGIN
             myempname='' ;
             mydeptname='' ;
             open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=OLD.neweb_contract_contract_id ;
             loop
               fetch ae1_cur into ae1_rec ;
               exit when not found ;
               select coalesce(name,' '),coalesce(department_id,0) into empname,empdeptid from hr_employee where id = ae1_rec.hr_employee_id ;
               if myempname='' then
                  myempname = empname ;
               else
                  myempname = concat(myempname,'/',empname) ;
               end if ;
               if empdeptid != 0 then
                  select name into deptname from hr_department where id = empdeptid ;
                  if mydeptname='' then
                     mydeptname = deptname ;
                  else
                     mydeptname = concat(mydeptname,'/',deptname) ;
                  end if ;
               end if ;
             end loop ;
             close ae1_cur ;
             update neweb_contract_contract set ae1_name=myempname,ae1_dept=mydeptname where id=OLD.neweb_contract_contract_id ;
             return OLD ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次新增 hr_employee_neweb_contract_contract_rel  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_on_contract_ae1 on hr_employee_neweb_contract_contract_rel ;""")
        self._cr.execute("""create trigger insert_on_contract_ae1 after insert on hr_employee_neweb_contract_contract_rel
                                 for each row execute procedure insert_contract_ae1();""")

        # 針對每次刪除 hr_employee_neweb_contract_contract_rel  作動一次 trigger
        self._cr.execute("""drop trigger if exists delete_on_contract_ae1 on hr_employee_neweb_contract_contract_rel ;""")
        self._cr.execute("""create trigger delete_on_contract_ae1 after delete on hr_employee_neweb_contract_contract_rel
                                        for each row execute procedure delete_contract_ae1();""")

        self._cr.execute("""drop function if exists ins_neweb_contract_contract_line() cascade""")
        self._cr.execute("""create  or replace function ins_neweb_contract_contract_line() returns trigger as $BODY$
          DECLARE
             ncount int ;
          BEGIN
             select count(*) into ncount from neweb_contract_contract_line1 where contract_line_id=NEW.id ;
             if ncount = 0 then
                insert into neweb_contract_contract_line1(prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,rack_loc,warranty_duedate,
                  prod_line_os,contract_line_id,sequence) values (NEW.prod_set,NEW.prod_brand,NEW.prod_modeltype,NEW.prod_modeltype1,NEW.machine_serial_no,NEW.rack_loc,NEW.warranty_duedate,NEW.prod_line_os,NEW.id,NEW.sequence) ;
             else
                update neweb_contract_contract_line1 set prod_set=NEW.prod_set,prod_brand=NEW.prod_brand,prod_modeltype=NEW.prod_modeltype,prod_modeltype1=NEW.prod_modeltype1,
                  machine_serial_no=NEW.machine_serial_no,rack_loc=NEW.rack_loc,warranty_duedate=NEW.warranty_duedate,sequence=NEW.sequence where contract_line_id=NEW.id ;
             end if ;
             return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 neweb_contract_contract_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists ins_neweb_contract_contract_line on neweb_contract_contract_line ;""")
        self._cr.execute("""create trigger ins_neweb_contract_contract_line after insert on neweb_contract_contract_line
                                         for each row execute procedure ins_neweb_contract_contract_line();""")

        self._cr.execute("""drop function if exists upd_neweb_contract_contract_line() cascade""")
        # self._cr.execute("""create  or replace function upd_neweb_contract_contract_line() returns trigger as $BODY$
        #   DECLARE
        #      ncount int ;
        #   BEGIN
        #      select count(*) into ncount from neweb_contract_contract_line1 where contract_line_id=NEW.id ;
        #      if ncount = 0 then
        #         insert into neweb_contract_contract_line1(prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,rack_loc,warranty_duedate,
        #           prod_line_os,contract_line_id) values (NEW.prod_set,NEW.prod_brand,NEW.prod_modeltype,NEW.prod_modeltype1,NEW.machine_serial_no,NEW.rack_loc,NEW.warranty_duedate,NEW.prod_line_os,NEW.id) ;
        #      else
        #         update neweb_contract_contract_line1 set prod_set=NEW.prod_set,prod_brand=NEW.prod_brand,prod_modeltype=NEW.prod_modeltype,prod_modeltype1=NEW.prod_modeltype1,
        #           machine_serial_no=NEW.machine_serial_no,rack_loc=NEW.rack_loc,warranty_duedate=NEW.warranty_duedate where contract_line_id=NEW.id ;
        #      end if ;
        #      return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")

        # 針對每次更新prod_set neweb_contract_contract_line  作動一次 trigger
        self._cr.execute("""drop trigger if exists upd_neweb_contract_contract_line on neweb_contract_contract_line ;""")
        # self._cr.execute("""create trigger upd_neweb_contract_contract_line after update
        #      on neweb_contract_contract_line for each row execute procedure upd_neweb_contract_contract_line();""")

        self._cr.execute("""drop function if exists upd_contract_rack_loc() cascade""")
        self._cr.execute("""create  or replace function upd_contract_rack_loc() returns trigger as $BODY$
        DECLARE
            ncount int ;
        BEGIN
            select count(*) into ncount from neweb_contract_contract_line where id = OLD.contract_line_id ;
            if ncount > 0 then
                update neweb_contract_contract_line set rack_loc = NEW.rack_loc where id = OLD.contract_line_id ;
            end if ;    
            return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists upd_contract_rack_loc on neweb_contract_contract_line1 ;""")
        self._cr.execute("""create trigger upd_contract_rack_loc after update of rack_loc on neweb_contract_contract_line1
            for each row execute procedure upd_contract_rack_loc();""")



        self._cr.execute("""drop function if exists upd_contract_warranty_duedate() cascade""")
        self._cr.execute("""create  or replace function upd_contract_warranty_duedate() returns trigger as $BODY$
        DECLARE
            ncount int ;
        BEGIN
            select count(*) into ncount from neweb_contract_contract_line where id = OLD.contract_line_id ;
            if ncount > 0 then
                update neweb_contract_contract_line set warranty_duedate = NEW.warranty_duedate where id = OLD.contract_line_id ;
            end if ;
            return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists upd_contract_warranty_duedate on neweb_contract_contract_line1 ;""")
        self._cr.execute("""create trigger upd_contract_warranty_duedate after update of warranty_duedate on neweb_contract_contract_line1
                    for each row execute procedure upd_contract_warranty_duedate();""")


        self._cr.execute("""drop function if exists upd_contract_sequence() cascade""")
        self._cr.execute("""create  or replace function upd_contract_sequence() returns trigger as $BODY$
        DECLARE
            ncount int ;
        BEGIN
            select count(*) into ncount from neweb_contract_contract_line1 where contract_line_id = OLD.id ;
            if ncount > 0 then
                update neweb_contract_contract_line1 set sequence = NEW.sequence where contract_line_id = OLD.id ;
            end if ;
            return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists upd_contract_sequence on neweb_contract_contract_line ;""")
        self._cr.execute("""create trigger upd_contract_sequence after update of sequence on neweb_contract_contract_line
                            for each row execute procedure upd_contract_sequence();""")












