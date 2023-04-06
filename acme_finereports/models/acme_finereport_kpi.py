# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api,tools
from odoo.exceptions import UserError


class AlldoAcmeIotFineReportKpi(models.Model):
    _name = "alldo_acme_iot.finereport_kpi"
    _description = "FineReport KPI專用"
    _order = "seq"


    product_no = fields.Many2one('product.product', string="產品")
    eng_type = fields.Char(string="工程別")
    mo_no = fields.Many2one('alldo_acme_iot.workorder', string="工單號")
    seq = fields.Integer(string="SEQ")

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists getlast10qcratio(wkid int) cascade""")
        self._cr.execute("""create or replace function getlast10qcratio(wkid int) returns float as $BODY$
         DECLARE
           myres float ;
           pnn int ;
           mnn int ;
           totnum int ;
         BEGIN
           select coalesce(total_amount_num,0),coalesce(processing_ng_num,0),coalesce(material_ng_num,0) into totnum,pnn,mnn from alldo_acme_iot_cnc_performance_report2
              where wkorder_id=wkid ;
           if pnn is null then
              pnn = 0 ;
           end if ;   
           if mnn is null then
              mnn = 0 ;
           end if ;
           if totnum > 0 then
              myres = round(((pnn::numeric+mnn::numeric)/totnum::numeric)*100,2) ; 
           else
              myres = 0 ;
           end if ;   
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop view if exists finereport_last10kpi_view cascade""")
        self._cr.execute("""CREATE VIEW finereport_last10kpi_view as (
                 select A.product_no,A.eng_type,A.mo_no,A.seq,B.total_amount_num,B.processing_ng_num,B.material_ng_num,B.std_num,B.iot_duration,
                 B.prod_num,B.performance_rate,(select getlast10qcratio(A.mo_no)) as qcratio from alldo_acme_iot_finereport_kpi A left join alldo_acme_iot_cnc_performance_report2 B 
                 on A.mo_no = B.wkorder_id order by A.seq
                  )""")









