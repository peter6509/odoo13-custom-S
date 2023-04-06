# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class migrationstoreproc(models.Model):
    _name = "neweb_migration.storeproc"

    @api.model
    def init(self):

        self._cr.execute("""drop function if exists genempname() cascade""")
        self._cr.execute("""create or replace function 	genempname() returns void as $BODY$
          DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            myname varchar ;
          BEGIN
            open emp_cur for select id,resource_id,name from hr_employee ;
            loop
               fetch emp_cur into emp_rec ;
               exit when not found ;
               /* select substring(name,length(name)-2,6) into myname from resource_resource where id = emp_rec.resource_id ; */
               select name into myname from resource_resource where id = emp_rec.resource_id ;
               update hr_employee set name=coalesce(myname,' '),resource_calendar_id=1 where id=emp_rec.id ;
            end loop ;
            close emp_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genactiveemployee() cascade""")
        self._cr.execute("""create or replace function genactiveemployee() returns void as $BODY$
          DECLARE
            ncount int;
          BEGIN
            update hr_employee set active=False where resource_id in (select id from resource_resource where active=False) ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genirseq() cascade""")
        self._cr.execute("""create or replace function genirseq() returns void as $BODY$
          DECLARE
          BEGIN
            CREATE SEQUENCE if not exists ir_sequence_034 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_035 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_036 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_037 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_038 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_039 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_040 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_041 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_042 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_043 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_044 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_045 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_046 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_047 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_048 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_049 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_050 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_051 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_052 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_053 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_054 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_055 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_056 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_056 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_058 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_059 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_060 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_061 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_062 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_063 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_064 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_065 START 5000 ;
            CREATE SEQUENCE if not exists ir_sequence_066 START 5000 ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setrepairstate() cascade""")
        self._cr.execute("""create or replace function setrepairstate() returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update neweb_repair_repair set x_wkf_state='43' where state='repair_draft' ;
            update neweb_repair_repair set x_wkf_state='44' where state='repair_waiting' ;
            update neweb_repair_repair set x_wkf_state='45' where state='repair_AE' ;
            update neweb_repair_repair set x_wkf_state='46' where state='repair_Manager' ;
            update neweb_repair_repair set x_wkf_state='47' where state='repair_done' ;
            update neweb_repair_repair set x_wkf_state='48' where state='repair_closed' ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genstockparentpath() cascade""")
        self._cr.execute("""create or replace function genstockparentpath() returns void as $BODY$
         DECLARE
           p1_cur refcursor ;
           p1_rec record ;
           p2_cur refcursor ;
           p2_rec record ;
           p3_cur refcursor ;
           p3_rec record ;
           myid int ;
           myparentpath varchar ;
           myparentpath1 varchar ;
           myparentpath2 varchar ;
           myparentpath3 varchar ;
         BEGIN
           myid = 7 ;
           select parent_path into myparentpath from stock_location where id = myid ;
           open p1_cur for select id,parent_path,active,usage from stock_location where location_id = myid ;
           loop
             fetch p1_cur into p1_rec ;
             exit when not found ;
             myparentpath1 = concat(myparentpath,p1_rec.id::TEXT,'/') ;
             update stock_location set parent_path=myparentpath1 where id = p1_rec.id ;
             open p2_cur for select id,parent_path,active,usage from stock_location where location_id = p1_rec.id ;
             loop
               fetch p2_cur into p2_rec ;
               exit when not found ;
               myparentpath2 = concat(myparentpath1,p2_rec.id::TEXT,'/') ;
               update stock_location set parent_path=myparentpath2 where id = p2_rec.id ;
               open p3_cur for select id,parent_path,active,usage from stock_location where location_id = p2_rec.id ;
               loop
                 fetch p3_cur into p3_rec ;
                 exit when not found ;
                  myparentpath3 = concat(myparentpath2,p3_rec.id::TEXT,'/') ;
                  update stock_location set parent_path=myparentpath3 where id = p3_rec.id ;
               end loop ;
               close p3_cur ;
             end loop ;
             close p2_cur ;
           end loop ;
           close p1_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpartnerrank() cascade""")
        self._cr.execute("""create or replace function genpartnerrank() returns void as $BODY$
         DECLARE
           sale_cur refcursor ;
           sale_rec record ;
           pur_cur refcursor ;
           pur_rec record ;
         BEGIN
           open sale_cur for select distinct partner_id from sale_order ;
           loop
             fetch sale_cur into sale_rec ;
             exit when not found ;
             update res_partner set customer_rank=1 where id = sale_rec.partner_id ;
           end loop ;
           close sale_cur ;
           open pur_cur for select distinct partner_id from purchase_order ;
           loop
             fetch pur_cur into pur_rec ;
             exit when not found ;
             update res_partner set supplier_rank=1 where id = pur_rec.partner_id ;
           end loop ;
           close pur_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 產生 res_partner property_account_receivable_id & property_account_payable_id
        self._cr.execute("""drop function if exists genallpartnerproperty() cascade""")
        self._cr.execute("""create or replace function genallpartnerproperty() returns void as $BODY$
          DECLARE
            par_cur refcursor ;
            par_rec record ;
            myresid varchar ;
            ncount int ;
            ncount1 int ;
          BEGIN
            
            open par_cur for select id from res_partner where is_company=True and active=True ;
            loop
              fetch par_cur into par_rec ;
              exit when not found ;
              myresid = concat('res.partner,',par_rec.id::TEXT) ;
              delete from ir_property where name='property_account_receivable_id' and res_id=myresid ;
              delete from ir_property where name='property_account_payable_id' and res_id=myresid ;
              select count(*) into ncount from ir_property where name = 'property_account_receivable_id' and res_id=myresid ;
              if ncount = 0 then
                 insert into ir_property(name,res_id,company_id,fields_id,value_reference,type) values
                  ('property_account_receivable_id',myresid,1,2436,'account.account,50','many2one') ;
              end if ;
              select count(*) into ncount1 from ir_property where name = 'property_account_payable_id' and res_id=myresid ;
              if ncount1 = 0 then
                 insert into ir_property(name,res_id,company_id,fields_id,value_reference,type) values
                  ('property_account_payable_id',myresid,1,2428,'account.account,442','many2one') ;
              end if ;
            end loop ;
            close par_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists clear_dup_respartner() cascade""")
        self._cr.execute("""create or replace function clear_dup_respartner() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
           par1_cur refcursor ;
           par1_rec record ;
           nitem int ;
           ncount int ;
         BEGIN 
           open par_cur for select name from res_partner group by name having count(*) > 1 ;
           loop 
             fetch par_cur into par_rec ;
             exit when not found ;
            /* nitem=1 ;
             ncount = 0 ;
             open par1_cur for select id,name,employee from res_partner where name=par_rec.name order by id ;
             loop
               fetch par1_cur into par1_rec ;
               exit when not found ;
               if ncount > 0 then
                  update res_partner set name=concat(name,nitem::TEXT) where id = par1_rec.id ;
                  nitem = nitem + 1 ;
               end if ;
               ncount = ncount + 1 ;
             end loop ; 
             close par1_cur ; */
             update res_partner set active=False,name=concat(name,'_dup') where name=par_rec.name and id not in (select partner_id from res_users where active=true) ;
           end loop ;
           close par_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists clear_dup_respartner1() cascade""")
        self._cr.execute("""create or replace function clear_dup_respartner1() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
           par1_cur refcursor ;
           par1_rec record ;
           nitem int ;
           ncount int ;
         BEGIN 
            open par_cur for select vat from res_partner group by vat having count(*) > 1 ;
           loop 
             fetch par_cur into par_rec ;
             exit when not found ;
             nitem=1 ;
             ncount = 0 ;
             open par1_cur for select id,vat from res_partner where vat=par_rec.vat order by id ;
             loop
               fetch par1_cur into par1_rec ;
               exit when not found ;
               if ncount > 0 then
                  update res_partner set vat=concat(vat,nitem::TEXT) where id = par1_rec.id ;
                  nitem = nitem + 1 ;
               end if ;
               ncount = ncount + 1 ;
             end loop ;
             close par1_cur ;
           end loop ;
           close par_cur ;
          /* update res_partner set ref=vat ; */
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists clear_dup_respartner2() cascade""")
        self._cr.execute("""create or replace function clear_dup_respartner2() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
           par1_cur refcursor ;
           par1_rec record ;
           nitem int ;
           ncount int ;
         BEGIN 
            open par_cur for select ref from res_partner group by ref having count(*) > 1 ;
           loop 
             fetch par_cur into par_rec ;
             exit when not found ;
             nitem=1 ;
             ncount = 0 ;
             open par1_cur for select id,ref from res_partner where ref=par_rec.ref order by id ;
             loop
               fetch par1_cur into par1_rec ;
               exit when not found ;
               if ncount > 0 then
                  update res_partner set ref=concat(ref,nitem::TEXT) where id = par1_rec.id ;
                  nitem = nitem + 1 ;
               end if ;
               ncount = ncount + 1 ;
             end loop ;
             close par1_cur ;
           end loop ;
           close par_cur ;
           /* update res_partner set ref=vat ; */
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genempuserid() cascade""")
        self._cr.execute("""create or replace function genempuserid() returns void as $BODY$
         DECLARE
           ncount int ;
           myuserid int ;
           emp_cur refcursor ;
           emp_rec record ;
         BEGIN
           open emp_cur for select * from hr_employee where user_id is null ;
           loop
             fetch emp_cur into emp_rec ;
             exit when not found ;
             select coalesce(user_id,0) into myuserid from resource_resource where id = emp_rec.resource_id ;
             if myuserid > 0 then
                update hr_employee set user_id = myuserid where id=emp_rec.id ;
             end if ;
           end loop ;
           close emp_cur ;         
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gendeptcompletename() cascade""")
        self._cr.execute("""create or replace function gendeptcompletename() returns void as $BODY$
          DECLARE
            dept_cur refcursor ;
            dept_rec record ;
            myname varchar ;
          BEGIN
            open dept_cur for select * from hr_department where parent_id is null ;
            loop
              fetch dept_cur into dept_rec ;
              exit when not found ;
              update hr_department set complete_name=dept_rec.name where id=dept_rec.id ;
            end loop ;
            close dept_cur ;
            open dept_cur for select * from hr_department where parent_id in (select id from hr_department where complete_name is not null) and parent_id is not null;
            loop
              fetch dept_cur into dept_rec ;
              exit when not found ;
              select complete_name into myname from hr_department where id = dept_rec.parent_id ; 
              myname = concat(myname,'/',dept_rec.name) ;
              update hr_department set complete_name=myname where id=dept_rec.id ;
            end loop ;
            close dept_cur ;
            open dept_cur for select * from hr_department where parent_id in (select id from hr_department where complete_name is not null) and parent_id is not null;
            loop
              fetch dept_cur into dept_rec ;
              exit when not found ;
              select complete_name into myname from hr_department where id = dept_rec.parent_id ; 
              myname = concat(myname,'/',dept_rec.name) ;
              update hr_department set complete_name=myname where id=dept_rec.id ;
            end loop ;
            close dept_cur ;
            open dept_cur for select * from hr_department where parent_id in (select id from hr_department where complete_name is not null) and parent_id is not null;
            loop
              fetch dept_cur into dept_rec ;
              exit when not found ;
              select complete_name into myname from hr_department where id = dept_rec.parent_id ; 
              myname = concat(myname,'/',dept_rec.name) ;
              update hr_department set complete_name=myname where id=dept_rec.id ;
            end loop ;
            close dept_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists dupuser() cascade""")
        self._cr.execute("""create or replace function dupuser() returns void as $BODY$
         DECLARE
           ncount int ;
           minid int ;
           user_cur refcursor ;
           user_rec record ;
         BEGIN
           open user_cur for select distinct login from res_users where active=True ;
           loop
              fetch user_cur into user_rec ;
              exit when not found ;
              select count(*) into ncount from res_users where login=user_rec.login and active=True ;
              if ncount > 1 then
                 select min(id) into minid from res_users where login=user_rec.login and active=True ;
                 update res_users set login=concat(user_rec.login,'**'),active=False where login=user_rec.login and active=True and id != minid;
              end if ;
           end loop ;
           close user_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists ckcompuser() cascade""")
        self._cr.execute("""create or replace function ckcompuser() returns void as $BODY$
          DECLARE
           ncount int ;
           user_cur refcursor ;
           user_rec record ;
          BEGIN
           open user_cur for select id,active from res_users where active=True ;
           loop
             fetch user_cur into user_rec ;
             exit when not found ;
             select count(*) into ncount from res_company_users_rel where cid=1 and user_id=user_rec.id ;
             if ncount = 0 then
                insert into res_company_users_rel(cid,user_id) values (1,user_rec.id) ;
             end if ;
           end loop ;
           close user_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute(""" drop function if exists genseqcode() cascade""")
        self._cr.execute("""create or replace function genseqcode() returns void as $BODY$
          DECLARE
            myres varchar ;
          BEGIN
            update stock_picking_type set sequence_code='IN' where code='incoming' ;
            update stock_picking_type set sequence_code='OUT' where code='outgoing' ;
            update stock_picking_type set sequence_code='INT' where code='internal' ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists stockloc() cascade""")
        self._cr.execute("""create or replace function stockloc() returns void as $BODY$
         DECLARE
           loc_cur refcursor ;
           loc_rec record ;
           myppath varchar ;
           mypath varchar ;
         BEGIN
           open loc_cur for select * from stock_location where parent_path is null ;
           loop
             fetch loc_cur into loc_rec ;
             exit when not found ;
             select parent_path into myppath from stock_location where id=loc_rec.location_id ;
             mypath = concat(myppath,loc_rec.id::TEXT,'/') ;
             update stock_location set parent_path=mypath where id = loc_rec.id ; 
           end loop ;
           close loc_cur ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists prodcate() cascade""")
        self._cr.execute("""create or replace function prodcate() returns void as $BODY$
         DECLARE
           myppath varchar ;
           mypath varchar ;
           mypcompname varchar ;
           mycompname varchar ;
           cate_cur refcursor ;
           cate_rec record ;
           myparent int ;
           mypp varchar ;
           myppname varchar ;
         BEGIN
           update product_category set parent_id=1 where parent_id is null and id > 1 ;
           open cate_cur for select * from product_category where parent_path is null order by id ;
           loop
             fetch cate_cur into cate_rec ;
             exit when not found ;
             select parent_path,complete_name into myppath,mypcompname from product_category where id = cate_rec.parent_id ; 
             mypath = concat(myppath,cate_rec.id::TEXT,'/') ;
             mycompname = concat(mypcompname,'/',cate_rec.name) ;
             update product_category set parent_path=mypath,complete_name=mycompname where id = cate_rec.id ;
           end loop ;
           close cate_cur ;
           
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists migtest() cascade""")
        self._cr.execute("""create or replace function migtest() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=PROD host=192.168.1.222 port=5432 user=odoo password=odoo');
             /* migration neweb_payment_term_rule*/
               
              alter table neweb_contract_inspection_warn_users_rel disable trigger all;
             insert into neweb_contract_inspection_warn_users_rel(neweb_contract_contract_id,hr_employee_id)
             select neweb_contract_contract_id,hr_employee_id from
             dblink('hostaddr=192.168.1.222 port=5432 dbname=PROD user=odoo password=odoo','select 
                neweb_contract_contract_id,hr_employee_id from hr_employee_neweb_contract_contract_rel')
              as fields (neweb_contract_contract_id int,hr_employee_id int) ;
             alter table neweb_contract_inspection_warn_users_rel enable trigger all ;
             
            perform dblink_disconnect('NEWEB') ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists migcalendar() cascade""")
        self._cr.execute("""create or replace function migcalendar() returns void as $BODY$
         DECLARE
            maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration calendar.event*/
             
             
             
            alter table calendar_event disable trigger all ;
            insert into calendar_event (id,name,state,display_start,start,stop,allday,start_date,start_datetime,stop_date,stop_datetime,duration,description,privacy,location,show_as,rrule,rrule_type,recurrent_id,recurrent_id_date,end_type,"interval","count",mo,tu,we,th,fr,sa,su,month_by,day,week_list,final_date,user_id,active,create_uid,create_date,write_uid,
write_date,oe_update_date)
            select id,name,state,display_start,start,stop,allday,start_date,start_datetime,stop_date,stop_datetime,duration,description,privacy,location,show_as,rrule,rrule_type,recurrent_id,recurrent_id_date,end_type,"interval","count",mo,tu,we,th,fr,sa,su,month_by,day,week_list,final_date,user_id,active,create_uid,create_date,write_uid,
write_date,oe_update_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,state,display_start,create_date,stop,allday,start_date,start_datetime,stop_date,stop_datetime,duration,description,privacy,location,show_as,rrule,rrule_type,recurrent_id,recurrent_id_date,end_type,"interval","count",mo,tu,we,th,fr,sa,su,month_by,day,week_list,final_date,user_id,active,create_uid,create_date,write_uid,
write_date,oe_update_date from calendar_event')
             as fields (id integer,name character varying,state character varying,display_start character varying,start timestamp without time zone,stop timestamp without time zone,allday boolean,start_date date,start_datetime timestamp without time zone,stop_date date,stop_datetime timestamp without time zone,duration double precision,description text,privacy character varying,location character varying,show_as character varying,rrule character varying,rrule_type character varying,recurrent_id integer,recurrent_id_date timestamp without time zone,end_type character varying,"interval" integer,"count" integer,mo boolean,tu boolean,we boolean,th boolean,fr boolean,sa boolean,su boolean,month_by character varying,day integer,week_list character varying,final_date date,user_id integer,active boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,
write_date timestamp without time zone,oe_update_date timestamp without time zone) ;
            select max(id)+1 into maxseq from calendar_event ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence calendar_event_id_seq restart with ' || maxseq  ;
            alter table calendar_event enable trigger all ; 
            
            /* migration calendar_event_res_partner_rel */
             
             alter table calendar_event_res_partner_rel disable trigger all;
              insert into calendar_event_res_partner_rel(calendar_event_id,res_partner_id)
             select calendar_event_id,res_partner_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                calendar_event_id,res_partner_id from calendar_event_res_partner_rel')
              as fields (calendar_event_id integer,res_partner_id integer) ;
             alter table calendar_event_res_partner_rel enable trigger all ; 
             
             /*  migration calendar_attendee  */
              alter table calendar_attendee disable trigger all ;
            insert into calendar_attendee (id,state,common_name,partner_id,email,availability,access_token,event_id,create_uid,create_date,write_uid,write_date,google_internal_event_id,oe_synchro_date)
            select id,state,common_name,partner_id,email,availability,access_token,event_id,create_uid,create_date,write_uid,write_date,google_internal_event_id,oe_synchro_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,state,common_name,partner_id,email,availability,access_token,event_id,create_uid,create_date,write_uid,write_date,google_internal_event_id,oe_synchro_date from calendar_attendee')
             as fields (id integer,state character varying,common_name character varying,partner_id integer,email character varying,availability character varying,access_token character varying,event_id integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,google_internal_event_id character varying,oe_synchro_date timestamp without time zone) ;
            select max(id)+1 into maxseq from calendar_attendee ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence calendar_attendee_id_seq restart with ' || maxseq  ;
            alter table calendar_attendee enable trigger all ; 
            
              /*  migration calendar_contacts  */
             alter table calendar_contacts disable trigger all ;
            insert into calendar_contacts (id,user_id,partner_id,active,create_uid,create_date,write_uid,write_date)
            select id,user_id,partner_id,active,create_uid,create_date,write_uid,write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,user_id,partner_id,active,create_uid,create_date,write_uid,write_date from calendar_contacts')
             as fields (id integer,user_id integer,partner_id integer,active boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
            select max(id)+1 into maxseq from calendar_contacts;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence calendar_contacts_id_seq restart with ' || maxseq  ;
            alter table calendar_contacts enable trigger all ; 
             

              /* migration neweb_projcustom */
            
          /*  delete from neweb_projcustom ;
            alter table neweb_projcustom disable trigger all;
            insert into neweb_projcustom (id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select)
            select id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select from neweb_projcustom')
             as fields (id integer,create_uid integer,cus_type character varying,cus_fax character varying,cus_id integer,cus_address character varying,cus_memo text,write_uid integer,create_date timestamp without time zone,
             cus_phone character varying,write_date timestamp without time zone,cus_select integer) ;
            select max(id)+1 into maxseq from neweb_projcustom ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projcustom_id_seq restart with ' || maxseq  ;
            alter table neweb_projcustom enable trigger all ; */

             /* migration neweb_projcontact */
            
          /* delete from neweb_projcontact ;
            alter table neweb_projcontact disable trigger all;
            insert into neweb_projcontact (id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone)
            select id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone from neweb_projcontact')
             as fields (id integer,create_uid integer,contact_type integer,contact_fax character varying,contact_id integer,contact_function character varying,contact_email character varying,write_date timestamp without time zone,contact_mobile character varying,
             create_date timestamp without time zone,contact_name integer,write_uid integer,contact_phone character varying) ;
            select max(id)+1 into maxseq from neweb_projcontact ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projcontact_id_seq restart with ' || maxseq  ;
            alter table neweb_projcontact enable trigger all ; */
           

                    
           perform dblink_disconnect('NEWEB') ;
           END;$BODY$
           LANGUAGE plpgsql ;
           """)

        self._cr.execute("""drop function if exists migpurinv() cascade""")
        self._cr.execute("""create or replace function migpurinv() returns void as $BODY$
         DECLARE
            maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration neweb_purinv_invoice */

             
             
              alter table neweb_purinv_invoice disable trigger all;
             insert into neweb_purinv_invoice(id,name,invoice_total,invoice_memo,is_signed,report_date,purinv_type,is_closed,create_uid,create_date,write_uid,write_date)
             select id,name,invoice_total,invoice_memo,is_signed,report_date,purinv_type,is_closed,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,invoice_total,invoice_memo,is_signed,report_date,purinv_type,is_closed,create_uid,create_date,write_uid,write_date from neweb_purinv_invoice')
              as fields (id integer,name character varying,invoice_total numeric,invoice_memo text,is_signed boolean,report_date date,purinv_type character varying,is_closed boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_purinv_invoice ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_purinv_invoice_id_seq restart with ' || maxseq  ;
             alter table neweb_purinv_invoice enable trigger all ;    
             
             alter table neweb_purinv_invoiceline disable trigger all;
             insert into neweb_purinv_invoiceline(id,invline_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,currency_id,invoice_sum,invoice_partner,taxes_id,invoice_date,invoice_no,payment_yn,sequence,invline_memo,invline_item,create_uid,create_date,write_uid,write_date,is_gen,gen_date,gen_man,is_m_gen,gen_m_date,gen_m_man,main_purno)
             select id,invline_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,currency_id,invoice_sum,invoice_partner,taxes_id,invoice_date,invoice_no,payment_yn,sequence,invline_memo,invline_item,create_uid,create_date,write_uid,write_date,is_gen,gen_date,gen_man,is_m_gen,gen_m_date,gen_m_man,main_purno from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,invline_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,currency_id,invoice_sum,invoice_partner,taxes_id,invoice_date,invoice_no,payment_yn,sequence,invline_memo,invline_item,create_uid,create_date,write_uid,write_date,is_gen,gen_date,gen_man,is_m_gen,gen_m_date,gen_m_man,main_purno from neweb_purinv_invoiceline')
              as fields (id integer,invline_id integer,inv_prodspec character varying,cus_partner character varying,purchase_no integer,
pitem_origin_no character varying,inv_paymentterm date,currency_id integer,invoice_sum numeric,invoice_partner integer,taxes_id integer,invoice_date date,invoice_no character varying,payment_yn character varying,sequence integer,invline_memo text,invline_item numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,is_gen boolean,gen_date date,gen_man integer,is_m_gen boolean,gen_m_date date,gen_m_man integer,main_purno character varying) ;
             select max(id)+1 into maxseq from neweb_purinv_invoiceline ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_purinv_invoiceline_id_seq restart with ' || maxseq  ;
             alter table neweb_purinv_invoiceline enable trigger all ; 
               
           perform dblink_disconnect('NEWEB') ;
           END;$BODY$
           LANGUAGE plpgsql ;
           """)

        self._cr.execute("""drop function if exists migsaleana() cascade""")
        self._cr.execute("""create or replace function migsaleana() returns void as $BODY$
         DECLARE
            maxseq int ;
         BEGIN
           perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo'); 
           
           /*  migration neweb_sale_analysis_expense_report   */
           
            alter table neweb_sale_analysis_expense_report disable trigger all;
              insert into neweb_sale_analysis_expense_report(id,name,emp_no,exp_sum,exp_type,travel_no,is_signed,is_closed,create_uid,create_date,write_uid,write_date)
             select id,name,emp_no,exp_sum,exp_type,travel_no,is_signed,is_closed,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,emp_no,exp_sum,exp_type,travel_no,is_signed,is_closed,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_expense_report')
              as fields (id integer,name character varying,emp_no integer,exp_sum numeric,exp_type character varying,travel_no integer,is_signed boolean,is_closed boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_expense_report ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_expense_report_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_expense_report enable trigger all ;
             
             /*  migration neweb_sale_analysis_expense_line   */
           
            alter table neweb_sale_analysis_expense_line  disable trigger all;
              insert into neweb_sale_analysis_expense_line(id,sequence,nitem,exp_id,exp_date,exp_date1,exp_item,exp_event,exp_location,exp_desc,exp_attach,exp_money,create_uid,create_date,write_uid,write_date)
             select id,sequence,nitem,exp_id,exp_date,exp_date1,exp_item,exp_event,exp_location,exp_desc,exp_attach,exp_money,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,sequence,nitem,exp_id,exp_date,exp_date1,exp_item,exp_event,exp_location,exp_desc,exp_attach,exp_money,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_expense_line')
              as fields (id integer,sequence integer,nitem integer,exp_id integer,exp_date character varying(5),exp_date1 date,exp_item integer,exp_event integer,exp_location text,exp_desc text,exp_attach integer,exp_money numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_expense_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_expense_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_expense_line enable trigger all ;
             
               /*  migration neweb_sale_analysis_expenseitem   */
           
             alter table neweb_sale_analysis_expenseitem  disable trigger all;
              insert into neweb_sale_analysis_expenseitem(id,name,sequence,create_uid,create_date,write_uid,write_date)
             select id,name,sequence,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,sequence,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_expenseitem')
              as fields (id integer,name character varying,sequence integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_expenseitem ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_expenseitem_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_expenseitem enable trigger all ; 
             
              /*  migration neweb_sale_analysis_expenseevent  */
           
            alter table neweb_sale_analysis_expenseevent disable trigger all;
              insert into neweb_sale_analysis_expenseevent(id,name,sequence,create_uid,create_date,write_uid,write_date)
             select id,name,sequence,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,sequence,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_expenseevent')
              as fields (id integer,name character varying,sequence integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_expenseevent ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_expenseevent_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_expenseevent enable trigger all ; 
             
               /*  migration neweb_sale_analysis_expensedoc  */
           
            alter table neweb_sale_analysis_expensedoc disable trigger all;
              insert into neweb_sale_analysis_expensedoc(id,name,sequence,create_uid,create_date,write_uid,write_date)
             select id,name,sequence,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,sequence,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_expensedoc')
              as fields (id integer,name character varying,sequence integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_expensedoc ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_expensedoc_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_expensedoc enable trigger all ; 
             
               /*  migration neweb_sale_analysis_cf_sumline  */
           
            alter table neweb_sale_analysis_cf_sumline disable trigger all;
              insert into neweb_sale_analysis_cf_sumline(id,exp_id,sumline_exp_item,sum_tot,create_uid,create_date,write_uid,write_date)
             select id,exp_id,sumline_exp_item,sum_tot,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,exp_id,sumline_exp_item,sum_tot,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_cf_sumline')
              as fields (id integer,exp_id integer,sumline_exp_item integer,sum_tot double precision,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_cf_sumline ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_cf_sumline_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_cf_sumline enable trigger all ;
             
                /*  migration neweb_sale_analysis_team_targetgp  */
           
            alter table neweb_sale_analysis_team_targetgp disable trigger all;
              insert into neweb_sale_analysis_team_targetgp(id,team_id,team_target_year,team_target_year_gp,team_target_q1_gp,team_target_q1_magp,team_target_q1_sigp,team_target_q2_gp,team_target_q2_magp,team_target_q2_sigp,team_target_q3_gp,team_target_q3_magp,team_target_q3_sigp,team_target_q4_gp,team_target_q4_magp,team_target_q4_sigp,is_generation,create_uid,create_date,write_uid,write_date)
             select id,team_id,team_target_year,team_target_year_gp,team_target_q1_gp,team_target_q1_magp,team_target_q1_sigp,team_target_q2_gp,team_target_q2_magp,team_target_q2_sigp,team_target_q3_gp,team_target_q3_magp,team_target_q3_sigp,team_target_q4_gp,team_target_q4_magp,team_target_q4_sigp,is_generation,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,team_id,team_target_year,team_target_year_gp,team_target_q1_gp,team_target_q1_magp,team_target_q1_sigp,team_target_q2_gp,team_target_q2_magp,team_target_q2_sigp,team_target_q3_gp,team_target_q3_magp,team_target_q3_sigp,team_target_q4_gp,team_target_q4_magp,team_target_q4_sigp,is_generation,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_team_targetgp')
              as fields (id integer,team_id integer,team_target_year character varying(4),team_target_year_gp double precision,team_target_q1_gp double precision,team_target_q1_magp double precision,team_target_q1_sigp double precision,team_target_q2_gp double precision,team_target_q2_magp double precision,team_target_q2_sigp double precision,team_target_q3_gp double precision,team_target_q3_magp double precision,team_target_q3_sigp double precision,team_target_q4_gp double precision,team_target_q4_magp double precision,team_target_q4_sigp double precision,is_generation boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_team_targetgp ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_team_targetgp_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_team_targetgp enable trigger all ; 
             
              /*  migration neweb_sale_analysis_teammember_targetgp  */
           
            alter table neweb_sale_analysis_teammember_targetgp disable trigger all;
              insert into neweb_sale_analysis_teammember_targetgp(id,team_line_id,sales_id,salesempid,teammember_total_year_gp,teammember_total_q1_gp,teammember_total_q1_magp,teammember_total_q1_sigp,teammember_total_q2_gp,teammember_total_q2_magp,teammember_total_q2_sigp,teammember_total_q3_gp,teammember_total_q3_magp,teammember_total_q3_sigp,teammember_total_q4_gp,teammember_total_q4_magp,teammember_total_q4_sigp,create_uid,create_date,write_uid,write_date)
             select id,team_line_id,sales_id,salesempid,teammember_total_year_gp,teammember_total_q1_gp,teammember_total_q1_magp,teammember_total_q1_sigp,teammember_total_q2_gp,teammember_total_q2_magp,teammember_total_q2_sigp,teammember_total_q3_gp,teammember_total_q3_magp,teammember_total_q3_sigp,teammember_total_q4_gp,teammember_total_q4_magp,teammember_total_q4_sigp,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,team_line_id,sales_id,salesempid,teammember_total_year_gp,teammember_total_q1_gp,teammember_total_q1_magp,teammember_total_q1_sigp,teammember_total_q2_gp,teammember_total_q2_magp,teammember_total_q2_sigp,teammember_total_q3_gp,teammember_total_q3_magp,teammember_total_q3_sigp,teammember_total_q4_gp,teammember_total_q4_magp,teammember_total_q4_sigp,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_teammember_targetgp')
              as fields (id integer,team_line_id integer,sales_id integer,salesempid integer,teammember_total_year_gp numeric,teammember_total_q1_gp numeric,teammember_total_q1_magp numeric,teammember_total_q1_sigp numeric,teammember_total_q2_gp numeric,teammember_total_q2_magp numeric,teammember_total_q2_sigp numeric,teammember_total_q3_gp numeric,teammember_total_q3_magp numeric,teammember_total_q3_sigp numeric,teammember_total_q4_gp numeric,teammember_total_q4_magp numeric,teammember_total_q4_sigp numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_teammember_targetgp ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_teammember_targetgp_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_teammember_targetgp enable trigger all ; 
             
              /*  migration neweb_sale_analysis_teammember_utargetgp  */
           
            alter table neweb_sale_analysis_teammember_utargetgp disable trigger all;
              insert into neweb_sale_analysis_teammember_utargetgp(id,team_line_id,sales_id,salesempid,teammember_target_year_gp,teammember_target_q1_gp,teammember_target_q1_magp,teammember_target_q1_sigp,teammember_target_q2_gp,teammember_target_q2_magp,teammember_target_q2_sigp,teammember_target_q3_gp,teammember_target_q3_magp,teammember_target_q3_sigp,teammember_target_q4_gp,teammember_target_q4_magp,teammember_target_q4_sigp,create_uid,create_date,write_uid,write_date)
             select id,team_line_id,sales_id,salesempid,teammember_target_year_gp,teammember_target_q1_gp,teammember_target_q1_magp,teammember_target_q1_sigp,teammember_target_q2_gp,teammember_target_q2_magp,teammember_target_q2_sigp,teammember_target_q3_gp,teammember_target_q3_magp,teammember_target_q3_sigp,teammember_target_q4_gp,teammember_target_q4_magp,teammember_target_q4_sigp,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,team_line_id,sales_id,salesempid,teammember_target_year_gp,teammember_target_q1_gp,teammember_target_q1_magp,teammember_target_q1_sigp,teammember_target_q2_gp,teammember_target_q2_magp,teammember_target_q2_sigp,teammember_target_q3_gp,teammember_target_q3_magp,teammember_target_q3_sigp,teammember_target_q4_gp,teammember_target_q4_magp,teammember_target_q4_sigp,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_teammember_utargetgp')
              as fields (id integer,team_line_id integer,sales_id integer,salesempid integer,teammember_target_year_gp numeric,teammember_target_q1_gp numeric,teammember_target_q1_magp numeric,teammember_target_q1_sigp numeric,teammember_target_q2_gp numeric,teammember_target_q2_magp numeric,teammember_target_q2_sigp numeric,teammember_target_q3_gp numeric,teammember_target_q3_magp numeric,teammember_target_q3_sigp numeric,teammember_target_q4_gp numeric,teammember_target_q4_magp numeric,teammember_target_q4_sigp numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_teammember_utargetgp ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_teammember_utargetgp_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_teammember_utargetgp enable trigger all ; 
             
               /*  migration neweb_sale_analysis_sale_revenueq  */
           
            alter table neweb_sale_analysis_sale_revenueq disable trigger all;
              insert into neweb_sale_analysis_sale_revenueq(id,saleq_line_id,sales_id,salesempid,sale_quarter,
si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date)
             select id,saleq_line_id,sales_id,salesempid,sale_quarter,
si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,saleq_line_id,sales_id,salesempid,sale_quarter,
si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_sale_revenueq')
              as fields (id integer,saleq_line_id integer,sales_id integer,salesempid integer,sale_quarter character varying,
si_revenue numeric,si_profit numeric,si_profitrate numeric,service_revenue numeric,service_profit numeric,service_profitrate numeric,oldma_revenue numeric,oldma_cost numeric,oldma_profit numeric,newma_revenue numeric,newma_revenue1 numeric,newma_cost numeric,newma_profit numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_sale_revenueq ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_sale_revenueq_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_sale_revenueq enable trigger all ; 
             
                /*  migration neweb_sale_analysis_sale_revenuem  */
           
            alter table neweb_sale_analysis_sale_revenuem disable trigger all;
              insert into neweb_sale_analysis_sale_revenuem(id,salem_line_id,sales_id,salesempid,sale_month,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date)
             select id,salem_line_id,sales_id,salesempid,sale_month,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,salem_line_id,sales_id,salesempid,sale_month,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_sale_revenuem')
              as fields (id integer,salem_line_id integer,sales_id integer,salesempid integer,sale_month character varying,si_revenue numeric,si_profit numeric,si_profitrate numeric,service_revenue numeric,service_profit numeric,service_profitrate numeric,oldma_revenue numeric,oldma_cost numeric,oldma_profit numeric,newma_revenue numeric,newma_revenue1 numeric,newma_cost numeric,newma_profit numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_sale_revenuem ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_sale_revenuem_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_sale_revenuem enable trigger all ; 
             
                /*  migration neweb_sale_analysis_sale_revenuel  */
           
            alter table neweb_sale_analysis_sale_revenuel disable trigger all;
              insert into neweb_sale_analysis_sale_revenuel(id,salel_line_id,sales_id,salesempid,monthday,cus_name,prod_name,invoice_date,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,project_no,sale_memo,create_uid,create_date,write_uid,write_date)
             select id,salel_line_id,sales_id,salesempid,monthday,cus_name,prod_name,invoice_date,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,project_no,sale_memo,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,salel_line_id,sales_id,salesempid,monthday,cus_name,prod_name,invoice_date,si_revenue,si_profit,si_profitrate,service_revenue,service_profit,service_profitrate,oldma_revenue,oldma_cost,oldma_profit,newma_revenue,newma_revenue1,newma_cost,newma_profit,project_no,sale_memo,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_sale_revenuel')
              as fields (id integer,salel_line_id integer,sales_id integer,salesempid integer,monthday character varying(4),cus_name character varying,prod_name character varying,invoice_date date,si_revenue numeric,si_profit numeric,si_profitrate numeric,service_revenue numeric,service_profit numeric,service_profitrate numeric,oldma_revenue numeric,oldma_cost numeric,oldma_profit numeric,newma_revenue numeric,newma_revenue1 numeric,newma_cost numeric,newma_profit numeric,project_no character varying(15),sale_memo text,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_sale_revenuel ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_sale_revenuel_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_sale_revenuel enable trigger all ; 
             
              /*  migration neweb_sale_analysis_group_member  */
           
            alter table neweb_sale_analysis_group_member disable trigger all;
              insert into neweb_sale_analysis_group_member(id,op_id,leader_man,create_uid,create_date,write_uid,write_date)
             select id,op_id,leader_man,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,op_id,leader_man,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_group_member')
              as fields (id integer,op_id integer,leader_man integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_group_member ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_group_member_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_group_member enable trigger all ; 
             
             
                /*  migration group_member_hr_employee_rel  */
           
            alter table group_member_hr_employee_rel disable trigger all;
              insert into group_member_hr_employee_rel(gmember_id,emp_id)
             select gmember_id,emp_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                gmember_id,emp_id from group_member_hr_employee_rel')
              as fields (gmember_id integer,emp_id integer) ;
             alter table group_member_hr_employee_rel enable trigger all ; 
             
                /*  migration neweb_sale_analysis_op_program  */
           
            alter table neweb_sale_analysis_op_program disable trigger all;
              insert into neweb_sale_analysis_op_program(id,name,op_name,create_uid,create_date,write_uid,write_date)
             select id,name,op_name,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,op_name,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_op_program')
              as fields (id integer,name character varying,op_name character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_op_program ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_op_program_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_op_program enable trigger all ; 
             
                /*  migration neweb_sale_analysis_official_doc  */
           
            alter table neweb_sale_analysis_official_doc disable trigger all;
              insert into neweb_sale_analysis_official_doc(id,name,send_owner,send_name,send_address,send_phone,send_phoneext,send_fax,send_email,receiver_owner,receiver_address,receiver_zip,doc_date,doc_date_y,doc_date_m,doc_date_d,doc_urgent,doc_security,doc_attach,doc_subject,doc_memo,doc_set1,doc_set2,is_signed,is_closed,create_uid,create_date,write_uid,write_date)
             select id,name,send_owner,send_name,send_address,send_phone,send_phoneext,send_fax,send_email,receiver_owner,receiver_address,receiver_zip,doc_date,doc_date_y,doc_date_m,doc_date_d,doc_urgent,doc_security,doc_attach,doc_subject,doc_memo,doc_set1,doc_set2,is_signed,is_closed,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,send_owner,send_name,send_address,send_phone,send_phoneext,send_fax,send_email,receiver_owner,receiver_address,receiver_zip,doc_date,doc_date_y,doc_date_m,doc_date_d,doc_urgent,doc_security,doc_attach,doc_subject,doc_memo,doc_set1,doc_set2,is_signed,is_closed,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_official_doc')
              as fields (id integer,name character varying,send_owner integer,send_name character varying,send_address character varying,send_phone character varying,send_phoneext character varying,send_fax character varying,send_email character varying,receiver_owner integer,receiver_address character varying,receiver_zip character varying,doc_date date,doc_date_y character varying,doc_date_m character varying,doc_date_d character varying,
doc_urgent character varying,doc_security character varying,doc_attach character varying,doc_subject text,doc_memo text,doc_set1 character varying,doc_set2 character varying,is_signed boolean,is_closed boolean,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_official_doc ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_official_doc_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_official_doc enable trigger all ;
             
               /*  migration neweb_sale_analysis_saleanalysis_excel_download  */
           
            alter table neweb_sale_analysis_saleanalysis_excel_download disable trigger all;
              insert into neweb_sale_analysis_saleanalysis_excel_download(id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file)
             select id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file from neweb_sale_analysis_saleanalysis_excel_download')
              as fields (id integer,xls_file_name character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_saleanalysis_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_saleanalysis_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_saleanalysis_excel_download enable trigger all ;
             
               /*  migration neweb_sale_analysis_travel_report  */
           
            alter table neweb_sale_analysis_travel_report disable trigger all;
              insert into neweb_sale_analysis_travel_report(id,name,user_id,emp_id,ext,department_id,travel_start_date,travel_end_date,travel_man,travel_addr,
travel_event,travel_doc,travel_day,is_signed,is_closed,create_uid,create_date,write_uid,write_date)
             select id,name,user_id,emp_id,ext,department_id,travel_start_date,travel_end_date,travel_man,travel_addr,
travel_event,travel_doc,travel_day,is_signed,is_closed,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,user_id,emp_id,ext,department_id,travel_start_date,travel_end_date,travel_man,travel_addr,
travel_event,travel_doc,travel_day,is_signed,is_closed,create_uid,create_date,write_uid,write_date from neweb_sale_analysis_travel_report')
              as fields (id integer,name character varying(15),user_id integer,emp_id integer,ext character varying(10),
department_id integer,travel_start_date date,travel_end_date date,travel_man text,travel_addr text,
travel_event text,travel_doc text,travel_day integer,is_signed boolean,is_closed boolean,create_uid integer,
create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_sale_analysis_travel_report ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_sale_analysis_travel_report_id_seq restart with ' || maxseq  ; 
             alter table neweb_sale_analysis_travel_report enable trigger all ;

           perform dblink_disconnect('NEWEB') ;
           END;$BODY$
           LANGUAGE plpgsql ;
           """)


        self._cr.execute("""drop function if exists migchi() cascade""")
        self._cr.execute("""create or replace function migchi() returns void as $BODY$
         DECLARE
            maxseq int ;
         BEGIN
           perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
            
           
           
           alter table neweb_chi_invoicing_excel_download disable trigger all;
              insert into neweb_chi_invoicing_excel_download(id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,invoicing4_owner,invoicing5_date,
                invoicing5_owner,invoicing6_date,invoicing6_owner,is_completed,create_uid,create_date,write_uid,
                write_date,xls_file1,xls_file2,xls_file3,xls_file4,xls_file5,xls_file6)
             select id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,invoicing4_owner,invoicing5_date,
                invoicing5_owner,invoicing6_date,invoicing6_owner,is_completed,create_uid,create_date,write_uid,
                write_date,xls_file1,xls_file2,xls_file3,xls_file4,xls_file5,xls_file6 from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,invoicing4_owner,invoicing5_date,
                invoicing5_owner,invoicing6_date,invoicing6_owner,is_completed,create_uid,create_date,write_uid,
                write_date,xls_file1,xls_file2,xls_file3,xls_file4,xls_file5,xls_file6 from neweb_chi_invoicing_excel_download')
              as fields (id integer,project_no integer,xls_file_name1 character varying,xls_file_name2 character varying,
                xls_file_name3 character varying,xls_file_name4 character varying,xls_file_name5 character varying,xls_file_name6 character varying,run_desc character varying,invoicing1_date date,
                invoicing1_owner integer,invoicing2_date date,invoicing2_owner integer,invoicing3_date date,
                invoicing3_owner integer,invoicing4_date date,invoicing4_owner integer,invoicing5_date date,
                invoicing5_owner integer,invoicing6_date date,invoicing6_owner integer,is_completed character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,xls_file1 bytea,xls_file2 bytea,xls_file3 bytea,
                xls_file4 bytea,xls_file5 bytea,xls_file6 bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_excel_download enable trigger all ;  
             
             alter table neweb_chi_invoicing_purinv_excel_download disable trigger all;
              insert into neweb_chi_invoicing_purinv_excel_download(id,purchase_no,chi_purchase_name,xls_file_name,run_desc,invoicing_date,invoicing_owner,
                create_uid,create_date,write_uid,write_date,xls_file)
             select id,purchase_no,chi_purchase_name,xls_file_name,run_desc,invoicing_date,invoicing_owner,
                create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,purchase_no,chi_purchase_name,xls_file_name,run_desc,invoicing_date,invoicing_owner,
                create_uid,create_date,write_uid,write_date,xls_file from neweb_chi_invoicing_purinv_excel_download')
              as fields (id integer,purchase_no integer,chi_purchase_name character varying,xls_file_name character varying,run_desc character varying,invoicing_date date,invoicing_owner integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_purinv_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_purinv_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_purinv_excel_download enable trigger all ;
             
              alter table neweb_chi_invoicing_invoiceopen_excel_download disable trigger all;
              insert into neweb_chi_invoicing_invoiceopen_excel_download(id,project_no,chi_sales_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file)
             select id,project_no,chi_sales_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,chi_sales_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file from neweb_chi_invoicing_invoiceopen_excel_download')
              as fields (id integer,project_no integer,chi_sales_no character varying,xls_file_name character varying,
                run_desc character varying,invoicing_date date,invoicing_owner integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_invoiceopen_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_invoiceopen_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_invoiceopen_excel_download enable trigger all ;
             
              alter table neweb_chi_invoicing_excelset_seq disable trigger all;
              insert into neweb_chi_invoicing_excelset_seq(id,set_date,sales_num,purchase_num,project_num,product_num,create_uid,create_date,write_uid,write_date)
             select id,set_date,sales_num,purchase_num,project_num,product_num,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,set_date,sales_num,purchase_num,project_num,product_num,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_excelset_seq')
              as fields (id integer,set_date date,sales_num integer,purchase_num integer,project_num integer,product_num integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_excelset_seq ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_excelset_seq_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_excelset_seq enable trigger all ;
             
              alter table neweb_chi_invoicing_package_excel_download disable trigger all;
              insert into neweb_chi_invoicing_package_excel_download(id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,
                xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,
                invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,
                invoicing4_owner,invoicing5_date,invoicing5_owner,invoicing6_date,
                invoicing6_owner,create_uid,create_date,write_uid,write_date,xls_file1,xls_file2,
                xls_file3,xls_file4,xls_file5,xls_file6)
             select id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,
                xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,
                invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,
                invoicing4_owner,invoicing5_date,invoicing5_owner,invoicing6_date,
                invoicing6_owner,create_uid,create_date,write_uid,write_date,xls_file1,xls_file2,
                xls_file3,xls_file4,xls_file5,xls_file6 from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,xls_file_name1,xls_file_name2,xls_file_name3,xls_file_name4,
                xls_file_name5,xls_file_name6,run_desc,invoicing1_date,invoicing1_owner,invoicing2_date,
                invoicing2_owner,invoicing3_date,invoicing3_owner,invoicing4_date,
                invoicing4_owner,invoicing5_date,invoicing5_owner,invoicing6_date,
                invoicing6_owner,create_uid,create_date,write_uid,write_date,xls_file1,xls_file2,
                xls_file3,xls_file4,xls_file5,xls_file6 from neweb_chi_invoicing_package_excel_download')
              as fields (id integer,project_no character varying,xls_file_name1 character varying,xls_file_name2 character varying,xls_file_name3 character varying,xls_file_name4 character varying,
                xls_file_name5 character varying,xls_file_name6 character varying,
                run_desc character varying,invoicing1_date date,invoicing1_owner integer,invoicing2_date date,
                invoicing2_owner integer,invoicing3_date date,invoicing3_owner integer,invoicing4_date date,
                invoicing4_owner integer,invoicing5_date date,invoicing5_owner integer,invoicing6_date date,
                invoicing6_owner integer,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone,xls_file1 bytea,xls_file2 bytea,
                xls_file3 bytea,xls_file4 bytea,xls_file5 bytea,xls_file6 bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_excel_download enable trigger all ;
             
              alter table neweb_chi_invoicing_package_purinv_excel_download disable trigger all;
              insert into neweb_chi_invoicing_package_purinv_excel_download(id,purchase_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,create_date,write_uid,write_date,xls_file)
             select id,purchase_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,purchase_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,create_date,write_uid,write_date,xls_file from neweb_chi_invoicing_package_purinv_excel_download')
              as fields (id integer,purchase_no character varying,xls_file_name character varying,run_desc character varying,invoicing_date date,invoicing_owner integer,create_uid integer,
              create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_purinv_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_purinv_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_purinv_excel_download enable trigger all ;
             
              alter table neweb_chi_invoicing_package_saleinv_excel_download disable trigger all;
              insert into neweb_chi_invoicing_package_saleinv_excel_download(id,project_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file)
             select id,project_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,xls_file_name,run_desc,invoicing_date,invoicing_owner,create_uid,
                create_date,write_uid,write_date,xls_file from neweb_chi_invoicing_package_saleinv_excel_download')
              as fields (id integer,project_no character varying,xls_file_name character varying,
                run_desc character varying,invoicing_date date,invoicing_owner integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_saleinv_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_saleinv_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_saleinv_excel_download enable trigger all ;
             
               alter table neweb_chi_invoicing_package_project disable trigger all;
              insert into neweb_chi_invoicing_package_project(id,project_no,project_desc,project_memo,create_uid,create_date,write_uid,write_date)
             select id,project_no,project_desc,project_memo,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,project_desc,project_memo,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_package_project')
              as fields (id integer,project_no character varying,project_desc character varying,project_memo text,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_project ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_project_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_project enable trigger all ;
             
                alter table neweb_chi_invoicing_package_product disable trigger all;
              insert into neweb_chi_invoicing_package_product(id,prod_set,prod_no,prod_spec,prod_currency,prod_memo,proj_no,create_uid,create_date,write_uid,write_date)
             select id,prod_set,prod_no,prod_spec,prod_currency,prod_memo,proj_no,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,prod_set,prod_no,prod_spec,prod_currency,prod_memo,proj_no,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_package_product')
              as fields (id integer,prod_set character varying,prod_no character varying,
                prod_spec character varying,prod_currency character varying,
                prod_memo character varying,proj_no character varying,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_product ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_product_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_product enable trigger all ;
             
                 alter table neweb_chi_invoicing_package_purchase disable trigger all;
              insert into neweb_chi_invoicing_package_purchase(id,purchase_no,purchase_no1,purchase_indate,purchase_suppvat,purchase_currency,purchase_wh,
                purchase_projno,purchase_payment,purchase_prod,purchase_num,purchase_price,proj_no,
                create_uid,create_date,write_uid,write_date)
             select id,purchase_no,purchase_no1,purchase_indate,purchase_suppvat,purchase_currency,purchase_wh,
                purchase_projno,purchase_payment,purchase_prod,purchase_num,purchase_price,proj_no,
                create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,purchase_no,purchase_no1,purchase_indate,purchase_suppvat,purchase_currency,purchase_wh,
                purchase_projno,purchase_payment,purchase_prod,purchase_num,purchase_price,proj_no,
                create_uid,create_date,write_uid,write_date
                 from neweb_chi_invoicing_package_purchase')
              as fields (id integer,purchase_no character varying,purchase_no1 character varying,
                purchase_indate date,purchase_suppvat character varying,
                purchase_currency character varying,purchase_wh character varying,
                purchase_projno character varying,purchase_payment date,purchase_prod character varying,
                purchase_num numeric,purchase_price numeric,proj_no character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_purchase ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_purchase_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_purchase enable trigger all ;
             
                alter table neweb_chi_invoicing_package_sales disable trigger all;
              insert into neweb_chi_invoicing_package_sales(id,sales_no,sales_outdate,sales_cusvat,sales_currency,
              sales_man,sales_wh,sales_proj_no,sales_cus_order,sales_paymentdate,sales_prod,sales_num,sales_price,
              proj_no,sales_memo,sale_spec,saleitem_seq,create_uid,create_date,write_uid,write_date)
             select id,sales_no,sales_outdate,sales_cusvat,sales_currency,sales_man,sales_wh,sales_proj_no,sales_cus_order,
             sales_paymentdate,sales_prod,sales_num,sales_price,proj_no,sales_memo,sale_spec,saleitem_seq,create_uid,
             create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,sales_no,sales_outdate,sales_cusvat,sales_currency,sales_man,sales_wh,sales_proj_no,sales_cus_order,
                sales_paymentdate,sales_prod,sales_num,sales_price,proj_no,sales_memo,sale_spec,saleitem_seq,create_uid,
                create_date,write_uid,write_date from neweb_chi_invoicing_package_sales')
              as fields (id integer,sales_no character varying,sales_outdate date,sales_cusvat character varying,
                sales_currency character varying,sales_man character varying,sales_wh character varying,sales_proj_no character varying,
                sales_cus_order character varying,sales_paymentdate date,sales_prod character varying,sales_num numeric,
                sales_price numeric,proj_no character varying,sales_memo text,sale_spec character varying,saleitem_seq integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_package_sales ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_package_sales_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_package_sales enable trigger all ;
             
             alter table neweb_chi_invoicing_export_main_proj_log disable trigger all;
              insert into neweb_chi_invoicing_export_main_proj_log(id,project_no,export_user,export_date,
              is_export_project_master,is_export_project_product,is_export_project_sale,is_export_project_purchase,
              create_uid,create_date,write_uid,write_date)
             select id,project_no,export_user,export_date,is_export_project_master,is_export_project_product,
             is_export_project_sale,is_export_project_purchase,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,export_user,export_date,is_export_project_master,is_export_project_product,is_export_project_sale,
                is_export_project_purchase,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_export_main_proj_log')
              as fields (id integer,project_no integer,export_user integer,export_date date,is_export_project_master boolean,
              is_export_project_product boolean,is_export_project_sale boolean,is_export_project_purchase boolean,create_uid integer,
              create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_export_main_proj_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_export_main_proj_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_export_main_proj_log enable trigger all ;
             
             alter table neweb_chi_invoicing_export_purchase_log disable trigger all;
              insert into neweb_chi_invoicing_export_purchase_log(id,chi_purchase_name,chi_income_date,chi_purchase_vat,chi_purchase_sup,chi_currency_type,chi_wh,
                chi_project_no,proj_no,chi_paymentdate,chi_product,chi_purchase_num,chi_purchase_price,chi_origin_id,chi_purchase_no,purchase_seq,pitem_id,create_uid,create_date,write_uid,write_date)
             select id,chi_purchase_name,chi_income_date,chi_purchase_vat,chi_purchase_sup,chi_currency_type,chi_wh,
                chi_project_no,proj_no,chi_paymentdate,chi_product,chi_purchase_num,chi_purchase_price,chi_origin_id,chi_purchase_no,purchase_seq,pitem_id,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,chi_purchase_name,chi_income_date,chi_purchase_vat,chi_purchase_sup,chi_currency_type,chi_wh,
                chi_project_no,proj_no,chi_paymentdate,chi_product,chi_purchase_num,chi_purchase_price,chi_origin_id,chi_purchase_no,purchase_seq,pitem_id,
                create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_export_purchase_log')
              as fields (id integer,chi_purchase_name character varying,chi_income_date date,chi_purchase_vat character varying,chi_purchase_sup integer,chi_currency_type character varying,chi_wh character varying,
                chi_project_no character varying,proj_no integer,chi_paymentdate date,chi_product character varying,chi_purchase_num numeric,chi_purchase_price numeric,chi_origin_id integer,chi_purchase_no integer,purchase_seq integer,pitem_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_export_purchase_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_export_purchase_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_export_purchase_log enable trigger all ;
             
             alter table neweb_chi_invoicing_export_sales_log disable trigger all;
              insert into neweb_chi_invoicing_export_sales_log(id,chi_sales_no,chi_outcome_date,chi_sales_vat,chi_sales_cus,chi_currency_type,proj_sale ,proj_sale_name,chi_wh,proj_no,chi_project_no,chi_cus_order,chi_paymentdate,
                chi_product,chi_sales_num,chi_sales_price,chi_origin_id,chi_sale_memo,chi_sale_spec,saleitem_seq,create_uid,create_date,write_uid,write_date)
             select id,chi_sales_no,chi_outcome_date,chi_sales_vat,chi_sales_cus,chi_currency_type,proj_sale ,proj_sale_name,chi_wh,proj_no,chi_project_no,chi_cus_order,chi_paymentdate,
                chi_product,chi_sales_num,chi_sales_price,chi_origin_id,chi_sale_memo,chi_sale_spec,saleitem_seq,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,chi_sales_no,chi_outcome_date,chi_sales_vat,chi_sales_cus,chi_currency_type,proj_sale ,proj_sale_name,chi_wh,proj_no,chi_project_no,chi_cus_order,chi_paymentdate,
                chi_product,chi_sales_num,chi_sales_price,chi_origin_id,chi_sale_memo,chi_sale_spec,saleitem_seq,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_export_sales_log')
              as fields (id integer,chi_sales_no character varying,chi_outcome_date date,chi_sales_vat character varying,chi_sales_cus integer,chi_currency_type character varying,proj_sale integer,proj_sale_name character varying,chi_wh character varying,proj_no integer,chi_project_no character varying,chi_cus_order character varying,chi_paymentdate date,
                chi_product character varying,chi_sales_num numeric,chi_sales_price numeric,chi_origin_id integer,chi_sale_memo text,chi_sale_spec character varying,saleitem_seq integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_export_sales_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_export_sales_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_export_sales_log enable trigger all ;
             
              alter table neweb_chi_invoicing_productset_seq disable trigger all;
              insert into neweb_chi_invoicing_productset_seq(id,chi_year,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date)
             select id,chi_year,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,chi_year,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date from neweb_chi_invoicing_productset_seq')
              as fields (id integer,chi_year character varying,chi_sname character varying,
                chi_seq integer,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_productset_seq ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_productset_seq_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_productset_seq enable trigger all ;
             
               alter table neweb_chi_invoicing_export_proj_log disable trigger all;
              insert into neweb_chi_invoicing_export_proj_log(id,project_no,export_user,export_date,is_export_project_master,
              is_export_project_product,is_export_project_sale,is_export_project_purchase,create_uid,create_date,write_uid,write_date)
             select id,project_no,export_user,export_date,is_export_project_master,is_export_project_product,is_export_project_sale,
             is_export_project_purchase,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,export_user,export_date,is_export_project_master,is_export_project_product,
                is_export_project_sale,is_export_project_purchase,create_uid,create_date,write_uid,write_date 
                from neweb_chi_invoicing_export_proj_log')
              as fields (id integer,project_no integer,export_user integer,export_date date,is_export_project_master boolean,
              is_export_project_product boolean,is_export_project_sale boolean,is_export_project_purchase boolean,create_uid integer,
              create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_export_proj_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_export_proj_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_export_proj_log enable trigger all ;
             
               alter table neweb_chi_invoicing_incomeoutcome_seq disable trigger all;
              insert into neweb_chi_invoicing_incomeoutcome_seq(id,chi_year,chi_month,chi_day,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date)
             select id,chi_year,chi_month,chi_day,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,chi_year,chi_month,chi_day,chi_sname,chi_seq,create_uid,create_date,write_uid,write_date 
                from neweb_chi_invoicing_incomeoutcome_seq')
              as fields (id integer,chi_year character varying,chi_month character varying,
                chi_day character varying,chi_sname character varying,chi_seq integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_chi_invoicing_incomeoutcome_seq ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_chi_invoicing_incomeoutcome_seq_id_seq restart with ' || maxseq  ; 
             alter table neweb_chi_invoicing_incomeoutcome_seq enable trigger all ;
           
           
           perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists migtimesheet() cascade""")
        self._cr.execute("""create or replace function migtimesheet() returns void as $BODY$
         DECLARE
            maxseq int ;
         BEGIN
           perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
           
            
           
            alter table neweb_emp_timesheet_timesheet_worktype disable trigger all;
              insert into neweb_emp_timesheet_timesheet_worktype(id,sequence,nitem,worktype_code,worktype_link,worktype_categ,worktype_desc,worktype_cat,
                create_uid,create_date,write_uid,write_date)
             select id,sequence,nitem,worktype_code,worktype_link,worktype_categ,worktype_desc,worktype_cat,
                create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,sequence,nitem,worktype_code,worktype_link,worktype_categ,worktype_desc,worktype_cat,
                create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_timesheet_worktype')
              as fields (id integer,sequence integer,nitem integer,worktype_code character varying,
                worktype_link character varying,worktype_categ character varying,
                worktype_desc character varying,worktype_cat character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_worktype ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_worktype_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_worktype enable trigger all ;  
             
             alter table neweb_emp_timesheet_inspection_alert_mail disable trigger all;
              insert into neweb_emp_timesheet_inspection_alert_mail(id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,inspection_alert1 ,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,create_uid,
                create_date,write_uid,write_date)
             select id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,inspection_alert1 ,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,create_uid,
                create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,inspection_alert1 ,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,create_uid,
                create_date,write_uid,write_date from neweb_emp_timesheet_inspection_alert_mail')
              as fields (id integer,emp_id integer,dept_id integer,cus_id integer,contract_no integer,inspection_datetime timestamp without time zone,inspection_complete character varying,inspection_alert1 boolean,inspection_alert2 boolean,alert_date1 date,alert_date2 date,emp_manager integer,
                inspection_name character varying,inspection_sequence integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_inspection_alert_mail ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_inspection_alert_mail_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_inspection_alert_mail enable trigger all ;
             
             alter table neweb_emp_timesheet_hrholiday disable trigger all;
              insert into neweb_emp_timesheet_hrholiday(id,hr_holiday_year,create_uid,create_date,write_uid,write_date)
             select id,hr_holiday_year,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,hr_holiday_year,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_hrholiday')
              as fields (id integer,hr_holiday_year character varying,create_uid integer,create_date timestamp without time zone,
              write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_hrholiday ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_hrholiday_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_hrholiday enable trigger all ;
             
             alter table neweb_emp_timesheet_hrholiday_line disable trigger all;
              insert into neweb_emp_timesheet_hrholiday_line(id,holiday_id,nitem,holiday_date,holiday_memo,create_uid,create_date,write_uid,write_date)
             select id,holiday_id,nitem,holiday_date,holiday_memo,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,holiday_id,nitem,holiday_date,holiday_memo,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_hrholiday_line')
              as fields (id integer,holiday_id integer,nitem integer,holiday_date date,holiday_memo text,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_hrholiday_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_hrholiday_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_hrholiday_line enable trigger all ;
             
             alter table neweb_emp_timesheet_inspection_calendar disable trigger all;
              insert into neweb_emp_timesheet_inspection_calendar(id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,
                inspection_alert1,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,inspection_start_datetime,inspection_end_datetime,inspection_memo,create_uid,create_date,
                write_uid,write_date)
             select id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,
                inspection_alert1,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,inspection_start_datetime,inspection_end_datetime,inspection_memo,create_uid,create_date,
                write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,emp_id,dept_id,cus_id,contract_no,inspection_datetime,inspection_complete,
                inspection_alert1,inspection_alert2,alert_date1,alert_date2,emp_manager,inspection_name,inspection_sequence,inspection_start_datetime,inspection_end_datetime,inspection_memo,create_uid,create_date,
                write_uid,write_date from neweb_emp_timesheet_inspection_calendar')
              as fields (id integer,emp_id integer,dept_id integer,cus_id integer,contract_no integer,
                inspection_datetime timestamp without time zone,inspection_complete character varying,
                inspection_alert1 boolean,inspection_alert2 boolean,alert_date1 date,alert_date2 date,
                emp_manager integer,inspection_name character varying,inspection_sequence integer,
                inspection_start_datetime timestamp without time zone,inspection_end_datetime timestamp without time zone,
                inspection_memo text,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_inspection_calendar ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_inspection_calendar_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_inspection_calendar enable trigger all ;
             
             alter table neweb_emp_timesheet_repair_calendar disable trigger all;
              insert into neweb_emp_timesheet_repair_calendar(id,emp_id,dept_id,cus_id,contract_no,repair_no,
              repair_datetime,repair_complete,emp_manager,repair_name,repair_sequence,create_uid,create_date,write_uid,write_date)
             select id,emp_id,dept_id,cus_id,contract_no,repair_no,repair_datetime,repair_complete,emp_manager,repair_name,repair_sequence,
             create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,emp_id,dept_id,cus_id,contract_no,repair_no,repair_datetime,repair_complete,emp_manager,repair_name,repair_sequence,create_uid,
                create_date,write_uid,write_date from neweb_emp_timesheet_repair_calendar')
              as fields (id integer,emp_id integer,dept_id integer,cus_id integer,contract_no integer,repair_no integer,
                repair_datetime timestamp without time zone,repair_complete character varying,
                emp_manager integer,repair_name character varying,repair_sequence integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_repair_calendar ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_repair_calendar_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_repair_calendar enable trigger all ;
             
             alter table neweb_emp_timesheet_timesheet_calendar disable trigger all;
              insert into neweb_emp_timesheet_timesheet_calendar(id,emp_id,timesheet_yearmonth,is_closed,level_manager,
              running_level,emp_manager1,emp_manager2,emp_manager3,emp_manager4,emp_manager5,emp_approve1,create_uid,
              create_date,write_uid,write_date)
             select id,emp_id,timesheet_yearmonth,is_closed,level_manager,running_level,emp_manager1,emp_manager2,emp_manager3,
             emp_manager4,emp_manager5,emp_approve1,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,emp_id,timesheet_yearmonth,is_closed,level_manager,running_level,emp_manager1,emp_manager2,emp_manager3,
                emp_manager4,emp_manager5,emp_approve1,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_timesheet_calendar')
              as fields (id integer,emp_id integer,timesheet_yearmonth character varying,is_closed boolean,level_manager integer,running_level integer,
              emp_manager1 integer,emp_manager2 integer,emp_manager3 integer,emp_manager4 integer,emp_manager5 integer,emp_approve1 timestamp without time zone,
              create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_calendar ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_calendar_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_calendar enable trigger all ;
             
             alter table neweb_emp_timesheet_timesheet_calendar_line disable trigger all;
              insert into neweb_emp_timesheet_timesheet_calendar_line(id,line_id,sequence,nitem,emp_id,timesheet_start_date,timesheet_end_date,
                timesheet_duration,timesheet_worktype,timesheet_custom,timesheet_origin,timesheet_desc,duration,
                origin_id,origin_type,is_locked,is_complete,sale_id,timesheet_pivottype,create_uid,create_date,write_uid,write_date)
             select id,line_id,sequence,nitem,emp_id,timesheet_start_date,timesheet_end_date,
                timesheet_duration,timesheet_worktype,timesheet_custom,timesheet_origin,timesheet_desc,duration,
                origin_id,origin_type,is_locked,is_complete,sale_id,timesheet_pivottype,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,line_id,sequence,nitem,emp_id,timesheet_start_date,timesheet_end_date,
                timesheet_duration,timesheet_worktype,timesheet_custom,timesheet_origin,timesheet_desc,duration,
                origin_id,origin_type,is_locked,is_complete,sale_id,timesheet_pivottype,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_timesheet_calendar_line')
              as fields (id integer,line_id integer,sequence integer,nitem integer,emp_id integer,
                timesheet_start_date timestamp without time zone,timesheet_end_date timestamp without time zone,
                timesheet_duration numeric,timesheet_worktype integer,timesheet_custom integer,
                timesheet_origin character varying,timesheet_desc text,duration double precision,
                origin_id integer,origin_type character varying,is_locked boolean,is_complete character varying,
                sale_id integer,timesheet_pivottype character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_calendar_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_calendar_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_calendar_line enable trigger all ;
             
              alter table neweb_emp_timesheet_timesheet_lock disable trigger all;
              insert into neweb_emp_timesheet_timesheet_lock(id,yearmonth,lock_date,create_uid,create_date,write_uid,write_date)
             select id,yearmonth,lock_date,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,yearmonth,lock_date,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_timesheet_lock')
              as fields (id integer,yearmonth character varying,lock_date date,create_uid integer,create_date timestamp without time zone,
              write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_lock ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_lock_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_lock enable trigger all ;
             
              alter table neweb_emp_timesheet_timesheet_adjustowner disable trigger all;
              insert into neweb_emp_timesheet_timesheet_adjustowner(id,timesheet_adjustowner,create_uid,create_date,write_uid,write_date)
             select id,timesheet_adjustowner,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,timesheet_adjustowner,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_timesheet_adjustowner')
              as fields (id integer,timesheet_adjustowner integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_adjustowner ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_adjustowner_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_adjustowner enable trigger all ;
             
              alter table neweb_emp_timesheet_timesheet_download disable trigger all;
              insert into neweb_emp_timesheet_timesheet_download(id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file)
             select id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file from neweb_emp_timesheet_timesheet_download')
              as fields (id integer,xls_file_name character varying,run_desc character varying,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_timesheet_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_timesheet_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_timesheet_download enable trigger all ;
             
              alter table neweb_emp_timesheet_todo_calendar disable trigger all;
              insert into neweb_emp_timesheet_todo_calendar(id,emp_id,todo_datetime,dept_id,cus_id,assign_cus,todo_origin,todo_completed,
              todo_sequence,repair_no,assign_no,ins_start_datetime,ins_end_datetime,ins_memo,contract_no,ae_response_datetime,ae_on_site_datetime,
              ae_complete_datetime,create_uid,create_date,write_uid,write_date)
             select id,emp_id,todo_datetime,dept_id,cus_id,assign_cus,todo_origin,todo_completed,todo_sequence,repair_no,assign_no,
             ins_start_datetime,ins_end_datetime,ins_memo,contract_no,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,
             create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,emp_id,todo_datetime,dept_id,cus_id,assign_cus,todo_origin,todo_completed,todo_sequence,repair_no,assign_no,ins_start_datetime,
                ins_end_datetime,ins_memo,contract_no,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,create_uid,create_date,write_uid,
                write_date from neweb_emp_timesheet_todo_calendar')
              as fields (id integer,emp_id integer,todo_datetime timestamp without time zone,dept_id integer,
            cus_id integer,assign_cus character varying,todo_origin character varying,
            todo_completed character varying,todo_sequence integer,repair_no integer,
            assign_no integer,ins_start_datetime timestamp without time zone,ins_end_datetime timestamp without time zone,ins_memo text,
            contract_no integer,ae_response_datetime timestamp without time zone,ae_on_site_datetime timestamp without time zone,
            ae_complete_datetime timestamp without time zone,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_todo_calendar ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_todo_calendar_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_todo_calendar enable trigger all ;
             
              alter table neweb_emp_timesheet_tolerance_setting disable trigger all;
              insert into neweb_emp_timesheet_tolerance_setting(id,tolerance_time,create_uid,create_date,write_uid,write_date)
             select id,tolerance_time,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,tolerance_time,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_tolerance_setting')
              as fields (id integer,tolerance_time double precision,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_tolerance_setting ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_tolerance_setting_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_tolerance_setting enable trigger all ;
             
              alter table neweb_emp_timesheet_workdate_check disable trigger all;
              insert into neweb_emp_timesheet_workdate_check(id,timesheet_date,emp_id,dept_id,has_gen,timesheet_hours,create_uid,create_date,write_uid,write_date)
             select id,timesheet_date,emp_id,dept_id,has_gen,timesheet_hours,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,timesheet_date,emp_id,dept_id,has_gen,timesheet_hours,create_uid,create_date,write_uid,write_date from neweb_emp_timesheet_workdate_check')
              as fields (id integer,timesheet_date date,emp_id integer,dept_id integer,has_gen character varying,
                timesheet_hours double precision,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_emp_timesheet_workdate_check ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_emp_timesheet_workdate_check_id_seq restart with ' || maxseq  ; 
             alter table neweb_emp_timesheet_workdate_check enable trigger all ;
           
           perform dblink_disconnect('NEWEB') ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists miginvoice() cascade""")
        self._cr.execute("""create or replace function miginvoice() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
          perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
           
           /* migration neweb_invoice_invoiceopen */
            alter table neweb_invoice_invoiceopen disable trigger all;
             insert into neweb_invoice_invoiceopen(id,application_date,project_no,project_name,contract_no,
             contract_main_start,contract_main_end,invoice_title,payment_type,payment_memo,sno,project_amount_total,
             open_complete_total,open_amount_total,revenue_1,revenue_2,revenue_3,revenue_4 ,revenue_5,revenue_6,revenue_7,
             revenue_8,delivery_type,invoice_contact,invoice_phone,invoice_address,invoice_return_envelope,other_memo,name,
             have_inherit,is_completed,invoice_ver,is_signed,cus_name,main_cus_name,tax_type,projectno,is_closed,invoice_contact1,
             purchase_no,cus_order,invoice_paymentdate,create_uid,create_date,write_uid,write_date,is_gen,
                gen_date,gen_man)
             select id,application_date,project_no,project_name,contract_no,contract_main_start,contract_main_end,invoice_title,
             payment_type,payment_memo,sno,project_amount_total,open_complete_total,open_amount_total,revenue_1,revenue_2,revenue_3,
             revenue_4 ,revenue_5,revenue_6,revenue_7,revenue_8,delivery_type,invoice_contact,invoice_phone,invoice_address,
             invoice_return_envelope,other_memo,name,have_inherit,is_completed,invoice_ver,is_signed,cus_name,main_cus_name,tax_type,
             projectno,is_closed,invoice_contact1,purchase_no,cus_order,invoice_paymentdate,create_uid,create_date,write_uid,write_date,
             is_gen,gen_date,gen_man from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,application_date,project_no,project_name,contract_no,contract_main_start,contract_main_end,invoice_title,payment_type,
                payment_memo,sno,project_amount_total,open_complete_total,open_amount_total,revenue_1,revenue_2,revenue_3,revenue_4 ,revenue_5,
                revenue_6,revenue_7,revenue_8,delivery_type,invoice_contact,invoice_phone,invoice_address,invoice_return_envelope,other_memo,name,
                have_inherit,is_completed,invoice_ver,is_signed,cus_name,main_cus_name,tax_type,projectno,is_closed,invoice_contact1,purchase_no,
                cus_order,invoice_paymentdate,create_uid,create_date,write_uid,write_date,is_gen,gen_date,gen_man from neweb_invoice_invoiceopen')
              as fields (id integer,application_date date,project_no integer,project_name text,contract_no integer,contract_main_start date,
                contract_main_end date,invoice_title text,payment_type character varying,payment_memo text,sno character varying,
                project_amount_total numeric,open_complete_total numeric,open_amount_total numeric,revenue_1 numeric,revenue_2 numeric,
                revenue_3 numeric,revenue_4 numeric,revenue_5 numeric,revenue_6 numeric,revenue_7 numeric,revenue_8 numeric,
                delivery_type character varying,invoice_contact character varying,invoice_phone character varying,
                invoice_address text,invoice_return_envelope character varying,other_memo text,name character varying,
                have_inherit boolean,is_completed boolean,invoice_ver integer,is_signed boolean,cus_name integer,
                main_cus_name integer,tax_type character varying,projectno character varying,is_closed boolean,invoice_contact1 integer,
                purchase_no character varying,cus_order character varying,invoice_paymentdate date,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,is_gen boolean,
                gen_date date,gen_man integer) ;
             select max(id)+1 into maxseq from neweb_invoice_invoiceopen ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_invoiceopen_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_invoiceopen enable trigger all ;  
             
             alter table neweb_invoice_invoiceopen_line disable trigger all;
             insert into neweb_invoice_invoiceopen_line(id,invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,invoicetype,invoice_no,invoice_date,
                invoice_state,purchase_no,invoice_ver,sequence,create_uid,create_date,write_uid,write_date,
                receive_date,is_main_gen,is_main_completed,sales_no)
             select id,invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,invoicetype,invoice_no,invoice_date,
                invoice_state,purchase_no,invoice_ver,sequence,create_uid,create_date,write_uid,write_date,
                receive_date,is_main_gen,is_main_completed,sales_no from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,invoicetype,invoice_no,invoice_date,
                invoice_state,purchase_no,invoice_ver,sequence,create_uid,create_date,write_uid,write_date,
                receive_date,is_main_gen,is_main_completed,sales_no from neweb_invoice_invoiceopen_line')
              as fields (id integer,invoice_id integer,invoice_costtype integer,invoice_spec text,invoice_num integer,invoice_unit_price numeric,invoice_unit_price1 numeric,invoice_taxtype integer,invoicetype character varying,invoice_no character varying,invoice_date date,
                invoice_state character varying,purchase_no character varying,invoice_ver integer,sequence integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                receive_date date,is_main_gen boolean,is_main_completed boolean,sales_no character varying) ;
             select max(id)+1 into maxseq from neweb_invoice_invoiceopen_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_invoiceopen_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_invoiceopen_line enable trigger all ;  
             
             alter table neweb_invoice_invopen_list disable trigger all;
              insert into neweb_invoice_invopen_list(id,inv_id,inv_item,inv_date,inv_no,inv_open,inv_amount,inv_totalamount,
              inv_memo,create_uid,create_date,write_uid,write_date)
             select id,inv_id,inv_item,inv_date,inv_no,inv_open,inv_amount,inv_totalamount,inv_memo,create_uid,create_date,
             write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,inv_id,inv_item,inv_date,inv_no,inv_open,inv_amount,inv_totalamount,inv_memo,create_uid,create_date,
                write_uid,write_date from neweb_invoice_invopen_list')
              as fields (id integer,inv_id integer,inv_item integer,inv_date date,inv_no character varying,inv_open character varying,
                inv_amount numeric,inv_totalamount numeric,inv_memo text,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_invoice_invopen_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_invopen_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_invopen_list enable trigger all ;  
             
             alter table neweb_invoice_proj_inv_excel_download disable trigger all;
              insert into neweb_invoice_proj_inv_excel_download(id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file)
             select id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,xls_file_name,create_uid,create_date,write_uid,write_date,xls_file from neweb_invoice_proj_inv_excel_download')
              as fields (id integer,xls_file_name character varying,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone,xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_invoice_proj_inv_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_proj_inv_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_proj_inv_excel_download enable trigger all ;  
             
             alter table neweb_invoice_projectdata disable trigger all;
              insert into neweb_invoice_projectdata(id,project_no,prod_set,cus_name,prod_modeltype,prod_desc,prod_num,prod_cost_price,supplier,prod_sale_price,create_uid,create_date,write_uid,write_date)
             select id,project_no,prod_set,cus_name,prod_modeltype,prod_desc,prod_num,prod_cost_price,supplier,prod_sale_price,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,prod_set,cus_name,prod_modeltype,prod_desc,prod_num,prod_cost_price,supplier,prod_sale_price,create_uid,create_date,write_uid,write_date from neweb_invoice_projectdata')
              as fields (id integer,project_no integer,prod_set integer,cus_name integer,prod_modeltype text,prod_desc text,
                prod_num numeric,prod_cost_price numeric,supplier integer,prod_sale_price numeric,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_invoice_projectdata ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_projectdata_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_projectdata enable trigger all ;  
             
              alter table neweb_invoice_invoicedata disable trigger all;
              insert into neweb_invoice_invoicedata(id,project_no,invoice_date,invoice_no,invoice_untax_amount,application_date,other_memo,create_uid,create_date,write_uid,write_date)
             select id,project_no,invoice_date,invoice_no,invoice_untax_amount,application_date,other_memo,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,project_no,invoice_date,invoice_no,invoice_untax_amount,application_date,other_memo,create_uid,create_date,write_uid,write_date from neweb_invoice_invoicedata')
              as fields (id integer,project_no integer,invoice_date date,invoice_no character varying,invoice_untax_amount numeric,
                application_date date,other_memo text,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_invoice_invoicedata ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_invoicedata_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_invoicedata enable trigger all ;  
             
              alter table neweb_invoice_purinvdata disable trigger all;
              insert into neweb_invoice_purinvdata(id,pitem_origin_no,invoice_date,invoice_no,inv_paymentterm,invoice_partner,invoice_sum,payment_yn,create_uid,
                create_date,write_uid,write_date)
             select id,pitem_origin_no,invoice_date,invoice_no,inv_paymentterm,invoice_partner,invoice_sum,payment_yn,create_uid,
                create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,pitem_origin_no,invoice_date,invoice_no,inv_paymentterm,invoice_partner,invoice_sum,payment_yn,create_uid,
                create_date,write_uid,write_date from neweb_invoice_purinvdata')
              as fields (id integer,pitem_origin_no character varying,invoice_date date,invoice_no character varying,inv_paymentterm date,
                invoice_partner integer,invoice_sum double precision,payment_yn character varying,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_invoice_purinvdata ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_invoice_purinvdata_id_seq restart with ' || maxseq  ; 
             alter table neweb_invoice_purinvdata enable trigger all ;  
             
             
          perform dblink_disconnect('NEWEB') ;   
         END;$BODY$
         LANGUAGE plpgsql;""")




        self._cr.execute("""drop function if exists migsecurity() cascade""")
        self._cr.execute("""create or replace function migsecurity() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration res_company_users_rel */
             
             
              alter table res_company_users_rel disable trigger all;
             insert into res_company_users_rel(cid,user_id)
             select cid,user_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                cid,user_id from res_company_users_rel where user_id > 5')
              as fields (cid integer,user_id integer) ;
            
             alter table res_groups_users_rel enable trigger all ;    
             
             
              alter table res_groups_users_rel disable trigger all;
             insert into res_groups_users_rel(gid,uid)
             select gid,uid from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                gid,uid from res_groups_users_rel where uid > 5')
              as fields (gid integer,uid integer) ;
            
             alter table res_groups_users_rel enable trigger all ;  
             execute ckcompuser() ;
             
             perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;    
        """)


        self._cr.execute("""drop function if exists migrepair() cascade""")
        self._cr.execute("""create or replace function migrepair() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration ir_property */
             
             
            /* update res_users set chatter_position='sided',sidebar_visible=True,odoobot_state='onboarding_emoji' where chatter_position is null ; */
              alter table ir_property disable trigger all;
              delete from ir_property where id > 3361 ;
             insert into ir_property(id,name,res_id,company_id,fields_id,value_float,value_integer,value_text,value_binary,value_reference,value_datetime,type,create_uid,create_date,write_uid,write_date)
             select id,name,res_id,company_id,fields_id,value_float,value_integer,value_text,value_binary,value_reference,value_datetime,type,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,res_id,company_id,fields_id,value_float,value_integer,value_text,value_binary,value_reference,value_datetime,type,create_uid,create_date,write_uid,write_date from ir_property where id > 3361')
              as fields (id integer,name character varying,res_id character varying,company_id integer,fields_id integer,value_float double precision,value_integer integer,value_text text,value_binary bytea,value_reference character varying,value_datetime timestamp without time zone,type character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from ir_property ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence ir_property_id_seq restart with ' || maxseq  ; 
             alter table ir_property enable trigger all ;    
             
            /* delete from res_company_users_rel ; */ 
            /*  alter table res_company_users_rel disable trigger all;
            
             insert into res_company_users_rel(cid,user_id)
             select cid,user_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                cid,user_id from res_company_users_rel where user_id > 5')
              as fields (cid integer,user_id integer) ;
            
             alter table res_company_users_rel enable trigger all ;  */
            
             alter table neweb_repair_questionnaire disable trigger all;
             delete from neweb_repair_questionnaire ;
             insert into neweb_repair_questionnaire(id,name,code,disabled,create_uid,create_date,write_uid,write_date)
             select id,name,code,disabled,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,code,disabled,create_uid,create_date,write_uid,write_date from neweb_repair_questionnaire')
              as fields (id integer,name character varying,code character varying,disabled boolean,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_questionnaire ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_questionnaire_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_questionnaire enable trigger all ;  
             
              alter table neweb_repair_question disable trigger all;
              delete from neweb_repair_question ;
             insert into neweb_repair_question(id,name,disabled,questionnaire_id,create_uid,create_date,write_uid,write_date)
             select id,name,disabled,questionnaire_id,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,disabled,questionnaire_id,create_uid,create_date,write_uid,write_date from neweb_repair_question')
              as fields (id integer,name character varying,disabled boolean,questionnaire_id integer,create_uid integer,
            create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_question ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_question_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_question enable trigger all ;  
             
             ALTER TABLE neweb_repair_repair ALTER sales DROP NOT NULL;
               alter table neweb_repair_repair disable trigger all;
               delete from neweb_repair_repair ;
             insert into neweb_repair_repair(id,name,create_user,create_date,repair_type,repair_datetime,customer_id,contact_user,
             contact_user1,contact_tel,ae_id,device_location,contract_id,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,ae_is_sla_delay,
             ae_total_ma_time,problem,survey_remark,end_customer,device_contact,device_tel,memo,part_ready,state,
             care_call_date,sales,create_uid,write_uid,write_date)
             select id,name,create_user,create_date,repair_type,repair_datetime,customer_id,contact_user,contact_user1,contact_tel,
             ae_id,device_location,contract_id,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,ae_is_sla_delay,ae_total_ma_time,problem,
             survey_remark,end_customer,device_contact,device_tel,memo,part_ready,state,care_call_date,sales,
             create_uid,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,create_user,create_date,repair_type,repair_datetime,customer_id,contact_user,contact_user1,contact_tel,ae_id,
                device_location,contract_id,ae_response_datetime,ae_on_site_datetime,ae_complete_datetime,ae_is_sla_delay,ae_total_ma_time,problem,
                survey_remark,end_customer,device_contact,device_tel,memo,part_ready,state,care_call_date,sales,create_uid,write_uid,
                write_date from neweb_repair_repair')
              as fields (id integer,name character varying,create_user integer,create_date date,repair_type character varying,repair_datetime timestamp without time zone,
              customer_id integer,contact_user integer,contact_user1 character varying,contact_tel character varying,
                ae_id integer,device_location character varying,contract_id integer,ae_response_datetime timestamp without time zone,ae_on_site_datetime timestamp without time zone,
                ae_complete_datetime timestamp without time zone,ae_is_sla_delay boolean,ae_total_ma_time character varying,problem integer,
                survey_remark text,end_customer integer,
                device_contact character varying,device_tel character varying,memo text,part_ready boolean,
                state character varying,care_call_date date,sales integer,create_uid integer,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair enable trigger all ; 

             
               alter table neweb_repair_manager_note disable trigger all;
               delete from neweb_repair_manager_note ;
             insert into neweb_repair_manager_note(id,note_id,note_desc,create_uid,create_date,write_uid,write_date)
             select id,note_id,note_desc,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,note_id,note_desc,create_uid,create_date,write_uid,write_date from neweb_repair_manager_note')
              as fields (id integer,note_id integer,note_desc text,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_manager_note ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_manager_note_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_manager_note enable trigger all ;  
             
               alter table neweb_repair_repair_line disable trigger all;
               delete from neweb_repair_repair_line ;
             insert into neweb_repair_repair_line(id,sequence,contract_line,sla_delay_warn,repair_id,state,asset_num,ip_address,
                problem_desc,machine_serial_no,repair_timesheet_worktype,create_uid,create_date,write_uid,write_date)
             select id,sequence,contract_line,sla_delay_warn,repair_id,state,asset_num,ip_address,
                problem_desc,machine_serial_no,repair_timesheet_worktype,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,sequence,contract_line,sla_delay_warn,repair_id,state,asset_num,ip_address,
                problem_desc,machine_serial_no,repair_timesheet_worktype,create_uid,create_date,write_uid,write_date from neweb_repair_repair_line')
              as fields (id integer,sequence integer,contract_line integer,sla_delay_warn boolean,
                repair_id integer,state character varying,asset_num character varying,ip_address character varying,
                problem_desc text,machine_serial_no character varying,
                repair_timesheet_worktype character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair_line enable trigger all ;  
             
                alter table neweb_repair_repair_part disable trigger all;
                delete from neweb_repair_repair_part ;
             insert into neweb_repair_repair_part(id,prod,required_parts_qty,used_parts_qty,repair_line_id,state,part_maintenance_category_id,parts_categ,create_uid,create_date,write_uid,write_date)
             select id,prod,required_parts_qty,used_parts_qty,repair_line_id,state,part_maintenance_category_id,parts_categ,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,prod,required_parts_qty,used_parts_qty,repair_line_id,state,part_maintenance_category_id,parts_categ,create_uid,create_date,write_uid,write_date from neweb_repair_repair_part')
              as fields (id integer,prod integer,required_parts_qty integer,used_parts_qty integer,repair_line_id integer,
            state character varying,part_maintenance_category_id integer,parts_categ integer,create_uid integer,
            create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair_part ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_part_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair_part enable trigger all ;
             
                 alter table neweb_repair_repair_care_call_log disable trigger all;
                 delete from neweb_repair_repair_care_call_log ;
             insert into neweb_repair_repair_care_call_log(id,care_call_date,care_call_log,repair_id,state,create_uid,create_date,write_uid,write_date)
             select id,care_call_date,care_call_log,repair_id,state,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,care_call_date,care_call_log,repair_id,state,create_uid,create_date,write_uid,write_date from neweb_repair_repair_care_call_log')
              as fields (id integer,care_call_date date,care_call_log text,repair_id integer,state character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair_care_call_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_care_call_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair_care_call_log enable trigger all ;
             
              alter table neweb_repair_repair_work_log disable trigger all;
              delete from neweb_repair_repair_work_log ;
              insert into neweb_repair_repair_work_log(id,create_uid,repair_id,work_log,write_uid,state,write_date,create_date,work_date,work_emp,work_end_datetime,work_start_datetime)
             select id,create_uid,repair_id,work_log,write_uid,state,write_date,create_date,work_date,work_emp,work_end_datetime,work_start_datetime from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,create_uid,repair_id,work_log,write_uid,state,write_date,create_date,work_date,work_emp,work_end_datetime,work_start_datetime from neweb_repair_repair_work_log')
              as fields (id integer,create_uid integer,repair_id integer,work_log text,write_uid integer,state character varying,write_date timestamp without time zone,create_date timestamp without time zone,work_date date,work_emp integer,work_end_datetime timestamp without time zone,work_start_datetime timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair_work_log ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_work_log_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair_work_log enable trigger all ;
             
             alter table neweb_repair_repair_questionnaire disable trigger all;
             delete from neweb_repair_repair_questionnaire ;
             insert into neweb_repair_repair_questionnaire(id,question_id,rating,repair_id,state,create_uid,create_date,write_uid,write_date)
             select id,question_id,rating,repair_id,state,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,question_id,rating,repair_id,state,create_uid,create_date,write_uid,write_date from neweb_repair_repair_questionnaire')
              as fields (id integer,question_id integer,rating character varying,repair_id integer,state character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_repair_questionnaire ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repair_questionnaire_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repair_questionnaire enable trigger all ;
             
             alter table neweb_repair_parts_categ disable trigger all;
             delete from neweb_repair_parts_categ ;
             insert into neweb_repair_parts_categ(id,name,create_uid,create_date,write_uid,write_date)
             select id,name,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,create_uid,create_date,write_uid,write_date from neweb_repair_parts_categ')
              as fields (id integer,name character varying,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_repair_parts_categ ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_parts_categ_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_parts_categ enable trigger all ;
          
             alter table neweb_repair_repeatcall_excel_download disable trigger all;
             delete from neweb_repair_repeatcall_excel_download ;
             insert into neweb_repair_repeatcall_excel_download(id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file)
             select id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,xls_file_name,run_desc,create_uid,create_date,write_uid,write_date,xls_file from neweb_repair_repeatcall_excel_download')
              as fields (id integer,xls_file_name character varying,run_desc character varying,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                xls_file bytea) ;
             select max(id)+1 into maxseq from neweb_repair_repeatcall_excel_download ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_repair_repeatcall_excel_download_id_seq restart with ' || maxseq  ; 
             alter table neweb_repair_repeatcall_excel_download enable trigger all ;
          
             
            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists migcontract() cascade""")
        self._cr.execute("""create or replace function migcontract() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
            
            /* migration neweb_contract_contract */

             alter table neweb_contract_contract disable trigger all;
            insert into neweb_contract_contract(id,daily_maintain_hour_end,ae,site_check,warranty_end_date,cur_inspection_date,
                penalties,dr_time,is_maintenance_contract,write_uid,inspection_warn,recovery_rehearsal_status,
                warranty_warn,recovery_rehearsal_datetime,main_cost,daily_maintain_hour_start,
                customer_name,create_uid,need_recovery_rehearsal,end_customer,maintenance_warn_days,state,
                inspection_warn_days,warranty_warn_days,maintenance_start_date,contract_no,need_training,
                weekly_maintain_day,maintenance_end_date,sales_dept,main_manpower_cost,clinch_date,
                is_rental_contract,sales,recovery_rehearsal_description,contract_memo,deployment,warranty_start_date,inspection_date,is_sales_contract,project_no,write_date,name,tx_price,is_locked,maintenance_warn,
                inspection_method,subscribe_build,ae_dept,project,create_date,site_check_upload,is_outsourcing_service,contact_person,sla,revenue_analysis_mark,is_closed,is_signed,
                routine_maintenance_new,main_service_rule_new,contract_newold,
                need_control,is_warranty_contract,hasbackuphw,isduedate,cus_project)
             select id,daily_maintain_hour_end,ae,site_check,warranty_end_date,cur_inspection_date,
                penalties,dr_time,is_maintenance_contract,write_uid,inspection_warn,recovery_rehearsal_status,
                warranty_warn,recovery_rehearsal_datetime,main_cost,daily_maintain_hour_start,
                customer_name,create_uid,need_recovery_rehearsal,end_customer,maintenance_warn_days,state,
                inspection_warn_days,warranty_warn_days,maintenance_start_date,contract_no,need_training,
                weekly_maintain_day,maintenance_end_date,sales_dept,main_manpower_cost,clinch_date,
                is_rental_contract,sales,recovery_rehearsal_description,contract_memo,deployment,warranty_start_date,inspection_date,is_sales_contract,project_no,write_date,name,tx_price,is_locked,maintenance_warn,
                inspection_method,subscribe_build,ae_dept,project,create_date,site_check_upload,is_outsourcing_service,contact_person,sla,revenue_analysis_mark,is_closed,is_signed,
                routine_maintenance_new,main_service_rule_new,contract_newold,
                need_control,is_warranty_contract,hasbackuphw,isduedate,cus_project from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,daily_maintain_hour_end,ae,site_check,warranty_end_date,cur_inspection_date,
                penalties,dr_time,is_maintenance_contract,write_uid,inspection_warn,recovery_rehearsal_status,
                warranty_warn,recovery_rehearsal_datetime,main_cost,daily_maintain_hour_start,
                customer_name,create_uid,need_recovery_rehearsal,end_customer,maintenance_warn_days,state,
                inspection_warn_days,warranty_warn_days,maintenance_start_date,contract_no,need_training,
                weekly_maintain_day,maintenance_end_date,sales_dept,main_manpower_cost,clinch_date,
                is_rental_contract,sales,recovery_rehearsal_description,contract_memo,deployment,warranty_start_date,inspection_date,is_sales_contract,project_no,write_date,name,tx_price,is_locked,maintenance_warn,
                inspection_method,subscribe_build,ae_dept,project,create_date,site_check_upload,is_outsourcing_service,contact_person,sla,revenue_analysis_mark,is_closed,is_signed,
                routine_maintenance_new,main_service_rule_new,contract_newold,
                need_control,is_warranty_contract,hasbackuphw,isduedate,cus_project from neweb_contract_contract')
              as fields (id integer,daily_maintain_hour_end character varying,ae integer,site_check boolean,warranty_end_date date,cur_inspection_date character varying,
                penalties text,dr_time integer,is_maintenance_contract boolean,write_uid integer,
                inspection_warn boolean,recovery_rehearsal_status character varying,
                warranty_warn boolean,recovery_rehearsal_datetime timestamp without time zone,
                main_cost numeric,daily_maintain_hour_start character varying,
                customer_name integer,create_uid integer,need_recovery_rehearsal boolean,
                end_customer integer,maintenance_warn_days integer,state character varying,
                inspection_warn_days integer,warranty_warn_days integer,maintenance_start_date date,
                contract_no character varying,need_training boolean,weekly_maintain_day character varying,
                maintenance_end_date date,sales_dept integer,main_manpower_cost numeric,clinch_date date,
                is_rental_contract boolean,sales integer,recovery_rehearsal_description text,
                contract_memo text,deployment boolean,warranty_start_date date,inspection_date text,
                is_sales_contract boolean,project_no character varying,write_date timestamp without time zone,
                name character varying,tx_price double precision,is_locked boolean,maintenance_warn boolean,
                inspection_method character varying,subscribe_build boolean,ae_dept integer,project boolean,
                create_date timestamp without time zone,
                site_check_upload boolean,is_outsourcing_service boolean,contact_person integer,
                sla integer,revenue_analysis_mark boolean,is_closed boolean,is_signed boolean,
                routine_maintenance_new integer,main_service_rule_new integer,contract_newold character varying,
                need_control boolean,is_warranty_contract boolean,hasbackuphw boolean,
                isduedate boolean,cus_project character varying) ;
             select max(id)+1 into maxseq from neweb_contract_contract ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_contract_contract_id_seq restart with ' || maxseq  ; 
             alter table neweb_contract_contract enable trigger all ;
             
              /* migration neweb_contract_contract_line */

             alter table neweb_contract_contract_line disable trigger all;
            insert into neweb_contract_contract_line(id,sequence,prod,prod_modeltype,machine_serial_no,maintain_partner,prod_sla,
                contract_id,memo,special_warn,special_warn_date,special_warn_days,x_locked,contract_start_date,contract_end_date,prod_line_os,os_has_contract,
                prod_line_firmware,prod_line_db,db_has_contract,prod_set,prod_brand,create_uid,create_date,write_uid ,write_date,conline_item)
             select id,sequence,prod,prod_modeltype,machine_serial_no,maintain_partner,prod_sla,
                contract_id,memo,special_warn,special_warn_date,special_warn_days,x_locked,contract_start_date ,contract_end_date,prod_line_os,os_has_contract,
                prod_line_firmware,prod_line_db,db_has_contract,prod_set,prod_brand,create_uid,create_date,write_uid ,write_date,conline_item from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,sequence,prod,prod_modeltype,machine_serial_no,maintain_partner,prod_sla,
                contract_id,memo,special_warn,special_warn_date,special_warn_days,x_locked,contract_start_date ,contract_end_date,prod_line_os,os_has_contract,
                prod_line_firmware,prod_line_db,db_has_contract,prod_set,prod_brand,create_uid,create_date,write_uid ,write_date,conline_item from neweb_contract_contract_line')
              as fields (id integer,sequence integer,prod integer,prod_modeltype character varying,
                machine_serial_no character varying,maintain_partner integer,prod_sla integer,
                contract_id integer,memo text,special_warn boolean,special_warn_date date,
                special_warn_days integer,x_locked boolean,contract_start_date date,contract_end_date date,
                prod_line_os text,os_has_contract boolean,prod_line_firmware text,
                prod_line_db text,db_has_contract boolean,prod_set integer,prod_brand integer,
                create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone,conline_item integer) ;
             select max(id)+1 into maxseq from neweb_contract_contract_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_contract_contract_line_id_seq restart with ' || maxseq  ; 
             alter table neweb_contract_contract_line enable trigger all ;
             
              /* migration neweb_contract_inspection_list */

             alter table neweb_contract_inspection_list disable trigger all;
            insert into neweb_contract_inspection_list(id,inspection_id,subscribe_date,actual_date,inspection_memo,subscribe_year,create_uid,
                create_date,write_uid,write_date,actual_start_datetime,actual_end_datetime,emp_id)
             select id,inspection_id,subscribe_date,actual_date,inspection_memo,subscribe_year,create_uid,
                create_date,write_uid,write_date,actual_start_datetime,actual_end_datetime,emp_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,inspection_id,subscribe_date,actual_date,inspection_memo,subscribe_year,create_uid,
                create_date,write_uid,write_date,actual_start_datetime,actual_end_datetime,emp_id from neweb_contract_inspection_list')
              as fields (id integer,inspection_id integer,subscribe_date date,actual_date date,
                inspection_memo text,subscribe_year character varying,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                actual_start_datetime timestamp without time zone,actual_end_datetime timestamp without time zone,
                emp_id integer) ;
             select max(id)+1 into maxseq from neweb_contract_inspection_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_contract_inspection_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_contract_inspection_list enable trigger all ;
             
              /* migration neweb_contract_repaire_list */

             alter table neweb_contract_repaire_list disable trigger all;
            insert into neweb_contract_repaire_list(id,repaire_id,repaire_date,repaire_memo,create_uid,create_date,write_uid,write_date)
             select id,repaire_id,repaire_date,repaire_memo,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,repaire_id,repaire_date,repaire_memo,create_uid,create_date,write_uid,write_date from neweb_contract_repaire_list')
              as fields (id integer,repaire_id integer,repaire_date date,repaire_memo text,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_contract_repaire_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_contract_repaire_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_contract_repaire_list enable trigger all ;
             
              /* migration neweb_contract_dr_practice */

             alter table neweb_contract_dr_practice disable trigger all;
            insert into neweb_contract_dr_practice(id,dr_id,dr_date,dr_description,create_uid,create_date,write_uid,write_date)
             select id,dr_id,dr_date,dr_description,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,dr_id,dr_date,dr_description,create_uid,create_date,write_uid,write_date from neweb_contract_dr_practice')
              as fields (id integer,dr_id integer,dr_date date,dr_description text,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_contract_dr_practice ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_contract_dr_practice_id_seq restart with ' || maxseq  ; 
             alter table neweb_contract_dr_practice enable trigger all ;
             
              alter table neweb_contract_maintenance_warn_users_rel disable trigger all ;
            insert into neweb_contract_maintenance_warn_users_rel(neweb_contract_contract_id,hr_employee_id)
            select neweb_contract_contract_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,hr_employee_id from neweb_contract_maintenance_warn_users_rel')
             as fields (neweb_contract_contract_id integer,hr_employee_id integer) ;
             alter table neweb_contract_maintenance_warn_users_rel enable trigger all ;
             
              /* migration neweb_contract_warranty_warn_users_rel */
            
          /* alter table neweb_contract_warranty_warn_users_rel disable trigger all ;
            insert into neweb_contract_warranty_warn_users_rel(neweb_contract_contract_id,hr_employee_id)
            select neweb_contract_contract_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,hr_employee_id from neweb_contract_warranty_warn_users_rel')
             as fields (neweb_contract_contract_id integer,hr_employee_id integer) ;
             alter table neweb_contract_warranty_warn_users_rel enable trigger all ; */
             
              /* migration neweb_contract_inspection_warn_users_rel */
            
           /* alter table neweb_contract_inspection_warn_users_rel disable trigger all ;
            insert into neweb_contract_inspection_warn_users_rel(neweb_contract_contract_id,hr_employee_id)
            select neweb_contract_contract_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,hr_employee_id from neweb_contract_inspection_warn_users_rel')
             as fields (neweb_contract_contract_id integer,hr_employee_id integer) ;
             alter table neweb_contract_inspection_warn_users_rel enable trigger all ; */
             
              /* migration neweb_contract_satisfaction_partner_rel */
            
            alter table neweb_contract_satisfaction_partner_rel disable trigger all ;
            insert into neweb_contract_satisfaction_partner_rel(contract_id,partner_id)
            select contract_id,partner_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select contract_id,partner_id from neweb_contract_satisfaction_partner_rel')
             as fields (contract_id integer,partner_id integer) ;
             alter table neweb_contract_satisfaction_partner_rel enable trigger all ;
             
             /* migration hr_employee_neweb_contract_contract_rel */
            
            alter table hr_employee_neweb_contract_contract_rel disable trigger all ;
            insert into hr_employee_neweb_contract_contract_rel(neweb_contract_contract_id,hr_employee_id)
            select neweb_contract_contract_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,hr_employee_id from hr_employee_neweb_contract_contract_rel')
             as fields (neweb_contract_contract_id integer,hr_employee_id integer) ;
             alter table hr_employee_neweb_contract_contract_rel enable trigger all ;
             
             /* migration ir_attachment_neweb_contract_inspection_list_rel */
            
            alter table ir_attachment_neweb_contract_inspection_list_rel disable trigger all ;
            insert into ir_attachment_neweb_contract_inspection_list_rel(neweb_contract_inspection_list_id,ir_attachment_id)
            select neweb_contract_inspection_list_id,ir_attachment_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_inspection_list_id,ir_attachment_id from ir_attachment_neweb_contract_inspection_list_rel')
             as fields (neweb_contract_inspection_list_id integer,ir_attachment_id integer) ;
             alter table ir_attachment_neweb_contract_inspection_list_rel enable trigger all ;
             
               /* migration ir_attachment_neweb_contract_dr_practice_rel */
            
            alter table ir_attachment_neweb_contract_dr_practice_rel disable trigger all ;
            insert into ir_attachment_neweb_contract_dr_practice_rel(neweb_contract_dr_practice_id,ir_attachment_id)
            select neweb_contract_dr_practice_id,ir_attachment_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_dr_practice_id,ir_attachment_id from ir_attachment_neweb_contract_dr_practice_rel')
             as fields (neweb_contract_dr_practice_id integer,ir_attachment_id integer) ;
             alter table ir_attachment_neweb_contract_dr_practice_rel enable trigger all ;

            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists migcf() cascade""")
        self._cr.execute("""create or replace function migcf() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             delete from cf_template_history ;
             delete from cf_template ;
             delete from cf_template_category ;
            /* migration cf_template_category */

             alter table cf_template_category disable trigger all;
            insert into cf_template_category(id,name,create_uid,create_date,write_uid,write_date)
             select id,name,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,create_uid,create_date,write_uid,write_date from cf_template_category')
              as fields (id integer,name character varying,create_uid integer,create_date timestamp without time zone,
              write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from cf_template_category ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence cf_template_category_id_seq restart with ' || maxseq  ; 
             alter table cf_template_category enable trigger all ;
            
            
            /* migration cf_template */

             alter table cf_template disable trigger all;
            insert into cf_template(id,category_id,templ_id,name,description,create_uid,create_date,write_uid,write_date)
             select id,category_id,templ_id,name,description,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,category_id,templ_id,name,description,create_uid,create_date,write_uid,write_date from cf_template')
              as fields (id integer,category_id integer,templ_id character varying,name character varying,description text,create_uid integer,
              create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from cf_template ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence cf_template_id_seq restart with ' || maxseq  ; 
             alter table cf_template enable trigger all ;
             
             /* migration cf_template_history */

             alter table cf_template_history disable trigger all;
            insert into cf_template_history(id,category_id,origin,ver,templ_id,name,description,create_uid,create_date,write_uid,write_date)
             select id,category_id,origin,version,templ_id,name,description,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,category_id,origin,version,templ_id,name,description,create_uid,create_date,write_uid,write_date from cf_template_history')
              as fields (id integer,category_id integer,origin integer,version character varying,
                templ_id character varying,name character varying,description text,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from cf_template_history ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence cf_template_history_id_seq restart with ' || maxseq  ; 
             alter table cf_template_history enable trigger all ;

            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists migstock() cascade""")
        self._cr.execute("""create or replace function migstock() returns void as $BODY$
        DECLARE
          maxseq int;
        BEGIN
         perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
         
            /* migration stock_warehouse_orderpoint */
              
             alter table stock_warehouse_orderpoint disable trigger all;
            insert into stock_warehouse_orderpoint(id,name,active,warehouse_id,location_id,product_id,product_min_qty,product_max_qty,qty_multiple,group_id,
                company_id,lead_days,lead_type,create_uid,create_date,write_uid,write_date)
             select id,name,active,warehouse_id,location_id,product_id,product_min_qty,product_max_qty,qty_multiple,group_id,
                company_id,lead_days,lead_type,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,warehouse_id,location_id,product_id,product_min_qty,product_max_qty,qty_multiple,group_id,
                company_id,lead_days,lead_type,create_uid,create_date,write_uid,write_date from stock_warehouse_orderpoint')
              as fields (id integer,name character varying,active boolean,warehouse_id integer,location_id integer,
                product_id integer,product_min_qty numeric,product_max_qty numeric,qty_multiple numeric,group_id integer,
                company_id integer,lead_days integer,lead_type character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_warehouse_orderpoint ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_warehouse_orderpoint_id_seq restart with ' || maxseq  ; 
             alter table stock_warehouse_orderpoint enable trigger all ;
             
             /* migration stock_quant */

             alter table stock_quant disable trigger all;
            insert into stock_quant(id,product_id,company_id,location_id,lot_id,package_id,owner_id,quantity,in_date,create_uid,
                create_date,write_uid,write_date,reserved_quantity)
             select id,product_id,company_id,location_id,lot_id,package_id,owner_id,quantity,in_date,create_uid,
                create_date,write_uid,write_date,reserved_quantity from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,product_id,company_id,location_id,lot_id,package_id,owner_id,qty,in_date,create_uid,
                create_date,write_uid,write_date,0 from stock_quant')
              as fields (id integer,product_id integer,company_id integer,location_id integer,lot_id integer,package_id integer,owner_id integer,quantity double precision,in_date timestamp without time zone,create_uid integer,
                    create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,reserved_quantity double precision) ;
             select max(id)+1 into maxseq from stock_quant ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_quant_id_seq restart with ' || maxseq  ; 
             alter table stock_quant enable trigger all ;
             
              /* migration stock_picking */

             alter table stock_picking disable trigger all;
            insert into stock_picking(id,name,origin,note,backorder_id,move_type,state,group_id,priority,
                date,date_done,location_id,location_dest_id,picking_type_id,partner_id,company_id,
                owner_id,printed,create_uid,create_date,write_uid,write_date,stockin_type,
                stockout_type,stockin_checkman,stockin_desc,stockin_qc,stockin_checkyn,stockds_origin,stockin_qc_status,
                stockout_proj_no,stockout_custel,stockout_shipaddr,last_send_mail,stockout_customer,stockout_customer1,
                neweb_user_id,neweb_phone,neweb_email,neweb_address,neweb_fax,neweb_outmemo)
             select id,name,origin,note,backorder_id,move_type,state,group_id,priority,
                date,date_done,location_id,location_dest_id,picking_type_id,partner_id,company_id,
                owner_id,printed,create_uid,create_date,write_uid,write_date,stockin_type,
                stockout_type,stockin_checkman,stockin_desc,stockin_qc,stockin_checkyn,stockds_origin,stockin_qc_status,
                stockout_proj_no,stockout_custel,stockout_shipaddr,last_send_mail,stockout_customer,stockout_customer1,
                neweb_user_id,neweb_phone,neweb_email,neweb_address,neweb_fax,neweb_outmemo from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,origin,note,backorder_id,move_type,state,group_id,priority,
                date,date_done,location_id,location_dest_id,picking_type_id,partner_id,company_id,
                owner_id,printed,create_uid,create_date,write_uid,write_date,stockin_type,
                stockout_type,stockin_checkman,stockin_desc,stockin_qc,stockin_checkyn,stockds_origin,stockin_qc_status,
                stockout_proj_no,stockout_custel,stockout_shipaddr,last_send_mail,stockout_customer,stockout_customer1,
                neweb_user_id,neweb_phone,neweb_email,neweb_address,neweb_fax,neweb_outmemo from stock_picking')
              as fields (id integer,name character varying,origin character varying,note text,backorder_id integer,
                move_type character varying,state character varying,group_id integer,priority character varying,
                date timestamp without time zone,date_done timestamp without time zone,location_id integer,
                location_dest_id integer,picking_type_id integer,partner_id integer,company_id integer,
                owner_id integer,printed boolean,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone,stockin_type character varying,
                stockout_type character varying,stockin_checkman integer,stockin_desc text,stockin_qc boolean,
                stockin_checkyn boolean,stockds_origin character varying,stockin_qc_status character varying,
                stockout_proj_no character varying,stockout_custel character varying,stockout_shipaddr character varying,
                last_send_mail timestamp without time zone,stockout_customer character varying,stockout_customer1 integer,
                neweb_user_id integer,neweb_phone character varying,neweb_email character varying,neweb_address character varying,
                neweb_fax character varying,neweb_outmemo text) ;
             select max(id)+1 into maxseq from stock_picking ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_picking_id_seq restart with ' || maxseq  ; 
             alter table stock_picking enable trigger all ;
             
             /* migration stock_move */

             alter table stock_move disable trigger all;
            insert into stock_move(id,name,sequence,priority,create_date,date,company_id,date_expected,product_id,product_qty,product_uom_qty ,
            product_uom,location_id,location_dest_id,partner_id,picking_id,note,state,price_unit,origin,procure_method,scrapped,group_id,rule_id,
            picking_type_id,inventory_id,origin_returned_move_id,restrict_partner_id,warehouse_id,create_uid ,write_uid,write_date,purchase_line_id)
             select id,name,sequence,priority,create_date,date,company_id,date_expected,product_id,product_qty,product_uom_qty ,product_uom,location_id,
             location_dest_id,partner_id,picking_id,note,state,price_unit,origin,procure_method,scrapped,group_id,rule_id,picking_type_id,inventory_id,
             origin_returned_move_id,restrict_partner_id,warehouse_id,create_uid ,write_uid,write_date,purchase_line_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,sequence,priority,create_date,date,company_id,
             date_expected,product_id,product_qty,product_uom_qty ,product_uom,location_id,location_dest_id,partner_id,picking_id,note,state,price_unit,origin,
             procure_method,scrapped,group_id,rule_id,picking_type_id,inventory_id,origin_returned_move_id,restrict_partner_id,warehouse_id,create_uid ,write_uid,
             write_date,purchase_line_id from stock_move')
              as fields (id integer,name character varying,sequence integer,priority character varying,create_date timestamp without time zone,date timestamp without time zone,
              company_id integer,date_expected timestamp without time zone,product_id integer,product_qty numeric,product_uom_qty numeric,product_uom integer,location_id integer,
              location_dest_id integer,partner_id integer,picking_id integer,note text,state character varying,price_unit double precision,origin character varying,
              procure_method character varying,scrapped boolean,group_id integer,rule_id integer,picking_type_id integer,inventory_id integer,origin_returned_move_id integer,
              restrict_partner_id integer,warehouse_id integer,create_uid integer,write_uid integer,write_date timestamp without time zone,purchase_line_id integer) ;
             select max(id)+1 into maxseq from stock_move ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_move_id_seq restart with ' || maxseq  ; 
             alter table stock_move enable trigger all ;
             
             /* migration neweb_stockin_list */

             alter table neweb_stockin_list disable trigger all;
            insert into neweb_stockin_list(id,create_date,qc_man,prod_id,write_uid,stockin_desc,create_uid,stockin_sequence_id,stockin_spec,
                stockin_check,stockin_id,stockin_qcsendemail,stockin_prodno,stockin_modeltype,
                write_date,stockin_machinetype,stockin_num1,stockin_serial,stockin_sendemail,stockin_num,stockin_item)
             select id,create_date,qc_man,prod_id,write_uid,stockin_desc,create_uid,stockin_sequence_id,stockin_spec,
                stockin_check,stockin_id,stockin_qcsendemail,stockin_prodno,stockin_modeltype,
                write_date,stockin_machinetype,stockin_num1,stockin_serial,stockin_sendemail,stockin_num,stockin_item from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_date,qc_man,prod_id,write_uid,stockin_desc,create_uid,stockin_sequence_id,stockin_spec,
                stockin_check,stockin_id,stockin_qcsendemail,stockin_prodno,stockin_modeltype,
                write_date,stockin_machinetype,stockin_num1,stockin_serial,stockin_sendemail,stockin_num,stockin_item from neweb_stockin_list')
              as fields (id integer,create_date timestamp without time zone,qc_man integer,prod_id integer,write_uid integer,
                stockin_desc character varying,create_uid integer,stockin_sequence_id integer,stockin_spec text,
                stockin_check character varying,stockin_id integer,stockin_qcsendemail boolean,
                stockin_prodno character varying,stockin_modeltype character varying,
                write_date timestamp without time zone,stockin_machinetype character varying,stockin_num1 numeric,
                stockin_serial character varying,stockin_sendemail boolean,stockin_num numeric,stockin_item numeric) ;
             select max(id)+1 into maxseq from neweb_stockin_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_stockin_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_stockin_list enable trigger all ;
             
              /* migration neweb_stockout_list */

             alter table neweb_stockout_list disable trigger all;
            insert into neweb_stockout_list(id,stockout_prodno,stockout_num,stockout_modeltype,create_uid,write_uid,
                stockout_price,stockout_machinetype,stockout_sequence_id,stockout_id,write_date,
                create_date,stockout_desc,stockout_spec,line_item)
             select id,stockout_prodno,stockout_num,stockout_modeltype,create_uid,write_uid,
                stockout_price,stockout_machinetype,stockout_sequence_id,stockout_id,write_date,
                create_date,stockout_desc,stockout_spec,line_item from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,stockout_prodno,stockout_num,stockout_modeltype,create_uid,write_uid,
                stockout_price,stockout_machinetype,stockout_sequence_id,stockout_id,write_date,
                create_date,stockout_desc,stockout_spec,line_item from neweb_stockout_list')
              as fields (id integer,stockout_prodno character varying,stockout_num numeric,
                stockout_modeltype character varying,create_uid integer,write_uid integer,
                stockout_price numeric,stockout_machinetype character varying,stockout_sequence_id integer,
                stockout_id integer,write_date timestamp without time zone,
                create_date timestamp without time zone,stockout_desc character varying,
                stockout_spec character varying,line_item integer) ;
             select max(id)+1 into maxseq from neweb_stockout_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_stockout_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_stockout_list enable trigger all ;
             
              /* migration neweb_stockship_list */

             alter table neweb_stockship_list disable trigger all;
            insert into neweb_stockship_list(id,stockship_id,stockship_modeltype,stockship_prodno,create_uid,stockship_price,write_uid,stockship_spec,
                write_date,stockship_num,create_date,stockship_desc,stockship_machinetype,sequence,stockout_sequence_id,
                stockship_item,prod_serial,line_item)
             select id,stockship_id,stockship_modeltype,stockship_prodno,create_uid,stockship_price,write_uid,stockship_spec,
                write_date,stockship_num,create_date,stockship_desc,stockship_machinetype,sequence,stockout_sequence_id,
                stockship_item,prod_serial,line_item from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,stockship_id,stockship_modeltype,stockship_prodno,create_uid,stockship_price,write_uid,stockship_spec,
                write_date,stockship_num,create_date,stockship_desc,stockship_machinetype,sequence,stockout_sequence_id,
                stockship_item,prod_serial,line_item from neweb_stockship_list ')
              as fields (id integer,stockship_id integer,stockship_modeltype character varying,stockship_prodno character varying,
                create_uid integer,stockship_price numeric,write_uid integer,stockship_spec text,
                write_date timestamp without time zone,stockship_num numeric,create_date timestamp without time zone,
                stockship_desc text,stockship_machinetype character varying,sequence integer,stockout_sequence_id integer,
                stockship_item numeric,prod_serial text,line_item integer) ;
             select max(id)+1 into maxseq from neweb_stockship_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_stockship_list_id_seq restart with ' || maxseq  ; 
             alter table neweb_stockship_list enable trigger all ;
             
             /* migration neweb_payment_term_rule */

          alter table neweb_payment_term_rule disable trigger all;
            insert into neweb_payment_term_rule(id,create_uid,create_date,name,write_uid,write_date,active,sequence)
             select id,create_uid,create_date,name,write_uid,write_date,active,sequence from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,active,sequence from neweb_payment_term_rule')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,
                write_uid integer,write_date timestamp without time zone,active boolean,sequence integer) ;
             select max(id)+1 into maxseq from neweb_payment_term_rule ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_payment_term_rule_id_seq restart with ' || maxseq  ; 
             alter table neweb_payment_term_rule enable trigger all ; 
             
              /* migration stock_inventory */

             alter table stock_inventory disable trigger all;
            insert into stock_inventory(
                id,name,date,state,company_id,create_uid,create_date,write_uid,write_date,accounting_date)
             select id,name,date,state,company_id,create_uid,create_date,write_uid,write_date,accounting_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,name,date,state,company_id,create_uid,create_date,write_uid,write_date,accounting_date from stock_inventory')
              as fields (id integer,name character varying,date timestamp without time zone,state character varying,
                company_id integer,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,accounting_date date) ;
             select max(id)+1 into maxseq from stock_inventory ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_inventory_id_seq restart with ' || maxseq  ; 
             alter table stock_inventory enable trigger all ;
             
              /* migration stock_inventory_line */

             alter table stock_inventory_line disable trigger all;
            insert into stock_inventory_line(id,inventory_id,partner_id,product_id,product_uom_id,product_qty,location_id,package_id,prod_lot_id,company_id,
                theoretical_qty,create_uid,create_date,write_uid,write_date)
             select id,inventory_id,partner_id,product_id,product_uom_id,product_qty,location_id,package_id,prod_lot_id,company_id,
                theoretical_qty,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,inventory_id,partner_id,product_id,product_uom_id,product_qty,location_id,package_id,prod_lot_id,company_id,
                theoretical_qty,create_uid,create_date,write_uid,write_date from stock_inventory_line')
              as fields (id integer,inventory_id integer,partner_id integer,product_id integer,product_uom_id integer,
                product_qty numeric,location_id integer,package_id integer,prod_lot_id integer,company_id integer,
                theoretical_qty numeric,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_inventory_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_inventory_line_id_seq restart with ' || maxseq  ; 
             alter table stock_inventory_line enable trigger all ;
             
              /* migration procurement_group */

             alter table procurement_group disable trigger all;
            insert into procurement_group(id,partner_id,name,move_type,create_uid,create_date,write_uid,write_date)
             select id,partner_id,name,move_type,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                id,partner_id,name,move_type,create_uid,create_date,write_uid,write_date from procurement_group')
              as fields (id integer,partner_id integer,name character varying,move_type character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from procurement_group ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence procurement_group_id_seq restart with ' || maxseq  ; 
             alter table procurement_group enable trigger all ;
             
            perform dblink_disconnect('NEWEB') ;
        END;$BODY$
        LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod1() cascade""")
        self._cr.execute("""create or replace function migprod1() returns void as $BODY$
       DECLARE
         maxseq int ;
       BEGIN
           perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');

            /* migration ir_sequence */

           alter table ir_sequence disable trigger all;
           insert into ir_sequence(id,name,code,implementation,active,prefix,suffix,number_next,
               number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
               write_date)
            select id,name,code,implementation,active,prefix,suffix,number_next,
               number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
               write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,code,implementation,active,prefix,suffix,number_next,
               number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
               write_date from ir_sequence where id > 26')
             as fields (id integer,name character varying,code character varying,implementation character varying,
               active boolean,prefix character varying,suffix character varying,number_next integer,
               number_increment integer,padding integer,company_id integer,use_date_range boolean,
               create_uid integer,create_date timestamp without time zone,write_uid integer,
               write_date timestamp without time zone) ;
            select max(id)+1 into maxseq from ir_sequence ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence ir_sequence_id_seq restart with ' || maxseq  ; 
            alter table ir_sequence enable trigger all ; 

         
             perform dblink_disconnect('NEWEB') ;
         END;$BODY$
        LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod11() cascade""")
        self._cr.execute("""create or replace function migprod11() returns void as $BODY$
          DECLARE
            maxseq int ;
          BEGIN
              perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo'); 
    
              /* migration product_category */
    
              
              alter table product_category disable trigger all;
              insert into product_category(id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id)
               select id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id from
               dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id from product_category where id > 3')
                as fields (id integer,name character varying,parent_id integer,create_uid integer,
                  create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                  removal_strategy_id integer) ;
               select max(id)+1 into maxseq from product_category ;
               if maxseq is null then
                  maxseq = 1 ;
               end if ;
               execute 'alter sequence product_category_id_seq restart with ' || maxseq  ; 
               alter table product_category enable trigger all ;
              execute prodcate(); 
    
                perform dblink_disconnect('NEWEB') ;
            END;$BODY$
           LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod2() cascade""")
        self._cr.execute("""create or replace function migprod2() returns void as $BODY$
          DECLARE
            maxseq int ;
          BEGIN
              perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
                /* migration stock_location */
               
             alter table stock_location disable trigger all;
            insert into stock_location(id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date)
             select id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date from stock_location where id > 16')
              as fields (id integer,name character varying,complete_name character varying,active boolean,
                usage character varying,location_id integer,comment text,posx integer,posy integer,
                posz integer,company_id integer,scrap_location boolean,return_location boolean,
                removal_strategy_id integer,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_location ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_location_id_seq restart with ' || maxseq  ; 
             alter table stock_location enable trigger all ;      
             execute stockloc() ;  
            /* migration stock_location_route  */
              
            alter table stock_location_route disable trigger all ;
            insert into stock_location_route(id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable)
             select id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable from stock_location_route where id > 5')
              as fields (id integer,name character varying,active boolean,sequence integer,
                product_selectable boolean,product_categ_selectable boolean,warehouse_selectable boolean,
                supplied_wh_id integer,supplier_wh_id integer,company_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                sale_selectable boolean) ;
             select max(id)+1 into maxseq from stock_location_route ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_location_route_id_seq restart with ' || maxseq  ; 
             alter table stock_location_route enable trigger all ;    

             perform dblink_disconnect('NEWEB') ;
         END;$BODY$
        LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod3() cascade""")
        self._cr.execute("""create or replace function migprod3() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
             perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration stock_warehouse  */
             
             alter table stock_warehouse disable trigger all ;
             delete from stock_warehouse where id > 1 ;
            insert into stock_warehouse(id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,mto_pull_id,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,buy_pull_id)
             select id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,4,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,5 from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,4,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,5 from stock_warehouse where id > 1')
              as fields (id integer,name character varying,active boolean,company_id integer,partner_id integer,
                view_location_id integer,lot_stock_id integer,code character varying,reception_steps character varying,delivery_steps character varying,wh_input_stock_loc_id integer,wh_qc_stock_loc_id integer,
                wh_output_stock_loc_id integer,wh_pack_stock_loc_id integer,mto_pull_id integer,
                pick_type_id integer,pack_type_id integer,out_type_id integer,in_type_id integer,
                int_type_id integer,crossdock_route_id integer,reception_route_id integer,delivery_route_id integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,buy_to_resupply boolean,buy_pull_id integer) ;
             select max(id)+1 into maxseq from stock_warehouse ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_warehouse_id_seq restart with ' || maxseq  ; 
              
            update stock_warehouse set sequence=10 where sequence is null ;  
             
               /* migration stock_picking_type  */
              
             alter table stock_picking_type disable trigger all;
             delete from stock_picking_type where id > 5 ;
            insert into stock_picking_type(id,name,color,sequence,sequence_id,sequence_code,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,company_id,create_uid,create_date,write_uid,write_date)
             select id,name,color,sequence,sequence_id,'INT' as sequence_code,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,1,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,color,sequence,sequence_id,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,1,create_uid,create_date,write_uid,write_date from stock_picking_type where id > 5')
              as fields (id integer,name character varying,color integer,sequence integer,sequence_id integer,
               default_location_src_id integer,default_location_dest_id integer,
                code character varying,return_picking_type_id integer,show_entire_packs boolean,warehouse_id integer,active boolean,use_create_lots boolean,use_existing_lots boolean,company_id integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_picking_type ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_picking_type_id_seq restart with ' || maxseq  ; 
             alter table stock_picking_type enable trigger all ;      
             alter table stock_warehouse enable trigger all ;   
             perform genseqcode();  
             
             

            perform dblink_disconnect('NEWEB') ;
        END;$BODY$
       LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod4() cascade""")
        self._cr.execute("""create or replace function migprod4() returns void as $BODY$
        DECLARE
          maxseq int ;
        BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
             /* migration ir_attachment */
             
             
              
             alter table ir_attachment disable trigger all;
            insert into ir_attachment(id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date)
             select id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date from ir_attachment where id > 521')
              as fields (id integer,name character varying,description text,res_model character varying,
                res_field character varying,res_id integer,company_id integer,type character varying,
                url character varying,public boolean,db_datas bytea,store_fname character varying,
                file_size integer,checksum character varying,mimetype character varying,
                index_content text,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from ir_attachment ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence ir_attachment_id_seq restart with ' || maxseq  ; 
             alter table ir_attachment enable trigger all ;  

           perform dblink_disconnect('NEWEB') ;
       END;$BODY$
      LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists migprod5() cascade""")
        self._cr.execute("""create or replace function migprod5() returns void as $BODY$
               DECLARE
                 maxseq int ;
               BEGIN
                   perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
                     /* migration product_template */
                     
                   alter table product_template disable trigger all;
                   alter table product_product disable trigger all;
                   delete from product_product where id > 3 ;
                   delete from product_template where id > 3 ;         
            
                 
                insert into product_template(id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                    volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                    create_uid,create_date,write_uid,write_date,purchase_method,
                    purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification)
                 select id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                    volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                    create_uid,create_date,write_uid,write_date,purchase_method,
                    purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification from
                 dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                    volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                    create_uid,create_date,write_uid,write_date,purchase_method,
                    purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification from product_template where id > 3')
                  as fields (id integer,name character varying,sequence integer,description text,description_purchase text,
                    description_sale text,type character varying,rental boolean,categ_id integer,list_price numeric,
                    volume numeric,weight numeric,sale_ok boolean,purchase_ok boolean,uom_po_id integer,uom_id integer,
                    company_id integer,active boolean,color integer,default_code character varying,
                    create_uid integer,create_date timestamp without time zone,write_uid integer,
                    write_date timestamp without time zone,purchase_method character varying,
                    purchase_line_warn character varying,purchase_line_warn_msg text,sale_line_warn character varying,
                    sale_line_warn_msg text,expense_policy character varying,invoice_policy character varying,
                    sale_delay double precision,tracking character varying,description_picking text,
                    serial_no text,maintenance_category_id integer,is_maintenance_target boolean,
                    brand character varying,serial character varying,model character varying,
                    serial_num character varying,specification text) ;
                 select max(id)+1 into maxseq from product_template ;
                 if maxseq is null then
                    maxseq = 1 ;
                 end if ;
                 execute 'alter sequence product_template_id_seq restart with ' || maxseq  ; 
                 alter table product_template enable trigger all ;
                 
                  /* migration product_product */
                  
                 
                 
                insert into product_product(id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date)
                 select id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date from
                 dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date from product_product where id > 3')
                  as fields (id integer,default_code character varying,active boolean,product_tmpl_id integer,
                    barcode character varying,volume numeric,weight numeric,create_uid integer,
                    create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
                 select max(id)+1 into maxseq from product_product ;
                 if maxseq is null then
                    maxseq = 1 ;
                 end if ;
                 execute 'alter sequence product_product_id_seq restart with ' || maxseq  ; 
                 alter table product_product enable trigger all ;
                       
                  perform dblink_disconnect('NEWEB') ;
              END;$BODY$
             LANGUAGE plpgsql;  """)




        self._cr.execute("""drop function if exists migprod() cascade""")
        self._cr.execute("""create or replace function migprod() returns void as $BODY$
        DECLARE
          maxseq int ;
        BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
            
            delete from product_product where id > 3;
            delete from product_template where id > 3; 
            delete from ir_attachment where id > 485;
            delete from stock_warehouse where id > 1 ; 
            delete from stock_location_route where id > 5 ; 
            delete from stock_picking_type where id > 5 ; 
            delete from stock_location where id > 16 ;
            delete from product_category where id > 3 ; 
            delete from ir_sequence where id > 59 ; 
            
             /* migration ir_sequence */
             
             alter table ir_sequence disable trigger all;
            insert into ir_sequence(id,name,code,implementation,active,prefix,suffix,number_next,
                number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
                write_date)
             select id,name,code,implementation,active,prefix,suffix,number_next,
                number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
                write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,code,implementation,active,prefix,suffix,number_next,
                number_increment,padding,company_id,use_date_range,create_uid,create_date,write_uid,
                write_date from ir_sequence where id > 59')
              as fields (id integer,name character varying,code character varying,implementation character varying,
                active boolean,prefix character varying,suffix character varying,number_next integer,
                number_increment integer,padding integer,company_id integer,use_date_range boolean,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from ir_sequence ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence ir_sequence_id_seq restart with ' || maxseq  ; 
             alter table ir_sequence enable trigger all ;
            
            /* migration product_category */
             
             alter table product_category disable trigger all;
            insert into product_category(id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id)
             select id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,parent_id,create_uid,create_date,write_uid,write_date,removal_strategy_id from product_category where id > 3')
              as fields (id integer,name character varying,parent_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                removal_strategy_id integer) ;
             select max(id)+1 into maxseq from product_category ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence product_category_id_seq restart with ' || maxseq  ; 
             alter table product_category enable trigger all ;
             /* execute prodcate(); */
             
             /* migration stock_location */
               
             alter table stock_location disable trigger all;
            insert into stock_location(id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date)
             select id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,complete_name,active,usage,location_id,comment,posx,posy,
                posz,company_id,scrap_location,return_location,
                removal_strategy_id,create_uid,create_date,write_uid,write_date from stock_location where id > 16')
              as fields (id integer,name character varying,complete_name character varying,active boolean,
                usage character varying,location_id integer,comment text,posx integer,posy integer,
                posz integer,company_id integer,scrap_location boolean,return_location boolean,
                removal_strategy_id integer,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_location ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_location_id_seq restart with ' || maxseq  ; 
             alter table stock_location enable trigger all ;      
             execute stockloc() ;  
             
              /* migration stock_location_route  */
              
             alter table stock_location_route disable trigger all ;
            insert into stock_location_route(id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable)
             select id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,sequence,product_selectable,product_categ_selectable,warehouse_selectable,
                supplied_wh_id,supplier_wh_id,company_id,create_uid,create_date,write_uid,write_date,sale_selectable from stock_location_route where id > 5')
              as fields (id integer,name character varying,active boolean,sequence integer,
                product_selectable boolean,product_categ_selectable boolean,warehouse_selectable boolean,
                supplied_wh_id integer,supplier_wh_id integer,company_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                sale_selectable boolean) ;
             select max(id)+1 into maxseq from stock_location_route ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_location_route_id_seq restart with ' || maxseq  ; 
             alter table stock_location_route enable trigger all ;    
             
              /* migration stock_picking_type  */
              
             alter table stock_picking_type disable trigger all;
            insert into stock_picking_type(id,name,color,sequence,sequence_id,sequence_code,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,company_id,create_uid,create_date,write_uid,write_date)
             select id,name,color,sequence,sequence_id,'INT' as sequence_code,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,1,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,color,sequence,sequence_id,default_location_src_id,default_location_dest_id,
                code,return_picking_type_id,show_entire_packs,warehouse_id,active,use_create_lots,use_existing_lots,1,create_uid,create_date,write_uid,write_date from stock_picking_type where id > 5')
              as fields (id integer,name character varying,color integer,sequence integer,sequence_id integer,
               default_location_src_id integer,default_location_dest_id integer,
                code character varying,return_picking_type_id integer,show_entire_packs boolean,warehouse_id integer,active boolean,use_create_lots boolean,use_existing_lots boolean,company_id integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from stock_picking_type ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_picking_type_id_seq restart with ' || maxseq  ; 
             alter table stock_picking_type enable trigger all ;      
            /* perform genseqcode();  */
             
             /* migration stock_warehouse  */
             
             alter table stock_warehouse disable trigger all ;
            insert into stock_warehouse(id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,mto_pull_id,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,buy_pull_id)
             select id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,4,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,5 from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,company_id,partner_id,
                view_location_id,lot_stock_id,code,reception_steps,delivery_steps,wh_input_stock_loc_id,
                wh_qc_stock_loc_id,wh_output_stock_loc_id,wh_pack_stock_loc_id,4,
                pick_type_id,pack_type_id,out_type_id,in_type_id,int_type_id,crossdock_route_id,
                reception_route_id ,delivery_route_id,create_uid,create_date,write_uid,write_date,
                buy_to_resupply,5 from stock_warehouse where id > 1')
              as fields (id integer,name character varying,active boolean,company_id integer,partner_id integer,
                view_location_id integer,lot_stock_id integer,code character varying,reception_steps character varying,delivery_steps character varying,wh_input_stock_loc_id integer,wh_qc_stock_loc_id integer,
                wh_output_stock_loc_id integer,wh_pack_stock_loc_id integer,mto_pull_id integer,
                pick_type_id integer,pack_type_id integer,out_type_id integer,in_type_id integer,
                int_type_id integer,crossdock_route_id integer,reception_route_id integer,delivery_route_id integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,buy_to_resupply boolean,buy_pull_id integer) ;
             select max(id)+1 into maxseq from stock_warehouse ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence stock_warehouse_id_seq restart with ' || maxseq  ; 
             alter table stock_warehouse enable trigger all ;    
            /* update stock_warehouse set sequence=10 where sequence is null ;  */

             
             /* migration ir_attachment */
              
             alter table ir_attachment disable trigger all;
            insert into ir_attachment(id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date)
             select id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,description,res_model,res_field,res_id,company_id,type,
                url,public,db_datas,store_fname,file_size,checksum,mimetype,
                index_content,create_uid,create_date,write_uid,write_date from ir_attachment where id > 485')
              as fields (id integer,name character varying,description text,res_model character varying,
                res_field character varying,res_id integer,company_id integer,type character varying,
                url character varying,public boolean,db_datas bytea,store_fname character varying,
                file_size integer,checksum character varying,mimetype character varying,
                index_content text,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from ir_attachment ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence ir_attachment_id_seq restart with ' || maxseq  ; 
             alter table ir_attachment enable trigger all ; 
             
             /* migration product_template */
            
             alter table product_template disable trigger all;
            insert into product_template(id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                create_uid,create_date,write_uid,write_date,purchase_method,
                purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification)
             select id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                create_uid,create_date,write_uid,write_date,purchase_method,
                purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,sequence,description,description_purchase,description_sale,type,rental,categ_id,list_price,
                volume,weight,sale_ok,purchase_ok,uom_po_id,uom_id,company_id,active,color,default_code,
                create_uid,create_date,write_uid,write_date,purchase_method,
                purchase_line_warn,purchase_line_warn_msg,sale_line_warn,sale_line_warn_msg,expense_policy,invoice_policy,sale_delay,tracking,description_picking,serial_no,maintenance_category_id,is_maintenance_target,brand,serial,model,serial_num,specification from product_template where id > 3')
              as fields (id integer,name character varying,sequence integer,description text,description_purchase text,
                description_sale text,type character varying,rental boolean,categ_id integer,list_price numeric,
                volume numeric,weight numeric,sale_ok boolean,purchase_ok boolean,uom_po_id integer,uom_id integer,
                company_id integer,active boolean,color integer,default_code character varying,
                create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,purchase_method character varying,
                purchase_line_warn character varying,purchase_line_warn_msg text,sale_line_warn character varying,
                sale_line_warn_msg text,expense_policy character varying,invoice_policy character varying,
                sale_delay double precision,tracking character varying,description_picking text,
                serial_no text,maintenance_category_id integer,is_maintenance_target boolean,
                brand character varying,serial character varying,model character varying,
                serial_num character varying,specification text) ;
             select max(id)+1 into maxseq from product_template ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence product_template_id_seq restart with ' || maxseq  ; 
             alter table product_template enable trigger all ;
             
              /* migration product_product */
              
             alter table product_product disable trigger all;
            insert into product_product(id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date)
             select id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,default_code,active,product_tmpl_id,barcode,volume,weight,create_uid,create_date,write_uid,write_date from product_product where id > 3')
              as fields (id integer,default_code character varying,active boolean,product_tmpl_id integer,
                barcode character varying,volume numeric,weight numeric,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from product_product ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence product_product_id_seq restart with ' || maxseq  ; 
             alter table product_product enable trigger all ;
             
             update product_template set default_code=name where default_code is null ;
           
            perform dblink_disconnect('NEWEB') ;
        END;$BODY$
        LANGUAGE plpgsql;
        """)


        self._cr.execute("""drop function if exists migpur() cascade""")
        self._cr.execute("""create or replace function migpur() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN

           perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
           
           
           
            /* migration neweb_purchase_purchase_manager */
             
             alter table neweb_purchase_purchase_manager disable trigger all;
            insert into neweb_purchase_purchase_manager(id,create_uid,create_date,name,write_uid,write_date)
             select id,create_uid,create_date,name,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date from neweb_purchase_purchase_manager')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,name integer,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_purchase_purchase_manager ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_purchase_purchase_manager_id_seq restart with ' || maxseq  ;
             alter table neweb_purchase_purchase_manager enable trigger all ;

             /* migration neweb_pitem_list */
             
             alter table neweb_pitem_list disable trigger all;
            insert into neweb_pitem_list(id,pitem_spec,create_date,pitem_stockin_num,prod_id,write_uid,pitem_sum,pitem_model_type,
                create_uid,pitem_id,pitem_origin_id,pitem_warranty,
                pitem_machine_type,pitem_prod_no,pitem_origin_type,write_date,pitem_stockin_complete,pitem_delete_yn,pitem_num,pitem_origin_no,pitem_price,pitem_status,ap_select,pur_memo,sequence,chi_purchase_no)
             select id,pitem_spec,create_date,pitem_stockin_num,prod_id,write_uid,pitem_sum,pitem_model_type,
                create_uid,pitem_id,pitem_origin_id,pitem_warranty,
                pitem_machine_type,pitem_prod_no,pitem_origin_type,write_date,pitem_stockin_complete,pitem_delete_yn,pitem_num,pitem_origin_no,pitem_price,pitem_status,ap_select,pur_memo,sequence,chi_purchase_no from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,pitem_spec,create_date,pitem_stockin_num,prod_id,write_uid,pitem_sum,pitem_model_type,
                create_uid,pitem_id,pitem_origin_id,pitem_warranty,
                pitem_machine_type,pitem_prod_no,pitem_origin_type,write_date,pitem_stockin_complete,pitem_delete_yn,pitem_num,pitem_origin_no,pitem_price,pitem_status,ap_select,pur_memo,sequence,chi_purchase_no from neweb_pitem_list')
              as fields (id integer,pitem_spec text,create_date timestamp without time zone,pitem_stockin_num numeric,
                prod_id integer,write_uid integer,pitem_sum numeric,pitem_model_type character varying,
                create_uid integer,pitem_id integer,pitem_origin_id integer,pitem_warranty character varying,
                pitem_machine_type character varying,pitem_prod_no character varying,pitem_origin_type character varying,write_date timestamp without time zone,pitem_stockin_complete boolean,pitem_delete_yn boolean,pitem_num numeric,pitem_origin_no character varying,pitem_price numeric,
                pitem_status character varying,ap_select boolean,pur_memo text,
                sequence integer,chi_purchase_no character varying) ;
             select max(id)+1 into maxseq from neweb_pitem_list ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_pitem_list_id_seq restart with ' || maxseq  ;
             alter table neweb_pitem_list enable trigger all ;

            /* migration neweb_purchase_costtype */
             
             alter table neweb_purchase_costtype disable trigger all;
            insert into neweb_purchase_costtype(id,create_uid,create_date,name,write_uid,write_date)
             select id,create_uid,create_date,name,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date from neweb_purchase_costtype')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,
                name character varying,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_purchase_costtype ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_purchase_costtype_id_seq restart with ' || maxseq  ;
             alter table neweb_purchase_costtype enable trigger all ;

             /* migration neweb_require_purchase */
             
             alter table neweb_require_purchase disable trigger all;
            insert into neweb_require_purchase(id,create_date,write_uid,purchase_yn,require_desc,pay_type,expense_desc,
                asset_desc,state,create_uid,emp_name,write_date,catalog_attach_yn,
                asset_type,asset_custom,name,expense_type,
                ext_no,is_closed,is_signed,asset_expense_categ)
             select id,create_date,write_uid,purchase_yn,require_desc,pay_type,expense_desc,
                asset_desc,state,create_uid,emp_name,write_date,catalog_attach_yn,
                asset_type,asset_custom,name,expense_type,
                ext_no,is_closed,is_signed,asset_expense_categ from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_date,write_uid,purchase_yn,require_desc,pay_type,expense_desc,
                asset_desc,state,create_uid,emp_name,write_date,catalog_attach_yn,
                asset_type,asset_custom,name,expense_type,
                ext_no,is_closed,is_signed,asset_expense_categ from neweb_require_purchase')
              as fields (id integer,create_date timestamp without time zone,write_uid integer,purchase_yn boolean,require_desc text,pay_type character varying,expense_desc text,
                asset_desc text,state character varying,create_uid integer,emp_name integer,
                write_date timestamp without time zone,catalog_attach_yn character varying,
                asset_type character varying,asset_custom integer,name character varying,
                expense_type character varying,
                ext_no character varying,
                is_closed boolean,is_signed boolean,
                asset_expense_categ character varying) ;
             select max(id)+1 into maxseq from neweb_require_purchase ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_require_purchase_id_seq restart with ' || maxseq  ;
             alter table neweb_require_purchase enable trigger all ;

              /* migration neweb_require_purchase_item */
             
             alter table neweb_require_purchase_item disable trigger all;
            insert into neweb_require_purchase_item(id,pitem_desc,create_date,pitem_purnum,prod_id,write_uid,pitem_serial,
                create_uid,pitem_id,pitem_budget,supplier,pitem_price,purok,expense_custom,pitem_modeltype,
                pitem_pay,write_date,purchase_no,pitem_num,pitem_nid,pitem_no,pur_memo)
             select id,pitem_desc,create_date,pitem_purnum,prod_id,write_uid,pitem_serial,
                create_uid,pitem_id,pitem_budget,supplier,pitem_price,purok,expense_custom,pitem_modeltype,
                pitem_pay,write_date,purchase_no,pitem_num,pitem_nid,pitem_no,pur_memo from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,pitem_desc,create_date,pitem_purnum,prod_id,write_uid,pitem_serial,
                create_uid,pitem_id,pitem_budget,supplier,pitem_price,purok,expense_custom,pitem_modeltype,
                pitem_pay,write_date,purchase_no,pitem_num,pitem_nid,pitem_no,pur_memo from neweb_require_purchase_item')
              as fields (id integer,pitem_desc text,create_date timestamp without time zone,
                pitem_purnum numeric,prod_id integer,write_uid integer,pitem_serial character varying,
                create_uid integer,pitem_id integer,pitem_budget numeric,supplier integer,
                pitem_price numeric,purok boolean,expense_custom integer,pitem_modeltype character varying,
                pitem_pay boolean,write_date timestamp without time zone,purchase_no character varying,
                pitem_num numeric,pitem_nid integer,pitem_no character varying,pur_memo text) ;
             select max(id)+1 into maxseq from neweb_require_purchase_item ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_require_purchase_item_id_seq restart with ' || maxseq  ;
             alter table neweb_require_purchase_item enable trigger all ;

             /* migration neweb_ma_backup_type */
             
             alter table neweb_ma_backup_type disable trigger all;
            insert into neweb_ma_backup_type(id,create_uid,create_date,name,write_uid,write_date)
             select id,create_uid,create_date,name,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date from neweb_ma_backup_type')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,
                name character varying,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_ma_backup_type ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_ma_backup_type_id_seq restart with ' || maxseq  ;
             alter table neweb_ma_backup_type enable trigger all ;

             /* migration neweb_ma_parts_type */
             
             alter table neweb_ma_parts_type disable trigger all;
            insert into neweb_ma_parts_type(id,create_uid,create_date,name,write_uid,write_date)
             select id,create_uid,create_date,name,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date from neweb_ma_parts_type')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,
                name character varying,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_ma_parts_type ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_ma_parts_type_id_seq restart with ' || maxseq  ;
             alter table neweb_ma_parts_type enable trigger all ;

             /* migration neweb_requiregencode */
             
             alter table neweb_requiregencode disable trigger all;
            insert into neweb_requiregencode(id,create_uid,create_date,name,write_uid,write_date,gencode)
             select id,create_uid,create_date,name,write_uid,write_date,gencode from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,gencode from neweb_requiregencode')
              as fields (id integer,create_uid integer,create_date timestamp without time zone,
                name character varying,write_uid integer,write_date timestamp without time zone,gencode integer) ;
             select max(id)+1 into maxseq from neweb_requiregencode ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_requiregencode_id_seq restart with ' || maxseq  ;
             alter table neweb_requiregencode enable trigger all ;

             /* migration purchase_order_line */
             
             alter table purchase_order_line disable trigger all;
            insert into purchase_order_line(id,name,sequence,product_qty,date_planned,product_uom,product_id,price_unit,price_subtotal,price_total,price_tax,order_id,account_analytic_id,company_id,state,qty_invoiced,qty_received,partner_id,currency_id,create_uid,create_date,write_uid,write_date,pitem_modeltype,pitem_serial,pitem_no,write_type)
             select id,name,sequence,product_qty,date_planned,product_uom,product_id,price_unit,price_subtotal,price_total,price_tax,order_id,account_analytic_id,company_id,state,qty_invoiced,qty_received,partner_id,currency_id,create_uid,create_date,write_uid,write_date,pitem_modeltype,pitem_serial,pitem_no,write_type from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,sequence,product_qty,date_planned,product_uom,product_id,price_unit,price_subtotal,price_total,price_tax,order_id,account_analytic_id,company_id,state,qty_invoiced,qty_received,partner_id,currency_id,create_uid,create_date,write_uid,write_date,pitem_modeltype,pitem_serial,pitem_no,write_type from purchase_order_line')
              as fields (id integer,name text,sequence integer,product_qty numeric,date_planned timestamp without time zone,
                product_uom integer,product_id integer,price_unit numeric,price_subtotal numeric,price_total numeric,price_tax double precision,order_id integer,account_analytic_id integer,company_id integer,
                state character varying,qty_invoiced numeric,qty_received numeric,partner_id integer,currency_id integer,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone,pitem_modeltype character varying,pitem_serial character varying,pitem_no character varying,write_type character varying) ;
             select max(id)+1 into maxseq from purchase_order_line ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence purchase_order_line_id_seq restart with ' || maxseq  ;
             alter table purchase_order_line enable trigger all ;

              /* migration purchase_order */
             
             alter table purchase_order disable trigger all;
            insert into purchase_order(id,name,origin,partner_ref,date_order,date_approve,partner_id,dest_address_id,currency_id,state,
                notes,invoice_status,date_planned,amount_untaxed,amount_tax,amount_total,fiscal_position_id,
                payment_term_id,incoterm_id,user_id,company_id,create_uid,create_date,write_uid,write_date,
                picking_type_id,group_id,purchase_type,pitem_untax,
                pitem_tax,pitem_amounttot,taxes_id,purchase_loc,purchase_company,purchase_reciver,purchase_deliver,deliver_phone,deliver_date,deliver_date1,
                pur_rec_type_t,pur_rec_address_t,pur_rec_date_t,partner_contact,is_signed,invoiceok,purchase_memo,
                purchase_othernote,payment_desc,pay_term,purchase_default_receiver,is_closed,purchase_contract_type,pidno,cost_type ,foreign_purchase,invoice_mark,
                invoice_complete,invoice_openamount)
             select id,name,origin,partner_ref,date_order,date_approve,partner_id,dest_address_id,currency_id,state,
                notes,invoice_status,date_planned,amount_untaxed,amount_tax,amount_total,fiscal_position_id,
                payment_term_id,incoterm_id,user_id,company_id,create_uid,create_date,write_uid,write_date,
                picking_type_id,group_id,purchase_type,pitem_untax,
                pitem_tax,pitem_amounttot,taxes_id,purchase_loc,purchase_company,purchase_reciver,purchase_deliver,deliver_phone,
                deliver_date,deliver_date1,pur_rec_type_t,pur_rec_address_t,pur_rec_date_t,partner_contact,is_signed,invoiceok,purchase_memo,
                purchase_othernote,payment_desc,pay_term,purchase_default_receiver,is_closed,purchase_contract_type,pidno,cost_type ,foreign_purchase,
                invoice_mark,invoice_complete,invoice_openamount from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,origin,partner_ref,date_order,date_approve,partner_id,dest_address_id,currency_id,state,
                notes,invoice_status,date_planned,amount_untaxed,amount_tax,amount_total,fiscal_position_id,
                payment_term_id,incoterm_id,user_id,company_id,create_uid,create_date,write_uid,write_date,
                picking_type_id,group_id,purchase_type,pitem_untax,
                pitem_tax,pitem_amounttot,taxes_id,purchase_loc,purchase_company,purchase_reciver,purchase_deliver,deliver_phone,deliver_date,deliver_date1,pur_rec_type_t,pur_rec_address_t,pur_rec_date_t,partner_contact,
                is_signed,invoiceok,purchase_memo,purchase_othernote,payment_desc,pay_term,purchase_default_receiver,is_closed,purchase_contract_type,pidno,cost_type ,foreign_purchase,invoice_mark,invoice_complete,
                invoice_openamount from purchase_order')
              as fields (id integer,name character varying,origin character varying,partner_ref character varying,
                date_order timestamp without time zone,date_approve timestamp without time zone,
                partner_id integer,dest_address_id integer,currency_id integer,state character varying,
                notes text,invoice_status character varying,date_planned timestamp without time zone,
                amount_untaxed numeric,amount_tax numeric,amount_total numeric,fiscal_position_id integer,
                payment_term_id integer,incoterm_id integer,user_id integer,company_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                picking_type_id integer,group_id integer,purchase_type character varying,pitem_untax numeric,
                pitem_tax numeric,pitem_amounttot numeric,taxes_id integer,purchase_loc character varying,
                purchase_company text,purchase_reciver text,purchase_deliver text,deliver_phone character varying,
                deliver_date date,deliver_date1 date,pur_rec_type_t character varying,pur_rec_address_t character varying,pur_rec_date_t character varying,partner_contact integer,is_signed boolean,invoiceok boolean,purchase_memo text,purchase_othernote text,payment_desc character varying,pay_term character varying,purchase_default_receiver text,is_closed boolean,purchase_contract_type character varying,pidno character varying,cost_type integer,foreign_purchase boolean,invoice_mark boolean,
                invoice_complete boolean,invoice_openamount numeric) ;
             select max(id)+1 into maxseq from purchase_order ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence purchase_order_id_seq restart with ' || maxseq  ;
             alter table purchase_order enable trigger all ;


            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists migprojrel() cascade""")
        self._cr.execute("""create or replace function migprojrel() returns void as $BODY$
         DECLARE
           maxseq int;
         BEGIN
          perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
    
             /* migration neweb_engmaintype_neweb_proj_eng_assign_rel */
             
              alter table neweb_project_neweb_transationtype_rel disable trigger all;
             insert into neweb_project_neweb_transationtype_rel(neweb_project_id,neweb_transationtype_id)
             select neweb_project_id,neweb_transationtype_id from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select 
                neweb_project_id,neweb_transationtype_id from neweb_project_neweb_transationtype_rel')
              as fields (neweb_project_id integer,neweb_transationtype_id integer) ;
             alter table neweb_project_neweb_transationtype_rel enable trigger all ;
            
            alter table neweb_engmaintype_neweb_proj_eng_assign_rel disable trigger all ;
            insert into neweb_engmaintype_neweb_proj_eng_assign_rel(neweb_proj_eng_assign_id,neweb_engmaintype_id)
            select neweb_proj_eng_assign_id,neweb_engmaintype_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_proj_eng_assign_id,neweb_engmaintype_id from neweb_engmaintype_neweb_proj_eng_assign_rel')
             as fields (neweb_proj_eng_assign_id integer,neweb_engmaintype_id integer) ;
             alter table neweb_engmaintype_neweb_proj_eng_assign_rel enable trigger all ;

              /* migration hr_employee_neweb_contract_contract_rel */
            
           /* alter table hr_employee_neweb_contract_contract_rel disable trigger all ;
            insert into hr_employee_neweb_contract_contract_rel(neweb_contract_contract_id,hr_employee_id)
            select neweb_contract_contract_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,hr_employee_id from hr_employee_neweb_contract_contract_rel')
             as fields (neweb_contract_contract_id integer,hr_employee_id integer) ;
             alter table hr_employee_neweb_contract_contract_rel enable trigger all ; */

             /* migration hr_employee_neweb_sale_analysis_travel_report_rel */
            
            alter table hr_employee_neweb_sale_analysis_travel_report_rel disable trigger all ;
            insert into hr_employee_neweb_sale_analysis_travel_report_rel(neweb_sale_analysis_travel_report_id,hr_employee_id)
            select neweb_sale_analysis_travel_report_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_sale_analysis_travel_report_id,hr_employee_id from hr_employee_neweb_sale_analysis_travel_report_rel')
             as fields (neweb_sale_analysis_travel_report_id integer,hr_employee_id integer) ;
            alter table hr_employee_neweb_sale_analysis_travel_report_rel enable trigger all ;

           /* migration hr_employee_projengassign_rel */
            
            alter table hr_employee_projengassign_rel disable trigger all ;
            insert into hr_employee_projengassign_rel(ass_id,emp_id)
            select ass_id,emp_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select ass_id,emp_id from hr_employee_projengassign_rel')
             as fields (ass_id integer,emp_id integer) ;
            alter table hr_employee_projengassign_rel enable trigger all ;

            /* migration hr_employee_res_partner_rel */
            
            alter table hr_employee_res_partner_rel disable trigger all ;
            insert into hr_employee_res_partner_rel(res_partner_id,hr_employee_id)
            select res_partner_id,hr_employee_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select res_partner_id,hr_employee_id from hr_employee_res_partner_rel')
             as fields (res_partner_id integer,hr_employee_id integer) ;
            alter table hr_employee_res_partner_rel enable trigger all ;

            

            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;  """)


        self._cr.execute("""drop function if exists migproj3() cascade""")
        self._cr.execute("""create or replace function migproj3() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
            
             /* migration crm_team  */
            
            alter table crm_team disable trigger all ;
            delete from crm_team ;
            insert into crm_team(id,name,active,company_id,user_id,color,create_uid,create_date,write_uid,write_date,use_quotations,invoiced_target)
            select id,name,active,company_id,user_id,color,create_uid,create_date,write_uid,write_date,use_quotations,invoiced_target from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,company_id,user_id,color,create_uid,create_date,write_uid,write_date,use_quotations,invoiced_target from crm_team')
             as fields (id integer,name character varying,active boolean,company_id integer,user_id integer,color integer,
            create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,use_quotations boolean,invoiced_target integer) ;
            select max(id)+1 into maxseq from crm_team ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence crm_team_id_seq restart with ' || maxseq  ;
            alter table crm_team enable trigger all ; 

            /* migration neweb_routine_maintenance  */
            
            alter table neweb_routine_maintenance disable trigger all ;
            delete from neweb_routine_maintenance ;
            insert into neweb_routine_maintenance(id,create_uid,create_date,name,write_uid,write_date,active,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,active,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,active,sequence from neweb_routine_maintenance')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,
                    write_uid integer,write_date timestamp without time zone,active boolean,sequence integer) ;
            select max(id)+1 into maxseq from neweb_routine_maintenance ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_routine_maintenance_id_seq restart with ' || maxseq  ;
            alter table neweb_routine_maintenance enable trigger all ; 

            /* migration sale_order  */
            
            alter table sale_order disable trigger all ;
            delete from sale_order ;
            insert into sale_order(id,name,origin,client_order_ref, state,date_order,validity_date,
                create_date,user_id,partner_id,partner_invoice_id,partner_shipping_id,pricelist_id,
                invoice_status,note,amount_untaxed,amount_tax,amount_total,payment_term_id,fiscal_position_id,
                company_id,team_id,create_uid,write_uid,write_date,incoterm,picking_policy,warehouse_id,
                procurement_group_id,sitem_untax,sitem_tax,sitem_amounttot,taxes_id,neweb_memo,
                discount_amount,payment_term,open_account_day,maintenance_payment_type,project_payment_type,
                delivery_term,service_rule,warranty_service_rule,warranty_service_rule1,
                maintenance_service_rule,routine_maintenance,maintenance_start,maintenance_end,quotation_include,
                call_service_response,quotation_term,mobile_phone,work_phone,contact_id,quotation_memo,is_signed,
                is_closed,payment_term_new,warranty_service_rule_new,main_service_rule_new,routine_maintenance_new,
                project_name,contact_address,quotation_address,call_service_response1,credit_limit,credit_rulelist,project_no)
            select id,name,origin,client_order_ref, state,date_order,validity_date,
                create_date,user_id,partner_id,partner_invoice_id,partner_shipping_id,pricelist_id,
                invoice_status,note,amount_untaxed,amount_tax,amount_total,payment_term_id,fiscal_position_id,
                company_id,team_id,create_uid,write_uid,write_date,incoterm,picking_policy,warehouse_id,
                procurement_group_id,sitem_untax,sitem_tax,sitem_amounttot,taxes_id,neweb_memo,
                discount_amount,payment_term,open_account_day,maintenance_payment_type,project_payment_type,
                delivery_term,service_rule,warranty_service_rule,warranty_service_rule1,
                maintenance_service_rule,routine_maintenance,maintenance_start,maintenance_end,quotation_include,
                call_service_response,quotation_term,mobile_phone,work_phone,contact_id,quotation_memo,is_signed,
                is_closed,payment_term_new,warranty_service_rule_new,main_service_rule_new,routine_maintenance_new,
                project_name,contact_address,quotation_address,call_service_response1,credit_limit,credit_rulelist,project_no from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,origin,client_order_ref, state,date_order,validity_date,
                create_date,user_id,partner_id,partner_invoice_id,partner_shipping_id,pricelist_id,
                invoice_status,note,amount_untaxed,amount_tax,amount_total,payment_term_id,fiscal_position_id,
                company_id,team_id,create_uid,write_uid,write_date,incoterm,picking_policy,warehouse_id,
                procurement_group_id,sitem_untax,sitem_tax,sitem_amounttot,taxes_id,neweb_memo,
                discount_amount,payment_term,open_account_day,maintenance_payment_type,project_payment_type,
                delivery_term,service_rule,warranty_service_rule,warranty_service_rule1,
                maintenance_service_rule,routine_maintenance,maintenance_start,maintenance_end,quotation_include,
                call_service_response,quotation_term,mobile_phone,work_phone,contact_id,quotation_memo,is_signed,
                is_closed,payment_term_new,warranty_service_rule_new,main_service_rule_new,routine_maintenance_new,
                project_name,contact_address,quotation_address,call_service_response1,credit_limit,credit_rulelist,project_no from sale_order')
             as fields (id integer,name character varying,origin character varying,client_order_ref character varying,
                state character varying,date_order timestamp without time zone,validity_date date,
                create_date timestamp without time zone,user_id integer,partner_id integer,
                partner_invoice_id integer,partner_shipping_id integer,pricelist_id integer,
                invoice_status character varying,note text,amount_untaxed numeric,amount_tax numeric,
                amount_total numeric,payment_term_id integer,fiscal_position_id integer,company_id integer,
                team_id integer, create_uid integer,write_uid integer,write_date timestamp without time zone,
                incoterm integer,picking_policy character varying,warehouse_id integer,procurement_group_id integer,
                sitem_untax numeric,sitem_tax numeric,sitem_amounttot numeric,taxes_id integer,neweb_memo text,
                discount_amount numeric,payment_term character varying,open_account_day character varying,
                maintenance_payment_type character varying,project_payment_type character varying,
                delivery_term character varying,service_rule character varying,
                warranty_service_rule character varying,warranty_service_rule1 character varying,
                maintenance_service_rule character varying,routine_maintenance character varying,
                maintenance_start date,maintenance_end date,quotation_include integer,call_service_response integer,
                quotation_term integer,mobile_phone character varying,work_phone character varying,
                contact_id integer,quotation_memo text,is_signed boolean,is_closed boolean,payment_term_new integer,
                warranty_service_rule_new integer,main_service_rule_new integer,routine_maintenance_new integer,
                project_name character varying,contact_address integer,quotation_address character varying,
                call_service_response1 integer,credit_limit double precision,credit_rulelist text,project_no integer) ;
            select max(id)+1 into maxseq from sale_order ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence sale_order_id_seq restart with ' || maxseq  ;
            alter table sale_order enable trigger all ;

             /* migration neweb_sitem_list  */
       
            alter table neweb_sitem_list disable trigger all ;
            delete from neweb_sitem_list ;
            insert into neweb_sitem_list (id,sitem_cost,sitem_costsubtot,sitem_modeltype,write_date,create_uid,sitem_stockout_complete,
                sitem_price,sitem_profit,sitem_profitrate,write_uid,sitem_stockout_num,sitem_id,create_date,
                sitem_brand,sitem_desc,sitem_num,sitem_serial,sitem_item,newebmaindate,maintenance_start,
                maintenance_end,dept_id,cost_dept)
            select id,sitem_cost,sitem_costsubtot,sitem_modeltype,write_date,create_uid,sitem_stockout_complete,
                sitem_price,sitem_profit,sitem_profitrate,write_uid,sitem_stockout_num,sitem_id,create_date,
                sitem_brand,sitem_desc,sitem_num,sitem_serial,sitem_item,newebmaindate,maintenance_start,
                maintenance_end,dept_id,cost_dept from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,sitem_cost,sitem_costsubtot,sitem_modeltype,write_date,create_uid,sitem_stockout_complete,
                sitem_price,sitem_profit,sitem_profitrate,write_uid,sitem_stockout_num,sitem_id,create_date,
                sitem_brand,sitem_desc,sitem_num,sitem_serial,sitem_item,newebmaindate,maintenance_start,
                maintenance_end,dept_id,cost_dept from neweb_sitem_list')
             as fields (id integer,sitem_cost numeric,sitem_costsubtot numeric,sitem_modeltype character varying,
                write_date timestamp without time zone,create_uid integer,sitem_stockout_complete boolean,
                sitem_price numeric,sitem_profit numeric,sitem_profitrate numeric,write_uid integer,
                sitem_stockout_num numeric,sitem_id integer,create_date timestamp without time zone,
                sitem_brand integer,sitem_desc text,sitem_num numeric,sitem_serial character varying,
                sitem_item character varying,newebmaindate text,maintenance_start date,maintenance_end date,
                dept_id integer,cost_dept integer) ;
            select max(id)+1 into maxseq from neweb_sitem_list ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_sitem_list_id_seq restart with ' || maxseq  ;
            alter table neweb_sitem_list enable trigger all ;

             /* migration neweb_projprodset  */
            
            alter table neweb_projprodset disable trigger all ;
            delete from neweb_projprodset ;
            insert into neweb_projprodset(id,create_uid,prod_revenue_tot,write_uid,prodset_id,prod_set,write_date,create_date,prod_price_tot)
            select id,create_uid,prod_revenue_tot,write_uid,prodset_id,prod_set,write_date,create_date,prod_price_tot from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,prod_revenue_tot,write_uid,prodset_id,prod_set,write_date,create_date,prod_price_tot from neweb_projprodset')
             as fields (id integer,create_uid integer,prod_revenue_tot numeric,write_uid integer,prodset_id integer,
                prod_set integer,write_date timestamp without time zone,create_date timestamp without time zone,
                prod_price_tot numeric) ;
            select max(id)+1 into maxseq from neweb_projprodset ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projprodset_id_seq restart with ' || maxseq  ;
            alter table neweb_projprodset enable trigger all ;

              /* migration neweb_salenocheck  */
            
            alter table neweb_salenocheck disable trigger all ;
            delete from neweb_salenocheck ;
            insert into neweb_salenocheck(id,create_uid,trans_proj,vernum,sale_no,write_uid,write_date,create_date)
            select id,create_uid,trans_proj,vernum,sale_no,write_uid,write_date,create_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,trans_proj,vernum,sale_no,write_uid,write_date,create_date from neweb_salenocheck where id > 2282')
             as fields (id integer,create_uid integer,trans_proj boolean,vernum integer,sale_no character varying,
                write_uid integer,write_date timestamp without time zone,create_date timestamp without time zone) ;
            select max(id)+1 into maxseq from neweb_salenocheck ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_salenocheck_id_seq restart with ' || maxseq  ;
            alter table neweb_salenocheck enable trigger all ;

             /* migration neweb_quotation_include  */
            
           alter table neweb_quotation_include disable trigger all ;
           delete from neweb_quotation_include ;
            insert into neweb_quotation_include(id,name,sequence,create_uid,create_date,write_uid,write_date)
            select id,name,sequence,create_uid,create_date,write_uid,write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,sequence,create_uid,create_date,write_uid,write_date from neweb_quotation_include')
             as fields (id integer,name character varying,sequence integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
            select max(id)+1 into maxseq from neweb_quotation_include ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_quotation_include_id_seq restart with ' || maxseq  ;
            alter table neweb_quotation_include enable trigger all ; 

             /* migration neweb_call_service_response  */
            
            alter table neweb_call_service_response disable trigger all ;
            delete from neweb_call_service_response ;
            insert into neweb_call_service_response(id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_call_service_response')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,
                name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_call_service_response ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_call_service_response_id_seq restart with ' || maxseq  ;
            alter table neweb_call_service_response enable trigger all ;

             /* migration neweb_partner_list  */
            
            alter table neweb_partner_list disable trigger all ;
            delete from neweb_partner_list ;
            insert into neweb_partner_list(id,comment,function,tel,create_uid,mobile,email,contact_type,cus_name,write_uid,tel1,birthday,
                contact,write_date,address,create_date,vat,sales)
            select id,comment,function,tel,create_uid,mobile,email,contact_type,cus_name,write_uid,tel1,birthday,
                contact,write_date,address,create_date,vat,sales from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,comment,function,tel,create_uid,mobile,email,contact_type,cus_name,write_uid,tel1,birthday,
                contact,write_date,address,create_date,vat,sales from neweb_partner_list')
             as fields (id integer,comment text,function character varying,tel character varying,create_uid integer,
                mobile character varying,email character varying,contact_type integer,
                cus_name character varying,write_uid integer,tel1 character varying,birthday character varying,
                contact character varying,write_date timestamp without time zone,address character varying,
                create_date timestamp without time zone,vat character varying,sales character varying) ;
            select max(id)+1 into maxseq from neweb_partner_list ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_partner_list_id_seq restart with ' || maxseq  ;
            alter table neweb_partner_list enable trigger all ;

              /* migration neweb_saleorder_excel_download  */
            
            alter table neweb_saleorder_excel_download disable trigger all ;
            delete from neweb_saleorder_excel_download ;
            insert into neweb_saleorder_excel_download(id,create_uid,xls_file,xls_file_name,write_uid,write_date,run_desc,create_date)
            select id,create_uid,xls_file,xls_file_name,write_uid,write_date,run_desc,create_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,xls_file,xls_file_name,write_uid,write_date,run_desc,create_date from neweb_saleorder_excel_download')
             as fields (id integer,create_uid integer,xls_file bytea,xls_file_name character varying,
                write_uid integer,write_date timestamp without time zone,run_desc character varying,
                create_date timestamp without time zone) ;
            select max(id)+1 into maxseq from neweb_saleorder_excel_download ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_saleorder_excel_download_id_seq restart with ' || maxseq  ;
            alter table neweb_saleorder_excel_download enable trigger all ;

            /* migration neweb_cost_dept  */
            
            alter table neweb_cost_dept disable trigger all ;
            delete from neweb_cost_dept ;
            insert into neweb_cost_dept(id,create_uid,create_date,name,sequence,write_uid,write_date,active)
            select id,create_uid,create_date,name,sequence,write_uid,write_date,active from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,sequence,write_uid,write_date,active from neweb_cost_dept')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,
                sequence integer,write_uid integer,write_date timestamp without time zone,active boolean) ;
            select max(id)+1 into maxseq from neweb_cost_dept ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_cost_dept_id_seq restart with ' || maxseq  ;
            alter table neweb_cost_dept enable trigger all ; 

              /* migration neweb_setupcost_line  */
            
            alter table neweb_setupcost_line disable trigger all ;
            delete from neweb_setupcost_line ;
            insert into neweb_setupcost_line(id,create_uid,r6_revenue,name,nt_percent,r6_percent,nt_revenue,networking_percent,write_uid,
                    write_date,create_date,project_id,networking_revenue)
            select id,create_uid,r6_revenue,name,nt_percent,r6_percent,nt_revenue,networking_percent,write_uid,
                    write_date,create_date,project_id,networking_revenue from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,r6_revenue,name,nt_percent,r6_percent,nt_revenue,networking_percent,write_uid,
                    write_date,create_date,project_id,networking_revenue from neweb_setupcost_line')
             as fields (id integer,create_uid integer,r6_revenue numeric,name character varying,nt_percent numeric,
                    r6_percent numeric,nt_revenue numeric,networking_percent numeric,write_uid integer,
                    write_date timestamp without time zone,create_date timestamp without time zone,
                    project_id integer,networking_revenue numeric) ;
            select max(id)+1 into maxseq from neweb_setupcost_line ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_setupcost_line_id_seq restart with ' || maxseq  ;
            alter table neweb_setupcost_line enable trigger all ;

             /* migration neweb_maincost_line */
            
            alter table neweb_maincost_line disable trigger all ;
            delete from neweb_maincost_line ;
            insert into neweb_maincost_line(id,create_uid,r6_revenue,create_date,networking_revenue,nt_percent,r6_percent,support_percent,
                    nt_revenue,networking_percent,write_uid,write_date,support_revenue,project_id,name,keytype,subtot_revenue1)
            select id,create_uid,r6_revenue,create_date,networking_revenue,nt_percent,r6_percent,support_percent,
                    nt_revenue,networking_percent,write_uid,write_date,support_revenue,project_id,name,keytype,subtot_revenue1 from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,r6_revenue,create_date,networking_revenue,nt_percent,r6_percent,support_percent,
                    nt_revenue,networking_percent,write_uid,write_date,support_revenue,project_id,name,keytype,subtot_revenue1 from neweb_maincost_line')
             as fields (id integer,create_uid integer,r6_revenue numeric,create_date timestamp without time zone,
                    networking_revenue numeric,nt_percent numeric,r6_percent numeric,support_percent numeric,
                    nt_revenue numeric,networking_percent numeric,write_uid integer,write_date timestamp without time zone,support_revenue numeric,project_id integer,name character varying,
                    keytype character varying,subtot_revenue1 numeric) ;
            select max(id)+1 into maxseq from neweb_maincost_line ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_maincost_line_id_seq restart with ' || maxseq  ;
            alter table neweb_maincost_line enable trigger all ;

            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql
         """)

        self._cr.execute("""drop function if exists migproj2() cascade""")
        self._cr.execute("""create or replace function migproj2() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
        
            /* migration neweb_projsaleitem  */
            
            alter table neweb_projsaleitem disable trigger all ;
            insert into neweb_projsaleitem (id,warranty,create_date,prod_modeltype,write_uid,create_uid,prod_desc,prod_set,prod_price,supplier,prod_purnum,paymark_date,
            prod_serial,purok,purchase_no,prod_brand,write_date,prod_revenue,saleitem_id,prod_num,prod_no,cost_type,origin_warranty,neweb_warranty,origin_end_date,
            neweb_end_date,origin_start_date,neweb_start_date,saleitem_item,prod_stockoutnum,prod_stockout_complete,dept_id,chi_product_no,chi_export_product,chi_sales_no,cost_dept,is_can_update,line_item,not_chiout)
            select id,warranty,create_date,prod_modeltype,write_uid,create_uid,prod_desc,prod_set,prod_price,supplier,prod_purnum,paymark_date,
            prod_serial,purok,purchase_no,prod_brand,write_date,prod_revenue,saleitem_id,prod_num,prod_no,cost_type,origin_warranty,neweb_warranty,origin_end_date,
            neweb_end_date,origin_start_date,neweb_start_date,saleitem_item,prod_stockoutnum,prod_stockout_complete,dept_id,chi_product_no,chi_export_product,chi_sales_no,cost_dept,is_can_update,line_item,not_chiout from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,warranty,create_date,prod_modeltype,write_uid,create_uid,prod_desc,prod_set,prod_price,supplier,prod_purnum,paymark_date,
            prod_serial,purok,purchase_no,prod_brand,write_date,prod_revenue,saleitem_id,prod_num,prod_no,cost_type,origin_warranty,neweb_warranty,origin_end_date,
            neweb_end_date,origin_start_date,neweb_start_date,saleitem_item,prod_stockoutnum,prod_stockout_complete,dept_id,chi_product_no,chi_export_product,chi_sales_no,cost_dept,is_can_update,line_item,not_chiout from neweb_projsaleitem')
             as fields (id integer,warranty character varying,create_date timestamp without time zone,prod_modeltype character varying,write_uid integer,create_uid integer,prod_desc text,prod_set integer,prod_price numeric,supplier integer,prod_purnum numeric,paymark_date date,
            prod_serial text,purok boolean,purchase_no character varying,prod_brand integer,write_date timestamp without time zone,prod_revenue numeric,saleitem_id integer,prod_num numeric,prod_no character varying,cost_type integer,origin_warranty integer,neweb_warranty integer,origin_end_date date,
            neweb_end_date date,origin_start_date date,neweb_start_date date,saleitem_item character varying,prod_stockoutnum double precision,prod_stockout_complete boolean,dept_id integer,chi_product_no character varying,chi_export_product boolean,chi_sales_no character varying,cost_dept integer,
            is_can_update boolean,line_item integer,not_chiout boolean) ;
            select max(id)+1 into maxseq from neweb_projsaleitem ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projsaleitem_id_seq restart with ' || maxseq  ;
            alter table neweb_projsaleitem enable trigger all ;

             /* migration neweb_engmaintype  */
            
            alter table neweb_engmaintype disable trigger all ;
            insert into neweb_engmaintype (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_engmaintype')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_engmaintype ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_engmaintype_id_seq restart with ' || maxseq  ;
            alter table neweb_engmaintype enable trigger all ;
            
            /* migration neweb_costtype */
            
             alter table neweb_costtype disable trigger all;
            insert into neweb_costtype(id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence)
             select id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence from neweb_costtype')
              as fields (id integer,create_uid integer,name character varying,write_uid integer,write_date timestamp without time zone,create_date timestamp without time zone,costtype_sequence integer,sequence integer) ;
             select max(id)+1 into maxseq from neweb_costtype ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence neweb_costtype_id_seq restart with ' || maxseq  ;
             alter table neweb_costtype enable trigger all ;

             /* migration neweb_projanalysys  */
            
            alter table neweb_projanalysis disable trigger all ;
            insert into neweb_projanalysis (id,create_uid,analysis_sequence,analysis_id,analysis_costtype,write_uid,write_date,analysis_cost,analysis_profit,create_date,analysis_profitrate,analysis_revenue)
            select id,create_uid,analysis_sequence,analysis_id,analysis_costtype,write_uid,write_date,analysis_cost,analysis_profit,create_date,analysis_profitrate,analysis_revenue from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,analysis_sequence,analysis_id,analysis_costtype,write_uid,write_date,analysis_cost,analysis_profit,create_date,analysis_profitrate,analysis_revenue from neweb_projanalysis')
             as fields (id integer,create_uid integer,analysis_sequence integer,analysis_id integer,analysis_costtype integer,write_uid integer,write_date timestamp without time zone,analysis_cost numeric,analysis_profit numeric,create_date timestamp without time zone,analysis_profitrate numeric,analysis_revenue numeric) ;
            select max(id)+1 into maxseq from neweb_projanalysis ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projanalysis_id_seq restart with ' || maxseq  ;
            alter table neweb_projanalysis enable trigger all ;

             /* migration neweb_project  */
             alter table neweb_project disable trigger all ;
            insert into neweb_project (id,assign_no,write_uid,acc_receivable,comp_ename,main_other,old_contact_cost,
            total_saleitem_amount,invoice_type,invoice_description,cus_name,post_term,warranty_start_date,contract_build_mark,
            send_letter_date,name,main_cus_name,eng_main_type,sales_member,proj_branch,post_date,decision_date,other_date,
            self_rece_stamp,parent_projno,old_contact_revenue,acceptance_step,state,acceptance_other_desc,proj_paytype,origin_warranty_desc,setup_type,
            setup_description,other_warranty_desc,tt_date,proj_sale,comp_cname,proj_other_desc,main_end_date,group_name,proj_acceptance_date,total_saleitem_tax,
            shipping_type,create_date,create_uid,warranty_end_date,comp_sname,memo,cus_order,neweb_warranty_desc,ship_type,proj_step,cus_project,
            main_paytype,proj_pay,neweb_manpower_desc,sale_no,eng_assign,acceptance_date,ship_description,self_receive_date,acc_close_day,purchase_yn,
            complete_days,main_start_date,post_envelop,total_saleitem,proj_complete_days,setup_date,cate_type,proj_pay_type,description,sno,pay_term,
            write_date,payto_date,taxes_id,is_closed,is_signed,invoice_openamount,invoice_mark,invoice_complete,proj_cost_case,
            proj_main_case,firstgen,acc_close_day1,discount_amount,self_receive_type,proj_info_memo,proj_info_desc,warrantyyn,projectyn,
            maintenanceyn,opentrender,proj_import_status,main_service_rule_new,routine_maintenance_new,call_service_response,proj_pay1,
            company_id,revenue_ratio,chi_export_outcome,chi_invoice_complete,chi_export_income,chi_export_project,chi_export_product,
            open_account_day,stamp_duty_type,have_contract,stampduty_apply,proj_write_num,proj_status)
            select id,assign_no,write_uid,acc_receivable,comp_ename,main_other,old_contact_cost,total_saleitem_amount,
            invoice_type,invoice_description,cus_name,post_term,warranty_start_date,contract_build_mark,
            send_letter_date,name,main_cus_name,eng_main_type,sales_member,proj_branch,post_date,decision_date,other_date,self_rece_stamp,parent_projno,
            old_contact_revenue,acceptance_step,state,acceptance_other_desc,proj_paytype,origin_warranty_desc,setup_type,setup_description,
            other_warranty_desc,tt_date,proj_sale,comp_cname,proj_other_desc,main_end_date,group_name,proj_acceptance_date,total_saleitem_tax,
            shipping_type,create_date,create_uid,warranty_end_date,comp_sname,memo,cus_order,neweb_warranty_desc,ship_type,
            proj_step,cus_project,main_paytype,proj_pay,neweb_manpower_desc,sale_no,eng_assign,acceptance_date,ship_description,self_receive_date,
            acc_close_day,purchase_yn,complete_days,main_start_date,post_envelop,total_saleitem,proj_complete_days,setup_date,cate_type,
            proj_pay_type,description,sno,pay_term,write_date,payto_date,taxes_id,is_closed,is_signed,invoice_openamount,
            invoice_mark,invoice_complete,proj_cost_case,proj_main_case,firstgen,acc_close_day1,discount_amount,self_receive_type,
            proj_info_memo,proj_info_desc,warrantyyn,projectyn,maintenanceyn,opentrender,proj_import_status,main_service_rule_new,routine_maintenance_new,
            call_service_response,proj_pay1,company_id,revenue_ratio,chi_export_outcome,chi_invoice_complete,chi_export_income,chi_export_project,
            chi_export_product,open_account_day,stamp_duty_type,have_contract,stampduty_apply,proj_write_num,proj_status from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,assign_no,write_uid,acc_receivable,
            comp_ename,main_other,old_contact_cost,total_saleitem_amount,invoice_type,invoice_description,
            cus_name,post_term,warranty_start_date,contract_build_mark,send_letter_date,name,main_cus_name,eng_main_type,
            sales_member,proj_branch,post_date,decision_date,other_date,self_rece_stamp,parent_projno,old_contact_revenue,acceptance_step,state,
            acceptance_other_desc,proj_paytype,origin_warranty_desc,setup_type,setup_description,other_warranty_desc,tt_date,proj_sale,
            comp_cname,proj_other_desc,main_end_date,group_name,proj_acceptance_date,total_saleitem_tax,shipping_type,create_date,create_uid,
            warranty_end_date,comp_sname,memo,cus_order,neweb_warranty_desc,ship_type,proj_step,cus_project,main_paytype,
            proj_pay,neweb_manpower_desc,sale_no,eng_assign,acceptance_date,ship_description,self_receive_date,acc_close_day,purchase_yn,
            complete_days,main_start_date,post_envelop,total_saleitem,proj_complete_days,setup_date,cate_type,proj_pay_type,description,sno,
            pay_term,write_date,payto_date,taxes_id,is_closed,is_signed,invoice_openamount,invoice_mark,invoice_complete,
            proj_cost_case,proj_main_case,firstgen,acc_close_day1,discount_amount,self_receive_type,proj_info_memo,proj_info_desc,
            warrantyyn,projectyn,maintenanceyn,opentrender,proj_import_status,main_service_rule_new,routine_maintenance_new,call_service_response,
            proj_pay1,company_id,revenue_ratio,chi_export_outcome,chi_invoice_complete,chi_export_income,chi_export_project,chi_export_product,
            open_account_day,stamp_duty_type,have_contract,stampduty_apply,proj_write_num,proj_status from neweb_project')
             as fields (id integer,assign_no character varying,write_uid integer,acc_receivable character varying,
             comp_ename character varying,main_other text,old_contact_cost numeric,total_saleitem_amount numeric,
             invoice_type character varying,invoice_description text,cus_name integer,post_term character varying,warranty_start_date date,
             contract_build_mark boolean,send_letter_date date,name character varying,main_cus_name integer,
             eng_main_type integer,sales_member character varying,proj_branch integer,post_date character varying,decision_date date,
             other_date character varying,self_rece_stamp character varying,parent_projno character varying,old_contact_revenue numeric,
             acceptance_step character varying,state character varying,acceptance_other_desc text,proj_paytype text,origin_warranty_desc text,
             setup_type character varying,setup_description text,other_warranty_desc text,tt_date character varying,proj_sale integer,comp_cname character varying,
             proj_other_desc text,main_end_date date,group_name character varying,proj_acceptance_date date,total_saleitem_tax numeric,shipping_type character varying,
             create_date timestamp without time zone,create_uid integer,warranty_end_date date,comp_sname character varying,
             memo text,cus_order character varying,neweb_warranty_desc text,ship_type character varying,proj_step character varying,cus_project character varying,main_paytype character varying,
             proj_pay integer,neweb_manpower_desc text,sale_no character varying,eng_assign character varying,acceptance_date date,ship_description text,
             self_receive_date character varying,acc_close_day character varying,purchase_yn boolean,complete_days character varying,main_start_date date,
             post_envelop character varying,total_saleitem numeric,proj_complete_days character varying,setup_date date,cate_type integer,proj_pay_type character varying,
             description text,sno character varying,pay_term character varying,write_date timestamp without time zone,payto_date character varying,
             taxes_id integer,is_closed boolean,is_signed boolean,invoice_openamount numeric,invoice_mark boolean,invoice_complete boolean,
             proj_cost_case character varying,proj_main_case character varying,firstgen integer,acc_close_day1 character varying,
             discount_amount numeric,self_receive_type character varying,proj_info_memo text,proj_info_desc text,warrantyyn boolean,projectyn boolean,
             maintenanceyn boolean,opentrender boolean,proj_import_status boolean,main_service_rule_new integer,routine_maintenance_new integer,
             call_service_response integer,proj_pay1 integer,company_id integer,revenue_ratio numeric,chi_export_outcome boolean,
             chi_invoice_complete boolean,chi_export_income boolean,chi_export_project boolean,chi_export_product boolean,open_account_day character varying,
             stamp_duty_type character varying,have_contract character varying,stampduty_apply boolean,proj_write_num integer,proj_status character varying) ;
            select max(id)+1 into maxseq from neweb_project ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_project_id_seq restart with ' || maxseq  ;
            alter table neweb_project enable trigger all ;


            /* migration neweb_projgencode  */
           
          
            alter table neweb_projgencode disable trigger all ;
            insert into neweb_projgencode (id,create_uid,name,write_uid,create_date,write_date,prefixcode,gencode)
            select id,create_uid,name,write_uid,create_date,write_date,prefixcode,gencode from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,name,write_uid,create_date,write_date,prefixcode,gencode from neweb_projgencode')
             as fields (id integer,create_uid integer,name character varying,write_uid integer,create_date timestamp without time zone,
                        write_date timestamp without time zone,prefixcode character varying,gencode integer) ;
            select max(id)+1 into maxseq from neweb_projgencode ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projgencode_id_seq restart with ' || maxseq  ;
            alter table neweb_projgencode enable trigger all ;

            /* migration neweb_transationtype  */
            
            alter table neweb_transationtype disable trigger all ;
            insert into neweb_transationtype (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_transationtype')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_transationtype ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_transationtype_id_seq restart with ' || maxseq  ;
            alter table neweb_transationtype enable trigger all ;

             /* migration neweb_prodbrand  */
            
            alter table neweb_prodbrand disable trigger all ;
            insert into neweb_prodbrand(id,create_uid,create_date,name,write_uid,write_date,sequence,active)
            select id,create_uid,create_date,name,write_uid,write_date,sequence,active from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence,active from neweb_prodbrand')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,
                   name character varying,write_uid integer,write_date timestamp without time zone,
                   sequence integer,active boolean) ;
            select max(id)+1 into maxseq from neweb_prodbrand  ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_prodbrand_id_seq restart with ' || maxseq  ;
            alter table neweb_prodbrand  enable trigger all ;

            /* migration neweb_projbranch  */
            
            alter table neweb_projbranch disable trigger all ;
            insert into neweb_projbranch(id,create_uid,create_date,name,write_uid,write_date,prefixcode)
            select id,create_uid,create_date,name,write_uid,write_date,prefixcode from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,prefixcode from neweb_projbranch')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,
                     write_date timestamp without time zone,prefixcode character varying) ;
            select max(id)+1 into maxseq from neweb_projbranch;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projbranch_id_seq restart with ' || maxseq  ;
            alter table neweb_projbranch enable trigger all ;

            /* migration neweb_costtype  */

            /* alter table neweb_costtype disable trigger all ;
            insert into neweb_costtype(id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence)
            select id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,name,write_uid,write_date,create_date,costtype_sequence,sequence from neweb_costtype')
             as fields (id integer,create_uid integer,name character varying,write_uid integer,write_date timestamp without time zone,
                        create_date timestamp without time zone,costtype_sequence integer,sequence integer) ;
            select max(id)+1 into maxseq from neweb_costtype;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_costtype_id_seq restart with ' || maxseq  ;
            alter table neweb_costtype enable trigger all ; */

           
            /* migration neweb_warranty_service_rule  */
            
            alter table neweb_warranty_service_rule disable trigger all ;
            insert into neweb_warranty_service_rule(id,create_uid,create_date,name,write_uid,write_date,active,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,active,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,active,sequence from neweb_warranty_service_rule')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,
                        write_uid integer,write_date timestamp without time zone,active boolean,sequence integer) ;
            select max(id)+1 into maxseq from neweb_warranty_service_rule ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_warranty_service_rule_id_seq restart with ' || maxseq  ;
            alter table neweb_warranty_service_rule enable trigger all ;

            /* migration neweb_main_service_rule  */
            
            alter table neweb_main_service_rule disable trigger all ;
            insert into neweb_main_service_rule(id,create_uid,create_date,name,write_uid,write_date,active,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,active,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,active,sequence from neweb_main_service_rule')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,
                    write_uid integer,write_date timestamp without time zone,active boolean,sequence integer) ;
            select max(id)+1 into maxseq from neweb_main_service_rule ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_main_service_rule_id_seq restart with ' || maxseq  ;
            alter table neweb_main_service_rule enable trigger all ;

            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists migproj1() cascade""")
        self._cr.execute("""create or replace function migproj1() returns void as $BODY$
         DECLARE
           maxseq int ;
         BEGIN
           /* create extension dblink; */
            perform dblink_connect('NEWEB','dbname=NEWEB host=localhost port=5432 user=odoo password=odoo');
            
             
            
             /* migration res_users  */
           /* delete from res_users where id > 5; */
            alter table res_users disable trigger all ;
            insert into res_users(id,active,login,password,company_id,partner_id,create_date,signature,action_id,share,
                create_uid,write_uid,write_date,alias_id,sale_team_id,google_calendar_rtoken,google_calendar_token,
                google_calendar_token_validity,google_calendar_last_sync_date,google_calendar_cal_id,notification_type,odoobot_state)
            select id,active,login,password,company_id,partner_id,create_date,signature,action_id,share,
                create_uid,write_uid,write_date,alias_id,sale_team_id,google_calendar_rtoken,google_calendar_token,
                google_calendar_token_validity,google_calendar_last_sync_date,google_calendar_cal_id,'email','not_initialized' from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,active,login,password,company_id,partner_id,create_date,signature,action_id,share,
                create_uid,write_uid,write_date,alias_id,sale_team_id,google_calendar_rtoken,google_calendar_token,
                google_calendar_token_validity,google_calendar_last_sync_date,google_calendar_cal_id from res_users where id > 5')
             as fields (id integer,active boolean,login character varying,password character varying,company_id integer,
                partner_id integer,create_date timestamp without time zone,signature text,action_id integer,share boolean,
                create_uid integer,write_uid integer,write_date timestamp without time zone,alias_id integer,sale_team_id integer,google_calendar_rtoken character varying,google_calendar_token character varying,
                google_calendar_token_validity timestamp without time zone,google_calendar_last_sync_date timestamp without time zone,google_calendar_cal_id character varying) ;
            select max(id)+1 into maxseq from res_users;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence res_users_id_seq restart with ' || maxseq  ;
            alter table res_users enable trigger all ; 
            
            /* migration res_partner_title */
            
            alter table res_partner_title disable trigger all ;
             insert into res_partner_title (id,create_uid,create_date,name,shortcut,write_uid,write_date)
            select id,create_uid,create_date,name,shortcut,write_uid,write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,shortcut,write_uid,write_date from res_partner_title')
             as fields (id integer,create_uid integer,create_date timestamp,name character varying,shortcut character varying,write_uid integer,write_date timestamp) ;
            select max(id)+1 into maxseq from res_partner_title ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence res_partner_title_id_seq restart with ' || maxseq  ;
            alter table res_partner_title enable trigger all ;          
            
             /* migration res_partner  */
            
            alter table res_partner disable trigger all ;
            insert into res_partner (id,name,company_id,create_date,display_name,date,title,parent_id,ref,
                lang,tz,user_id,vat,website,comment,credit_limit,active,employee,function,type,street,
                street2,zip,city,country_id,
                email,phone,mobile,is_company,color,partner_share,commercial_partner_id ,
                commercial_company_name,company_name,create_uid,write_uid,write_date,message_bounce ,signup_token,
                signup_type,signup_expiration,debit_limit,last_time_entries_checked,
                invoice_warn,invoice_warn_msg,team_id,
                purchase_warn,purchase_warn_msg,sale_warn,sale_warn_msg,calendar_last_notif_ack,
                picking_warn,picking_warn_msg,sno,comp_sname,comp_ename,cate_type,
                group_name,proj_pay_type,proj_pay,acc_close_day,pay_term,payto_date,
                other_date,acc_receivable,post_date,post_term,post_envelop,tt_date,
                self_receive_date,self_rece_stamp,description,memo,contact_type,cus_payment,self_receive_type,
                survey_mark,credit_rulelist,birthday_month,birthday_day,
                payment_days,comp_create_date,paidup_capital,payment,checkout_date,pay_date,
                related_user_id,customer_category_id)
            select id,name,company_id,create_date,display_name,date,title,parent_id,ref,
                lang,tz,user_id,vat,website,comment,credit_limit,active,employee,function,type,street,
                street2,zip,city,country_id,
                email,phone,mobile,is_company,color,partner_share,commercial_partner_id ,
                commercial_company_name,company_name,create_uid,write_uid,write_date,message_bounce ,signup_token,
                signup_type,signup_expiration,debit_limit,last_time_entries_checked,
                invoice_warn,invoice_warn_msg,team_id,
                purchase_warn,purchase_warn_msg,sale_warn,sale_warn_msg,calendar_last_notif_ack,
                picking_warn,picking_warn_msg,sno,comp_sname,comp_ename,cate_type,
                group_name,proj_pay_type,proj_pay,acc_close_day,pay_term,payto_date,
                other_date,acc_receivable,post_date,post_term,post_envelop,tt_date,
                self_receive_date,self_rece_stamp,description,memo,contact_type,cus_payment,self_receive_type,
                survey_mark,credit_rulelist,birthday_month,birthday_day,
                payment_days,comp_create_date,paidup_capital,payment,checkout_date,pay_date,
                related_user_id,customer_category_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,company_id,create_date,display_name,date,title,parent_id,ref,
                lang,tz,user_id,vat,website,comment,credit_limit,active,employee,function,type,street,
                street2,zip,city,country_id,
                email,phone,mobile,is_company,color,partner_share,commercial_partner_id ,
                commercial_company_name,company_name,create_uid,write_uid,write_date,message_bounce ,signup_token,
                signup_type,signup_expiration,debit_limit,last_time_entries_checked,
                invoice_warn,invoice_warn_msg,team_id,
                purchase_warn,purchase_warn_msg,sale_warn,sale_warn_msg,calendar_last_notif_ack,
                picking_warn,picking_warn_msg,sno,comp_sname,comp_ename,cate_type,
                group_name,proj_pay_type,proj_pay,acc_close_day,pay_term,payto_date,
                other_date,acc_receivable,post_date,post_term,post_envelop,tt_date,
                self_receive_date,self_rece_stamp,description,memo,contact_type,cus_payment,self_receive_type,
                survey_mark,credit_rulelist,birthday_month,birthday_day,
                payment_days,comp_create_date,paidup_capital,payment,checkout_date,pay_date,
                related_user_id,customer_category_id from res_partner where id > 6')
             as fields (id integer,name character varying,company_id integer,create_date timestamp without time zone,
                display_name character varying,date date,title integer,parent_id integer,ref character varying,
                lang character varying,tz character varying,user_id integer,vat character varying,
                website character varying,comment text,credit_limit double precision,active boolean,
                employee boolean,function character varying,type character varying,street character varying,
                street2 character varying,zip character varying,city character varying,country_id integer,
                email character varying,phone character varying,mobile character varying,is_company boolean,   color integer,partner_share boolean,commercial_partner_id integer,commercial_company_name character varying,company_name character varying,create_uid integer,write_uid integer,write_date timestamp without time zone,message_bounce integer,signup_token character varying,
                signup_type character varying,signup_expiration timestamp without time zone,
                debit_limit numeric,last_time_entries_checked timestamp without time zone,
                invoice_warn character varying,invoice_warn_msg text,team_id integer,
                purchase_warn character varying,purchase_warn_msg text,sale_warn character varying,
                sale_warn_msg text,calendar_last_notif_ack timestamp without time zone,
                picking_warn character varying,picking_warn_msg text,sno character varying,
                comp_sname character varying,comp_ename character varying,cate_type integer,
                group_name character varying,proj_pay_type character varying,proj_pay character varying,
                acc_close_day character varying,pay_term character varying,payto_date character varying,
                other_date character varying,acc_receivable character varying,post_date character varying,
                post_term character varying,post_envelop character varying,tt_date character varying,
                self_receive_date character varying,self_rece_stamp character varying,description text,
                memo text,contact_type integer,cus_payment integer,self_receive_type character varying,
                survey_mark boolean,credit_rulelist text,birthday_month integer,birthday_day integer,
                payment_days integer,comp_create_date date,paidup_capital numeric,
                payment character varying,checkout_date integer,pay_date integer,
                related_user_id integer,customer_category_id integer) ;
            select max(id)+1 into maxseq from res_partner ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence res_partner_id_seq restart with ' || maxseq  ;
            alter table res_partner enable trigger all ; 
            
             /* migration hr_department */
           
           alter table hr_department disable trigger all ;
            insert into hr_department(id,name,active,company_id,parent_id,manager_id,note,color,create_uid,create_date,write_uid,write_date)
            select id,name,active,company_id,parent_id,manager_id,note,color,create_uid,create_date,write_uid,write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,company_id,parent_id,manager_id,note,color,create_uid,create_date,write_uid,write_date from hr_department')
             as fields (id integer,name character varying,active boolean,company_id integer,parent_id integer,manager_id integer,note text,
                color integer,create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
            select max(id)+1 into maxseq from hr_department ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence hr_department_id_seq restart with ' || maxseq  ;
            alter table hr_department enable trigger all ; 

              /* migration hr_job */
            
            alter table hr_job disable trigger all ;
            insert into hr_job(id,name,expected_employees,no_of_employee,no_of_recruitment,no_of_hired_employee,description,requirements,department_id,company_id,state,create_uid,create_date,write_uid,write_date)
            select id,name,expected_employees,no_of_employee,no_of_recruitment,no_of_hired_employee,description,requirements,department_id,company_id,state,create_uid,create_date,write_uid,write_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,expected_employees,no_of_employee,no_of_recruitment,no_of_hired_employee,description,requirements,department_id,company_id,state,create_uid,create_date,write_uid,write_date from hr_job')
             as fields (id integer,name character varying,expected_employees integer,no_of_employee integer,no_of_recruitment integer,
                no_of_hired_employee integer,description text,requirements text,department_id integer,company_id integer,
                state character varying,create_uid integer,create_date timestamp without time zone,write_uid integer,
                write_date timestamp without time zone) ;
            select max(id)+1 into maxseq from hr_job ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence hr_job_id_seq restart with ' || maxseq  ;
            alter table hr_job enable trigger all ; 

          

              /* migration resource_resource */
            
          alter table resource_resource disable trigger all ;
            insert into resource_resource(id,name,active,company_id,resource_type,user_id,time_efficiency,calendar_id,create_uid,create_date,write_uid,write_date,tz)
            select id,name,active,company_id,resource_type,user_id,time_efficiency,1,create_uid,create_date,write_uid,write_date,2 from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,company_id,resource_type,user_id,time_efficiency,
            1,create_uid,create_date,write_uid,write_date,2 from resource_resource where id > 1')
             as fields (id integer,name character varying,active boolean,company_id integer,resource_type character varying,user_id integer,
            time_efficiency double precision,calendar_id integer,create_uid integer,create_date timestamp without time zone,write_uid integer,
              write_date timestamp without time zone,tz character varying) ;
            select max(id)+1 into maxseq from resource_resource ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence resource_resource_id_seq restart with ' || maxseq  ;
            alter table resource_resource enable trigger all ;
            update resource_resource set tz='Asia/Taipei' ; 

            
               /* migration hr_employee */
           
            alter table hr_employee disable trigger all ;
            insert into hr_employee(id,name,address_home_id,country_id,gender,marital,birthday,ssnid,sinid,identification_id,
                passport_id,bank_account_id,notes,color,department_id,job_id,address_id,work_phone,mobile_phone,work_email,
                work_location,resource_id,parent_id,coach_id,create_uid,create_date,write_uid,write_date,
                residnet_ship,educational_level,employee_num,timesheet_expense,timesheet_cost,active)
            select id,name,address_home_id,country_id,gender,marital,birthday,ssnid,sinid,identification_id,
                passport_id,bank_account_id,notes,color,department_id,job_id,address_id,work_phone,mobile_phone,work_email,
                work_location,resource_id,parent_id,coach_id,create_uid,create_date,write_uid,write_date,
                residnet_ship,educational_level,employee_num,timesheet_expense,timesheet_cost,True from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name_related as name,address_home_id,country_id,gender,marital,birthday,ssnid,sinid,identification_id,
                passport_id,bank_account_id,notes,color,department_id,job_id,address_id,work_phone,mobile_phone,work_email,
                work_location,resource_id,parent_id,coach_id,create_uid,create_date,write_uid,write_date,
                residnet_ship,educational_level,employee_num,timesheet_expense,timesheet_cost from hr_employee where id > 1')
             as fields (id integer,name character varying,address_home_id integer,country_id integer,gender character varying,marital character varying,
                birthday date,ssnid character varying,sinid character varying,identification_id character varying,
                passport_id character varying,bank_account_id integer,notes text,color integer,department_id integer,job_id integer,
                address_id integer,work_phone character varying,mobile_phone character varying,work_email character varying,
                work_location character varying,resource_id integer,parent_id integer,coach_id integer,create_uid integer,
                create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone,
                residnet_ship character varying,educational_level character varying,employee_num character varying,
                timesheet_expense numeric,timesheet_cost numeric) ;
            select max(id)+1 into maxseq from hr_employee ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence hr_employee_id_seq restart with ' || maxseq  ;
            alter table hr_employee enable trigger all ; 
            
            /* migration account_tax */
             
           alter table account_tax disable trigger all;
            insert into account_tax(id,name,type_tax_use,amount_type,active,company_id,sequence,amount,description,
                price_include,include_base_amount,analytic,tax_group_id,create_uid,create_date,write_uid,write_date)
             select id,name,type_tax_use,amount_type,active,company_id,sequence,amount,description,
                price_include,include_base_amount,analytic,tax_group_id,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,type_tax_use,amount_type,active,company_id,sequence,amount,description,
                price_include,include_base_amount,analytic,tax_group_id,create_uid,create_date,write_uid,write_date from account_tax ')
              as fields (id integer,name character varying,type_tax_use character varying,amount_type character varying,
                active boolean,company_id integer,sequence integer,amount numeric,description character varying,
                price_include boolean,include_base_amount boolean,analytic boolean,tax_group_id integer,
                create_uid integer,create_date timestamp without time zone,write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from account_tax ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence account_tax_id_seq restart with ' || maxseq  ; 
             alter table account_tax enable trigger all ; 
             
             /* migration account_payment_term */
              
             alter table account_payment_term disable trigger all;
            insert into account_payment_term(id,name,active,note,company_id,sequence,create_uid,create_date,write_uid,write_date)
             select id,name,active,note,company_id,10,create_uid,create_date,write_uid,write_date from
             dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,name,active,note,company_id,10,create_uid,create_date,write_uid,write_date from account_payment_term')
              as fields (id integer,name character varying,active boolean,note text,company_id integer,
                sequence integer,create_uid integer,create_date timestamp without time zone,
                write_uid integer,write_date timestamp without time zone) ;
             select max(id)+1 into maxseq from account_payment_term ;
             if maxseq is null then
                maxseq = 1 ;
             end if ;
             execute 'alter sequence account_payment_term_id_seq restart with ' || maxseq  ; 
             alter table account_payment_term enable trigger all ;
            
            /* migration neweb_setup_desc_item  */
           
           alter table neweb_setup_desc_item disable trigger all ;
            insert into neweb_setup_desc_item (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_setup_desc_item')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_setup_desc_item ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_setup_desc_item_id_seq restart with ' || maxseq  ;
            alter table neweb_setup_desc_item enable trigger all ; 

            /* migration neweb_setup_prod */
            
            alter table neweb_setup_prod disable trigger all;
            insert into neweb_setup_prod (id,create_uid,prod_num,prod_desc,prod_memo,prod_modeltype,write_uid,prod_no,setup_id,prod_set,write_date,software_ver,create_date,prod_serial)
            select id,create_uid,prod_num,prod_desc,prod_memo,prod_modeltype,write_uid,prod_no,setup_id,prod_set,write_date,software_ver,create_date,prod_serial from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,prod_num,prod_desc,prod_memo,prod_modeltype,write_uid,prod_no,setup_id,prod_set,write_date,software_ver,create_date,prod_serial from neweb_setup_prod')
             as fields (id integer,create_uid integer,prod_num float,prod_desc character varying,prod_memo character varying,prod_modeltype character varying,write_uid integer,prod_no character varying,setup_id integer,prod_set integer,write_date timestamp without time zone,
             software_ver character varying,create_date timestamp without time zone,prod_serial character varying) ;
            select max(id)+1 into maxseq from neweb_setup_prod ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_setup_prod_id_seq restart with ' || maxseq  ;
            alter table neweb_setup_prod enable trigger all ;

            /* migration neweb_ass_service_mode */
            
            
            alter table neweb_ass_service_mode disable trigger all;
            insert into neweb_ass_service_mode (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_ass_service_mode')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_ass_service_mode ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_ass_service_mode_id_seq restart with ' || maxseq  ;
            alter table neweb_ass_service_mode enable trigger all ;



             /* migration neweb_ass_service_type */
            
            alter table neweb_ass_service_type disable trigger all;
            insert into neweb_ass_service_type (id,create_uid,create_date,name,write_uid,write_date,sequence,service_manager)
            select id,create_uid,create_date,name,write_uid,write_date,sequence,service_manager from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence,service_manager from neweb_ass_service_type')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer,service_manager integer) ;
            select max(id)+1 into maxseq from neweb_ass_service_type ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_ass_service_type_id_seq restart with ' || maxseq  ;
            alter table neweb_ass_service_type enable trigger all ;

            alter table neweb_proj_eng_assign disable trigger all ;
            insert into neweb_proj_eng_assign (id,assign_man_day,create_date,proj_manager,assign_no,write_uid,assign_man_hour,setup_contact,setup_contact_phone,create_uid,state,
            eng_man_desc,setup_other_desc,proj_no,service_name,require_date,setup_date,proj_cus_name,setup_contact_mobile,assign_man_desc,setup_address,write_date,setup_other_attach,proj_sale,assign_man_num,
            task_desc,name,is_closed,is_signed,service_type,borrow_need,completed_date,assign_man_date,assign_man_subject,is_attach1,is_attach2,is_attach3,assign_mans)
            select id,assign_man_day,create_date,proj_manager,assign_no,write_uid,assign_man_hour,setup_contact,"setup_contact_phone",create_uid,state,
            "eng_man_desc","setup_other_desc",proj_no,service_name,require_date,setup_date,proj_cus_name,"setup_contact_mobile","assign_man_desc","setup_address",write_date,setup_other_attach,proj_sale,assign_man_num,
            task_desc,name,is_closed,is_signed,service_type,borrow_need,completed_date,assign_man_date,coalesce(assign_man_subject,' '),is_attach1,is_attach2,is_attach3,"assign_mans" from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,assign_man_day,create_date,proj_manager,assign_no,write_uid,assign_man_hour,setup_contact,"setup_contact_phone",create_uid,state,"eng_man_desc","setup_other_desc",proj_no,service_name,require_date,setup_date,proj_cus_name,"setup_contact_mobile","assign_man_desc","setup_address",write_date,setup_other_attach,proj_sale,assign_man_num,task_desc,name,is_closed,is_signed,service_type,borrow_need,completed_date,assign_man_date,assign_man_subject,is_attach1,is_attach2,is_attach3,"assign_mans" from neweb_proj_eng_assign')
             as fields (id integer,assign_man_day float,create_date timestamp without time zone,proj_manager character varying,assign_no character varying,write_uid integer,assign_man_hour numeric,setup_contact integer,
             setup_contact_phone character varying,create_uid integer,state character varying,eng_man_desc text,setup_other_desc text,proj_no integer,service_name integer,require_date date,setup_date date,proj_cus_name integer,setup_contact_mobile character varying,assign_man_desc text,setup_address character varying,write_date timestamp without time zone,
            setup_other_attach text,proj_sale integer,assign_man_num numeric,task_desc text,name character varying,is_closed boolean,is_signed boolean,service_type integer,borrow_need character varying,
            completed_date date,assign_man_date date,assign_man_subject character varying,is_attach1 boolean,is_attach2 boolean,is_attach3 boolean,assign_mans character varying) ;
            select max(id)+1 into maxseq from neweb_proj_eng_assign ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_proj_eng_assign_id_seq restart with ' || maxseq  ;
            alter table neweb_proj_eng_assign enable trigger all ;

            /*  migration neweb_ass_service_type_neweb_proj_eng_assign_rel */
            
            delete from neweb_ass_service_type_neweb_proj_eng_assign_rel ;
            alter table neweb_ass_service_type_neweb_proj_eng_assign_rel disable trigger all;
            insert into neweb_ass_service_type_neweb_proj_eng_assign_rel (neweb_proj_eng_assign_id,neweb_ass_service_type_id)
            select neweb_proj_eng_assign_id,neweb_ass_service_type_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_proj_eng_assign_id,neweb_ass_service_type_id from neweb_ass_service_type_neweb_proj_eng_assign_rel')
             as fields (neweb_proj_eng_assign_id integer,neweb_ass_service_type_id integer) ;
            alter table neweb_ass_service_type_neweb_proj_eng_assign_rel enable trigger all ;

            /* migration neweb_assign_complete */
            
            alter table neweb_assign_complete disable trigger all;
            insert into neweb_assign_complete (id,man_hour,create_uid,complete_id,man_memo,write_uid,man_day,write_date,create_date,man_id,work_type,assign_start_datetime,assign_end_datetime,emp_id)
            select id,man_hour,create_uid,complete_id,man_memo,write_uid,man_day,write_date,create_date,man_id,work_type,assign_start_datetime,assign_end_datetime,emp_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,man_hour,create_uid,complete_id,man_memo,write_uid,man_day,write_date,create_date,man_id,work_type,assign_start_datetime,assign_end_datetime,emp_id from neweb_assign_complete')
             as fields (id integer,man_hour numeric,create_uid integer,complete_id integer,man_memo text,write_uid integer,man_day numeric,write_date timestamp without time zone,create_date timestamp without time zone,man_id integer,work_type integer,assign_start_datetime timestamp without time zone,assign_end_datetime timestamp without time zone,emp_id integer) ;
            select max(id)+1 into maxseq from neweb_assign_complete ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_assign_complete_id_seq restart with ' || maxseq  ;
            alter table neweb_assign_complete enable trigger all ;

            /* migration neweb_base_maintenance_category */
           
            
            alter table neweb_base_maintenance_category disable trigger all;
            insert into neweb_base_maintenance_category (id,create_uid,name,memo,disabled,write_date,create_date,write_uid,product_attr)
            select id,create_uid,name,memo,disabled,write_date,create_date,write_uid,product_attr from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,name,memo,disabled,write_date,create_date,write_uid,product_attr from neweb_base_maintenance_category')
             as fields (id integer,create_uid integer,name character varying,memo text,disabled boolean,write_date timestamp without time zone,create_date timestamp without time zone,write_uid integer,product_attr character varying) ;
            select max(id)+1 into maxseq from neweb_base_maintenance_category ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_base_maintenance_category_id_seq restart with ' || maxseq  ;
            alter table neweb_base_maintenance_category enable trigger all ;

            /* migration neweb_base_problem */
            
            alter table neweb_base_problem disable trigger all;
            insert into neweb_base_problem (id,problem_category,create_uid,description,write_uid,memo,name,disabled,err_log,event_log,write_date,create_date,err_code,maintenance_category_id)
            select id,problem_category,create_uid,description,write_uid,memo,name,disabled,err_log,event_log,write_date,create_date,err_code,maintenance_category_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,problem_category,create_uid,description,write_uid,memo,name,disabled,err_log,event_log,write_date,create_date,err_code,maintenance_category_id from neweb_base_problem')
             as fields (id integer,problem_category character varying,create_uid integer,description text,write_uid integer,memo text,name character varying,disabled boolean,err_log character varying,event_log character varying,write_date timestamp without time zone,create_date timestamp without time zone,err_code character varying,maintenance_category_id integer) ;
            select max(id)+1 into maxseq from neweb_base_problem ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_base_problem_id_seq restart with ' || maxseq  ;
            alter table neweb_base_problem enable trigger all ;

            /* migration neweb_base_sla */
            
            alter table neweb_base_sla disable trigger all;
            insert into neweb_base_sla (id,create_uid,name,maintenance_time,write_uid,disabled,create_date,write_date,onsite_time,response_time,backup_equipment)
            select id,create_uid,name,maintenance_time,write_uid,disabled,create_date,write_date,onsite_time,response_time,backup_equipment from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,name,maintenance_time,write_uid,disabled,create_date,write_date,onsite_time,response_time,backup_equipment from neweb_base_sla')
             as fields (id int,create_uid int,name character varying,maintenance_time numeric,write_uid int,disabled boolean,create_date timestamp without time zone,write_date timestamp without time zone,onsite_time numeric,response_time numeric,backup_equipment boolean) ;
            select max(id)+1 into maxseq from neweb_base_sla ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_base_sla_id_seq restart with ' || maxseq  ;
            alter table neweb_base_sla enable trigger all ;

            /* migration neweb_base_value_added_service */
            
            alter table neweb_base_value_added_service disable trigger all;
            insert into neweb_base_value_added_service (id,disabled,name,create_uid,write_uid,content,write_date,create_date)
            select id,disabled,name,create_uid,write_uid,content,write_date,create_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,disabled,name,create_uid,write_uid,content,write_date,create_date from neweb_base_value_added_service')
             as fields (id integer,disabled boolean,name character varying,create_uid integer,write_uid integer,content text,write_date timestamp without time zone,create_date timestamp without time zone) ;
            select max(id)+1 into maxseq from neweb_base_value_added_service ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_base_value_added_service_id_seq restart with ' || maxseq  ;
            alter table neweb_base_value_added_service enable trigger all ;

            /* migration neweb_base_value_added_service_neweb_contract_contract_rel */
            
            delete from neweb_base_value_added_service_neweb_contract_contract_rel ;
            alter table neweb_base_value_added_service_neweb_contract_contract_rel disable trigger all;
            insert into neweb_base_value_added_service_neweb_contract_contract_rel (neweb_contract_contract_id,neweb_base_value_added_service_id)
            select neweb_contract_contract_id,neweb_base_value_added_service_id from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select neweb_contract_contract_id,neweb_base_value_added_service_id from neweb_base_value_added_service_neweb_contract_contract_rel')
             as fields (neweb_contract_contract_id integer,neweb_base_value_added_service_id integer) ;
            alter table neweb_base_value_added_service_neweb_contract_contract_rel enable trigger all ;
            
              /* migration neweb_contacttype  */
            
            alter table neweb_contacttype disable trigger all ;
            insert into neweb_contacttype (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_contacttype')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_contacttype ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_contacttype_id_seq restart with ' || maxseq  ;
            alter table neweb_contacttype enable trigger all ;

            /* migration neweb_buscate */
            
            alter table neweb_buscate disable trigger all;
            insert into neweb_buscate (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_buscate')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
             select max(id)+1 into maxseq from neweb_buscate ;
             if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_buscate_id_seq restart with ' || maxseq  ;
            alter table neweb_buscate enable trigger all ;

            /* migration neweb_call_service_response */
            
            alter table neweb_call_service_response disable trigger all;
            insert into neweb_call_service_response (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_call_service_response')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
             select max(id)+1 into maxseq from neweb_call_service_response ;
             if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_call_service_response_id_seq restart with ' || maxseq  ;
            alter table neweb_call_service_response enable trigger all ;

             /* migration neweb_export_excel_download */
            
            alter table neweb_export_excel_download disable trigger all;
            insert into neweb_export_excel_download (id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date)
            select id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date from neweb_export_excel_download')
             as fields (id integer,create_uid integer,xls_file bytea,xls_file_name character varying,write_uid integer,xls_file_memo text,write_date timestamp without time zone,create_date timestamp without time zone) ;
             select max(id)+1 into maxseq from neweb_export_excel_download ;
             if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_export_excel_download_id_seq restart with ' || maxseq  ;
            alter table neweb_export_excel_download enable trigger all ;

             /* migration neweb_import_excel_download */
            
            alter table neweb_import_excel_download disable trigger all;
            insert into neweb_import_excel_download (id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date)
            select id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,xls_file,xls_file_name,write_uid,xls_file_memo,write_date,create_date from neweb_import_excel_download')
             as fields (id integer,create_uid integer,xls_file bytea,xls_file_name character varying,write_uid integer,xls_file_memo text,write_date timestamp without time zone,create_date timestamp without time zone) ;
            select max(id)+1 into maxseq from neweb_import_excel_download ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_import_excel_download_id_seq restart with ' || maxseq  ;
            alter table neweb_import_excel_download enable trigger all ;

             /* migration neweb_projcustom */
            
            alter table neweb_projcustom disable trigger all;
            insert into neweb_projcustom (id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select)
            select id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,cus_type,cus_fax,cus_id,cus_address,cus_memo,write_uid,create_date,cus_phone,write_date,cus_select from neweb_projcustom')
             as fields (id integer,create_uid integer,cus_type character varying,cus_fax character varying,cus_id integer,cus_address character varying,cus_memo text,write_uid integer,create_date timestamp without time zone,
             cus_phone character varying,write_date timestamp without time zone,cus_select integer) ;
            select max(id)+1 into maxseq from neweb_projcustom ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projcustom_id_seq restart with ' || maxseq  ;
            alter table neweb_projcustom enable trigger all ;

             /* migration neweb_projcontact */
            
            alter table neweb_projcontact disable trigger all;
            insert into neweb_projcontact (id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone)
            select id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,contact_type,contact_fax,contact_id,contact_function,contact_email,write_date,contact_mobile,create_date,contact_name,write_uid,contact_phone from neweb_projcontact')
             as fields (id integer,create_uid integer,contact_type integer,contact_fax character varying,contact_id integer,contact_function character varying,contact_email character varying,write_date timestamp without time zone,contact_mobile character varying,
             create_date timestamp without time zone,contact_name integer,write_uid integer,contact_phone character varying) ;
            select max(id)+1 into maxseq from neweb_projcontact ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projcontact_id_seq restart with ' || maxseq  ;
            alter table neweb_projcontact enable trigger all ;

             /* migration neweb_prodset */
           
            alter table neweb_prodset disable trigger all;
            insert into neweb_prodset (id,create_uid,create_date,name,write_uid,write_date,name1,sname,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,name1,sname,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,name1,sname,sequence from neweb_prodset')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,name1 character varying,sname character varying,sequence integer) ;
            select max(id)+1 into maxseq from neweb_prodset ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_prodset_id_seq restart with ' || maxseq  ;
            alter table neweb_prodset enable trigger all ;

             /* migration neweb_projmaintype */
            
            alter table neweb_projmaintype disable trigger all;
            insert into neweb_projmaintype (id,create_uid,create_date,name,write_uid,write_date,sequence)
            select id,create_uid,create_date,name,write_uid,write_date,sequence from
            dblink('hostaddr=127.0.0.1 port=5432 dbname=NEWEB user=postgres password=odoo','select id,create_uid,create_date,name,write_uid,write_date,sequence from neweb_projmaintype')
             as fields (id integer,create_uid integer,create_date timestamp without time zone,name character varying,write_uid integer,write_date timestamp without time zone,sequence integer) ;
            select max(id)+1 into maxseq from neweb_projmaintype ;
            if maxseq is null then
               maxseq = 1 ;
            end if ;
            execute 'alter sequence neweb_projmaintype_id_seq restart with ' || maxseq  ;
            alter table neweb_projmaintype enable trigger all ;


            perform dblink_disconnect('NEWEB') ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists rundeldata() cascade""")
        self._cr.execute("""create or replace function rundeldata() returns void as $BODY$
         DECLARE
          ncount int ;
         BEGIN
            /* migproj1 */         
            delete from neweb_projmaintype ;
            delete from neweb_prodset ;
            delete from neweb_projcontact ;
            delete from neweb_projcustom ;
            delete from neweb_import_excel_download ;
            delete from neweb_export_excel_download ;
            delete from neweb_call_service_response ;
            delete from neweb_buscate ;
            delete from neweb_contacttype ;
            delete from neweb_base_value_added_service_neweb_contract_contract_rel ;
            delete from neweb_base_value_added_service ;
            delete from neweb_base_sla ;
            delete from neweb_base_problem ;
            delete from stock_inventory_line;
            delete from stock_move ;
            delete from stock_quant ;
            delete from neweb_repair_repair_part ;
            delete from purchase_order_line;
            delete from neweb_base_maintenance_category ;
            delete from neweb_base_problem ;
            delete from neweb_assign_complete ;
            delete from neweb_ass_service_type_neweb_proj_eng_assign_rel ;
            delete from neweb_ass_service_type ;
            delete from neweb_proj_eng_assign;
            delete from neweb_ass_service_mode ;
            delete from neweb_setup_prod ;
            delete from neweb_setup_desc_item ;
            delete from account_payment_term ; 
            delete from account_tax ; 
            delete from neweb_repair_repair;
            delete from hr_employee where id > 1;
            delete from resource_resource where id > 1 ; 
            delete from hr_job ; 
            delete from hr_department ; 
            delete from neweb_project ; 
            delete from sale_order;
            delete from purchase_order; 
            delete from calendar_contacts ; 
            delete from account_move_line ;
            delete from mail_activity ;
            delete from res_users where id > 5 ;
            delete from res_partner where id > 6 ; 
            delete from res_partner_title ;
            
            
            /* migproj2   */
            delete from neweb_projsaleitem ; 
            delete from neweb_main_service_rule ;
            delete from neweb_warranty_service_rule ;
            delete from neweb_projanalysis ;
            delete from neweb_costtype  ;
            delete from neweb_projbranch  ;
            delete from neweb_prodbrand  ;
            delete from neweb_transationtype ;
            delete from neweb_projgencode ;
            delete from neweb_engmaintype ;
            /* migproj3  */
            
             delete from neweb_maincost_line ;
             delete from neweb_setupcost_line ;
             delete from neweb_cost_dept ;
             delete from neweb_saleorder_excel_download ;
             delete from neweb_partner_list ;
             delete from neweb_call_service_response ;
             delete from neweb_quotation_include ;
             delete from neweb_salenocheck ;
             delete from neweb_projprodset ;
             delete from neweb_sitem_list ; 
             delete from sale_order ;
             delete from neweb_routine_maintenance ;
             delete from neweb_sale_analysis_team_targetgp ; 
             delete from crm_team ; 
             /* migprojrel  */
             
             delete from hr_employee_res_partner_rel ;
             delete from hr_employee_projengassign_rel ;
             delete from hr_employee_neweb_sale_analysis_travel_report_rel ;
             delete from hr_employee_neweb_contract_contract_rel ;
             delete from neweb_engmaintype_neweb_proj_eng_assign_rel ;
             delete from neweb_project_neweb_transationtype_rel  ;
             
             /* migprod1 */
             
             delete from stock_valuation_layer ;
             delete from product_product where id > 3 ;
             delete from product_template where id > 3 ; 
             delete from ir_attachment where id > 521;
             delete from stock_picking; 
             delete from stock_warehouse where id > 1 ; 
             delete from stock_location_route where id > 5 ; 
             delete from stock_picking_type where id > 5 ; 
             delete from stock_location where id > 16 ;
             delete from product_category where id > 3 ; 
             delete from ir_sequence where id > 26 ;
             
             /* migprod2  */
             
              delete from stock_location_route where id > 5 ;
              delete from stock_location where id > 16 ;
              
              /* migprod3 */
              
              delete from stock_picking_type where id > 5 ;
             delete from stock_warehouse where id > 1 ;
             
             /* migprod4 */
             
             /* migpur */
             
             delete from purchase_order_line ;
             delete from purchase_order ;
             delete from neweb_requiregencode ;
             delete from neweb_ma_parts_type ;
             delete from neweb_ma_backup_type ;
             delete from neweb_require_purchase_item ;
             delete from neweb_require_purchase ;
             delete from neweb_purchase_costtype ;
             delete from neweb_pitem_list ;
             delete from neweb_purchase_purchase_manager ;
             
             /* migstock */
             
              delete from procurement_group ;
              delete from stock_inventory_line ;
              delete from stock_inventory ;
              delete from neweb_payment_term_rule ;
              delete from neweb_stockship_list ;
              delete from neweb_stockout_list ;
              delete from neweb_stockin_list ;
              delete from stock_move ;
              delete from stock_warehouse_orderpoint ;
              
              /* migcontract */

               delete from hr_employee_neweb_contract_contract_rel ;
               delete from neweb_contract_dr_practice ;
               delete from neweb_contract_repaire_list ;
               delete from neweb_contract_inspection_list ;
               delete from neweb_contract_contract_line ;
               delete from neweb_contract_contract ;
               
               /* migrepair */
               
               delete from neweb_repair_repeatcall_excel_download ;
               delete from neweb_repair_parts_categ ;
               delete from neweb_repair_repair_questionnaire ;
               delete from neweb_repair_repair_work_log ;
               delete from neweb_repair_repair_care_call_log ;
               delete from neweb_repair_repair_part ;
               delete from neweb_repair_repair_line ;
               delete from neweb_repair_manager_note ;
               delete from neweb_repair_repair ;
               delete from neweb_repair_question ;
               delete from neweb_repair_questionnaire ;
               delete from ir_property where id > 3361 ;
               
               /* migsecurity */
               
               delete from res_groups_users_rel where uid > 5 ;
               delete from res_company_users_rel where user_id > 5 ;
               
               /* miginvoice */
               
                delete from neweb_invoice_invoiceopen ;
               delete from neweb_invoice_invoiceopen_line ;
               delete from neweb_invoice_invopen_list ;
               delete from neweb_invoice_proj_inv_excel_download ;
               delete from neweb_invoice_projectdata ;
               delete from neweb_invoice_invoicedata ;
               delete from neweb_invoice_purinvdata ;
               
               /* migtimesheet */
               
               delete from neweb_emp_timesheet_workdate_check ;
               delete from neweb_emp_timesheet_tolerance_setting ;
               delete from neweb_emp_timesheet_todo_calendar  ;
               delete from neweb_emp_timesheet_timesheet_download ;
               delete from neweb_emp_timesheet_timesheet_adjustowner ;
               delete from neweb_emp_timesheet_timesheet_lock ;
               delete from neweb_emp_timesheet_timesheet_calendar_line ;
               delete from neweb_emp_timesheet_timesheet_calendar ;
               delete from neweb_emp_timesheet_repair_calendar ;
               delete from neweb_emp_timesheet_inspection_calendar ;
               delete from neweb_emp_timesheet_hrholiday_line ;
               delete from neweb_emp_timesheet_hrholiday ;
               delete from neweb_emp_timesheet_inspection_alert_mail ;
               delete from neweb_emp_timesheet_timesheet_worktype ;
               
               /* migchi */
               
               delete from neweb_chi_invoicing_incomeoutcome_seq ; 
               delete from neweb_chi_invoicing_export_proj_log ; 
               delete from neweb_chi_invoicing_productset_seq ; 
               delete from neweb_chi_invoicing_export_sales_log ; 
               delete from neweb_chi_invoicing_export_purchase_log ; 
               delete from neweb_chi_invoicing_export_main_proj_log ; 
               delete from neweb_chi_invoicing_package_sales ; 
               delete from neweb_chi_invoicing_package_purchase ; 
               delete from neweb_chi_invoicing_package_product ; 
               delete from neweb_chi_invoicing_package_project ; 
               delete from neweb_chi_invoicing_package_saleinv_excel_download ; 
               delete from neweb_chi_invoicing_package_purinv_excel_download ; 
               delete from neweb_chi_invoicing_package_excel_download ; 
               delete from neweb_chi_invoicing_excelset_seq ; 
               delete from neweb_chi_invoicing_invoiceopen_excel_download ; 
               delete from neweb_chi_invoicing_purinv_excel_download ; 
               delete from neweb_chi_invoicing_excel_download ;
               
               /* migsaleana */
               
               delete from neweb_sale_analysis_travel_report ;
               delete from neweb_sale_analysis_saleanalysis_excel_download ;
               delete from neweb_sale_analysis_official_doc ;
               delete from neweb_sale_analysis_op_program ;
               delete from group_member_hr_employee_rel ;
               delete from neweb_sale_analysis_group_member ;
               delete from neweb_sale_analysis_sale_revenuel ;
               delete from neweb_sale_analysis_sale_revenuem ;
               delete from neweb_sale_analysis_sale_revenueq ;
               delete from neweb_sale_analysis_teammember_utargetgp ;
               delete from neweb_sale_analysis_teammember_targetgp ;
               delete from neweb_sale_analysis_team_targetgp ;
               delete from neweb_sale_analysis_cf_sumline ;
               delete from neweb_sale_analysis_expensedoc ;
               delete from neweb_sale_analysis_expenseevent ;
               delete from neweb_sale_analysis_expenseitem ;
               delete from neweb_sale_analysis_expense_line ;
               delete from neweb_sale_analysis_expense_report ;
               
               /* migpurinv */
               
                delete from neweb_purinv_invoiceline ;
                delete from neweb_purinv_invoice ;
                
                /* migcalendar */
                
                delete from calendar_contacts ;
                delete from calendar_attendee ;
                delete from calendar_event_res_partner_rel ;
                delete from calendar_event ;
                
                delete from neweb_payment_term_rule ;
                
                
           





            
         END;$BODY$
         LANGUAGE plpgsql;""")




