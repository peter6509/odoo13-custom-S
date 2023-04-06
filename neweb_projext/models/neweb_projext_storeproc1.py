# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api


class newebprojextstoreproc(models.Model):
    _name = "neweb_projext.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genstockout_projno(projid int) cascade;""")
        self._cr.execute("""create or replace function genstockout_projno(projid int) returns void as $BODY$
            declare 
              ncount int ;
              myprojno VARCHAR;
              mysaleno VARCHAR ;
            begin 
              myprojno := 'None' ;
              mysaleno := 'None' ;
              select count(*) into ncount from neweb_project where id = projid ;
              if ncount > 0 then
                 select name,sale_no into myprojno,mysaleno from neweb_project where id=projid ; 
              end if ;
              select count(*) into ncount from stock_picking where origin like mysaleno ;
              if ncount > 0 then 
                 update stock_picking set stockout_proj_no=myprojno where origin like mysaleno ;
              end if ;
            end; $BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallstockoutprojno() cascade;""")
        self._cr.execute("""create or replace function genallstockoutprojno() returns void as $BODY$
             declare 
               proj_cur refcursor ;
               proj_rec record ;
               ncount int ;
             begin 
               open proj_cur for select name,sale_no from neweb_project ;
               loop
                 fetch proj_cur into proj_rec ;
                 exit when not found ;
                 select count(*) into ncount from stock_picking where origin like proj_rec.sale_no ;
                 if ncount > 0 then
                    update stock_picking set stockout_proj_no = proj_rec.name where origin like proj_rec.sale_no ; 
                 end if ;
               end loop ;
               close proj_cur ;
             end; $BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmainrec(myprojid int) cascade;""")
        self._cr.execute("""create or replace function genmainrec(myprojid int) returns void as $BODY$
             declare 
               ncount int ;
               mycallserviceresponse int ;
               myroutinemaintenancenew int ;
               mymainservicerulenew int ;
               mysaleno varchar;
             begin 
               select count(*) into ncount from neweb_project where id=myprojid and sale_no is not null ;
               if ncount > 0 then
                  select sale_no into mysaleno from neweb_project where id=myprojid ;
                  select call_service_response1,routine_maintenance_new,main_service_rule_new into 
                     mycallserviceresponse,myroutinemaintenancenew,mymainservicerulenew from sale_order
                     where name like mysaleno ; 
                  if mycallserviceresponse is not null then 
                     update neweb_project set call_service_response=mycallserviceresponse where id=myprojid ;
                  end if ;  
                  if myroutinemaintenancenew is not null then 
                     update neweb_project set routine_maintenance_new=myroutinemaintenancenew where id=myprojid ;
                  end if ;
                  if mymainservicerulenew is not null then 
                     update neweb_project set main_service_rule_new=mymainservicerulenew where id=myprojid ;
                  end if ;
               end if ;
             end; $BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencreditlimit(projid int) cascade""")
        self._cr.execute("""create or replace function gencreditlimit(projid int) returns void as $BODY$
             declare 
               mycredit FLOAT;
               mycusid int;
               mycreditmemo varchar;
             begin 
               select cus_name into mycusid from neweb_project where id = projid ;
               select round(credit_limit) into mycredit from res_partner where id=mycusid ;
               mycreditmemo := concat(to_char(mycredit,'999,999,999'),'  元');
               update neweb_project set proj_info_memo=mycreditmemo where id = projid ;
             end ;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_cusproject(projid int) cascade""")
        self._cr.execute("""create or replace function check_cusproject(projid int) returns Boolean as $BODY$
             declare 
               ncount int;
               myresult Boolean;
             begin 
               select count(*) into ncount from neweb_project where id=projid and cus_project is null ;
               if ncount = 0 then 
                  myresult := True ;
               else 
                  myresult := False ;
               end if ;
               return myresult ;
             end ; $BODY$
             LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists check_projectname(saleid int) cascade""")
        self._cr.execute("""create or replace function check_projectname(saleid int) returns Boolean as $BODY$
             declare 
                ncount int;
                myresult Boolean;
             begin 
               select count(*) into ncount from sale_order where id=saleid and project_name is null ;
               if ncount = 0 then 
                  myresult := True ;
               else 
                  myresult := False ;
               end if ;
               return myresult ;
             end;$BODY$
             LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists getpayterm(cusid int) cascade""")
        self._cr.execute("""create or replace function getpayterm(cusid int) returns CHAR as $BODY$
            declare 
              ncount int;
              mytype CHAR;
              mypayterm varchar;
              mypaymentdays int ;
            begin 
              select count(*) into ncount from res_partner where id=cusid ;
              mytype := '0';
              if ncount >0 then
                 select payment_days into mypaymentdays from res_partner where id=cusid ;
                 if mypaymentdays <= 30 then
                    mytype := '1' ;
                 elsif mypaymentdays > 30 and mypaymentdays <= 45 then
                    mytype := '2' ;
                 elsif mypaymentdays > 45 and mypaymentdays <= 60 then   
                    mytype := '3' ;
                 elsif mypaymentdays > 60 and mypaymentdays <= 90 then  
                    mytype := '4' ;
                 else
                    mytype := '5' ;   
                 end if ;
              end if ;   
              return mytype ;              
            end;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists hasproj(saleorderid int) cascade""")
        self._cr.execute("""create or replace function hasproj(saleorderid int) returns Boolean as $BODY$
            declare 
              ncount int ;
              saleno varchar ;
              myresult Boolean ;
            begin
              myresult := False ;
              select name into saleno from sale_order where id=saleorderid ;
              select count(*) into ncount from neweb_project where sale_no=saleno ;
              if ncount > 0 then
                 myresult := True ;
              end if ;
              return myresult ;
            end ; $BODY$
            LANGUAGE plpgsql ; 
             """)

        self._cr.execute("""drop function if exists setpaymentterm(projid int) cascade""")
        self._cr.execute("""create or replace function setpaymentterm(projid int) returns void as $BODY$
            declare 
               ncount int ;
               mysaleno varchar ;
               paymentterm INT;
            begin 
               select payment_term_new into paymentterm from sale_order where name like (select sale_no from neweb_project where id=projid);
               if paymentterm is not null then 
                  update neweb_project set proj_pay1=paymentterm where id=projid ;
               end if ;
            end;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists hasdisamount(saleid int) cascade;""")
        self._cr.execute("""create or replace function hasdisamount(saleid int) returns Boolean as $BODY$
            declare 
              myres Boolean ;
              ncount INT;
            BEGIN 
              select count(*) into ncount from sale_order where id=saleid and discount_amount > 0 ;
              if ncount > 0 then 
                 myres := TRUE ;
              else 
                 myres := FALSE ;
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setprodserial(projid int) cascade;""")
        self._cr.execute("""create or replace function setprodserial(projid int) returns void as $BODY$
             DECLARE 
               ncount int ;
               proj_cur refcursor ;
               proj_rec record ;
             BEGIN 
               open proj_cur for select id,prod_serial from neweb_projsaleitem where saleitem_id = projid ;
               loop
                  fetch proj_cur into proj_rec ;
                  exit when not found ;
                  if proj_rec.prod_serial is not null then 
                     update neweb_stockship_list set prod_serial = proj_rec.prod_serial 
                         where stockout_sequence_id = proj_rec.id and prod_serial is null ; 
                  end if ;
               end loop ;
               close proj_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setallprodserial() cascade;""")
        self._cr.execute("""create or replace function setallprodserial() returns void as $BODY$
             DECLARE 
                proj_cur refcursor ;
                proj_rec record ;
                line_cur refcursor ;
                line_rec record ;
             BEGIN 
                open proj_cur for select id from neweb_project ;
                loop
                   fetch proj_cur into proj_rec;
                   exit when not found ;
                   open line_cur for select id,prod_serial from neweb_projsaleitem where saleitem_id = proj_rec.id ;
                   loop
                     fetch line_cur into line_rec ;
                     exit when not found ;
                     if line_rec.prod_serial is not null then 
                        update neweb_stockship_list set prod_serial = line_rec.prod_serial 
                            where stockout_sequence_id = line_rec.id and prod_serial is null ; 
                     end if ;
                   end loop ;
                   close line_cur ;
                end loop ;
                close proj_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkinvoiceprojsum(projid int) cascade;""")
        self._cr.execute("""create or replace function checkinvoiceprojsum(projid int) returns void as $BODY$
             DECLARE 
               ncount int;
               invoiceid int ;
             BEGIN
               select count(*) into ncount from neweb_invoice_invoiceopen where project_no=projid ;
               if ncount > 0 then 
                  select id into invoiceid from neweb_invoice_invoiceopen where project_no=projid ;
                  execute calinvoiceamount(invoiceid) ;
               end if ;
             END; $BODY$
             LANGUAGE plpgsql; """)

        self._cr.execute("""drop function if exists check_cus_address(projid int) cascade""")
        self._cr.execute("""create or replace function check_cus_address(projid int) returns void as $BODY$
             DECLARE 
                add_cur refcursor ;
                add_rec record ;
                myaddress varchar ;
             BEGIN 
                myaddress := ' ' ; 
                open add_cur for select * from neweb_projcustom where cus_id = projid  order by cus_address ;
                loop
                  fetch add_cur into add_rec ;
                  exit when not found ;
                  if myaddress = add_rec.cus_address then 
                     delete from neweb_projcustom where cus_id=projid and id = add_rec.id ;
                  else
                     myaddress := add_rec.cus_address ;
                  end if ;
                end loop ;
                close add_cur ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_all_address() cascade""")
        self._cr.execute("""create or replace function check_all_address() returns void as $BODY$
             DECLARE 
                proj_cur refcursor ;
                proj_rec record ; 
                add_cur refcursor ;
                add_rec record ;
                myaddress varchar ;
             BEGIN 
                open proj_cur for select id from neweb_project ;
                loop
                    fetch proj_cur into proj_rec ;
                    exit when not found ;
                    myaddress := ' ' ; 
                    open add_cur for select * from neweb_projcustom where cus_id = proj_rec.id  order by cus_address ;
                    loop
                      fetch add_cur into add_rec ;
                      exit when not found ;
                      if myaddress = add_rec.cus_address then 
                         delete from neweb_projcustom where cus_id=proj_rec.id and id = add_rec.id ;
                      else
                         myaddress := add_rec.cus_address ;
                      end if ;
                    end loop ;
                    close add_cur ;
                end loop ;
                close proj_cur ;    
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkispur(saleitemid int) cascade""")
        self._cr.execute("""create or replace function checkispur(saleitemid int) returns Boolean as $BODY$
             DECLARE 
                ncount int ;
                myres Boolean ;
             BEGIN 
                select count(*) into ncount from neweb_projsaleitem where id=saleitemid and purchase_no is not null ;
                if ncount > 0 then 
                   myres = TRUE  ;
                else 
                   myres = FALSE ;
                end if ;
                return myres ;
             END;$BODY$
             LANGUAGE plpgsql; """)

        self._cr.execute("""drop function if exists setallopaccday() cascade""")
        self._cr.execute("""create or replace function setallopaccday() returns void as $BODY$
            DECLARE
              proj_cur refcursor ;
              proj_rec record ;
              paydays int;
              accday char ;
            BEGIN
              open proj_cur for select id,open_account_day,cus_name from neweb_project where open_account_day is null ;
              loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                select payment_days into paydays from res_partner where id = proj_rec.cus_name ;
                if paydays <= 30 then
                   accday := '1' ;
                elsif paydays <= 45 and paydays > 30 then
                   accday := '2' ;
                elsif paydays <= 60 and paydays > 45 then
                   accday := '3' ;
                elsif paydays <= 90 and paydays > 60 then
                   accday := '4' ;
                else
                   accday := '5' ;
                end if ;
                update neweb_project set open_account_day=accday where id = proj_rec.id ;
              end loop;
              close proj_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists hasservicetype(engid int) cascade""")
        self._cr.execute("""create or replace function hasservicetype(engid int) returns Boolean as $BODY$
           DECLARE
             ncount int ;
             myres Boolean ;
           BEGIN
            select count(*) into ncount from neweb_ass_service_type_neweb_proj_eng_assign_rel where neweb_proj_eng_assign_id = engid ;
            if ncount > 0 then
               myres := True ;
            else
               myres := False ;
            end if ;
            return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencostdeptdata(projid int) cascade""")
        self._cr.execute("""create or replace function gencostdeptdata(projid int) returns void as $BODY$
           DECLARE
             pl_cur refcursor ;
             pl_rec record ;
             s_r6rev float = 0.0 ;
             s_r6mes float = 0.0 ;
             s_r6per float = 0.00 ;
             s_r6mesper float = 0.00 ;
             s_r6outcost float = 0.0 ;
             s_r6outper float = 0.00;
             m_r6rev float = 0.0 ;
             m_r6per float = 0.00 ;
             m_r6outcost float = 0.0 ;
             m_r6outper float = 0.00;
             m_r6mescost float = 0.0 ;
             m_r6mesper float = 0.00 ;
             s_ntrev float = 0.0 ;
             s_ntmes float = 0.0 ;
             s_ntper float = 0.00 ;
             s_ntmesper float = 0.00 ;
             s_ntoutcost float = 0.0 ;
             s_ntoutper float = 0.00;
             m_ntrev float = 0.0 ;
             m_ntper float = 0.00 ;
             m_ntoutcost float = 0.0 ;
             m_ntoutper float = 0.00;
             m_ntmescost float = 0.0 ;
             m_ntmesper float = 0.00 ;
             s_nwrev float = 0.0 ;
             s_nwmes float = 0.0 ;
             s_nwper float = 0.00 ;
             s_nwmesper float = 0.00 ;
             s_nwoutcost float = 0.0 ;
             s_nwoutper float = 0.00;
             m_nwrev float = 0.0 ;
             m_nwper float = 0.00 ;
             m_nwoutcost float = 0.0 ;
             m_nwoutper float = 0.00;
             m_nwmescost float = 0.0 ;
             m_nwmesper float = 0.00 ;
             m_suprev float = 0.0 ;
             m_supper float = 0.00 ;
             m_supoutcost float = 0.0 ;
             m_supoutper float = 0.00;
             m_supmescost float = 0.0 ;
             m_supmesper float = 0.00 ;
             ncount int ;
             ncount1 int ;
             subtotrevenue1 float = 0.0 ;
           BEGIN
             open pl_cur for select id,prod_num,prod_price,prod_revenue,cost_type,cost_dept from neweb_projsaleitem where
                saleitem_id = projid ;
             loop
               fetch pl_cur into pl_rec ;
               exit when not found ;
               if pl_rec.cost_type=3 then   /*  建置 */
                  if pl_rec.cost_dept in (2,3) then  /* R6 */
                     s_r6rev= s_r6rev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=3 then /* R6 MES COST */
                        s_r6mes = s_r6mes + (pl_rec.prod_num * pl_rec.prod_price) ;
                      elsif pl_rec.cost_dept=2 then /* R6 OUTSOURCING COST */   
                        s_r6outcost = s_r6outcost + (pl_rec.prod_num * pl_rec.prod_price) ;   
                     end if ;
                  elsif pl_rec.cost_dept in (5,6) then   /* NT */
                      s_ntrev= s_ntrev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=6 then /* NT MES COST */
                        s_ntmes = s_ntmes + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=5 then /* NT OUTSOURCING COST */   
                        s_ntoutcost = s_ntoutcost + (pl_rec.prod_num * pl_rec.prod_price) ;    
                     end if ;
                  elsif pl_rec.cost_dept in (8,9) then   /* NW */ 
                    s_nwrev= s_nwrev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=9 then /* NW MES COST */
                        s_nwmes = s_nwmes + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=8 then /* NW OUTSOURCING COST */   
                        s_nwoutcost = s_nwoutcost + (pl_rec.prod_num * pl_rec.prod_price) ;    
                     end if ;
                  else
                     if pl_rec.cost_dept !=12 then /* 沒有成本部門且 非駐點 (全加入 R6收入) */
                        s_r6rev= s_r6rev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     end if ;   
                  end if ;   
               elsif pl_rec.cost_type=4 or pl_rec.cost_type=9 or pl_rec.cost_type=12 then  /* 維護舊約,維護新約,保固維護 */
                  if pl_rec.cost_dept in (2,3) then  /* R6 */
                     m_r6rev= m_r6rev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=3 then /* R6 MES COST */
                        m_r6mescost = m_r6mescost + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=2 then /* R6 OUTSOURCING COST */   
                        m_r6outcost = m_r6outcost + (pl_rec.prod_num * pl_rec.prod_price) ;
                     end if ;
                  elsif pl_rec.cost_dept in (5,6) then   /* NT */
                     m_ntrev= m_ntrev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=6 then /* NT MES COST */
                        m_ntmescost = m_ntmescost + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=5 then /* NT OUTSOURCING COST */   
                        m_ntoutcost = m_ntoutcost + (pl_rec.prod_num * pl_rec.prod_price) ; 
                     end if ;
                  elsif pl_rec.cost_dept in (8,9) then   /* NW */ 
                     m_nwrev= m_nwrev + (pl_rec.prod_num * pl_rec.prod_revenue) ; 
                     if pl_rec.cost_dept=9 then /* NW MES COST */
                        m_nwmescost = m_nwmescost + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=8 then /* NW OUTSOURCING COST */   
                        m_nwoutcost = m_nwoutcost + (pl_rec.prod_num * pl_rec.prod_price) ;    
                     end if ;
                  elsif pl_rec.cost_dept in (10,11) then   /* SUPPORT */ 
                    /* m_suprev= m_suprev + (pl_rec.prod_num * pl_rec.prod_revenue) ; */
                     if pl_rec.cost_dept=11 then /* SUPPORT MES COST */
                        m_supmescost = m_supmescost + (pl_rec.prod_num * pl_rec.prod_price) ;
                     elsif pl_rec.cost_dept=10  then /* SUPPORT OUTSOURCING */   
                        m_supoutcost = m_supoutcost + (pl_rec.prod_num * pl_rec.prod_price) ;   
                     end if ; 
                     m_suprev = m_suprev + (m_supmescost + m_supoutcost) ;  /* 委外收入 = 委外零件成本 + 委外成本 */
                  else
                     if pl_rec.cost_dept != 12 then   /* 沒有成本部門且 非駐點 (全加入 R6收入)*/
                        m_r6rev= m_r6rev + (pl_rec.prod_num * pl_rec.prod_revenue) ;
                     end if ;   
                  end if ;   
               end if;
             end loop ;   
             close pl_cur ;
             if m_suprev > 0 then
                m_r6rev = m_r6rev - m_suprev ;
             end if ;
             if s_r6rev+s_ntrev+s_nwrev = 0 then
                 s_r6per = 0.00 ;
                 s_ntper = 0.00 ;
                 s_nwper = 0.00 ;
             else
                 s_r6per = round((s_r6rev::numeric/(s_r6rev+s_ntrev+s_nwrev)::numeric)*100,2) ;
                 s_ntper = round((s_ntrev::numeric/(s_r6rev+s_ntrev+s_nwrev)::numeric)*100,2) ;
                 s_nwper = round((s_nwrev::numeric/(s_r6rev+s_ntrev+s_nwrev)::numeric)*100,2) ;
             end if ;   
             if s_r6mes+s_ntmes+s_nwmes = 0 then
                 s_r6mesper = 0.00 ;
                 s_ntmesper = 0.00 ;
                 s_nwmesper = 0.00 ;
             else
                 s_r6mesper = round((s_r6mes::numeric/(s_r6mes+s_ntmes+s_nwmes)::numeric)*100,2) ;
                 s_ntmesper = round((s_ntmes::numeric/(s_r6mes+s_ntmes+s_nwmes)::numeric)*100,2) ;
                 s_nwmesper = round((s_nwmes::numeric/(s_r6mes+s_ntmes+s_nwmes)::numeric)*100,2) ;
             end if ;  
             if s_r6outcost+s_ntoutcost+s_nwoutcost= 0 then
                s_r6outper = 0.00 ;
                s_ntoutper = 0.00 ;
                s_nwoutper = 0.00 ;
             else
                s_r6outper = round((s_r6outcost::numeric/(s_r6outcost+s_ntoutcost+s_nwoutcost)::numeric)*100,2) ;
                s_ntoutper = round((s_ntoutcost::numeric/(s_r6outcost+s_ntoutcost+s_nwoutcost)::numeric)*100,2) ;
                s_nwoutper = round((s_nwoutcost::numeric/(s_r6outcost+s_ntoutcost+s_nwoutcost)::numeric)*100,2) ;
             end if ; 
             if m_r6rev+m_ntrev+m_nwrev+m_suprev = 0 then
                m_r6per = 0.00 ;
                m_ntper = 0.00 ;
                m_nwper = 0.00 ;
                m_supper = 0.00 ;
             else
                m_r6per = round((m_r6rev::numeric/(m_r6rev+m_ntrev+m_nwrev+m_suprev)::numeric)*100,2) ;
                m_ntper = round((m_ntrev::numeric/(m_r6rev+m_ntrev+m_nwrev+m_suprev)::numeric)*100,2) ;
                m_nwper = round((m_nwrev::numeric/(m_r6rev+m_ntrev+m_nwrev+m_suprev)::numeric)*100,2) ;
                m_supper = round((m_suprev::numeric/(m_r6rev+m_ntrev+m_nwrev+m_suprev)::numeric)*100,2) ;
             end if ;
             if m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost = 0 then
                m_r6mesper = 0.00 ;
                m_ntmesper = 0.00 ;
                m_nwmesper = 0.00 ;
                m_supmesper = 0.00 ;
             else
                m_r6mesper = round((m_r6mescost::numeric/(m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost)::numeric)*100,2) ;
                m_ntmesper = round((m_ntmescost::numeric/(m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost)::numeric)*100,2) ;
                m_nwmesper = round((m_nwmescost::numeric/(m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost)::numeric)*100,2) ;
                m_supmesper = round((m_supmescost::numeric/(m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost)::numeric)*100,2) ;
             end if ;
             if m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost = 0 then
                m_r6outper = 0.00 ;
                m_ntoutper = 0.00 ;
                m_nwoutper = 0.00 ;
                m_supoutper = 0.00 ;
             else
                m_r6outper = round((m_r6outcost::numeric/(m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost)::numeric)*100,2) ;
                m_ntoutper = round((m_ntoutcost::numeric/(m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost)::numeric)*100,2) ;
                m_nwoutper = round((m_nwoutcost::numeric/(m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost)::numeric)*100,2) ;
                m_supoutper = round((m_supoutcost::numeric/(m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost)::numeric)*100,2) ;
             end if ;
           
             if s_r6rev+s_ntrev+s_nwrev > 0 then
                select count(*) into ncount from neweb_setupcost_line where project_id=projid and name='1' ;
                if ncount = 0 then
                   insert into neweb_setupcost_line (project_id,name) values (projid,'1') ;
                   update neweb_setupcost_line set r6_revenue=s_r6rev,r6_percent=s_r6per,nt_revenue=s_ntrev,nt_percent=s_ntper,
                    networking_revenue=s_nwrev,networking_percent=s_nwper where project_id=projid and name='1' ; 
                end if ;         
             end if ; 
             if s_r6mes+s_ntmes+s_nwmes > 0 then
                 select count(*) into ncount from neweb_setupcost_line where project_id = projid and name='2' ;
                 if ncount = 0 then
                    insert into neweb_setupcost_line (project_id,name) values (projid,'2') ;
                 end if ; 
                 update neweb_setupcost_line set r6_revenue=s_r6mes,r6_percent=s_r6mesper,nt_revenue=s_ntmes,nt_percent=s_ntmesper,
                    networking_revenue=s_nwmes,networking_percent=s_nwmesper where project_id=projid and name='2' ;    
             end if ;
             if s_r6outcost+s_ntoutcost+s_nwoutcost > 0 then
                 /* 如果有 委外成本(手動) */
                 select count(*) into ncount1 from neweb_setupcost_line where project_id=projid and name='4' ;
                 select count(*) into ncount from neweb_setupcost_line where project_id=projid and name='3' ;
                 if ncount = 0 and ncount1 = 0 then
                    insert into neweb_setupcost_line (project_id,name) values (projid,'3') ;
                 end if ;
                 if ncount1 = 0 then
                    update neweb_setupcost_line set r6_revenue=s_r6outcost,r6_percent=s_r6outper,nt_revenue=s_ntoutcost,nt_percent=s_ntoutper,
                          networking_revenue=s_nwoutcost,networking_percent=s_nwoutper where project_id=projid and name='3' ; 
                 end if ;   
             end if ;
            if m_r6rev+m_ntrev+m_nwrev+m_suprev > 0 then
                 select count(*) into ncount from neweb_maincost_line where project_id=projid and name='1'  ;
                 if ncount = 0 then
                    insert into neweb_maincost_line (project_id,name) values (projid,'1') ;
                    update neweb_maincost_line set r6_revenue=m_r6rev,r6_percent=m_r6per,nt_revenue=m_ntrev,nt_percent=m_ntper,networking_revenue=m_nwrev,
                        networking_percent=m_nwper,support_revenue=m_suprev,support_percent=m_supper where project_id=projid and name='1' ; 
                    update neweb_maincost_line set subtot_revenue1= (m_r6rev+m_ntrev+m_nwrev+m_suprev) where project_id=projid and name='1' ;   
                 end if ;     
            end if ;    
            if m_r6mescost+m_ntmescost+m_nwmescost+m_supmescost > 0 then
                  select count(*) into ncount from neweb_maincost_line where project_id=projid and name='2' ;
                  if ncount = 0 then
                     insert into neweb_maincost_line (project_id,name) values (projid,'2') ;
                  end if ;   
                 update neweb_maincost_line set r6_revenue=m_r6mescost,r6_percent=m_r6mesper,nt_revenue=m_ntmescost,nt_percent=m_ntmesper,networking_revenue=m_nwmescost,
                        networking_percent=m_nwmesper,support_revenue=m_supmescost,support_percent=m_supmesper where project_id=projid and name='2' ;      
             end if ; 
             if m_r6outcost+m_ntoutcost+m_nwoutcost+m_supoutcost > 0 then
                 /* 如果有 委外成本(手動)  name='3'委外成本(自)  name='4'委外成本(手)  */
                 select count(*) into ncount1 from neweb_maincost_line where project_id=projid and name='4' ;
                 select count(*) into ncount from neweb_maincost_line where project_id=projid and name='3' ;
                 if ncount = 0 and ncount1 = 0 then
                    insert into neweb_maincost_line (project_id,name) values (projid,'3') ;
                 end if ;   
                 if ncount1 = 0 then
                    update neweb_maincost_line set r6_revenue=m_r6outcost,r6_percent=m_r6outper,nt_revenue=m_ntoutcost,nt_percent=m_ntoutper,networking_revenue=m_nwoutcost,
                           networking_percent=m_nwoutper,support_revenue=m_supoutcost,support_percent=m_supoutper where project_id=projid and name='3' ;   
                 end if ;          
                 if m_supoutcost > 0 then
                    select count(*) into ncount from neweb_maincost_line where project_id=projid and name='1'  ;
                     if ncount = 0 then
                        insert into neweb_maincost_line (project_id,name) values (projid,'1') ;   
                        update neweb_maincost_line set r6_revenue=(coalesce(r6_revenue,0) - m_supoutcost),support_revenue=m_supoutcost,support_percent=m_supoutper where project_id=projid and name='1' ; 
                     end if ;  
                 end if ;           
             end if ;       
    
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencostdeptper(projid int) cascade""")
        self._cr.execute("""create or replace function gencostdeptper(projid int) returns void as $BODY$
           DECLARE
              prev_cur refcursor ;
              prev_rec record ;
              s_r6per float = 0.00 ;
              m_r6per float = 0.00 ;
              s_ntper float = 0.00 ;
              m_ntper float = 0.00 ;
              s_nwper float = 0.00 ;
              m_nwper float = 0.00 ;
              m_supper float = 0.00 ;
              s_pmper float = 0.00 ;
              subtot float ;
              subtot1 float ;
           BEGIN
              open prev_cur for select * from neweb_setupcost_line where project_id=projid and name='1' ;
              loop
               fetch prev_cur into prev_rec ;
               exit when not found ;
               if (coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0)) > 0 then
                  s_r6per = round((coalesce(prev_rec.r6_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.pm_revenue,0))::numeric)*100,2) ;
                  s_ntper = round((coalesce(prev_rec.nt_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.pm_revenue,0))::numeric)*100,2) ;
                  s_nwper = round((coalesce(prev_rec.networking_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.pm_revenue,0))::numeric)*100,2) ;
                  s_pmper = round((coalesce(prev_rec.pm_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.pm_revenue,0))::numeric)*100,2) ;
               else
                  s_r6per = 0 ;
                  s_ntper = 0 ;
                  s_nwper = 0 ;
                  s_pmper = 0 ;
               end if ;   
               update neweb_setupcost_line set r6_percent=s_r6per,nt_percent=s_ntper,networking_percent=s_nwper,pm_percent=s_pmper where id = prev_rec.id;         
             end loop ;
             close prev_cur ; 
             open prev_cur for select * from neweb_maincost_line where project_id=projid and name='1' ;
             loop
               fetch prev_cur into prev_rec ;
               exit when not found ;
               if (coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0)) > 0 then
                  subtot1 = (coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.support_revenue,0)) ; 
                  subtot = (coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0)) ;
                  m_r6per = round((coalesce(prev_rec.r6_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0))::numeric)*100,2) ;
                  m_ntper = round((coalesce(prev_rec.nt_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0))::numeric)*100,2) ;
                  m_nwper = round((coalesce(prev_rec.networking_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0))::numeric)*100,2) ;
                  /* m_supper = round((coalesce(prev_rec.support_revenue,0)::numeric/(coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.support_revenue,0))::numeric)*100,2) ; */
               else
                  subtot1 = (coalesce(prev_rec.r6_revenue,0) + coalesce(prev_rec.nt_revenue,0) + coalesce(prev_rec.networking_revenue,0) + coalesce(prev_rec.support_revenue,0)) ; 
                  m_r6per = 0 ;
                  m_ntper = 0 ;
                  m_nwper = 0 ;
                  m_supper = 0 ;
               end if ;   

               update neweb_maincost_line set r6_percent=m_r6per,nt_percent=m_ntper,networking_percent=m_nwper where id = prev_rec.id;

             end loop ;
             close prev_cur ;              
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallmainrevenue() cascade""")
        self._cr.execute("""create or replace function genallmainrevenue() returns void as $BODY$
         DECLARE
           main_cur refcursor ;
           main_rec record ;
           subtot float ;
         BEGIN
           open main_cur for select * from neweb_maincost_line ;
           loop
             fetch main_cur into main_rec ;
             exit when not found ;
             subtot = (coalesce(main_rec.r6_revenue,0) + coalesce(main_rec.nt_revenue,0) + coalesce(main_rec.networking_revenue,0) + coalesce(main_rec.support_revenue,0)) ;
             update neweb_maincost_line set subtot_revenue1=coalesce(subtot,0),keytype='1' where id = main_rec.id ;
           end loop ;
           close main_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setprojstampduty() cascade""")
        self._cr.execute("""create or replace function setprojstampduty() returns void as $BODY$
           DECLARE

           BEGIN
              update neweb_project set stamp_duty_type='2',stamp_duty=floor(total_analysis_revenue * 0.001) ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getuseremp(userid int) cascade""")
        self._cr.execute("""create or replace function getuseremp(userid int) returns INT as $BODY$
           DECLARE
             myres int ;
             myresourceid int ;
           BEGIN
             select id into myresourceid from resource_resource where user_id=userid ;
             select id into myres from hr_employee where resource_id=myresourceid ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getsalepartner(empid int) cascade""")
        self._cr.execute("""create or replace function getsalepartner(empid int) returns setof INT as $BODY$
           DECLARE
             par_cur refcursor ;
             par_rec record ;
             iscompany Boolean ;
           BEGIN
             if empid = 0 then
                open par_cur for select * from hr_employee_res_partner_rel;
             else
                open par_cur for select * from hr_employee_res_partner_rel where hr_employee_id = empid ;
             end if ; 
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
               select is_company into iscompany from res_partner where id = par_rec.res_partner_id  ;
               if iscompany=True then
                  return next par_rec.res_partner_id ;
               end if ;   
             end loop ;
             close par_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpartnerlist(empid int) cascade""")
        self._cr.execute("""drop function if exists genallpartnerlist(empid int,exptype char) cascade""")
        self._cr.execute("""create or replace function genallpartnerlist(empid int,exptype char) returns void as $BODY$
           DECLARE
             par_cur refcursor ;
             par_rec record ;
             chi_cur refcursor ;
             chi_rec record ;
             mycusname varchar ;
             myvat varchar ;
             mytel varchar ;
             myaddress varchar ;
             mybirm varchar ;
             mybird varchar ;
             mybirthday varchar ;
             saleempid int ;
             sa_cur refcursor ;
             sa_rec record ;
             salesname varchar ;
             salename varchar ;
             resourceid int ;
             ncount int ;
             isactive Boolean ;
           BEGIN
             delete from neweb_partner_list ;
             if empid > 0 then
                if exptype='1' then
                   open par_cur for select * from res_partner where id in (select res_partner_id from hr_employee_res_partner_rel where hr_employee_id = empid) 
                        and is_company=true and customer_rank=1 ;
                elsif exptype='2' then
                   open par_cur for select * from res_partner where id in (select res_partner_id from hr_employee_res_partner_rel where hr_employee_id = empid) 
                        and is_company=true and supplier_rank=1 ;
                else
                   open par_cur for select * from res_partner where id in (select res_partner_id from hr_employee_res_partner_rel where hr_employee_id = empid) 
                        and is_company=true ;
                end if ;
             else
                if exptype='1' then
                   open par_cur for select * from res_partner where is_company=true and customer_rank=1 ;
                elsif exptype='2' then
                   open par_cur for select * from res_partner where is_company=true and supplier_rank=1 ;
                else
                   open par_cur for select * from res_partner where is_company=true ;
                end if ;
             end if ;   
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
               salesname = '' ;
               open sa_cur for select * from hr_employee_res_partner_rel where res_partner_id = par_rec.id ;
               loop
                 fetch sa_cur into sa_rec ;
                 exit when not found ;
                 select resource_id into resourceid from hr_employee where id = sa_rec.hr_employee_id ;
                 select count(*) into ncount from hr_employee where id = sa_rec.hr_employee_id ;
                 if ncount > 0 then
                     salename='' ;
                     select name into salename from resource_resource where id = resourceid and active=true ;
                     if salename is not null then
                         if salesname='' then
                            salesname = salename ;
                         else
                            salesname = concat(salesname,' ,',salename) ;
                         end if ;
                     end if ;    
                 end if ;    
               end loop ;
               close sa_cur ;
               open chi_cur for select * from res_partner where parent_id=par_rec.id ;
               loop
                  fetch chi_cur into chi_rec ;
                  exit when not found ;
                  select name into mybirm from neweb_partner_birthday_month where id = chi_rec.birthday_month ;
                  select name into mybird from neweb_partner_birthday_day where id = chi_rec.birthday_day ;
                  mybirthday = concat(coalesce(mybirm,' '),'/',coalesce(mybird,' ')) ;

                  insert into neweb_partner_list(cus_name,vat,tel,address,contact,contact_type,function,tel1,mobile,email,birthday,comment,sales) values
                    (par_rec.name,par_rec.vat,par_rec.phone,par_rec.street,chi_rec.name,chi_rec.contact_type,chi_rec.function,chi_rec.phone,chi_rec.mobile,
                    chi_rec.email,mybirthday,chi_rec.comment,coalesce(salesname,' ')) ;
               end loop ;
               close chi_cur ;
             end loop ;
             close par_cur ;
              delete from neweb_partner_export_wizard ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpartnerlist(wizid int) cascade""")
        self._cr.execute("""create or replace function genpartnerlist(wizid int) returns void as $BODY$
           DECLARE
             par_cur refcursor ;
             par_rec record ;
             chi_cur refcursor ;
             chi_rec record ;
             mycusname varchar ;
             myvat varchar ;
             mytel varchar ;
             myaddress varchar ;
             mybirm varchar ;
             mybird varchar ;
             mybirthday varchar ;
             mywizid int ;
             sa_cur refcursor ;
             sa_rec record ;
             salesname varchar ;
             salename varchar ;
             resourceid int ;
           BEGIN
             delete from neweb_partner_list ;
             select max(id) into mywizid from neweb_partner_export_wizard ;
             open par_cur for select * from res_partner where id in 
               (select partner_id from partner_export_wizard_rel where wizard_id = mywizid) ;
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
               open chi_cur for select * from res_partner where parent_id=par_rec.id ;
               loop
                  fetch chi_cur into chi_rec ;
                  exit when not found ;
                  salesname = '' ;
                   open sa_cur for select * from hr_employee_res_partner_rel where res_partner_id = par_rec.id ;
                   loop
                     fetch sa_cur into sa_rec ;
                     exit when not found ;
                     salename='' ;
                     select resource_id into resourceid from hr_employee where id = sa_rec.hr_employee_id ;
                     select name into salename from resource_resource where id = resourceid and active=true ;

                     if salename is not null then
                         if salesname='' then
                            salesname = salename ;
                         else
                            salesname = concat(salesname,' ,',salename) ;
                         end if ;
                     end if ;    
                   end loop ;
                   close sa_cur ;
                  select name into mybirm from neweb_partner_birthday_month where id = chi_rec.birthday_month ;
                  select name into mybird from neweb_partner_birthday_day where id = chi_rec.birthday_day ;
                  mybirthday = concat(coalesce(mybirm,' '),'/',coalesce(mybird,' ')) ;
                  insert into neweb_partner_list(cus_name,vat,tel,address,contact,contact_type,function,tel1,mobile,email,birthday,comment,sales) values
                    (par_rec.name,par_rec.vat,par_rec.phone,par_rec.street,chi_rec.name,chi_rec.contact_type,chi_rec.function,chi_rec.phone,chi_rec.mobile,
                    chi_rec.email,mybirthday,chi_rec.comment,coalesce(salesname,' ')) ;
               end loop ;
               close chi_cur ;
             end loop ;
             close par_cur ;
             delete from neweb_partner_export_wizard ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genassengperm(assid int) cascade""")
        self._cr.execute("""create or replace function genassengperm(assid int) returns void as $BODY$ 
           DECLARE
             ser_cur refcursor ;
             ser_rec record ;
             manempid int ;
             ncount int ;
           BEGIN
             delete from hr_employee_projengassign_rel where ass_id=assid ;
             open ser_cur for select * from neweb_ass_service_type_neweb_proj_eng_assign_rel where neweb_proj_eng_assign_id = assid ;
             loop
               fetch ser_cur into ser_rec ;
               exit when not found ;
               select service_manager into manempid from neweb_ass_service_type where id = ser_rec.neweb_ass_service_type_id ;
               if manempid is not null then
                 select count(*) into ncount from hr_employee_projengassign_rel where ass_id=assid and emp_id=manempid ;
                 if ncount = 0 then
                    insert into hr_employee_projengassign_rel(ass_id,emp_id) values (assid,manempid) ;
                 end if ;   
               end if ;
             end loop ;
             close ser_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runchangesale(empid int) cascade""")
        self._cr.execute("""create or replace function runchangesale(empid int) returns void as $BODY$
           DECLARE
             parentid int ;
             par_cur refcursor ;
             par_rec record ;
             ncount int ;
           BEGIN
             select parent_id into parentid from hr_employee where id = empid ;
             open par_cur for select * from hr_employee_res_partner_rel where hr_employee_id=empid ;
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
                select count(*) into ncount from hr_employee_res_partner_rel where res_partner_id=par_rec.res_partner_id and hr_employee_id = parentid ;
                if ncount = 0 then
                   insert into hr_employee_res_partner_rel(res_partner_id,hr_employee_id) values (par_rec.res_partner_id,parentid) ;
                end if ;
                delete from hr_employee_res_partner_rel where res_partner_id=par_rec.res_partner_id and hr_employee_id=par_rec.hr_employee_id ;
             end loop ;
             close par_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists rechecksetuprevenue(projid int) cascade""")
        self._cr.execute("""create or replace function rechecksetuprevenue(projid int) returns Boolean as $BODY$
           DECLARE
             ncount int ;
             ncount1 int ;
             myres Boolean ;
             mysetuprevenue float;
             myprojrevenue float ;
           BEGIN
             select count(*) into ncount from neweb_projanalysis where analysis_id = projid and analysis_costtype = 3 ;
             select count(*) into ncount1 from neweb_setupcost_line where project_id = projid and name='1' ;
             select sum(coalesce(analysis_revenue,0)) into myprojrevenue from neweb_projanalysis where analysis_id = projid and analysis_costtype=3 ;
             select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into mysetuprevenue
                 from neweb_setupcost_line where project_id=projid and name='1' ;
             if myprojrevenue = mysetuprevenue then
                myres = True ;
             else
                if ncount1 = 0 then
                   myres = True ;
                else   
                   myres = False ;
                end if ;   
             end if ;    
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        ### 建置成本歸戶與專案成本分析金額比對
        self._cr.execute("""drop function if exists checksetupcost(projid int) cascade""")
        self._cr.execute("""create or replace function checksetupcost(projid int) returns Boolean as $BODY$
           DECLARE
             myres Boolean ;
             mysetupcost float ;
             mymaincost float ;
             mysetupcost1 float ;
             mymaincost1 float ;
             ncount int ;
             ncount1 int ;
             ncount2 int ;
             projwritenum int ;
           BEGIN
             ncount = 0 ;
             ncount1 = 0 ;
             ncount2 = 0 ;
             mysetupcost = 0 ;
             mymaincost = 0 ;
             mysetupcost1 = 0 ;
             mymaincost1 = 0 ;
             select coalesce(proj_write_num,0) into projwritenum from neweb_project where id = projid ;
             select sum(coalesce(analysis_revenue,0)) into mysetupcost from neweb_projanalysis where analysis_id = projid 
                and analysis_costtype = 3 ;
             select sum(coalesce(analysis_revenue,0)) into mymaincost from neweb_projanalysis where analysis_id = projid 
                and (analysis_costtype = 4 or analysis_costtype = 9 or analysis_costtype = 12) ;   
             select count(*) into ncount from  neweb_projanalysis where analysis_id = projid ;  
             select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into mysetupcost1
                from neweb_setupcost_line where project_id = projid and name='1' ;
             select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(support_revenue,0)) into mymaincost1
                from neweb_maincost_line where project_id = projid and name='1' ;   
             select count(*) into ncount1 from neweb_setupcost_line where project_id = projid ;   
             select count(*) into ncount2 from neweb_maincost_line where project_id = projid ;
             if abs((coalesce(mysetupcost,0) + coalesce(mymaincost,0)) - (coalesce(mysetupcost1,0) + coalesce(mymaincost1,0))) <= 10 then
                myres = True ;
             else
                if  projwritenum <= 3 then
                   myres = True ;
                else
                   myres = False ;
                end if ;
             end if ;   
             update neweb_project set proj_write_num = coalesce(proj_write_num,0) + 1 where id = projid ;
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        ### 維護新舊約 成本歸戶與專案成本分析金額比對
        self._cr.execute("""drop function if exists checkmaincost(projid int) cascade""")
        self._cr.execute("""create or replace function checkmaincost(projid int) returns Boolean as $BODY$
           DECLARE
             myres Boolean ;
             mymaincost float ;
             mymaincost1 float ;
           BEGIN
             select sum(coalesce(analysis_revenue,0)) into mymaincost from neweb_projanalysis where analysis_id = projid 
                and analysis_costtype in (9,4) ;
             select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(support_revenue,0)) into mymaincost1
                from neweb_maincost_line where project_id = projid and name='1' ;
             if coalesce(mymaincost,0) = coalesce(mymaincost1,0) then
                myres = True ;
             else
                if mymaincost1 = 0 then
                   myres = True ;
                else
                   myres = False ;
                end if ;   
             end if ;   
             return myres ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getanalysistotrev(projid int) cascade""")
        self._cr.execute("""create or replace function getanalysistotrev(projid int) returns Float as $BODY$
         DECLARE
           mysetupcost float ;
           mymaincost float ;
           myres float ;
         BEGIN
             myres = 0 ;
             select sum(coalesce(analysis_revenue,0)) into mysetupcost from neweb_projanalysis where analysis_id = projid 
                and analysis_costtype = 3 ;
             select sum(coalesce(analysis_revenue,0)) into mymaincost from neweb_projanalysis where analysis_id = projid 
                and analysis_costtype in (9,4,12) ;  
             myres = coalesce(mysetupcost,0) + coalesce(mymaincost,0) ; 
             /* select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid ;*/
             return coalesce(myres,0) ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gettotdeptrev(projid int) cascade""")
        self._cr.execute("""create or replace function gettotdeptrev(projid int) returns Float as $BODY$
         DECLARE
           myres float ;
           myres1 float ;
           myres2 float ;
         BEGIN
            myres = 0 ;
            select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into myres1
                from neweb_setupcost_line where project_id = projid and name='1' ;
            select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(support_revenue,0)) into myres2
                from neweb_maincost_line where project_id = projid and name='1' ;  
            myres = coalesce(myres1,0) + coalesce(myres2,0) ;
            return coalesce(myres,0) ;        
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getsetupanalysisrev(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupanalysisrev(projid int) returns Float as $BODY$
          DECLARE
            myres float ;
          BEGIN
             select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid 
                and analysis_costtype = 3 ;   
             return coalesce(myres,0) ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getsetupcosdeptrev(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupcostdeptrev(projid int) returns Float as $BODY$
          DECLARE
            myres float ;
          BEGIN
             select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into myres
                from neweb_setupcost_line where project_id = projid and name='1' ;
             return coalesce(myres,0) ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmainanalysisrev(projid int) cascade""")
        self._cr.execute("""create or replace function getmainanalysisrev(projid int) returns Float as $BODY$
         DECLARE
           myres float ;
         BEGIN
            select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid 
               and analysis_costtype in (4,9,12) ;
            return coalesce(myres,0) ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmaincosdeptrev(projid int) cascade""")
        self._cr.execute("""create or replace function getmaincostdeptrev(projid int) returns Float as $BODY$
         DECLARE
           myres float ;
         BEGIN
            select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into myres
               from neweb_maincost_line where project_id = projid and name='1' ;
            return coalesce(myres,0) ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genstampduty(projid int) cascade""")
        self._cr.execute("""create or replace function genstampduty(projid int) returns void as $BODY$
         DECLARE
           ncount int ;
           stampduty int ;
           stampdutytype char ;
           tot_rev float ;
         BEGIN
           select stamp_duty,stamp_duty_type,total_analysis_revenue into stampduty,stampdutytype,tot_rev from neweb_project where id = projid ;
           if (stampduty is null or stampduty = 0 ) then
              if stampdutytype='1' then
                 stampduty = 12 ;
              elsif stampdutytype='2' then
                 stampduty = (tot_rev::numeric * 0.001)::INTEGER ; 
                 if stampduty > (tot_rev::numeric * 0.001) then
                    stampduty =stampduty - 1 ;
                 end if ;
              else
                 stampduty = 0 ;   
              end if ;
              update neweb_project set stamp_duty=stampduty where id = projid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists genallstampduty() cascade""")
        self._cr.execute("""create or replace function genallstampduty() returns void as $BODY$
         DECLARE
           proj_cur refcursor ;
           proj_rec record ;
           stampduty int ;
           stampdutytype char ;
           tot_rev float ;
           myres int ;
         BEGIN
           open proj_cur for select id,name,stamp_duty_type,stamp_duty,total_analysis_revenue from neweb_project where (stamp_duty is null 
                or stamp_duty = 0 ) ;
           loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              if proj_rec.stamp_duty_type='1' then
                 myres = 12 ;
              else
                 myres = (proj_rec.total_analysis_revenue::numeric * 0.001)::INTEGER ;
              end if ;
              update neweb_project set stamp_duty=myres where id = proj_rec.id ;
           end loop ;
           close proj_cur ;     
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genprojlineitem(projid int) cascade""")
        self._cr.execute("""create or replace function genprojlineitem(projid int) returns void as $BODY$
         DECLARE
           lineitem int ;
           sale_cur refcursor ;
           sale_rec record ;
         BEGIN
           lineitem = 1 ;
           open sale_cur for select id,line_item,saleitem_id from neweb_projsaleitem where saleitem_id=projid order by id ;
           loop
              fetch sale_cur into sale_rec ;
              exit when not found ;
              update neweb_projsaleitem set line_item=lineitem where id = sale_rec.id ;
              lineitem = lineitem + 1 ;
           end loop ;
           close sale_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallprojlineitem() cascade""")
        self._cr.execute("""create or replace function genallprojlineitem() returns void as $BODY$
         DECLARE
           proj_cur refcursor ;
           proj_rec record ;
         BEGIN
           open proj_cur for select id from neweb_project ;
           loop
             fetch proj_cur into proj_rec ;
             exit when not found ;
             execute genprojlineitem(proj_rec.id) ;
           end loop ;
           close proj_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensaleprojectno(projid int) cascade""")
        self._cr.execute("""create or replace function gensaleprojectno(projid int) returns void as $BODY$
         DECLARE
           nount int ;
           proj_cur refcursor ;
           proj_rec record ;
           saleno varchar ;
           saleid int ;
           projno int ;
         BEGIN
           if projid = 0 then
              open proj_cur for select * from neweb_project ;
              loop
                 fetch proj_cur into proj_rec ;
                 exit when not found ;
                 select coalesce(sale_no,' ') into saleno from neweb_project where id = proj_rec.id ;
                 select id into saleid from sale_order where name = saleno ;
                 if saleid is not null then
                    update sale_order set project_no=proj_rec.id where id = saleid ;
                 end if ;
              end loop ;
              close proj_cur ;
           else
              select coalesce(sale_no,' ') into saleno from neweb_project where id = projid ;
                 select id into saleid from sale_order where name = saleno ;
                 if saleid is not null then
                    update sale_order set project_no=projid where id = saleid ;
                 end if ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallmainlinerev() cascade""")
        self._cr.execute("""create or replace function genallmaintlinerev() returns void as $BODY$
         DECLARE
           main_cur refcursor ;
           main_rec record ;
           subtotrev float ;
         BEGIN
           open main_cur for select * from neweb_maincost_line where name='1' ;
           loop 
             fetch main_cur into main_rec ;
             exit when not found ;
             select sum(colesce(prod_num,0) * coalesce(prod_revenue,0)) into subtotrev from neweb_projsaleitem
                     where saleitem_id=main_rec.project_id and cost_type in (4,9,12) ;
             if subtotrev > 0 then
                update neweb_maincost_line set subtot_revenue1=subtotrev where id=main_rec.id ;
             end if ;  
           end loop ;
           close main_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gensalestockout(saleid int) cascade""")
        self._cr.execute("""create or replace function gensalestockout(saleid int) returns void as $BODY$
         DECLARE
           saleno varchar ;
           picking_cur refcursor ;
           picking_rec record ;
           tpoutloc int ; /* picking_type_id */
           locationlocid int ;
           locationdestlocid int ;
           pickingid int ;
         BEGIN
           select max(tp_outloc) into tpoutloc from neweb_company_stockloc ;
           select default_location_src_id,default_location_dest_id into locationlocid,locationdestlocid from stock_picking_type where id = tpoutloc ;
           select name into saleno from sale_order where id = saleid ;
           select id into pickingid from stock_picking where origin=saleno ;
           if pickingid is not null then
              update stock_picking set location_id=locationlocid,location_dest_id=locationdestlocid,picking_type_id=tpoutloc where id = pickingid ;
              update stock_move set location_id=locationlocid,location_dest_id=locationdestlocid where picking_id = pickingid ;
           end if ;  
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists sale_order_state_change on sale_order;""")

        # 計算傳回 neweb_projanalysis 建置收入
        self._cr.execute("""drop function if exists getsetupanalysistotrev(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupanalysistotrev(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
            myres = 0 ;
            select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid 
               and analysis_costtype = 3 ;
            return coalesce(myres,0) ;   
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 計算傳回 neweb_projanalysis 建置成本
        self._cr.execute("""drop function if exists getsetupanalysistotcost(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupanalysistotcost(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
            myres = 0 ;
            select sum(coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid 
               and analysis_costtype = 3 ;
            return coalesce(myres,0) ;   
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 計算傳回 neweb_projanalysis 維護收入
        self._cr.execute("""drop function if exists getmainanalysistotrev(projid int) cascade""")
        self._cr.execute("""create or replace function getmainanalysistotrev(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
            myres = 0 ;
            select sum(coalesce(analysis_revenue,0)) into myres from neweb_projanalysis where analysis_id = projid 
               and analysis_costtype in (4,9,12) ;
            return coalesce(myres,0) ;   
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 計算傳回 neweb_projanalysis 維護成本
        self._cr.execute("""drop function if exists getmainanalysistotcost(projid int) cascade""")
        self._cr.execute("""create or replace function getmainanalysistotcost(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
            myres = 0 ;
            select sum(coalesce(analysis_cost,0)) into myres from neweb_projanalysis where analysis_id = projid 
               and analysis_costtype in (4,9,12) ;
            return coalesce(myres,0) ;   
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 計算回傳建置成本歸戶 neweb_setupcost_line 收入金額並回傳
        self._cr.execute("""drop function if exists getsetupdeptrev(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupdeptrev(projid int) returns Float as $BODY$
         DECLARE
           myres float ;
         BEGIN
            myres = 0 ;
            select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(pm_revenue,0)) into myres
                from neweb_setupcost_line where project_id = projid and name='1' ;
            return coalesce(myres,0) ;        
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 計算回傳建置成本歸戶 neweb_setupcost_line 成本金額並回傳
        self._cr.execute("""drop function if exists getsetupdeptcost(projid int) cascade""")
        self._cr.execute("""create or replace function getsetupdeptcost(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
           myres = 0 ;
           select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)) into myres
               from neweb_setupcost_line where project_id = projid and name in ('2','3','4') ;
           return coalesce(myres,0) ;        
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 計算回傳維護成本歸戶 收入金額並回傳
        self._cr.execute("""drop function if exists getmaindeptrev(projid int) cascade""")
        self._cr.execute("""create or replace function getmaindeptrev(projid int) returns Float as $BODY$
         DECLARE
           myres float ;
         BEGIN
            myres = 0 ;
            select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(support_revenue,0)) into myres
                from neweb_maincost_line where project_id = projid and name='1' ;  
            return coalesce(myres,0) ;        
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 計算回傳維護成本歸戶 成本金額並回傳
        self._cr.execute("""drop function if exists getmaindeptcost(projid int) cascade""")
        self._cr.execute("""create or replace function getmaindeptcost(projid int) returns Float as $BODY$
        DECLARE
          myres float ;
        BEGIN
           myres = 0 ;
           select sum(coalesce(r6_revenue,0)+coalesce(nt_revenue,0)+coalesce(networking_revenue,0)+coalesce(support_revenue,0)) into myres
               from neweb_maincost_line where project_id = projid and name in ('2','3','4') ;  
           return coalesce(myres,0) ;        
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkprojstatus(projid int) cascade""")
        self._cr.execute("""create or replace function checkprojstatus(projid int) returns Boolean as $BODY$
         DECLARE
          myres Boolean ;
          ncount int ;
         BEGIN
           select count(*) into ncount from neweb_project where proj_write_num > 5 and proj_status != 'Balance' ;
           if ncount > 0 then
              myres = True ;
           else
              myres = False ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql; """)

        self._cr.execute("""drop function if exists clearcostline(projid int) cascade""")
        self._cr.execute("""create or replace function clearcostline(projid int) returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
         BEGIN
           select count(*) into ncount from neweb_setupcost_line where project_id=projid and name in ('3','4') ;
           if ncount = 2 then
              delete from neweb_setupcost_line where project_id=projid and name='3' ;
           end if ;
           select count(*) into ncount1 from neweb_maincost_line where project_id=projid and name in ('3','4') ;
           if ncount1 = 2 then
              delete from neweb_maincost_line where project_id=projid and name='3' ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists setempids(partnerid int) cascade""")
        self._cr.execute("""create or replace function setempids(partnerid int) returns void as $BODY$
         DECLARE
           emp_cur refcursor ;
           emp_rec record ;
           isactive Boolean ;
           userid int ;
           nitem int ;
         BEGIN
           update res_partner set salesp1=null,salesp2=null,salesp3=null,salesp4=null,salesp5=null where id = partnerid ;
           nitem=1 ;
           open emp_cur for select * from hr_employee_res_partner_rel where res_partner_id=partnerid ;
           loop
             fetch emp_cur into emp_rec ;
             exit when not found ;
             select user_id into userid from hr_employee where id=emp_rec.hr_employee_id and active=True ;
             if userid is not null then
                if nitem = 1 then
                   update res_partner set salesp1=userid where id = partnerid ;
                elsif nitem = 2 then
                   update res_partner set salesp2=userid where id = partnerid ;
                elsif nitem = 3 then
                   update res_partner set salesp3=userid where id = partnerid ;
                elsif nitem = 4 then
                   update res_partner set salesp4=userid where id = partnerid ;
                elsif nitem = 5 then
                   update res_partner set salesp5=userid where id = partnerid ;
                end if ; 
                nitem = nitem + 1 ;
             end if ;
           end loop ;
           close emp_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists allsetempids() cascade""")
        self._cr.execute("""create or replace function allsetempids() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
         BEGIN
           open par_cur for select id from res_partner where customer_rank > 0 and active=True ;
           loop
             fetch par_cur into par_rec ;
             exit when not found ;
             execute setempids(par_rec.id) ;
           end loop ;
           close par_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpartnerlist1() cascade""")
        self._cr.execute("""create or replace function genallpartnerlist1() returns void as $BODY$
           DECLARE
             par_cur refcursor ;
             par_rec record ;
             chi_cur refcursor ;
             chi_rec record ;
             mycusname varchar ;
             myvat varchar ;
             mytel varchar ;
             myaddress varchar ;
             mybirm varchar ;
             mybird varchar ;
             mybirthday varchar ;
             saleempid int ;
             resourceid int ;
             ncount int ;
             isactive Boolean ;
           BEGIN
            delete from neweb_partner_list ;
            open par_cur for select * from res_partner where is_company=true and supplier_rank=1 and active=True; 
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
               open chi_cur for select * from res_partner where parent_id=par_rec.id ;
               loop
                  fetch chi_cur into chi_rec ;
                  exit when not found ;
                   insert into neweb_partner_list(cus_name,vat,tel,address,contact,contact_type,function,tel1,mobile,email,comment,payment_days) values
                        (par_rec.name,par_rec.vat,coalesce(chi_rec.phone,par_rec.phone),coalesce(chi_rec.street,par_rec.street),chi_rec.name,chi_rec.contact_type,chi_rec.function,chi_rec.phone,chi_rec.mobile,
                        chi_rec.email,chi_rec.comment,coalesce(par_rec.payment_days,0)) ;
               end loop ;
               close chi_cur ;
             end loop ;
             close par_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallengownerman() cascade""")
        self._cr.execute("""create or replace function genallengownerman() returns void as $BODY$
         DECLARE
           emp_cur refcursor ;
           emp_rec record ;
           eng_cur refcursor ;
           eng_rec record ;
           nitem  int ;
           empid int ;
         BEGIN
            update neweb_proj_eng_assign set owner_man1=null,owner_man2=null,owner_man3=null,owner_man4=null,owner_man5=null,owner_man6=null;
            open eng_cur for select id from neweb_proj_eng_assign ;
            loop
               fetch eng_cur into eng_rec ;
               exit when not found ;
                nitem=1 ;
                open emp_cur for select * from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id=eng_rec.id ;
                loop
                  fetch emp_cur into emp_rec ;
                  exit when not found ;
                  select id into empid from hr_employee where user_id=emp_rec.res_users_id and active=True ;
                  if nitem = 1 then
                     update neweb_proj_eng_assign set owner_man1=empid where id = eng_rec.id;
                  elsif nitem = 2 then
                     update neweb_proj_eng_assign set owner_man2=empid where id = eng_rec.id ;
                  elsif nitem = 3 then
                     update neweb_proj_eng_assign set owner_man3=empid where id = eng_rec.id ;
                  elsif nitem = 4 then
                     update neweb_proj_eng_assign set owner_man4=empid where id = eng_rec.id ;
                  elsif nitem = 5 then
                     update neweb_proj_eng_assign set owner_man5=empid where id = eng_rec.id ;
                  elsif nitem = 6 then
                     update neweb_proj_eng_assign set owner_man6=empid where id = eng_rec.id ;
                  end if ;
                  nitem = nitem + 1 ;
                end loop ;
                close emp_cur ;
            end loop ;
            close eng_cur ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists recheckvat() cascade""")
        self._cr.execute("""create or replace function recheckvat() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
           myres Boolean ;
         BEGIN
           open par_cur for select * from res_partner where is_company=True and length(trim(vat)) > 8 ;
           loop
             fetch par_cur into par_rec ;
             exit when not found ;
             select par_rec.vat ~ '^[0-9\.]+$' into myres ;
             if myres=True then
                update res_partner set vat=substring(trim(par_rec.vat),1,8) where id=par_rec.id ;
             end if ;
           end loop ;
           close par_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpartnerlist() cascade""")
        self._cr.execute("""create or replace function genallpartnerlist() returns void as $BODY$
           DECLARE
             par_cur refcursor ;
             par_rec record ;
             chi_cur refcursor ;
             chi_rec record ;
             mycusname varchar ;
             myvat varchar ;
             mytel varchar ;
             myaddress varchar ;
             mybirm varchar ;
             mybird varchar ;
             mybirthday varchar ;
             mywizid int ;
             sa_cur refcursor ;
             sa_rec record ;
             salesname varchar ;
             salename varchar ;
             resourceid int ;
           BEGIN
             delete from neweb_partner_list ;
             /* select max(id) into mywizid from neweb_partner_export_wizard ; 
             open par_cur for select * from res_partner where id in 
               (select partner_id from partner_export_wizard_rel where wizard_id = mywizid) ; */
             open par_cur for select * from res_partner where customer_rank > 0 and is_company=True ;  
             loop
               fetch par_cur into par_rec ;
               exit when not found ;
               open chi_cur for select * from res_partner where parent_id=par_rec.id ;
               loop
                  fetch chi_cur into chi_rec ;
                  exit when not found ;
                  salesname = '' ;
                   open sa_cur for select * from hr_employee_res_partner_rel where res_partner_id = par_rec.id ;
                   loop
                     fetch sa_cur into sa_rec ;
                     exit when not found ;
                     salename='' ;
                     select resource_id into resourceid from hr_employee where id = sa_rec.hr_employee_id ;
                     select name into salename from resource_resource where id = resourceid and active=true ;

                     if salename is not null then
                         if salesname='' then
                            salesname = salename ;
                         else
                            salesname = concat(salesname,' ,',salename) ;
                         end if ;
                     end if ;    
                   end loop ;
                   close sa_cur ;
                  select name into mybirm from neweb_partner_birthday_month where id = chi_rec.birthday_month ;
                  select name into mybird from neweb_partner_birthday_day where id = chi_rec.birthday_day ;
                  mybirthday = concat(coalesce(mybirm,' '),'/',coalesce(mybird,' ')) ;
                  insert into neweb_partner_list(cus_name,vat,tel,address,contact,contact_type,function,tel1,mobile,email,birthday,comment,sales) values
                    (par_rec.name,par_rec.vat,par_rec.phone,par_rec.street,chi_rec.name,chi_rec.contact_type,chi_rec.function,chi_rec.phone,chi_rec.mobile,
                    chi_rec.email,mybirthday,chi_rec.comment,coalesce(salesname,' ')) ;
               end loop ;
               close chi_cur ;
             end loop ;
             close par_cur ;
             delete from neweb_partner_export_wizard ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gennewopenaccday1() cascade""")
        self._cr.execute("""create or replace function gennewopenaccday1() returns void as $BODY$
         DECLARE
           s_cur refcursor ;
           s_rec record ;
           p_cur refcursor ;
           p_rec record ;
           openaccid int ;
         BEGIN
           open p_cur for select id,open_account_day,payment_days from res_partner ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             if p_rec.payment_days >= 0 and p_rec.payment_days < 30 then
                update res_partner set open_account_day1=2 where id = p_rec.id ;
             elsif p_rec.payment_days >= 30 and p_rec.payment_days < 45 then
                update res_partner set open_account_day1=3 where id = p_rec.id ;
             elsif p_rec.payment_days >= 45 and p_rec.payment_days < 60 then
                update res_partner set open_account_day1=4 where id = p_rec.id ;
             elsif p_rec.payment_days >= 60 and p_rec.payment_days < 90 then
                update res_partner set open_account_day1=5 where id = p_rec.id ;
             elsif p_rec.payment_days >= 90 and p_rec.payment_days < 120 then
                update res_partner set open_account_day1=6 where id = p_rec.id ;
             elsif p_rec.payment_days >= 120 and p_rec.payment_days < 150 then
                update res_partner set open_account_day1=7 where id = p_rec.id ; 
             elsif p_rec.payment_days >= 150 and p_rec.payment_days <= 180 then
                update res_partner set open_account_day1=8 where id = p_rec.id ;       
             else
                update res_partner set open_account_day1=9 where id = p_rec.id ;
             end if ;
           end loop ;
           close p_cur ;
           open s_cur for select id,open_account_day,partner_id from sale_order ;
           loop
             fetch s_cur into s_rec ;
             exit when not found ;
             select open_account_day1 into openaccid from res_partner where id = s_rec.partner_id ;
             if openaccid is not null then
                update sale_order set open_account_day1=openaccid where id = s_rec.id ;
             end if ;
             if s_rec.open_account_day='1' then
                update sale_order set open_account_day2=3 where id = s_rec.id ;
             elsif s_rec.open_account_day='2' then
                update sale_order set open_account_day2=4 where id = s_rec.id ;
             elsif s_rec.open_account_day='3' then
                update sale_order set open_account_day2=5 where id = s_rec.id ;
             elsif s_rec.open_account_day='4' then
                update sale_order set open_account_day2=6 where id = s_rec.id ;
             elsif s_rec.open_account_day='5' then
                update sale_order set open_account_day2=7 where id = s_rec.id ;
             else
                update sale_order set open_account_day2=9 where id = s_rec.id ;
             end if ;
           end loop ;
           close s_cur ;
           open p_cur for select id,open_account_day,cus_name from neweb_project ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select open_account_day1 into openaccid from res_partner where id = p_rec.cus_name ;
             if openaccid is not null then
                update neweb_project set open_account_day1=openaccid where id = p_rec.id ;
             end if ;
             if p_rec.open_account_day='1' then
                update neweb_project set open_account_day2=3 where id = p_rec.id ;
             elsif p_rec.open_account_day='2' then
                update neweb_project set open_account_day2=4 where id = p_rec.id ;
             elsif p_rec.open_account_day='3' then
                update neweb_project set open_account_day2=5 where id = p_rec.id ;
             elsif p_rec.open_account_day='4' then
                update neweb_project set open_account_day2=6 where id = p_rec.id ;
             elsif p_rec.open_account_day='5' then
                update neweb_project set open_account_day2=7 where id = p_rec.id ;
             else
                update neweb_project set open_account_day2=9 where id = p_rec.id ;
             end if ;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")












