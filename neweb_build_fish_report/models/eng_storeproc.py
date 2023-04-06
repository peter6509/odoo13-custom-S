# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
class newebbuildfishstoreproc(models.Model):
    _name = "neweb_build_fish_report.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getengprojno(engid int) cascade""")
        self._cr.execute("""create or replace function getengprojno(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           projid int ;
         BEGIN
           select proj_no into projid from neweb_proj_eng_assign where id = engid ;
           select name into myres from neweb_project where id = projid ;
           if myres is null then
              myres = ' ' ;   
           end if ;
           return myres ;
           END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getengprojcusname(engid int) cascade""")
        self._cr.execute("""create or replace function getengprojcusname(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           partnerid int ;
           assigntype char ;
         BEGIN
           select proj_cus_name,assign_type into partnerid,assigntype from neweb_proj_eng_assign where id = engid ;
           if assigntype='1' then
              select proj_cus_name1 into myres from neweb_proj_eng_assign where id = engid ;
           else
              select name into myres from res_partner where id = partnerid ;
           end if ;
           if myres is null then
              myres = ' ' ;   
           end if ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getengprojsalename(engid int) cascade""")
        self._cr.execute("""create or replace function getengprojsalename(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           empid int ;
         BEGIN
           select proj_sale into empid from neweb_proj_eng_assign where id = engid ;
           select name into myres from hr_employee where id = empid ;
           if myres is null then
              myres = ' ' ;   
           end if ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getengsetupcontact(engid int) cascade""")
        self._cr.execute("""create or replace function getengsetupcontact(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           partnerid int ;
           con_cur refcursor ;
           con_rec record ;
         BEGIN
           select setup_contact into partnerid from neweb_proj_eng_assign where id = engid ;
           if partnerid is null then
              select setup_contact1 into myres from neweb_proj_eng_assign where id = engid ;
           else
              select name into myres from res_partner where id = partnerid ;    
           end if ;
           if myres is null then
              myres = ' ' ;   
           end if ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getengassignman(engid int) cascade""")
        self._cr.execute("""create or replace function getengassignman(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           partnerid int ;
           myname varchar ;
           ass_cur refcursor ;
           ass_rec record ;
         BEGIN
           myres='' ;
           open ass_cur for select * from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id = engid ;
           loop
             fetch ass_cur into ass_rec ;
             exit when not found ;
             select partner_id into partnerid from res_users where id = ass_rec.res_users_id ;
             select name into myname from res_partner where id = partnerid ;
             if myres ='' then
                myres = myname ;
             else
                myres = concat(myres,'/',myname) ;
             end if ;   
           end loop;
           close ass_cur ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getengservicename(engid int) cascade""")
        self._cr.execute("""create or replace function getengservicename(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           serviceid int ;
         BEGIN
           select service_name into serviceid from neweb_proj_eng_assign where id = engid ;
           select name into myres from neweb_ass_service_mode where id = serviceid ;
           if myres is null then
              myres = ' ' ;   
           end if ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists getengservicetypename(engid int) cascade""")
        self._cr.execute("""create or replace function getengservicetypename(engid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           serviceid int ;
           myname varchar ;
           ser_cur refcursor ;
           ser_rec record ;
         BEGIN
           myres='' ;
           open ser_cur for select * from neweb_ass_service_type_neweb_proj_eng_assign_rel where neweb_proj_eng_assign_id = engid ;
           loop
             fetch ser_cur into ser_rec ;
             exit when not found ;
             select name into myname from neweb_ass_service_type where id = ser_rec.neweb_ass_service_type_id ;
             if myres ='' then
                myres = myname ;
             else
                myres = concat(myres,'/',myname) ;
             end if ;   
           end loop;
           close ser_cur ;
           return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists insert_bfrepair_line(repairid int) cascade""")
        self._cr.execute("""create or replace function insert_bfrepair_line(repairid int) returns void as $BODY$
          DECLARE
            ncount int ;
            rep_cur refcursor ;
            rep_rec record ;
            prodmodel varchar ;
            machno varchar ;
            prodtmplid int ;
            prodname1 varchar ;
            prodspec1 varchar ;
            defcode varchar ;
            usedqty1 varchar ;
            reqqty1 varchar ;
          BEGIN
            open rep_cur for select R.repair_id,R.contract_line,P.prod,P.used_parts_qty,P.required_parts_qty from neweb_repair_repair_line R left join neweb_repair_repair_part P
               on R.id = P.repair_line_id where R.repair_id = repairid ;
            loop
              fetch rep_cur into rep_rec ;
              exit when not found ;
              select coalesce(machine_serial_no,' '),coalesce(prod_modeltype,' ') into machno,prodmodel 
                      from neweb_contract_contract_line where id = rep_rec.contract_line ;
              select product_tmpl_id into prodtmplid from product_product where id = rep_rec.prod ;
              select coalesce(name,' '),coalesce(specification,' '),(default_code,' ') into prodname1,prodspec1,defcode from product_template where id = prodtmplid ; 
             /* if defcode != ' ' then
                 prodname1 = concat('[',defcode,']',prodname1) ;
              end if ; */
              select count(*) into ncount from neweb_repair_bfrepair_line where repair_id=repairid and machine_serial_no=machno and prodname=prodname1 ;
              if ncount = 0 then
                 if rep_rec.used_parts_qty = 0 then
                    usedqty1 = ' ' ;
                 else
                    usedqty1 = rep_rec.used_parts_qty::TEXT ;
                 end if ;
                 if rep_rec.required_parts_qty = 0 then
                    reqqty1 = ' ' ;
                 else
                    reqqty1 = rep_rec.required_parts_qty::TEXT ;
                 end if ;
                 insert into neweb_repair_bfrepair_line(repair_id,prod_modeltype,machine_serial_no,prodname,prodspec,usedqty,requiredqty) values
                   (repairid,prodmodel,machno,prodname1,prodspec1,usedqty1,reqqty1) ;
              end if ;        
            end loop ;
            close rep_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_bfrepair_line(repairid int) cascade""")
        self._cr.execute("""create or replace function update_bfrepair_line(repairid int) returns void as $BODY$
          DECLARE
            ncount int ;
            rep_cur refcursor ;
            rep_rec record ;
            prodmodel varchar ;
            machno varchar ;
            prodtmplid int ;
            prodname1 varchar ;
            prodspec1 varchar ;
            usedqty1 varchar ;
            reqqty1 varchar ;
          BEGIN
            update neweb_repair_bfrepair_line set update_tag=False where repair_id=repairid ;
            open rep_cur for select R.repair_id,R.contract_line,P.prod,P.used_parts_qty,P.required_parts_qty from neweb_repair_repair_line R left join neweb_repair_repair_part P
               on R.id = P.repair_line_id where R.repair_id = repairid ;
            loop
              fetch rep_cur into rep_rec ;
              exit when not found ;
              select coalesce(machine_serial_no,' '),coalesce(prod_modeltype,' ') into machno,prodmodel 
                      from neweb_contract_contract_line where id = rep_rec.contract_line ;
              select product_tmpl_id into prodtmplid from product_product where id = rep_rec.prod ;
              select coalesce(name,' '),coalesce(specification,' ') into prodname1,prodspec1 from product_template where id = prodtmplid ; 
              select count(*) into ncount from neweb_repair_bfrepair_line where repair_id=repairid and machine_serial_no=machno and prodname=prodname1 ;
              if rep_rec.used_parts_qty = 0 then
                 usedqty1 = ' ' ;
              else
                 usedqty1 = rep_rec.used_parts_qty::TEXT ;
              end if ;
              if rep_rec.required_parts_qty = 0 then
                 reqqty1 = ' ' ;
              else
                 reqqty1 = rep_rec.required_parts_qty::TEXT ;
              end if ;   
              if ncount = 0 then
                 insert into neweb_repair_bfrepair_line(repair_id,prod_modeltype,machine_serial_no,prodname,prodspec,usedqty,requiredqty,update_tag) values
                   (repairid,prodmodel,machno,prodname1,prodspec1,usedqty1,reqqty1,True) ;
              else
                 update neweb_repair_bfrepair_line set usedqty=usedqty1,requiredqty=reqqty1,update_tag=True where repair_id=repairid and machine_serial_no=machno and prodname=prodname1 ;     
              end if ;        
            end loop ;
            delete from neweb_repair_bfrepair_line where repair_id=repairid and update_tag=False ;
            close rep_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallbfrepairline() cascade""")
        self._cr.execute("""create or replace function genallbfrepairline() returns void as $BODY$
         DECLARE
           rep_cur refcursor;
           rep_rec record ;
         BEGIN
           open rep_cur for select id from neweb_repair_repair ;
           loop
             fetch rep_cur into rep_rec ;
             exit when not found ;
             execute insert_bfrepair_line(rep_rec.id) ;
           end loop ;
           close rep_cur;
         END;$BODY$
         LANGUAGE plpgsql;""")

