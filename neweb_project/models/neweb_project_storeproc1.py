# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebprojectstoreproc(models.Model):
    _name = "neweb.projectstoreproc1"

    @api.model
    def init(self):
        #  專案成本分析計算store procedure
        self._cr.execute("""DROP FUNCTION IF EXISTS proj_cal_prodset(proj_id int) cascade;""")
        self._cr.execute("""create or replace function proj_cal_prodset(proj_id int) returns void as $BODY$
         declare
      proj_saleitem_cur cursor is select DISTINCT prod_set from neweb_projsaleitem where saleitem_id = proj_id and prod_num > 0 ;
      saleitem_rec record;
      ncount integer ;
      myprodpricetot FLOAT ;
      myprodrevenuetot FLOAT ;
    BEGIN 
      delete from neweb_projprodset where prodset_id = proj_id ;
      open proj_saleitem_cur ;
      loop
        fetch proj_saleitem_cur into saleitem_rec ;
        exit when not found;
        select count(*) into ncount from neweb_projprodset where prodset_id=proj_id and prod_set=saleitem_rec.prod_set ;
        if ncount = 0 THEN 
           insert into neweb_projprodset(prodset_id,prod_set) values (proj_id,saleitem_rec.prod_set);
        end if ;
        select sum(prod_num * prod_price),sum(prod_num * prod_revenue) into myprodpricetot,myprodrevenuetot from 
            neweb_projsaleitem where saleitem_id = proj_id and prod_set=saleitem_rec.prod_set ;
        update neweb_projprodset set prod_price_tot=myprodpricetot,prod_revenue_tot=myprodrevenuetot WHERE 
            prodset_id=proj_id and prod_set = saleitem_rec.prod_set ;    
      end loop;
      close proj_saleitem_cur ;
   END;$BODY$
   LANGUAGE plpgsql;   """)

        self._cr.execute("""DROP FUNCTION IF EXISTS proj_delsaleitem_cost(proj_id int) cascade;""")
        self._cr.execute("""create or replace function proj_delsaleitem_cost(proj_id int) returns void as $BODY$
              BEGIN 
                delete from neweb_projanalysis where analysis_id=proj_id ;
                delete from neweb_setupcost_line where project_id=proj_id ;
                delete from neweb_maincost_line where project_id=proj_id ;
                update neweb_project set proj_status='Balance',proj_status1='Balance' where id = proj_id ;
                
                /* update neweb_project set total_analysis_cost=0,total_analysis_profit=0,
                                         total_analysis_profitrate=0 where id=proj_id ; */
              END ;$BODY$
              LANGUAGE plpgsql;                          
        """)


        self._cr.execute("""drop function if exists sale_drop_messagefollower(saleid int) cascade;""")
        self._cr.execute("""create or replace function sale_drop_messagefollower(saleid int) returns void as $BODY$
                BEGIN 
                   delete from mail_followers where res_model='sale.order' and res_id=saleid ;
                END ;$BODY$
                LANGUAGE plpgsql;""")

        self._cr.execute("drop function if exists update_discount_amount(saleid int) cascade;")
        self._cr.execute("""create or replace function update_discount_amount(saleid int) returns void as $BODY$
               DECLARE 
                 ncount INTEGER ;
                 untaxamount FLOAT ;
                 taxamount FLOAT ;
                 taxamount1 FLOAT;
               BEGIN 
                 select sum(sitem_num*sitem_price) into untaxamount from neweb_sitem_list where sitem_id=saleid ;
                 taxamount := round(untaxamount * 0.05) + untaxamount ;
                 select sitem_amounttot into taxamount1 from sale_order where id=saleid ;
                 if taxamount1=0 or taxamount1 is null then 
                    update sale_order set discount_amount=taxamount where id=saleid;
                 else 
                    update sale_order set discount_amount=taxamount1 where id=saleid;
                 end if ;
               END ;$BODY$
               LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_warrantyyn(projid int) cascade;""")
        self._cr.execute("""create or replace function check_warrantyyn(projid int) returns CHAR as $BODY$
               declare
                 ncount int ;
                 mytext varchar;
                 mydate DATE;
                 mytype CHAR ;
                 myimportstatus Boolean;
               begin
                 mytype := '0' ;
                 select count(*) into ncount from neweb_project where id=projid and origin_warranty_desc is null 
                   and neweb_manpower_desc is null and neweb_warranty_desc is null and other_warranty_desc is null ;
                 select proj_import_status into myimportstatus from neweb_project where id = projid ;  
                 if ncount > 0 and myimportstatus=FALSE then
                    mytype := '1' ;
                 else
                    mytype := '0' ;   
                 end if ;
                 select count(*) into ncount from neweb_project where id=projid and 
                    (warranty_start_date is null or warranty_end_date is null) ; 
                 if ncount > 0 then
                    mytype := '2' ;
                 else
                    mytype := '0' ;   
                 end if ;   
                 return mytype ;
              END ; $BODY$
              LANGUAGE plpgsql;   
                   """)

        self._cr.execute("""drop function if exists check_opentrender(projid int) cascade;""")
        self._cr.execute("""create or replace function check_opentrender(projid int) returns CHAR as $BODY$
                       declare
                         ncount int ;
                         mytext varchar;
                         mydate DATE;
                         mytype CHAR ;
                         myimportstatus Boolean ;
                       begin
                         mytype := '0' ;
                         select count(*) into ncount from neweb_project where id=projid and decision_date is null 
                           and acceptance_step is null and complete_days is null and send_letter_date is null 
                           and acceptance_date is null and acceptance_other_desc is null  ;
                           select proj_import_status into myimportstatus from neweb_project where id = projid ;
                         if ncount > 0 and myimportstatus=FALSE then
                            mytype := '1' ;
                         else
                            mytype := '0' ;   
                         end if ;
                            
                         return mytype ;
                      END ; $BODY$
                      LANGUAGE plpgsql;   
                           """)

        self._cr.execute("""drop function if exists check_maintenanceyn(projid int) cascade;""")
        self._cr.execute("""create or replace function check_maintenanceyn(projid int) returns CHAR as $BODY$
                               declare
                                 ncount int ;
                                 mytext varchar;
                                 mydate DATE;
                                 mytype CHAR ;
                                 myimportstatus Boolean;
                               begin
                                 mytype := '0' ;
                                 select count(*) into ncount from neweb_project where id=projid 
                                   and main_start_date is null and main_end_date is null and 
                                   old_contact_revenue=0.00 and old_contact_cost=0.00 and main_other is null  ;
                                   select proj_import_status into myimportstatus from neweb_project where id = projid ;
                                 if ncount > 0 and myimportstatus=FALSE then
                                    mytype := '1' ;
                                 else
                                    mytype := '0' ;   
                                 end if ;

                                 return mytype ;
                              END ; $BODY$
                              LANGUAGE plpgsql;   
                                   """)

        self._cr.execute("""drop function if exists check_projectyn(projid int) cascade;""")
        self._cr.execute("""create or replace function check_projectyn(projid int) returns CHAR as $BODY$
                                       declare
                                         ncount int ;
                                         mytext varchar;
                                         mydate DATE;
                                         mytype CHAR ;
                                         myimportstatus Boolean;
                                       begin
                                         mytype := '0' ;
                                         select count(*) into ncount from neweb_project where id=projid and proj_step is null 
                                           and proj_complete_days is null and proj_acceptance_date is null and proj_paytype is null   
                                           and proj_other_desc is null ;
                                         select proj_import_status into myimportstatus from neweb_project where id = projid ;  
                                         if ncount > 0 and myimportstatus=FALSE then 
                                            mytype := '1' ;
                                         else
                                            mytype := '0' ;   
                                         end if ;
                                         return mytype ;
                                      END ; $BODY$
                                      LANGUAGE plpgsql;   
                                           """)

        self._cr.execute("""drop function if exists getprodset1(myprodset VARCHAR) cascade;""")
        self._cr.execute("""create or replace function getprodset1(myprodset VARCHAR) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select max(id) into myres from neweb_prodset where name1 = myprodset  ;
            return myres ;
          END ;$BODY$
          LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists getprodbrand1(myprodbrand VARCHAR) cascade;""")
        self._cr.execute("""create or replace function getprodbrand1(myprodbrand VARCHAR) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select max(id) into myres from neweb_prodbrand where name = myprodbrand and active=True ;
            return myres ;
          END ;$BODY$
          LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists getcosttype1(mycosttype VARCHAR) cascade;""")
        self._cr.execute("""create or replace function getcosttype1(mycosttype VARCHAR) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select max(id) into myres from neweb_costtype where name = mycosttype ;
            return myres ;
          END ;$BODY$
          LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists setcontactaddress(myprojid int) cascade;""")
        self._cr.execute("""drop function if exists setcontactaddress(mysaleid int) cascade;""")
        self._cr.execute("""create or replace function setcontactaddress(mysaleid int) returns void as $BODY$
               declare 
                  ncount int;
                  ncount1 int ;
                  mycontactid int ;
                  mypartnerid int ;
                  myaddress varchar ;
               begin 
                  select count(*) into ncount from sale_order where id=mysaleid and contact_address is not null ;
                  if ncount > 0 then 
                     select contact_address into mycontactid from sale_order where id=mysaleid ;
                     select street into myaddress from res_partner where id=mycontactid ;
                     update sale_order set quotation_address=myaddress where id=mysaleid ;
                  else 
                     select count(*) into ncount1 from sale_order where id=mysaleid and contact_id is not null ;
                     if ncount1 > 0 then
                        select contact_id into mycontactid from sale_order where id=mysaleid ;
                        select street into myaddress from res_partner where id=mycontactid ;
                        update sale_order set quotation_address=myaddress where id=mysaleid ;
                     else 
                        select partner_id into mycontactid from sale_order where id=mysaleid ;
                        select street into myaddress from res_partner where id=mycontactid ;
                        update sale_order set quotation_address=myaddress where id=mysaleid ;
                     end if ;
                  end if ;
               end; $BODY$
               LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists cancel_saleorderline(saleorderid int) cascade""")
        self._cr.execute("""create or replace function cancel_saleorderline(saleorderid int) returns void as $BODY$
               declare 
                  ncount int ;
               begin 
                 select count(*) into ncount from sale_order where id=saleorderid ;
                 if ncount >0 then
                     delete from neweb_sitem_list where sitem_id = saleorderid ;
                     update sale_order set amount_untaxed=0,amount_tax=0,amount_total=0,sitem_untax=0,sitem_tax=0,sitem_amounttot=0,
                        discount_amount=0 where id=saleorderid ;
                 end if ;        
               end ; $BODY$
               LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists get_partnercloseday(partnerid int) cascade;""")
        self._cr.execute("""create or replace function get_partnercloseday(partnerid int) returns VARCHAR as $BODY$
               DECLARE
                 ncount int ;
                 checkoutday int ;
                 myacc_close_days VARCHAR;
               BEGIN
                 select count(*) into ncount from res_partner where id = partnerid ;
                 if ncount > 0 then
                    select checkout_date into checkoutday from res_partner where id = partnerid ;
                    if checkoutday > 0 then 
                       select concat(to_char(checkoutday,'999'),' 日') into myacc_close_days ;
                    else 
                       myacc_close_days := '-' ;  
                    end if ;
                 else   
                    myacc_close_days := '-' ; 
                 end if ;
                 return myacc_close_days ;
               END ; $BODY$
               LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprojhaspurchase(projid int) cascade;""")
        self._cr.execute("""create or replace function getprojhaspurchase(projid int) returns Boolean as $BODY$
               DECLARE 
                  ncount int;
                  myres Boolean ;
               BEGIN 
                  select count(*) into ncount from neweb_projsaleitem where saleitem_id = projid and purchase_no is not null  ;
                  if ncount > 0 then 
                     myres := True ;
                  else 
                     myres := False ;
                  end if ;
                  return myres ;
               END;$BODY$
               LANGUAGE plpgsql; """)

        self._cr.execute("""drop function if exists getsaleowner(partnerid int) cascade;""")
        self._cr.execute("""create or replace function getsaleowner(partnerid int) returns int as $BODY$
               DECLARE 
                  ncount int ;
                  myuserid int ;
                  myempid int ;
                  myresourceid int ;
               BEGIN 
                  myuserid := 0 ;
                  select max(hr_employee_id) into myempid from hr_employee_res_partner_rel where res_partner_id=partnerid ;
                  select resource_id into myresourceid from hr_employee where id = myempid ;
                  select user_id into myuserid from resource_resource where id = myresourceid ;
                  if myuserid is null then 
                     myuserid := 0 ;
                  end if ;
                  return myuserid ;   
               END;$BODY$
               LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists allparuserid() cascade;""")
        self._cr.execute("""create or replace function allparuserid() returns void as $BODY$
               DECLARE 
                 par_cur refcursor ;
                 par_rec record ;
                 ncount int ;
                 myuserid int ;
               BEGIN 
                 open par_cur for select * from res_partner where is_company = TRUE and customer = TRUE ;
                 loop
                   fetch par_cur into par_rec ;
                   exit when not found ;
                   select getsaleowner(par_rec.id) into myuserid ;
                   if myuserid > 0 then 
                      update res_partner set user_id = myuserid where id = par_rec.id ;
                   else 
                      update res_partner set user_id = null where id = par_rec.id ;  
                   end if ;
                 end loop ;
                 close par_cur ;                 
               END;$BODY$
               LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists regenengsetupprod(engid int) cascade""")
        self._cr.execute("""create or replace function regenengsetupprod(engid int) returns void as $BODY$
           DECLARE
             proj_cur refcursor ;
             proj_rec record ;
             ncount int ;
             projid int ;
             mymaxid int ;
           BEGIN
             select proj_no into projid from neweb_proj_eng_assign where id = engid ;
             delete from neweb_setup_prod where setup_id = engid ;
             open proj_cur for select * from neweb_projsaleitem where saleitem_id = projid order by id ;
             loop
               fetch proj_cur into proj_rec ;
               exit when not found ;
               insert into neweb_setup_prod (setup_id,prod_modeltype,prod_serial,prod_no,prod_desc,prod_num) values
                 (engid,coalesce(proj_rec.prod_modeltype,' '),coalesce(proj_rec.prod_serial,' '),
                 coalesce(proj_rec.prod_no,' '),coalesce(proj_rec.prod_desc,' '),coalesce(proj_rec.prod_num,0)) ;
               select max(id) into mymaxid from  neweb_setup_prod ;
               if proj_rec.prod_set is not null then
                  update neweb_setup_prod set prod_set = proj_rec.prod_set where id = mymaxid ;
               end if ; 
             end loop ;
             close proj_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setallsequence() cascade""")
        self._cr.execute("""create or replace function setallsequence() returns void as $BODY$
           DECLARE
             ncount int ;
           BEGIN
             update neweb_buscate set sequence=20 where sequence is null ;
             update neweb_transationtype set sequence=20 where sequence is null ;
             update neweb_contacttype set sequence=20 where sequence is null ;
             update neweb_prodset set sequence=20 where sequence is null ;
             update neweb_prodbrand set sequence=20 where sequence is null ;
             update neweb_projmaintype set sequence=20 where sequence is null ;
             update neweb_engmaintype set sequence=20 where sequence is null ;
             update neweb_warranty_service_rule set sequence=20 where sequence is null ;
             update neweb_payment_term_rule set sequence=20 where sequence is null ;
             update neweb_main_service_rule set sequence=20 where sequence is null ;
             update neweb_quotation_include set sequence=20 where sequence is null ;
             update neweb_call_service_response set sequence=20 where sequence is null ;
             update neweb_costtype set sequence=20 where sequence is null;
             update neweb_ass_service_mode set sequence=20 where sequence is null ;
             update neweb_ass_service_type set sequence=20 where sequence is null ;
             update neweb_routine_maintenance set sequence=20 where sequence is null ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getengsetupdesc1(engid int) cascade""")
        self._cr.execute("""create or replace function getengsetupdesc1(engid int) returns INT as $BODY$
         DECLARE
           set_cur refcursor ;
           set_rec record ;
           myres int ;
         BEGIN
           myres=0 ;
           open set_cur for select * from neweb_engmaintype_neweb_proj_eng_assign_rel where neweb_proj_eng_assign_id = engid ;
           loop
             fetch set_cur into set_rec ;
             exit when not found ;
             if set_rec.neweb_engmaintype_id=1 then
                myres = 1 ;
             end if ;
           end loop ;
           close set_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getengsetupdesc2(engid int) cascade""")
        self._cr.execute("""create or replace function getengsetupdesc2(engid int) returns INT as $BODY$
         DECLARE
           set_cur refcursor ;
           set_rec record ;
           myres int ;
         BEGIN
           myres=0 ;
           open set_cur for select * from neweb_engmaintype_neweb_proj_eng_assign_rel where neweb_proj_eng_assign_id = engid ;
           loop
             fetch set_cur into set_rec ;
             exit when not found ;
             if set_rec.neweb_engmaintype_id=2 then
                myres = 2 ;
             end if ;
           end loop ;
           close set_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmainsuprev(projid int) cascade""")
        self._cr.execute("""create or replace function genmainsuprev(projid int) returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           supcost float ;
           
         BEGIN
           select count(*) into ncount from neweb_maincost_line where name in ('2','3','4') and support_revenue > 0 and project_id=projid ;
           if ncount > 0 then
              select sum(support_revenue) into supcost from neweb_maincost_line  where name in ('2','3','4')  and project_id=projid ;
              select count(*) into ncount1 from neweb_maincost_line where name='1' and project_id=projid ;
              if ncount1 = 0 then
                 insert into neweb_maincost_line(name,project_id) values ('1',projid) ;
              end if ;
              update neweb_maincost_line set r6_revenue=(coalesce(r6_revenue,0) - supcost),support_revenue=supcost where name='1' and project_id=projid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chksono(sono varchar) cascade""")
        self._cr.execute("""create or replace function chksono(sono varchar) returns varchar as $BODY$
         DECLARE
           maxso varchar ;
           presono varchar ;
           maxcode varchar ;
           maxnum int ;
           ncount int ;
           myres varchar ;
         BEGIN
           select count(*) into ncount from sale_order where name=sono ;
           if ncount >= 1 then
              select max(name) into maxso from sale_order where substring(name,1,8)=substring(sono,1,8);
              select substring(sono,1,8) into presono ;
              select substring(maxso,9,2) into maxcode ;
              maxnum = maxcode::int + 1 ;
              myres = concat(presono,lpad(maxnum::TEXT,2,'0')) ;
              update ir_sequence set number_next=maxnum + 1 where code='sale.order' ;
           else
              myres = sono ;   
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genovergencode(projno varchar) cascade""")
        self._cr.execute("""create or replace function genovergencode(projno varchar) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            myprefix varchar ;
            myym varchar ;
            myprojno varchar ;
            mymaxprojno varchar ;
            myseq int ;
          BEGIN
            select substring(projno,1,9) into myprojno ;
            select max(name) into mymaxprojno from neweb_project where name like '%'|| myprojno ||'%' ;
            select substring(projno,1,1) into myprefix ;
            select substring(projno,5,4) into myym ;
            select substring(mymaxprojno,10,3)::INT into myseq ;
            update neweb_projgencode set gencode=myseq+1 where name=myym and prefixcode=myprefix ;
            myres = concat(myprojno,lpad((myseq+1)::TEXT,3,'0')) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")




