# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api


class newebstockinstoreproc(models.Model):
    _name = "neweb.stockinstoreproc"

    #  按照採購明細 產生一筆進貨記錄 store procedure
    @api.model
    def init(self):
        self._cr.execute(
            """DROP FUNCTION IF EXISTS genstockinline(pitemid int,stockinid int,prodid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function genstockinline(pitemid int,stockinid int,prodid int) returns void as $BODY$
declare
  refpitem_cur cursor is select * from neweb_pitem_list where id=pitemid order by id ;
  refpitem_row record ;
  unstockinnum neweb_pitem_list.pitem_num%type;
  sequenceid neweb_pitem_list.id%type;
  ncount integer;
  stockqc stock_picking.stockin_qc%type;
  mystockcheck neweb_stockin_list.stockin_check%type;
  mytoday stock_picking.create_date%type;
  mypitemorigintype varchar ;
  mypitemoriginno varchar ;
  mypitemoriginid int ;
  mystockindesc varchar ;
  mycusname int ;
  myitem int ;
  mymaxinid FLOAT;
  ncount1 int ;
begin
  select DATE 'now' into mytoday;
  select stockin_qc into stockqc from stock_picking where id=stockinid ;
  if stockqc = TRUE THEN
     mystockcheck = '2' ;
  else
     mystockcheck = '3' ;
  end if ;
  
  open refpitem_cur ;
  LOOP
    fetch refpitem_cur into refpitem_row ;
    exit when not found ;
    mystockindesc='-' ;
    if refpitem_row.pitem_origin_type = 'R' then 
       if refpitem_row.pur_memo is null then
          mystockindesc := '備品' ;
       else 
          mystockindesc := refpitem_row.pur_memo ;
       end if ;  
    else 
       select cus_name into mycusname from neweb_project where name=refpitem_row.pitem_origin_no ;
       select coalesce(comp_sname,'-') into mystockindesc from res_partner where id=mycusname ;
    end if ;
    unstockinnum := refpitem_row.pitem_num - refpitem_row.pitem_stockin_num ;
    select count(*) into ncount from neweb_stockin_list where stockin_id = stockinid ;
    if ncount > 0 then
       select coalesce(stockin_item,0) into myitem from neweb_stockin_list where 
                  id = (select max(id) from neweb_stockin_list where stockin_id = stockinid) ; 
       myitem := myitem + 1 ;  
    else 
       myitem := 1 ;
    end if ;  
    select count(*) into ncount1 from neweb_stockin_list where stockin_id = stockinid ;
    if ncount1 = 0 then 
       mymaxinid := 0 ;
    else 
       select round(max(stockin_item)) into mymaxinid from neweb_stockin_list where stockin_id = stockinid ;
    end if ;
    mymaxinid := mymaxinid + 1 ;
    insert into neweb_stockin_list(stockin_id,stockin_machinetype,stockin_modeltype,stockin_prodno,stockin_spec,stockin_num,stockin_num1,stockin_sequence_id,stockin_check,create_date,write_date,prod_id,stockin_desc,stockin_item) values
     (stockinid,refpitem_row.pitem_machine_type,refpitem_row.pitem_model_type,refpitem_row.pitem_prod_no,refpitem_row.pitem_spec,unstockinnum,unstockinnum,refpitem_row.id,mystockcheck,mytoday,mytoday,refpitem_row.prod_id,mystockindesc,mymaxinid);
  END LOOP;
  close refpitem_cur ;

end ;
$BODY$
LANGUAGE plpgsql ;""")

        self._cr.execute(
            """DROP FUNCTION IF EXISTS genpurstockcheck(stockid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function genpurstockcheck(stockid int,prodid int) returns void as $BODY$
declare
  refstockcur cursor is select distinct stockin_sequence_id from neweb_stockin_list where stockin_id=stockid ;
  refstockrow record;
  nstocknum neweb_pitem_list.pitem_stockin_num%type;
  ncount integer ;
  ncount1 integer ;
  refstockcur1 refcursor ;
  refstockrow1 record ;
  refstockcur2 refcursor ;
  refstockrow2 record ;
  nqtynum neweb_pitem_list.pitem_num%type;
  nstockinnum neweb_pitem_list.pitem_stockin_num%type;
  stockinqc stock_picking.stockin_qc%type;
  myorigin stock_picking.origin%type;
  mypitemid neweb_pitem_list.id%type;
begin
  select stockin_qc,origin into stockinqc,myorigin from stock_picking where id=stockid ;
  select id into mypitemid from purchase_order where name=myorigin ;
  update neweb_pitem_list set pitem_stockin_num=0 where pitem_id=mypitemid ;
  if stockinqc = TRUE THEN
     update neweb_stockin_list set stockin_check='2' where stockin_id=stockid and stockin_check != '3'and stockin_check != '1';
  end if ;
  open refstockcur ;
  loop
    fetch refstockcur into refstockrow ;
    exit when not found ;
    select sum(stockin_num) into nstocknum from neweb_stockin_list A where A.stockin_sequence_id=refstockrow.stockin_sequence_id;
    if nstocknum > 0 then
       update neweb_pitem_list set pitem_stockin_num=nstocknum where id=refstockrow.stockin_sequence_id;
   end if ;
  end loop;
  close refstockcur ;
  open refstockcur1 for select distinct stockin_sequence_id from neweb_stockin_list where stockin_id=stockid ;
  loop
     fetch refstockcur1 into refstockrow1 ;
     exit when not found ;
     select sum(stockin_num) into nstockinnum from neweb_stockin_list where stockin_sequence_id=refstockrow1.stockin_sequence_id ;
     update neweb_pitem_list set pitem_stockin_num=nstockinnum where id=refstockrow1.stockin_sequence_id ;
     select pitem_num into nqtynum from neweb_pitem_list where id=refstockrow1.stockin_sequence_id ;
     if nstockinnum = nqtynum then
        update neweb_pitem_list set pitem_stockin_complete = True where id=refstockrow1.stockin_sequence_id ;
     end if ;
  end loop;
  close refstockcur1 ;
  /* update stock_pack_operation set qty_done=1 where picking_id=stockid and product_id=prodid ; */
  open refstockcur2 for select * from neweb_stockin_list where stockin_id=stockid ;
  loop
    fetch refstockcur2 into refstockrow2;
    exit when not found;
    nqtynum := refstockrow2.stockin_num1 ;
    if refstockrow2.prod_id is not null then
      /* update stock_pack_operation set qty_done=nqtynum where picking_id=stockid and product_id=refstockrow2.prod_id; */
    end if;
  end loop;
  close refstockcur2;
  select count(*) into ncount from neweb_pitem_list where pitem_stockin_complete='FALSE' and pitem_id=stockid ;
  select count(*) into ncount1 from neweb_stockin_list where stockin_check='2' and stockin_id=stockid ;
  if ncount > 0 or ncount1 > 0 then
     update stock_picking set state='partially_available' where id=stockid  ;
  end if ;
end ;
$BODY$
LANGUAGE plpgsql ;""")



        self._cr.execute("""DROP FUNCTION IF EXISTS gencheckqc(pickid int) cascade;""")
        self._cr.execute("""create or replace function gencheckqc(pickid int) returns void as $BODY$
declare
  ncount integer;
  mystockpickid stock_picking.id%type;
  mystockinseqid neweb_stockin_list.id%type;
  myorigintype neweb_pitem_list.pitem_origin_type%type;
  myoriginid neweb_pitem_list.pitem_origin_id%type;
  mystockinserial neweb_stockin_list.stockin_serial%type;
  myprodserial neweb_projsaleitem.prod_serial%type;
  refqccur refcursor;
  refqcrec record;
begin
  select count(*) into ncount from neweb_stockin_list where stockin_id=pickid and stockin_check='2' ;
  if ncount > 0 then
     update stock_picking set state='partially_available',stockin_checkyn=False where id=pickid ;
    /* update stock_pack_operation set qty_done=0 where picking_id=pickid ;*/
  else
     update stock_picking set stockin_checkyn=TRUE,stockin_qc_status='2' where id=pickid ;
  end if ;
  open refqccur for select * from neweb_stockin_list where stockin_id=pickid;
  loop
     fetch refqccur into refqcrec;
     exit when not found;
     select pitem_origin_type into myorigintype from neweb_pitem_list where id=refqcrec.stockin_sequence_id;
     if myorigintype='P' then
        select pitem_origin_id into myoriginid from neweb_pitem_list where id=refqcrec.stockin_sequence_id;  
        select prod_serial into myprodserial from neweb_projsaleitem where id=myoriginid ;
        if myprodserial is null then
           update neweb_projsaleitem set prod_serial=refqcrec.stockin_serial where id=myoriginid and prod_serial is null; 
        end if;
     end if;
  end loop;
  close refqccur;
end;
$BODY$
LANGUAGE plpgsql;""")


        self._cr.execute("""DROP FUNCTION IF EXISTS genstockoutline(sitemid int,stockoutid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function genstockoutline(sitemid int,stockoutid int,prodid int) returns void as $BODY$
        declare
          refsitem_cur cursor is select * from neweb_sitem_list where id=sitemid order by sitem_item ;
          refsitem_row record ;
          unstockoutnum neweb_sitem_list.sitem_num%type;
          sequenceid neweb_sitem_list.id%type;
          ncount integer;
          mytoday stock_picking.create_date%type;
          myname neweb_prodbrand.name%type;
          myitem int ;
          ncount1 int ;
        begin
          select DATE 'now' into mytoday;
          open refsitem_cur ;
          LOOP
            fetch refsitem_cur into refsitem_row ;
            exit when not found ;
            unstockoutnum := refsitem_row.sitem_num - refsitem_row.sitem_stockout_num ;
            select name into myname from neweb_prodbrand where id=refsitem_row.sitem_brand;
            insert into neweb_stockout_list(stockout_id,stockout_machinetype,stockout_modeltype,stockout_spec,stockout_num,stockout_price,stockout_sequence_id,create_date,write_date) values
             (stockoutid,myname,refsitem_row.sitem_modeltype,refsitem_row.sitem_desc,unstockoutnum,refsitem_row.sitem_price,refsitem_row.id,mytoday,mytoday);
             select count(*) into ncount from neweb_stockship_list where stockship_id = stockoutid ;
             if ncount > 0 then
                 select coalesce(stockship_item,0) into myitem from neweb_stockship_list where 
                      id = (select max(id) from neweb_stockship_list where stockship_id = stockoutid) ; 
                myitem := myitem + 1 ;   
             else 
                myitem := 1 ;
             end if ;   
            insert into neweb_stockship_list(stockship_id,stockship_machinetype,stockship_modeltype,stockship_spec,stockship_num,stockship_price,create_date,write_date,stockout_sequence_id,stockship_item) values
             (stockoutid,myname,refsitem_row.sitem_modeltype,refsitem_row.sitem_desc,unstockoutnum,refsitem_row.sitem_price,mytoday,mytoday,refsitem_row.id,myitem);
          END LOOP;
          close refsitem_cur ;
           EXECUTE gensalestockcheck(stockoutid,prodid);
        end ;
        $BODY$
        LANGUAGE plpgsql ;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS genstockoutline1(sitemid int,stockoutid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function genstockoutline1(sitemid int,stockoutid int,prodid int) returns void as $BODY$
        declare
          refsitem_cur cursor is select * from neweb_projsaleitem where id=sitemid order by line_item ;
          refsitem_row record ;
          unstockoutnum neweb_projsaleitem.prod_num%type;
          sequenceid neweb_projsaleitem.id%type;
          ncount integer;
          mytoday stock_picking.create_date%type;
          myname neweb_prodbrand.name%type;
          myitem int ;
          ncount1 int ;
          mymaxshipid FLOAT ;
          ncount3 int ;
        begin
          select DATE 'now' into mytoday;
          open refsitem_cur ;
          LOOP
            fetch refsitem_cur into refsitem_row ;
            exit when not found ;
            if refsitem_row.prod_stockoutnum is null then 
               unstockoutnum := refsitem_row.prod_num ;
            else 
               unstockoutnum := refsitem_row.prod_num - refsitem_row.prod_stockoutnum ;
            end if ;
            select name into myname from neweb_prodbrand where id=refsitem_row.prod_brand;
            insert into neweb_stockout_list(stockout_id,stockout_machinetype,stockout_modeltype,stockout_spec,stockout_num,stockout_price,stockout_sequence_id,create_date,write_date,line_item) values
             (stockoutid,myname,refsitem_row.prod_modeltype,refsitem_row.prod_desc,unstockoutnum,refsitem_row.prod_price,refsitem_row.id,mytoday,mytoday,refsitem_row.line_item);
            select count(*) into ncount from neweb_stockship_list where stockship_id = stockoutid ;
            if ncount > 0 then
               select coalesce(stockship_item,0) into myitem from neweb_stockship_list where 
                   id = (select max(id) from neweb_stockship_list where stockship_id = stockoutid) ; 
               myitem := myitem + 1 ;   
            else 
               myitem := 1 ;
            end if ;   
            select count(*) into ncount3 from neweb_stockship_list where stockship_id = stockoutid ;
            if ncount3 = 0 then 
               mymaxshipid := 0 ;
            else 
               select round(max(stockship_item)) into mymaxshipid from neweb_stockship_list where stockship_id = stockoutid ;
            end if ;
            mymaxshipid := mymaxshipid + 1 ;
            insert into neweb_stockship_list(stockship_id,stockship_machinetype,stockship_modeltype,stockship_spec,stockship_num,stockship_price,create_date,write_date,stockout_sequence_id,stockship_item,line_item) values
             (stockoutid,myname,refsitem_row.prod_modeltype,refsitem_row.prod_desc,unstockoutnum,refsitem_row.prod_price,mytoday,mytoday,refsitem_row.id,mymaxshipid,refsitem_row.line_item);
          END LOOP;
          close refsitem_cur ;
           EXECUTE gensalestockcheck1(stockoutid,prodid);
        end ;
        $BODY$
        LANGUAGE plpgsql ;""")



        self._cr.execute("""DROP FUNCTION IF EXISTS gensalestockcheck(stockid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function gensalestockcheck(stockid int,prodid int) returns void as $BODY$
        declare
          refstockcur cursor is select distinct stockout_sequence_id from neweb_stockout_list where stockout_id=stockid ;
          refstockrow record;
          nstocknum neweb_sitem_list.sitem_stockout_num%type;
          ncount integer ;
          ncount1 integer ;
          refstockcur1 refcursor ;
          refstockrow1 record ;
          nqtynum neweb_sitem_list.sitem_num%type;
          nstockoutnum neweb_sitem_list.sitem_stockout_num%type;
          myorigin stock_picking.origin%type;
          mysitemid neweb_sitem_list.id%type;
        begin
          select origin into myorigin from stock_picking where id=stockid ;
          select id into mysitemid from sale_order where name=myorigin ;
         
          open refstockcur ;
          loop
            fetch refstockcur into refstockrow ;
            exit when not found ;
            select sum(stockout_num) into nstocknum from neweb_stockout_list A where A.stockout_sequence_id=refstockrow.stockout_sequence_id;
            if nstocknum > 0 then
               update neweb_sitem_list set sitem_stockout_num=nstocknum where id=refstockrow.stockout_sequence_id ;
           end if ;
          end loop;
          close refstockcur ;
          open refstockcur1 for select distinct stockout_sequence_id from neweb_stockout_list where stockout_id=stockid ;
          loop
             fetch refstockcur1 into refstockrow1 ;
             exit when not found ;
             select sum(stockout_num) into nstockoutnum from neweb_stockout_list where stockout_sequence_id=refstockrow1.stockout_sequence_id ;
             update neweb_sitem_list set sitem_stockout_num=nstockoutnum where id=refstockrow1.stockout_sequence_id ;
             select sitem_num into nqtynum from neweb_sitem_list where id=refstockrow1.stockout_sequence_id ;
             if nstockoutnum = nqtynum then
                update neweb_sitem_list set sitem_stockout_complete = True where id=refstockrow1.stockout_sequence_id ;
             end if ;
          end loop;
          close refstockcur1 ;
          select count(*) into ncount from neweb_sitem_list where sitem_stockout_complete='FALSE' and sitem_id=stockid ;
          if ncount=0  then
             /* update stock_pack_operation set qty_done=1,product_qty=1 where picking_id=stockid and product_id=prodid ; */
          else
             /* update stock_pack_operation set qty_done=0,product_qty=1 where picking_id=stockid and product_id=prodid;*/
             update stock_picking set state='partially_available' where id=stockid ;
          end if ;
        end ;
        $BODY$
        LANGUAGE plpgsql ;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS gensalestockcheck1(stockid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function gensalestockcheck1(stockid int,prodid int) returns void as $BODY$
                declare
                  refstockcur cursor is select distinct stockout_sequence_id from neweb_stockout_list where stockout_id=stockid ;
                  refstockrow record;
                  nstocknum neweb_projsaleitem.prod_stockoutnum%type;
                  ncount integer ;
                  ncount1 integer ;
                  refstockcur1 refcursor ;
                  refstockrow1 record ;
                  nqtynum neweb_projsaleitem.prod_num%type;
                  nstockoutnum neweb_projsaleitem.prod_stockoutnum%type;
                  myorigin stock_picking.origin%type;
                  mysitemid neweb_sitem_list.id%type;
                begin
                  select origin into myorigin from stock_picking where id=stockid ;
                  select id into mysitemid from sale_order where name=myorigin ;

                  open refstockcur ;
                  loop
                    fetch refstockcur into refstockrow ;
                    exit when not found ;
                    select sum(stockout_num) into nstocknum from neweb_stockout_list A where A.stockout_sequence_id=refstockrow.stockout_sequence_id;
                    if nstocknum > 0 then
                       update neweb_projsaleitem set prod_stockoutnum=nstocknum where id=refstockrow.stockout_sequence_id ;
                   end if ;
                  end loop;
                  close refstockcur ;
                  open refstockcur1 for select distinct stockout_sequence_id from neweb_stockout_list where stockout_id=stockid ;
                  loop
                     fetch refstockcur1 into refstockrow1 ;
                     exit when not found ;
                     select sum(stockout_num) into nstockoutnum from neweb_stockout_list where stockout_sequence_id=refstockrow1.stockout_sequence_id ;
                     update neweb_projsaleitem set prod_stockoutnum=nstockoutnum where id=refstockrow1.stockout_sequence_id ;
                     select prod_num into nqtynum from neweb_projsaleitem where id=refstockrow1.stockout_sequence_id ;
                     if nstockoutnum = nqtynum then
                        update neweb_projsaleitem set prod_stockout_complete = True where id=refstockrow1.stockout_sequence_id ;
                     end if ;
                  end loop;
                  close refstockcur1 ;
                  select count(*) into ncount from neweb_projsaleitem where prod_stockout_complete='FALSE' and saleitem_id=stockid ;
                  if ncount=0  then
                    /* update stock_pack_operation set qty_done=1,product_qty=1 where picking_id=stockid and product_id=prodid ; */
                  else
                    /* update stock_pack_operation set qty_done=0,product_qty=1 where picking_id=stockid and product_id=prodid; */
                     update stock_picking set state='partially_available' where id=stockid ;
                  end if ;
                end ;
                $BODY$
                LANGUAGE plpgsql ;""")



        self._cr.execute(
                """DROP FUNCTION IF EXISTS genstockdsline(pitemid int,stockinid int,prodid int) cascade;""")
        self._cr.execute("""create or replace function genstockdsline(pitemid int,stockinid int,prodid int) returns void as $BODY$
        declare
          refpitem_cur cursor is select * from neweb_pitem_list where id=pitemid ;
          refpitem_row record ;
          unstockinnum neweb_pitem_list.pitem_num%type;
          sequenceid neweb_pitem_list.id%type;
          ncount integer;
          stockqc stock_picking.stockin_qc%type;
          mystockcheck neweb_stockin_list.stockin_check%type;
          mytoday stock_picking.create_date%type;
          myorigintype neweb_pitem_list.pitem_origin_type%type;
          myoriginid neweb_pitem_list.pitem_origin_id%type;
          myname neweb_prodset.name%type;
          myprodsetid neweb_prodset.id%type;
          mymodeltype neweb_projsaleitem.prod_modeltype%type;
          myprodno neweb_projsaleitem.prod_no%type;
          myproddesc neweb_projsaleitem.prod_desc%type;
          myprodnum neweb_projsaleitem.prod_num%type;
          myprodprice neweb_projsaleitem.prod_price%type;
          myprodserial neweb_projsaleitem.prod_serial%type;
          myid neweb_projsaleitem.id%type;
          myitem int ;
          myitem1 int ;
          ncount1 int ;
        begin
          select DATE 'now' into mytoday;
          select stockin_qc into stockqc from stock_picking where id=stockinid ;
          if stockqc = TRUE THEN
             mystockcheck = '2' ;
          else
             mystockcheck = '3' ;
          end if ;
          open refpitem_cur ;
          LOOP
            fetch refpitem_cur into refpitem_row ;
            exit when not found ;
            unstockinnum := refpitem_row.pitem_num - refpitem_row.pitem_stockin_num ;
            select count(*) into ncount from neweb_stockin_list where stockin_id = stockinid ;
            if ncount > 0 then
               select coalesce(stockin_item,0) into myitem from neweb_stockin_list where 
                  id = (select max(id) from neweb_stockin_list where stockin_id = stockinid) ; 
               myitem := myitem + 1 ;     
            else 
               myitem := 1 ;   
            end if ;   
            insert into neweb_stockin_list(stockin_id,stockin_machinetype,stockin_modeltype,stockin_prodno,stockin_spec,stockin_num,stockin_num1,stockin_sequence_id,stockin_check,create_date,write_date,stockin_item) values
             (stockinid,refpitem_row.pitem_machine_type,refpitem_row.pitem_model_type,refpitem_row.pitem_prod_no,refpitem_row.pitem_spec,unstockinnum,unstockinnum,refpitem_row.id,mystockcheck,mytoday,mytoday,myitem);
            
            if refpitem_row.pitem_origin_type='P' then
                myoriginid := refpitem_row.pitem_origin_id;
                select prod_set,prod_modeltype,prod_serial,prod_no,prod_desc,prod_num,prod_price,id into
                    myprodsetid,mymodeltype,myprodserial,myprodno,myproddesc,myprodnum,myprodprice,myid from
                       neweb_projsaleitem where id = refpitem_row.pitem_origin_id;
                select name into myname from neweb_prodset where id=myprodsetid ;
                insert into neweb_stockout_list(stockout_id,stockout_machinetype,stockout_modeltype,stockout_spec,stockout_num,stockout_price,stockout_sequence_id,create_date,write_date,stockout_desc) values
                  (stockinid,myname,mymodeltype,myproddesc,unstockinnum,myprodprice,myid,mytoday,mytoday,myprodserial);
                  
                select count(*) into ncount from neweb_stockship_list where stockship_id = stockinid ;
                if ncount > 0 then
                   select coalesce(stockship_item,0) into myitem1 from neweb_stockship_list where 
                      id = (select max(id) from neweb_stockship_list where stockship_id = stockinid) ;     
                   myitem1 := myitem1 + 1 ;   
                else 
                   myitem1 := 1 ;
                end if ;       
                insert into neweb_stockship_list(stockship_id,stockship_machinetype,stockship_modeltype,stockship_spec,stockship_num,stockship_price,create_date,write_date,stockship_desc,stockout_sequence_id,stockship_item) values
                  (stockinid,myname,mymodeltype,myproddesc,unstockinnum,myprodprice,mytoday,mytoday,myprodserial,myid,myitem1);
                 
            end if;
          END LOOP;
          close refpitem_cur ;
          EXECUTE genpurstockcheck(stockinid,prodid);
        end ;
        $BODY$
        LANGUAGE plpgsql ;""")

        self._cr.execute(
            """DROP FUNCTION IF EXISTS qcwritepitem(pitemid int,stockinnum float) cascade;""")
        self._cr.execute("""create or replace function qcwritepitem(pitemid int,stockinnum float) returns void as $BODY$
                BEGIN
                  update neweb_pitem_list set pitem_stockin_num=stockinnum,pitem_stockin_complete=False where id=pitemid;
                end;
                $BODY$
                LANGUAGE plpgsql ;""")


        self._cr.execute("""drop function if exists checkbackorder(stockinid int) cascade;""")
        self._cr.execute("""create or replace function checkbackorder(stockinid int) returns void as $BODY$
               declare
                  refstockincur refcursor;
                  refstockinrow record;
                  mybackorderid stock_picking.backorder_id%type;
               BEGIN
                  open refstockincur for select * from neweb_stockin_list where stockin_id=stockinid and stockin_num is null;
                  loop
                    fetch refstockincur into refstockinrow;
                    exit when not found ;
                    select backorder_id into mybackorderid from stock_picking where id=stockinid;
                    if mybackorderid is not null then
                       delete from neweb_stockin_list where id=refstockinrow.id ;
                      /*  update stock_pack_operation set qty_done=0 where picking_id=stockinid; */
                    end if;
                  end loop;
                  close refstockincur;
               end;
               $BODY$
               LANGUAGE plpgsql;
                   """)

        self._cr.execute("""drop function if exists updatepurchasenum(myorigin stock_picking.origin%type) cascade;""")
        self._cr.execute("""create or replace function updatepurchasenum(myorigin stock_picking.origin%type) returns void as $BODY$
              DECLARE
                refpurchasecur refcursor;
                refpurchaserow record;
                mypitemid neweb_pitem_list.pitem_id%type;
                ncount INTEGER ;
                ncount1 INTEGER ;
              begin
                select id into mypitemid from purchase_order where name=myorigin;
                update neweb_pitem_list set pitem_stockin_num=0 where pitem_id=mypitemid;
                open refpurchasecur for select * from neweb_stockin_list where stockin_sequence_id
                     in (select id from neweb_pitem_list where pitem_id=mypitemid) ;
                loop
                  fetch refpurchasecur into refpurchaserow;
                  exit when not found;
                  update neweb_pitem_list set pitem_stockin_num=pitem_stockin_num+refpurchaserow.stockin_num1
                        where id=refpurchaserow.stockin_sequence_id;
                end loop;
                close refpurchasecur;
                update neweb_pitem_list set pitem_stockin_complete=TRUE where pitem_stockin_num=pitem_num
                      and pitem_id=mypitemid;
                select count(*) into ncount from neweb_pitem_list where pitem_stockin_num=pitem_num and pitem_id=mypitemid;
                select count(*) into ncount1 from neweb_pitem_list where pitem_id=mypitemid;
                if ncount = ncount1 then

                else
                end if;
              end;$BODY$
              LANGUAGE plpgsql;
                """)


        self._cr.execute("""drop function if exists updateqcman(stockinid int,qcmanid int) cascade;""")
        self._cr.execute("""create or replace function updateqcman(stockinid int,qcmanid int) returns void as $BODY$
                      DECLARE
                         ncount INTEGER ;
                      BEGIN
                         select count(*) into ncount from stockpicking_resusers_rel where picking_id=stockinid and users_id=qcmanid ;
                         if ncount = 0 then
                           insert into stockpicking_resusers_rel(picking_id,users_id) values (stockinid,qcmanid) ;
                         end if;
                      end ;$BODY$
                      LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists updateinventoryline(invid int,locid int,prodid int,prodqty int) cascade;""")
        self._cr.execute("""create or replace function updateinventoryline(invid int,locid int,prodid int,prodqty int) returns void as $BODY$
         DECLARE 
            ncount int;
            locname VARCHAR ;
            prodcode VARCHAR ;
            prodname VARCHAR ;
            curtime TIMESTAMP ;
            produomid int;
         BEGIN 
            curtime := now();
            select count(*) into ncount from stock_inventory_line where inventory_id=invid and location_id=locid and product_id=prodid ;
            if ncount = 0 THEN 
               select name into locname from stock_location where id=locid;
               select default_code,name,uom_id into prodcode,prodname,produomid from product_template where id=prodid;
               insert into stock_inventory_line (inventory_id,location_id,product_id,product_uom_id,location_name,product_code,product_name,product_qty,create_date,write_date,create_uid,write_uid) values
                (invid,locid,prodid,produomid,locname,prodcode,prodname,prodqty,curtime,curtime,1,1);
            ELSE 
               update stock_inventory_line set product_qty=prodqty where inventory_id=invid and location_id=locid and product_id=prodid ;
            end if;
         END ; $BODY$
         LANGUAGE plpgsql; """)


        self._cr.execute("""drop function if exists getstockquantqty(prodid int,locid int) cascade;""")
        self._cr.execute("""create or replace function getstockquantqty(prodid int,locid int) returns INTEGER as $BODY$
             DECLARE 
                nqty int = 0 ;
             BEGIN 
                select sum(qty) into nqty from stock_quant where product_id=prodid and location_id=locid ;
                if nqty is null THEN 
                   nqty := 0 ;
                end if ;
                return nqty;
             END;$BODY$
             LANGUAGE plpgsql;    """)

        self._cr.execute("""drop function if exists unlinkstockoutlist(stockshiplistid int) cascade;""")
        self._cr.execute("""create or replace function unlinkstockoutlist(stockshiplistid int) returns void as $BODY$
             DECLARE 
               ncount int ;
               stockpickingid int ;
               sitemid int ;
               stockoutnum FLOAT;
               stockshipspec varchar ;
               
             BEGIN 
               select stockout_sequence_id into sitemid from neweb_stockship_list where id = stockshiplistid ;
               if sitemid is null  then 
                   select stockship_id into stockpickingid from neweb_stockship_list where id = stockshiplistid ;
                   select count(*) into ncount from neweb_stockout_list where stockout_id=stockpickingid and 
                          stockout_spec like (select stockship_spec from neweb_stockship_list where id = stockshiplistid ) ;
                   if ncount > 0 then 
                      select stockship_num into stockoutnum from neweb_stockship_list where id = stockshiplistid ;
                      select stockout_sequence_id into sitemid from neweb_stockout_list where stockout_id=stockpickingid and 
                          stockout_spec like (select stockship_spec from neweb_stockship_list where id = stockshiplistid ) ;
                      update neweb_sitem_list set sitem_stockout_num = sitem_stockout_num - stockoutnum,sitem_stockout_complete = False   
                          where id = sitemid ;  
                   end if ;      
               else 
                    select stockship_num into stockoutnum from neweb_stockship_list where id = stockshiplistid ;
                    update neweb_sitem_list set sitem_stockout_num = sitem_stockout_num - stockoutnum,sitem_stockout_complete = False   
                          where id = sitemid ;  
               end if ;   
               
             END ;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists unlinkstockoutlist1(stockshiplistid int) cascade;""")
        self._cr.execute("""create or replace function unlinkstockoutlist1(stockshiplistid int) returns void as $BODY$
            DECLARE 
              ncount int ;
              stockpickingid int ;
              sitemid int ;
              stockoutnum FLOAT;
              stockshipspec varchar ;
            BEGIN 
              select stockout_sequence_id into sitemid from neweb_stockship_list where id = stockshiplistid ;
              if sitemid is null  then 
                  select stockship_id into stockpickingid from neweb_stockship_list where id = stockshiplistid ;
                  select count(*) into ncount from neweb_stockout_list where stockout_id=stockpickingid and 
                         stockout_spec like (select stockship_spec from neweb_stockship_list where id = stockshiplistid ) ;
                  if ncount > 0 then 
                     select stockship_num into stockoutnum from neweb_stockship_list where id = stockshiplistid ;
                     select stockout_sequence_id into sitemid from neweb_stockout_list where stockout_id=stockpickingid and 
                         stockout_spec like (select stockship_spec from neweb_stockship_list where id = stockshiplistid ) ;
                     update neweb_projsaleitem set prod_stockoutnum = prod_stockoutnum - stockoutnum,prod_stockout_complete = False   
                         where id = sitemid ;  
                  end if ;      
              else 
                   select stockship_num into stockoutnum from neweb_stockship_list where id = stockshiplistid ;
                   update neweb_projsaleitem set prod_stockoutnum = prod_stockoutnum - stockoutnum,prod_stockout_complete = False   
                         where id = sitemid ;  
              end if ;  
              update neweb_projsaleitem set prod_stockoutnum=0 where prod_stockoutnum < 0 and id = sitemid ; 
              select stockship_id into stockpickingid from neweb_stockship_list where id = stockshiplistid ;
              delete from neweb_stockout_list where stockout_sequence_id = sitemid and stockout_id = stockpickingid ; 
            END ;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists unlinkstockoutlist2(stockoutlistid int) cascade;""")
        self._cr.execute("""create or replace function unlinkstockoutlist2(stockoutlistid int) returns void as $BODY$
            DECLARE 
              ncount int ;
              stockpickingid int ;
              sitemid int ;
              stockoutnum FLOAT;
              stockshipspec varchar ;
            BEGIN 
              select stockout_sequence_id into sitemid from neweb_stockout_list where id = stockoutlistid ;
              select stockout_num into stockoutnum from neweb_stockout_list where id = stockoutlistid ;
              update neweb_projsaleitem set prod_stockoutnum = coalesce(prod_stockoutnum,0) - coalesce(stockoutnum,0),prod_stockout_complete = False   
                     where id = sitemid ;  
              update neweb_projsaleitem set prod_stockoutnum=0 where prod_stockoutnum < 0 and id = sitemid ; 
            END ;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_stockout_origin(pickingid int) cascade;""")
        self._cr.execute("""create or replace function check_stockout_origin(pickingid int) returns void as $BODY$
             DECLARE
               ncount int;
               purchaseno varchar;
               projno varchar ;
               scheduleddt timestamp ;
             BEGIN
               select origin,scheduled_date into purchaseno,scheduleddt from stock_picking where id=pickingid ;
               select count(*) into ncount from purchase_order where name like purchaseno ;
               if ncount > 0 then 
                  select origin into projno from purchase_order where name like purchaseno ;
                  if projno is not null then 
                     update stock_picking set stockout_proj_no=projno where id=pickingid ;
                  end if ;
               end if ;
               if scheduleddt is not null then
                  update stock_picking set scheduled_date1=(scheduleddt + interval '8 hours')::DATE where id = pickingid ;
               end if ;
             END;$BODY$
             LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists check_all_stockout_origin() cascade;""")
        self._cr.execute("""create or replace function check_all_stockout_origin() returns void as $BODY$
         DECLARE
           ncount int;
           stock_cur refcursor ;
           stock_rec record ;
           purchaseno varchar;
           projno varchar ;
         BEGIN
           open stock_cur for select * from stock_picking ;
           loop
             fetch stock_cur into stock_rec ;
             exit when not found ;
             
             select count(*) into ncount from purchase_order where name like stock_rec.origin ;
             if ncount > 0 then 
               select origin into projno from purchase_order where name like stock_rec.origin ;
               if projno is not null then 
                 update stock_picking set stockout_proj_no=projno where id = stock_rec.id ;
               end if ;
             end if ;
           end loop ;
           close stock_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists unlinkstockinlist(stockinlistid int) cascade""")
        self._cr.execute("""create or replace function unlinkstockinlist(stockinlistid int) returns void as $BODY$
            DECLARE 
            pitemid int ;
            stockinnum float;
            BEGIN 
              select stockin_sequence_id,stockin_num into pitemid,stockinnum from neweb_stockin_list where id = stockinlistid ;
              update neweb_pitem_list set pitem_stockin_num=pitem_stockin_num - stockinnum,
                     pitem_stockin_complete=FALSE where id=pitemid ;
              
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setstockitem(stockid int) cascade;""")
        self._cr.execute("""create or replace function setstockitem(stockid int) returns void as $BODY$
        DECLARE 
          ncount int;
          stock_cur refcursor ;
          stock_rec record ;
          myitem int ;
        BEGIN
          /*select count(*) into ncount from neweb_stockin_list where stockin_id = stockid ;
          if ncount > 0 then */
             myitem := 1 ; 
             open stock_cur for select id from neweb_stockin_list where stockin_id = stockid order by stockin_item ;
             loop
               fetch stock_cur into stock_rec ;
               exit when not found ;
               update neweb_stockin_list set stockin_item=myitem where id = stock_rec.id ;
               myitem = myitem + 1 ;
             end loop ;
             close stock_cur ;
         /* else */
             myitem := 1 ; 
             open stock_cur for select id from neweb_stockship_list where stockship_id = stockid order by stockship_item ;
             loop
               fetch stock_cur into stock_rec ;
               exit when not found ;
               update neweb_stockship_list set stockship_item=myitem where id = stock_rec.id ;
               myitem = myitem + 1 ;
             end loop ;
             close stock_cur ;
          /*end if ;*/
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists setallitem() cascade;""")
        self._cr.execute("""create or replace function setallitem() returns void as $BODY$
        DECLARE 
          ncount int ;
          stock_cur refcursor ;
          stock_rec record ;
          line_cur refcursor ;
          line_rec record ;
          myitem int ;
        BEGIN 
          open stock_cur for select id from stock_picking where picking_type_id in
            (select id from stock_picking_type where code = 'incoming') ;
          loop
            fetch stock_cur into stock_rec ;
            exit when not found ;
            myitem := 1 ;
            open line_cur for select id from neweb_stockin_list where stockin_id = stock_rec.id ;
            loop
              fetch line_cur into line_rec ;
              exit when not found ;
              update neweb_stockin_list set stockin_item=myitem where id = line_rec.id ;
              myitem := myitem + 1 ;
            end loop ;
            close line_cur ;
          end loop ;
          close stock_cur ;  
          open stock_cur for select id from stock_picking where picking_type_id in
            (select id from stock_picking_type where code = 'outgoing') ;
          loop
            fetch stock_cur into stock_rec ;
            exit when not found ;
            myitem := 1 ;
            open line_cur for select id from neweb_stockship_list where stockship_id = stock_rec.id order by sequence ;
            loop
              fetch line_cur into line_rec ;
              exit when not found ;
              update neweb_stockship_list set stockship_item=myitem where id = line_rec.id ;
              myitem := myitem + 1 ;
            end loop ;
            close line_cur ;
          end loop ;
          close stock_cur ;  
            
        END;$BODY$
        LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists getstockinpono(pitemid int) cascade""")
        self._cr.execute("""create or replace function getstockinpono(pitemid int) returns varchar as $BODY$
            DECLARE 
              myres varchar ;
              purid int ;
              ncount int ;
            BEGIN
              select count(*) into ncount from neweb_pitem_list where id = pitemid ;
              if ncount > 0 then 
                 select coalesce(pitem_origin_no,' ') into myres from neweb_pitem_list 
                      where id = pitemid ;
              else 
                 myres = ' ' ;       
              end if ;
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists allpickoutaddress() cascade""")
        self._cr.execute("""create or replace function allpickoutaddress() returns void as $BODY$
           DECLARE
             pick_cur refcursor ;
             pick_rec record ;
           BEGIN
             open pick_cur for select id,neweb_phone from stock_picking where neweb_phone is not null ;
             loop
                fetch pick_cur into pick_rec ;
                exit when not found ;
                if substring(pick_rec.neweb_phone,1,3)='(03' or substring(pick_rec.neweb_phone,1,2)='03' then
                   update stock_picking set neweb_address='新竹市東區慈雲路118號12樓之5',neweb_fax='(03)-577-7380' where id=pick_rec.id ;
                elsif substring(pick_rec.neweb_phone,1,3)='(07' or substring(pick_rec.neweb_phone,1,2)='07' then
                    update stock_picking set neweb_address='高雄市前鎮區中山二路260號21樓A1',neweb_fax='(07)-334-5639' where id=pick_rec.id ;
                elsif substring(pick_rec.neweb_phone,1,3)='(04' or substring(pick_rec.neweb_phone,1,2)='04' then
                    update stock_picking set neweb_address='台中市南區工學一街197巷32號',neweb_fax=' ' where id=pick_rec.id ;    
                else
                    update stock_picking set neweb_address='114台北市內湖區行忠路42號2樓',neweb_fax='(02)-2795-5510' where id=pick_rec.id ;
                end if ;
             end loop ;
             close pick_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getprojserial(pickid int) cascade""")
        self._cr.execute("""create or replace function getprojserial(pickid int) returns void as $BODY$
           DECLARE
             ship_cur refcursor ;
             ship_rec record ;
             myprodserial varchar ;
           BEGIN
             open ship_cur for select id,stockout_sequence_id,prod_serial from neweb_stockship_list where stockship_id=pickid ;
             loop
               fetch ship_cur into ship_rec ;
               exit when not found ;
               select prod_serial into myprodserial from neweb_projsaleitem where id = ship_rec.stockout_sequence_id ;
               update neweb_stockship_list set prod_serial=myprodserial where id = ship_rec.id ;
             end loop ;
             close ship_cur ;
           END;$BODY$
           LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gendelstockout(pickingid int) cascade""")
        self._cr.execute("""create or replace function gendelstockout(pickingid int) returns void as $BODY$
          DECLARE
            ship_cur refcursor ;
            ship_rec record ;
            shipnum float ;
          BEGIN
            open ship_cur for select * from neweb_stockship_list where stockship_id = pickingid ;
            loop
               fetch ship_cur into ship_rec ;
               exit when not found ;
               execute unlinkstockoutlist1(ship_rec.id) ;
            end loop ;
            close ship_cur ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallshiplineitem() cascade""")
        self._cr.execute("""create or replace function genallshiplineitem() returns void as $BODY$
          DECLARE
            pick_cur refcursor ;
            pick_rec record ;
            ship_cur refcursor ;
            ship_rec record ;
            lineitem int ;
          BEGIN
            open pick_cur for select id,picking_type_id from stock_picking where picking_type_id in (4,9,14,19,24,29) ;
            loop
              fetch pick_cur into pick_rec ;
              exit when not found ;
              lineitem = 1 ;
              open ship_cur for select id from neweb_stockship_list where stockship_id=pick_rec.id order by id ;
              loop
                 fetch ship_cur into ship_rec ;
                 exit when not found ;
                 update neweb_stockship_list set line_item=lineitem where id = ship_rec.id ;
                 lineitem = lineitem + 1 ;
              end loop ;
              close ship_cur ;
            end loop ;
            close pick_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists insert_stock_picking() cascade""")
        self._cr.execute("""create or replace function insert_stock_picking() returns trigger as $BODY$
         DECLARE
          ncount int ;
          saleid int ;
         BEGIN
           select count(*) into ncount from sale_order where name=NEW.origin ;
           if ncount > 0 then
              select id into saleid from sale_order where name=NEW.origin ;
              execute gensalestockout(saleid) ;
           end if ;
           return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists stock_picking_insert on stock_picking;""")
        self._cr.execute("""create trigger stock_picking_insert after insert on stock_picking for each row execute procedure insert_stock_picking();""")

        self._cr.execute("""drop function if exists check_stock_quant() cascade""")
        self._cr.execute("""create or replace function check_stock_quant() returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           q_cur refcursor ;
           q_rec record ;
           ncount int ;
           qty float ;
           maxid int ;
         BEGIN
          open l_cur for select id from stock_location where usage='internal' and active=True ;
          loop
            fetch l_cur into l_rec ;
            exit when not found ;
            open q_cur for select distinct product_id from stock_quant where company_id=1 and location_id=l_rec.id and quantity != 0 ;
            loop
              fetch q_cur into q_rec ;
              exit when not found ;
              select sum(quantity) into qty from stock_quant where company_id=1 and location_id=l_rec.id and product_id=q_rec.product_id ;
              select max(id) into maxid from stock_quant where company_id=1 and location_id=l_rec.id and product_id=q_rec.product_id ;
              select count(*) into ncount from stock_quant where company_id=1 and location_id=l_rec.id and product_id=q_rec.product_id and quantity != 0;
              if ncount > 1 then
                 update stock_quant set quantity=0 where id < maxid and company_id=1 and location_id=l_rec.id and product_id=q_rec.product_id ;
                 update stock_quant set quantity=qty where id=maxid ;
              end if ;
            end loop ;
            close q_cur ;
          end loop ;
          close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genstockoutdate() cascade""")
        self._cr.execute("""create or replace function genstockoutdate() returns void as $BODY$
         DECLARE
           s_cur refcursor ;
           s_rec record ;
           outdate date ;
           pickingid int ;
         BEGIN
           open s_cur for select stockout_id,stockout_sequence_id,id,stockout_num,create_date from neweb_stockout_list where stockout_num > 0 ;
           loop
             fetch s_cur into s_rec ;
             exit when not found ;
             outdate = NULL ;
             select (s_rec.create_date + interval '8 hour')::DATE into outdate ;
             if outdate is null then
                select (scheduled_date + interval '8 hour')::DATE into outdate from stock_picking where id = s_rec.stockout_id ;
             end if ;
             if outdate is not null then
                update neweb_projsaleitem set stockout_date = outdate where id = s_rec.stockout_sequence_id ;
             end if ;   
           end loop ;
           close s_cur ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genstockindate() cascade""")
        self._cr.execute("""create or replace function genstockindate() returns void as $BODY$
         DECLARE
           s_cur refcursor ;
           s_rec record ;
           indate date ;
           pickingid int ;
           psaleitemid int ;
         BEGIN
           open s_cur for select stockin_id,stockin_sequence_id,id,stockin_num,create_date from neweb_stockin_list where stockin_num > 0 ;
           loop
             fetch s_cur into s_rec ;
             exit when not found ;
             indate = NULL ;
             select (s_rec.create_date + interval '8 hour')::DATE into indate ;
             if indate is null then
                select (scheduled_date + interval '8 hour')::DATE into indate from stock_picking where id = s_rec.stockin_id ;
             end if ;
             select pitem_origin_id into psaleitemid from neweb_pitem_list where id = s_rec.stockin_sequence_id ;
             if indate is not null then
                update neweb_projsaleitem set stockin_date = indate where id = psaleitemid ;
             end if ;   
           end loop ;
           close s_cur ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_copy_stockout1(projno varchar,stockid int) cascade""")
        self._cr.execute("""create or replace function gen_copy_stockout1(projno varchar,stockid int) returns void as $BODY$
         DECLARE
           projid int ;
           outnum float ;
           pj_cur refcursor ;
           pj_rec record ;
         BEGIN
           update stock_picking set is_proj_main=FALSE where id=stockid ;
           select id into projid from neweb_project where name=projno ;
           if projid is not null then
              open pj_cur for select * from neweb_projsaleitem where saleitem_id=projid ;
              loop
                 fetch pj_cur into pj_rec ;
                 exit when not found ;
                 select sum(stockout_num) into outnum from neweb_stockout_list where 
                     stockout_id in (select name from neweb_stockoutno_line where out_id=projid) 
                     and stockout_sequence_id=pj_rec.id ;
                 update neweb_projsaleitem set prod_stockoutnum=outnum where id = pj_rec.id ;
              end loop ;
              close pj_cur ;
           end if ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop index if exists stockout_idx1 cascade""")
        self.env.cr.execute("""create index stockout_idx1 on neweb_stockout_list(stockout_id)""")
        self.env.cr.execute("""drop index if exists stockout_idx2 cascade""")
        self.env.cr.execute("""create index stockout_idx2 on neweb_stockout_list(stockout_sequence_id)""")
        self.env.cr.execute("""drop index if exists stockoutnoline_idx1 cascade""")
        self.env.cr.execute("""create index stockoutnoline_idx1 on neweb_stockoutno_line(out_id)""")
        self.env.cr.execute("""drop index if exists stockoutnoline_idx2 cascade""")
        self.env.cr.execute("""create index stockoutnoline_idx2 on neweb_stockoutno_line(name)""")

        self._cr.execute("""drop function if exists gen_copy_stockout2(projno varchar,stockid int) cascade""")
        self._cr.execute("""create or replace function gen_copy_stockout2(projno varchar,stockid int) returns void as $BODY$
         DECLARE
           projid int ;
           outnum float ;
           pj_cur refcursor ;
           pj_rec record ;
           nitem int ;
           machinename varchar ;
           myname varchar ;
           unoutnum float ;
           mynowday timestamp ;
           ncount int ;
         BEGIN
           select id into projid from neweb_project where name=projno ;
           select current_timestamp into mynowday ;
           if projid is not null then
              nitem = 1 ;
              open pj_cur for select * from neweb_projsaleitem where saleitem_id=projid and (coalesce(prod_num,0) - coalesce(prod_stockoutnum,0)) > 0 order by line_item;
              loop
                fetch pj_cur into pj_rec ;
                exit when not found ;
                select name into machinename from neweb_sitem_modeltype1 where id=pj_rec.prod_modeltype1 ;
                unoutnum = coalesce(pj_rec.prod_num::numeric,0) - coalesce(pj_rec.prod_stockoutnum::numeric,0) ;
                insert into neweb_stockship_list(stockship_id,stockship_machinetype,stockship_modeltype,stockship_spec,stockship_num,stockship_price,create_date,write_date,stockout_sequence_id,stockship_item,line_item) values
                 (stockid,machinename,pj_rec.prod_modeltype,pj_rec.prod_desc,unoutnum,pj_rec.prod_price,mynowday,mynowday,pj_rec.id,nitem,nitem) ;
                select name into myname from neweb_prodbrand where id=pj_rec.prod_brand;
                insert into neweb_stockout_list(stockout_id,stockout_machinetype,stockout_modeltype,stockout_spec,stockout_num,stockout_price,stockout_sequence_id,create_date,write_date,line_item) values
                 (stockid,myname,pj_rec.prod_modeltype,pj_rec.prod_desc,unoutnum,pj_rec.prod_price,pj_rec.id,mynowday,mynowday,pj_rec.line_item);
                nitem = nitem + 1 ; 
              end loop ;
              close pj_cur ;
              select count(*) into ncount from neweb_stockoutno_line where out_id=projid and name=stockid ;
              if ncount = 0 and nitem > 1 then
                 insert into neweb_stockoutno_line(out_id,name) values (projid,stockid) ; 
              end if ;
           end if ;   
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallstockline() cascade""")
        self._cr.execute("""create or replace function genallstockline() returns void as $BODY$
         DECLARE
           p_cur refcursor ;
           p_rec record ;
           ncount int ;
           ncount1 int ;
           myid int ;
         BEGIN
           open p_cur for select id,name from neweb_project ;
           loop
             fetch p_cur into p_rec ;
             exit when not found ;
             select count(*) into ncount from neweb_stockoutno_line where out_id=p_rec.id ;
             if ncount=0 then
                select min(id) into myid from stock_picking where 
                picking_type_id in (select id from stock_picking_type where sequence_code='OUT') 
                    and stockout_proj_no=p_rec.name ;
                    if myid is not null then
                       update stock_picking set is_proj_main=TRUE where id = myid ;
                    end if ;    
                   insert into neweb_stockoutno_line(out_id,name) select p_rec.id,A.id 
                      from stock_picking A where stockout_proj_no=p_rec.name and 
                      picking_type_id in (select id from stock_picking_type where sequence_code='OUT')  ;
             end if;
           end loop ;
           close p_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_stockout(stockid int) cascade""")
        self._cr.execute("""create or replace function chk_stockout(stockid int) returns INT as $BODY$
         DECLARE
           projno varchar ;
           projid int ;
           pj_cur refcursor ;
           pj_rec record ;
           outnum float ;
           nitem int ;
           myres INT ;
         BEGIN
           select stockout_proj_no into projno from stock_picking where id=stockid ;
           select id into projid from neweb_project where name = projno ;
            if projid is not null then
              nitem = 0 ;
              open pj_cur for select * from neweb_projsaleitem where saleitem_id=projid ;
              loop
                 fetch pj_cur into pj_rec ;
                 exit when not found ;
                 select sum(stockout_num) into outnum from neweb_stockout_list where 
                     stockout_id in (select name from neweb_stockoutno_line where out_id=projid) 
                     and stockout_sequence_id=pj_rec.id ;
                 update neweb_projsaleitem set prod_stockoutnum=outnum where id = pj_rec.id ;
                 if coalesce(pj_rec.prod_num,0) > coalesce(outnum,0)  then
                    nitem = nitem + 1 ;
                 end if ;
              end loop ;
              close pj_cur ;
           end if ;   
           myres = nitem ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")




