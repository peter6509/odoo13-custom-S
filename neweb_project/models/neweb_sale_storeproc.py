# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebsalestoreproc(models.Model):
    _name = "neweb.salestoreproc"

    # 銷售訂單非列管料號產生一筆(原生列管料號)總金額相同,銷單明細皆為雜項沒有料號,整張銷單加總金額產生一筆 銷售商品(非可庫存料號),讓銷單正常流程走下去
    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS gensaleline(ownerid int,saleid int,prodid int,taxesid int) cascade;""")
        self._cr.execute("""create or replace function gensaleline(ownerid int,saleid int,prodid int,taxesid int) returns void as $BODY$
          declare
            mycreatedate sale_order.create_date%type;
            myprodname product_template.name%type;
            mycount integer;
            mycompanyid integer;
            mypartnerid integer;
            myproduom integer;
            mypriceunit float;
            mytaxesid integer;
            mypricesubtot float;
            mypricetotal  float;
            mypricetax  float;
            mycurrencyid integer;
            myname product_template.name%type;
            mytaxrate account_tax.amount%type;
            mylineid integer;
            mysaleno sale_order.name%type;
          begin
            select company_id into mycompanyid from res_users where id=ownerid;
            select partner_id,create_date into mypartnerid,mycreatedate from sale_order where id=saleid;
            select name,uom_id into myname,myproduom from product_template where id=prodid ;
            select amount into mytaxrate from account_tax where id=taxesid ;
            select count(*) into mycount from sale_order_line where order_id=saleid ;
            select sum(round(sitem_num::numeric * sitem_price::numeric)) into mypricesubtot from neweb_sitem_list where sitem_id=saleid ;
            mypricetax := round((mypricesubtot::numeric * mytaxrate::numeric / 100::numeric)) ;
            mypricetotal := mypricesubtot::numeric + mypricetax::numeric ;
            select currency_id into mycurrencyid from res_company where id=mycompanyid ;
            select id into mylineid from sale_order_line where order_id=saleid ;
            if mycount = 0 then
               insert into sale_order_line (create_uid,write_uid,create_date,write_date,product_uom,product_uom_qty,product_id,name,
                price_unit,price_subtotal,price_total,price_tax,order_id,company_id,currency_id,customer_lead) values (ownerid,ownerid,
                mycreatedate,mycreatedate,myproduom,1,prodid,myname,mypricesubtot,mypricesubtot,mypricetotal,
                mypricetax,saleid,mycompanyid,mycurrencyid,7);

            else
              update sale_order_line set product_uom=myproduom,product_uom_qty=1,product_id=prodid,name=myname,
                 price_unit=mypricesubtot,price_subtotal=mypricesubtot,price_total=mypricetotal,
                 price_tax=mypricetax,currency_id=mycurrencyid,customer_lead=7 where order_id=saleid ;
            end if ;
            update sale_order set amount_untaxed=mypricesubtot,amount_tax=mypricetax,amount_total=mypricetotal where id=saleid;
            delete from neweb_sitem_list where sitem_num=0 and sitem_id=saleid;
          end;
          $BODY$
          LANGUAGE plpgsql ;
          """)


        # 訂單編號格式設定,
        # mysequence = self.env['ir.sequence'].search([('code', '=', 'sale.order')])
        # if mysequence:
        #     mysequence.write({'prefix': 'N%(year)s%(month)s%(day)s',
        #                       'padding': 2,
        #                       # 'auto_reset': True,
        #                       'reset_period': 'day',
        #                       'reset_init_number': 1})

        # 原生訂單(列管料號) 產生 taxes_id many2many store procedure
        self._cr.execute(
            """DROP FUNCTION IF EXISTS gensaletaxesid(saleorderid int) cascade;""")
        self._cr.execute("""create or replace function gensaletaxesid(saleorderid int) returns void as $BODY$
            declare
              mytaxesid account_tax.id%type;
              mysaleorderlineid sale_order.id%type;
              ncount integer;
            begin
              select id into mysaleorderlineid from sale_order_line where order_id=saleorderid ;
              select taxes_id into mytaxesid from sale_order where id=saleorderid ;
              select count(*) into ncount from account_tax_sale_order_line_rel where sale_order_line_id = mysaleorderlineid and account_tax_id=mytaxesid ;
              if ncount = 0 then
                insert into account_tax_sale_order_line_rel (sale_order_line_id,account_tax_id) values (mysaleorderlineid,mytaxesid) ;
              end if ;
            end;$BODY$
            LANGUAGE plpgsql ;
            """)


        #  getownpartner => 業務員選擇客戶時有domain 限制,因使用 odoo python domain 不容易達成,用 pg store proc 較為簡單,效能較佳


        self._cr.execute("""drop function if exists getownpartner(empid int) cascade;""")
        self._cr.execute("""create or replace function getownpartner(empid int) returns setof INT as $BODY$
            DECLARE 
               myownpar_cur cursor is select res_partner_id from hr_employee_res_partner_rel where hr_employee_id=empid;
               myownpar_rec record;
               noownpar_cur cursor is select id from res_partner where id not in (select distinct res_partner_id from hr_employee_res_partner_rel);
               noownpar_rec record;
               iscustomer int;
               iscompany int ;
            BEGIN 
               open myownpar_cur ;
               loop
                 fetch myownpar_cur into myownpar_rec ;
                 exit when not found ;
                 select customer_rank,is_company into iscustomer,iscompany from res_partner where id=myownpar_rec.res_partner_id ;
                 if iscustomer=1 and iscompany=TRUE THEN 
                    return next myownpar_rec.res_partner_id ;
                 end if ;
               end loop ;
               close myownpar_cur ;
               
               open noownpar_cur ;
               loop
                 fetch noownpar_cur into noownpar_rec ;
                 exit when not found ;
                 select customer_rank,is_company into iscustomer,iscompany from res_partner where id=noownpar_rec.id ;
                 if iscustomer=1 and iscompany=TRUE THEN 
                    return next noownpar_rec.id ;
                 end if ;
               end loop ;
               close noownpar_cur ;
               return next 0 ;
            END ; $BODY$
            LANGUAGE plpgsql ; 
                  """)


        self._cr.execute("drop function if exists getmaincase(projid int) cascade")
        self._cr.execute("""create or replace function getmaincase(projid int) returns void as $BODY$
          DECLARE 
             ncount int;
             myprojmaincase CHAR;
          BEGIN 
             select count(*) into ncount from neweb_project_neweb_transationtype_rel where neweb_project_id=projid and 
                   (neweb_transationtype_id=6 or neweb_transationtype_id=7 or neweb_transationtype_id=8) ;
             if ncount > 0 THEN 
                update neweb_project set proj_main_case='Y' where id=projid ;
                myprojmaincase := 'Y' ;
             ELSE 
                update neweb_project set proj_main_case='N' where id=projid ;
                myprojmaincase := 'N' ;
             end if;
             select count(*) into ncount from neweb_project where total_analysis_revenue <= 300000 and total_analysis_profitrate > 8 and id=projid ;
             if ncount > 0 THEN 
                if myprojmaincase = 'N' then
                   update neweb_project set proj_cost_case='1' where id=projid ;
                ELSE 
                   update neweb_project set proj_cost_case='5' where id=projid ;
                end if ;  
                return ;
             end if ;
             select count(*) into ncount from neweb_project where (total_analysis_revenue <= 300000 and total_analysis_profitrate < 8) or 
                   (total_analysis_revenue > 300000 and total_analysis_revenue <= 1200000) and id=projid ;
             if ncount > 0 THEN
                if myprojmaincase = 'N' THEN 
                   update neweb_project set proj_cost_case='2' where id=projid ;
                ELSE 
                   update neweb_project set proj_cost_case='6' where id=projid ;
                end if;
                return ;
             end if ;     
             select count(*) into ncount from neweb_project where (total_analysis_revenue > 300000 and total_analysis_revenue <= 1200000 and total_analysis_profitrate < 8) OR 
                 (total_analysis_revenue > 1200000 and total_analysis_revenue <=15000000) and id=projid ;
             if ncount > 0 THEN 
                if myprojmaincase = 'N' THEN 
                   update neweb_project set proj_cost_case='3' where id=projid ;
                ELSE 
                   update neweb_project set proj_cost_case='7' where id=projid ;
                end if;
                 
                return ;
             end if ;   
             select count(*) into ncount from neweb_project where total_analysis_revenue > 15000000 and id=projid ;
             if ncount > 0 THEN 
                if myprojmaincasef = 'N' THEN 
                   update neweb_project set proj_cost_case='4' where id=projid ;
                ELSE 
                   update neweb_project set proj_cost_case='8' where id=projid ;
                end if;
                
                return ;
             end if ;
           
          END; $BODY$
          LANGUAGE plpgsql ;   
          """)

        self._cr.execute("drop function if exists getmobilephone(userid int) cascade")
        self._cr.execute("""create or replace function getmobilephone(userid int) returns VARCHAR as $BODY$
            DECLARE 
               ncount int;
               mymobilephone VARCHAR ;
               myresourceid INTEGER ;
            BEGIN 
               select id into myresourceid from resource_resource where user_id=userid ;
               select mobile_phone into mymobilephone from hr_employee where resource_id=myresourceid;
               return mymobilephone ;
            END ;$BODY$
            LANGUAGE plpgsql; 
            """)

        self._cr.execute("drop function if exists getworkphone(userid int) cascade")
        self._cr.execute("""create or replace function getworkphone(userid int) returns VARCHAR as $BODY$
            DECLARE 
               ncount int;
               myworkphone VARCHAR ;
               myresourceid INTEGER ;
            BEGIN 
               select id into myresourceid from resource_resource where user_id=userid ;
               select work_phone into myworkphone from hr_employee where resource_id=myresourceid;
               return myworkphone ;
            END ;$BODY$
            LANGUAGE plpgsql; 
            """)

        self._cr.execute("""drop function if exists gensaletoprojdata(saleid int,projid int) cascade""")
        self._cr.execute("""create or replace function gensaletoprojdata(saleid int,projid int) returns void as $BODY$
          DECLARE
            s_cur refcursor ;
            s_rec record ;
            mynowdate date ;
            mysitemid int ;
          BEGIN
            select current_timestamp::DATE into mynowdate ;
            open s_cur for select * from neweb_sitem_list where sitem_id = saleid order by id ;
            loop
              fetch s_cur into s_rec ;
              exit when not found ;
              insert into neweb_projsaleitem(saleitem_id,saleitem_item,prod_modeltype,prod_modeltype1,prod_serial,prod_desc,prod_num,prod_price,prod_revenue,prod_brand,neweb_start_date,neweb_end_date,cost_dept,cost_type,prod_purnum,prod_set,create_date,not_chiout,supplier) values
               (projid,s_rec.sitem_item,s_rec.sitem_modeltype,s_rec.sitem_modeltype1,s_rec.sitem_serial,s_rec.sitem_desc,s_rec.sitem_num,s_rec.sitem_cost,s_rec.sitem_price,s_rec.sitem_brand,s_rec.maintenance_start,s_rec.maintenance_end,s_rec.cost_dept,s_rec.cost_type,0,s_rec.prod_set,mynowdate,FALSE,s_rec.supplier) ;
            end loop ;
            close s_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chksalenotoproj(saleno varchar) cascade""")
        self._cr.execute("""create or replace function chksalenotoproj(saleno varchar) returns Boolean as $BODY$
          DECLARE
            ncount int ;
            myres Boolean ;
          BEGIN
            select count(*) into ncount from neweb_project where sale_no=saleno ;
            if ncount > 0 then
               myres = TRUE ;
               update neweb_salenocheck set trans_proj=TRUE where sale_no=saleno ;
            else
               myres = FALSE ;
               update neweb_salenocheck set trans_proj=FALSE where sale_no=saleno ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getmodeltype1(mt1 varchar) cascade""")
        self._cr.execute("""create or replace function getmodeltype1(mt1 varchar) returns INT as $BODY$
          DECLARE
            myres int ;
            ncount int ;
          BEGIN
            select count(*) into ncount from neweb_sitem_modeltype1 where name ilike '%%'|| mt1 ||'%%' and active=TRUE ;
            if ncount > 0 then
               select min(id) into myres from neweb_sitem_modeltype1 where name ilike '%%'|| mt1 ||'%%' and active=TRUE ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql""")

        self._cr.execute("""drop function if exists gen_sitem() cascade""")
        self._cr.execute("""create or replace function gen_sitem() returns void as $BODY$
          DECLARE
            s_cur refcursor ;
            s_rec record ;
            nitem float ;
          BEGIN
            open s_cur for select id,sitem_item from neweb_sitem_list ;
            loop
              fetch s_cur into s_rec;
              exit when not found ;
              if s_rec.sitem_item is not null then
                   if s_rec.sitem_item  ~  '^[0-9\.]+$' then
                      nitem = s_rec.sitem_item::numeric ;  
                   else
                      nitem = null ;
                   end if ;     
              else   
                 nitem = null ;
              end if ;
              update neweb_sitem_list set sitem_item1=nitem where id = s_rec.id ;
            end loop ;
            close s_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")