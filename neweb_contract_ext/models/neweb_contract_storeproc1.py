# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api


class newebcontractstoreproc1(models.Model):
    _name = "neweb_contract.contract_storeproc1"


    @api.model
    def init(self):
        self._cr.execute("""drop function if exists gen_warn_user(mycontractid int) cascade;""")
        self._cr.execute("""create or replace function gen_warn_user(mycontractid int) returns void as $BODY$
             declare 
                ae1_cur refcursor ;
                ae1_rec record ;
                ncount int ;
                saleid int ;
             begin 
                select sales into saleid from neweb_contract_contract where id=mycontractid ;
                select count(*) into ncount from neweb_contract_maintenance_warn_users_rel where neweb_contract_contract_id=mycontractid and 
                      hr_employee_id=saleid ;
                if ncount = 0 and saleid is not null then
                   insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id) values (mycontractid,saleid) ; 
                end if ;     
                open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=mycontractid ;
                loop
                  fetch ae1_cur into ae1_rec ;
                  exit when not found ;
                  select count(*) into ncount from neweb_contract_maintenance_warn_users_rel where neweb_contract_contract_id=mycontractid and 
                      hr_employee_id=ae1_rec.hr_employee_id ;
                  if ncount = 0 then 
                     insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id) values (mycontractid,ae1_rec.hr_employee_id ) ; 
                  end if ;   
                end loop;
                close ae1_cur ;
             end ; $BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genall_warn_user() cascade;""")
        self._cr.execute("""create or replace function genall_warn_user() returns void as $BODY$
             declare 
               contract_cur refcursor ;
               contract_rec record ;
               ae1_cur refcursor ;
               ae1_rec record ;
               ncount int ;
               saleid int ;
             begin 
               open contract_cur for select id,sales from neweb_contract_contract ;
               loop
                 fetch contract_cur into contract_rec ;
                 exit when not found ;
                 select count(*) into ncount from neweb_contract_maintenance_warn_users_rel where neweb_contract_contract_id=contract_rec.id and 
                      hr_employee_id=contract_rec.sales ;
                 if ncount = 0 and contract_rec.sales is not null then
                    insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id) values (contract_rec.id,contract_rec.sales) ; 
                 end if ;     
                 open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=contract_rec.id ;
                 loop
                   fetch ae1_cur into ae1_rec ;
                   exit when not found ;
                   select count(*) into ncount from neweb_contract_maintenance_warn_users_rel where neweb_contract_contract_id=contract_rec.id and 
                       hr_employee_id=ae1_rec.hr_employee_id ;
                   if ncount = 0 then 
                      insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id) values (contract_rec.id,ae1_rec.hr_employee_id) ; 
                   end if ;   
                end loop;
                close ae1_cur ;
               end loop ;
               close contract_cur ;
             end ; $BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_inspection_method(mycontractid int) cascade;""")
        self._cr.execute("""create or replace function check_inspection_method(mycontractid int) returns void as $BODY$
             declare 
               routinetype int ;
               myinstype VARCHAR ;
               ncount int ;
               mytype char ;
               mymainservicerulenew int;
             begin 
               select routine_maintenance_new into routinetype from neweb_contract_contract where id = mycontractid ;
               myinstype := 'none' ;
               if routinetype=1 then 
                  myinstype := 'monthly' ;
               elsif routinetype=2 then
                  myinstype := 'quarterly' ;
               elsif routinetype=3 then
                  myinstype := 'bimonthly' ;
               elsif routinetype=4 then
                  myinstype := 'semiannually' ; 
               end if ;    
               if myinstype != 'none' then 
                  update neweb_contract_contract set inspection_method=myinstype where id = mycontractid ;
               end if ;  
               select main_service_rule_new into mymainservicerulenew from  neweb_contract_contract where id = mycontractid ;
               if mymainservicerulenew = 2 or mymainservicerulenew = 3 then 
                  update neweb_contract_contract set weekly_maintain_day='1' where id = mycontractid ;
               elsif mymainservicerulenew = 4 or mymainservicerulenew = 5 then 
                  update neweb_contract_contract set weekly_maintain_day='2' where id = mycontractid ;
               end if ;
             end ; $BODY$
             LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists updateconlineitem(contractid int) cascade;""")
        self._cr.execute("""create or replace function updateconlineitem(contractid int) returns void as $BODY$
             DECLARE 
                con_cur refcursor ;
                con_rec record ;
                myitem int ;
             BEGIN 
                myitem := 1 ;
                open con_cur for select id from neweb_contract_contract_line where contract_id=contractid order by sequence ;
                loop
                   fetch con_cur into con_rec ;
                   exit when not found ;
                   update neweb_contract_contract_line set conline_item=myitem where id=con_rec.id ;
                   myitem := myitem + 1 ;
                end loop ;
                close con_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists allconlineitem() cascade;""")
        self._cr.execute("""create or replace function allconlineitem() returns void as $BODY$
             DECLARE 
               con_cur refcursor ;
               con_rec record ;
               conline_cur refcursor ;
               conline_rec record ;
               myitem int ;
             BEGIN 
               open con_cur for select id from neweb_contract_contract ;
               loop
                 fetch con_cur into con_rec ;
                 exit when not found ;
                 myitem := 1 ;
                 open conline_cur for select id from neweb_contract_contract_line where contract_id=con_rec.id order by sequence ;
                 loop
                   fetch conline_cur into conline_rec ;
                   exit when not found ;
                   update neweb_contract_contract_line set conline_item=myitem where id = conline_rec.id ;
                   myitem := myitem + 1 ;
                 end loop ;
                 close conline_cur ;
               end loop ;
               close con_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists satisfaction_check(contractid int) cascade""")
        self._cr.execute("""create or replace function satisfaction_check(contractid int) returns void as $BODY$
            DECLARE 
               ncount int ;
            BEGIN 
               select count(*) into ncount from neweb_contract_satisfaction_partner_rel where contract_id=contractid ;
               if ncount > 0 then
                  update res_partner set survey_mark=TRUE where id in 
                     (select partner_id from neweb_contract_satisfaction_partner_rel where contract_id=contractid) ;
               end if ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists satisfaction_allcheck() cascade""")
        self._cr.execute("""create or replace function satisfaction_allcheck() returns void as $BODY$
            DECLARE 
              con_cur refcursor ;
              con_rec record ;
              ncount int ;
            BEGIN 
              open con_cur for select id from neweb_contract_contract ;
              loop
                 fetch con_cur into con_rec ;
                 exit when not found ;
                 select count(*) into ncount from neweb_contract_satisfaction_partner_rel where contract_id = con_rec.id ;
                 if ncount > 0 then 
                    update res_partner set survey_mark=TRUE where id in 
                     (select partner_id from neweb_contract_satisfaction_partner_rel where contract_id=con_rec.id) ;
                 end if ;
              end loop ;
              close con_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_subscribebuild(inspectionid int) cascade""")
        self._cr.execute("""create or replace function check_subscribebuild(inspectionid int) returns void as $BODY$
            DECLARE
              ncount int ;
            BEGIN
              select count(*) into ncount from neweb_contract_inspection_list where inspection_id = inspectionid ;
              if ncount = 0 then
                 update neweb_contract_contract set subscribe_build=False where id = inspectionid ;
              else
                 update neweb_contract_contract set subscribe_build=True where id = inspectionid ;
              end if ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runallsubscribebuild() cascade;""")
        self._cr.execute("""create or replace function runallsubscribebuild() returns void as $BODY$
            DECLARE
              con_cur refcursor ;
              con_rec record ;
              ncount int ;
            BEGIN
              open con_cur for select * from neweb_contract_contract ;
              loop
                 fetch con_cur into con_rec ;
                 exit when not found ;
                 select count(*) into ncount from neweb_contract_inspection_list where inspection_id=con_rec.id ;
                 if ncount = 0 then
                    update neweb_contract_contract set subscribe_build=False where id = con_rec.id ;
                 else
                    update neweb_contract_contract set subscribe_build=True where id = con_rec.id ;
                 end if ;
              end loop ;
              close con_cur ; 
            END;$BODY$
            LANGUAGE plpgsql;
            """)

        self._cr.execute("""drop function if exists delinspectionlist(contractid int) cascade""")
        self._cr.execute("""drop function if exists delinspectionlist(contractid int,userid int) cascade""")
        self._cr.execute("""create or replace function delinspectionlist(contractid int,userid int) returns void as $BODY$
            DECLARE
              conl_cur refcursor ;
              conl_rec record ;
              ncount int ;
            BEGIN
              open conl_cur for select * from neweb_contract_inspection_list where inspection_id=contractid ;
              loop
                 fetch conl_cur into conl_rec ;
                 exit when not found ;
                 execute delinspectiontimesheet(conl_rec.id,userid) ;
                 execute del_plan_ins_calendar(conl_rec.id,userid) ;
                 delete from neweb_contract_inspection_list where id = conl_rec.id ;
              end loop ;
              close conl_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runcheckduedate() cascade""")
        self._cr.execute("""create or replace function runcheckduedate() returns void as $BODY$
           DECLARE
             con_cur refcursor ;
             con_rec record ;
             duedate DATE ;
           BEGIN
             select now()::DATE + interval '30 days' into duedate ;
             open con_cur for select id,hasbackuphw,maintenance_end_date from neweb_contract_contract where hasbackuphw = True ;
             loop
               fetch con_cur into con_rec ;
               exit when not found ;
               if con_rec.maintenance_end_date::DATE = duedate::DATE then
                  update neweb_contract_contract set isduedate=True where id = con_rec.id ;
               else
                  update neweb_contract_contract set isduedate=False where id = con_rec.id ;
               end if ;
             end loop ;
             close con_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runcontractcusproj() cascade""")
        self._cr.execute("""create or replace function runcontractcusproj() returns void as $BODY$
          DECLARE
            con_cur refcursor ;
            con_rec record ;
            cusproj varchar ;
            ncount int ;
          BEGIN
            open con_cur for select id,project_no from neweb_contract_contract ;
            loop
              fetch con_cur into con_rec ;
              exit when not found ;
              select count(*) into ncount from neweb_project where name = con_rec.project_no ;
              if ncount > 0 then
                 select cus_project into cusproj from neweb_project where name = con_rec.project_no ;
                 update neweb_contract_contract set cus_project=cusproj where id = con_rec.id ;
              end if ;
            end loop ;
            close con_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractae1() cascade""")
        self._cr.execute("""create or replace function gencontractae1() returns void as $BODY$
         DECLARE
           c_cur refcursor ;
           c_rec record ;
           e_cur refcursor ;
           e_rec record ;
           empname varchar ;
           empdeptid int ;
           deptname varchar ;
           myempname varchar ;
           mydeptname varchar ;
         BEGIN
           open c_cur for select distinct neweb_contract_contract_id from hr_employee_neweb_contract_contract_rel ;
           loop
             fetch c_cur into c_rec ;
             exit when not found ;
             myempname='' ;
             mydeptname='' ;
             open e_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id=c_rec.neweb_contract_contract_id ;
             loop
               fetch e_cur into e_rec ;
               exit when not found ;
               select coalesce(name,' '),coalesce(department_id,0) into empname,empdeptid from hr_employee where id = e_rec.hr_employee_id ;
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
             close e_cur ;
             update neweb_contract_contract set ae1_name=myempname,ae1_dept=mydeptname where id=c_rec.neweb_contract_contract_id ;
           end loop ;
           close c_cur ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists gencontractae1(conid int) cascade""")
        self._cr.execute("""create  or replace function gencontractae1(conid int) returns void as $BODY$
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
            open ae1_cur for select * from hr_employee_neweb_contract_contract_rel where neweb_contract_contract_id = conid ;
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
            update neweb_contract_contract set ae1_name=myempname,ae1_dept=mydeptname where id=conid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallae1() cascade""")
        self._cr.execute("""create or replace function genallae1() returns void as $BODY$
         DECLARE
           con_cur refcursor ;
           con_rec record ;
         BEGIN
           delete from hr_employee_neweb_contract_contract_rel where hr_employee_id in 
              (select id from hr_employee where active=False) ;
           open con_cur for select id from neweb_contract_contract ;
           loop
             fetch con_cur into con_rec ;
             exit when not found ;
             execute gencontractae1(con_rec.id) ;
           end loop ;
           close con_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractinherit4(conid int,conid1 int) cascade""")
        self._cr.execute("""create or replace function gencontractinherit4(conid int,conid1 int) returns void as $BODY$
         DECLARE
           conl_cur refcursor ;
           conl_rec record ;
           ncount int ;
           ncount1 int ;
           lineid int ;
           hd_cur refcursor ;
           hd_rec record ;
           cpu_cur refcursor ;
           cpu_rec record ;
           ram_cur refcursor ;
           ram_rec record ;
           expcard_cur refcursor ;
           expcard_rec record ;
           power_cur refcursor ;
           power_rec record ;   
         BEGIN
           open conl_cur for select * from neweb_contract_contract_line1 where contract_id = conid and machine_serial_no is not null ;
           loop
             fetch conl_cur into conl_rec ;
             exit when not found ;
             select count(*) into ncount from  neweb_contract_contract_line1 where contract_id = conid1 and machine_serial_no = conl_rec.machine_serial_no ;
             if ncount > 0 then
                select id into lineid from neweb_contract_contract_line1 where contract_id = conid1 and machine_serial_no = conl_rec.machine_serial_no ;
                update neweb_contract_contract_line1 set rack_loc=conl_rec.rack_loc,warranty_duedate=conl_rec.warranty_duedate,server_name=conl_rec.server_name,
                machine_used_desc=conl_rec.machine_used_desc,prod_line_os=conl_rec.prod_line_os,expand_module=conl_rec.expand_module,machine_other=conl_rec.machine_other,
                machine_loc=conl_rec.machine_loc where id=lineid ;
                delete from neweb_contract_hd_line where hd_id = conl_rec.id ;
                open hd_cur for select * from neweb_contract_hd_line where hd_id = conl_rec.id ;
                loop
                  fetch hd_cur into hd_rec ;
                  exit when not found ;
                  insert into neweb_contract_hd_line(hd_id,hd_item,hd_no,hd_num) values(lineid,hd_rec.hd_item,hd_rec.hd_no,hd_rec.hd_num) ;
                end loop;
                close hd_cur ;
                delete from neweb_contract_cpu_line where cpu_id = conl_rec.id ;
                open cpu_cur for select * from neweb_contract_cpu_line where cpu_id = conl_rec.id ;
                loop
                  fetch cpu_cur into cpu_rec ;
                  exit when not found ;
                  insert into neweb_contract_cpu_line(cpu_id,cpu_item,cpu_no,cpu_num) values(lineid,cpu_rec.cpu_item,cpu_rec.cpu_no,cpu_rec.cpu_num) ;
                end loop;
                close cpu_cur ; 
                delete from neweb_contract_ram_line where ram_id = conl_rec.id ;
                open ram_cur for select * from neweb_contract_ram_line where ram_id = conl_rec.id ;
                loop
                  fetch ram_cur into ram_rec ;
                  exit when not found ;
                  insert into neweb_contract_ram_line(ram_id,ram_item,ram_no,ram_num) values(lineid,ram_rec.ram_item,ram_rec.ram_no,ram_rec.ram_num) ;
                end loop;
                close ram_cur ; 
                delete from neweb_contract_expand_card_line where expand_card_id = conl_rec.id ;
                open expcard_cur for select * from neweb_contract_expand_card_line where expand_card_id = conl_rec.id ;
                loop
                  fetch expcard_cur into expcard_rec ;
                  exit when not found ;
                  insert into neweb_contract_expand_card_line(expand_card_id,expand_card_item,expand_card_no,expand_card_num) values(lineid,expcard_rec.expand_card_item,expcard_rec.expand_card_no,expcard_rec.expand_card_num) ;
                end loop;
                close expcard_cur ;  
                delete from neweb_contract_power_line where power_id = conl_rec.id ;
                open power_cur for select * from neweb_contract_power_line where power_id = conl_rec.id ;
                loop
                  fetch power_cur into power_rec ;
                  exit when not found ;
                  insert into neweb_contract_power_line(power_id,power_item,power_no,power_num) values(lineid,power_rec.power_item,power_rec.power_no,power_rec.power_num) ;
                end loop;
                close power_cur ;
             end if ;
           end loop ;
           close conl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractline1byid(conid int) cascade""")
        self._cr.execute("""create or replace function gencontractline1byid(conid int) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           ncount int ;
         BEGIN
           open l_cur for select * from neweb_contract_contract_line where contract_id=conid order by sequence,id ;
           loop
             fetch l_cur into l_rec;
             exit when not found ;
             select count(*) into ncount from neweb_contract_contract_line1 where contract_line_id=l_rec.id and contract_id=l_rec.contract_id ;
             if ncount = 0 then
               insert into neweb_contract_contract_line1(contract_id,prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,rack_loc,warranty_duedate,prod_line_os,contract_line_id,sequence) values
                  (l_rec.contract_id,l_rec.prod_set,l_rec.prod_brand,l_rec.prod_modeltype,l_rec.prod_modeltype1,l_rec.machine_serial_no,l_rec.rack_loc,l_rec.warranty_duedate,l_rec.prod_line_os,l_rec.id,l_rec.sequence) ;
             end if ;
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genlossconline1() cascade""")
        self._cr.execute("""create or replace function genlossconline1() returns void as $BODY$
        DECLARE
          con_cur refcursor ;
          con_rec record ;
          mynowdate date ;
        BEGIN
          select now()::date into mynowdate ; 
          open con_cur for select * from neweb_contract_contract where maintenance_end_date::DATE >= mynowdate::DATE  ;
          loop
            fetch con_cur into con_rec ;
            exit when not found ;
            delete from neweb_contract_contract_line1 where contract_id = con_rec.id ;
            execute gencontractline1byid(con_rec.id) ;
          end loop ;
          close con_cur ;
        END ;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractsel(conid int,conid1 int) cascade""")
        self._cr.execute("""create or replace function gencontractsel(conid int,conid1 int) returns void as $BODY$
         DECLARE
           conl_cur refcursor ;
           conl_rec record ;
           ncount int ;
           maxid int ;
           lineid int ; 
         BEGIN
           delete from neweb_contract_contract_selline ;
           delete from neweb_contract_contract_sel ;
           select count(*) into ncount from neweb_contract_contract_line1 where contract_id = conid and machine_serial_no is not null ;
           if ncount > 0 then
               insert into neweb_contract_contract_sel(contract_id,contract_id1) values (conid,conid1) ;
               select max(id) into maxid from neweb_contract_contract_sel ;
               open conl_cur for select * from neweb_contract_contract_line1 where contract_id = conid and machine_serial_no is not null ;
               loop
                 fetch conl_cur into conl_rec ;
                 exit when not found ;
                 insert into neweb_contract_contract_selline(sel_id,contract_id,prod_set,prod_brand,prod_modeltype,prod_modeltype1,machine_serial_no,rack_loc,warranty_duedate,server_name,machine_used_desc,prod_line_os,expand_module,machine_other,machine_loc,contract_line_id) 
                  values (maxid,conid,conl_rec.prod_set,conl_rec.prod_brand,conl_rec.prod_modeltype,conl_rec.prod_modeltype1,conl_rec.machine_serial_no,conl_rec.rack_loc,conl_rec.warranty_duedate,conl_rec.server_name,conl_rec.machine_used_desc,conl_rec.prod_line_os,conl_rec.expand_module,
                  conl_rec.machine_other,conl_rec.machine_loc,conl_rec.id) ;
               end loop ;
               close conl_cur ;
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractselline() cascade""")
        self._cr.execute("""create or replace function gencontractselline() returns void as $BODY$
         DECLARE
           conl_cur refcursor ;
           conl_rec record ;
           consl_cur refcursor ;
           consl_rec record ;
           ncount int ;
           ncount1 int ;
           lineid int ;
           hd_cur refcursor ;
           hd_rec record ;
           cpu_cur refcursor ;
           cpu_rec record ;
           ram_cur refcursor ;
           ram_rec record ;
           expcard_cur refcursor ;
           expcard_rec record ;
           power_cur refcursor ;
           power_rec record ;   
           conid int ;
           conid1 int ;
         BEGIN
           select contract_id,contract_id1 into conid,conid1 from neweb_contract_contract_sel order by id desc limit 1 ;
           open consl_cur for select * from neweb_contract_contract_selline where  selitem=True ;
           loop
             fetch consl_cur into consl_rec ;
             exit when not found ;
             open conl_cur for select * from neweb_contract_contract_line1 where  id=consl_rec.contract_line_id ;
             loop
                fetch conl_cur into conl_rec ;
                exit when not found ;
                select id into lineid from neweb_contract_contract_line1 where contract_id = conid1 and machine_serial_no = conl_rec.machine_serial_no ;
                update neweb_contract_contract_line1 set rack_loc=conl_rec.rack_loc,warranty_duedate=conl_rec.warranty_duedate,server_name=conl_rec.server_name,
                machine_used_desc=conl_rec.machine_used_desc,prod_line_os=conl_rec.prod_line_os,expand_module=conl_rec.expand_module,machine_other=conl_rec.machine_other,
                machine_loc=conl_rec.machine_loc where id=lineid ;
                delete from neweb_contract_hd_line where hd_id = lineid ;
                open hd_cur for select * from neweb_contract_hd_line where hd_id = conl_rec.id ;
                loop
                  fetch hd_cur into hd_rec ;
                  exit when not found ;
                  insert into neweb_contract_hd_line(hd_id,hd_item,hd_no,hd_num) values(lineid,hd_rec.hd_item,hd_rec.hd_no,hd_rec.hd_num) ;
                end loop;
                close hd_cur ;
                delete from neweb_contract_cpu_line where cpu_id = lineid ;
                open cpu_cur for select * from neweb_contract_cpu_line where cpu_id = conl_rec.id ;
                loop
                  fetch cpu_cur into cpu_rec ;
                  exit when not found ;
                  insert into neweb_contract_cpu_line(cpu_id,cpu_item,cpu_no,cpu_num) values(lineid,cpu_rec.cpu_item,cpu_rec.cpu_no,cpu_rec.cpu_num) ;
                end loop;
                close cpu_cur ; 
                delete from neweb_contract_ram_line where ram_id = lineid ;
                open ram_cur for select * from neweb_contract_ram_line where ram_id = conl_rec.id ;
                loop
                  fetch ram_cur into ram_rec ;
                  exit when not found ;
                  insert into neweb_contract_ram_line(ram_id,ram_item,ram_no,ram_num) values(lineid,ram_rec.ram_item,ram_rec.ram_no,ram_rec.ram_num) ;
                end loop;
                close ram_cur ; 
                delete from neweb_contract_expand_card_line where expand_card_id = lineid ;
                open expcard_cur for select * from neweb_contract_expand_card_line where expand_card_id = conl_rec.id ;
                loop
                  fetch expcard_cur into expcard_rec ;
                  exit when not found ;
                  insert into neweb_contract_expand_card_line(expand_card_id,expand_card_item,expand_card_no,expand_card_num) values(lineid,expcard_rec.expand_card_item,expcard_rec.expand_card_no,expcard_rec.expand_card_num) ;
                end loop;
                close expcard_cur ;  
                delete from neweb_contract_power_line where power_id = conl_rec.id ;
                open power_cur for select * from neweb_contract_power_line where power_id = conl_rec.id ;
                loop
                  fetch power_cur into power_rec ;
                  exit when not found ;
                  insert into neweb_contract_power_line(power_id,power_item,power_no,power_num) values(lineid,power_rec.power_item,power_rec.power_no,power_rec.power_num) ;
                end loop;
                close power_cur ;
             end loop ;
             close conl_cur ;   
           end loop ;
           close consl_cur ; 
           delete from neweb_contract_contract_selline ;
           delete from neweb_contract_contract_sel ;
         END;$BODY$
         LANGUAGE plpgsql;""")






