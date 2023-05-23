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