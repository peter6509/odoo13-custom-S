# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo import exceptions

class uninvoice_storeproc(models.Model):

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genallpurflowman() cascade""")
        self._cr.execute("""create or replace function genallpurflowman() returns void as $BODY$
          DECLARE
            pur_cur refcursor ;
            pur_rec record ;
          BEGIN
            open pur_cur for select * from neweb_purinv_invoice ;
            loop
              fetch pur_cur into pur_rec ;
              exit when not found ;
              execute genpurinvflowman(pur_rec.id) ;
            end loop ;
            close pur_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpurinvflowman(purid int) cascade""")
        self._cr.execute("""create or replace function genpurinvflowman(purid int) returns void as $BODY$
          DECLARE
            resid int ;
            empid int ;
            userid int;
            flowman1 int ;
            flowman2 int ;
            flowman3 int ;
            flowman4 int ;
          BEGIN
            select create_uid into userid from neweb_purinv_invoice where id = purid ; 
            select id into resid from resource_resource where user_id=userid ;
            if resid is not null then
               select id into empid from hr_employee where resource_id = resid ;
               if empid is not null then
                  update neweb_purinv_invoice set flow_owner=empid where id = purid ;
                  select flow_man1,flow_man2,flow_man3,flow_man4 into flowman1,flowman2,flowman3,flowman4 from hr_employee_postype where emp_id=empid ;
                  if flowman1 is not null then
                     update neweb_purinv_invoice set flow_man1=flowman1,has_man1=1 where id = purid ;
                  end if ;
                  if flowman2 is not null then
                     update neweb_purinv_invoice set flow_man2=flowman2,has_man2=1 where id = purid ;
                  end if ;
                  if flowman3 is not null then
                     update neweb_purinv_invoice set flow_man3=flowman3,has_man3=1 where id = purid ;
                  end if ;
                  if flowman4 is not null then
                     update neweb_purinv_invoice set flow_man4=flowman4,has_man4=1 where id = purid ;
                  end if ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""DROP FUNCTION IF EXISTS getpurinvdata(invopid int,purid int) cascade;""")
        self._cr.execute("""create or replace function getpurinvdata(invopid int,purid int) returns void as $BODY$
            DECLARE
              refcur refcursor;
              refrec record;
              myname purchase_order.name%type;
              myid INTEGER ;
              taxid INTEGER ;
              mypitemid INTEGER ;
              myamount FLOAT ;
              mysupplier INTEGER ;
              myamountuntax FLOAT ;
              myamounttot FLOAT ;
              myinvoiceopen FLOAT ;
              myreqid INTEGER ;
              ncount INTEGER ;
              ncount1 int ;
              mycuspartner INTEGER ;
              mypuramounttot FLOAT ;
              myopenamounttot FLOAT ;
              mycuspartnername VARCHAR ;
              mycurrencyid INTEGER ;
              myrate Float ;
              mytotinvoice FLOAT ;
              myinvoicesum FLOAT ;
              mymaxitemid FLOAT ;
              mypitemspec varchar ;
            BEGIN
              mymaxitemid := 0 ;
              select pitem_amounttot,invoice_openamount,pitem_untax into myamounttot,myinvoiceopen,myamountuntax 
                     from purchase_order where id = purid ;
              open refcur for select * from neweb_pitem_list where pitem_id=purid and 
                   id=(select min(id) from neweb_pitem_list where pitem_id=purid) ;
              select name,taxes_id into myname,taxid from purchase_order where id = purid ;
             select amount into myamount from account_tax where id=taxid ; 
              loop
                fetch refcur into refrec;
                exit when not found;
                if refrec.pitem_origin_type='R' THEN 
                   select id into myreqid from neweb_require_purchase where name=refrec.pitem_origin_no;
                   select count(*) into ncount from neweb_require_purchase_item where pitem_id=myreqid and expense_custom is not null;
                   if ncount >0 THEN 
                      select distinct expense_custom into mycuspartner from neweb_require_purchase_item where pitem_id=myreqid ;
                      select comp_sname into mycuspartnername from res_partner where id=mycuspartner ;
                   end if;  
                ELSE 
                   select cus_name into mycuspartner from neweb_project where name like refrec.pitem_origin_no ;
                   select comp_sname into mycuspartnername from res_partner where id=mycuspartner ;
                END  if;
                select pitem_amounttot,invoice_openamount,partner_id,currency_id into mypuramounttot,myopenamounttot,mysupplier,mycurrencyid from purchase_order where id=purid ;
                mytotinvoice := (mypuramounttot - myopenamounttot) ;
              /*  select coalesce(round(max(invline_item)),0) into mymaxitemid from neweb_purinv_invoiceline where invline_id = invopid ;
                select count(*) into ncount1 from neweb_purinv_invoiceline where invline_id = invopid ;
                if ncount1 = 0 then
                   mymaxitemid = 1 ;
                else   
                   mymaxitemid := mymaxitemid + 1 ;
                end if ; */
                select genforeignpitemmodeltype(purid) into mypitemspec ;
                insert into neweb_purinv_invoiceline(invline_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,invoice_sum,invoice_partner,taxes_id,currency_id) values 
                   (invopid,mypitemspec,mycuspartnername,purid,refrec.pitem_origin_no,mytotinvoice,mysupplier,taxid,mycurrencyid) ;
              end loop;
              select sum(invoice_sum) into myinvoicesum from neweb_purinv_invoiceline where invline_id=invopid; 
              update neweb_purinv_invoice set invoice_total=myinvoicesum where id = invopid;
              close refcur;
            END ;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS genpurinvline(unpurinvid int) cascade;""")
        self._cr.execute("""create or replace function genpurinvline(unpurinvid int) returns void as $BODY$
            declare
               invcur refcursor ;
               invrec record ;
               invid INTEGER ;
               mypurno VARCHAR ;
               mysupplier INTEGER ;
               mytaxid INTEGER ;
               mynewid INTEGER ;
            BEGIN 
               select invitem_id,supplier,prod_tax into invid,mysupplier,mytaxid from neweb_unpurinvitem where id = unpurinvid;
               select name into mypurno from neweb_unpurinv where id=invid ;
               insert into neweb_purinv_invoice(invoice_partner,taxes_id) values (mysupplier,mytaxid) ;
               select max(id) into mynewid from neweb_purinv_invoice ;
               open invcur for select * from neweb_unpurinvitem where id=unpurinvid;
               loop
                 fetch invcur into invrec ;
                 exit when not found;
                  insert into neweb_purinv_invoiceline(invline_id,inv_prodspec,purchase_no,pitem_origin_no,pitem_id,invoice_sum) VALUES 
                      (mynewid,invrec.prod_desc,mypurno,invrec.pitem_origin_no,invrec.purseq_id,invrec.prod_tottax) ;                
               end loop;
               close invcur ;
               
            END;  $BODY$
            LANGUAGE plpgsql ;
            """)

        self._cr.execute("""DROP FUNCTION IF EXISTS getinvid(unpurinvid int) cascade;""")
        self._cr.execute("""create or replace function getinvid(unpurinvid int) returns INTEGER as $BODY$
            DECLARE 
              myinvid INTEGER ;
            BEGIN 
              select max(id) into myinvid from neweb_purinv_invoice ;
              return myinvid ;
            END ;$BODY$
            LANGUAGE plpgsql;
               """)

        self._cr.execute("""drop function if exists checkpurapselect(purid int) cascade;""")
        self._cr.execute("""create or replace function checkpurapselect(purid int) returns void as $BODY$
            DECLARE 
               ncount INTEGER ;
            BEGIN 
               select count(*) into ncount from neweb_pitem_list where pitem_id=purid and (ap_select=FALSE or ap_select is null);
               if ncount > 0 THEN
                  update purchase_order set invoiceok=FALSE  where id = purid ;
               ELSE 
                  update purchase_order set invoiceok=TRUE  where id = purid ;
               END if;
            END ; $BODY$
            LANGUAGE plpgsql; 
                 """)

        self._cr.execute("""drop function if exists updateapselect(pitemid int,aptype Boolean) cascade;""")
        self._cr.execute("""create or replace function updateapselect(pitemid int,aptype Boolean) returns void as $BODY$
            DECLARE 
               ncount INTEGER ;
            BEGIN 
               select count(*) into ncount from neweb_pitem_list where pitem_id=pitemid;
               if ncount > 0 THEN 
                  update neweb_pitem_list set ap_select=aptype where pitem_id=pitemid ;
               END if ;
            END ;$BODY$
            LANGUAGE plpgsql;   """)


        self._cr.execute("""drop function if exists get_invoicedate(invlineid int) cascade""")
        self._cr.execute("""create or replace function get_invoicedate(invlineid int) returns void as $BODY$
              DECLARE
                 purid INTEGER ;
                 paymentid INTEGER ;
                 termid INTEGER ;
                 termdays INTEGER ;
                 ncount INTEGER ;
                 invdate DATE ;
                 myinvday CHAR(2) ;
                 myinvmonth CHAR(2) ;
                 myinvyear CHAR(4);
                 cinvyear CHAR(4);
                 cinvmonth CHAR(2);
                 cinvday CHAR(2);
                 calmonthday TIMESTAMP ;
                 mymainymd DATE ;
                 mynumber INTEGER ;
                 mynumber1 INTEGER ;
                 mypayterm varchar;
                 mypaytermday int ;
                 mypartnerid int;
              BEGIN
                 select purchase_no,invoice_date into purid,invdate from neweb_purinv_invoiceline where id=invlineid ;     
                 select payment_term_id,pay_term,partner_id into paymentid,mypayterm,mypartnerid from purchase_order where id=purid ;  
                 select nullif(mypayterm,'')::int into termdays ;     
                 select EXTRACT (DAY FROM invdate) into myinvday ;
                 select to_number(myinvday,'99') into mynumber;
                 if mynumber > 20 THEN 
                    select date_trunc('day',invdate + interval '1 month') into calmonthday;
                    select date_trunc('month',calmonthday) into mymainymd ;
                    if termdays = 30 then
                       select (mymainymd::DATE + interval '2 month')::DATE  into mymainymd ;
                    elsif termdays = 45 then
                       select (mymainymd::DATE + interval '2 month' + interval '14 days')::DATE  into mymainymd ;
                    elsif termdays = 60 then
                       select (mymainymd::DATE + interval '3 month')::DATE  into mymainymd ;
                    elsif termdays = 90 then
                       select (mymainymd::DATE + interval '4 month')::DATE  into mymainymd ;
                    elsif termdays = 120 then
                       select (mymainymd::DATE + interval '5 month')::DATE  into mymainymd ;
                    else
                       select (mymainymd::DATE + interval '1 month')::DATE + termdays into mymainymd ;
                    end if ;
                    select date_trunc('day',mymainymd) into calmonthday;
                    select calmonthday::DATE - 1 into calmonthday ;
                    select to_char(extract (day from calmonthday),'FM99') into cinvday ;
                    select to_number(cinvday,'99') into mynumber1 ;
                   if mynumber1 > 15 THEN 
                       select date_trunc('month',calmonthday + interval '1 month') into calmonthday;
                       select calmonthday::DATE - 1 into calmonthday ;
                    ELSE 
                       select date_trunc('month',calmonthday) into calmonthday;
                       select calmonthday::DATE + 14 into calmonthday;
                    end if;
                   
                 ELSE 
                    select date_trunc('month',invdate::DATE + interval '1 month') into invdate ; 
                    if termdays = 30 then
                        select date_trunc('day',invdate)::DATE + interval '1 month' into calmonthday;
                    elsif termdays = 45 then
                        select date_trunc('day',invdate)::DATE + interval '1 month' + interval '14 days' into calmonthday;
                    elsif termdays = 60 then
                        select date_trunc('day',invdate)::DATE + interval '2 month' into calmonthday;
                    elsif termdays = 90 then
                        select date_trunc('day',invdate)::DATE + interval '3 month' into calmonthday;
                    elsif termdays = 120 then
                        select date_trunc('day',invdate)::DATE + interval '4 month' into calmonthday;
                    else
                        select date_trunc('day',invdate)::DATE + termdays into calmonthday;
                    end if ;
                    select calmonthday::DATE - 1 into calmonthday ;
                    select to_char(extract (day from calmonthday),'FM99') into cinvday ;
                    select to_number(cinvday,'99') into mynumber1 ;
                    if mynumber1 > 15 THEN 
                       select date_trunc('month',calmonthday + interval '1 month') into calmonthday;
                       select calmonthday::DATE - 1 into calmonthday ;
                    ELSE 
                       select date_trunc('month',calmonthday) into calmonthday;
                       select calmonthday::DATE + 14 into calmonthday;
                    end if;
                    
                 end if;
                 if invdate is not null then
                    update neweb_purinv_invoiceline set inv_paymentterm=calmonthday where id=invlineid and inv_paymentterm is null;
                 end if ;   
              END;$BODY$
              LANGUAGE plpgsql;
                 """)

        self._cr.execute("""drop function if exists get_invoicedate1(invlineid int) cascade""")
        self._cr.execute("""create or replace function get_invoicedate1(invlineid int) returns DATE as $BODY$
          DECLARE
             purid INTEGER ;
             paymentid INTEGER ;
             termid INTEGER ;
             termdays INTEGER ;
             ncount INTEGER ;
             invdate DATE ;
             myinvday CHAR(2) ;
             myinvmonth CHAR(2) ;
             myinvyear CHAR(4);
             cinvyear CHAR(4);
             cinvmonth CHAR(2);
             cinvday CHAR(2);
             calmonthday TIMESTAMP ;
             mymainymd DATE ;
             mynumber INTEGER ;
             mynumber1 INTEGER ;
             mypayterm varchar;
             mypaytermday int ;
             mypartnerid int;
          BEGIN
             select purchase_no,invoice_date into purid,invdate from neweb_purinv_invoiceline where id=invlineid ;     
             select payment_term_id,pay_term,partner_id into paymentid,mypayterm,mypartnerid from purchase_order where id=purid ;  
             select nullif(mypayterm,'')::int into termdays ;     
             select EXTRACT (DAY FROM invdate) into myinvday ;
             select to_number(myinvday,'99') into mynumber;
             if mynumber > 20 THEN 
                select date_trunc('day',invdate + interval '1 month') into calmonthday;
                select date_trunc('month',calmonthday) into mymainymd ;
                if termdays = 30 then
                   select (mymainymd::DATE + interval '2 month')::DATE  into mymainymd ;
                elsif termdays = 45 then
                   select (mymainymd::DATE + interval '2 month' + interval '14 days')::DATE  into mymainymd ;
                elsif termdays = 60 then
                   select (mymainymd::DATE + interval '3 month')::DATE  into mymainymd ;
                elsif termdays = 90 then
                   select (mymainymd::DATE + interval '4 month')::DATE  into mymainymd ;
                elsif termdays = 120 then
                   select (mymainymd::DATE + interval '5 month')::DATE  into mymainymd ;
                else
                   select (mymainymd::DATE + interval '1 month')::DATE + termdays into mymainymd ;
                end if ;
                select date_trunc('day',mymainymd) into calmonthday;
                select calmonthday::DATE - 1 into calmonthday ;
                select to_char(extract (day from calmonthday),'FM99') into cinvday ;
                select to_number(cinvday,'99') into mynumber1 ;
               if mynumber1 > 15 THEN 
                   select date_trunc('month',calmonthday + interval '1 month') into calmonthday;
                   select calmonthday::DATE - 1 into calmonthday ;
                ELSE 
                   select date_trunc('month',calmonthday) into calmonthday;
                   select calmonthday::DATE + 14 into calmonthday;
                end if;

             ELSE 
                select date_trunc('month',invdate::DATE + interval '1 month') into invdate ; 
                if termdays = 30 then
                    select date_trunc('day',invdate)::DATE + interval '1 month' into calmonthday;
                elsif termdays = 45 then
                    select date_trunc('day',invdate)::DATE + interval '1 month' + interval '14 days' into calmonthday;
                elsif termdays = 60 then
                    select date_trunc('day',invdate)::DATE + interval '2 month' into calmonthday;
                elsif termdays = 90 then
                    select date_trunc('day',invdate)::DATE + interval '3 month' into calmonthday;
                elsif termdays = 120 then
                    select date_trunc('day',invdate)::DATE + interval '4 month' into calmonthday;
                else
                    select date_trunc('day',invdate)::DATE + termdays into calmonthday;
                end if ;
                select calmonthday::DATE - 1 into calmonthday ;
                select to_char(extract (day from calmonthday),'FM99') into cinvday ;
                select to_number(cinvday,'99') into mynumber1 ;
                if mynumber1 > 15 THEN 
                   select date_trunc('month',calmonthday + interval '1 month') into calmonthday;
                   select calmonthday::DATE - 1 into calmonthday ;
                ELSE 
                   select date_trunc('month',calmonthday) into calmonthday;
                   select calmonthday::DATE + 14 into calmonthday;
                end if;

             end if;
             return calmonthday ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists complete_invoice(invid int) cascade""")
        self._cr.execute("""create or replace function complete_invoice(invid int) returns void as $BODY$
             DECLARE
               refcur refcursor;
               refrec record;
               ncount INTEGER ;
               invoicesum FLOAT ;
               purid INTEGER ;
               pitemamounttot FLOAT;
               invoiceamounttot FLOAT;
             BEGIN 
               open refcur for select * from neweb_purinv_invoiceline where invline_id=invid ;
               loop
                 fetch refcur into refrec ;
                 exit when not found;
                 update purchase_order set invoice_mark=TRUE,invoice_openamount=invoice_openamount+refrec.invoice_sum,invoice_time=invoice_time + 1
                   where id=refrec.purchase_no ;
                 update purchase_order set invoice_complete=TRUE where id=refrec.purchase_no and invoice_openamount >= pitem_amounttot ;
               end loop;
               close refcur;
             END ;$BODY$
             LANGUAGE plpgsql;
             """)

        self._cr.execute("""drop function if exists invlineitem(purinvid int) cascade;""")
        self._cr.execute("""create or replace function invlineitem(purinvid int) returns void as $BODY$
                DECLARE 
                  ncount int;
                  invline_cur refcursor ;
                  invline_rec record ;
                  myitem int ;
                BEGIN
                     myitem := 1 ; 
                     open invline_cur for select id from neweb_purinv_invoiceline where invline_id = purinvid order by invline_item ;
                     loop
                       fetch invline_cur into invline_rec ;
                       exit when not found ;
                       update neweb_purinv_invoiceline set invline_item=myitem where id = invline_rec.id ;
                       myitem = myitem + 1 ;
                     end loop ;
                     close invline_cur ;
                END;$BODY$
                LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists allpurinvitem() cascade;""")
        self._cr.execute("""create or replace function allpurinvitem() returns void as $BODY$
            DECLARE 
              ncount int ;
              pur_cur refcursor ;
              pur_rec record ;
              line_cur refcursor ;
              line_rec record ;
              myitem int ;
            BEGIN 
              open pur_cur for select id from neweb_purinv_invoice ;
              loop
                fetch pur_cur into pur_rec ;
                exit when not found ;
                myitem := 1 ;
                open line_cur for select id from neweb_purinv_invoiceline where invline_id = pur_rec.id order by sequence ;
                loop
                  fetch line_cur into line_rec ;
                  exit when not found ;
                  update neweb_purinv_invoiceline set invline_item=myitem where id = line_rec.id ;
                  myitem := myitem + 1 ;
                end loop ;
                close line_cur ;
              end loop ;
              close pur_cur ;  
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genforeignpitemmodeltype(purid int) cascade""")
        self._cr.execute("""create or replace function genforeignpitemmodeltype(purid int) returns varchar as $BODY$
           DECLARE
             myres varchar ;
             ncount int ;
             pitem_cur refcursor ;
             pitem_rec record ;
             originno varchar ;
             cpitemnum varchar ;
           BEGIN
             select count(*) into ncount from purchase_order where id = purid and foreign_purchase = True ;
              myres := '' ;
             if ncount > 0 then
                open pitem_cur for select pitem_id,pitem_model_type,pitem_num,pitem_origin_no,id,sequence from neweb_pitem_list where pitem_id=purid 
                   order by sequence,id ;
                originno := '' ;   
                loop
                   fetch pitem_cur into pitem_rec ;
                   exit when not found ;
                   if originno != pitem_rec.pitem_origin_no then
                      if originno = '' then
                         myres = concat('(',pitem_rec.pitem_origin_no,'):',trim(pitem_rec.pitem_model_type),'*',trim(pitem_rec.pitem_num::integer::TEXT)) ;
                      else
                         myres = concat(trim(myres),'   ','(',pitem_rec.pitem_origin_no,'):',trim(pitem_rec.pitem_model_type),'*',trim(pitem_rec.pitem_num::integer::TEXT)) ;
                      end if ;   
                      
                   else
                      myres = concat(trim(myres),',',trim(pitem_rec.pitem_model_type),'*',trim(pitem_rec.pitem_num::integer::TEXT)) ;
                   end if ;
                   originno = pitem_rec.pitem_origin_no ;
                end loop ;
                close pitem_cur ;   
             else
                select coalesce(pitem_spec,' ') into myres from neweb_pitem_list where pitem_id=purid and id =
                 (select min(id) from neweb_pitem_list where pitem_id=purid) ;
             end if ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
             """)



