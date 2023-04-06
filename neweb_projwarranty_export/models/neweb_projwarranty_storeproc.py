# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError

class newebprojwarrantystoreproc(models.Model):
    _name = "neweb.projwarrantystoreproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genprojwarrantyexport(wizid int) cascade""")
        self._cr.execute("""create or replace function genprojwarrantyexport(wizid int) returns void as $BODY$
          DECLARE
            sitem_cur refcursor ;
            sitem_rec record ;
            exp_cur refcursor ;
            exp_rec record ;
            cusid int ;
            mycusname varchar ;
            mysupname varchar ;
            myproject varchar ;
            projsale int ;
            mycount int = 1 ;
            myloc int ;
            mytserial varchar ;
            myserial varchar ;
            myseriallen int ;
            mypickingid int ;
            mymindate date ;
            mymaxid int ;
            myinvoiceid int ;
            myinvoiceno varchar ;
            myinvoicedate date ;
          BEGIN
            delete from neweb_projwarrantyinfo_export ;
            open sitem_cur for select * from neweb_projsaleitem where saleitem_id in 
              (select proj_id from neweb_projwarranty_export_rel where wizard_id=wizid) 
              and prod_set in (1,2,3,4,5,6,10,11) order by saleitem_id;
            loop
               fetch sitem_cur into sitem_rec ;
               exit when not found ;
               select cus_name,name,proj_sale into cusid,myproject,projsale from neweb_project where id = sitem_rec.saleitem_id ;
               select name into mycusname from res_partner where id = cusid ;
               select name into mysupname from res_partner where id = sitem_rec.supplier ;
               mycount = 1 ;
               mytserial = sitem_rec.prod_serial ;
               loop
                 exit when mycount > sitem_rec.prod_num ;
                 if sitem_rec.prod_num > 1 then
                    select position(',' in mytserial) into myloc ;
                    if myloc > 0 then
                       select substring(mytserial,0,myloc) into myserial ;
                       select length(mytserial) into myseriallen ;
                       select substring(mytserial,myloc+1,myseriallen) into mytserial ;
                    else
                       myserial = mytserial ;   
                    end if ;   
                 else  
                    myserial = sitem_rec.prod_serial ; 
                 end if ;
                 insert into neweb_projwarrantyinfo_export(proj_no,cus_name,prod_modeltype,prod_serial,neweb_start_date,neweb_end_date,sale_id,supplier_id) values
                   (myproject,mycusname,sitem_rec.prod_modeltype,myserial,sitem_rec.neweb_start_date,sitem_rec.neweb_end_date,projsale,sitem_rec.supplier) ;
                 mycount = mycount + 1 ;
                 select max(id) into mymaxid from neweb_projwarrantyinfo_export ;
                 select stockship_id into mypickingid from neweb_stockship_list where stockout_sequence_id=sitem_rec.id ;
                 select date_done::DATE into mymindate from stock_picking where id=mypickingid ;
                 if mymindate is not null then
                    update neweb_projwarrantyinfo_export set shipping_date=mymindate where id = mymaxid ;
                 end if ;
                 select id into myinvoiceid from neweb_invoice_invoiceopen where project_no=sitem_rec.saleitem_id ;
                 select invoice_no,invoice_date::DATE into myinvoiceno,myinvoicedate from neweb_invoice_invoiceopen_line where
                    invoice_id=myinvoiceid and invoice_state='3' ;
                 if myinvoiceno is not null then
                    update neweb_projwarrantyinfo_export set invoice_no=myinvoiceno where id=mymaxid ;
                 end if ;   
                 if myinvoicedate is not null then
                    update neweb_projwarrantyinfo_export set invoice_date=myinvoicedate where id=mymaxid ;
                 end if ;
               end loop ;
            end loop ;
            close sitem_cur ;  
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genprojwarrantyexport1(projdesc varchar) cascade""")
        self._cr.execute("""create or replace function genprojwarrantyexport1(projdesc varchar) returns void as $BODY$
          DECLARE
            sitem_cur refcursor ;
            sitem_rec record ;
            exp_cur refcursor ;
            exp_rec record ;
            cusid int ;
            mycusname varchar ;
            mysupname varchar ;
            myproject varchar ;
            projsale int ;
            mycount int = 1 ;
            myloc int ;
            mytserial varchar ;
            myserial varchar ;
            myseriallen int ;
            mypickingid int ;
            mymindate date ;
            mymaxid int ;
            myinvoiceid int ;
            myinvoiceno varchar ;
            myinvoicedate date ;
          BEGIN
            delete from neweb_projwarrantyinfo_export ;
            open sitem_cur for select * from neweb_projsaleitem where saleitem_id in 
              (select id from neweb_project where name like '%'|| projdesc ||'%') 
              and prod_set in (1,2,3,4,5,6,10,11) order by saleitem_id;
            loop
               fetch sitem_cur into sitem_rec ;
               exit when not found ;
               select cus_name,name,proj_sale into cusid,myproject,projsale from neweb_project where id = sitem_rec.saleitem_id ;
               select name into mycusname from res_partner where id = cusid ;
               select name into mysupname from res_partner where id = sitem_rec.supplier ;
               mycount = 1 ;
               mytserial = sitem_rec.prod_serial ;
               loop
                 exit when mycount > sitem_rec.prod_num ;
                 if sitem_rec.prod_num > 1 then
                    select position(',' in mytserial) into myloc ;
                    if myloc > 0 then
                       select substring(mytserial,0,myloc) into myserial ;
                       select length(mytserial) into myseriallen ;
                       select substring(mytserial,myloc+1,myseriallen) into mytserial ;
                    else
                       myserial = mytserial ;   
                    end if ;   
                 else  
                    myserial = sitem_rec.prod_serial ; 
                 end if ;
                 insert into neweb_projwarrantyinfo_export(proj_no,cus_name,prod_modeltype,prod_serial,neweb_start_date,neweb_end_date,sale_id,supplier_id) values
                   (myproject,mycusname,sitem_rec.prod_modeltype,myserial,sitem_rec.neweb_start_date,sitem_rec.neweb_end_date,projsale,sitem_rec.supplier) ;
                 mycount = mycount + 1 ;
                 select max(id) into mymaxid from neweb_projwarrantyinfo_export ;
                 select stockship_id into mypickingid from neweb_stockship_list where stockout_sequence_id=sitem_rec.id ;
                 select date_done::DATE into mymindate from stock_picking where id=mypickingid ;
                 if mymindate is not null then
                    update neweb_projwarrantyinfo_export set shipping_date=mymindate where id = mymaxid ;
                 end if ;
                 select id into myinvoiceid from neweb_invoice_invoiceopen where project_no=sitem_rec.saleitem_id ;
                 select invoice_no,invoice_date::DATE into myinvoiceno,myinvoicedate from neweb_invoice_invoiceopen_line where
                    invoice_id=myinvoiceid and invoice_state='3' ;
                 if myinvoiceno is not null then
                    update neweb_projwarrantyinfo_export set invoice_no=myinvoiceno where id=mymaxid ;
                 end if ;   
                 if myinvoicedate is not null then
                    update neweb_projwarrantyinfo_export set invoice_date=myinvoicedate where id=mymaxid ;
                 end if ;
               end loop ;
            end loop ;
            close sitem_cur ;  
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprojname(wizid int) cascade""")
        self._cr.execute("""create or replace function getprojname(wizid int) returns varchar as $BODY$
           DECLARE
             myres varchar ;
             proj_cur refcursor ;
             proj_rec record ;
           BEGIN
             open proj_cur for select id,name from neweb_project where id in (select proj_id from neweb_projwarranty_export_rel where wizard_id=wizid) ;
             loop
               fetch proj_cur into proj_rec ;
               exit when not found ;
               if myres is null then
                  myres = proj_rec.name ;
               else
                  myres = concat(myres,'/',proj_rec.name) ;
               end if ;
             end loop ;
             close proj_cur ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprojname1(projdesc varchar) cascade""")
        self._cr.execute("""create or replace function getprojname1(projdesc varchar) returns varchar as $BODY$
           DECLARE
             myres varchar ;
             proj_cur refcursor ;
             proj_rec record ;
           BEGIN
             open proj_cur for select id,name from neweb_project where name like '%'|| projdesc ||'%'  ;
             loop
               fetch proj_cur into proj_rec ;
               exit when not found ;
               if myres is null then
                  myres = proj_rec.name ;
               else
                  myres = concat(myres,'/',proj_rec.name) ;
               end if ;
             end loop ;
             close proj_cur ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genengmaintype()""")
        self._cr.execute("""create or replace function genengmaintype() returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update neweb_engmaintype set name='需於公司內作業' where id = 1 ;
            update neweb_engmaintype set name='需於客戶端作業' where id = 2 ;
            select count(*) into ncount from neweb_engmaintype where name='電話支援' ;
            if ncount=0 then
               insert into neweb_engmaintype(name) values ('電話支援') ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")
