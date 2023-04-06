# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class shippingkpiPivotReport(models.Model):
    _name = 'alldo_acme_iot.shipping_kpi'
    _description = "Shipping KPI Statistics"
    _auto = False


class ShippingKPIPivotanalysisreport(shippingkpiPivotReport):
    _name = 'alldo_acme_iot.shipping_kpi_report'

    @api.depends('dif_value','holiday_num')
    def _get_kpi(self):
        myday = 0
        for rec in self:
            if rec.dif_value and rec.holiday_num:
               myday = rec.dif_value - rec.holiday_num
            else:
               myday = 0
            rec.shipping_kpi = 100 - (0.5 * myday)


    so_no = fields.Char(string="銷售單號")
    so_pi = fields.Char(string="客戶PI")
    product_no = fields.Many2one('product.product', string="產品")
    commitment_date = fields.Date(string="應交日期")
    shipping_date = fields.Date(string="實際交期")
    partner_id = fields.Many2one('res.partner',string="客戶")
    dif_value = fields.Integer(string="差異天數")
    holiday_num = fields.Integer(string="假日數")
    shipping_kpi = fields.Float(digits=(6,2),string="KPI",group_operator="avg")


    @api.model
    def init(self):
        # 傳回最後的出貨日期
        self.env.cr.execute("""drop function if exists getmaxstmdate(slid int) cascade""")
        self.env.cr.execute("""create or replace function getmaxstmdate(slid int) returns DATE as $BODY$
         DECLARE 
            myres date ;
         BEGIN
            select max(date) into myres from stock_move where sale_line_id=slid ;
            return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 傳回 (實際貨日 - 應交貨日)= 延遲交貨日數
        self._cr.execute("""drop function if exists getdifdatenum(slid int) cascade""")
        self._cr.execute("""create or replace function getdifdatenum(slid int) returns INT as $BODY$
         DECLARE
           myres int ;
           comdate date ;
           shipdate date ;
           orderid int ;
         BEGIN
           select order_id into orderid from sale_order_line where id = slid ;
           select commitment_date into comdate from sale_order where id = orderid ;
           select getmaxstmdate(slid) into shipdate ;
           if comdate is not null and shipdate is not null then
              select (shipdate::DATE - comdate::DATE) into myres ;
           else
              myres = 0 ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 傳回 遲交期間有幾天假日
        self._cr.execute("""drop function if exists getholidaynum(slid int) cascade""")
        self._cr.execute("""create or replace function getholidaynum(slid int) returns INT as $BODY$
         DECLARE
           myres int ;
           comdate date ;
           shipdate date ;
           maxdate date ;
           mindate date ;
           orderid int ;
           ndow int ;
           nnum int ;
         BEGIN
           select order_id into orderid from sale_order_line where id = slid ;
           select commitment_date::DATE into comdate from sale_order where id = orderid ;
           select getmaxstmdate(slid) into shipdate ;
           if shipdate is not null and comdate is not null then
              if shipdate > comdate then  /* 出貨日超過交貨期  */
                  mindate = comdate ;
                  maxdate = shipdate ;
                  nnum = 0 ;
                  loop
                     exit when mindate > maxdate or nnum > 100 ;
                     select EXTRACT(isodow from mindate) into ndow ;
                     if ndow in (6,7) then
                        nnum = nnum + 1 ;
                     end if ;
                     select mindate + interval '1 day' into mindate ;
                  end loop ;
                  myres = nnum ;
              else
                  myres = 0 ;     
              end if ;
           else
              myres = 0 ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getshipkpi(slid int) cascade""")
        self._cr.execute("""create or replace function getshipkpi(slid int) returns float as $BODY$
         DECLARE
           difday int ;
           holiday int ;
           nkpi int ;
           myres float ;
         BEGIN
           select getdifdatenum(slid) into difday ;
           select getholidaynum(slid) into holiday ;
           nkpi = difday - holiday ;
           if nkpi > 0 then
              myres = (100 - (0.5 * (nkpi))) ;
           else
              myres = 100 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop materialized view if exists alldo_acme_iot_shipping_kpi_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (SELECT A.id as id,B.partner_id as partner_id,A.product_id as product_no,B.so_pi as so_pi,B.name as so_no,
             B.commitment_date::DATE as commitment_date,(select getmaxstmdate(A.id)) as shipping_date,
             (select getdifdatenum(A.id)) as dif_value,(select getholidaynum(A.id)) as holiday_num,(select getshipkpi(A.id)) as shipping_kpi from sale_order_line A
                LEFT JOIN sale_order B ON A.order_id = B.id  where A.is_completed=true
                GROUP BY A.product_id,B.partner_id,B.so_pi,B.name,B.commitment_date,A.id)""" % self._table)

        self._cr.execute("""create index ship_kpi1 on %s (so_no)""" % self._table)
        self._cr.execute("""create index ship_kpi2 on %s (so_pi)""" % self._table)
        self._cr.execute("""create index ship_kpi3 on %s (product_no)""" % self._table)
        self._cr.execute("""create index ship_kpi4 on %s (partner_id)""" % self._table)
        self._cr.execute("""create index ship_kpi5 on %s (commitment_date)""" % self._table)
        self._cr.execute("""create index ship_kpi6 on %s (shipping_date)""" % self._table)

        self._cr.execute("""select gensocompleted();""")




