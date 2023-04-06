# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class migrationstoreproc1(models.Model):
    _name = "neweb_migration.storeproc1"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists check_partner_status(parid int,parentid int) cascade""")
        self._cr.execute("""create or replace function check_partner_status(parid int,parentid int) returns Char as $BODY$
         DECLARE
           myres char ;
           ncount int ;
           ncount1 int ;
           ncount3 int ;
           ncount4 int ;
           ncount5 int ;
           myvat varchar ;
           mymaxid int ;
           mymaxid1 int ;
           myname varchar ;
         BEGIN
           select count(*) into ncount4 from res_partner where id = parid ;
           if ncount4 > 0 then
               select count(*) into ncount from res_partner where id=parentid and active=True and is_company=True;
               if ncount > 0 then
                  myres = '0' ;   /* 正常資料 */
               else
                  select count(*) into ncount1 from res_partner where id=parentid and active=False and is_company=True;
                  if ncount1 > 0 then   /* 公司資料歸檔狀態 */
                     select max(id) into mymaxid from res_partner where id=parentid and active=False and is_company=True;
                     select trim(name) into myname from res_partner where id=mymaxid ;
                     /* select substring(trim(vat),1,8) into myvat from res_partner where id=mymaxid ; */
                     /* select max(id) into mymaxid1 from res_partner where substring(vat,1,8)=myvat and active=True and is_company=True; */
                     select max(id) into mymaxid1 from res_partner where name like '%'|| myname ||'%' and active=True and is_company=True;
                     if mymaxid1 is not null then  /* 有新的正常公司資料 */
                        update res_partner set parent_id=mymnaxid1,active=True where id = parid ; 
                        myres = '1' ;  /* 變更過公司資料,變更 parent_id */
                     end if ;
                  end if ;
               end if ;
           else
              select count(*) into ncount5 from res_partner where id = parentid and is_company=True ;
              if ncount5 > 0 then
                 myres = '2' ;  /* 聯絡人不存在,公司資料已歸檔 */
              end if ;    
           end if ;   
           return myres ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gennewpardata(contacttype int,cname varchar,ctitle int,cfunction varchar,cemail varchar,surveymark Boolean,cphone varchar,cfax varchar,cmobile varchar,ccomment varchar,birmonth int,birday int,pname varchar) cascade""")
        self._cr.execute("""create or replace function gennewpardata(contacttype int,cname varchar,ctitle int,cfunction varchar,cemail varchar,surveymark Boolean,cphone varchar,cfax varchar,cmobile varchar,ccomment varchar,birmonth int,birday int,pname varchar) returns void as $BODY$
          DECLARE
            ncount int ;
            maxid int ;
          BEGIN
            select count(*) into ncount from res_partner where name like '%'|| pname ||'%' and is_company=True and active=True ;
            maxid = 0 ;
            if ncount > 0 then
               select max(id) into maxid from res_partner where name like '%'|| pname ||'%' and is_company=True and active=True ;
               if maxid > 0 then
                  insert into res_partner(parent_id,is_company,contact_type,name,title,function,email,survey_mark,phone,fax,mobile,comment,birthday_month,birthday_day) values
                  (maxid,False,contacttype,cname,ctitle,cfunction,cemail,surveymark,cphone,cfax,cmobile,ccomment,birmonth,birday) ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_purchase_reciver(purid int,reciver varchar) cascade""")
        self._cr.execute("""create or replace function check_purchase_reciver(purid int,reciver varchar) returns void as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           select count(*) into ncount from purchase_order where id=purid ;
           if ncount > 0 then
              update purchase_order set purchase_reciver=reciver where id=purid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists check_partner_status1(myid int,parid int,myname varchar) cascade""")
        self._cr.execute("""create or replace function check_partner_status1(myid int,parid int,myname varchar) returns INT as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           myid int ;
           myres int ;
           myname1 varchar ; 
         BEGIN
           select count(*) into ncount from res_partner where id=parid and is_company=True;
           if ncount > 0 then
              select name into myname1 from res_partner where id=parid and is_company=True;
              select count(*) into ncount1 from res_partner where name=myname1 and active=True and is_company=True;
              if ncount1 > 0 then
                 select max(id) into myid from res_partner where name=myname1 and active=True and is_company=True;
                 select count(*) into ncount2 from res_partner where parent_id=myid and name=myname ;
                 if ncount2 = 0 then
                    myres = 0 ;
                 else
                    myres = myid ;   
                 end if ;
              end if ;
           else
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")
