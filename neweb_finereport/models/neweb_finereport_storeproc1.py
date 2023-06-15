# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api,tools
from odoo.exceptions import UserError

class newebfinereport1(models.Model):
    _name = "neweb_finereport.storeproc1"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getpuryear(purid int) cascade""")
        self._cr.execute("""create or replace function getpuryear(purid int) returns varchar as $$
        declare
          myyear varchar;
          purdate date ;
        begin
          select date_approve into purdate from purchase_order where id = purid;
          select date_part('year',purdate)::TEXT into myyear;
          return myyear ;
        end; $$ language plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'neweb_supplier_brand_view')
        self._cr.execute("""create or replace view neweb_supplier_brand_view as (
        select (select getpuryear(A.id)) as puryear,A.partner_id,B.name as partnername,(coalesce(C.pitem_num::numeric,0) * coalesce(C.pitem_price::numeric,0)) as pprice,
        D.prod_brand,E.name as brandname from purchase_order A 
        left join res_partner B on A.partner_id = B.id 
        left join neweb_pitem_list C on A.id = C.pitem_id 
        left join neweb_projsaleitem D on C.pitem_origin_id = D.id
        left join neweb_prodbrand E on D.prod_brand = E.id 
        where A.state in ('purchase','done') and D.prod_brand is not null 
        order by A.partner_id,D.prod_brand)""")

        self._cr.execute("""drop function if exists getsaleitemyear(sitemid int) cascade""")
        self._cr.execute("""create or replace function getsaleitemyear(sitemid int) returns varchar as $$
        declare
          myres varchar ;
        begin
            select date_part('year',create_date)::TEXT into myres from neweb_projsaleitem where id = sitemid ;
            if myres is null then
               myres = ' ' ;
            end if ;   
            return myres ;
        end ; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getsitemprofitrate(sitemid int) cascade""")
        self._cr.execute("""create or replace function getsitemprofitrate(sitemid int) returns float as $$
        declare
            prodnum int ;
            myrprice float ;
            mycprice float ;
            myprofit float ;
            myrate float ;
        begin
            select coalesce(prod_num,0),(coalesce(prod_num,0) * coalesce(prod_revenue,0)),(coalesce(prod_num,0) * coalesce(prod_price,0)) into prodnum,myrprice,mycprice from neweb_projsaleitem where id = sitemid ;
            myprofit = myrprice - mycprice ;
            if myrprice > 0  then
                myrate = round((myprofit::numeric / myrprice::numeric),2) ;
            else
                myrate = 0 ;
            end if ;
            return myrate ;
        end ; $$ language plpgsql;""")

        self._cr.execute("""drop function if exists getsaleitemdept(sitemid int) cascade""")
        self._cr.execute("""create or replace function getsaleitemdept(sitemid int) returns INT as $$
        declare
          projid int ;
          saleid int ;
          deptid int ;
        begin
          select saleitem_id into projid from neweb_projsaleitem where id = sitemid ;
          select proj_sale into saleid from neweb_project where id = projid ;
          select department_id into deptid from hr_employee where id = saleid ;
          return deptid ;
        end ; $$ language plpgsql;""")

        tools.drop_view_if_exists(self._cr, 'neweb_prodset_analysis_view')
        self._cr.execute("""create or replace view neweb_prodset_analysis_view as (
        select (select getsaleitemyear(A.id)) as sitemyear,A.prod_set,B.name as setname,A.prod_num,A.prod_revenue,A.prod_price,
        (A.prod_num::numeric * A.prod_revenue::numeric) as rprice,
        (A.prod_num::numeric * A.prod_price::numeric) as cprice,
        (A.prod_num::numeric * (A.prod_revenue::numeric - A.prod_price::numeric)) as profit,
        (select getsitemprofitrate(A.id)) as profitrate,(select getsaleitemdept(A.id)) as saledept
        from neweb_projsaleitem A left join neweb_prodset B on A.prod_set = B.id
        where A.prod_set is not null and A.prod_num > 0 and A.prod_revenue > 0 order by A.prod_set)""")

        tools.drop_view_if_exists(self._cr, 'neweb_prodset_modeltype_view')
        self._cr.execute("""create or replace view neweb_prodset_modeltypeview as (
        select (select getsaleitemyear(A.id)) as sitemyear,A.prod_set,B.name as setname,A.prod_num,A.prod_price,
        (A.prod_num::numeric * A.prod_price::numeric) as cprice,D.name as salename,C.proj_sale,A.prod_brand,F.name as brandname,
        A.prod_modeltype,A.prod_desc,C.name as projname,E.name as partnername,(select getsaleitemdept(A.id)) as saledept
        from neweb_projsaleitem A left join neweb_prodset B on A.prod_set = B.id
        left join neweb_project C on A.saleitem_id = C.id
        left join res_partner E on C.cus_name = E.id
        left join hr_employee D on C.proj_sale = D.id
        left join neweb_prodbrand F on A.prod_brand = F.id
        where A.prod_set is not null   order by A.prod_set)""")




