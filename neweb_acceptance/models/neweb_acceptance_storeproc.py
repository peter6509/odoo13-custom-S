# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,tools

class NewebAcceptanceStoreProc(models.Model):
    _name = "neweb.acceptance_storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists chkprojsaletype(projid int) cascade""")
        self._cr.execute("""create or replace function chkprojsaletype(projid int) returns Boolean as $BODY$
         DECLARE
           ncount int ;
           myres Boolean ;
         BEGIN
           select count(*) into ncount from neweb_projsaleitem where saleitem_id=projid and cost_type in (1,12) ;
           if ncount = 0 then
              myres = FALSE ;
           else
              myres = TRUE ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'neweb_stockout_list_view')
        self._cr.execute("""create or replace view neweb_stockout_list_view as (
                    select A.name,A.create_date,A.stockout_proj_no,A.picking_type_id,B.stockout_modeltype,B.stockout_prodno,B.stockout_spec,
                    B.stockout_num,B.stockout_desc,B.id as outlist_id,B.stockout_sequence_id,A.id as pickingid,A.scheduled_date,C.cost_type,C.chi_product_no from stock_picking A 
                    left join neweb_stockout_list B on A.id = B.stockout_id
                    left join neweb_projsaleitem C on B.stockout_sequence_id = C.id
                    where A.picking_type_id in (select id from stock_picking_type where sequence_code='OUT')
                    and C.cost_type in (1,12))""")

        tools.drop_view_if_exists(self._cr, 'neweb_uncomplete_invoice_view')
        self._cr.execute("""create or replace view neweb_uncomplete_invoice_view as (
                    select A.project_no,A.contract_no,A.cus_name,A.main_cus_name,A.project_amount_total,A.open_complete_total,A.is_completed,B.proj_sale
                    from neweb_invoice_invoiceopen A  
                    left join neweb_project B on A.project_no = B.id
                    where abs(A.project_amount_total - A.open_complete_total) > 5)""")


        # 每月1號 產生未結案貨品狀態狀況清單,讓業務進行狀態回報確認
        self._cr.execute("""drop function if exists genprojacceptance() cascade""")
        self._cr.execute("""create or replace function genprojacceptance() returns void as $BODY$
         DECLARE
           p_cur refcursor ;  /* neweb_project refcursor*/
           p_rec record ;
           pickid int ;
           out_cur refcursor ; /* neweb_stockout_list_view refcursor*/
           out_rec record ;
           inv_cur refcursor ;
           inv_rec record ;
           ncount int ;
           ncount1 int ;
           nnum int ;
           projid int ;
           projsale int ;
           cusname int ;
           cusproject varchar ;
           accdate1 date ;
           accdate2 date ;
           accmaxid int ;
           accmaxid1 int ;
           purno varchar ;
           sup varchar ;
           soutdate date ;
           sindate date ;
           cym varchar ;
           mynowdate date ;
           purdate date ;
         BEGIN
           select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
           cym = concat(date_part('year',mynowdate)::TEXT,'-',lpad(date_part('month',mynowdate)::TEXT,2,'0')) ;
           update neweb_acceptance_line set active=false  ;
           update neweb_acceptance set keyin_date=null,projsaleitem_status=null where active=true ;
           open p_cur for select id,proj_sale,name from neweb_project 
              where projsaleitem_completed=false or projsaleitem_completed is null ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select count(*) into ncount1 from neweb_projsaleitem where saleitem_id =  p_rec.id and purchase_no is not null ;
             if ncount1 > 0 then   /* 已發採購單的記錄 */
                 /* nnum = 1 ;*/
                 open out_cur for select * from neweb_stockout_list_view where stockout_proj_no=p_rec.name order by name,outlist_id ;
                 loop
                   fetch out_cur into out_rec ;
                   exit when not found ;
                   select id,proj_sale,cus_name,cus_project,acceptanced_date1,acceptanced_date2 into projid,projsale,cusname,cusproject,accdate1,accdate2 from neweb_project where name=out_rec.stockout_proj_no ;
                   select count(*) into ncount from neweb_acceptance where stockout_no=out_rec.name and active=true ;
                   if ncount = 0 then      
                      insert into neweb_acceptance(project_no,project_no1,stockout_no,stockout_no1,acceptance_status,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,prod_num,acceptanced_date1,acceptanced_date2,active,stockout_date) values
                       (projid,out_rec.stockout_proj_no,out_rec.name,out_rec.pickingid,'1',projsale,cusname,cusproject,out_rec.chi_product_no,out_rec.stockout_modeltype,out_rec.stockout_spec,out_rec.stockout_num,accdate1,accdate2,true,out_rec.scheduled_date) ;
                   end if ;
                   /* nnum = nnum + 1 ; */
                   select max(id) into accmaxid from neweb_acceptance where stockout_no=out_rec.name and active=true ;
                   if accmaxid is not null then
                      select getpurchaseno(out_rec.stockout_sequence_id) into purno ;
                      select getpursupplier(out_rec.stockout_sequence_id) into sup ;
                      select getpurchasedate(out_rec.stockout_sequence_id) into purdate ;
                      if purno is not null then
                         insert into neweb_acceptance_line(acceptance_id,project_no,project_no1,purchase_no,purchase_date,stockout_no,acceptance_status,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,prod_num,acceptanced_date1,acceptanced_date2,active,supplier,projsaleitem_id,accym) values
                               (accmaxid,projid,out_rec.stockout_proj_no,purno,purdate,out_rec.pickingid,'1',projsale,cusname,cusproject,out_rec.chi_product_no,out_rec.stockout_modeltype,out_rec.stockout_spec,out_rec.stockout_num,accdate1,accdate2,true,sup,out_rec.stockout_sequence_id,cym) ;
                      end if ;    
                      if out_rec.stockout_sequence_id is not null then
                         select get_stockout_date(out_rec.stockout_sequence_id) into soutdate ;
                         select max(id) into accmaxid1 from neweb_acceptance_line ;
                         update neweb_acceptance_line set stockout_date=soutdate where id = accmaxid1 and active=true ;
                      end if ;
                      if out_rec.stockout_sequence_id is not null then
                         select get_stockin_date(out_rec.stockout_sequence_id) into sindate ;
                         select max(id) into accmaxid1 from neweb_acceptance_line ;
                         update neweb_acceptance_line set stockin_date=sindate where id = accmaxid1 and active=true ;
                      end if ;    
                   end if ;       
                 end loop ;
                 close out_cur ;
             end if ;    
           end loop ;
           close p_cur ;
           open inv_cur for select * from neweb_invoice_invoiceopen where 
                abs(project_amount_total - open_complete_total) <= 10  or acc_sale_close=TRUE ;
           loop
              fetch inv_cur into inv_rec ;
              exit when not found ;
              update neweb_acceptance set acceptance_status='2',active=false where project_no=inv_rec.project_no ;
           end loop ;
           close inv_cur ;
           open p_cur for select id,active from neweb_acceptance where active=true ;
           loop
              fetch p_cur into p_rec ;
              exit when not found ;
              select count(*) into ncount1 from neweb_acceptance_line where acceptance_id=p_rec.id and active=true and prod_modeltype is not null;
              if ncount1 = 0 then
                 delete from neweb_acceptance where id = p_rec.id ;
              end if ;
           end loop ;
           close p_cur ;
           update neweb_acceptance set acceptance_status='2',active=false where project_no in (select id from neweb_project where acceptanced_date2 is not null and acceptanced_date2 <= mynowdate) ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 透過 pitem_origin_id 專案明細源id 找出採購單號
        self._cr.execute("""drop function if exists getpurchaseno(seqid int) cascade""")
        self._cr.execute("""create or replace function getpurchaseno(seqid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           pitemid int ;
         BEGIN
           select pitem_id into pitemid from neweb_pitem_list where pitem_origin_id=seqid ;
           if pitemid is not null then
              select name into myres from purchase_order where id=pitemid ;
           else
              myres = ' ' ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 透過 pitem_origin_id 專案明細源id 找出採購日期
        self._cr.execute("""drop function if exists getpurchasedate(seqid int) cascade""")
        self._cr.execute("""create or replace function getpurchasedate(seqid int) returns DATE as $BODY$
         DECLARE
           myres DATE ;
           pitemid int ;
         BEGIN
           select pitem_id into pitemid from neweb_pitem_list where pitem_origin_id=seqid ;
           if pitemid is not null then
              select date_order into myres from purchase_order where id=pitemid ;
           else
              myres = null ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 透過 pitem_origin_id 專案明細源id 找出 供應商簡名
        self._cr.execute("""drop function if exists getpursupplier(seqid int) cascade""")
        self._cr.execute("""create or replace function getpursupplier(seqid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           pitemid int ;
           partnerid int ;
         BEGIN
           select pitem_id into pitemid from neweb_pitem_list where pitem_origin_id=seqid ;
           if pitemid is not null then
              select partner_id into partnerid from purchase_order where id=pitemid ;
              select comp_sname into myres from res_partner where id=partnerid ;
           else
              myres = ' ' ;   
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 找出並寫入 neweb_acceptance 貨品明細的採購單號,供應商
        self._cr.execute("""drop function if exists gen_purno_supp() cascade""")
        self._cr.execute("""create or replace function gen_purno_supp() returns void as $BODY$
         DECLARE
           acc_cur refcursor ;
           acc_rec record ;
           accl_cur refcursor ;
           accl_rec record ;
           purno varchar ;
           supp varchar ;
           purdate date ;
           suppdate date ;
         BEGIN
           open acc_cur for select * from neweb_acceptance where active=True ;
           loop
             fetch acc_cur into acc_rec ;
             exit when not found ;
             purno=' ';
             supp=' ';
             open accl_cur for select distinct purchase_no from neweb_acceptance_line where acceptance_id=acc_rec.id ;
             loop
                fetch accl_cur into accl_rec ;
                exit when not found ;
                if purno=' ' then
                   purno = accl_rec.purchase_no ;
                else
                   purno = concat(purno,',',accl_rec.purchase_no) ;
                end if ;
             end loop ;
             close accl_cur ;
             open accl_cur for select distinct supplier from neweb_acceptance_line where acceptance_id=acc_rec.id ;
             loop
                fetch accl_cur into accl_rec ;
                exit when not found ;
                if supp=' ' then
                   supp = accl_rec.supplier ;
                else
                   supp = concat(supp,',',accl_rec.supplier) ;
                end if ;
             end loop ;
             close accl_cur ;
             update neweb_acceptance set purchase_no=purno,supplier=supp where id=acc_rec.id ;
           end loop ;
           close acc_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 要 scan neweb_acceptance 開完 invoice 的記錄將其 active=False
        self._cr.execute("""drop function if exists genprojinvcomplete() cascade;""")
        self._cr.execute("""create or replace function genprojinvcomplete() returns void as $BODY$
         DECLARE
          inv_cur refcursor ;
          inv_rec record ;
          projamounttot float ;
          nowtoday date ;
          ncount int ;
         BEGIN
           select current_timestamp::DATE into nowtoday ;
           open inv_cur for select * from neweb_invoice_invoiceopen ;
           loop
             fetch inv_cur into inv_rec ;
             exit when not found ;
             
             /* select getsalediscountamount(inv_rec.id) into projamounttot ; */
             select project_amount_total into projamounttot from neweb_invoice_invoiceopen where id = inv_rec.id ;
             if abs(inv_rec.project_amount_total - inv_rec.open_complete_total) <= 10 or inv_rec.open_complete_total >= inv_rec.project_amount_total or inv_rec.acc_sale_close = TRUE then
                update neweb_project set projsaleitem_completed=True where id=inv_rec.project_no ;
                update neweb_acceptance set active=FALSE,acceptance_status='2' where project_no = inv_rec.project_no ;
             else
                select count(*) into ncount from neweb_project where id=inv_rec.project_no and acceptanced_date2 is not null and acceptanced_date2 <= nowtoday ;
                if ncount = 0 then
                   update neweb_project set projsaleitem_completed=False where id=inv_rec.project_no ;
                   update neweb_acceptance set active=TRUE,acceptance_status='1' where project_no = inv_rec.project_no ;
                end if ;   
             end if ;
           end loop ;
           close inv_cur ;
           update neweb_project set projsaleitem_completed=TRUE where projsaleitem_completed=FALSE and acceptanced_date2 is not null and acceptanced_date2 <= nowtoday ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 產生每月初要發信給業務的 neweb_acceptance 清單;要請業務上線填寫 貨品狀態現況
        self._cr.execute("""drop function if exists genacceptanceemail() cascade""")
        self._cr.execute("""create or replace function genacceptanceemail() returns void as $BODY$
          DECLARE
            acc_cur refcursor ;
            acc_rec record ;
            accl_cur refcursor ;
            accl_rec record ;
            mynowdate date ;
            mymaxid int ;
            accstatus char ;
            urladdr varchar ;
            urladdr1 varchar ;
            cym varchar ;
            ncount int ;
            ncount1 int ;
            mysenddate date ;
          BEGIN
            delete from neweb_acceptance_email_line ;
            delete from neweb_acceptance_email ;
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
            cym = concat(date_part('year',mynowdate)::TEXT,'-',lpad(date_part('month',mynowdate)::TEXT,2,'0')) ;
            mysenddate = concat(cym,'-01')::DATE ;
            select config_value into urladdr from neweb_acceptance_config where config_key='url_address' ;
            select config_value into urladdr1 from neweb_acceptance_config where config_key='url_address1' ;
            open acc_cur for select distinct proj_sale from neweb_acceptance where active=TRUE and proj_sale in (select id from hr_employee where active=True) ;
            loop
              fetch acc_cur into acc_rec ;
              exit when not found ;
              select count(*) into ncount from neweb_acceptance_email where proj_sale=acc_rec.proj_sale and accym=cym and active=TRUE ;
              if ncount = 0 then
                 insert into neweb_acceptance_email(proj_sale,send_date,url_address,url_address1,accym,active) values (acc_rec.proj_sale,mysenddate,urladdr,urladdr1,cym,True) ;
              else
                 update neweb_acceptance_email set url_address=urladdr,url_address1=urladdr1 where proj_sale=acc_rec.proj_sale and accym=cym and active=TRUE ;   
              end if ;   
            end loop ;
            close acc_cur ;
            open acc_cur for select * from neweb_acceptance where active=TRUE order by proj_sale ;
            loop
              fetch acc_cur into acc_rec ;
              exit when not found ;
              select max(id) into mymaxid from neweb_acceptance_email where proj_sale=acc_rec.proj_sale and active=TRUE ;
              select count(*) into ncount1 from neweb_acceptance_email_line where line_id=mymaxid and stockout_no=acc_rec.stockout_no ;
              if ncount1 = 0 then
                 insert into neweb_acceptance_email_line(line_id,project_no,stockout_no,cus_name,acceptanced_date1,stockin_date,stockout_date,projsaleitem_status) values
                  (mymaxid,acc_rec.project_no,acc_rec.stockout_no,acc_rec.cus_name,acc_rec.acceptanced_date1,acc_rec.stockin_date,acc_rec.stockout_date,acc_rec.projsaleitem_status) ;  
              end if ;
            end loop ;
            close acc_cur ;
            
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 將 整理好的 neweb_acceptance 賦予權限組
        self._cr.execute("""drop function if exists genaccsecurity() cascade""")
        self._cr.execute("""create or replace function genaccsecurity() returns void as $BODY$
         DECLARE
          acc_cur refcursor ;
          acc_rec record ;
          parentid int ;
          userid int ;
         BEGIN
           open acc_cur for select id,proj_sale,active from neweb_acceptance where active=TRUE ;
           loop
             fetch acc_cur into acc_rec ;
             exit when not found ;
             select user_id,parent_id into userid,parentid from hr_employee where id = acc_rec.proj_sale ;
             update neweb_acceptance set own_user1=userid where id = acc_rec.id ;
             if parentid is not null then
                select user_id into userid from hr_employee where id = parentid ;
                if userid is not null then
                   update neweb_acceptance set own_user2=userid where id = acc_rec.id ;
                end if ;
             end if ;
           end loop ;
           close acc_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 每日異動 cronjob 執行 gennewprojacceptace() => neweb_acceptance 的最新狀態
        self._cr.execute("""drop function if exists gennewprojacceptance() cascade""")
        self._cr.execute("""create or replace function gennewprojacceptance() returns void as $BODY$
         DECLARE
           p_cur refcursor ;  /* neweb_project refcursor*/
           p_rec record ;
           pickid int ;
           out_cur refcursor ; /* neweb_stockout_list_view refcursor*/
           out_rec record ;
           inv_cur refcursor ;
           inv_rec record ;
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           projid int ;
           projsale int ;
           cusname int ;
           cusproject varchar ;
           accdate1 date ;
           accdate2 date ;
           accmaxid int ;
           purno varchar ;
           sup varchar ;
           sindate date ;
           soutdate date ;
           mynowdate date ;
           cym varchar ;
           purdate date ;
           projdate date ;
         BEGIN
           select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
           cym = concat(date_part('year',mynowdate)::TEXT,'-',lpad(date_part('month',mynowdate)::TEXT,2,'0')) ;
           open p_cur for select id,proj_sale,name from neweb_project  where projsaleitem_completed=false or projsaleitem_completed is null;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select count(*) into ncount1 from neweb_projsaleitem where saleitem_id =  p_rec.id and purchase_no is not null ;
             if ncount1 > 0 then   /* 已發採購單的記錄 */
                 open out_cur for select * from neweb_stockout_list_view where stockout_proj_no=p_rec.name order by name,outlist_id ;
                 loop
                   fetch out_cur into out_rec ;
                   exit when not found ;
                   select id,proj_sale,cus_name,cus_project,acceptanced_date1,acceptanced_date2,create_date into projid,projsale,cusname,cusproject,accdate1,accdate2,projdate from neweb_project where name=out_rec.stockout_proj_no ;
                   select count(*) into ncount from neweb_acceptance where stockout_no=out_rec.name and active=true ;
                   if ncount = 0  then
                      insert into neweb_acceptance(project_no,project_no1,stockout_no,stockout_no1,acceptance_status,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,prod_num,acceptanced_date1,acceptanced_date2,active,stockout_date,proj_date) values
                       (projid,out_rec.stockout_proj_no,out_rec.name,out_rec.pickingid,'1',projsale,cusname,cusproject,out_rec.chi_product_no,out_rec.stockout_modeltype,out_rec.stockout_spec,out_rec.stockout_num,accdate1,accdate2,true,out_rec.scheduled_date,projdate) ;
                   else
                      update neweb_acceptance set proj_date=projdate where stockout_no=out_rec.name and active=true ;    
                   end if ;
                   select max(id) into accmaxid from neweb_acceptance where stockout_no=out_rec.name and active=true ;
                   if accmaxid is not null then
                       select getpurchaseno(out_rec.stockout_sequence_id) into purno ;
                       select getpurchasedate(out_rec.stockout_sequence_id) into purdate ;
                       select getpursupplier(out_rec.stockout_sequence_id) into sup ;
                       select get_stockout_date(out_rec.stockout_sequence_id) into soutdate ;
                       select get_stockin_date(out_rec.stockout_sequence_id) into sindate ;
                       select count(*) into ncount2 from neweb_acceptance_line where acceptance_id=accmaxid and prod_modeltype=out_rec.stockout_modeltype and prod_num=out_rec.stockout_num and active=true ;
                       if ncount = 0 then
                          insert into neweb_acceptance_line(acceptance_id,project_no,project_no1,purchase_no,purchase_date,stockout_no,acceptance_status,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,prod_num,acceptanced_date1,acceptanced_date2,active,supplier,projsaleitem_id,stockin_date,stockout_date,accym,proj_date) values
                              (accmaxid,projid,out_rec.stockout_proj_no,purno,purdate,out_rec.pickingid,'1',projsale,cusname,cusproject,out_rec.chi_product_no,out_rec.stockout_modeltype,out_rec.stockout_spec,out_rec.stockout_num,accdate1,accdate2,true,sup,out_rec.stockout_sequence_id,sindate,soutdate,cym,projdate) ;
                              
                       else
                          update neweb_acceptance_line set purchase_no=purno,purchase_date=purdate,stockout_no1=out_rec.pickingid,prod_num=out_rec.stockout_num,acceptanced_date1=accdate1,prod_no=out_rec.chi_product_no,
                            acceptanced_date2=accdate2,supplier=sup,stockout_date=soutdate,stockin_date=sindate,project_no=projid,project_no1=out_rec.stockout_proj_no,cus_name=cusname,cus_project=cusproject,proj_date=projdate 
                            where acceptance_id=accmaxid and prod_modeltype=out_rec.stockout_modeltype and prod_num=out_rec.stockout_num and active=true;
                       end if ;
                   end if ;        
                 end loop ;
                 close out_cur ;
             end if ;    
           end loop ;
           close p_cur ;
           open inv_cur for select * from neweb_invoice_invoiceopen where 
               abs(project_amount_total - open_complete_total) <= 10 or acc_sale_close = TRUE ;
           loop
              fetch inv_cur into inv_rec ;
              exit when not found ;
              update neweb_acceptance set acceptance_status='2',active=false where project_no=inv_rec.project_no ;
           end loop ;
           close inv_cur ;
           update neweb_acceptance set acceptance_status='2',active=false where project_no in (select id from neweb_project where projsaleitem_completed=TRUE) and active=TRUE  ;
           update neweb_acceptance set acceptance_status='2',active=false where project_no in (select id from neweb_project where acceptanced_date2 is not null and acceptanced_date2 <= mynowdate) ;
           open p_cur for select id,active from neweb_acceptance where active=true ;
           loop
              fetch p_cur into p_rec ;
              exit when not found ;
              select count(*) into ncount1 from neweb_acceptance_line where acceptance_id=p_rec.id and active=true and prod_modeltype is not null;
              if ncount1 = 0 then
                 delete from neweb_acceptance where id = p_rec.id ;
              end if ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 抓出 業務員(員工主檔) 集合
        self._cr.execute("""drop function if exists get_proj_sale() cascade""")
        self._cr.execute("""create or replace function get_proj_sale() returns setof int as $BODY$
         DECLARE
           myres int ;
           emp_cur refcursor ;
           emp_rec record ;
         BEGIN
           open emp_cur for select id from hr_employee where id in (select distinct proj_sale from neweb_project) ;
           loop
             fetch emp_cur into emp_rec ;
             exit when not found ;
             return next emp_rec.id ;
           end loop ;
           close emp_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 找出 專案成本分析明細記錄的 出貨日期
        self._cr.execute("""drop function if exists get_stockout_date(projsaleitemid int) cascade""")
        self._cr.execute("""create or replace function get_stockout_date(projsaleitemid int) returns DATE as $BODY$
         DECLARE
           ncount int ;
           myres DATE ;
           soutid int ;
         BEGIN
           select count(*) into ncount from neweb_stockout_list where stockout_sequence_id=projsaleitemid ;
           if ncount > 0 then
              select stockout_id into soutid from neweb_stockout_list where stockout_sequence_id=projsaleitemid ;
              select scheduled_date into myres from stock_picking where id = soutid ;
           else
              myres = null ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        # 找出 專案成本分析明細記錄的 進貨日期
        self._cr.execute("""drop function if exists get_stockin_date(projsaleitemid int) cascade""")
        self._cr.execute("""create or replace function get_stockin_date(projsaleitemid int) returns DATE as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           myres DATE ;
           sinid int ;
           pitemid int ;
         BEGIN
           select count(*) into ncount from neweb_pitem_list where pitem_origin_id = projsaleitemid ;
           if ncount > 0 then
              select id into pitemid from neweb_pitem_list where pitem_origin_id=projsaleitemid ;
              select stockin_id into sinid from neweb_stockin_list where stockin_sequence_id=pitemid ;
              select scheduled_date into myres from stock_picking where id = sinid ;
           else
              myres = null ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        # 將每一版次的 貨品狀態履歷記錄寫進 neweb_acceptance_acc_list
        self._cr.execute("""drop function if exists genacceptancelist(accid int) cascade""")
        self._cr.execute("""create or replace function genacceptancelist(accid int) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
         BEGIN
           open l_cur for select * from neweb_acceptance_line where acceptance_id=accid and proj_date >= '2022-01-01'::DATE order by id ;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             insert into neweb_acceptance_acc_list(acceptance_id,keyin_date,purchase_no,stockout_no,project_no,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,
             prod_num,supplier,acceptanced_date1,stockin_date,stockout_date,acceptanced_date2,projsaleitem_status,memo,accym,projsaleitem_id,active) values 
             (l_rec.acceptance_id,l_rec.keyin_date,l_rec.purchase_no,l_rec.stockout_no,l_rec.project_no,l_rec.proj_sale,l_rec.cus_name,l_rec.cus_project,l_rec.prod_no,
             l_rec.prod_modeltype,l_rec.prod_desc,l_rec.prod_num,l_rec.supplier,l_rec.acceptanced_date1,l_rec.stockin_date,l_rec.stockout_date,l_rec.acceptanced_date2,
             l_rec.projsaleitem_status,l_rec.memo,l_rec.accym,l_rec.projsaleitem_id,true) ;
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 將每一版次的 貨品狀態履歷記錄寫進 neweb_acceptance_acc_list
        self._cr.execute("""drop function if exists genacceptancelist1(saleid int,startym varchar,endym varchar) cascade""")
        self._cr.execute("""create or replace function genacceptancelist1(saleid int,startym varchar,endym varchar) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
         BEGIN
           if saleid = 0 then
              open l_cur for select * from neweb_acceptance_line where accym >= startym and accym <= endym and proj_date >= '2022-01-01'::DATE order by proj_sale,accym,project_no1;
           else
              open l_cur for select * from neweb_acceptance_line where proj_sale=saleid and accym >= startym and accym <= endym and proj_date >= '2022-01-01'::DATE order by proj_sale,accym,project_no1;
           end if ;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             insert into neweb_acceptance_acc_list(acceptance_id,keyin_date,purchase_no,stockout_no,project_no,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,
             prod_num,supplier,acceptanced_date1,stockin_date,stockout_date,acceptanced_date2,projsaleitem_status,memo,accym,projsaleitem_id,active) values 
             (l_rec.acceptance_id,l_rec.keyin_date,l_rec.purchase_no,l_rec.stockout_no,l_rec.project_no,l_rec.proj_sale,l_rec.cus_name,l_rec.cus_project,l_rec.prod_no,
             l_rec.prod_modeltype,l_rec.prod_desc,l_rec.prod_num,l_rec.supplier,l_rec.acceptanced_date1,l_rec.stockin_date,l_rec.stockout_date,l_rec.acceptanced_date2,
             l_rec.projsaleitem_status,l_rec.memo,l_rec.accym,l_rec.projsaleitem_id,true) ;
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 將每一版次的 貨品狀態履歷記錄寫進 neweb_acceptance_acc_list
        self._cr.execute("""drop function if exists genacceptancelist2(wizid int,startym varchar,endym varchar) cascade""")
        self._cr.execute("""create or replace function genacceptancelist2(wizid int,startym varchar,endym varchar) returns void as $BODY$
        DECLARE
          l_cur refcursor ;
          l_rec record ;
        BEGIN
          open l_cur for select * from neweb_acceptance_line where accym >= startym and accym <= endym
            and project_no in (select proj_id from neweb_project_export_wizard_rel1 where wiz_id=wizid) 
            and proj_date >= '2022-01-01'::DATE order by proj_sale,accym,project_no1;
          loop
            fetch l_cur into l_rec ;
            exit when not found ;
            insert into neweb_acceptance_acc_list(acceptance_id,keyin_date,purchase_no,stockout_no,project_no,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,
            prod_num,supplier,acceptanced_date1,stockin_date,stockout_date,acceptanced_date2,projsaleitem_status,memo,accym,projsaleitem_id,active) values 
            (l_rec.acceptance_id,l_rec.keyin_date,l_rec.purchase_no,l_rec.stockout_no,l_rec.project_no,l_rec.proj_sale,l_rec.cus_name,l_rec.cus_project,l_rec.prod_no,
            l_rec.prod_modeltype,l_rec.prod_desc,l_rec.prod_num,l_rec.supplier,l_rec.acceptanced_date1,l_rec.stockin_date,l_rec.stockout_date,l_rec.acceptanced_date2,
            l_rec.projsaleitem_status,l_rec.memo,l_rec.accym,l_rec.projsaleitem_id,true) ;
          end loop ;
          close l_cur ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 從 neweb_invoice_invoiceopen 中找出合計金額-已開金額 < 10 的專案,並抓出最後驗收日期
        self._cr.execute("""drop function if exists getinvoiceopendate(projid int) cascade""")
        self._cr.execute("""create or replace function getinvoiceopendate(projid int) returns DATE as $BODY$
          DECLARE
            myres date ;
            ncount int ;
            maxid int ;
            inv_cur refcursor ;
            inv_rec record ;
          BEGIN
            myres = NULL ;
            open inv_cur for select * from neweb_invoice_invoiceopen where project_no=projid ;
            loop
              fetch inv_cur into inv_rec ;
              exit when not found ;
              if (abs(inv_rec.project_amount_total - inv_rec.open_complete_total) <= 15) and (inv_rec.project_amount_total > 0) then
                  select max(id) into maxid from neweb_invoice_invoiceopen_line where invoice_id=inv_rec.id and invoice_state in ('2','3') ;
                  if maxid is not null then
                     select invoice_date into myres from neweb_invoice_invoiceopen_line where id = maxid ;
                  end if ;
              end if ;
            end loop ;
            close inv_cur ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 產出專案 實際驗收日期 並寫入 neweb_project acceptanced_date2
        self._cr.execute("""drop function if exists genacceptancedate() cascade""")
        self._cr.execute("""create or replace function genacceptancedate() returns void as $BODY$
         DECLARE
           p_cur refcursor ;
           p_rec record ;
           accdate date ;
         BEGIN
           open p_cur for select id,acceptanced_date1,acceptanced_date2 from neweb_project where acceptanced_date2 is null ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select getinvoiceopendate(p_rec.id) into accdate ;
             if accdate is not null then
                if p_rec.acceptanced_date1 is null then
                   update neweb_project set acceptanced_date1=accdate,acceptanced_date2=accdate,projsaleitem_completed=true where id = p_rec.id ;
                else
                   update neweb_project set acceptanced_date2=accdate,projsaleitem_completed=true where id = p_rec.id ;
                end if ;
             end if ;
             update neweb_acceptance set acceptanced_date1=p_rec.acceptanced_date1,acceptanced_date2=p_rec.acceptanced_date2 where project_no=p_rec.id ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists ismonth1day() cascade""")
        self._cr.execute("""create or replace function ismonth1day() returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           nday int ;
           mynowdate DATE ;
         BEGIN
           select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
           select date_part('day',mynowdate)::INT into nday ;
           if nday = 1 then
              myres = True ;
           else
              myres = False ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_uncomplete_invoice(saleid int) cascade""")
        self._cr.execute("""create or replace function gen_uncomplete_invoice(saleid int) returns void as $BODY$
          DECLARE
            u_cur refcursor ;
            u_rec record ;
            ncount int ;
            havesale Boolean ;
            accdate2 date ;
            nowtoday date ;
          BEGIN
            select current_timestamp::DATE into nowtoday ;
            delete from neweb_acceptance_uncomplete_list ;
            if saleid > 0 then 
               open u_cur for select * from neweb_uncomplete_invoice_view where proj_sale=saleid order by proj_sale,project_no ;
            else
               open u_cur for select * from neweb_uncomplete_invoice_view  order by proj_sale,project_no ;
            end if ;
            loop
              fetch u_cur into u_rec ;
              exit when not found ;
              select acceptanced_date2 into accdate2 from neweb_project where id = u_rec.project_no ;
              select chkprojsaletype(u_rec.project_no) into havesale ;
              if havesale = TRUE then
                 select count(*) into ncount from neweb_acceptance_uncomplete_list where project_no=u_rec.project_no ;
                 if ncount = 0 and u_rec.project_no is not null then
                    if accdate2 is null then 
                       insert into neweb_acceptance_uncomplete_list(project_no,contract_no,cus_name,main_cus_name,project_amount_total,open_complete_total,proj_sale) values
                           (u_rec.project_no,u_rec.contract_no,u_rec.cus_name,u_rec.main_cus_name,u_rec.project_amount_total,u_rec.open_complete_total,u_rec.proj_sale) ;
                    end if ;       
                 end if ; 
              end if ;   
            end loop ;
            close u_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genacceptancelist3(accid int) cascade""")
        self._cr.execute("""create or replace function genacceptancelist3(accid int) returns void as $BODY$
          DECLARE
            ncount int ;
            accdate1 date ;
            accdate2 date ;
            l_cur refcursor ;
            l_rec record ;
            mynowdate date ;
            maxaccym varchar ;
          BEGIN
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
            select acceptanced_date1,acceptanced_date2 into accdate1,accdate2 from neweb_acceptance where id =accid ;
            if (accdate2 > accdate1 and accdate1 is not null) or (accdate2 is null and accdate1 > mynowdate) then
                select max(accym) into maxaccym from neweb_acceptance_line where acceptance_id=accid ;
                open l_cur for select * from neweb_acceptance_line where acceptance_id=accid and accym=maxaccym order by id ;
                loop
                   fetch l_cur into l_rec ;
                   exit when not found ;
                   insert into neweb_acceptance_acc_list(acceptance_id,keyin_date,purchase_no,stockout_no,project_no,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,
                     prod_num,supplier,acceptanced_date1,stockin_date,stockout_date,acceptanced_date2,projsaleitem_status,memo,accym,projsaleitem_id,active) values 
                     (l_rec.acceptance_id,l_rec.keyin_date,l_rec.purchase_no,l_rec.stockout_no,l_rec.project_no,l_rec.proj_sale,l_rec.cus_name,l_rec.cus_project,l_rec.prod_no,
                     l_rec.prod_modeltype,l_rec.prod_desc,l_rec.prod_num,l_rec.supplier,l_rec.acceptanced_date1,l_rec.stockin_date,l_rec.stockout_date,l_rec.acceptanced_date2,
                     l_rec.projsaleitem_status,l_rec.memo,l_rec.accym,l_rec.projsaleitem_id,true) ;
                end loop ;
                close l_cur ;  
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genacceptancelist4(saleid int,sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function genacceptancelist4(saleid int,sdate date,edate date) returns void as $BODY$
          DECLARE
            ncount int ;
            accdate1 date ;
            accdate2 date ;
            a_cur refcursor ;
            a_rec record ;
            l_cur refcursor ;
            l_rec record ;
            mynowdate date ;
            maxaccym varchar ;
            acceptanceddate2 date ;
          BEGIN
            delete from neweb_acceptance_acc_list ;
            select (current_timestamp + interval '8 hour')::DATE into mynowdate ;

            if saleid = 0 then
               open a_cur for select * from neweb_acceptance where ((acceptanced_date2 > acceptanced_date1) or 
                  (acceptanced_date1 < mynowdate and acceptanced_date2 is null)) and proj_date >= sdate and proj_date <= edate 
                   order by project_no ;
            else
               open a_cur for select * from neweb_acceptance where ((acceptanced_date2 > acceptanced_date1) or 
                  (acceptanced_date1 < mynowdate and acceptanced_date2 is null)) and proj_date >= sdate 
                  and proj_date <= edate and proj_sale=saleid order by project_no ;
            end if ; 
            loop
               fetch a_cur into a_rec ;
               exit when not found ;
               select max(accym) into maxaccym from neweb_acceptance_line where acceptance_id=a_rec.id ;
               if saleid = 0 then
                  open l_cur for select * from neweb_acceptance_line where acceptance_id=a_rec.id 
                       and accym=maxaccym  order by id ;
               else
                  open l_cur for select * from neweb_acceptance_line where acceptance_id=a_rec.id 
                       and accym=maxaccym and proj_sale=saleid order by id ;
               end if ;        
                loop
                   fetch l_cur into l_rec ;
                   exit when not found ;
                   if l_rec.acceptanced_date2 is null then
                       select acceptanced_date2 into acceptanceddate2 from neweb_project where id = l_rec.project_no ;
                   else
                       acceptanceddate2 = l_rec.acceptanced_date2 ;    
                   end if ;
                   insert into neweb_acceptance_acc_list(acceptance_id,keyin_date,purchase_no,stockout_no,project_no,proj_sale,cus_name,cus_project,prod_no,prod_modeltype,prod_desc,
                     prod_num,supplier,acceptanced_date1,stockin_date,stockout_date,acceptanced_date2,projsaleitem_status,memo,accym,projsaleitem_id,active) values 
                     (l_rec.acceptance_id,l_rec.keyin_date,l_rec.purchase_no,l_rec.stockout_no,l_rec.project_no,l_rec.proj_sale,l_rec.cus_name,l_rec.cus_project,l_rec.prod_no,
                     l_rec.prod_modeltype,l_rec.prod_desc,l_rec.prod_num,l_rec.supplier,l_rec.acceptanced_date1,l_rec.stockin_date,l_rec.stockout_date,acceptanceddate2,
                     l_rec.projsaleitem_status,l_rec.memo,l_rec.accym,l_rec.projsaleitem_id,true) ;
                end loop ;
                close l_cur ; 
            end loop ;
            close a_cur ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getcosttypemix(projid int) cascade""")
        self._cr.execute("""create or replace function getcosttypemix(projid int) returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           ncount int ;
           ncount1 int ;
         BEGIN
           select count(distinct cost_type) into ncount from neweb_projsaleitem where 
              saleitem_id = projid and cost_type in (1,3,4,5,9) ;
           select count(*) into ncount1 from neweb_projsaleitem where cost_type=1 and saleitem_id=projid ;   
           if ncount > 1 and ncount1 > 0 then  /* 代表本案是有銷貨在內之混合專案 */
              myres = TRUE ;
           else
              myres = FALSE ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getaccprojno(wizid int) cascade""")
        self._cr.execute("""create or replace function getaccprojno(wizid int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           p_cur refcursor ;
           p_rec record ;
           projno varchar ;
         BEGIN
           myres='' ; 
           open p_cur for select proj_id from neweb_project_export_wizard_rel1 where wiz_id=wizid ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select name into projno from neweb_project where id = p_rec.proj_id ;
             if myres='' then
                myres = projno ;
             else
                myres = concat(myres,'/',projno) ;
             end if ;
           end loop ;
           close p_cur ;
           if myres = '' then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallacceptancedate() cascade""")
        self._cr.execute("""create or replace function genallacceptancedate() returns void as $BODY$
         DECLARE
           p_cur refcursor ;
           p_rec record ;
           accdate date ;
         BEGIN
           open p_cur for select id,acceptanced_date1,acceptanced_date2 from neweb_project  ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             update neweb_acceptance set acceptanced_date1=p_rec.acceptanced_date1,acceptanced_date2=p_rec.acceptanced_date2 where project_no=p_rec.id ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")




