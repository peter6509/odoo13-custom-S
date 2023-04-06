# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api, tools, _
import logging

_logger = logging.getLogger(__name__)


class wkorderqckpiPivotReport(models.Model):
    _name = 'alldo_acme_iot.wkorderqc_kpi'
    _description = "Workorder QC KPI Statistics"
    _auto = False


class WkorderQCKPIPivotanalysisreport(wkorderqckpiPivotReport):
    _name = 'alldo_acme_iot.wkorderqc_kpi_report'

    so_no = fields.Char(string="銷售單號")
    so_pi = fields.Char(string="客戶PI")
    product_no = fields.Many2one('product.product', string="產品")
    partner_id = fields.Many2one('res.partner',string="客戶")
    commitment_date = fields.Date(string="交貨日期")
    good_num = fields.Integer(string="良品數")
    cast_ng_num = fields.Integer(string="鑄造不良",group_operator="sum")
    cut_ng_num = fields.Integer(string="切割不良",group_operator="sum")
    prod_tot_num = fields.Integer(string="總數量",group_operator="sum")
    ngratio_kpi = fields.Float(digits=(6,2),string="KPI",group_operator="avg")

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getwkgoodnum(soid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getwkgoodnum(soid int,prodid int) returns INT as $BODY$
         DECLARE
           ncount int ;
           wkid int ;
           myres int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
           if ncount > 0 then
              select id into wkid from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
              select sum(wk_good_num) into myres from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
              if myres is null then
                 myres = 0 ;
              end if ;
           else 
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         language plpgsql""")

        self._cr.execute("""drop function if exists getwkngnum(soid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getwkngnum(soid int,prodid int) returns INT as $BODY$
         DECLARE
           ncount int ;
           wkid int ;
           myres int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
           if ncount > 0 then
              select id into wkid from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
              select sum(wk_ng_num) into myres from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
              if myres is null then
                 myres = 0 ;
              end if ;
           else 
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         language plpgsql""")

        self._cr.execute("""drop function if exists getcutngnum(soid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getcutngnum(soid int,prodid int) returns INT as $BODY$
         DECLARE
           ncount int ;
           wkid int ;
           myres int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
           if ncount > 0 then
              select id into wkid from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
              select sum(cut_ng_num) into myres from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
              if myres is null then
                 myres = 0 ;
              end if ;
           else 
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         language plpgsql""")

        self._cr.execute("""drop function if exists getwktotnum(soid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getwktotnum(soid int,prodid int) returns INT as $BODY$
        DECLARE
          ncount int ;
          wkid int ;
          myres int ;
        BEGIN
          select count(*) into ncount from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
          if ncount > 0 then
             select id into wkid from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
             select sum(coalesce(wk_good_num,0)+coalesce(wk_ng_num,0)+coalesce(cut_ng_num,0)) into myres from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
             if myres is null then
                myres = 0 ;
             end if ;
          else 
             myres = 0 ;
          end if ;
          return myres ;
        END;$BODY$
        language plpgsql""")

        self._cr.execute("""drop function if exists getwkngratio(soid int,prodid int) cascade""")
        self._cr.execute("""create or replace function getwkngratio(soid int,prodid int) returns INT as $BODY$
        DECLARE
          ncount int ;
          wkid int ;
          myres float ;
          ntot int ;
          nng int ;
        BEGIN
          select count(*) into ncount from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
          if ncount > 0 then
             select id into wkid from alldo_acme_iot_workorder where so_no=soid and product_no=prodid ;
             select sum(coalesce(wk_good_num,0)+coalesce(wk_ng_num,0)+coalesce(cut_ng_num,0)) into ntot from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
             select sum(coalesce(wk_ng_num,0)+coalesce(cut_ng_num,0)) into nng from alldo_acme_iot_wkorder_ngratio where order_id=wkid ;
             if ntot > 0 then
                myres = round((nng::numeric/ntot::numeric)*100::numeric ,2) ;
             else
                myres = 0.00 ;
             end if ;
          else 
             myres = 0.00 ;
          end if ;
          return myres ;
        END;$BODY$
        language plpgsql""")

        self._cr.execute("""drop materialized view if exists alldo_acme_iot_wkorderqc_kpi_report cascade""")
        self._cr.execute("""CREATE MATERIALIZED VIEW %s as (SELECT A.id as id,B.partner_id as partner_id,A.product_id as product_no,B.so_pi as so_pi,B.name as so_no,B.commitment_date::DATE as commitment_date,
             (select getwkgoodnum(A.order_id,A.product_id)) as good_num,(select getwkngnum(A.order_id,A.product_id)) as cast_ng_num,(select getcutngnum(A.order_id,A.product_id)) as cut_ng_num,
              (select getwktotnum(A.order_id,A.product_id)) as prod_tot_num,(select getwkngratio(A.order_id,A.product_id)) as ngratio_kpi from sale_order_line A
                LEFT JOIN sale_order B ON A.order_id = B.id  where A.is_completed=true
                GROUP BY A.product_id,B.partner_id,B.so_pi,B.name,A.order_id,A.id,B.commitment_date)""" % self._table)

        self._cr.execute("""create index wkqc_kpi1 on %s (so_no)""" % self._table)
        self._cr.execute("""create index wkqc_kpi2 on %s (so_pi)""" % self._table)
        self._cr.execute("""create index wkqc_kpi3 on %s (product_no)""" % self._table)
        self._cr.execute("""create index wkqc_kpi4 on %s (partner_id)""" % self._table)
        self._cr.execute("""create index wkqc_kpi5 on %s (commitment_date)""" % self._table)






