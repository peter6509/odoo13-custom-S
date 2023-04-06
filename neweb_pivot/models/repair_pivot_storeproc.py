# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class newebpivotstoreproc(models.Model):
    _name = "neweb_pivot.store_proc"


    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS get_repairae_dept(empid int) cascade;""")
        self._cr.execute("""create or replace function get_repairae_dept(empid int) returns int as $BODY$
         declare
           ncount int ;
           deptid int;
         BEGIN
           select department_id into deptid from hr_employee where id=empid;
           if deptid is null then 
              deptid := 150 ;
           end if ;
           return deptid ;
          
         end; $BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS get_sale_dept(empid int) cascade;""")
        self._cr.execute("""create or replace function get_sale_dept(empid int) returns int as $BODY$
            declare
              ncount int ;
              deptid int;
            BEGIN
              select department_id into deptid from hr_employee where id=empid;
              if deptid is null then 
                 deptid := 148 ;
              end if ;
              return deptid ;

            end; $BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_vendor_sname(supplierid int) cascade""")
        self._cr.execute("""create or replace function get_vendor_sname(supplierid int) returns VARCHAR as $BODY$
                DECLARE 
                  ncount int ;
                  mycompsname varchar ;
                BEGIN 
                  select coalesce(comp_sname,' ') into mycompsname from res_partner where id=supplierid ;
                  return mycompsname ;
                END;$BODY$
                LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getparts(prodid int) cascade;""")
        self._cr.execute("""create or replace function getparts(prodid int) returns varchar as $BODY$
                DECLARE 
                  mytempid int ;
                  ncount int ;
                  myparts varchar ;
                  myname varchar ;
                  myspec varchar ;
                BEGIN
                myparts := 'No Parts' ;
                select count(*) into ncount from product_product where id = prodid ;
                  if ncount > 0 then 
                     select product_tmpl_id into mytempid from product_product where id = prodid ;
                     select name,specification into myname,myspec from product_template where 
                         id = mytempid ;
                     select concat(myname,'-') into myparts ;
                     select concat(myparts,myspec) into myparts ;    
                  end if ;    
                  return myparts ;   
                END;$BODY$
                LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists getprodset(setid int) cascade;""")
        self._cr.execute("""create or replace function getprodset(setid int) returns varchar as $BODY$
                 DECLARE 
                    myres varchar ;
                    ncount int ;
                 BEGIN 
                    myres := 'NO_PRODSET' ;
                    select count(*) into ncount from neweb_prodset where id = setid ;
                    if ncount > 0 then 
                       select name into myres from neweb_prodset where id = setid ;
                    end if ;
                    return myres ;
                 END;$BODY$
                 LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprodbrand(brandid int) cascade;""")
        self._cr.execute("""create or replace function getprodbrand(brandid int) returns varchar as $BODY$
                         DECLARE 
                            myres varchar ;
                            ncount int ;
                         BEGIN 
                            myres := 'NO_PRODBRAND' ;
                            select count(*) into ncount from neweb_prodbrand where id = brandid ;
                            if ncount > 0 then 
                               select name into myres from neweb_prodbrand where id = brandid ;
                            end if ;
                            return myres ;
                         END;$BODY$
                         LANGUAGE plpgsql;""")





