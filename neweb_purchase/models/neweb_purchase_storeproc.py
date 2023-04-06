# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class newebpurchasestoreproc(models.Model):
    _name = "neweb.purchasestoreproc"


    #  按照採購明細(非列管品項) 產生一筆列管料號品項記錄 store procedure
    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS genpurline(ownerid int,purid int,prodid int,taxesid int) cascade;""")
        self._cr.execute("""create or replace function genpurline(ownerid int,purid int,prodid int,taxesid int) returns void as $BODY$
    declare
      mycreatedate purchase_order.create_date%type;
      myprodname product_template.name%type;
      mycount integer;
      mycompanyid integer;
      mypartnerid integer;
      myproduom integer;
      mypriceunit purchase_order_line.price_unit%type;
      mytaxesid integer;
      mydateplanned purchase_order_line.date_planned%type ;
      mypricesubtot purchase_order_line.price_subtotal%type;
      mypricetotal  purchase_order_line.price_total%type;
      mypricetax  purchase_order_line.price_tax%type;
      mycurrencyid integer;
      myname product_template.name%type;
      mytaxrate account_tax.amount%type;
      mylineid integer;
      mypurchaseno purchase_order.name%type;
      myprodnum neweb_pitem_list.pitem_num%type;
      refpur refcursor;
      refpurrow record;
    begin
      select company_id into mycompanyid from res_users where id=ownerid;
      select date_planned,partner_id,create_date into mydateplanned,mypartnerid,mycreatedate from purchase_order where id=purid;
      if mydateplanned is null then
         mydateplanned := mycreatedate ;
      end if ;
      select name,uom_po_id into myname,myproduom from product_template where id=prodid ;
      select amount into mytaxrate from account_tax where id=taxesid ;
      select count(*) into mycount from purchase_order_line where order_id=purid and product_id=prodid;
      select sum(pitem_num*pitem_price) into mypricesubtot from neweb_pitem_list where pitem_id=purid ;
      mypricetax := round(mypricesubtot * (mytaxrate / 100)) ;
      mypricetotal := mypricesubtot + mypricetax ;
      select currency_id into mycurrencyid from res_company where id=mycompanyid ;
      select id into mylineid from purchase_order_line where order_id=purid ;
      if mycount = 0 then
         insert into purchase_order_line (create_uid,write_uid,create_date,write_date,partner_id,product_uom,product_id,name,product_qty,
          price_unit,date_planned,order_id,company_id,currency_id,price_subtotal,price_total,price_tax,write_type) values
          (ownerid,ownerid,mycreatedate,mycreatedate,mypartnerid,myproduom,prodid,myname,1,mypricesubtot,mydateplanned,
          purid,mycompanyid,mycurrencyid,mypricesubtot,mypricetotal,mypricetax,'2');
      else
        update purchase_order_line set partner_id=mypartnerid,product_uom=myproduom,product_id=prodid,name=myname,product_qty=1,
               price_unit=mypricesubtot,date_planned=mydateplanned,price_subtotal=mypricesubtot,price_total=mypricetotal,
               price_tax=mypricetax,currency_id=mycurrencyid where order_id=purid and product_id=prodid;
      end if ;
      delete from purchase_order_line where product_id != prodid and order_id=purid and write_type='2' ;
      open refpur for select * from neweb_pitem_list where pitem_id=purid and prod_id is not null;
      loop
        fetch refpur into refpurrow ;
        exit when not found;
        select count(*) into mycount from purchase_order_line where product_id=refpurrow.prod_id and order_id=purid;
        if mycount=0 then
           select name into myname from product_template where id=refpurrow.prod_id ;
           insert into purchase_order_line (create_uid,write_uid,create_date,write_date,partner_id,product_uom,product_id,name,product_qty,
             price_unit,date_planned,order_id,company_id,currency_id,price_subtotal,price_total,price_tax,write_type) values
             (ownerid,ownerid,mycreatedate,mycreatedate,mypartnerid,myproduom,refpurrow.prod_id,myname,refpurrow.pitem_num,0,mydateplanned,
             purid,mycompanyid,mycurrencyid,0,0,mypricetax,'2');
        else
           select sum(pitem_num) into myprodnum from neweb_pitem_list where pitem_id=purid and prod_id=refpurrow.prod_id;
           select name into myname from product_template where id=refpurrow.prod_id ;
           update purchase_order_line set name=myname,product_qty=myprodnum where order_id=purid and product_id=refpurrow.prod_id;
        end if;
      end loop;
      close refpur;
      update purchase_order set amount_untaxed=mypricesubtot,amount_tax=mypricetax,amount_total=mypricetotal,pitem_tax=mypricetax,
         pitem_amounttot=mypricetotal  where id=purid;
      delete from neweb_pitem_list where pitem_num=0 and pitem_price=0 and pitem_id=purid ;
    end;
    $BODY$
    LANGUAGE plpgsql ;

    """)

        # 採購選取申購單內容(局部or全部)資料copy到採購單明細
        self._cr.execute("""DROP FUNCTION IF EXISTS genreqline(reqlineid int,purid int) cascade;""")
        self._cr.execute("""create or replace function genreqline(reqlineid int,purid int) returns void as $BODY$
           declare
             myrequireno neweb_require_purchase.name%type;
             mypitemid neweb_require_purchase_item.pitem_id%type;
             myamountuntaxed purchase_order.amount_untaxed%type;
             myamounttax purchase_order.amount_tax%type;
             myamounttotal purchase_order.amount_total%type;
             mytaxesid account_tax.id%type;
             myamount account_tax.amount%type;
           begin
            select pitem_id into mypitemid from neweb_require_purchase_item where id=reqlineid;
            select name into myrequireno from neweb_require_purchase where id=mypitemid;
            insert into neweb_pitem_list (pitem_id,pitem_model_type,prod_id,pitem_spec,pitem_num,pitem_price,pitem_sum,pitem_origin_no,pitem_origin_id,pitem_origin_type,pitem_stockin_num,pur_memo) select
              purid,pitem_modeltype,prod_id,pitem_desc,(pitem_num - pitem_purnum),pitem_price,(pitem_num*pitem_price),myrequireno,id,'R',0,pur_memo from neweb_require_purchase_item
              where id=reqlineid ;
            select sum(pitem_num*pitem_price) into myamountuntaxed from neweb_pitem_list where pitem_id = purid ;
                 select taxes_id into mytaxesid from purchase_order where id=purid ;
                 select amount into myamount from account_tax where id = mytaxesid ;
                 myamounttax := round(myamountuntaxed * (myamount / 100)) ;
                 myamounttotal := myamountuntaxed + myamounttax ;
                 update purchase_order set amount_untaxed=myamountuntaxed,amount_tax=myamounttax,amount_total=myamounttotal,
                      pitem_untax=myamountuntaxed,pitem_tax=myamounttax,pitem_amounttot=myamounttotal where id=purid ;
           end;
           $BODY$
           LANGUAGE plpgsql;""")

        # 定義採購單號格式
        mysequence = self.env['ir.sequence'].search([('code', '=', 'purchase.order')])
        if mysequence:
            mysequence.write({'prefix': 'PO%(y)s%(month)s%(day)s',
                              'padding': 2,
                              # 'auto_reset': True,
                              # 'reset_period': 'day',
                              'number_next_actual': 1})

        # 寫入採購明細行中(原生purchase_order_line) taxes_id 值
        self._cr.execute(
            """DROP FUNCTION IF EXISTS genpurchasetaxesid(purchaseorderid int) cascade;""")
        self._cr.execute("""create or replace function genpurchasetaxesid(purchaseorderid int) returns void as $BODY$
        declare
          mytaxesid account_tax.id%type;
          mypurchaseorderlineid purchase_order.id%type;
          ncount integer;
        begin
          select id into mypurchaseorderlineid from purchase_order_line where order_id=purchaseorderid ;
          select taxes_id into mytaxesid from purchase_order where id=purchaseorderid ;
          select count(*) into ncount from account_tax_purchase_order_line_rel where purchase_order_line_id = mypurchaseorderlineid and account_tax_id=mytaxesid ;
          if ncount = 0 then
            insert into account_tax_purchase_order_line_rel (purchase_order_line_id,account_tax_id) values (mypurchaseorderlineid,mytaxesid) ;
          end if ;
        end;$BODY$
        LANGUAGE plpgsql ;
        """)


        # 當採購單確認正式訂單後,要回填 專案分析或申購單採購單號與狀態(並改寫 供應商與單價) purtype="1"
        self._cr.execute("""DROP FUNCTION IF EXISTS purchasecommit(purid int,purtype int) cascade;""")
        self._cr.execute("""create or replace function purchasecommit(purid int,purtype int) returns void as $BODY$
    declare
      refpur refcursor ;
      refpurrow record ;
      mypurchaseno purchase_order.name%type ;
      mysuppliername res_partner.name%type;
      mycompsname res_partner.comp_sname%type;
      mysupplierid purchase_order.id%type;
      ncount INTEGER ;
      ncount1 INTEGER ;
      myprodnum neweb_projsaleitem.prod_num%type;
      myprodpurnum neweb_projsaleitem.prod_purnum%type;
      mystate purchase_order.state%type;
      myrate FLOAT ;
      mycurrencyid INTEGER ;
      projid INTEGER ;
      myoriginno VARCHAR ;
      myorigintype CHAR ;
      myprodprice float ;
    begin
      select pitem_origin_no,pitem_origin_type into myoriginno,myorigintype from neweb_pitem_list where pitem_id=purid ;
      select name,partner_id,state,currency_id into mypurchaseno,mysupplierid,mystate,mycurrencyid from purchase_order where id=purid ;
      select count(*) into ncount from res_currency_rate where currency_id=mycurrencyid ;
      if ncount > 0 THEN 
         select rate into myrate from res_currency_rate where currency_id=mycurrencyid and id=(select max(id) from res_currency_rate where currency_id=mycurrencyid) ;
      ELSE 
         myrate := 1 ;
      end if;
      select name,comp_sname into mysuppliername,mycompsname from res_partner where id=mysupplierid ;
      open refpur for select * from neweb_pitem_list where pitem_id=purid ;
      LOOP
        fetch refpur into refpurrow;
        exit when not found;
        myprodprice = refpurrow.pitem_price * round(1::numeric/myrate::numeric) ;
        if purtype=1 then   /* confirm write purchase_order*/
           if refpurrow.pitem_origin_type='R' then
              update neweb_require_purchase set state='2' where name=refpurrow.pitem_origin_no;
              update neweb_require_purchase_item set pitem_purnum=pitem_purnum+refpurrow.pitem_num,purchase_no=mypurchaseno,supplier=mysupplierid,pitem_price=(refpurrow.pitem_price/myrate),pitem_budget=(pitem_num * pitem_price) where id=refpurrow.pitem_origin_id ;
              select pitem_num,pitem_purnum into myprodnum,myprodpurnum from neweb_require_purchase_item where id=refpurrow.pitem_origin_id ;
              if myprodnum = myprodpurnum then
                 update neweb_require_purchase_item set purok=TRUE where id=refpurrow.pitem_origin_id ;
              else
                 update neweb_require_purchase_item set purok=FALSE where id=refpurrow.pitem_origin_id ;
              end if;
           else
              update neweb_project set purchase_yn=TRUE where name=refpurrow.pitem_origin_no;
              update neweb_projsaleitem set prod_origin_price=prod_price where id=refpurrow.pitem_origin_id ;
              if length(mycompsname) > 0 then
                 update neweb_projsaleitem set prod_purnum=prod_purnum+refpurrow.pitem_num,purchase_no=mypurchaseno,supplier=mysupplierid,prod_price=myprodprice where id=refpurrow.pitem_origin_id ;
              else
                 update neweb_projsaleitem set prod_purnum=prod_purnum+refpurrow.pitem_num,purchase_no=mypurchaseno,supplier=mysupplierid,prod_price=myprodprice where id=refpurrow.pitem_origin_id ;
              end if ;
              select prod_num,prod_purnum into myprodnum,myprodpurnum from neweb_projsaleitem where id=refpurrow.pitem_origin_id ;
              if myprodnum = myprodpurnum then
                 update neweb_projsaleitem set purok=TRUE where id=refpurrow.pitem_origin_id ;
              else
                 update neweb_projsaleitem set purok=FALSE where id=refpurrow.pitem_origin_id ;
              end if;
              update neweb_pitem_list set pitem_delete_yn=FALSE  where id=refpurrow.id;
           end if ;
       elsif purtype=2 then  /* cancel purchase_order */
           if refpurrow.pitem_origin_type='R' then
              if mystate='purchase' or mystate='done' then
                 update neweb_require_purchase set state='1' where name=refpurrow.pitem_origin_no;
                 update neweb_require_purchase_item set pitem_purnum=pitem_purnum - refpurrow.pitem_num,purchase_no=null where id=refpurrow.pitem_origin_id ;
                 select pitem_num,pitem_purnum into myprodnum,myprodpurnum from neweb_require_purchase_item where id=refpurrow.pitem_origin_id ;
                 if myprodnum = myprodpurnum then
                    update neweb_require_purchase_item set purok=TRUE where id=refpurrow.pitem_origin_id ;
                 else
                    update neweb_require_purchase_item set purok=FALSE where id=refpurrow.pitem_origin_id ;
                 end if;
              end if;
           else
              if mystate='purchase' or mystate='done' then
                 update neweb_project set purchase_yn=FALSE where name=refpurrow.pitem_origin_no;
                 update neweb_projsaleitem set prod_purnum=prod_purnum-refpurrow.pitem_num,purchase_no=null where id=refpurrow.pitem_origin_id ;
                 select prod_num,prod_purnum into myprodnum,myprodpurnum from neweb_projsaleitem where id=refpurrow.pitem_origin_id ;
                 if myprodnum = myprodpurnum then
                    update neweb_projsaleitem set purok=TRUE where id=refpurrow.pitem_origin_id ;
                 else
                    update neweb_projsaleitem set purok=FALSE where id=refpurrow.pitem_origin_id ;
                 end if;
              end if;
           end if ;
           update neweb_pitem_list set pitem_delete_yn=TRUE  where id=refpurrow.id;
       end if;
      END LOOP ;
      close refpur ;
      open refpur for select distinct pitem_origin_no,pitem_origin_type from neweb_pitem_list where pitem_id = purid;
      loop
        fetch refpur into refpurrow;
        exit when not found;
        if refpurrow.pitem_origin_type='P' then
           select count(A.saleitem_id) into ncount from neweb_projsaleitem A,neweb_project B where A.saleitem_id=B.id and B.name=refpurrow.pitem_origin_no and A.prod_purnum < A.prod_num ;
           if ncount = 0 then
              update neweb_project set purchase_yn=TRUE where name=refpurrow.pitem_origin_no ;
           else
              update neweb_project set purchase_yn=FALSE where name=refpurrow.pitem_origin_no ;
           end if;
       else
           select count(A.pitem_id) into ncount1 from neweb_require_purchase_item A,neweb_require_purchase B where A.pitem_id=B.id and
               B.name=refpurrow.pitem_origin_no and A.pitem_purnum < A.pitem_num ;
           if ncount1 = 0 then
              update neweb_require_purchase set purchase_yn=TRUE,state=2  where name=refpurrow.pitem_origin_no ;
           else
               update neweb_require_purchase set purchase_yn=FALSE,state=1  where name=refpurrow.pitem_origin_no ;
           end if;
        end if;
      end loop;
      close refpur ;
      if myorigintype='P' and purtype='1' THEN 
         select id into projid from neweb_project where name like myoriginno ;
         execute proj_rcal_cost(projid) ;
      END if;
    end;$BODY$
    LANGUAGE plpgsql;""")



        self._cr.execute("""DROP FUNCTION IF EXISTS purchaseitemunlink(pitemid int) cascade;""")
        self._cr.execute("""create or replace function purchaseitemunlink(pitemid int) returns void as $BODY$
        DECLARE
           refpur refcursor;
           refpurrow record;
           myprodnum neweb_projsaleitem.prod_num%type;
           myprodpurnum neweb_projsaleitem.prod_purnum%type;
           mystate purchase_order.state%type;
           mypurnum neweb_require_purchase_item.pitem_purnum%type;
        BEGIN
           open refpur for select * from neweb_pitem_list where id=pitemid ;
           loop
             fetch refpur into refpurrow;
             exit when not found;
             select state into mystate from purchase_order where id=pitemid;
             if refpurrow.pitem_origin_type='R' then
                  update neweb_require_purchase set state='1' where name=refpurrow.pitem_origin_no;
                  select (pitem_purnum - refpurrow.pitem_num) into mypurnum from neweb_require_purchase_item where id=refpurrow.pitem_origin_id ;
                  if mystate = 'purchase' or mystate='done' then
                     if mypurnum < 0 then
                        update neweb_require_purchase_item set pitem_purnum=0,purchase_no=null where id=refpurrow.pitem_origin_id ;
                     else
                        update neweb_require_purchase_item set pitem_purnum=pitem_purnum - refpurrow.pitem_num,purchase_no=null where id=refpurrow.pitem_origin_id ;
                     end if;
                  end if;
                  select pitem_num,pitem_purnum into myprodnum,myprodpurnum from neweb_require_purchase_item where id=refpurrow.pitem_origin_id ;
                  if myprodnum = myprodpurnum then
                     update neweb_require_purchase_item set purok=TRUE where id=refpurrow.pitem_origin_id ;
                  else
                     update neweb_require_purchase_item set purok=FALSE where id=refpurrow.pitem_origin_id ;
                  end if;
               elsif refpurrow.pitem_origin_type='P' then
                  update neweb_project set purchase_yn=FALSE where name=refpurrow.pitem_origin_no;
                  if mystate='purchase' or mystate='done' then
                     update neweb_projsaleitem set prod_purnum=prod_purnum-refpurrow.pitem_num,purchase_no=null where id=refpurrow.pitem_origin_id ;
                     select prod_num,prod_purnum into myprodnum,myprodpurnum from neweb_projsaleitem where id=refpurrow.pitem_origin_id ;
                     if myprodnum = myprodpurnum then
                        update neweb_projsaleitem set purok=TRUE where id=refpurrow.pitem_origin_id ;
                     else
                        update neweb_projsaleitem set purok=FALSE where id=refpurrow.pitem_origin_id ;
                     end if;
                  end if;
               end if ;
               update neweb_pitem_list set pitem_delete_yn=TRUE  where id=refpurrow.id;
           end loop;
           close refpur;
        END ;$BODY$
        LANGUAGE plpgsql;
        
                                 """)


        self._cr.execute("""DROP FUNCTION IF EXISTS getunpurchaseitem(unpurid int,reqid int) cascade;""")
        self._cr.execute("""create or replace function getunpurchaseitem(unpurid int,reqid int) returns void as $BODY$
DECLARE
   refreq refcursor;
   refreqrec record;
BEGIN
  open refreq for select id from neweb_require_purchase_item where purok=FALSE and id=reqid;
  loop
    fetch refreq into refreqrec;
    exit when not found;
    insert into neweb_require_purchase_item_neweb_unpurchase_item_rel(neweb_unpurchase_item_id,neweb_require_purchase_item_id) VALUES
       (unpurid,refreqrec.id);
  end loop;
  close refreq;
END ; $BODY$
LANGUAGE plpgsql;
        """)


        self._cr.execute("""DROP FUNCTION IF EXISTS getpurdata(purid int) cascade;""")
        self._cr.execute("""create or replace function getpurdata(purid int) returns void as $BODY$
DECLARE
  refcur refcursor;
  refrec record;
  myname purchase_order.name%type;
  myid INTEGER ;
  mypitemid neweb_require_purchase.id%type;
BEGIN
  delete from neweb_unpur ;
  open refcur for select * from neweb_require_purchase_item where pitem_id=purid and (pitem_num - pitem_purnum) > 0 
     order by pitem_nid,id;
  select distinct pitem_id into mypitemid from neweb_require_purchase_item where pitem_id=purid ;
  select name into myname from neweb_require_purchase where id = mypitemid ;
  insert into neweb_unpur(name) values (myname);
  select id into myid from neweb_unpur where name=myname;
  loop
    fetch refcur into refrec;
    exit when not found;
    insert into neweb_unpuritem(pitem_id,pseq_id,pitem_modeltype,prod_id,pitem_serial,pitem_no,pitem_desc,pitem_num,pitem_purnum,pitem_price,supplier,pur_memo) VALUES
     (myid,refrec.id,refrec.pitem_modeltype,refrec.prod_id,refrec.pitem_serial,refrec.pitem_no,refrec.pitem_desc,refrec.pitem_num,
      refrec.pitem_purnum,refrec.pitem_price,refrec.supplier,refrec.pur_memo);
  end loop;
  close refcur;
END ;$BODY$
LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS getprojdata(projid int) cascade;""")
        self._cr.execute("""create or replace function getprojdata(projid int) returns void as $BODY$
        DECLARE
          refcur refcursor;
          refrec record;
          myname neweb_project.name%type;
          myid neweb_project.id%type;
          mysaleitemid neweb_projsaleitem.id%type;
        BEGIN
          delete from neweb_unproj ;
          open refcur for select * from neweb_projsaleitem where saleitem_id=projid and (coalesce(prod_num,0) - coalesce(prod_purnum,0)) > 0 order by id;
          select distinct saleitem_id into mysaleitemid from neweb_projsaleitem where saleitem_id=projid ;
          select name into myname from neweb_project where id = mysaleitemid ;
          insert into neweb_unproj(name) values (myname);
          select id into myid from neweb_unproj where name=myname;
          loop
            fetch refcur into refrec;
            exit when not found;
            insert into neweb_unprojitem(saleitem_id,prodseq_id,prod_modeltype,prod_serial,prod_no,prod_desc,prod_num,prod_purnum,prod_price,supplier) VALUES
             (myid,refrec.id,refrec.prod_modeltype,refrec.prod_serial,refrec.prod_no,refrec.prod_desc,refrec.prod_num,
              refrec.prod_purnum,refrec.prod_price,refrec.supplier);
          end loop;
          close refcur;
        END ;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS purupdateprojanalysis(purid int) cascade;""")
        self._cr.execute("""create or replace function purupdateprojanalysis(purid int) returns void as $BODY$
        DECLARE
           mypurchaseno varchar;
           refcur refcursor;
           refrec record;
           myanalysiscost FLOAT ;
           myprojid int;
           mytotanalysisrevenue FLOAT ;
           mytotanalysiscost FLOAT ;
           
        BEGIN 
           select name into mypurchaseno from purchase_order where id=purid;
           open refcur for select distinct cost_type from neweb_projsaleitem where purchase_no like mypurchaseno ;
           loop
             fetch refcur into refrec ;
             exit when not found;
             select sum(prod_price*prod_num) into myanalysiscost from neweb_projsaleitem where purchase_no like mypurchaseno and cost_type=refrec.cost_type;
             select distinct saleitem_id into myprojid from neweb_projsaleitem where purchase_no like mypurchaseno ;
             update neweb_projanalysis set analysis_cost=myanalysiscost where analysis_id=myprojid and analysis_costtype=refrec.cost_type;
             update neweb_projanalysis set analysis_profit=(analysis_revenue - analysis_cost),analysis_profitrate=(((analysis_revenue - analysis_cost) / analysis_cost) * 100) where analysis_id=myprojid and 
                analysis_costtype=refrec.cost_type and analysis_cost > 0;
           end loop;
           close refcur;
           select sum(analysis_revenue),sum(analysis_cost) into mytotanalysisrevenue,mytotanalysiscost from neweb_projanalysis where analysis_id=myprojid ;
          /* update neweb_project set total_analysis_revenue=mytotanalysisrevenue,total_analysis_cost=mytotanalysiscost,
                  total_analysis_profit=(mytotanalysisrevenue - mytotanalysiscost),total_analysis_profitrate=((mytotanalysisrevenue - mytotanalysiscost)/mytotanalysiscost)
                  where id = myprojid and mytotanalysiscost > 0 ; */
           END ;$BODY$
           LANGUAGE plpgsql;
        """)


        self._cr.execute("""drop function if exists getprojid(purchaseid int) cascade""")
        self._cr.execute("""create or replace function getprojid(purchaseid int) returns INTEGER as $BODY$
           declare 
             ncount int ;
             myprojid int;
             mypurchasename varchar;
           begin 
             select name into mypurchasename from purchase_order where id=purchaseid ;
             select distinct saleitem_id into myprojid from neweb_projsaleitem where purchase_no = mypurchasename ;
             return myprojid ; 
           end;$BODY$
           LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists check_projreqno(purchaseid int) cascade""")
        self._cr.execute("""create or replace function check_projreqno(purchaseid int) returns void as $BODY$
           declare 
             ncount int;
             myorigintype CHAR;
             myoriginid int ;
             myoriginno varchar;
             myoriginno1 varchar;
             mypurchasename varchar ;
             pur_cur refcursor ;
             pur_rec record ;
             myno varchar ;
             myno1 varchar ;
           begin 
             select name into mypurchasename from purchase_order where id=purchaseid ;
             open pur_cur for select * from neweb_pitem_list where pitem_id=purchaseid order by pitem_origin_no;
             myno := '' ;
             myno1 := '' ;
             loop
                fetch pur_cur into pur_rec ;
                exit when not found ;
                if myno != pur_rec.pitem_origin_no then
                   if myno1 = '' then
                     myno1 := pur_rec.pitem_origin_no ;
                   else
                     myno1 := concat(myno1,',',pur_rec.pitem_origin_no) ;
                   end if ;
                   myno := pur_rec.pitem_origin_no ;
                end if ;
             end loop ;
             close pur_cur ;
             if substring(myno1,1,1)=',' then
                myno1 = substring(myno1,2,length(myno1)-1) ;
             end if ;
             update stock_picking set stockout_proj_no=myno1,state='assigned' where origin=mypurchasename ;  
           end;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_allprojreqno() cascade""")
        self._cr.execute("""create or replace function check_allprojreqno() returns void as $BODY$
            declare 
              pur_cur refcursor ;
              pur_rec record ;
              myorigintype CHAR;
              myoriginid int ;
              myoriginno varchar;
              myoriginno1 varchar;
              pur1_cur refcursor ;
              pur1_rec record ;
              myno varchar ;
              myno1 varchar ;
            begin 
              open pur_cur for select id,name from purchase_order ;
              loop
                fetch pur_cur into pur_rec ;
                exit when not found ;
                open pur1_cur for select * from neweb_pitem_list where pitem_id=pur_rec.id order by pitem_origin_no;
                myno := '' ;
                myno1 := '' ;
                loop
                   fetch pur1_cur into pur1_rec ;
                   exit when not found ;
                   if myno != pur1_rec.pitem_origin_no and pur1_rec.pitem_origin_no is not null then
                      if myno1 = '' then
                        myno1 := pur1_rec.pitem_origin_no ;
                      else
                        myno1 := concat(myno1 , ',' , pur1_rec.pitem_origin_no) ;
                      end if ;
                      myno := pur1_rec.pitem_origin_no ;
                   end if ;
                end loop ;
                close pur1_cur ;
                if substring(myno1,1,1)=',' then
                   myno1 = substring(myno1,2,length(myno1)-1) ;
                end if ;
                update stock_picking set stockout_proj_no=myno1 where origin=pur_rec.name ; 
              end loop ;
              close pur_cur ;
            end ; $BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_all_origin() cascade;""")
        self._cr.execute("""create or replace function check_all_origin() returns void as $BODY$
            DECLARE 
              pur_cur refcursor ;
              pur_rec record ;
              myorigin varchar;
              pur1_cur refcursor ;
              pur1_rec record ;
              myno varchar ;
              myno1 varchar ;
            BEGIN
              open pur_cur for select * from purchase_order ;
              loop
                fetch pur_cur into pur_rec ;
                exit when not found ;
                myno := '' ;
                myno1 := '' ;
                open pur1_cur for select * from neweb_pitem_list where  pitem_id = pur_rec.id  order by pitem_origin_no;
                loop
                   fetch pur1_cur into pur1_rec ;
                   exit when not found ;
                   if myno != pur1_rec.pitem_origin_no then
                      if myno1 ='' then
                         myno1 := pur1_rec.pitem_origin_no ;
                      else
                         myno1 := concat(myno1,',',pur1_rec.pitem_origin_no) ;
                      end if ;
                      myno := pur1_rec.pitem_origin_no ;
                   end if ;
                end loop ;
                close pur1_cur ;
                if substring(myno1,1,1)=',' then
                  myno1 = substring(myno1,2,length(myno1)-1) ;
               end if ;
                update purchase_order set origin=myno1 where id=pur_rec.id ; 
              end loop ;
              close pur_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_origin(purid int) cascade;""")
        self._cr.execute("""create or replace function check_origin(purid int) returns void as $BODY$
            DECLARE
               myorigin varchar;
               pur_cur refcursor ;
               pur_rec record ;
               myno varchar ;
               myno1 varchar ;
            BEGIN
               myno := '' ;
               myno1 := '' ;
               open pur_cur for select * from neweb_pitem_list where  pitem_id = purid  order by pitem_origin_no;
               loop
                 fetch pur_cur into pur_rec ;
                 exit when not found ;
                 if myno != pur_rec.pitem_origin_no then
                    myno1 := concat(myno1,',',pur_rec.pitem_origin_no) ;
                    myno := pur_rec.pitem_origin_no ;
                 end if ;
               end loop ;
               close pur_cur ;
               if substring(myno1,1,1)=',' then
                  myno1 = substring(myno1,2,length(myno1)-1) ;
               end if ;
               update purchase_order set origin=myno1 where id=purid;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists updatepurnum(purid int) cascade;""")
        self._cr.execute("""create or replace function updatepurnum(purid int) returns void as $BODY$
            DECLARE 
              ncount int ;
              purnum float ;
              purcur refcursor ;
              purrec record ;
            BEGIN 
              open purcur for select * from neweb_pitem_list where pitem_id=purid and pitem_origin_type='P' ;
              loop
                 fetch purcur into purrec ;
                 exit when not found ;
                 if purrec.pitem_num > 0 then 
                    update neweb_projsaleitem set prod_num=purrec.pitem_num where id=purrec.pitem_origin_id ;
                 end if ;
              end loop ;
              close purcur ;
            END ; $BODY$
            LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genallpid() cascade""")
        self._cr.execute("""create or replace function genallpid() returns void as $BODY$
            DECLARE
              pur_cur refcursor ;
              pur_rec record ;
              purline_cur refcursor ;
              purline_rec record ;
              mypid varchar ;
              mypidno varchar ;
            BEGIN
              open pur_cur for select id from purchase_order ;
              loop
                mypid := '' ;
                fetch pur_cur into pur_rec ;
                exit when not found ;
                mypidno := '' ;
                open purline_cur for select pitem_origin_no,pitem_id from neweb_pitem_list
                    where pitem_id=pur_rec.id order by pitem_origin_no ;
                loop
                    fetch purline_cur into purline_rec ;
                    exit when not found ;
                    if mypid='' then 
                       mypid := purline_rec.pitem_origin_no ;
                       mypidno := purline_rec.pitem_origin_no ;
                    else 
                       if mypidno != purline_rec.pitem_origin_no then
                          mypid := concat(mypid,',',purline_rec.pitem_origin_no) ;
                          mypidno := purline_rec.pitem_origin_no ;
                       end if ;   
                    end if ;
                end loop ;
                close purline_cur ;    
                if substring(mypid,1,1)=',' then
                  mypid = substring(mypid,2,length(mypid)-1) ;
               end if ;
                update purchase_order set pidno=mypid,origin=mypid where id = pur_rec.id ;
              end loop ;
              close pur_cur ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpidno(purid int) cascade;""")
        self._cr.execute("""create or replace function getpidno(purid int) returns void as $BODY$
            DECLARE 
              purline_cur refcursor ;
              purline_rec record ;
              mypid varchar ;
              mypidno varchar ;
            BEGIN
                mypid := '' ;
                mypidno := '' ;
                open purline_cur for select pitem_origin_no,pitem_id from neweb_pitem_list
                    where pitem_id=purid order by pitem_origin_no ;
                loop
                    fetch purline_cur into purline_rec ;
                    exit when not found ;
                    if mypid='' then 
                       mypid := purline_rec.pitem_origin_no ;
                       mypidno := purline_rec.pitem_origin_no ;
                    else 
                       if mypidno != purline_rec.pitem_origin_no then
                          mypid := concat(mypid,',',purline_rec.pitem_origin_no) ;
                          mypidno := purline_rec.pitem_origin_no ;
                       end if ;   
                    end if ;
                end loop ;
                close purline_cur ;    
                update purchase_order set pidno=mypid where id = purid ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists purorderunlink(purid int) cascade;""")
        self._cr.execute("""create or replace function purorderunlink(purid int) returns void as $BODY$
               DECLARE 
                  pur_cur refcursor ;
                  pur_rec record ;
                  ncount int ;
               BEGIN 
                  open pur_cur for select * from neweb_pitem_list where pitem_id = purid ;
                  loop
                    fetch pur_cur into pur_rec;
                    exit when not found ;
                    if pur_rec.pitem_origin_type='P' then 
                       update neweb_projsaleitem set purchase_no=null,prod_purnum=prod_purnum - pur_rec.pitem_num,purchase_ok=FALSE 
                         where id = pur_rec.pitem_origin_id ;
                    end if ;     
                  end loop ;
                  close pur_cur ;
               END;$BODY$
               LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists reset_pitem_budget() cascade""")
        self._cr.execute("""create or replace function reset_pitem_budget() returns void as $BODY$
            DECLARE
               budget_cur refcursor ;
               budget_rec record ;
               ncount int ;
            BEGIN
               open budget_cur for select pitem_num,pitem_price,id from neweb_require_purchase_item where pitem_num > 0 and pitem_price > 0 ;
               loop
                  fetch budget_cur into budget_rec ;
                  exit when not found ;
                  update neweb_require_purchase_item set pitem_budget=(coalesce(budget_rec.pitem_num,0) * coalesce(budget_rec.pitem_price,0)) where 
                     id = budget_rec.id ;
               end loop ;
               close budget_cur ; 
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpitemseq(reqid int) cascade""")
        self._cr.execute("""create or replace function genpitemseq(reqid int) returns void as $BODY$
         DECLARE
           req_cur refcursor ;
           req_rec record ;
           nitem int ;
         BEGIN
           nitem = 1 ;
           open req_cur for select id from neweb_require_purchase_item where pitem_id=reqid order by pitem_nid,id;
           loop
             fetch req_cur into req_rec ;
             exit when not found ;
             update neweb_require_purchase_item set pitem_seq=nitem where id=req_rec.id ;
             nitem = nitem + 1 ;
           end loop ;
           close req_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallitemseq() cascade""")
        self._cr.execute("""create or replace function genallitemseq() returns void as $BODY$
          DECLARE
            preq_cur refcursor ;
            preq_rec record ;
          BEGIN
            open preq_cur for select id from neweb_require_purchase ;
            loop
               fetch preq_cur into preq_rec ;
               exit when not found ;
               execute genpitemseq(preq_rec.id) ;
            end loop ;
            close preq_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genflowman(rpid int) cascade""")
        self._cr.execute("""drop function if exists genrfqflowman(rpid int) cascade""")
        self._cr.execute("""create or replace function genrfqflowman(rpid int) returns void as $BODY$
          DECLARE
            resid int ;
            empid int ;
            userid int;
            flowman1 int ;
            flowman2 int ;
            flowman3 int ;
            flowman4 int ;
          BEGIN
            select emp_name into userid from neweb_require_purchase where id = rpid ; 
            select id into resid from resource_resource where user_id=userid ;
            if resid is not null then
               select id into empid from hr_employee where resource_id = resid ;
               if empid is not null then
                  update neweb_require_purchase set flow_owner=empid where id = rpid ;
                  select flow_man1,flow_man2,flow_man3,flow_man4 into flowman1,flowman2,flowman3,flowman4 from hr_employee_postype where emp_id=empid ;
                  if flowman1 is not null then
                     update neweb_require_purchase set flow_man1=flowman1,has_man1=1 where id = rpid ;
                  end if ;
                  if flowman2 is not null then
                     update neweb_require_purchase set flow_man2=flowman2,has_man2=1 where id = rpid ;
                  end if ;
                  if flowman3 is not null then
                     update neweb_require_purchase set flow_man3=flowman3,has_man3=1 where id = rpid ;
                  end if ;
                  if flowman4 is not null then
                     update neweb_require_purchase set flow_man4=flowman4,has_man4=1 where id = rpid ;
                  end if ;
               end if ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genplitem(poid int) cascade""")
        self._cr.execute("""create or replace function genplitem(poid int) returns void as $BODY$
         DECLARE
          po_cur refcursor ;
          po_rec record ;
          nitem int ;
         BEGIN
           nitem = 1 ;
           open po_cur for select id from neweb_pitem_list where pitem_id=poid order by sequence,id ;
           loop
             fetch po_cur into po_rec ;
             exit when not found ;
             update neweb_pitem_list set pitem_item=nitem where id = po_rec.id ;
             nitem = nitem + 1 ;
           end loop ;
           close po_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallplitem() cascade""")
        self._cr.execute("""create or replace function genallplitem() returns void as $BODY$
          DECLARE
            allpo_cur refcursor ;
            allpo_rec record ;
          BEGIN
            open allpo_cur for select id from purchase_order ;
            loop
              fetch allpo_cur into allpo_rec ;
              exit when not found ;
              execute genplitem(allpo_rec.id) ;
            end loop ;
            close allpo_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gendateorder() cascade""")
        self._cr.execute("""create or replace function gendateorder() returns void as $BODY$
         DECLARE
         BEGIN
           update purchase_order set date_order1=date_order + interval '8 hours'::DATE where date_order1 is null ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists gensmpurchaselineid() cascade""")
        self._cr.execute("""create or replace function gensmpurchaselineid() returns void as $BODY$
          DECLARE
            sm_cur refcursor ;
            sm_rec record ;
            po varchar ;
            poid int ;
            plineid int ;
          BEGIN
            open sm_cur for select id,picking_id,product_id,purchase_line_id from stock_move where purchase_line_id is null and 
               picking_id in (select id from stock_picking where picking_type_id=1) and product_id not in (1,2) ;
            loop
              fetch sm_cur into sm_rec ;
              exit when not found ;
              select origin into po from stock_picking where id = sm_rec.picking_id ;
              select id into poid from purchase_order where name=po ;
              select id into plineid from purchase_order_line where product_id=sm_rec.product_id and order_id=poid ;
              update stock_move set purchase_line_id=plineid where id = sm_rec.id ; 
            end loop ;
            close sm_cur ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        # (只改寫 供應商與單價)
        self._cr.execute("""DROP FUNCTION IF EXISTS purchase_change_price(purid int) cascade;""")
        self._cr.execute("""create or replace function purchase_change_price(purid int) returns void as $BODY$
         declare
           refpur refcursor ;
           refpurrow record ;
           projsaleitemid int ;
           mypurchaseno purchase_order.name%type ;
           mysuppliername res_partner.name%type;
           mycompsname res_partner.comp_sname%type;
           mysupplierid purchase_order.id%type;
           ncount INTEGER ;
           ncount1 INTEGER ;
           myprodnum neweb_projsaleitem.prod_num%type;
           myprodpurnum neweb_projsaleitem.prod_purnum%type;
           mystate purchase_order.state%type;
           myrate float ;
           mycurrencyid INTEGER ;
           projid INTEGER ;
           projid1 int ;
           myoriginno VARCHAR ;
           myorigintype CHAR ;
           myprodprice float ;
         begin
           open refpur for select * from neweb_pitem_list where pitem_origin_id is null and pitem_origin_no is not null and pitem_origin_type='P' ;
           loop
              fetch refpur into refpurrow ;
              exit when not found ;
              select id into projid1 from neweb_project where name=refpurrow.pitem_origin_no ;
              select max(id) into projsaleitemid from neweb_projsaleitem where saleitem_id=projid1 and prod_modeltype=refpurrow.pitem_model_type ;
              if projsaleitemid is not null then
                 update neweb_pitem_list set pitem_origin_id=projsaleitemid where id=refpurrow.id ;
              end if ;   
           end loop ;
           close refpur ;
           select pitem_origin_no,pitem_origin_type into myoriginno,myorigintype from neweb_pitem_list where pitem_id=purid ;
           select name,partner_id,state,currency_id into mypurchaseno,mysupplierid,mystate,mycurrencyid from purchase_order where id=purid ;
           select count(*) into ncount from res_currency_rate where currency_id=mycurrencyid ;
           if ncount > 0 THEN 
              select rate into myrate from res_currency_rate where currency_id=mycurrencyid and id=(select max(id) from res_currency_rate where currency_id=mycurrencyid) ;
           ELSE 
              myrate := 1 ;
           end if;
           select name,comp_sname into mysuppliername,mycompsname from res_partner where id=mysupplierid ;
           open refpur for select * from neweb_pitem_list where pitem_id=purid ;
           LOOP
             fetch refpur into refpurrow;
             exit when not found;
             myprodprice = refpurrow.pitem_price * round(1::numeric/myrate::numeric);
             if refpurrow.pitem_origin_type='R' then
               update neweb_require_purchase_item set purchase_no=mypurchaseno,supplier=mysupplierid,pitem_price=myprodprice,pitem_budget=(pitem_num * pitem_price) where id=refpurrow.pitem_origin_id ;
             else
               update neweb_projsaleitem set purchase_no=mypurchaseno,supplier=mysupplierid,prod_price=myprodprice where id=refpurrow.pitem_origin_id ;
             end if ;  
           END LOOP ;
           close refpur ;
           if myorigintype='P' THEN 
              select id into projid from neweb_project where name like myoriginno ;
              execute proj_rcal_cost(projid) ;
           END if;
         end;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chkpono(pono varchar) cascade""")
        self._cr.execute("""create or replace function chkpono(pono varchar) returns varchar as $BODY$
         DECLARE
           maxpo varchar ;
           prepono varchar ;
           maxcode varchar ;
           maxnum int ;
           ncount int ;
           myres varchar ;
         BEGIN
           select count(*) into ncount from purchase_order where name=pono ;
           if ncount >= 1 then
              select max(name) into maxpo from purchase_order where substring(name,1,8)=substring(pono,1,8);
              select substring(pono,1,8) into prepono ;
              select substring(maxpo,9,2) into maxcode ;
              maxnum = maxcode::int + 1 ;
              myres = concat(prepono,lpad(maxnum::TEXT,2,'0')) ;
              update ir_sequence set number_next=maxnum + 1 where code='purchase.order' ;
           else
              myres = pono ;   
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpuroriginid(purid int) cascade""")
        self._cr.execute("""create or replace function genpuroriginid(purid int) returns void as $BODY$
          DECLARE
            pur_cur refcursor ;
            pur_rec record ;
            cpidno varchar ;
            projid int ;
            saleitemid int ;
          BEGIN
            select pidno into cpidno from purchase_order where id = purid ;
            if length(cpidno)=12 then
               select id into projid from neweb_project where name = cpidno ;
               open pur_cur for select * from neweb_pitem_list where pitem_id=purid and pitem_origin_type='P' and pitem_origin_id is null ;
               loop
                  fetch pur_cur into pur_rec ;
                  exit when not found ;
                  select id into saleitemid from neweb_projsaleitem where saleitem_id=projid and prod_modeltype=pur_rec.pitem_model_type ;
                  if saleitemid is not null then
                     update neweb_pitem_list set pitem_origin_no=cpidno,pitem_origin_id=saleitemid where id = pur_rec.id ;
                  end if ;
               end loop ;
               close pur_cur ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genprojectpriceanalysis(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function genprojectpriceanalysis(sdate date,edate date) returns void as $BODY$
          DECLARE
            pj_cur refcursor ;
            pj_rec record ;
            sl_cur refcursor ;
            sl_rec record ;
          BEGIN
            delete from neweb_prod_price_list ;
            open pj_cur for select id,name,create_date from neweb_project where create_date::DATE <= edate::DATE and create_date::DATE >= sdate::DATE order by name ;
            loop
              fetch pj_cur into pj_rec ;
              exit when not found ;
              open sl_cur for select * from neweb_projsaleitem where saleitem_id = pj_rec.id order by line_item ;
              loop
                fetch sl_cur into sl_rec ;
                exit when not found ;
                insert into neweb_prod_price_list(proj_no,prod_set,prod_modeltype,prod_modeltype1,prod_serial,prod_no,prod_desc,prod_num,prod_origin_price,prod_price) values
                 (pj_rec.id,sl_rec.prod_set,sl_rec.prod_modeltype,sl_rec.prod_modeltype1,sl_rec.prod_serial,sl_rec.prod_no,sl_rec.prod_desc,sl_rec.prod_num,sl_rec.prod_origin_price,sl_rec.prod_price) ;
              end loop ;
              close sl_cur ;
            end loop ;
            close pj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_all_sp_proj_no() cascade""")
        self._cr.execute("""create or replace function gen_all_sp_proj_no() returns void as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update stock_picking set stockout_proj_no=substring(stockout_proj_no,2,length(stockout_proj_no)-1) where substring(stockout_proj_no,1,1)=',' ;
            update purchase_order set origin=substring(origin,2,length(origin)-1) where substring(origin,1,1)=',' ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genrpsdata1(rpno varchar) cascade""")
        self._cr.execute("""create or replace function genrpsdata1(rpno varchar) returns void as $BODY$
         DECLARE
           rps_cur refcursor ;
           rps_rec record ;
           ncount int ;
           rpnoid int ;
           rporiginno varchar ;
           ponum int ;
           pitemid int ;
           dateapprove date ;
           pitemid1 int ;
           stockinid int ;
           stockinnum int ;
           respartner int ;
           stockindate date ;
           maxid int ;
         BEGIN
           select count(*) into ncount from neweb_require_purchase where name like '%%'|| rpno ||'%%' ;
           if ncount > 0 then
              delete from neweb_rps_schedule ;
              open rps_cur for select A.id as rpid,A.pitem_id,A.prod_id as rppid,A.pitem_modeltype as rpmodeltype,A.pitem_desc as rppitemspec,A.pitem_num as rpnum,A.create_date::DATE as rpdate,
                A.pitem_budget as rpbudget from neweb_require_purchase_item A,neweb_require_purchase B where B.name ilike '%%'|| rpno ||'%%' and B.id = A.pitem_id order by A.pitem_id,A.id ;
               loop
                 fetch rps_cur into rps_rec ;
                 exit when not found ;
                 select id,name into rpnoid,rporiginno from neweb_require_purchase where id = rps_rec.pitem_id ;
                 select coalesce(pitem_num,0),pitem_id,id into ponum,pitemid,pitemid1 from neweb_pitem_list where pitem_origin_id=rps_rec.rpid and pitem_origin_no=rporiginno ; 
                 select date_approve::DATE into dateapprove from purchase_order where id = pitemid ;
                 insert into neweb_rps_schedule(rp_no,rp_modeltype,rp_pid,rp_pitemspec,rp_date,rp_num,rp_budget) values 
                  (rpnoid,rps_rec.rpmodeltype,rps_rec.rppid,rps_rec.rppitemspec,rps_rec.rpdate,rps_rec.rpnum,rps_rec.rpbudget) ;
                 select max(id) into maxid from  neweb_rps_schedule ;
                 if pitemid is not null then
                    select date_approve::DATE,partner_id into dateapprove,respartner from purchase_order where id = pitemid ;
                    update neweb_rps_schedule set po_partner=respartner,po_no=pitemid where id = maxid ;
                    if dateapprove is not null then
                       update neweb_rps_schedule set po_date=dateapprove,po_num=ponum where id = maxid ;
                    end if ;
                 end if ;
                 if pitemid1 is not null then
                   select stockin_num,stockin_id,create_date into stockinnum,stockinid,stockindate from neweb_stockin_list where stockin_sequence_id=pitemid1 ;
                   if stockinnum is not null then
                      update neweb_rps_schedule set stockin_no=stockinid,stockin_num=stockinnum,stockin_date=stockindate where id = maxid ;
                   end if ;
                 end if ;
               end loop ;
               close rps_cur ; 
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genrpsdata1emp(rpno varchar,empid int) cascade""")
        self._cr.execute("""create or replace function genrpsdata1emp(rpno varchar,empid int) returns void as $BODY$
         DECLARE
           rps_cur refcursor ;
           rps_rec record ;
           ncount int ;
           rpnoid int ;
           rporiginno varchar ;
           ponum int ;
           pitemid int ;
           dateapprove date ;
           pitemid1 int ;
           stockinid int ;
           stockinnum int ;
           respartner int ;
           stockindate date ;
           maxid int ;
         BEGIN
           select count(*) into ncount from neweb_require_purchase where name like '%%'|| rpno ||'%%' and  emp_name = empid ;
           if ncount > 0 then
              delete from neweb_rps_schedule ;
              open rps_cur for select A.id as rpid,A.pitem_id,A.prod_id as rppid,A.pitem_modeltype as rpmodeltype,A.pitem_desc as rppitemspec,A.pitem_num as rpnum,A.create_date::DATE as rpdate,
                A.pitem_budget as rpbudget from neweb_require_purchase_item A,neweb_require_purchase B where B.name ilike '%%'|| rpno ||'%%' and B.emp_name=empid and B.id = A.pitem_id order by A.pitem_id,A.id ;
               loop
                 fetch rps_cur into rps_rec ;
                 exit when not found ;
                 select id,name into rpnoid,rporiginno from neweb_require_purchase where id = rps_rec.pitem_id ;
                 select coalesce(pitem_num,0),pitem_id,id into ponum,pitemid,pitemid1 from neweb_pitem_list where pitem_origin_id=rps_rec.rpid and pitem_origin_no=rporiginno ; 
                 select date_approve::DATE into dateapprove from purchase_order where id = pitemid ;
                 insert into neweb_rps_schedule(rp_no,rp_modeltype,rp_pid,rp_pitemspec,rp_date,rp_num,rp_budget) values 
                  (rpnoid,rps_rec.rpmodeltype,rps_rec.rppid,rps_rec.rppitemspec,rps_rec.rpdate,rps_rec.rpnum,rps_rec.rpbudget) ;
                 select max(id) into maxid from  neweb_rps_schedule ;
                 if pitemid is not null then
                    select date_approve::DATE,partner_id into dateapprove,respartner from purchase_order where id = pitemid ;
                    update neweb_rps_schedule set po_partner=respartner,po_no=pitemid where id = maxid ;
                    if dateapprove is not null then
                       update neweb_rps_schedule set po_date=dateapprove,po_num=ponum where id = maxid ;
                    end if ;
                 end if ;
                 if pitemid1 is not null then
                   select stockin_num,stockin_id,create_date into stockinnum,stockinid,stockindate from neweb_stockin_list where stockin_sequence_id=pitemid1 ;
                   if stockinnum is not null then
                      update neweb_rps_schedule set stockin_no=stockinid,stockin_num=stockinnum,stockin_date=stockindate where id = maxid ;
                   end if ;
                 end if ;
               end loop ;
               close rps_cur ; 
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genrpsdata2(sdate date,edate date) cascade""")
        self._cr.execute("""create or replace function genrpsdata2(sdate date,edate date) returns void as $BODY$
         DECLARE
           rps_cur refcursor ;
           rps_rec record ;
           ncount int ;
           rpnoid int ;
           rporiginno varchar ;
           ponum int ;
           pitemid int ;
           dateapprove date ;
           pitemid1 int ;
           stockinid int ;
           stockinnum int ;
           respartner int ;
           stockindate date ;
           maxid int ;
         BEGIN
           select count(*) into ncount from neweb_require_purchase where create_date::DATE >= sdate::DATE and create_date::DATE <= edate::DATE ;
           if ncount > 0 then
               delete from neweb_rps_schedule ;
              open rps_cur for select A.id as rpid,A.pitem_id,A.prod_id as rppid,A.pitem_modeltype as rpmodeltype,A.pitem_desc as rppitemspec,A.pitem_num as rpnum,A.create_date::DATE as rpdate,
                A.pitem_budget as rpbudget from neweb_require_purchase_item A,neweb_require_purchase B where B.create_date::DATE >= sdate::DATE and B.create_date::DATE <= edate::DATE and B.id = A.pitem_id order by A.pitem_id,A.id ;
               loop
                 fetch rps_cur into rps_rec ;
                 exit when not found ;
                 select id,name into rpnoid,rporiginno from neweb_require_purchase where id = rps_rec.pitem_id ;
                 select coalesce(pitem_num,0),pitem_id,id into ponum,pitemid,pitemid1 from neweb_pitem_list where pitem_origin_id=rps_rec.rpid and pitem_origin_no=rporiginno ; 
                 select date_approve::DATE into dateapprove from purchase_order where id = pitemid ;
                 insert into neweb_rps_schedule(rp_no,rp_modeltype,rp_pid,rp_pitemspec,rp_date,rp_num,rp_budget) values 
                  (rpnoid,rps_rec.rpmodeltype,rps_rec.rppid,rps_rec.rppitemspec,rps_rec.rpdate,rps_rec.rpnum,rps_rec.rpbudget) ;
                 select max(id) into maxid from  neweb_rps_schedule ;
                 if pitemid is not null then
                    select date_approve::DATE,partner_id into dateapprove,respartner from purchase_order where id = pitemid ;
                    update neweb_rps_schedule set po_partner=respartner,po_no=pitemid where id = maxid ;
                    if dateapprove is not null then
                       update neweb_rps_schedule set po_date=dateapprove,po_num=ponum where id = maxid ;
                    end if ;
                 end if ;
                 if pitemid1 is not null then
                   select stockin_num,stockin_id,create_date into stockinnum,stockinid,stockindate from neweb_stockin_list where stockin_sequence_id=pitemid1 ;
                   if stockinnum is not null then
                      update neweb_rps_schedule set stockin_no=stockinid,stockin_num=stockinnum,stockin_date=stockindate where id = maxid ;
                   end if ;
                 end if ;
               end loop ;
               close rps_cur ;
           
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genrpsdata2emp(sdate date,edate date,empid int) cascade""")
        self._cr.execute("""create or replace function genrpsdata2emp(sdate date,edate date,empid int) returns void as $BODY$
         DECLARE
           rps_cur refcursor ;
           rps_rec record ;
           ncount int ;
           rpnoid int ;
           rporiginno varchar ;
           ponum int ;
           pitemid int ;
           dateapprove date ;
           pitemid1 int ;
           stockinid int ;
           stockinnum int ;
           respartner int ;
           stockindate date ;
           maxid int ;
         BEGIN
           select count(*) into ncount from neweb_require_purchase where create_date::DATE >= sdate::DATE and create_date::DATE <= edate::DATE and emp_name=empid ;
           if ncount > 0 then
               delete from neweb_rps_schedule ;
              open rps_cur for select A.id as rpid,A.pitem_id,A.prod_id as rppid,A.pitem_modeltype as rpmodeltype,A.pitem_desc as rppitemspec,A.pitem_num as rpnum,A.create_date::DATE as rpdate,
                A.pitem_budget as rpbudget from neweb_require_purchase_item A,neweb_require_purchase B where B.create_date::DATE >= sdate::DATE and B.create_date::DATE <= edate::DATE and B.emp_name=empid and B.id = A.pitem_id order by A.pitem_id,A.id ;
               loop
                 fetch rps_cur into rps_rec ;
                 exit when not found ;
                 select id,name into rpnoid,rporiginno from neweb_require_purchase where id = rps_rec.pitem_id ;
                 select coalesce(pitem_num,0),pitem_id,id into ponum,pitemid,pitemid1 from neweb_pitem_list where pitem_origin_id=rps_rec.rpid and pitem_origin_no=rporiginno ; 
                 select date_approve::DATE into dateapprove from purchase_order where id = pitemid ;
                 insert into neweb_rps_schedule(rp_no,rp_modeltype,rp_pid,rp_pitemspec,rp_date,rp_num,rp_budget) values 
                  (rpnoid,rps_rec.rpmodeltype,rps_rec.rppid,rps_rec.rppitemspec,rps_rec.rpdate,rps_rec.rpnum,rps_rec.rpbudget) ;
                 select max(id) into maxid from  neweb_rps_schedule ;
                 if pitemid is not null then
                    select date_approve::DATE,partner_id into dateapprove,respartner from purchase_order where id = pitemid ;
                    update neweb_rps_schedule set po_partner=respartner,po_no=pitemid where id = maxid ;
                    if dateapprove is not null then
                       update neweb_rps_schedule set po_date=dateapprove,po_num=ponum where id = maxid ;
                    end if ;
                 end if ;
                 if pitemid1 is not null then
                   select stockin_num,stockin_id,create_date into stockinnum,stockinid,stockindate from neweb_stockin_list where stockin_sequence_id=pitemid1 ;
                   if stockinnum is not null then
                      update neweb_rps_schedule set stockin_no=stockinid,stockin_num=stockinnum,stockin_date=stockindate where id = maxid ;
                   end if ;
                 end if ;
               end loop ;
               close rps_cur ;

           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")












