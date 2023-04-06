# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class outsourcingkpiPivotReport(models.Model):
    _name = 'alldo_acme_iot.outsourcing_kpi'
    _description = "Outsourcing KPI Statistics"
    _auto = False


class OutsourcingKPIPivotanalysisreport(outsourcingkpiPivotReport):
    _name = 'alldo_acme_iot.outsourcing_kpi_report'
    # _order = "iot_date,iot_owner"

    @api.depends('dif_value','holiday_num')
    def _get_kpi(self):
        myday = 0
        for rec in self:
            if rec.dif_value and rec.holiday_num:
               myday = rec.dif_value - rec.holiday_num
            else:
               myday = 0
            rec.outsourcing_kpi = 100 - (0.5 * myday) ;


    sub_no = fields.Char(string="委外單號")
    so_pi = fields.Char(string="客戶PI")
    cus_name = fields.Many2one('res.partner', string="委外加工商")
    product_no = fields.Many2one('product.product', string="產品")
    commitment_date = fields.Date(string="應交日期")
    shipping_date = fields.Date(string="實際交期")
    dif_value = fields.Integer(string="差異天數")
    holiday_num = fields.Integer(string="假日數")
    out_num = fields.Integer(string="給料數")
    in_num = fields.Integer(string="回料數")
    complete_per = fields.Float(digits=(6,2),string="完成比例")
    outsourcing_kpi = fields.Float(digits=(6,2),string="KPI",group_operator="avg")


    @api.model
    def init(self):
        # 傳回最後的委外最大收貨日期
        self.env.cr.execute("""drop function if exists getmaxossdate(orderid int) cascade""")
        self.env.cr.execute("""create or replace function getmaxossdate(orderid int) returns DATE as $BODY$
        DECLARE 
           myres date ;
        BEGIN
           select max(date_delivery) into myres from alldo_acme_iot_outsuborder_prodin where order_id=orderid and in_good_num > 0 ;
           return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 傳回最後的委外最大應交貨日期
        self.env.cr.execute("""drop function if exists getmaxoscdate(orderid int) cascade""")
        self.env.cr.execute("""create or replace function getmaxoscdate(orderid int) returns DATE as $BODY$
        DECLARE 
           myres date ;
        BEGIN
           select max(date_due) into myres from alldo_acme_iot_outsuborder_prodout where order_id=orderid and out_good_num > 0 ;
           return myres ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        # 傳回給料總數
        self._cr.execute("""drop function if exists getoutnum(orderid int) cascade""")
        self._cr.execute("""create or replace function getoutnum(orderid int) returns INT as $BODY$
         DECLARE
           myres int ;
         BEGIN
           select sum(out_good_num) into myres from alldo_acme_iot_outsuborder_prodout where order_id=orderid ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 傳回回料總數
        self._cr.execute("""drop function if exists getinnum(orderid int) cascade""")
        self._cr.execute("""create or replace function getinnum(orderid int) returns INT as $BODY$
         DECLARE
           myres int ;
         BEGIN
           select sum(in_good_num) into myres from alldo_acme_iot_outsuborder_prodin where order_id=orderid ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 傳回完成數比例
        self._cr.execute("""drop function if exists getreper(orderid int) cascade""")
        self._cr.execute("""create or replace function getreper(orderid int) returns Float as $BODY$
         DECLARE
           innum int ;
           outnum int ;
           myres Float ;
         BEGIN
           select sum(in_good_num) into innum from alldo_acme_iot_outsuborder_prodin where order_id=orderid ;
           select sum(out_good_num) into outnum from alldo_acme_iot_outsuborder_prodout where order_id=orderid ;
           if outnum = 0 then
              myres = 0.00 ;
           else
              myres = round((innum::numeric/outnum::numeric),2);   
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getodifdatenum(orderid int) cascade""")
        self._cr.execute("""create or replace function getodifdatenum(orderid int) returns INT as $BODY$
         DECLARE
           myres int ;
           outdate date ;
           indate date ;
         BEGIN
           select max(date_due) into outdate from alldo_acme_iot_outsuborder_prodout where order_id=orderid and out_good_num > 0 ;
           select max(date_delivery) into indate from alldo_acme_iot_outsuborder_prodin where order_id=orderid and in_good_num > 0 ;
           if outdate is not null and indate is not null then
              select (indate::DATE - outdate::DATE) into myres ;
           else
              myres = 0 ;
           end if ;   
           if myres < 0 then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getoholidaynum(orderid int) cascade""")
        self._cr.execute("""create or replace function getoholidaynum(orderid int) returns INT as $BODY$
         DECLARE
           myres int ;
           outdate date ;
           indate date ;
           maxdate date ;
           mindate date ;
           ndow int ;
           nnum int ;
         BEGIN
           select max(date_due) into outdate from alldo_acme_iot_outsuborder_prodout where order_id=orderid and out_good_num > 0 ;
           select max(date_delivery) into indate from alldo_acme_iot_outsuborder_prodin where order_id=orderid and in_good_num > 0 ; 
           if outdate is not null and indate is not null then
              if indate > outdate then  /* 實際交貨日超過應交貨期  */
                  mindate = outdate ;
                  maxdate = indate ;
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

        self._cr.execute("""drop function if exists getoutsourcingkpi(orderid int) cascade""")
        self._cr.execute("""create or replace function getoutsourcingkpi(orderid int) returns float as $BODY$
        DECLARE
          difday int ;
          holiday int ;
          nkpi int ;
          myres float ;
        BEGIN
          select getodifdatenum(orderid) into difday ;
          select getoholidaynum(orderid) into holiday ;
          nkpi = difday - holiday ;
              if nkpi > 0 then
                 myres = (100 - (0.5 * (nkpi))) ;
              else
                 myres = 100 ;
              end if ;
              return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        # tools.drop_view_if_exists(self.env.cr, self._table)
        self._cr.execute("""drop materialized view if exists alldo_acme_iot_outsourcing_kpi_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (SELECT A.id as id,A.name as sub_no,A.so_pi as so_pi,A.cus_name as cus_name,A.product_no as product_no,
            (select getmaxoscdate(A.id)) as commitment_date,(select getmaxossdate(A.id)) as shipping_date,(select getoutnum(A.id)) as out_num,
             (select getinnum(A.id)) as in_num,(select getreper(A.id)) as complete_per,(select getodifdatenum(A.id)) as dif_value,
             (select getoholidaynum(A.id)) as holiday_num,(select getoutsourcingkpi(A.id)) as outsourcing_kpi
                 from alldo_acme_iot_outsuborder A where A.active=True
                GROUP BY A.name,A.so_pi,A.cus_name,A.product_no,A.id
        )""" % self._table)

        self._cr.execute("""create index outsourcing_kpi1 on %s (sub_no)""" % self._table)
        self._cr.execute("""create index outsourcing_kpi2 on %s (so_pi)""" % self._table)
        self._cr.execute("""create index outsourcing_kpi3 on %s (product_no)""" % self._table)
        self._cr.execute("""create index outsourcing_kpi4 on %s (cus_name)""" % self._table)
        self._cr.execute("""create index outsourcing_kpi5 on %s (commitment_date)""" % self._table)
        self._cr.execute("""create index outsourcing_kpi6 on %s (shipping_date)""" % self._table)





