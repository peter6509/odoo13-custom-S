# -*- coding: utf-8 -*-
# Author : Peter Wu



from odoo import models,fields,api
from odoo.exceptions import UserError


class newebchiinvoicingstoreproc(models.Model):
    _name = "neweb_chi_invoicing.store_proc"


    @api.model
    def init(self):
       self._cr.execute("""drop function if exists genprojinvoicing(projid int) cascade""")
       self._cr.execute("""create or replace function genprojinvoicing(projid int) returns void as $BODY$
          DECLARE
            ncount int ;
            ncount1 int ;
          BEGIN
            select count(*) into ncount from neweb_project where id = projid ;
            select count(*) into ncount1 from neweb_chi_invoicing_excel_download where project_no=projid ;
            if ncount > 0 and ncount1 = 0 then
               insert into neweb_chi_invoicing_excel_download(project_no) values (projid) ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")


       self._cr.execute("""drop function if exists genprojchiprodno(projid int) cascade""")
       self._cr.execute("""create or replace function genprojchiprodno(projid int) returns void as $BODY$
          DECLARE
            code_len int ;
            myyear varchar ;
            myyear1 varchar ;
            mysname varchar ;
            mychiseq int ;
            mychiseqid int ;
            ncount int ;
            ncount1 int ;
            mychiprodcode varchar ;
            proj_cur refcursor ;
            proj_rec record ;
            mysnamelen int ;
            descpid int ;
          BEGIN
            select max(id) into descpid from neweb_costtype where name ilike '%說明%' ;
            open proj_cur for select id,prod_set,create_date,cost_type from neweb_projsaleitem where saleitem_id=projid and chi_product_no is null and 
                 not_chiout != True and prod_set is not null and create_date is not null ;
            loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                if proj_rec.cost_type=3 then   /* 建置 */
                   update neweb_projsaleitem set chi_product_no='ZZC00000001' where id = proj_rec.id ;
                elsif proj_rec.cost_type=2 then   /* 專案合作 */
                   update neweb_projsaleitem set chi_product_no='ZZA00000001' where id = proj_rec.id ;
                elsif proj_rec.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                   update neweb_projsaleitem set chi_product_no='ZZB00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=5 then   /* 維運人力 */
                   update neweb_projsaleitem set chi_product_no='ZZD00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=7 then   /* 租賃 */
                   update neweb_projsaleitem set chi_product_no='ZZE00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=11 then   /* 行銷獎勵 */
                   update neweb_projsaleitem set chi_product_no='ZZG00000001' where id = proj_rec.id ; 
                elsif proj_rec.cost_type in (6,8) then   /* 利息,其他 */
                   update neweb_projsaleitem set chi_product_no='ZZH00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=12 then   /* 保固維護 */
                  update neweb_projsaleitem set chi_product_no='ZZW00000001' where id = proj_rec.id  ; 
                elsif proj_rec.cost_type=descpid then   /* 說明 */
                  update neweb_projsaleitem set chi_product_no='ZZI00000001' where id = proj_rec.id  ;          
                else
                   select date_part('year',proj_rec.create_date::DATE)::TEXT into myyear ;
                   select substring(myyear,3,2) into myyear1 ;
                   select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                   select length(mysname) into code_len ;
                   select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                   if ncount > 0 then
                      select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                      select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                      update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                      update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                   else
                      select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                      update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                      insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                   end if ; 
                end if ;   
            end loop ;
            close proj_cur ;  
            open proj_cur for select id,prod_set,create_date,chi_product_no,cost_type from neweb_projsaleitem where saleitem_id=projid and prod_set is not null and create_date is not null
                and not_chiout != True;
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              if proj_rec.cost_type=3 then
                  update neweb_projsaleitem set chi_product_no='ZZC00000001' where id = proj_rec.id and chi_product_no != 'ZZC00000001' ;
              elsif proj_rec.cost_type=2 then   /* 專案合作 */
                   update neweb_projsaleitem set chi_product_no='ZZA00000001' where id = proj_rec.id and chi_product_no != 'ZZA00000001';
              elsif proj_rec.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                  update neweb_projsaleitem set chi_product_no='ZZB00000001' where id = proj_rec.id and chi_product_no != 'ZZB00000001' ;   
              elsif proj_rec.cost_type=5 then   /* 維運人力 */
                  update neweb_projsaleitem set chi_product_no='ZZD00000001' where id = proj_rec.id and chi_product_no != 'ZZD00000001' ;   
              elsif proj_rec.cost_type=7 then   /* 租賃 */
                  update neweb_projsaleitem set chi_product_no='ZZE00000001' where id = proj_rec.id and chi_product_no != 'ZZE00000001' ;   
              elsif proj_rec.cost_type=11 then   /* 行銷獎勵 */
                  update neweb_projsaleitem set chi_product_no='ZZG00000001' where id = proj_rec.id and chi_product_no != 'ZZG00000001' ; 
              elsif proj_rec.cost_type in (6,8) then   /* 利息,其他 */
                  update neweb_projsaleitem set chi_product_no='ZZH00000001' where id = proj_rec.id and chi_product_no != 'ZZH00000001' ;   
              elsif proj_rec.cost_type=12 then   /* 保固維護 */
                  update neweb_projsaleitem set chi_product_no='ZZW00000001' where id = proj_rec.id and chi_product_no != 'ZZW00000001' ;  
              elsif proj_rec.cost_type=descpid then   /* 說明 */
                  update neweb_projsaleitem set chi_product_no='ZZI00000001' where id = proj_rec.id and chi_product_no != 'ZZI00000001'  ;         
              else   
                 select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                 select length(trim(mysname)) into mysnamelen ;
                 if mysnamelen > 0 and substring(proj_rec.chi_product_no,1,mysnamelen) != mysname then
                    select date_part('year',proj_rec.create_date::DATE)::TEXT into myyear ;
                    select substring(myyear,3,2) into myyear1 ;
                    select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                    select length(mysname) into code_len ;
                    select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                    if ncount > 0 then
                       select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                       select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                       update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                    else
                       select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                       insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                    end if ; 
                 end if ;
              end if ;   
            end loop ;
            close proj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")



       self._cr.execute("""drop function if exists gen_chi_export_proj(mystartdate date,myenddate date,exportuser int) cascade""")
       self._cr.execute("""create or replace function gen_chi_export_proj(mystartdate date,myenddate date,exportuser int) returns void as $BODY$
          DECLARE
            proj_cur refcursor ;
            proj_rec record ;
            mymaxid int ;
            mynowdate date ;
            myinvcomplete Boolean ;
          BEGIN
            myinvcomplete := False ; 
            select now()::DATE into mynowdate ; 
            delete from neweb_chi_invoicing_un_export_proj ;
            insert into neweb_chi_invoicing_un_export_proj(export_date,export_user) values (mynowdate,exportuser) ;
            select max(id) into mymaxid from neweb_chi_invoicing_un_export_proj ;
            open proj_cur for select * from neweb_project where create_date between mystartdate::DATE and myenddate::DATE ;
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              insert into neweb_chi_invoicing_un_export_proj_line(export_id,proj_no,partner_id,amount_untaxed,amount_tax,amount_total,chi_export_project,chi_export_product,chi_export_outcome,
                 chi_export_income,chi_invoice_complete) values (mymaxid,proj_rec.id,proj_rec.cus_name,proj_rec.total_saleitem,proj_rec.total_saleitem_tax,proj_rec.total_saleitem_amount,
                 proj_rec.chi_export_project,proj_rec.chi_export_product,proj_rec.chi_export_outcome,proj_rec.chi_export_income,myinvcomplete) ;
              
            end loop ;
            close proj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute(
           """drop function if exists gen_chi_export_proj1(myprojid int,exportuser int) cascade""")
       self._cr.execute("""create or replace function gen_chi_export_proj1(myprojid int,exportuser int) returns void as $BODY$
            DECLARE
              proj_cur refcursor ;
              proj_rec record ;
              mymaxid int ;
              mynowdate date ;
              myinvcomplete Boolean ;
            BEGIN
              myinvcomplete := False ; 
              select now()::DATE into mynowdate ; 
              delete from neweb_chi_invoicing_un_export_proj ;
              insert into neweb_chi_invoicing_un_export_proj(export_date,export_user) values (mynowdate,exportuser) ;
              select max(id) into mymaxid from neweb_chi_invoicing_un_export_proj ;
              open proj_cur for select * from neweb_project where id = myprojid ;
              loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                insert into neweb_chi_invoicing_un_export_proj_line(export_id,proj_no,partner_id,amount_untaxed,amount_tax,amount_total,chi_export_project,chi_export_product,chi_export_outcome,
                   chi_export_income,chi_invoice_complete,selectyn) values (mymaxid,proj_rec.id,proj_rec.cus_name,proj_rec.total_saleitem,proj_rec.total_saleitem_tax,proj_rec.total_saleitem_amount,
                   proj_rec.chi_export_project,proj_rec.chi_export_product,proj_rec.chi_export_outcome,proj_rec.chi_export_income,myinvcomplete,True) ;

              end loop ;
              close proj_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")


       self._cr.execute("""drop function if exists getprojmemo(projid int) cascade""")
       self._cr.execute("""create or replace function getprojmemo(projid int) returns varchar as $BODY$
            DECLARE
               myres varchar ;
               ncount int ;
            BEGIN
               select count(*) into ncount from neweb_chi_invoicing_un_export_proj_line where proj_no=projid ;
               if ncount > 0 then
                  select coalesce(export_memo,' ') into myres from neweb_chi_invoicing_un_export_proj_line where proj_no=projid ;
               else
                  myres = ' ' ;
               end if ;
               return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getexportempid(userid int) cascade""")
       self._cr.execute("""create or replace function getexportempid(userid int) returns int as $BODY$
            DECLARE
              ncount int ;
              myres int ; 
              myresourceid int ;
            BEGIN
             select count(*) into ncount from resource_resource where user_id=userid ;
             if ncount > 0 then
                select id into myresourceid from resource_resource where user_id=userid ;
                select id into myres from hr_employee where resource_id=myresourceid ;
             else
                myres = 0 ;   
             end if ;
             return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")


       self._cr.execute("""drop function if exists genincomeoutcomeno(purid int) cascade""")
       self._cr.execute("""create or replace function genincomeoutcomeno(purid int) returns void as $BODY$
          DECLARE
            proj_cur refcursor ;
            proj_rec record ;
            pitem_cur refcursor ;
            pitem_rec record ;
            saleitem_cur refcursor ;
            saleitem_rec record ;
            projno varchar ;
            myyear varchar ;
            mymonth varchar ;
            myday varchar ;
            ncount int ;
            ncount1 int ;
            ncount2 int ;
            mysname varchar ;
            myseq int ;
            myseqid int ;
            mychipurno varchar ;
            mychisaleno varchar ;
            mydateorder date ;
            myincomedate date ;
            myinvid int ;
            mysuppid int ;
            mycurrencyid int ;
            myvat varchar ;
            mycurrency varchar ;
            myproject varchar ;
            mypaymentdate date ;
            myproduct varchar ;
            mypo varchar ;
            mypi varchar ;
            mycusid int ;
            mysaleid int ;
            myprojname varchar ;
            myoutcomedate date ;
            mysaleno varchar ;
            mypurdateorder date ;
            mypitemid int ;
            purchaseno varchar ;
            myinvoicedate date ;
            mychipurchaseno varchar;
          BEGIN
            select report_date into myinvoicedate from neweb_purinv_invoice where id =
              (select max(invline_id) from neweb_purinv_invoiceline where purchase_no=purid) ;
            myinvoicedate := myinvoicedate + interval '8 hours' ;
            mysname = 'income' ;
            select date_part('year',myinvoicedate)::TEXT into myyear ;
            select lpad(date_part('month',myinvoicedate)::TEXT,2,'0') into mymonth ;
            select lpad(date_part('day',myinvoicedate)::TEXT,2,'0') into myday ;
            mypo = ' ' ;
            select name into purchaseno from purchase_order where id = purid ;
            /* open proj_cur for select id,chi_product_no,purchase_no,saleitem_id,not_chiout from neweb_projsaleitem where id in 
               (select pitem_origin_id from neweb_pitem_list where pitem_id=purid and pitem_origin_type='P' and ap_select=True ) 
               and not_chiout != True order by id ; */
            open proj_cur for select id,chi_product_no,purchase_no,saleitem_id,not_chiout from neweb_projsaleitem where id in 
               (select pitem_origin_id from neweb_pitem_list where pitem_id=purid and pitem_origin_type='P') 
               and not_chiout != True order by id ;
            loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                 select pitem_id,chi_purchase_no into mypitemid,mychipurchaseno from neweb_pitem_list where pitem_origin_id = proj_rec.id ;
                 select date_order into mypurdateorder from purchase_order where id = mypitemid ;
                 if mypo = ' ' and mychipurchaseno is null then
                    select count(*) into ncount1 from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                         and chi_sname=mysname ;
                    if ncount1 > 0 then
                       select id,chi_seq into myseqid,myseq from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                         and chi_sname=mysname ;
                       mychipurno = concat('B',myyear,mymonth,myday,lpad(myseq::TEXT,3,'0')) ; 
                       update neweb_chi_invoicing_incomeoutcome_seq set chi_seq = chi_seq + 1 where id = myseqid ;
                    else
                       mychipurno = concat('B',myyear,mymonth,myday,'001') ; 
                       insert into neweb_chi_invoicing_incomeoutcome_seq (chi_year,chi_month,chi_day,chi_sname,chi_seq) values (myyear,mymonth,myday,mysname,2) ;
                    end if ;  
                 else
                    if mychipurchaseno is not null then
                       mychipurno := mychipurchaseno ;   
                    end if ;   
                 end if ;   
                 mypo = proj_rec.purchase_no ;   
                 select coalesce(cus_order,' ') into mypi from neweb_project where id = proj_rec.saleitem_id ;
                 open pitem_cur for select * from neweb_pitem_list where pitem_origin_id=proj_rec.id order by sequence,id ;
                 loop
                   fetch pitem_cur into pitem_rec ;
                   exit when not found ;
                   select partner_id,currency_id into mysuppid,mycurrencyid from purchase_order where id = pitem_rec.pitem_id ;
                   select coalesce(vat,'No Set') into myvat from res_partner where id = mysuppid ;
                   select name into mycurrency from res_currency where id = mycurrencyid ;
                   if mycurrency = 'TWD' then
                      mycurrency = 'NTD' ;
                   end if ;
                   if mycurrency = 'CNY' then
                      mycurrency = 'RMB' ;
                   end if ;
                   select name into myproject from neweb_project where id = proj_rec.saleitem_id ;
                   myproduct = proj_rec.chi_product_no ; 
                   select invline_id,inv_paymentterm into myinvid,mypaymentdate from neweb_purinv_invoiceline where purchase_no=pitem_rec.pitem_id ;
                   select report_date into myincomedate from neweb_purinv_invoice where id = myinvid ;
                   if pitem_rec.chi_purchase_no is null then
                      insert into neweb_chi_invoicing_export_purchase_log (chi_purchase_no,chi_income_date,chi_income_cdate,chi_purchase_vat,chi_currency_type,chi_wh,chi_project_no,chi_product,
                        chi_purchase_num,chi_purchase_price,chi_origin_id,proj_no,chi_purchase_name,chi_purchase_sup,purchase_seq,pitem_id) values (purid,myinvoicedate,myinvoicedate::TEXT,myvat,mycurrency,'001',myproject,myproduct,
                        pitem_rec.pitem_num,pitem_rec.pitem_price,pitem_rec.id,proj_rec.saleitem_id,mychipurno,mysuppid,pitem_rec.sequence,pitem_rec.id) ;
                        
                      if mypaymentdate is not null then
                         update neweb_chi_invoicing_export_purchase_log set chi_paymentdate = mypaymentdate,chi_cpaymentdate = mypaymentdate::TEXT,pitem_id=pitem_rec.id where chi_origin_id = pitem_rec.id ;
                      end if ;
                   else
                      update neweb_chi_invoicing_export_purchase_log set chi_paymentdate = mypaymentdate,chi_cpaymentdate = mypaymentdate::TEXT,chi_income_date=myinvoicedate,chi_income_cdate=myinvoicedate::TEXT,chi_purchase_vat=myvat,chi_currency_type=mycurrency,
                         chi_product=myproduct,chi_purchase_num=pitem_rec.pitem_num,chi_purchase_price=pitem_rec.pitem_price,chi_purchase_sup=mysuppid,pitem_id=pitem_rec.id where chi_origin_id = pitem_rec.id ;
                   end if ;   
                   update neweb_pitem_list set chi_purchase_no=mychipurno  where id = pitem_rec.id ;
                 end loop ;
                 close pitem_cur ;
            end loop ;
            close proj_cur ;  
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genincomeoutcomeno1(projid int) cascade""")
       self._cr.execute("""create or replace function genincomeoutcomeno1(projid int) returns void as $BODY$
          DECLARE
            saleitem_cur refcursor ;
            saleitem_rec record ;
            projno varchar ;
            myyear varchar ;
            mymonth varchar ;
            myday varchar ;
            ncount int ;
            ncount1 int ;
            ncount2 int ;
            mysname varchar ;
            myseq int ;
            myseqid int ;
            mychipurno varchar ;
            mychisaleno varchar ;
            mydateorder date ;
            myinvid int ;
            mysuppid int ;
            mycurrencyid int ;
            myvat varchar ;
            mycurrency varchar ;
            myproject varchar ;
            mypaymentdate date ;
            myproduct varchar ;
            mypi varchar ;
            mycusid int ;
            mysaleid int ;
            myprojname varchar ;
            myoutcomedate date ;
            mysaleno varchar ;
            myoutpaymentdate date ;
            myprojdate date ;
            myinvoicedate date ;
            mychisaleno1 varchar ;
            myothermemo varchar ;
          BEGIN
            mysname = 'outcome' ;  
            /* 產生正航銷售單號 */
            select coalesce(other_memo,' ') into myothermemo from neweb_invoice_invoiceopen where project_no=projid ;
            select max(invoice_date) into myinvoicedate from neweb_invoice_invoiceopen_line where invoice_id in (select id from neweb_invoice_invoiceopen where project_no=projid) ;
            if myinvoicedate is not null then
               select create_date into myprojdate from neweb_project where id = projid ;
               select date_part('year',myinvoicedate)::TEXT into myyear ;
               select lpad(date_part('month',myinvoicedate)::TEXT,2,'0') into mymonth ;
               select lpad(date_part('day',myinvoicedate)::TEXT,2,'0') into myday ;
               select count(*) into ncount1 from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                           and chi_sname=mysname ;
               select max(chi_sales_no) into mychisaleno1 from  neweb_projsaleitem where saleitem_id=projid ;
               if mychisaleno1 is null then          
                  if ncount1 > 0 then
                      select id,chi_seq into myseqid,myseq from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                        and chi_sname=mysname ;
                      mychisaleno = concat('A',myyear,mymonth,myday,lpad(myseq::TEXT,3,'0')) ; 
                      update neweb_chi_invoicing_incomeoutcome_seq set chi_seq = chi_seq + 1 where id = myseqid ;
                  else 
                      mychisaleno = concat('A',myyear,mymonth,myday,'001') ;
                      insert into neweb_chi_invoicing_incomeoutcome_seq (chi_year,chi_month,chi_day,chi_sname,chi_seq) values (myyear,mymonth,myday,mysname,2) ;
                  end if ; 
               else
                  if mychisaleno1 is not null then
                     mychisaleno := mychisaleno1 ;
                  end if ;   
               end if ;   
               /* 產生未出貨明細記錄  */      
               open saleitem_cur for select * from neweb_projsaleitem where saleitem_id=projid and not_chiout != True order by id ;
               loop
                  fetch saleitem_cur into saleitem_rec ;
                  exit when not found ;
                  select cus_name,proj_sale,name,coalesce(cus_order,' ') into mycusid,mysaleid,myproject,mypi from neweb_project where id = saleitem_rec.saleitem_id ;
                  select coalesce(employee_num,' ') into mysaleno from hr_employee where id = mysaleid ;
                  select coalesce(vat,'No Set') into myvat from res_partner where id = mycusid ;
                  select name into mycurrency from res_currency where id = mycurrencyid ;
                  mycurrency = 'NTD' ;
                  myproduct = saleitem_rec.chi_product_no ; 
                  if saleitem_rec.chi_sales_no is null then
                     insert into neweb_chi_invoicing_export_sales_log (chi_sales_no,chi_sales_vat,chi_currency_type,proj_sale_name,chi_wh,chi_project_no,chi_cus_order,
                     chi_product,chi_sales_num,chi_sales_price,chi_origin_id,proj_no,proj_sale,chi_sale_memo,saleitem_seq) values (mychisaleno,myvat,mycurrency,mysaleno,'001',myproject,mypi,myproduct,
                     saleitem_rec.prod_num,saleitem_rec.prod_revenue,saleitem_rec.id,projid,mysaleid,myothermemo,saleitem_rec.id) ;
                     select getoutcomedate(saleitem_rec.saleitem_id) into myoutcomedate ;   
                     if myoutcomedate is not null then
                        update neweb_chi_invoicing_export_sales_log set chi_outcome_date = myoutcomedate,chi_outcome_cdate = myoutcomedate::TEXT where chi_origin_id = saleitem_rec.id ;
                     end if ;
                     select getoutpaymentdate(projid) into myoutpaymentdate ;
                     if myoutpaymentdate is not null then
                        update neweb_chi_invoicing_export_sales_log set chi_paymentdate = myoutpaymentdate,chi_cpaymentdate = myoutpaymentdate::TEXT where chi_origin_id = saleitem_rec.id ;
                     end if ;
                  else
                     /* 20200901 update chi_sales_no=mychisaleno */
                     update neweb_chi_invoicing_export_sales_log set chi_sales_vat=myvat,chi_currency_type=mycurrency,proj_sale_name=mysaleno,chi_project_no=myproject,chi_cus_order=mypi,proj_sale=mysaleid,chi_sale_memo=myothermemo,
                       chi_product=myproduct,chi_sales_num=saleitem_rec.prod_num,chi_sales_price=saleitem_rec.prod_revenue,chi_sales_no=mychisaleno,proj_no=projid,saleitem_seq=saleitem_rec.id  where chi_origin_id=saleitem_rec.id ;
                     select getoutcomedate(saleitem_rec.saleitem_id) into myoutcomedate ;   
                     if myoutcomedate is not null then
                        update neweb_chi_invoicing_export_sales_log set chi_outcome_date = myoutcomedate,chi_outcome_cdate = myoutcomedate::TEXT where chi_origin_id = saleitem_rec.id ;
                     end if ;
                     select getoutpaymentdate(projid) into myoutpaymentdate ;
                     if myoutpaymentdate is not null then
                        update neweb_chi_invoicing_export_sales_log set chi_paymentdate = myoutpaymentdate,chi_cpaymentdate = myoutpaymentdate::TEXT where chi_origin_id = saleitem_rec.id ;
                     end if ;  
                  end if ;   
                 update neweb_projsaleitem set chi_sales_no=mychisaleno  where id = saleitem_rec.id ;
               end loop ;
               close saleitem_cur ;
            end if ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists prerunpackageexport() cascade""")
       self._cr.execute("""create or replace function prerunpackageexport() returns void as $BODY$
          DECLARE
             ncount int ;
          BEGIN
             delete from neweb_chi_invoicing_package_project ;
             delete from neweb_chi_invoicing_package_product ;
             delete from neweb_chi_invoicing_package_purchase ;
             delete from neweb_chi_invoicing_package_sales ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getoutcomedate(projid int) cascade""")
       self._cr.execute("""create or replace function getoutcomedate(projid int) returns DATE as $BODY$
           DECLARE
             myres DATE ;
           BEGIN
             select max(invoice_date) into myres from neweb_invoice_invoiceopen_line where invoice_id = 
               (select id from neweb_invoice_invoiceopen where project_no=projid) and invoice_state in ('2','3') ;
             return myres ;  
           END;$BODY$
           LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getoutpaymentdate(projid int) cascade""")
       self._cr.execute("""create or replace function getoutpaymentdate(projid int) returns DATE as $BODY$
            DECLARE
              myres DATE ;
            BEGIN
              select invoice_paymentdate into myres from neweb_invoice_invoiceopen  where project_no = projid ; 
              return myres ;  
            END;$BODY$
            LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getpackageprodprojno() cascade""")
       self._cr.execute("""create or replace function getpackageprodprojno() returns varchar as $BODY$
           DECLARE
             myres varchar ;
             proj_cur refcursor ;
             proj_rec record ;
           BEGIN
             myres = ' ' ;
             open proj_cur for select distinct proj_no from neweb_chi_invoicing_package_product order by proj_no ;
             loop
               fetch proj_cur into proj_rec ;
               exit when not found ;
               if myres = ' ' then
                  myres = proj_rec.proj_no ;
               else
                  myres = concat(myres,' / ',proj_rec.proj_no) ;
               end if ;
             end loop ;
             close proj_cur ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;
        """)

       self._cr.execute("""drop function if exists getpackageprojno() cascade""")
       self._cr.execute("""create or replace function getpackageprojno() returns varchar as $BODY$
              DECLARE
                myres varchar ;
                proj_cur refcursor ;
                proj_rec record ;
              BEGIN
                myres = ' ' ;
                open proj_cur for select distinct project_no from neweb_chi_invoicing_package_project order by project_no ;
                loop
                  fetch proj_cur into proj_rec ;
                  exit when not found ;
                  if myres = ' ' then
                     myres = proj_rec.project_no ;
                  else
                     myres = concat(myres,' / ',proj_rec.project_no) ;
                  end if ;
                end loop ;
                close proj_cur ;
                return myres ;
              END;$BODY$
              LANGUAGE plpgsql;
           """)

       self._cr.execute("""drop function if exists getpackagesalesprojno() cascade""")
       self._cr.execute("""create or replace function getpackagesalesprojno() returns varchar as $BODY$
                 DECLARE
                   myres varchar ;
                   proj_cur refcursor ;
                   proj_rec record ;
                 BEGIN
                   myres = ' ' ;
                   open proj_cur for select distinct sales_proj_no from neweb_chi_invoicing_package_sales order by sales_proj_no ;
                   loop
                     fetch proj_cur into proj_rec ;
                     exit when not found ;
                     if myres = ' ' then
                        myres = proj_rec.sales_proj_no ;
                     else
                        myres = concat(myres,' / ',proj_rec.sales_proj_no) ;
                     end if ;
                   end loop ;
                   close proj_cur ;
                   return myres ;
                 END;$BODY$
                 LANGUAGE plpgsql;
              """)

       self._cr.execute("""drop function if exists getpackagepurchaseprojno() cascade""")
       self._cr.execute("""drop function if exists getpackagepurchasepurchaseno() cascade""")
       self._cr.execute("""create or replace function getpackagepurchasepurchaseno() returns varchar as $BODY$
               DECLARE
                 myres varchar ;
                 proj_cur refcursor ;
                 proj_rec record ;
               BEGIN
                 myres = ' ' ;
                 open proj_cur for select distinct purchase_no from neweb_chi_invoicing_package_purchase order by purchase_no ;
                 loop
                   fetch proj_cur into proj_rec ;
                   exit when not found ;
                   if myres = ' ' then
                      myres = proj_rec.purchase_no ;
                   else
                      myres = concat(myres,' / ',proj_rec.purchase_no) ;
                   end if ;
                 end loop ;
                 close proj_cur ;
                 return myres ;
               END;$BODY$
               LANGUAGE plpgsql;
            """)

       self._cr.execute("""drop function if exists getpackdownloadid(empid int,ptype char) cascade""")
       self._cr.execute("""create or replace function getpackdownloadid(empid int,ptype char) returns INT as $BODY$
          DECLARE
            ncount int ;
            myid int ;
            myres int ;
          BEGIN
            if ptype = '1' then
               select count(*) into ncount from neweb_chi_invoicing_package_excel_download where 
               (invoicing1_owner=empid or invoicing2_owner=empid) and xls_file_name1 is null and
                (invoicing1_date::DATE = now()::DATE or invoicing2_date::DATE = now()::DATE) ;
               if ncount > 0 then
                 select max(id) into myres from neweb_chi_invoicing_package_excel_download where 
                 (invoicing1_owner=empid or invoicing2_owner=empid) and xls_file_name1 is null and 
                   (invoicing1_date::DATE = now()::DATE or invoicing2_date::DATE = now()::DATE) ;
                 update neweb_chi_invoicing_package_excel_download set invoicing1_date=now()::DATE,invoicing1_owner=empid where id=myres ;   
               else
                 insert into neweb_chi_invoicing_package_excel_download(invoicing1_date,invoicing1_owner) values (now()::DATE,empid) ;
                 select max(id) into myres from neweb_chi_invoicing_package_excel_download where invoicing1_owner=empid and invoicing1_date::DATE = now()::DATE ; 
               end if ;
            elsif ptype='2' then
               select count(*) into ncount from neweb_chi_invoicing_package_excel_download where 
               (invoicing1_owner=empid or invoicing2_owner=empid) and xls_file_name2 is null and
                (invoicing1_date::DATE = now()::DATE or invoicing2_date::DATE = now()::DATE) ;
               if ncount > 0 then
                 select max(id) into myres from neweb_chi_invoicing_package_excel_download where 
                 (invoicing1_owner=empid or invoicing2_owner=empid) and xls_file_name2 is null and
                   (invoicing1_date::DATE = now()::DATE or invoicing2_date::DATE = now()::DATE) ;
                 update neweb_chi_invoicing_package_excel_download set invoicing2_date=now()::DATE,invoicing2_owner=empid where id=myres ;   
               else
                 insert into neweb_chi_invoicing_package_excel_download(invoicing2_date,invoicing2_owner) values (now()::DATE,empid) ;
                 select max(id) into myres from neweb_chi_invoicing_package_excel_download where invoicing2_owner=empid and invoicing2_date::DATE = now()::DATE ; 
               end if ;
            elsif ptype='3' then
               select count(*) into ncount from neweb_chi_invoicing_package_purinv_excel_download where 
               invoicing_owner=empid and invoicing_date::DATE = now()::DATE ;
               if ncount > 0 then
                 select max(id) into myres from neweb_chi_invoicing_package_purinv_excel_download where 
                      invoicing_owner=empid  and invoicing_date::DATE = now()::DATE ;
                 update neweb_chi_invoicing_package_purinv_excel_download set invoicing_date=now()::DATE,invoicing_owner=empid where id=myres ;   
               else
                 insert into neweb_chi_invoicing_package_purinv_excel_download(invoicing_date,invoicing_owner) values (now()::DATE,empid) ;
                 select max(id) into myres from neweb_chi_invoicing_package_purinv_excel_download where invoicing_owner=empid and invoicing_date::DATE = now()::DATE ; 
               end if ;
            else
               select count(*) into ncount from neweb_chi_invoicing_package_saleinv_excel_download where 
                    invoicing_owner=empid  and invoicing_date::DATE = now()::DATE  ;
               if ncount > 0 then
                 select max(id) into myres from neweb_chi_invoicing_package_saleinv_excel_download where 
                 invoicing_owner=empid  and invoicing_date::DATE = now()::DATE  ;
                 update neweb_chi_invoicing_package_saleinv_excel_download set invoicing_date=now()::DATE,invoicing_owner=empid where id=myres ;   
               else
                 insert into neweb_chi_invoicing_package_saleinv_excel_download(invoicing_date,invoicing_owner) values (now()::DATE,empid) ;
                 select max(id) into myres from neweb_chi_invoicing_package_saleinv_excel_download where invoicing_owner=empid and invoicing_date::DATE = now()::DATE ; 
               end if ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getvatname(myvat varchar) cascade""")
       self._cr.execute("""create or replace function getvatname(myvat varchar) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select count(*) into ncount from res_partner where vat = myvat and is_company=True and active=True ;
            if ncount > 0 then
               select max(id) into myres from res_partner where vat = myvat and is_company=True and active=True;
            else
               myres := 0 ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")


       self._cr.execute("""drop function if exists genallprojprodno() cascade""")
       self._cr.execute("""create or replace function genallprojprodno() returns void as $BODY$
          DECLARE
            proj_cur refcursor ;
            proj_rec record ;
          BEGIN
            open proj_cur for select id from neweb_project ;
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              execute genprojchiprodno(proj_rec.id) ;
            end loop ;
            close proj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_purinv(userid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_purinv(userid int) returns void as $BODY$
          DECLARE
            myempid int ;
            mymaxid int ;
            purinv_cur refcursor ;
            purinv_rec record ;
          BEGIN
            delete from neweb_chi_invoicing_un_export_purinv ;
            insert into neweb_chi_invoicing_un_export_purinv(export_user,export_date) values (userid,now()::DATE) ;
            select max(id) into mymaxid from neweb_chi_invoicing_un_export_purinv where export_user = userid ;
            select getexportempid(userid) into myempid ;
            open purinv_cur for select * from neweb_purinv_invoiceline where is_gen=true and gen_man=myempid order by invline_id,invline_item;
            loop
               fetch purinv_cur into purinv_rec ;
               exit when not found ;
               insert into neweb_chi_invoicing_un_export_purinvline(export_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,
                currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo) values (mymaxid,purinv_rec.inv_prodspec,purinv_rec.cus_partner,
                purinv_rec.purchase_no,purinv_rec.pitem_origin_no,purinv_rec.inv_paymentterm,purinv_rec.currency_id,purinv_rec.invoice_sum,
                purinv_rec.invoice_partner,purinv_rec.invoice_date,purinv_rec.invoice_no,purinv_rec.invline_memo) ;
            end loop ;
            close purinv_cur ;      
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_purinv1(userid int,purid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_purinv1(userid int,purid int) returns void as $BODY$
           DECLARE
             myempid int ;
             mymaxid int ;
             purinv_cur refcursor ;
             purinv_rec record ;
           BEGIN
             delete from neweb_chi_invoicing_un_export_purinv ;
             insert into neweb_chi_invoicing_un_export_purinv(export_user,export_date) values (userid,now()::DATE) ;
             select max(id) into mymaxid from neweb_chi_invoicing_un_export_purinv where export_user = userid ;
             select getexportempid(userid) into myempid ;
             open purinv_cur for select * from neweb_purinv_invoiceline where purchase_no=purid ;
             loop
                fetch purinv_cur into purinv_rec ;
                exit when not found ;
                insert into neweb_chi_invoicing_un_export_purinvline(export_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,
                 currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo) values (mymaxid,purinv_rec.inv_prodspec,purinv_rec.cus_partner,
                 purinv_rec.purchase_no,purinv_rec.pitem_origin_no,purinv_rec.inv_paymentterm,purinv_rec.currency_id,purinv_rec.invoice_sum,
                 purinv_rec.invoice_partner,purinv_rec.invoice_date,purinv_rec.invoice_no,purinv_rec.invline_memo) ;
             end loop ;
             close purinv_cur ;      
           END;$BODY$
           LANGUAGE plpgsql;""")



       self._cr.execute("""drop function if exists genpurinvdata(purid int,purinvlineid int) cascade""")
       self._cr.execute("""create or replace function genpurinvdata(purid int,purinvlineid int) returns void as $BODY$
           DECLARE
             pitem_cur refcursor ;
             pitem_rec record ;
             saleitem_cur refcursor ;
             saleitem_rec record ;
             projno varchar ;
             myyear varchar ;
             mymonth varchar ;
             myday varchar ;
             ncount int ;
             ncount1 int ;
             ncount2 int ;
             mysname varchar ;
             myseq int ;
             myseqid int ;
             mychipurno varchar ;
             mychisaleno varchar ;
             mydateorder date ;
             myincomedate date ;
             myinvid int ;
             mysuppid int ;
             mycurrencyid int ;
             myvat varchar ;
             mycurrency varchar ;
             myproject varchar ;
             mypaymentdate date ;
             myproduct varchar ;
             mypo varchar ;
             mypi varchar ;
             mycusid int ;
             mysaleid int ;
             myprojname varchar ;
             myoutcomedate date ;
             mysaleno varchar ;
             mypurdateorder date ;
             mypitemid int ;
             myprojid int ;
             myinvoicedate date ;
           BEGIN
             mysname = 'income' ;
             select invoice_date into myinvoicedate from neweb_invoice_invoiceopen_line where id = purinvlineid ;
             if myinvoicedate is not null then
                select date_part('year',myinvoicedate::DATE)::TEXT into myyear ;
                select lpad(date_part('month',myinvoicedate::DATE)::TEXT,2,'0') into mymonth ;
                select lpad(date_part('day',myinvoicedate::DATE)::TEXT,2,'0') into myday ;
                select name into mypo from purchase_order where id = purid ;
                select count(*) into ncount from neweb_pitem_list where pitem_id = purid and chi_purchase_no is null ;
                if ncount > 0 then
                  select date_order,origin into mypurdateorder,myprojname from purchase_order where id = purid ;
                  select id into myprojid from neweb_project where name = myprojname ;
                  select count(*) into ncount1 from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                    and chi_sname=mysname ;
                  if ncount1 > 0 then
                     select id,chi_seq into myseqid,myseq from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                       and chi_sname=mysname ;
                     mychipurno = concat('B',myyear,mymonth,myday,lpad(myseq::TEXT,3,'0')) ; 
                     update neweb_chi_invoicing_incomeoutcome_seq set chi_seq = chi_seq + 1 where id = myseqid ;
                  else
                     mychipurno = concat('B',myyear,mymonth,myday,'001') ; 
                     insert into neweb_chi_invoicing_incomeoutcome_seq(chi_year,chi_month,chi_day,chi_sname,chi_seq) values (myyear,mymonth,myday,mysname,2) ;
                  end if ;    
                  select coalesce(cus_order,' '),name into mypi,myproject from neweb_project where id = myprojid ;   
                  open pitem_cur for select * from neweb_pitem_list where pitem_id=purid and chi_purchase_no is null ;
                  loop
                    fetch pitem_cur into pitem_rec ;
                    exit when not found ;
                    select partner_id,currency_id into mysuppid,mycurrencyid from purchase_order where id = purid ;
                    select coalesce(vat,'No Set') into myvat from res_partner where id = mysuppid ;
                    select name into mycurrency from res_currency where id = mycurrencyid ;
                    if mycurrency = 'TWD' then
                       mycurrency = 'NTD' ;
                    end if ;
                    if mycurrency = 'CNY' then
                       mycurrency = 'RMB' ;
                    end if ;
                    select chi_product_no into myproduct from neweb_projsaleitem where id = pitem_rec.pitem_origin_id ;
                    select invline_id,inv_paymentterm into myinvid,mypaymentdate from neweb_purinv_invoiceline where purchase_no=pitem_rec.pitem_id ;
                    select report_date into myincomedate from neweb_purinv_invoice where id = myinvid ;
                    insert into neweb_chi_invoicing_export_purchase_log (chi_purchase_no,chi_income_date,chi_income_cdate,chi_purchase_vat,chi_currency_type,chi_wh,chi_project_no,chi_product,
                     chi_purchase_num,chi_purchase_price,chi_origin_id,proj_no,chi_purchase_name) values (purid,myincomedate,myincomedate::TEXT,myvat,mycurrency,'001',myproject,myproduct,pitem_rec.pitem_num,
                       pitem_rec.pitem_price,pitem_rec.id,myprojid,mychipurno) ;
                    if mypaymentdate is not null then
                       update neweb_chi_invoicing_export_purchase_log set chi_paymentdate = mypaymentdate,chi_cpaymentdate = mypaymentdate::TEXT where chi_origin_id = pitem_rec.id ;
                    end if ;
                    update neweb_pitem_list set chi_purchase_no=mychipurno  where id = pitem_rec.id ;
                  end loop ;
                  close pitem_cur ;
                end if ;
             end if ;   
           END;$BODY$
           LANGUAGE plpgsql;""")


       self._cr.execute("""drop function if exists purinvgenstatus(purid int,genman int) cascade""")
       self._cr.execute("""create or replace function purinvgenstatus(purid int,genman int) returns void as $BODY$
           DECLARE
             pur_cur refcursor ;
             pur_rec record ;
             mynowdate date ;
           BEGIN
             open pur_cur for select id,is_gen,gen_man,gen_date,pitem_origin_no from neweb_purinv_invoiceline where is_gen is True ;
             loop
                fetch pur_cur into pur_rec ;
                exit when not found ;
                update neweb_purinv_invoiceline set is_gen=False,gen_man=genman,gen_date=now()::DATE where id = pur_rec.id ;
                update neweb_pitem_list set chi_select=False where chi_select=True and pitem_origin_no = pur_rec.pitem_origin_no ;
             end loop ;
             close pur_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_saleinv(userid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_saleinv(userid int) returns void as $BODY$
          DECLARE
            myempid int ;
            mymaxid int ;
            inv_cur refcursor ;
            inv_rec record ;
            myoriginno varchar ;
            mycurrencyid int;
            myinvoicedate date;
            myinvoiceno varchar ;
            myinvoicecus int;
            myinvoicememo varchar ;
            myorderlineid int ;
            myinvlineid int ;
          BEGIN
            delete from neweb_chi_invoicing_un_export_invoiceopen ;
            insert into neweb_chi_invoicing_un_export_invoiceopen(export_user,export_date) values (userid,now()::DATE) ;
            select max(id) into mymaxid from neweb_chi_invoicing_un_export_invoiceopen where export_user = userid ;
            select getexportempid(userid) into myempid ;
            open inv_cur for select * from neweb_invoice_invoiceopen where is_gen=true and gen_man=myempid order by project_no ;            
            loop
               fetch inv_cur into inv_rec ;
               exit when not found ;
               select cus_order,cus_name into myoriginno,myinvoicecus from neweb_project where id = inv_rec.project_no ;
               select min(id) into myorderlineid from sale_order_line where order_id in (select id from sale_order where name = myoriginno) ;
               select currency_id into mycurrencyid from sale_order_line where id = myorderlineid ;
               select max(invoice_date) into myinvoicedate from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id ;
               if myinvoicedate is not null then
                  select max(id) into myinvlineid from neweb_invoice_invoiceopen_line where invoice_id = inv_rec.id and invoice_date = myinvoicedate ;
                  select invoice_no into myinvoiceno from neweb_invoice_invoiceopen_line where id = myinvlineid ;
                  insert into neweb_chi_invoicing_un_export_invoiceopenline(export_id,inv_prodspec,cus_partner,project_no,invoice_origin_no,inv_paymentterm,
                   currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo) values (mymaxid,inv_rec.invoice_title,inv_rec.sno,
                   inv_rec.project_no,myoriginno,inv_rec.invoice_paymentdate,mycurrencyid,inv_rec.project_amount_total,
                   myinvoicecus,myinvoicedate,myinvoiceno,inv_rec.project_name) ;
               end if ;    
            end loop ;
            close inv_cur ;      
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_saleinv1(projid int,userid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_saleinv1(projid int,userid int) returns void as $BODY$
        DECLARE
          myempid int ;
          mymaxid int ;
          inv_cur refcursor ;
          inv_rec record ;
          myoriginno varchar ;
          mycurrencyid int;
          myinvoicedate date;
          myinvoiceno varchar ;
          myinvoicecus int;
          myinvoicememo varchar ;
          myorderlineid int ;
          myinvlineid int ;
        BEGIN
          delete from neweb_chi_invoicing_un_export_invoiceopen ;
          insert into neweb_chi_invoicing_un_export_invoiceopen(export_user,export_date) values (userid,now()::DATE) ;
          select max(id) into mymaxid from neweb_chi_invoicing_un_export_invoiceopen where export_user = userid ;
          select getexportempid(userid) into myempid ;
          open inv_cur for select * from neweb_invoice_invoiceopen where project_no = projid ;            
          loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             select cus_order,cus_name into myoriginno,myinvoicecus from neweb_project where id = inv_rec.project_no ;
             select min(id) into myorderlineid from sale_order_line where order_id in (select id from sale_order where name = myoriginno) ;
             select currency_id into mycurrencyid from sale_order_line where id = myorderlineid ;
             select max(invoice_date) into myinvoicedate from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id ;
             if myinvoicedate is not null then
                select max(id) into myinvlineid from neweb_invoice_invoiceopen_line where invoice_id = inv_rec.id and invoice_date = myinvoicedate ;
                select invoice_no into myinvoiceno from neweb_invoice_invoiceopen_line where id = myinvlineid ;
                insert into neweb_chi_invoicing_un_export_invoiceopenline(export_id,inv_prodspec,cus_partner,project_no,invoice_origin_no,inv_paymentterm,
                 currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo) values (mymaxid,inv_rec.invoice_title,inv_rec.sno,
                 inv_rec.project_no,myoriginno,inv_rec.invoice_paymentdate,mycurrencyid,inv_rec.project_amount_total,
                 myinvoicecus,myinvoicedate,myinvoiceno,inv_rec.project_name) ;
             end if ;    
          end loop ;
          close inv_cur ;      
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists saleinvgenstatus(projid int,genman int) cascade""")
       self._cr.execute("""create or replace function saleinvgenstatus(projid int,genman int) returns void as $BODY$
         DECLARE
           inv_cur refcursor ;
           inv_rec record ;
           mynowdate date ;
         BEGIN
           open inv_cur for select id,is_gen,gen_man,gen_date from neweb_invoice_invoiceopen where is_gen=True ;
           loop
              fetch inv_cur into inv_rec ;
              exit when not found ;
              update neweb_invoice_invoiceopen set is_gen=False,gen_man=genman,gen_date=now()::DATE where id = inv_rec.id ;
           end loop ;
           close inv_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists check_null_reportdate(purid int) cascade""")
       self._cr.execute("""create or replace function check_null_reportdate(purid int) returns Boolean as $BODY$
           DECLARE
             ncount int ;
             myres Boolean ;
           BEGIN
             select count(*) into ncount from neweb_purinv_invoice where report_date is null and 
                id = (select max(invline_id) from neweb_purinv_invoiceline where purchase_no=purid) ; 
             if ncount > 0 then
                myres := True ;
             else
                myres := False ;
             end if ;
             return myres ;   
           END;$BODY$
           LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists return_purinvno(purid int) cascade""")
       self._cr.execute("""create or replace function return_purinvno(purid int) returns varchar as $BODY$
         DECLARE
           ncount int ;
           myres varchar ;
         BEGIN
           select count(*) into ncount from neweb_purinv_invoice where report_date is null and 
              id = (select max(invline_id) from neweb_purinv_invoiceline where purchase_no=purid) ; 
           if ncount > 0 then
              select name into myres from neweb_purinv_invoice where report_date is null and 
              id = (select max(invline_id) from neweb_purinv_invoiceline where purchase_no=purid) ; 
           else
              myres := ' ' ;
           end if ;
           return myres ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists setallzzc() cascade""")
       self._cr.execute("""create or replace function setallzzc() returns void as $BODY$
       DECLARE
         ncount int ;
       BEGIN
         update neweb_projsaleitem set chi_product_no='ZZC00000001' where cost_type=3 ;
         update neweb_projsaleitem set chi_product_no='ZZA00000001' where cost_type=2 ;
         update neweb_projsaleitem set chi_product_no='ZZB00000001' where cost_type in (4,9) ;
         update neweb_projsaleitem set chi_product_no='ZZD00000001' where cost_type=5 ;
         update neweb_projsaleitem set chi_product_no='ZZE00000001' where cost_type=7 ;
         update neweb_projsaleitem set chi_product_no='ZZG00000001' where cost_type=11 ;
         update neweb_projsaleitem set chi_product_no='ZZH00000001' where cost_type in (6,8) ;
         update neweb_projsaleitem set chi_product_no='ZZW00000001' where cost_type=12 ;
         update neweb_projsaleitem set chi_product_no='ZZI00000001' where cost_type=descpid ;
       END;$BODY$
       LANGUAGE plpgsql;""")

       self._cr.execute(
          """drop function if exists gen_chi_export_proj_ids(chiid int,exportuser int) cascade""")
       self._cr.execute("""create or replace function gen_chi_export_proj_ids(chiid int,exportuser int) returns void as $BODY$
           DECLARE
             proj_cur refcursor ;
             proj_rec record ;
             mymaxid int ;
             mynowdate date ;
             myinvcomplete Boolean ;
           BEGIN
             myinvcomplete := False ; 
             select now()::DATE into mynowdate ; 
             delete from neweb_chi_invoicing_un_export_proj ;
             insert into neweb_chi_invoicing_un_export_proj(export_date,export_user) values (mynowdate,exportuser) ;
             select max(id) into mymaxid from neweb_chi_invoicing_un_export_proj ;
             open proj_cur for select * from neweb_project where id in (select proj_id from chi_project_rel where chi_id=chiid);
             loop
               fetch proj_cur into proj_rec ;
               exit when not found ;
               insert into neweb_chi_invoicing_un_export_proj_line(export_id,proj_no,partner_id,amount_untaxed,amount_tax,amount_total,chi_export_project,chi_export_product,chi_export_outcome,
                  chi_export_income,chi_invoice_complete) values (mymaxid,proj_rec.id,proj_rec.cus_name,proj_rec.total_saleitem,proj_rec.total_saleitem_tax,proj_rec.total_saleitem_amount,
                  proj_rec.chi_export_project,proj_rec.chi_export_product,proj_rec.chi_export_outcome,proj_rec.chi_export_income,myinvcomplete) ;

             end loop ;
             close proj_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getsetnum(mydate date,mytype char) cascade""")
       self._cr.execute("""create or replace function getsetnum(mydate date,mytype char) returns Integer as $BODY$
          DECLARE
            ncount int ;
            myres Integer ;
          BEGIN
            select count(*) into ncount from neweb_chi_invoicing_excelset_seq where set_date::DATE = mydate::DATE ;
            if ncount > 0 then
               if mytype='1' then                  /* sales */
                  select coalesce(sales_num,1) into myres from neweb_chi_invoicing_excelset_seq where set_date::DATE = mydate::DATE ;
                  update neweb_chi_invoicing_excelset_seq set sales_num=coalesce(sales_num,1) + 1 where set_date::DATE = mydate::DATE ;
               elsif mytype='2' then               /* purchase */
                  select coalesce(purchase_num,1) into myres from neweb_chi_invoicing_excelset_seq where set_date::DATE = mydate::DATE ;
                  update neweb_chi_invoicing_excelset_seq set purchase_num=coalesce(purchase_num,1) + 1 where set_date::DATE = mydate::DATE ;
               elsif mytype='3' then              /* project */
                  select coalesce(project_num,1) into myres from neweb_chi_invoicing_excelset_seq where set_date::DATE = mydate::DATE ;
                  update neweb_chi_invoicing_excelset_seq set project_num=coalesce(project_num,1) + 1 where set_date::DATE = mydate::DATE ;  
               elsif mytype='4' then               /* product */
                  select coalesce(product_num,1) into myres from neweb_chi_invoicing_excelset_seq where set_date::DATE = mydate::DATE ;
                  update neweb_chi_invoicing_excelset_seq set product_num=coalesce(product_num,1) + 1 where set_date::DATE = mydate::DATE ;   
               end if ;
            else
               myres = 1 ;
               if mytype='1' then    /* sales */
                  insert into neweb_chi_invoicing_excelset_seq(set_date,sales_num,purchase_num,project_num,product_num) values (mydate::DATE,2,1,1,1) ;
               elsif mytype='2' then     /* purchase */
                   insert into neweb_chi_invoicing_excelset_seq(set_date,sales_num,purchase_num,project_num,product_num) values (mydate::DATE,1,2,1,1) ;
               elsif mytype='3' then    /* project */
                  insert into neweb_chi_invoicing_excelset_seq(set_date,sales_num,purchase_num,project_num,product_num) values (mydate::DATE,1,1,2,1) ;
               elsif mytype='4' then    /* product */  
                  insert into neweb_chi_invoicing_excelset_seq(set_date,sales_num,purchase_num,project_num,product_num) values (mydate::DATE,1,1,1,2) ;  
               end if ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_chi_export_mainproj(mystartdate date,myenddate date,exportuser int) cascade""")

       self._cr.execute("""drop function if exists getmaincontract() cascade""")


       self._cr.execute("""drop function if exists gen_chi_export_mainproj_ids(contractid int,exportuser int) cascade""")
       self._cr.execute("""drop function if exists gen_chi_export_mainproj_ids(wizid int,exportuser int) cascade""")

       self._cr.execute("""drop view if exists neweb_project_contract_view cascade""")
       self._cr.execute("""create or replace view neweb_project_contract_view as select 
              A.project_no,A.clinch_date,A.is_maintenance_contract,A.is_outsourcing_service,B.id,B.cus_name,B.total_saleitem,B.total_saleitem_tax,B.total_saleitem_amount,B.chi_export_project,
              B.chi_export_product,B.chi_export_outcome,B.chi_export_income,B.name from neweb_contract_contract A left join neweb_project B
              on A.project_no=B.name where (A.is_maintenance_contract=True or A.is_outsourcing_service=True) and A.clinch_date is not null and B.id is not null ;""")

       self._cr.execute("""drop function if exists gen_chi_export_mainproj(startdate date,enddate date,exportuser int) cascade""")
       self._cr.execute("""create or replace function gen_chi_export_mainproj(startdate date,enddate date,exportuser int) returns void as $BODY$
          DECLARE
            proj_cur refcursor ;
            proj_rec record ;
            mymaxid int ;
            mynowdate date ;
            myinvcomplete Boolean ;
            myprojname varchar ;
            myprojid int ;
          BEGIN
            delete from neweb_chi_invoicing_un_export_main_proj ; 
            myinvcomplete := False ; 
            select now()::DATE into mynowdate ; 
            insert into neweb_chi_invoicing_un_export_main_proj(export_date,export_user) values (mynowdate,exportuser) ;
            select max(id) into mymaxid from neweb_chi_invoicing_un_export_main_proj ;
            open proj_cur for select * from neweb_project_contract_view where clinch_date::DATE between startdate::DATE and enddate::DATE ;
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              insert into neweb_chi_invoicing_un_export_main_proj_line(export_id,proj_no,partner_id,amount_untaxed,amount_tax,amount_total,chi_export_project,chi_export_product,chi_export_outcome,
                 chi_export_income,chi_invoice_complete) values (mymaxid,proj_rec.id,proj_rec.cus_name,proj_rec.total_saleitem,proj_rec.total_saleitem_tax,proj_rec.total_saleitem_amount,
                 proj_rec.chi_export_project,proj_rec.chi_export_product,proj_rec.chi_export_outcome,proj_rec.chi_export_income,myinvcomplete) ; 
            end loop ;
            close proj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_mainsaleinv(userid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_mainsaleinv(userid int) returns void as $BODY$
        DECLARE
          myempid int ;
          mymaxid int ;
          inv_cur refcursor ;
          inv_rec record ;
          myoriginno varchar ;
          mycurrencyid int;
          myinvoicedate date;
          myinvoiceno varchar ;
          myinvoicecus int;
          myinvoicememo varchar ;
          myorderlineid int ;
          myinvlineid int ;
          myprojid int ;
          myinvoicetitle varchar ;
          mysno varchar ;
          myprojectname varchar ;
          invtaxamount float ;
        BEGIN
          delete from neweb_chi_invoicing_un_export_invoiceopen ;
          insert into neweb_chi_invoicing_un_export_invoiceopen(export_user,export_date) values (userid,now()::DATE) ;
          select max(id) into mymaxid from neweb_chi_invoicing_un_export_invoiceopen where export_user = userid ;
          select getexportempid(userid) into myempid ;
          open inv_cur for select * from neweb_invoice_invoiceopen_line where is_main_gen=true and 
            (is_main_completed is null or is_main_completed = False) ;            
          loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             invtaxamount = (inv_rec.invoice_num * inv_rec.invoice_unit_price1) ;
             select project_no,invoice_title,sno,project_name into myprojid,myinvoicetitle,mysno,myprojectname from neweb_invoice_invoiceopen where id = inv_rec.invoice_id ;
             select cus_order,cus_name into myoriginno,myinvoicecus from neweb_project where id = myprojid;
             select min(id) into myorderlineid from sale_order_line where order_id in (select id from sale_order where name = myoriginno) ;
             select currency_id into mycurrencyid from sale_order_line where id = myorderlineid ;
             insert into neweb_chi_invoicing_un_export_invoiceopenline(export_id,inv_prodspec,cus_partner,project_no,invoice_origin_no,inv_paymentterm,
              currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo) values (mymaxid,inv_rec.invoice_spec,mysno,
              myprojid,myoriginno,inv_rec.receive_date,mycurrencyid,invtaxamount,
              myinvoicecus,inv_rec.invoice_date,inv_rec.invoice_no,myprojectname) ; 
          end loop ;
          close inv_cur ;      
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genincomeoutcomenom1(projid int) cascade""")
       self._cr.execute("""create or replace function genincomeoutcomenom1(projid int) returns void as $BODY$
           DECLARE
             invl_cur refcursor ;
             invl_rec record ;
             projno varchar ;
             myyear varchar ;
             mymonth varchar ;
             myday varchar ;
             ncount int ;
             ncount1 int ;
             ncount2 int ;
             mysname varchar ;
             myseq int ;
             myseqid int ;
             mychipurno varchar ;
             mychisaleno varchar ;
             mydateorder date ;
             myinvid int ;
             mysuppid int ;
             mycurrencyid int ;
             myvat varchar ;
             mycurrency varchar ;
             myproject varchar ;
             mypaymentdate date ;
             myproduct varchar ;
             mypi varchar ;
             mycusid int ;
             mysaleid int ;
             myprojname varchar ;
             myoutcomedate date ;
             mysaleno varchar ;
             myoutpaymentdate date ;
             myprojdate date ;
             myinvoicedate date ;
             mychisaleno1 varchar ;
             myothermemo varchar ;
             mycontractid int ;
             mylen int;
             mytaxamount float ;
           BEGIN
             mysname = 'moutcome' ;  
             /* 產生正航銷售單號 */
             select coalesce(other_memo,' ') into myothermemo from neweb_invoice_invoiceopen where project_no=projid ;
             open invl_cur for select * from neweb_invoice_invoiceopen_line where invoice_id in (select id from neweb_invoice_invoiceopen where project_no=projid)
                 and is_main_gen=true and (is_main_completed is null or is_main_completed=false) and invoice_date is not null ;
             loop
                fetch invl_cur into invl_rec ;
                exit when not found ;
                mycurrency = 'NTD' ;
                mytaxamount = (invl_rec.invoice_num * invl_rec.invoice_unit_price1) ;
                select sno,contract_no,cus_order,project_no,other_memo into myvat,mycontractid,mypi,projid,myothermemo from neweb_invoice_invoiceopen where id = invl_rec.invoice_id ;
                select length(name) into mylen from  neweb_contract_contract where id = mycontractid ;
                select substring(name,1,(mylen - 6)) into myproject from neweb_contract_contract where id = mycontractid ;
                myproduct = 'ZZB00000001' ;
                select proj_sale into mysaleid from neweb_project where id = projid;
                if invl_rec.sales_no is null then
                   select date_part('year',invl_rec.invoice_date)::TEXT into myyear ;
                   select lpad(date_part('month',invl_rec.invoice_date)::TEXT,2,'0') into mymonth ;
                   select lpad(date_part('day',invl_rec.invoice_date)::TEXT,2,'0') into myday ;
                   select count(*) into ncount1 from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                               and chi_sname=mysname ;
                   if ncount1 > 0 then
                      select id,chi_seq into myseqid,myseq from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                         and chi_sname=mysname ;
                      mychisaleno = concat('C',myyear,mymonth,myday,lpad(myseq::TEXT,3,'0')) ; 
                      update neweb_chi_invoicing_incomeoutcome_seq set chi_seq = chi_seq + 1 where id = myseqid ;
                   else 
                      mychisaleno = concat('C',myyear,mymonth,myday,'001') ;
                      insert into neweb_chi_invoicing_incomeoutcome_seq (chi_year,chi_month,chi_day,chi_sname,chi_seq) values (myyear,mymonth,myday,mysname,2) ;
                   end if ;  
                   insert into neweb_chi_invoicing_export_sales_log (chi_sales_no,chi_sales_vat,chi_currency_type,proj_sale_name,chi_wh,chi_project_no,chi_cus_order,
                         chi_product,chi_sales_num,chi_sales_price,chi_origin_id,proj_no,proj_sale,chi_sale_memo,chi_paymentdate,chi_cpaymentdate,chi_sale_spec,chi_outcome_date,chi_outcome_cdate) values (mychisaleno,myvat,mycurrency,'ZZB','001',myproject,mypi,myproduct,
                         1,mytaxamount,invl_rec.id,projid,mysaleid,myothermemo,invl_rec.receive_date,invl_rec.receive_date::TEXT,invl_rec.invoice_spec,invl_rec.invoice_date,invl_rec.invoice_date::TEXT) ;     
                   update neweb_invoice_invoiceopen_line set is_main_completed=true,sales_no=mychisaleno,is_main_gen=False where id = invl_rec.id ;   
                else
                   update neweb_chi_invoicing_export_sales_log set chi_paymentdate=invl_rec.receive_date,chi_cpaymentdate=invl_rec.receive_date::TEXT,chi_sales_price=mytaxamount,
                         chi_sale_memo=myothermemo,chi_sale_spec=invl_rec.invoice_spec where chi_sales_no=invl_rec.sales_no ;
                   update neweb_invoice_invoiceopen_line set is_main_completed=true,sales_no=mychisaleno,is_main_gen=False where id = invl_rec.id ;      
                end if ;             
             end loop ;
             close invl_cur ;    
             
           END;$BODY$
           LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genincomeoutcomenom2(purid int) cascade""")
       self._cr.execute("""drop function if exists genincomeoutcomenom2(purid int,unexportid int) cascade""")
       self._cr.execute("""create or replace function genincomeoutcomenom2(purid int,unexportid int) returns void as $BODY$
        DECLARE
          pinv_cur refcursor ;
          pinv_rec record ;
          projno varchar ;
          myyear varchar ;
          mymonth varchar ;
          myday varchar ;
          ncount int ;
          ncount1 int ;
          ncount2 int ;
          mysname varchar ;
          myseq int ;
          myseqid int ;
          mychipurno varchar ;
          mychisaleno varchar ;
          mydateorder date ;
          myincomedate date ;
          myinvid int ;
          mysuppid int ;
          mycurrencyid int ;
          myvat varchar ;
          mycurrency varchar ;
          myproject varchar ;
          mypaymentdate date ;
          myproduct varchar ;
          mypo varchar ;
          mypi varchar ;
          mycusid int ;
          mysaleid int ;
          myprojname varchar ;
          myoutcomedate date ;
          mysaleno varchar ;
          mypurdateorder date ;
          mypitemid int ;
          purchaseno varchar ;
          myinvoicedate date ;
          mychipurchaseno varchar;
          projid int ;
          mychioriginid int ;
          mynowdate date ;
        BEGIN 
          /* report_date 製表日期  */
          select current_timestamp::DATE into mynowdate ;
          select chi_origin_id into mychioriginid from neweb_chi_invoicing_un_export_purinvline where id = unexportid ;
          select report_date into myinvoicedate from neweb_purinv_invoice where id =
            (select invline_id from neweb_purinv_invoiceline where id = mychioriginid ) ;
          myinvoicedate := myinvoicedate + interval '8 hours' ;
          mysname = 'mincome' ;
          select date_part('year',myinvoicedate)::TEXT into myyear ;
          select lpad(date_part('month',myinvoicedate)::TEXT,2,'0') into mymonth ;
          select lpad(date_part('day',myinvoicedate)::TEXT,2,'0') into myday ;
          mypo = ' ' ;
          /* open pinv_cur for select * from neweb_purinv_invoiceline where is_m_gen=true and purchase_no=purid ; */
          open pinv_cur for select * from neweb_purinv_invoiceline where is_m_gen=true order by invline_id,invline_item ;
          loop
             fetch pinv_cur into pinv_rec ;
             exit when not found ;
             if (pinv_rec.main_purno is null or pinv_rec.main_purno='' or pinv_rec.main_purno = 'D001') then
               select count(*) into ncount1 from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                    and chi_sname=mysname ;
               if ncount1 > 0 then
                  select id,chi_seq into myseqid,myseq from neweb_chi_invoicing_incomeoutcome_seq where chi_year=myyear and chi_month = mymonth and chi_day=myday
                    and chi_sname=mysname ;
                  mychipurno = concat('D',myyear,mymonth,myday,lpad(myseq::TEXT,3,'0')) ; 
                  update neweb_chi_invoicing_incomeoutcome_seq set chi_seq = chi_seq + 1 where id = myseqid ;
               else
                  mychipurno = concat('D',myyear,mymonth,myday,'001') ; 
                  insert into neweb_chi_invoicing_incomeoutcome_seq (chi_year,chi_month,chi_day,chi_sname,chi_seq) values (myyear,mymonth,myday,mysname,2) ;
               end if ;  
             else
              /* if mychipurchaseno is not null then */
                  mychipurno := pinv_rec.main_purno ;   
             /*  end if ;   */
             end if ;  
                
                 select coalesce(vat,'No Set') into myvat from res_partner where id = pinv_rec.invoice_partner ;
                 select name into mycurrency from res_currency where id = pinv_rec.currency_id ;
                 if mycurrency = 'TWD' then
                    mycurrency = 'NTD' ;
                 end if ;
                 if mycurrency = 'CNY' then
                    mycurrency = 'RMB' ;
                 end if ;
                myproduct = 'ZZB00000001' ; 
                select id into projid from neweb_project where name = pinv_rec.pitem_origin_no ;
                if (pinv_rec.main_purno is null or pinv_rec.main_purno='' or pinv_rec.main_purno='D001') then
                   insert into neweb_chi_invoicing_export_purchase_log (chi_purchase_no,chi_income_date,chi_income_cdate,chi_purchase_vat,chi_currency_type,chi_wh,chi_project_no,chi_product,
                   chi_purchase_num,chi_purchase_price,chi_origin_id,proj_no,chi_purchase_name,chi_purchase_sup,chi_paymentdate,chi_cpaymentdate) values (pinv_rec.purchase_no,myinvoicedate,myinvoicedate::TEXT,myvat,mycurrency,'001',pinv_rec.pitem_origin_no
                   ,myproduct,1,pinv_rec.invoice_sum,pinv_rec.id,projid,mychipurno,pinv_rec.invoice_partner,pinv_rec.inv_paymentterm,pinv_rec.inv_paymentterm::TEXT) ;
                   update neweb_purinv_invoiceline set main_purno=mychipurno,is_m_gen=False,gen_m_date=mynowdate where id = pinv_rec.id ; 
                else
                    update neweb_chi_invoicing_export_purchase_log set chi_paymentdate = pinv_rec.inv_paymentterm,chi_cpaymentdate = pinv_rec.inv_paymentterm::TEXT,
                      chi_purchase_price=pinv_rec.invoice_sum,chi_income_date=myinvoicedate,chi_income_cdate=myinvoicedate::TEXT,chi_purchase_vat=myvat,chi_currency_type=mycurrency,
                      chi_purchase_name = mychipurno where chi_purchase_name = pinv_rec.main_purno ;
                   update neweb_purinv_invoiceline set main_purno=mychipurno,is_m_gen=False,gen_m_date=mynowdate where id = pinv_rec.id ;   
                end if ;  
                update neweb_chi_invoicing_un_export_purinvline set chi_origin_id=pinv_rec.id where id = unexportid ;   
          end loop ;
          close pinv_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists gen_unexport_mainpurinv(userid int) cascade""")
       self._cr.execute("""create or replace function gen_unexport_mainpurinv(userid int) returns void as $BODY$
        DECLARE
          myempid int ;
          mymaxid int ;
          purinv_cur refcursor ;
          purinv_rec record ;
        BEGIN
          delete from neweb_chi_invoicing_un_export_purinv ;
          insert into neweb_chi_invoicing_un_export_purinv(export_user,export_date) values (userid,now()::DATE) ;
          select max(id) into mymaxid from neweb_chi_invoicing_un_export_purinv where export_user = userid ;
          select getexportempid(userid) into myempid ;
          open purinv_cur for select * from neweb_purinv_invoiceline where is_m_gen=true and gen_m_man=myempid order by invline_id,invline_item;
          loop
             fetch purinv_cur into purinv_rec ;
             exit when not found ;
             insert into neweb_chi_invoicing_un_export_purinvline(export_id,inv_prodspec,cus_partner,purchase_no,pitem_origin_no,inv_paymentterm,
              currency_id,invoice_sum,invoice_partner,invoice_date,invoice_no,invline_memo,chi_origin_id) values (mymaxid,purinv_rec.inv_prodspec,purinv_rec.cus_partner,
              purinv_rec.purchase_no,purinv_rec.pitem_origin_no,purinv_rec.inv_paymentterm,purinv_rec.currency_id,purinv_rec.invoice_sum,
              purinv_rec.invoice_partner,purinv_rec.invoice_date,purinv_rec.invoice_no,purinv_rec.invline_memo,purinv_rec.id) ;
          end loop ;
          close purinv_cur ;      
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists ckmchipurchase(purid int) cascade""")
       self._cr.execute("""create or replace function ckmchipurchase(purid int) returns void as $BODY$
        DECLARE
          ncount int ;
          mchi_cur refcursor ;
          mchi_rec record ;
          myminid int ;
        BEGIN
          delete from neweb_chi_invoicing_export_purchase_log where chi_purchase_name='D001' and chi_purchase_no=purid ;
          open mchi_cur for select distinct chi_origin_id from neweb_chi_invoicing_export_purchase_log where chi_purchase_no=purid ;
          loop
             fetch mchi_cur into mchi_rec ;
             exit when not found ;
             select count(*) into ncount from neweb_chi_invoicing_export_purchase_log where chi_origin_id = mchi_rec.chi_origin_id 
                  and chi_purchase_no = purid ; 
             if ncount > 1 then
                select min(id) into myminid from neweb_chi_invoicing_export_purchase_log where chi_origin_id = mchi_rec.chi_origin_id 
                  and chi_purchase_no = purid ; 
                delete from neweb_chi_invoicing_export_purchase_log where chi_origin_id = mchi_rec.chi_origin_id and id > myminid 
                  and chi_purchase_no = purid ;   
             end if ;     
          end loop ;
          close mchi_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self.env.cr.execute("""drop function if exists renewmainchi() cascade""")
       self.env.cr.execute("""create or replace function renewmainchi() returns void as $BODY$
        DECLARE
          ncount int ;
        BEGIN
          update neweb_purinv_invoiceline set main_purno='' ;
          delete from neweb_chi_invoicing_export_purchase_log where chi_purchase_name like '%D%' ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genselectpuritem(invlineid int,myuid int) cascade""")
       self._cr.execute("""create or replace function genselectpuritem(invlineid int,myuid int) returns void as $BODY$
        DECLARE
          pur_cur refcursor ;
          pur_rec record ;
          purid int ;
          invid int ;
          mymaxid int ;
        BEGIN
          delete from neweb_chi_invoicing_purchase_select_line ;
          delete from neweb_chi_invoicing_purchase_select;
          insert into neweb_chi_invoicing_purchase_select(select_owner) values (myuid) ;
          select max(id) into mymaxid from neweb_chi_invoicing_purchase_select where select_owner=myuid ;
          select purchase_no into purid from neweb_purinv_invoiceline where id = invlineid ;
         /* open pur_cur for select * from neweb_pitem_list where pitem_id = purid and (chi_purchase_no = '' or chi_purchase_no is null)  ; */ 
          open pur_cur for select * from neweb_pitem_list where pitem_id = purid   ; 
          loop
            fetch pur_cur into pur_rec ;
            exit when not found ;
            insert into neweb_chi_invoicing_purchase_select_line(purchase_id,pitem_machine_type,pitem_model_type,pitem_spec,pitem_num,pitem_price,pitem_id)
              values (mymaxid,pur_rec.pitem_machine_type,pur_rec.pitem_model_type,pur_rec.pitem_spec,pur_rec.pitem_num,pur_rec.pitem_price,pur_rec.id) ;   
          end loop ;
          close pur_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genunselectpuritem(invlineid int) cascade""")
       self._cr.execute("""create or replace function genunselectpuritem(invlineid int) returns void as $BODY$
        DECLARE
          purid int ;
        BEGIN
          select purchase_no into purid from neweb_purinv_invoiceline where id = invlineid ;
          update neweb_pitem_list set chi_select=False where pitem_id=purid ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists getselectpurchaselog() cascade""")
       self._cr.execute("""create or replace function getselectpurchaselog() returns setof INT as $BODY$
        DECLARE
          pitem_cur refcursor ;
          pitem_rec record ;
        BEGIN
          open pitem_cur for select id,chi_select from neweb_pitem_list where chi_select = True ;
          loop
            fetch pitem_cur into pitem_rec ;
            exit when not found ;
            return next pitem_rec.id ;
          end loop ;
          close pitem_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

       self._cr.execute("""drop function if exists genprojtopitem(projno varchar,purno varchar) cascade""")
       self._cr.execute("""create or replace function genprojtopitem(projno varchar,purno varchar) returns void as $BODY$
        DECLARE
          p_cur refcursor ;
          p_rec record ;
          projid int ;
          purid int ;
        BEGIN
          select id into projid from neweb_project where name = projno ;
          select id into purid from purchase_order where name = purno ;
          if projid is not null and purid is not null then
             open p_cur for select * from neweb_projsaleitem where saleitem_id= projid order by line_item ;
             loop
                fetch p_cur into p_rec ;
                exit when not found ;
                update neweb_pitem_list set pitem_origin_id=p_rec.id  where pitem_id = purid and pitem_litem = p_rec.line_item::numeric and pitem_origin_id is null ;
             end loop ;
             close p_cur ;
          end if ;
        END ;$BODY$
        LANGUAGE plpgsql;""")