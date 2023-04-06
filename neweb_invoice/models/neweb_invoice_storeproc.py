# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,tools


class invoicestoreproc(models.Model):
    _name = "neweb_invoice.invoice_storeproc"


    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS gen_invoicedata(projectid int,rev1 int,rev2 int,rev3 int,rev4 int,rev5 int, rev6 int,rev7 int,rev8 int) cascade;""")
        self._cr.execute("""create or replace function gen_invoicedata(projectid int,rev1 int,rev2 int,rev3 int,rev4 int,rev5 int,rev6 int,rev7 int,rev8 int) returns void as $BODY$
          DECLARE 
             inv_cur cursor for select * from neweb_project where id=projectid;
             inv_rec record;
             inv_line_cur cursor for select * from neweb_projsaleitem where saleitem_id=projectid order by line_item ;
             inv_line_rec record ;
             curtime TIMESTAMP ;
             mycount int;
             myid int;
             mycontractid INTEGER ;
             myconno neweb_contract_contract.contract_no%type ;
             mycon_main_start neweb_contract_contract.maintenance_start_date%type ;
             mycon_main_end neweb_contract_contract.maintenance_end_date%type ;
             mycusaddress neweb_projcustom.cus_address%type ;
             mycusphone neweb_projcustom.cus_phone%type ;
             mycontact res_partner.name%type ;
             mypartnerid int ;
             myrev1 neweb_invoice_invoiceopen.revenue_1%type;
             myrev2 neweb_invoice_invoiceopen.revenue_2%type;
             myrev3 neweb_invoice_invoiceopen.revenue_3%type;
             myrev4 neweb_invoice_invoiceopen.revenue_4%type;
             myrev5 neweb_invoice_invoiceopen.revenue_5%type;
             myrev6 neweb_invoice_invoiceopen.revenue_6%type;
             myrev7 neweb_invoice_invoiceopen.revenue_7%type;
             myrev8 neweb_invoice_invoiceopen.revenue_8%type;
             myamount float;
             myuntaxamount float;
             mytaxamount float ;
             myincludetaxamount Boolean;
             myinvoicetype CHAR;
             pitemid INTEGER ;
             purchaseno VARCHAR ;
             myprojrevenuetaxtot FLOAT ;
             myprojectrevenuetot FLOAT ;
             mytotsaleitemamount FLOAT;
             mycusname INT;
             mymaincusname INT;
             mymaxid int ;
             mysaleno varchar ;
          BEGIN 
             myprojrevenuetaxtot := 0 ;
             mytotsaleitemamount := 0 ;
             select sale_no into mysaleno from neweb_project where id=projectid ;
             select coalesce(total_saleitem_amount,0) into mytotsaleitemamount from neweb_project where id=projectid ;
             select discount_amount into mytotsaleitemamount from sale_order where name like mysaleno ;
             open inv_cur;
             curtime := now();
             loop
                fetch inv_cur into inv_rec;
                exit when not found;
                select count(*) into mycount from neweb_invoice_invoiceopen where project_no=inv_rec.id;
                if mycount=0 then 
                   select cus_name,main_cus_name into mycusname,mymaincusname from neweb_project where id = projectid ;
                   insert into neweb_invoice_invoiceopen(application_date,project_no,project_name,invoice_title,sno,payment_type,project_amount_total,create_date,create_uid,name,invoice_ver,cus_order) values
                    (curtime,inv_rec.id,inv_rec.comp_cname,inv_rec.comp_cname,inv_rec.sno,inv_rec.proj_pay_type,mytotsaleitemamount,curtime,'1','New',0,inv_rec.cus_order) ; 
                   select max(id) into mymaxid from neweb_invoice_invoiceopen ; 
                   if mycusname is not null then
                      update neweb_invoice_invoiceopen set cus_name=mycusname where id=mymaxid ;
                   end if ; 
                   if mymaincusname is not null then 
                      update neweb_invoice_invoiceopen set main_cus_name=mymaincusname where id=mymaxid ;
                   end if ; 
                end if;
                select id into myid from neweb_invoice_invoiceopen where project_no=inv_rec.id;
                select id,contract_no,maintenance_start_date,maintenance_end_date into mycontractid,myconno,mycon_main_start,mycon_main_end from neweb_contract_contract where project_no=inv_rec.name;
                select cus_address,cus_phone into mycusaddress,mycusphone from neweb_projcustom where cus_id=inv_rec.id and id = (select min(id) from neweb_projcustom where cus_id=inv_rec.id);
                select contact_name into mypartnerid from neweb_projcontact where contact_id=inv_rec.id and id = (select min(id) from neweb_projcontact where contact_id=inv_rec.id);
                select name into mycontact from res_partner where id=mypartnerid ;
                select sum(prod_num * prod_revenue) into myrev1 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev1;
                select sum(prod_num * prod_revenue) into myrev2 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev2;
                select sum(prod_num * prod_revenue) into myrev3 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev3;
                select sum(prod_num * prod_revenue) into myrev4 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev4;
                select sum(prod_num * prod_revenue) into myrev5 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev5;
                select sum(prod_num * prod_revenue) into myrev6 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev6;
                select sum(prod_num * prod_revenue) into myrev7 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev7;
                select sum(prod_num * prod_revenue) into myrev8 from neweb_projsaleitem where saleitem_id=projectid and cost_type=rev8;
                update neweb_invoice_invoiceopen set contract_no=mycontractid,contract_main_start=mycon_main_start,contract_main_end=mycon_main_end,invoice_contact=mycontact,invoice_address=mycusaddress,
                       invoice_phone=mycusphone,revenue_1=myrev1,revenue_2=myrev2,revenue_3=myrev3,revenue_4=myrev4,revenue_5=myrev5,revenue_6=myrev6,revenue_7=myrev7,revenue_8=myrev8 where id=myid ;
                open inv_line_cur;
                loop
                  fetch inv_line_cur into inv_line_rec;
                  exit when not found;
                  select pitem_id into pitemid from neweb_pitem_list where pitem_origin_type='P' and pitem_origin_id=inv_line_rec.id ;
                  select name into purchaseno from purchase_order where id = pitemid ;
                  myuntaxamount := (inv_line_rec.prod_num * inv_line_rec.prod_revenue) ;
                  select amount,include_base_amount into myamount,myincludetaxamount from account_tax where id=inv_rec.taxes_id;
                  if myincludetaxamount=TRUE THEN 
                     mytaxamount := (inv_line_rec.prod_num * inv_line_rec.prod_revenue) ;
                     myinvoicetype := '1';
                  ELSE 
                     mytaxamount := round(inv_line_rec.prod_num * inv_line_rec.prod_revenue * (1 + ( myamount / 100)));
                     myinvoicetype := '2' ;
                  end if ;
                  myprojrevenuetaxtot := myprojrevenuetaxtot + mytaxamount ;
                  myprojectrevenuetot := myprojectrevenuetot + myuntaxamount ;
                  insert into neweb_invoice_invoiceopen_line(invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_taxtype,invoice_date,purchase_no,invoicetype,invoice_ver) values 
                   (myid,inv_line_rec.cost_type,inv_line_rec.prod_desc,inv_line_rec.prod_num,inv_line_rec.prod_revenue,inv_rec.taxes_id,curtime,purchaseno,myinvoicetype,0); 
                end loop;  
                close inv_line_cur;     
             end loop;
             update neweb_project set invoice_mark=TRUE,invoice_complete=TRUE where id=projectid ;
             update neweb_invoice_invoiceopen set project_untax_amount=myprojectrevenuetot where id = myid ;
             close inv_cur;  
          END ;$BODY$
          LANGUAGE plpgsql ; """)

        self._cr.execute("""DROP FUNCTION IF EXISTS compute_project_invoice(projno varchar,invoiceid int) cascade;""")
        self._cr.execute("""create or replace function compute_project_invoice(projno varchar,invoiceid int) returns void as $BODY$
          DECLARE 
              projid int ;
              proj_inv_amount neweb_invoice_invoiceopen.project_amount_total%type;
          BEGIN 
              proj_inv_amount := 0 ;
              select id into projid  from  neweb_project where name=projno;
             /* select sum(round(open_amount_total)) into proj_inv_amount from neweb_invoice_invoiceopen where id in (select iid from neweb_project_invoice_rel where pid=projid);
              update neweb_invoice_invoiceopen set open_complete_total=proj_inv_amount where id=invoiceid;
              update neweb_project set invoice_openamount=proj_inv_amount where id=projid; */
          END;$BODY$
          LANGUAGE plpgsql;    
             """)

        self._cr.execute("""DROP FUNCTION IF EXISTS update_invoice_record(invoiceid int) cascade;""")
        self._cr.execute("""create or replace function update_invoice_record(invoiceid int) returns void as $BODY$
          DECLARE 
             projid INTEGER ;
             ncount int;
          BEGIN 
             select project_no into projid from neweb_invoice_invoiceopen where id=invoiceid; 
             select count(*) into ncount from neweb_project_invoice_rel where pid=projid and iid=invoiceid;
             if ncount = 0 THEN 
                insert into neweb_project_invoice_rel(pid,iid) values (projid,invoiceid);
             end if;
             
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS cal_invoice_complete(invoiceid int) cascade; """)
        self._cr.execute("""create or replace function cal_invoice_complete(invoiceid int) returns void as $BODY$
          DECLARE 
              myver INTEGER ;
              myopencompletetot FLOAT ;
              myopenamounttot FLOAT ;
              mytot FLOAT ;
              projid INTEGER ;
              proj_inv_amount FLOAT ;
              proj_tot_amount FLOAT ;
              saleno varchar ;
          BEGIN 
              select invoice_ver,project_no into myver,projid from neweb_invoice_invoiceopen where id=invoiceid ;
              proj_inv_amount := 0 ;
              select open_complete_total,project_amount_total into mytot,proj_tot_amount from neweb_invoice_invoiceopen where id=invoiceid ;
              if abs(round(mytot - proj_tot_amount)) <= 1 THEN
                 update neweb_invoice_invoiceopen set is_completed = TRUE where id = invoiceid ;  
              ELSE 
                 update neweb_invoice_invoiceopen set is_completed = FALSE  where id = invoiceid ;    
              end if;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""DROP FUNCTION IF EXISTS set_invoice_complete(invoiceid int) cascade;""")
        self._cr.execute("""create or replace function set_invoice_complete(invoiceid int) returns void as $BODY$
          DECLARE
             projid INTEGER ;
          BEGIN 
             select project_no into projid from neweb_invoice_invoiceopen where id=invoiceid;
             update neweb_project set invoice_complete=TRUE where id = projid;
          END;$BODY$
          LANGUAGE plpgsql;   
             """)

        self._cr.execute("""drop function if exists update_warrantydate(invoiceid int) cascade;""")
        self._cr.execute("""create or replace function update_warrantydate(invoiceid int) returns void as $BODY$
          DECLARE
             invdate_cur refcursor ;
             invdate_rec record ;
             projno INTEGER ;
             ncount INTEGER ;
             myinvoicedate neweb_invoice_invoiceopen_line.invoice_date%type;
             mininvdate neweb_invoice_invoiceopen_line.invoice_date%type;
          BEGIN
             select count(*) into ncount from neweb_invoice_invoiceopen_line where invoice_state='3' and invoice_id = invoiceid ;
           if ncount > 0 THEN 
              open invdate_cur for select * from neweb_invoice_invoiceopen_line where invoice_state='3' and invoice_id = invoiceid ;
              loop
                  fetch invdate_cur into invdate_rec;
                  exit when not found ;
                  myinvoicedate := invdate_rec.invoice_date ;
                  select project_no into projno from neweb_invoice_invoiceopen where id=invoiceid ;
                  update neweb_projsaleitem set origin_start_date=invdate_rec.invoice_date,
                         neweb_start_date=invdate_rec.invoice_date where saleitem_id=projno and 
                         prod_modeltype like invdate_rec.invoice_spec ;  
              end loop;
              close invdate_cur ;
              select min(invoice_date) into mininvdate from neweb_invoice_invoiceopen_line where invoice_id=invoiceid
                     and invoice_state='3' ;
              update neweb_project set warranty_start_date=mininvdate where id=projno ;
           end if ;   
         END;$BODY$
         LANGUAGE  plpgsql;  
             """)



        self._cr.execute("""drop function if exists update_invoicever(invoicelineid int) cascade;""")
        self._cr.execute("""create or replace function update_invoicever(invoicelineid int) returns void as $BODY$
            DECLARE 
               invoiceid INTEGER ;
               invoicever INTEGER ;
            BEGIN 
               select invoice_id into invoiceid from neweb_invoice_invoiceopen_line where id=invoicelineid ;
               select invoice_ver into invoicever from neweb_invoice_invoiceopen where id = invoiceid ;
               update neweb_invoice_invoiceopen_line set invoice_ver=invoicever where id=invoicelineid ;
                      
               
            END ;$BODY$
            LANGUAGE plpgsql ;""")

        self._cr.execute("drop function if exists check_invoice_amount(invid int) cascade;")
        self._cr.execute("""create or replace function check_invoice_amount(invid int) returns Boolean as $BODY$
             DECLARE 
               myinvitem INTEGER ;
               nowinvamount FLOAT ;
               myprojamount FLOAT ;
               mycompleteamount FLOAT ;
               amounttot1 FLOAT ;
               amounttot2 FLOAT ;
               maxver INTEGER ;
               ncount INTEGER ;
               mycusname INTEGER ;
               mymaincusname INTEGER ;
             BEGIN 
               select count(*) into ncount from neweb_invoice_invoiceopen_line where (invoice_state='2' or invoice_state='3') ;
               if ncount > 0 THEN 
                   select round(project_amount_total) into myprojamount from neweb_invoice_invoiceopen where id = invid ;
                   select sum(round(invoice_num::numeric * invoice_unit_price1::numeric)) into mycompleteamount from neweb_invoice_invoiceopen_line 
                           where invoice_id=invid and (invoice_state='2' or invoice_state='3') ;
                   if mycompleteamount - myprojamount > 1 and myprojamount !=0  THEN 
                      return FALSE ;
                   END if ;
                   select max(invoice_ver) into maxver from neweb_invoice_invoiceopen_line 
                           where invoice_id=invid and (invoice_state='2' or invoice_state='3') ; 
                   select sum(invoice_num::numeric * invoice_unit_price1::numeric) into amounttot1 from neweb_invoice_invoiceopen_line 
                            where invoice_id=invid and (invoice_state='2' or invoice_state='3') ; 
                   select sum(invoice_num::numeric * invoice_unit_price1::numeric) into amounttot2 from neweb_invoice_invoiceopen_line 
                            where invoice_id=invid and (invoice_state='2' or invoice_state='3') and invoice_ver = maxver ; 
                  /* update neweb_invoice_invoiceopen set open_complete_total=amounttot1,open_amount_total=amounttot2
                            where id=invid ;*/
                  /* select sum(invoice_tax_amount) into mycompleteamount from neweb_invoice_invoiceopen_line 
                            where invoice_id=invid and (invoice_state='2' or invoice_state='3') ;   */
                   select cus_name,main_cus_name into mycusname,mymaincusname from neweb_project where id=(select project_no from neweb_invoice_invoiceopen where id = invid ) ;
                   update neweb_invoice_invoiceopen set cus_name=mycusname,main_cus_name=mymaincusname where id = invid ;       
                  /* if abs(round(mycompleteamount - myprojamount)) <= 10 THEN 
                      update neweb_invoice_invoiceopen set is_completed = TRUE where id = invid ; 
                   ELSE 
                      update neweb_invoice_invoiceopen set is_completed = FALSE where id = invid ; 
                   end if;  */
               end if ;    
               return TRUE  ;
             END ; $BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("drop function if exists get_max_invitem(invid int) cascade;")
        self._cr.execute("""create or replace function get_max_invitem(invid int) returns INTEGER as $BODY$
             DECLARE 
               ncount INTEGER ;
               mymaxinvitem INTEGER ;
             BEGIN 
               select count(*) into ncount from neweb_invoice_invopen_list where inv_id=invid ;
               if ncount = 0 THEN 
                  mymaxinvitem := 1 ;
               ELSE 
                  select max(inv_item) into mymaxinvitem from neweb_invoice_invopen_list where inv_id=invid ;
                  mymaxinvitem := mymaxinvitem + 1 ;
               end if ;
               return mymaxinvitem ;
             END ;$BODY$
             LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists calinvoiceamount(invoiceid int) cascade""")
        self._cr.execute("""create or replace function calinvoiceamount(invoiceid int) returns void as $BODY$
             DECLARE 
                amounttot1 FLOAT ;
                amounttot2 FLOAT ;
                maxver INTEGER ;
                ncount INTEGER ;
                projectid int ;
                taxid int ;
                myincludetaxamount Boolean ;
                myamount FLOAT  ;
                myamount1 float ;
                mytaxamount FLOAT ;
                myprojrevenuetaxtot FLOAT ;
                myprojectrevenuetot FLOAT ;
                saleno varchar ;
             BEGIN 
                select project_no into projectid from neweb_invoice_invoiceopen where id = invoiceid ;
                select sale_no into saleno from neweb_project where id = projectid ;
                
                select taxes_id into taxid from neweb_project where id=projectid ;
                select amount,include_base_amount into myamount,myincludetaxamount from account_tax where id=taxid;
                if myincludetaxamount=TRUE THEN 
                 select sum(analysis_revenue) into mytaxamount from neweb_projanalysis where analysis_id=projectid ;
                ELSE 
                 select sum(analysis_revenue) into mytaxamount  from neweb_projanalysis where analysis_id=projectid ;
                 myamount1 = round(mytaxamount::NUMERIC * 1.05) ;
                end if ;
                select discount_amount into mytaxamount from sale_order where name like saleno ;
                select count(*) into ncount from neweb_invoice_invoiceopen_line 
                       where invoice_id=invoiceid and (invoice_state='2' or invoice_state='3') ;
               /* if ncount > 0 THEN 
                    select max(invoice_ver) into maxver from neweb_invoice_invoiceopen_line 
                           where invoice_id=invoiceid and (invoice_state='2' or invoice_state='3') ;
                    select sum(invoice_tax_amount) into amounttot1 from neweb_invoice_invoiceopen_line
                           where invoice_id=invoiceid and (invoice_state='2' or invoice_state='3')  ;  
                    select sum(invoice_tax_amount) into amounttot2 from neweb_invoice_invoiceopen_line 
                           where invoice_id=invoiceid and (invoice_state='2' or invoice_state='3') and invoice_ver=maxver ;  
                ELSE 
                    amounttot1 := 0 ;
                    amounttot2 := 0 ;
                end if ;   
                update neweb_invoice_invoiceopen set open_complete_total = amounttot1,open_amount_total = amounttot2,
                   project_amount_total = myamount1  where id=invoiceid ; */
             END ;$BODY$
             LANGUAGE plpgsql;        
                """)



        self._cr.execute("""drop function if exists genprojinvdata(projno VARCHAR,cusname VARCHAR) cascade""")
        self._cr.execute("""create or replace function genprojinvdata(projno VARCHAR,cusname VARCHAR) returns void as $BODY$
         DECLARE 
            proj_cur refcursor ;
            proj_rec record ;
            projsaleline_cur refcursor ;
            projsaleline_rec record ;
            invoiceline_cur refcursor ;
            invoiceline_rec record ;
            purinv_cur refcursor ;
            purinv_rec record ;
            myprodprice FLOAT ;
            myprodrevenue FLOAT ;
            myothermemo VARCHAR ;
            mysupplier VARCHAR ;
            mycusname VARCHAR ;
            sql1 varchar ;
         BEGIN 
            delete from neweb_invoice_projectdata ;
            delete from neweb_invoice_invoicedata ;
            delete from neweb_invoice_purinvdata ;
            if cusname != '-' and projno != '-' then 
               open proj_cur for select id,name,cus_name FROM neweb_project where 
                  name ilike ''|| projno ||'%%' and cus_name in (select id from res_partner where name ilike ''|| cusname ||'%%') ;
            elsif cusname = '-' and projno != '-' then      
               open proj_cur for select id,name,cus_name FROM neweb_project where name ilike ''|| projno ||'%%' ;
            elsif cusname != '-' and projno = '-' then   
               open proj_cur for select id,name,cus_name FROM neweb_project where 
                   cus_name in (select id from res_partner where name ilike ''|| cusname ||'%%') ;
            end if ;  
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              open projsaleline_cur for select * from neweb_projsaleitem A where saleitem_id=proj_rec.id order by A.id;
              loop
                fetch projsaleline_cur into projsaleline_rec ;
                exit when not found ;
                myprodprice := projsaleline_rec.prod_num * projsaleline_rec.prod_price ;
                myprodrevenue := projsaleline_rec.prod_num * projsaleline_rec.prod_revenue ;
                insert into neweb_invoice_projectdata (project_no,prod_set,cus_name,prod_modeltype,prod_desc,
                prod_num,prod_cost_price,supplier,prod_sale_price) values (proj_rec.id,projsaleline_rec.prod_set,
                proj_rec.cus_name,projsaleline_rec.prod_modeltype,projsaleline_rec.prod_desc,projsaleline_rec.prod_num,
                myprodprice,projsaleline_rec.supplier,myprodrevenue) ;
              end loop ;
              close projsaleline_cur ;
              open invoiceline_cur for select * from neweb_invoice_invoiceopen_line where invoice_id
                 in (select id from neweb_invoice_invoiceopen where project_no=proj_rec.id) ;
              loop
                fetch invoiceline_cur into invoiceline_rec ;
                exit when not found ;
                select other_memo into myothermemo from neweb_invoice_invoiceopen where id=invoiceline_rec.invoice_id ;
                insert into neweb_invoice_invoicedata(project_no,invoice_date,invoice_no,invoice_untax_amount,application_date,other_memo) values
                 (proj_rec.id,invoiceline_rec.invoice_date,invoiceline_rec.invoice_no,invoiceline_rec.invoice_untax_amount,invoiceline_rec.create_date,myothermemo) ;
              end loop ;
              close invoiceline_cur ;   
            end loop ;
            close proj_cur ;
            if cusname != '-' and projno != '-'  then 
              open purinv_cur for select * from neweb_purinv_invoiceline WHERE    
                 pitem_origin_no ilike ''|| projno ||'%%' and cus_partner ilike ''|| cusname ||'%%';
            elsif cusname = '-' and projno != '-' then  
              open purinv_cur for select * from neweb_purinv_invoiceline WHERE    
                 pitem_origin_no ilike ''|| projno ||'%%' ;
            elsif cusname != '-' and projno = '-' then 
              open purinv_cur for select * from neweb_purinv_invoiceline WHERE    
                  cus_partner ilike ''|| cusname ||'%%';  
            end if ;
            loop
               fetch purinv_cur into purinv_rec ;
               exit when not found ;
               insert into neweb_invoice_purinvdata (pitem_origin_no,invoice_date,invoice_no,inv_paymentterm,invoice_partner,invoice_sum,payment_yn) values 
                (purinv_rec.pitem_origin_no,purinv_rec.invoice_date,purinv_rec.invoice_no,purinv_rec.inv_paymentterm,purinv_rec.invoice_partner,purinv_rec.invoice_sum,purinv_rec.payment_yn) ;
            end loop;
            close purinv_cur ;     
         END;$BODY$
         LANGUAGE plpgsql ; """)

        self._cr.execute("""drop function if exists genprojinvdata1(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function genprojinvdata1(sdate date,edate date) returns void as $BODY$
        DECLARE 
           proj_cur refcursor ;
           proj_rec record ;
           projsaleline_cur refcursor ;
           projsaleline_rec record ;
           invoiceline_cur refcursor ;
           invoiceline_rec record ;
           purinv_cur refcursor ;
           purinv_rec record ;
           myprodprice FLOAT ;
           myprodrevenue FLOAT ;
           myothermemo VARCHAR ;
           mysupplier VARCHAR ;
           mycusname VARCHAR ;
           sql1 varchar ;
           untaxamount float ;
           taxamount float ;
           tax float ;
        BEGIN 
           delete from neweb_invoice_projectdata ;
           delete from neweb_invoice_invoicedata ;
           delete from neweb_invoice_purinvdata ;
            open proj_cur for select id,name,cus_name FROM neweb_project where create_date::DATE between sdate::DATE and edate::DATE ;

           loop
             fetch proj_cur into proj_rec ;
             exit when not found ;
             open projsaleline_cur for select * from neweb_projsaleitem A where saleitem_id=proj_rec.id order by A.id;
             loop
               fetch projsaleline_cur into projsaleline_rec ;
               exit when not found ;
               myprodprice := projsaleline_rec.prod_num * projsaleline_rec.prod_price ;
               myprodrevenue := projsaleline_rec.prod_num * projsaleline_rec.prod_revenue ;
               insert into neweb_invoice_projectdata (project_no,prod_set,cus_name,prod_modeltype,prod_desc,
               prod_num,prod_cost_price,supplier,prod_sale_price) values (proj_rec.id,projsaleline_rec.prod_set,
               proj_rec.cus_name,projsaleline_rec.prod_modeltype,projsaleline_rec.prod_desc,projsaleline_rec.prod_num,
               myprodprice,projsaleline_rec.supplier,myprodrevenue) ;
             end loop ;
             close projsaleline_cur ;
             open invoiceline_cur for select * from neweb_invoice_invoiceopen_line where invoice_id
                in (select id from neweb_invoice_invoiceopen where project_no=proj_rec.id) ;
             loop
               fetch invoiceline_cur into invoiceline_rec ;
               exit when not found ;
               untaxamount = round(invoiceline_rec.invoice_num * invoiceline_rec.invoice_unit_price) ;
               tax = round(untaxamount * 0.05) ;
               taxamount = untaxamount + tax ;
               select other_memo into myothermemo from neweb_invoice_invoiceopen where id=invoiceline_rec.invoice_id ;
               insert into neweb_invoice_invoicedata(project_no,invoice_date,invoice_cdate,invoice_no,invoice_untax_amount,application_date,application_cdate,other_memo) values
                (proj_rec.id,invoiceline_rec.invoice_date,invoiceline_rec.invoice_date::TEXT,invoiceline_rec.invoice_no,untaxamount,invoiceline_rec.create_date,invoiceline_rec.create_date::DATE::TEXT,myothermemo) ;
             end loop ;
             close invoiceline_cur ;   
           end loop ;
           close proj_cur ;
           open purinv_cur for select * from neweb_purinv_invoiceline WHERE pitem_origin_no in 
              (select name from neweb_project where create_date::DATE between sdate::DATE and edate::DATE) ;
           loop
              fetch purinv_cur into purinv_rec ;
              exit when not found ;
              insert into neweb_invoice_purinvdata (pitem_origin_no,invoice_date,invoice_cdate,invoice_no,inv_paymentterm,inv_cpaymentterm,invoice_partner,invoice_sum,payment_yn) values 
               (purinv_rec.pitem_origin_no,purinv_rec.invoice_date,purinv_rec.invoice_date::TEXT,purinv_rec.invoice_no,purinv_rec.inv_paymentterm,purinv_rec.inv_paymentterm::TEXT,purinv_rec.invoice_partner,purinv_rec.invoice_sum,purinv_rec.payment_yn) ;
           end loop;
           close purinv_cur ;     
        END;$BODY$
        LANGUAGE plpgsql ; """)

        self._cr.execute("""drop function if exists genprojinvdata2(projinvid int) cascade""")
        self._cr.execute("""create or replace function genprojinvdata2(projinvid int) returns void as $BODY$
        DECLARE 
           proj_cur refcursor ;
           proj_rec record ;
           projsaleline_cur refcursor ;
           projsaleline_rec record ;
           invoiceline_cur refcursor ;
           invoiceline_rec record ;
           purinv_cur refcursor ;
           projinv_cur refcursor ;
           projinv_rec record ;
           purinv_rec record ;
           myprodprice FLOAT ;
           myprodrevenue FLOAT ;
           myothermemo VARCHAR ;
           mysupplier VARCHAR ;
           mycusname VARCHAR ;
           sql1 varchar ;
           untaxamount float ;
           taxamount float ;
           tax float ;
        BEGIN 
           delete from neweb_invoice_projectdata ;
           delete from neweb_invoice_invoicedata ;
           delete from neweb_invoice_purinvdata ;
            open proj_cur for select id,name,cus_name FROM neweb_project where id in 
               (select proj_id from neweb_project_projinv_rel where projinv_id=projinvid);
           loop
             fetch proj_cur into proj_rec ;
             exit when not found ;
             open projsaleline_cur for select * from neweb_projsaleitem A where saleitem_id=proj_rec.id order by A.id;
             loop
               fetch projsaleline_cur into projsaleline_rec ;
               exit when not found ;
               myprodprice := projsaleline_rec.prod_num * projsaleline_rec.prod_price ;
               myprodrevenue := projsaleline_rec.prod_num * projsaleline_rec.prod_revenue ;
               insert into neweb_invoice_projectdata (project_no,prod_set,cus_name,prod_modeltype,prod_desc,
               prod_num,prod_cost_price,supplier,prod_sale_price) values (proj_rec.id,projsaleline_rec.prod_set,
               proj_rec.cus_name,projsaleline_rec.prod_modeltype,projsaleline_rec.prod_desc,projsaleline_rec.prod_num,
               myprodprice,projsaleline_rec.supplier,myprodrevenue) ;
             end loop ;
             close projsaleline_cur ;
             open invoiceline_cur for select * from neweb_invoice_invoiceopen_line where invoice_id
                in (select id from neweb_invoice_invoiceopen where project_no=proj_rec.id) ;
             loop
               fetch invoiceline_cur into invoiceline_rec ;
               exit when not found ;
               untaxamount = round(invoiceline_rec.invoice_num * invoiceline_rec.invoice_unit_price) ;
               tax = round(untaxamount * 0.05) ;
               taxamount = untaxamount + tax ;
               select other_memo into myothermemo from neweb_invoice_invoiceopen where id=invoiceline_rec.invoice_id ;
               insert into neweb_invoice_invoicedata(project_no,invoice_date,invoice_cdate,invoice_no,invoice_untax_amount,application_date,application_cdate,other_memo) values
                (proj_rec.id,invoiceline_rec.invoice_date,invoiceline_rec.invoice_date::TEXT,invoiceline_rec.invoice_no,untaxamount,invoiceline_rec.create_date,invoiceline_rec.create_date::DATE::TEXT,myothermemo) ;
             end loop ;
             close invoiceline_cur ;   
           end loop ;
           close proj_cur ;
           open projinv_cur for select distinct proj_id from neweb_project_projinv_rel where projinv_id = projinvid ;
           loop
               fetch projinv_cur into projinv_rec ;
               exit when not found ;
               open purinv_cur for select * from neweb_purinv_invoiceline WHERE pitem_origin_no in (select name from neweb_project where id = projinv_rec.proj_id) ;
               loop
                  fetch purinv_cur into purinv_rec ;
                  exit when not found ;
                  insert into neweb_invoice_purinvdata (pitem_origin_no,invoice_date,invoice_cdate,invoice_no,inv_paymentterm,inv_cpaymentterm,invoice_partner,invoice_sum,payment_yn) values 
                   (purinv_rec.pitem_origin_no,purinv_rec.invoice_date,purinv_rec.invoice_date::TEXT,purinv_rec.invoice_no,purinv_rec.inv_paymentterm,purinv_rec.inv_paymentterm::TEXT,purinv_rec.invoice_partner,purinv_rec.invoice_sum,purinv_rec.payment_yn) ;
               end loop;
               close purinv_cur ;   
           end loop ;
           close projinv_cur ;      
        END;$BODY$
        LANGUAGE plpgsql ; """)

        self._cr.execute("""drop function if exists genprojinvdata3(projno varchar) cascade""")
        self._cr.execute("""create or replace function genprojinvdata3(projno varchar) returns void as $BODY$
        DECLARE 
           proj_cur refcursor ;
           proj_rec record ;
           projsaleline_cur refcursor ;
           projsaleline_rec record ;
           invoiceline_cur refcursor ;
           invoiceline_rec record ;
           purinv_cur refcursor ;
           purinv_rec record ;
           myprodprice FLOAT ;
           myprodrevenue FLOAT ;
           myothermemo VARCHAR ;
           mysupplier VARCHAR ;
           mycusname VARCHAR ;
           sql1 varchar ;
           projlen int ;
           untaxamount float ;
           taxamount float ;
           tax float ;
        BEGIN 
           select length(projno) into projlen ; 
           delete from neweb_invoice_projectdata ;
           delete from neweb_invoice_invoicedata ;
           delete from neweb_invoice_purinvdata ;
           open proj_cur for select id,name,cus_name FROM neweb_project where substring(name,1,projlen)=projno;
           loop
             fetch proj_cur into proj_rec ;
             exit when not found ;
             open projsaleline_cur for select * from neweb_projsaleitem A where saleitem_id=proj_rec.id order by A.id;
             loop
               fetch projsaleline_cur into projsaleline_rec ;
               exit when not found ;
               myprodprice := projsaleline_rec.prod_num * projsaleline_rec.prod_price ;
               myprodrevenue := projsaleline_rec.prod_num * projsaleline_rec.prod_revenue ;
               insert into neweb_invoice_projectdata (project_no,prod_set,cus_name,prod_modeltype,prod_desc,
               prod_num,prod_cost_price,supplier,prod_sale_price) values (proj_rec.id,projsaleline_rec.prod_set,
               proj_rec.cus_name,projsaleline_rec.prod_modeltype,projsaleline_rec.prod_desc,projsaleline_rec.prod_num,
               myprodprice,projsaleline_rec.supplier,myprodrevenue) ;
             end loop ;
             close projsaleline_cur ;
             open invoiceline_cur for select * from neweb_invoice_invoiceopen_line where invoice_id
                in (select id from neweb_invoice_invoiceopen where project_no=proj_rec.id) ;
             loop
               fetch invoiceline_cur into invoiceline_rec ;
               exit when not found ;
               untaxamount = round(invoiceline_rec.invoice_num * invoiceline_rec.invoice_unit_price) ;
               tax = round(untaxamount * 0.05) ;
               taxamount = untaxamount + tax ;
               select other_memo into myothermemo from neweb_invoice_invoiceopen where id=invoiceline_rec.invoice_id ;
               insert into neweb_invoice_invoicedata(project_no,invoice_date,invoice_cdate,invoice_no,invoice_untax_amount,application_date,application_cdate,other_memo) values
                (proj_rec.id,invoiceline_rec.invoice_date,invoiceline_rec.invoice_date::TEXT,invoiceline_rec.invoice_no,untaxamount,invoiceline_rec.create_date,invoiceline_rec.create_date::DATE::TEXT,myothermemo) ;
             end loop ;
             close invoiceline_cur ;   
           end loop ;
           close proj_cur ;
           open purinv_cur for select * from neweb_purinv_invoiceline WHERE pitem_origin_no in 
              (select name from neweb_project where substring(name,1,projlen)=projno) ;
           loop
              fetch purinv_cur into purinv_rec ;
              exit when not found ;
              insert into neweb_invoice_purinvdata (pitem_origin_no,invoice_date,invoice_cdate,invoice_no,inv_paymentterm,inv_cpaymentterm,invoice_partner,invoice_sum,payment_yn) values 
               (purinv_rec.pitem_origin_no,purinv_rec.invoice_date,purinv_rec.invoice_date::TEXT,purinv_rec.invoice_no,purinv_rec.inv_paymentterm,purinv_rec.inv_paymentterm::TEXT,purinv_rec.invoice_partner,purinv_rec.invoice_sum,purinv_rec.payment_yn) ;
           end loop;
           close purinv_cur ;     
        END;$BODY$
        LANGUAGE plpgsql ; """)

        self._cr.execute("""drop function if exists check_invoiceamounttot(invoiceid int) cascade""")
        self._cr.execute("""create or replace function check_invoiceamounttot(invoiceid int) returns Boolean as $BODY$
         declare 
         myresult Boolean ;
         ncount int ;
         begin 
           select count(*) into ncount from neweb_invoice_invoiceopen where id=invoiceid and 
                  round(open_complete_total) - round(project_amount_total) > 1 ;
           if ncount = 0 then 
              myresult := True ;
           else 
              myresult := False ;
           end if ;
           return myresult ;            
         end;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists check_start_date(invoiceopenid int) cascade;""")
        self._cr.execute("""create or replace function check_start_date(invoiceopenid int) returns void as $BODY$
         DECLARE 
           mystartdate DATE ;
           myprojid int ;
         BEGIN 
           select project_no into myprojid from neweb_invoice_invoiceopen where id = invoiceopenid ;
           select max(invoice_date) into mystartdate from neweb_invoice_invoiceopen_line where invoice_id=invoiceopenid and invoice_state = '3' and invoice_date is not null ;
           if mystartdate is not null then
              update neweb_projsaleitem set origin_start_date=mystartdate,neweb_start_date=mystartdate where saleitem_id=myprojid ; 
           end if;   
         END ;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists allinvcusorder() cascade;""")
        self._cr.execute("""create or replace function allinvcusorder() returns void as $BODY$
        DECLARE 
          inv_cur refcursor ;
          inv_rec record ;
          mycusorder varchar ;
        BEGIN 
          open inv_cur for select id,project_no from neweb_invoice_invoiceopen ;
          loop
            fetch inv_cur into inv_rec ;
            exit when not found ;
            select coalesce(cus_order,' ') into mycusorder from neweb_project where id = inv_rec.project_no ;
            update neweb_invoice_invoiceopen set cus_order=mycusorder where id = inv_rec.id ;
          end loop ;
          close inv_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists updatecusorder(invid int) cascade;""")
        self._cr.execute("""create or replace function updatecusorder(invid int) returns void as $BODY$
        DECLARE 
          mycusorder varchar ;
          myprojectid int ;
        BEGIN 
          select cus_order,project_no into mycusorder,myprojectid from neweb_invoice_invoiceopen where id = invid ;
          if mycusorder is not null then 
             update neweb_project set cus_order=mycusorder where id = myprojectid ;
          end if ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        # self._cr.execute("""drop function if exists check_invoiceamounttot(invoiceid int) cascade""")
        # self._cr.execute("""create or replace function check_invoiceamounttot(invoiceid int) returns Boolean as $BODY$
        #  declare
        #  myresult Boolean ;
        #  ncount int ;
        #  begin
        #    select count(*) into ncount from neweb_invoice_invoiceopen where id=invoiceid and
        #           round(open_complete_total) - round(project_amount_total) > 1 ;
        #    if ncount = 0 then
        #       myresult := True ;
        #    else
        #       myresult := False ;
        #    end if ;
        #    return myresult ;
        #  end;$BODY$
        #  LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists check_start_date(invoiceopenid int) cascade;""")
        self._cr.execute("""create or replace function check_start_date(invoiceopenid int) returns void as $BODY$
         DECLARE 
           mystartdate DATE ;
           myprojid int ;
         BEGIN 
           select project_no into myprojid from neweb_invoice_invoiceopen where id = invoiceopenid ;
           select max(invoice_date) into mystartdate from neweb_invoice_invoiceopen_line where invoice_id=invoiceopenid and invoice_state = '3' and invoice_date is not null ;
           if mystartdate is not null then
              update neweb_projsaleitem set origin_start_date=mystartdate,neweb_start_date=mystartdate where saleitem_id=myprojid ; 
           end if;   
         END ;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists allinvcusorder() cascade;""")
        self._cr.execute("""create or replace function allinvcusorder() returns void as $BODY$
            DECLARE 
              inv_cur refcursor ;
              inv_rec record ;
              mycusorder varchar ;
            BEGIN 
              open inv_cur for select id,project_no from neweb_invoice_invoiceopen ;
              loop
                fetch inv_cur into inv_rec ;
                exit when not found ;
                select coalesce(cus_order,' ') into mycusorder from neweb_project where id = inv_rec.project_no ;
                update neweb_invoice_invoiceopen set cus_order=mycusorder where id = inv_rec.id ;
              end loop ;
              close inv_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists updatecusorder(invid int) cascade;""")
        self._cr.execute("""create or replace function updatecusorder(invid int) returns void as $BODY$
            DECLARE 
              mycusorder varchar ;
              myprojectid int ;
            BEGIN 
              select cus_order,project_no into mycusorder,myprojectid from neweb_invoice_invoiceopen where id = invid ;
              if mycusorder is not null then 
                 update neweb_project set cus_order=mycusorder where id = myprojectid ;
              end if ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastinvdate(invid int) cascade""")
        self._cr.execute("""create or replace function getlastinvdate(invid int) returns DATE as $BODY$
          DECLARE
            myres DATE ;
          BEGIN
            select max(invoice_date) into myres from neweb_invoice_invoiceopen_line where invoice_id=invid ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentaxprice1(invlineid int) cascade""")
        self._cr.execute("""create or replace function gentaxprice1(invlineid int) returns void as $BODY$
         DECLARE
           invunitprice float ;
           invunitprice1 float ;
         BEGIN
           select invoice_unit_price,invoice_unit_price1 into invunitprice,invunitprice1 from neweb_invoice_invoiceopen_line where id=invlineid ;
           if invunitprice=0 and invunitprice1 != 0 then
              invunitprice = round((invunitprice1::numeric/1.05::numeric),0) ;
              update neweb_invoice_invoiceopen_line set invoice_unit_price=invunitprice where id = invlineid ;
           end if ;
           if invunitprice != 0 and invunitprice1 = 0 then
              invunitprice1 = round((invunitprice::numeric * 1.05::numeric),0) ;
              update neweb_invoice_invoiceopen_line set invoice_unit_price1=invunitprice1 where id = invlineid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getsalediscountamount(invid int) cascade""")
        self._cr.execute("""create or replace function getsalediscountamount(invid int) returns INT as $BODY$
         DECLARE
           myres int ;
           ncount int ;
           projid int ;
           saleno varchar ;
           taxesid int ;
           taxamount float ;
           taxamount1 int ;
           revenuetot float ;
           revenuetot1 float ;
         BEGIN
           select project_no into projid from neweb_invoice_invoiceopen where id = invid ;
           if projid is not null then
              select sum(analysis_revenue)::INT into revenuetot from neweb_projanalysis where analysis_id=projid ;
              select taxes_id into taxesid from neweb_project where id = projid ;
              if taxesid is not null then
                 select amount into taxamount from account_tax where id = taxesid ;
              else
                 taxamount = 0 ;
              end if ;
              /* select sum(prod_revenue) into revenuetot from neweb_projsaleitem where saleitem_id=projid ;*/
              taxamount1 = (revenuetot::numeric * (taxamount::numeric/100::numeric))::INT ;
              revenuetot =  revenuetot + taxamount1 ; 
             select sale_no into saleno from neweb_project where id = projid ;
              if saleno is not null then
                 select discount_amount into revenuetot1 from sale_order where name = saleno ;
              else
                revenuetot1 = 0 ;
              end if ;
             /* if revenuetot > revenuetot1 then
                 myres = revenuetot ;
              else
                 myres = revenuetot1 ;
              end if ; */
              myres = revenuetot ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genunitprice1() cascade""")
        self._cr.execute("""create or replace function genunitprice1() returns void as $BODY$
          DECLARE
           pr_cur refcursor ;
           pr_rec record ;
          BEGIN
            open pr_cur for select id,invoice_unit_price,invoice_unit_price1 from neweb_invoice_invoiceopen_line where (invoice_unit_price1=0 or invoice_unit_price1 is null) ;
            loop
              fetch pr_cur into pr_rec ;
              exit when not found ;
              if pr_rec.invoice_unit_price > 0 then
                 update neweb_invoice_invoiceopen_line set invoice_unit_price1=round(invoice_unit_price * 1.05,0) where id = pr_rec.id ;
              end if ;
            end loop ;
            close pr_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setinvoicesales(invid int) cascade""")
        self._cr.execute("""create or replace function setinvoicesales(invid int) returns void as $BODY$
         DECLARE
           projid int ;
           partnerid int ;
           emp_cur refcursor ;
           emp_rec record ;
           isactive Boolean ;
           userid int ;
           nitem int ;
           invoiceid int ;
         BEGIN
           select project_no into projid from neweb_invoice_invoiceopen where id=invid ;
           if projid is not null then
               select cus_name into partnerid from neweb_project where id=projid ; 
               update neweb_invoice_invoiceopen set salesp1=null,salesp2=null,salesp3=null,salesp4=null,salesp5=null where id = invid ;
               nitem=1 ;
               open emp_cur for select * from hr_employee_res_partner_rel where res_partner_id=partnerid ;
               loop
                 fetch emp_cur into emp_rec ;
                 exit when not found ;
                 select user_id into userid from hr_employee where id=emp_rec.hr_employee_id and active=True ;
                 if userid is not null then
                    if nitem = 1 then
                       update neweb_invoice_invoiceopen set salesp1=userid where id = invid ;
                    elsif nitem = 2 then
                       update neweb_invoice_invoiceopen set salesp2=userid where id = invid ;
                    elsif nitem = 3 then
                       update neweb_invoice_invoiceopen set salesp3=userid where id = invid ;
                    elsif nitem = 4 then
                       update neweb_invoice_invoiceopen set salesp4=userid where id = invid ;
                    elsif nitem = 5 then
                       update neweb_invoice_invoiceopen set salesp5=userid where id = invid ;
                    end if ; 
                    nitem = nitem + 1 ;
                 end if ;
               end loop ;
               close emp_cur ;
            end if ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geninvoicesales() cascade""")
        self._cr.execute("""create or replace function geninvoicesales() returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
         BEGIN
           open inv_cur for select id from neweb_invoice_invoiceopen ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             execute setinvoicesales(inv_rec.id) ;
           end loop ;
           close inv_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencandoinvmail() cascade""")
        self._cr.execute("""create or replace function gencandoinvmail() returns void as $BODY$
          DECLARE
            /*im_cur refcursor ;
            im_rec record ;*/
            mynowdate date ;
          BEGIN
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
            
            update neweb_invoice_invoice_sendmail set cando=TRUE,is_send=FALSE where 
             (is_send is null or is_send=FALSE) and send_date::DATE <= mynowdate::DATE 
             and sendmail_type='1' and send_date::DATE >= '2022-10-01'::DATE ;
             
             delete from neweb_invoice_invoice_sendmail where send_date < '2022-10-01'::DATE ;
           /* open im_cur for select * from neweb_invoice_invoice_sendmail where is_send=FALSE and send_date::DATE <= mynowdate::DATE and sendmail_type='1' and send_date::DATE >= '2022-09-01'::DATE ;
            loop
              fetch im_cur into im_rec ;
              exit when not found ;
              update neweb_invoice_invoice_sendmail set cando=TRUE where id = im_rec.id ;
            end loop ;
            close im_cur ;*/
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencandoremindermail() cascade""")
        self._cr.execute("""create or replace function gencandoremindermail() returns void as $BODY$
          DECLARE
            ra_cur refcursor ;
            ra_rec record ;
            mynowdate date ;
          BEGIN
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
            open ra_cur for select * from neweb_invoice_reminder_alert where is_send=FALSE and send_date::DATE <= mynowdate::DATE  and sendmail_type='2' and active=TRUE and send_date::DATE >= '2022-09-01'::DATE ;
            loop
              fetch ra_cur into ra_rec ;
              exit when not found ;
              update neweb_invoice_reminder_alert set cando=TRUE where id = ra_rec.id ;
            end loop ;
            close ra_cur ;
            update neweb_invoice_reminder_alert set active=FALSE where send_date::DATE < '2022-09-01'::DATE and sendmail_type='2' and active=TRUE ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencandoalertmail() cascade""")
        self._cr.execute("""create or replace function gencandoalertmail() returns void as $BODY$
          DECLARE
            ra_cur refcursor ;
            ra_rec record ;
            mynowdate date ;
          BEGIN
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
            open ra_cur for select * from neweb_invoice_reminder_alert where is_send=FALSE and send_date::DATE <= mynowdate::DATE  and sendmail_type='3' and active=TRUE and send_date::DATE >= '2022-09-01'::DATE ;
            loop
              fetch ra_cur into ra_rec ;
              exit when not found ;
              update neweb_invoice_reminder_alert set cando=TRUE where id = ra_rec.id ;
            end loop ;
            close ra_cur ;
            update neweb_invoice_reminder_alert set active=FALSE where send_date::DATE < '2022-09-01'::DATE and sendmail_type='3' and active=TRUE ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getsaleassist() cascade""")
        self._cr.execute("""create or replace function getsaleassist() returns varchar as $BODY$
         DECLARE
           ass_cur refcursor ;
           ass_rec record ;
           myres varchar ;
           empname varchar ;
         BEGIN
           myres='';
           open ass_cur for select * from neweb_acceptance_assist ;
           loop
             fetch ass_cur into ass_rec ;
             exit when not found ;
             select name into empname from hr_employee where id = ass_rec.sale_assist and active=True ;
             if myres='' then
                myres = empname ;
             else
                myres = concat(myres,'/',empname) ;
             end if ;   
           end loop ;
           close ass_cur ;
           if myres is null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 產生7天即將到期預計收款日發票發通知信
        # 測試區 暫設 1天
        self._cr.execute("""drop function if exists genweeklyinvoicemail() cascade""")
        self._cr.execute("""create or replace function genweeklyinvoicemail() returns void as $BODY$
         DECLARE
           invl_cur refcursor ;
           invl_rec record ;
           nowdate date ;
           sdate date ;
           edate date ;
           projid int;
           cusname int ;
           invcontact1 int ;
           invpaymentdate date ;
           senddate date ;
           saleassist varchar ;
           mymaxid int ;
           ncount int ;
           ncount1 int ;
         BEGIN
           select getsaleassist() into saleassist ;
           select current_timestamp::DATE into sdate ;
           select sdate + interval '7 day' into edate ;
           open invl_cur for select * from neweb_invoice_invoiceopen_line where receive_date >= sdate and receive_date <= edate 
                and receive_date1 is null and invoice_no is not null and invoice_state in ('2','3');
           loop
             fetch invl_cur into invl_rec ;
             exit when not found ;
             select project_no,invoice_contact1,invoice_paymentdate into projid,invcontact1,invpaymentdate 
                   from neweb_invoice_invoiceopen where id = invl_rec.invoice_id ;
                select cus_name into cusname from neweb_project where id = projid ;                  
                /* select (invl_rec.receive_date - interval '7 day')::DATE into senddate ; */
                /* 測試時都改成 1天 */ 
                select (invl_rec.receive_date - interval '1 day')::DATE into senddate ; 
                select count(*) into ncount from neweb_invoice_invoice_sendmail where invoice_no=NEW.invoice_no and send_date=senddate ; 
                if ncount = 0 then
                   insert into neweb_invoice_invoice_sendmail(invoice_date,send_date,partner_id,invoice_contact1,invoice_no,is_send,invoice_paymentdate,cando,invoice_taxtype,sale_assist,sendmail_type)
                    values (invl_rec.invoice_date,senddate,cusname,invcontact1,invl_rec.invoice_no,False,invpaymentdate,False,invl_rec.invoice_taxtype,saleassist,'2') ;
                end if ;
                select max(id) into mymaxid from neweb_invoice_invoice_sendmail where invoice_no=invl_rec.invoice_no and send_date=senddate ;
                select count(*) into ncount1 from neweb_invoice_invoice_sendmail_line where sendmail_id = mymaxid and inv_sequence_id = invl_rec.id ;
                if ncount1 = 0 then
                   insert into neweb_invoice_invoice_sendmail_line(sendmail_id,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,inv_sequence_id) values
                    (mymaxid,invl_rec.invoice_spec,invl_rec.invoice_num,invl_rec.invoice_unit_price,invl_rec.invoice_unit_price1,invl_rec.invoice_taxtype,invl_rec.id) ;
                end if ;
           end loop ;
           close invl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'inv_reminder_alert_view')
        self._cr.execute("""create or replace view inv_reminder_alert_view as (
                                   select A.invoice_id,A.invoice_costtype,A.invoice_num,A.invoice_unit_price1,A.invoice_no,A.invoice_date,A.invoice_state,A.receive_date,A.receive_date1,B.project_no,B.contract_no,B.invoice_contact1,C.cus_name as partner_id
                                   from neweb_invoice_invoiceopen_line A left join neweb_invoice_invoiceopen B on A.invoice_id=B.id 
                                   left join neweb_project C on B.project_no = C.id where A.invoice_state in ('2','3') and receive_date is not null and receive_date1 is null and C.cus_name is not null)
                                   """)

        self._cr.execute("""drop function if exists gen_month_reminder() cascade""")
        self._cr.execute("""create or replace function gen_month_reminder() returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           cy varchar ;
           cm varchar ;
           nowdate date ;
           senddate date ;
           duedate date ;
           inv_cur refcursor ;
           inv_rec record ;
           saleassist varchar ;
           mymaxid int ;
         BEGIN
           select getsaleassist() into saleassist ;
           select current_timestamp::DATE into nowdate ;
           select date_part('year',nowdate)::TEXT into cy ;
           select lpad(date_part('month',nowdate)::TEXT,2,'0') into cm ;
           open inv_cur for select * from inv_reminder_alert_view  order by partner_id,receive_date ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             select count(*) into ncount from neweb_invoice_reminder_alert where partner_id=inv_rec.partner_id and inv_year=cy and inv_month=cm ;
             if ncount = 0 then
                update neweb_invoice_reminder_alert set active=FALSE where partner_id=inv_rec.partner_id and active=TRUE ;
                select inv_rec.receive_date - interval '1 day' into senddate ;
                /*  select inv_rec.receive_date - interval '7 day' into senddate ; */
                if senddate::DATE >= '2022-09-01'::DATE then
                   insert into neweb_invoice_reminder_alert(send_date,partner_id,invoice_contact1,is_send,cando,sendmail_type,inv_year,inv_month,active) values
                      (senddate,inv_rec.partner_id,inv_rec.invoice_contact1,FALSE,FALSE,'2',cy,cm,TRUE) ;
                    select max(id) into mymaxid from neweb_invoice_reminder_alert ; 
                end if ;    
             else
                select max(id) into mymaxid from neweb_invoice_reminder_alert where partner_id=inv_rec.partner_id and inv_year=cy and inv_month=cm and active=TRUE ; 
             end if ;
             select count(*) into ncount1 from neweb_invoice_reminder_alert_line where ra_id = mymaxid and invoice_no=inv_rec.invoice_no ;
             if ncount1 = 0 and senddate::DATE >= '2022-09-01'::DATE then
                insert into neweb_invoice_reminder_alert_line(ra_id,invoice_date,project_no,contract_no,invoice_no,invoice_tax_amount,invoice_paymentdate) values
                 (mymaxid,inv_rec.invoice_date,inv_rec.project_no,inv_rec.contract_no,inv_rec.invoice_no,(inv_rec.invoice_num::numeric * inv_rec.invoice_unit_price1::numeric)::INT,inv_rec.receive_date) ;
             end if ;
           end loop ;
           close inv_cur ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_month_alert() cascade""")
        self._cr.execute("""create or replace function gen_month_alert() returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           cy varchar ;
           cm varchar ;
           nowdate date ;
           senddate date ;
           duedate date ;
           inv_cur refcursor ;
           inv_rec record ;
           saleassist varchar ;
           mymaxid int ;
         BEGIN
           select getsaleassist() into saleassist ;
           select current_timestamp::DATE into nowdate ;
           select date_part('year',nowdate)::TEXT into cy ;
           select lpad(date_part('month',nowdate)::TEXT,2,'0') into cm ;
           select concat(cy,'-',cm,'-01')::DATE into duedate ;
           senddate = duedate ;
           select duedate + interval '1 month' - interval '1 day' into duedate ; /* 結帳月底 */
           open inv_cur for select * from inv_reminder_alert_view where receive_date <= nowdate order by partner_id,receive_date ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             select count(*) into ncount from neweb_invoice_reminder_alert where partner_id=inv_rec.partner_id and sendmail_type='3' and active=TRUE ;
             if ncount = 0 then
                update neweb_invoice_reminder_alert set active=FALSE where partner_id=inv_rec.partner_id and sendmail_type='3' ;
                select inv_rec.receive_date + interval '1 day' into senddate ;
                /* select nowdate + interval '1 day' into senddate ;  */
                 if senddate::DATE >= '2022-09-01'::DATE then
                    insert into neweb_invoice_reminder_alert(send_date,partner_id,invoice_contact1,is_send,cando,sendmail_type,inv_year,inv_month,active) values
                      (senddate,inv_rec.partner_id,inv_rec.invoice_contact1,FALSE,FALSE,'3',cy,cm,TRUE) ;
                    select max(id) into mymaxid from neweb_invoice_reminder_alert ; 
                 end if ;   
             else
                select max(id) into mymaxid from neweb_invoice_reminder_alert where partner_id=inv_rec.partner_id and sendmail_type='3' and active=TRUE ; 
             end if ;
             select count(*) into ncount1 from neweb_invoice_reminder_alert_line where ra_id = mymaxid and invoice_no=inv_rec.invoice_no ;
             if ncount1 = 0 and senddate::DATE >= '2022-09-01'::DATE then
                insert into neweb_invoice_reminder_alert_line(ra_id,invoice_date,project_no,contract_no,invoice_no,invoice_tax_amount,invoice_paymentdate) values
                 (mymaxid,inv_rec.invoice_date,inv_rec.project_no,inv_rec.contract_no,inv_rec.invoice_no,(inv_rec.invoice_num::numeric * inv_rec.invoice_unit_price1::numeric)::INT,inv_rec.receive_date) ;
             end if ;
           end loop ;
           close inv_cur ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 將 整理好的 neweb_invoice_reminder_alert 賦予權限組
        self._cr.execute("""drop function if exists gen_reminder_alert_security() cascade""")
        self._cr.execute("""create or replace function gen_reminder_alert_security() returns void as $BODY$
         DECLARE
          ra_cur refcursor ;
          ra_rec record ;
          projid int ;
          projsaleid int ;
          parentid int ;
          userid int ;
         BEGIN
           open ra_cur for select id from neweb_invoice_reminder_alert where active=TRUE and is_send=FALSE ;
           loop
             fetch ra_cur into ra_rec ;
             exit when not found ;
             select max(project_no) into projid from neweb_invoice_reminder_alert_line where ra_id = ra_rec.id ;
             select proj_sale into projsaleid from neweb_project where id = projid ;
             select user_id,parent_id into userid,parentid from hr_employee where id = projsaleid ;
             update neweb_invoice_reminder_alert set own_user1=userid where id = ra_rec.id ;
             if parentid is not null then
                select user_id into userid from hr_employee where id = parentid ;
                if userid is not null then
                   update neweb_invoice_reminder_alert set own_user2=userid where id = ra_rec.id ;
                end if ;
             end if ;
           end loop ;
           close ra_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geninvprojamounttot() cascade""")
        self._cr.execute("""create or replace function geninvprojamounttot() returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
           invdate date ;
           invl_cur refcursor ;
           invl_rec record ;
           mytaxamount float ;
           myltaxamount float ;
           projamount int;
         BEGIN
           open inv_cur for select id from neweb_invoice_invoiceopen ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
              select getsalediscountamount(inv_rec.id) into projamount ;
              mytaxamount = 0 ;
              myltaxamount = 0 ;
              select max(invoice_date) into invdate from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id and invoice_state in ('2','3') ;
              select sum(invoice_num::numeric * invoice_unit_price1::numeric) into mytaxamount from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id and invoice_state in ('2','3') ;
              select sum(invoice_num::numeric * invoice_unit_price1::numeric) into myltaxamount from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id and invoice_state in ('2','3') and invoice_date=invdate;
              update neweb_invoice_invoiceopen set project_amount_total=projamount,open_complete_total=mytaxamount,open_amount_total=myltaxamount where id = inv_rec.id ;
           end loop;
           close inv_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists isweek1day() cascade""")
        self._cr.execute("""create or replace function isweek1day() returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           weekday int ;
           mynowdate DATE ;
         BEGIN
           select current_timestamp::DATE into mynowdate ;
           select extract(dow from mynowdate::DATE)::INT into weekday ;
           if weekday=1 then
              myres = TRUE ;
           else
              myres = FALSE ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists geninvprojamount(invid int) cascade""")
        self._cr.execute("""create or replace function geninvprojamount(invid int) returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
           invdate date ;
           invl_cur refcursor ;
           invl_rec record ;
           mytaxamount float ;
           myltaxamount float ;
           projamount int;
         BEGIN
             select getsalediscountamount(invid) into projamount ;
             mytaxamount = 0 ;
             myltaxamount = 0 ;
             select max(invoice_date) into invdate from neweb_invoice_invoiceopen_line where invoice_id=invid and invoice_state in ('2','3') ;
             select sum(invoice_num::numeric * invoice_unit_price1::numeric) into mytaxamount from neweb_invoice_invoiceopen_line where invoice_id=invid and invoice_state in ('2','3') ;
             select sum(invoice_num::numeric * invoice_unit_price1::numeric) into myltaxamount from neweb_invoice_invoiceopen_line where invoice_id=invid and invoice_state in ('2','3') and invoice_date=invdate;
             update neweb_invoice_invoiceopen set project_amount_total=projamount,open_complete_total=mytaxamount,open_amount_total=myltaxamount where id = invid ;
             if abs(projamount - mytaxamount) <= 10 or (mytaxamount > projamount) then
                update neweb_invoice_invoiceopen set is_completed=TRUE where id = invid ;
             end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists updatesendmailnew(smid int) cascade""")
        self._cr.execute("""create or replace function updatesendmailnew(smid int) returns void as $BODY$
         DECLARE
          sm_cur refcursor ;
          sm_rec record ;
          sml_cur refcursor ;
          sml_rec record ;
          partnerid int ;
          invcontact1 int ;
          projno int ;
          contractno int ;
          invno varchar ;
          invseqid int ;
          senddate date ;
         BEGIN
           open sm_cur for select * from neweb_invoice_invoice_sendmail_line where sendmail_id = smid ;
           loop
               fetch sm_cur into sm_rec ;
               exit when not found ;
                   open sml_cur for select * from neweb_invoice_invoiceopen_line 
                         where id = sm_rec.inv_sequence_id and invoice_no is not null and invoice_state in ('2','3') ;
                   loop
                     fetch sml_cur into sml_rec ;
                     exit when not found ;
                     select sml_rec.invoice_date + interval '7 day' into senddate ;
                     select project_no,contract_no,cus_name,invoice_contact1 into projno,contractno,partnerid,invcontact1 
                        from neweb_invoice_invoiceopen where id = sml_rec.invoice_id ;
                     update neweb_invoice_invoice_sendmail_line set invoice_spec=sml_rec.invoice_spec,invoice_num=sml_rec.invoice_num,
                           invoice_unit_price=sml_rec.invoice_unit_price,invoice_unit_price1=sml_rec.invoice_unit_price1,
                           invoice_taxtype=sml_rec.invoice_taxtype where inv_sequence_id=sml_rec.id ;
                     update neweb_invoice_invoice_sendmail set invoice_date=sml_rec.invoice_date,send_date=senddate,partner_id=partnerid,
                           invoice_contact1=invcontact1,project_no=projno,contract_no=contractno,invoice_taxtype=sml_rec.invoice_taxtype,
                           invoice_no=sml_rec.invoice_no,is_send=FALSE where id = smid ;      
                   end loop;
                   close sml_cur ;
           end loop ; 
           close sm_cur ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_invno_dup(invno varchar,invdate date,sno1 varchar) cascade""")
        self._cr.execute("""create or replace function chk_invno_dup(invno varchar,invdate date,sno1 varchar) returns Boolean as $BODY$
          DECLARE
            myres Boolean ;
            ncount int ;
            ncount1 int ;
            ncount2 int ;
            cusname int ;
          BEGIN
            select count(*) into ncount from neweb_invoice_invoiceopen_line where invoice_no=invno ;
            if ncount > 1 then
               select count(*) into ncount1 from neweb_invoice_invoiceopen_line where invoice_no=invno and invoice_date != invdate ;
               if ncount1 > 0 then
                  myres = TRUE ;  /* 發票號碼有重複  */
               else
                  select count(*) into ncount2 from neweb_invoice_invoiceopen where id in 
                    (select invoice_id from neweb_invoice_invoiceopen_line where invoice_no=invno) and sno != sno1 ;
                  if ncount2 > 0 then
                     myres = TRUE ;
                  else
                     myres = FALSE ;
                  end if ;   
               end if ;
            else
               myres = FALSE ;   
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")




