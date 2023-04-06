# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class acmestoreproc(models.Model):
    _name = "alldo_acme_iot.finereport_storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genparai(finekey varchar,finevalue int) cascade""")
        self._cr.execute("""create or replace function genparai(finekey varchar,finevalue int) returns void as $BODY$
         DECLARE
           ncount int ;
           myid int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_finereport_para where finereport_key=finekey ;
           if ncount = 0 then
              insert into alldo_acme_iot_finereport_para(finereport_key,finereport_ivalue) values (finekey,finevalue) ;
           else
              select id into myid from alldo_acme_iot_finereport_para where finereport_key = finekey ;
              update alldo_acme_iot_finereport_para set finereport_ivalue=finevalue where id = myid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genparac(finekey varchar,finevalue varchar) cascade""")
        self._cr.execute("""create or replace function genparac(finekey varchar,finevalue varchar) returns void as $BODY$
         DECLARE
           ncount int ;
           myid int ;
         BEGIN
           select count(*) into ncount from alldo_acme_iot_finereport_para where finereport_key=finekey ;
           if ncount = 0 then
              insert into alldo_acme_iot_finereport_para(finereport_key,finereport_cvalue) values (finekey,finevalue) ;
           else
              select id into myid from alldo_acme_iot_finereport_para where finereport_key = finekey ;
              update alldo_acme_iot_finereport_para set finereport_cvalue=finevalue where id = myid ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genprodkpi(prodid int,engtype varchar) cascade""")
        self._cr.execute("""create or replace function genprodkpi(prodid int,engtype varchar) returns void as $BODY$
         DECLARE
           mo_cur refcursor ;
           mo_rec record ;
           nseq int ;
         BEGIN
           delete from alldo_acme_iot_finereport_kpi where product_no=prodid and eng_type ilike '%%'||engtype||'%%' ; 
           nseq = 1 ;
           open mo_cur for select * from alldo_acme_iot_workorder where product_no=prodid and 
               eng_type ilike '%%'||engtype||'%%' and state in ('3','4') and active=True order by name desc ;
           loop
             fetch mo_cur into mo_rec ;
             exit when not found or nseq > 10 ;
             insert into alldo_acme_iot_finereport_kpi(product_no,eng_type,mo_no,seq) values (prodid,engtype,mo_rec.id,nseq) ;
             nseq = nseq + 1 ;
           end loop ;
           close mo_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genwkiotdatastd() cascade""")
        self._cr.execute("""create or replace function genwkiotdatastd() returns void as $BODY$
         DECLARE
           iot_cur refcursor ;
           iot_rec record ;
           prodid int ;
           prodtmplid int ;
           engtype varchar ;
           stdnum int ;
           stdduration int ;
           prnum int ;
         BEGIN
           open iot_cur for select * from alldo_acme_iot_workorder_iot_data where std_duration is null or std_duration = 0 ;
           loop
              fetch iot_cur into iot_rec ;
              exit when not found ;
              select product_no,eng_type into prodid,engtype from alldo_acme_iot_workorder where id = iot_rec.order_id ;
              select product_tmpl_id into prodtmplid from product_product where id = prodid ;
              select standard_num,prod_real_num into stdnum,prnum from alldo_acme_iot_eng_order where prod_id=prodtmplid and eng_type='1' ;
              if stdnum > 0 then
                 stdduration = round((60::numeric/stdnum::numeric),0) ;
              else
                 if prnum > 0 then
                    update alldo_acme_iot_eng_order set standard_num=prnum where prod_id=prodtmplid and eng_type='1' ;
                    stdduration = round((60::numeric/prnum::numeric),0) ;
                 else
                    stdduration = 0 ;
                 end if ;
              end if ;
              update alldo_acme_iot_workorder_iot_data set std_duration=stdduration where id = iot_rec.id ;
           end loop ;
           close iot_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genprodshippingkpi(prodid int) cascade""")
        self._cr.execute("""create or replace function genprodshippingkpi(prodid int) returns void as $BODY$
         DECLARE
           so_cur refcursor ;
           so_rec record ;
           nseq int ;
         BEGIN
           delete from alldo_acme_iot_finereport_shipping_kpi where product_no=prodid ;
           nseq = 1 ;
           open so_cur for select * from alldo_acme_iot_shipping_kpi_report where product_no=prodid order by commitment_date desc ;
           loop
             fetch so_cur into so_rec ;
             exit when not found or nseq > 10 ;
             insert into alldo_acme_iot_finereport_shipping_kpi(product_no,so_no,seq) values (prodid,so_rec.so_no,nseq) ;
             nseq = nseq + 1 ;
           end loop ;
           close so_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genequipprodkpi() cascade""")
        self._cr.execute("""create or replace function genequipprodkpi() returns void as $BODY$
         DECLARE
            equ_cur refcursor ;
            equ_rec record ;
            prodid int ;            
         BEGIN
            open equ_cur for select * from finereport_main_equip_view ;
            loop
              fetch equ_cur into equ_rec ;
              exit when not found ;
                select id into prodid from product_product where default_code = equ_rec.default_code ;
                perform genprodkpi(prodid,equ_rec.eng_type) ;
            end loop ;
            close equ_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

