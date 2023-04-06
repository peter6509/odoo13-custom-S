# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class outorderqcqckpiPivotReport(models.Model):
    _name = 'alldo_acme_iot.outorderqc_kpi'
    _description = "Workorder QC KPI Statistics"
    _auto = False


class OUTOrderQCKPIPivotanalysisreport(outorderqcqckpiPivotReport):
    _name = 'alldo_acme_iot.outorderqc_kpi_report'

    sub_no = fields.Char(string="委外單號")
    so_pi = fields.Char(string="客戶PI")
    product_no = fields.Many2one('product.product', string="產品")
    cus_name = fields.Many2one('res.partner', string="委外加工商")
    commitment_date = fields.Date(string="交貨日期")
    ng_num = fields.Integer(string="不良數",group_operator="sum")
    tot_num = fields.Integer(string="總數量",group_operator="sum")
    ngratio_kpi = fields.Float(digits=(6,2),string="委外不良率％ KPI",group_operator="avg")


    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getprodindate(orderid int) cascade""")
        self._cr.execute("""create or replace function getprodindate(orderid int) returns DATE as $BODY$
         DECLARE
           myres date ;
           ncount int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_outsuborder_prodin  where order_id=orderid ;
           if ncount > 0 then
              select max(prodin_datetime::DATE) into myres from alldo_acme_iot_outsuborder_prodin where order_id=orderid ;
           end if ;
           return myres ;
         END;$BODY$
         language plpgsql""")

        self._cr.execute("""drop function if exists getsubngnum(orderid int) cascade""")
        self._cr.execute("""create or replace function getsubngnum(orderid int) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_outsuborder_ngratio where order_id=orderid  ;
           if ncount > 0 then
              select sum(sub_ng_num) into myres from alldo_acme_iot_outsuborder_ngratio where order_id = orderid ;
           else 
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         language plpgsql""")

        self._cr.execute("""drop function if exists getsubtotnum(orderid int) cascade""")
        self._cr.execute("""create or replace function getsubtotnum(orderid int) returns INT as $BODY$
        DECLARE
          ncount int ;
          myres int ;
        BEGIN
          select count(*) into ncount from alldo_acme_iot_outsuborder_ngratio where order_id=orderid  ;
          if ncount > 0 then
             select sum(coalesce(sub_good_num,0)+coalesce(sub_ng_num,0)) into myres from alldo_acme_iot_outsuborder_ngratio where order_id=orderid  ;
          else 
             myres = 0 ;
          end if ;
          return myres ;
        END;$BODY$
        language plpgsql""")

        self._cr.execute("""drop function if exists getsubngratio(orderid int) cascade""")
        self._cr.execute("""create or replace function getsubngratio(orderid int) returns INT as $BODY$
        DECLARE
          ncount int ;
          myres float ;  
          ntot int ;
          nng int ;
        BEGIN
          select count(*) into ncount from alldo_acme_iot_outsuborder_ngratio where order_id = orderid  ;
          if ncount > 0 then
             select sum(sub_ng_num) into nng from alldo_acme_iot_outsuborder_ngratio where order_id = orderid ;
             if nng is null then
                nng = 0 ;
             end if ;
             select sum(coalesce(sub_good_num,0)+coalesce(sub_ng_num,0)) into ntot from 
                alldo_acme_iot_outsuborder_ngratio where order_id=orderid  ;
             if ntot >  0 then  
                myres = round((nng::numeric/ntot::numeric)*100,2) ;
             else
                myres = 0.00 ;
             end if ;   
          else 
             myres = 0.00 ;
          end if ;
          return myres ;
        END;$BODY$
        language plpgsql""")

        self._cr.execute("""drop materialized view if exists alldo_acme_iot_outorderqc_kpi_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as select A.id as id,A.name as sub_no,A.so_pi as so_pi,A.product_no as product_no,
                            A.cus_name as cus_name,(select getprodindate(A.id)) as commitment_date,(select getsubngnum(A.id)) as ng_num,
                            (select getsubtotnum(A.id)) as tot_num,(select getsubngratio(A.id)) as ngratio_kpi
                               from alldo_acme_iot_outsuborder A
                LEFT JOIN alldo_acme_iot_outsuborder_ngratio B ON B.order_id = A.id
                GROUP BY A.product_no,A.cus_name,A.so_pi,A.name,A.id""" % self._table)

        self._cr.execute("""create index outqc_kpi1 on %s (sub_no)""" % self._table)
        self._cr.execute("""create index outqc_kpi2 on %s (so_pi)""" % self._table)
        self._cr.execute("""create index outqc_kpi3 on %s (product_no)""" % self._table)
        self._cr.execute("""create index outqc_kpi4 on %s (cus_name)""" % self._table)
        self._cr.execute("""create index outqc_kpi5 on %s (commitment_date)""" % self._table)






