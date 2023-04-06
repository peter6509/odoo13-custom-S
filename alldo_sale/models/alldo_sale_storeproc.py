# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class alldosalestoreproc(models.Model):
    _name = "alldo_sale.salestoreproc"

    @api.model
    def init(self):
        self.env.cr.execute("""drop function if exists setdiscountamount(orderid int) cascade""")
        self.env.cr.execute("""create or replace function setdiscountamount(orderid int) returns void as $BODY$
          DECLARE
            amountuntax float ;
            amounttax float ;
            amounttot float ;
          BEGIN
            select sitem_untax into amountuntax from sale_order where id = orderid ;
            amounttax := amountuntax * 0.05 ;
            amounttot := amountuntax + amounttax ;
            update sale_order set discount_amount=amountuntax,sitem_tax=amounttax,sitem_amounttot=amounttot where id = orderid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute(
            """DROP FUNCTION IF EXISTS gensaleline(ownerid int,saleid int,prodid int,taxesid int) cascade;""")
        self.env.cr.execute("""create or replace function gensaleline(ownerid int,saleid int,prodid int,taxesid int) returns void as $BODY$
                 declare
                   mycreatedate DATE;
                   myprodname varchar;
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
                   myname varchar;
                   mytaxrate float;
                   mylineid integer;
                   mysaleno varchar;

                 begin
                   select company_id into mycompanyid from res_users where id=ownerid;
                   select partner_id,create_date,discount_amount into mypartnerid,mycreatedate,mypricesubtot from sale_order where id=saleid;
                   select name,uom_id into myname,myproduom from product_template where id=prodid ;
                   select amount into mytaxrate from account_tax where id=taxesid ;
                   select count(*) into mycount from sale_order_line where order_id=saleid ;
                   /*select sum(round(sitem_num*sitem_price)) into mypricesubtot from alldo_sale_sitem_list where sitem_id=saleid ;*/
                   mypricetax := round(mypricesubtot * mytaxrate / 100) ;
                   mypricetotal := mypricesubtot + mypricetax ;
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
                   update sale_order set amount_untaxed=mypricesubtot,amount_tax=mypricetax,amount_total=mypricetotal,
                    create_tag=False where id=saleid;
                   /* delete from alldo_sale_sitem_list where sitem_price=0 and sitem_id=saleid; */
                 end;
                 $BODY$
                 LANGUAGE plpgsql ;

                 """)

        self.env.cr.execute(
            """DROP FUNCTION IF EXISTS gensaletaxesid(saleorderid int) cascade;""")
        self.env.cr.execute("""create or replace function gensaletaxesid(saleorderid int) returns void as $BODY$
        declare
          mytaxesid int;
          mysaleorderlineid int;
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

        self.env.cr.execute("""drop function if exists setsaleitem(orderid int) cascade""")
        self.env.cr.execute("""create or replace function setsaleitem(orderid int) returns void as $BODY$
          DECLARE
            sale_cur refcursor ;
            sale_rec record ;
            att_cur refcursor ;
            att_rec record ;
            nitem int ;
          BEGIN
          nitem := 1 ;
            open sale_cur for select * from alldo_sale_sitem_list where sitem_id=orderid order by sequence,id ;
            loop
              fetch sale_cur into sale_rec ;
              exit when not found ;
              update alldo_sale_sitem_list set sitem_item=nitem where id = sale_rec.id ;
              nitem := nitem + 1 ;
            end loop ;
            close sale_cur ;
            nitem := 1 ;
            open att_cur for select * from alldo_sale_attach_line where attach_id=orderid order by sequence,id ;
            loop
              fetch att_cur into att_rec;
              exit when not found ;
              update alldo_sale_attach_line set attach_item=nitem where id = att_rec.id ;
              nitem := nitem + 1 ;
            end loop ;
            close att_cur ; 
          END;$BODY$
          LANGUAGE plpgsql;""")
