# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError
class newebprojectstoreproc(models.Model):
    _name = "neweb.projectstoreproc"

    @api.model
    def init(self):
        #  專案成本分析計算store procedure
        self._cr.execute("""DROP FUNCTION IF EXISTS proj_cal_cost(proj_id int) cascade;""")
        self._cr.execute("""create or replace function proj_cal_cost(proj_id int) returns void as $BODY$
    declare
      proj_saleitem_cur refcursor ;
      saleitem_row record;
      proj_saleitem_cur1 refcursor ;
      proj_saleitem_row1 record ;
      ncount integer ;
      ncount1 integer ;
      ntotcost neweb_projanalysis.analysis_cost%type ;
      nsequence neweb_projanalysis.analysis_sequence%type ;
      ncosttype neweb_costtype.id%type ;
      ntotrevenue FLOAT ;
      myanalysiscost FLOAT;
      myanalysisrevenue FLOAT;
      myanalysisrevenue1 FLOAT;
      myanalysisrevenue2 FLOAT ;
      myanalysisprofit neweb_projanalysis.analysis_profit%type;
      myanalysisprofitrate neweb_projanalysis.analysis_profitrate%type;
      mytotalsaleitem FLOAT ;
      mytotalsaleitemtax FLOAT ;
      mytotalsaleitemamount FLOAT ;
      ndiv int;
      mytaxesid INTEGER ;
      mytaxamount FLOAT ;
      mysaleno VARCHAR ;
      mydiscountamount FLOAT;
      mysalediscountamount FLOAT ;
      myminid INTEGER ;
      myreventot FLOAT ;
      myprofittot FLOAT ;
      mytotalanalysisrevenue FLOAT ;
      mytotalanalysiscost FLOAT ;
      mytotalanalysisprofit FLOAT ;
      mytotalanalysisprofitrate FLOAT ;
      descpid int ;
    begin
      select max(id) into descpid from neweb_costtype where name ilike '%說明%' ;
      open proj_saleitem_cur for select * from neweb_projsaleitem where saleitem_id = proj_id and prod_num > 0  and cost_type != descpid ;
      nsequence = 0 ;
      loop
        nsequence = nsequence + 10 ;
        fetch proj_saleitem_cur into saleitem_row ;
        exit when not found ;
        select count(*) into ncount from neweb_projanalysis where analysis_id = proj_id and analysis_costtype = saleitem_row.cost_type ;
        select costtype_sequence into nsequence from neweb_costtype where id=saleitem_row.cost_type ;
        ncosttype := saleitem_row.cost_type ;  
        if ncount = 0 and saleitem_row.cost_type is not null then
           insert into neweb_projanalysis(analysis_id,analysis_costtype,analysis_sequence) values (proj_id,ncosttype,nsequence) ;
        end if ;
      end loop ;
      close proj_saleitem_cur ;
      open proj_saleitem_cur1 for select distinct cost_type from neweb_projsaleitem  where saleitem_id = proj_id and cost_type is not null order by cost_type;
      loop
        fetch proj_saleitem_cur1 into proj_saleitem_row1 ;
        exit when not found ;
        select sum(A.prod_num * A.prod_price) into myanalysiscost from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ;
        select sum(A.prod_num * A.prod_revenue) into myanalysisrevenue1 from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ;
        select sale_no into mysaleno from neweb_project where id=proj_id;
        select round(discount_amount/1.05) into myanalysisrevenue from sale_order where name like mysaleno;
        select sum(A.prod_num * (A.prod_revenue - A.prod_price)) into myanalysisprofit from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ;
        myanalysisprofitrate := 0 ;
        if myanalysisrevenue1=0 THEN 
          myanalysisprofitrate := 0 ;
        ELSE 
          myanalysisprofitrate := (myanalysisprofit / myanalysisrevenue1);
        end if ;
         
        update neweb_projanalysis  set analysis_cost = myanalysiscost,analysis_profit = myanalysisprofit,
               analysis_profitrate = (myanalysisprofitrate * 100)  where analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type ;
        update neweb_projanalysis  set analysis_revenue=myanalysisrevenue1 where  analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type and (analysis_revenue is null or analysis_revenue = 0) ;     
      end loop ;
      close proj_saleitem_cur1 ;
      select taxes_id,sale_no into mytaxesid,mysaleno from neweb_project where id=proj_id ;
      select sum(analysis_cost),sum(analysis_revenue) into ntotcost,ntotrevenue from neweb_projanalysis where analysis_id = proj_id ;
     /* if ntotrevenue=0 THEN 
         update neweb_project set total_analysis_cost=ntotcost,total_analysis_revenue=ntotrevenue,total_analysis_profit = 0,
              total_analysis_profitrate = 0,discount_amount=ntotrevenue where id = proj_id ;
      ELSE 
         select sum(prod_num * prod_price) into ntotrevenue from neweb_projsaleitem where saleitem_id=proj_id ;
         if ntotrevenue > 0 THEN 
            update neweb_project set total_analysis_cost=ntotcost,total_analysis_revenue=ntotrevenue,total_analysis_profit = ntotrevenue - ntotcost,
                   total_analysis_profitrate = (((ntotrevenue-ntotcost)/ ntotrevenue) * 100),discount_amount=ntotrevenue where id = proj_id ;
         end if ;
         
      end if; */
      
      /*execute proj_adjust_cost(proj_id);*/
      /*select sum(analysis_revenue) into ntotrevenue from neweb_projanalysis where analysis_id = proj_id ;*/
      select sum(prod_num * prod_price) into mytotalsaleitem from neweb_projsaleitem where saleitem_id=proj_id ;
      select amount into mytaxamount from account_tax where id=mytaxesid ;
      if mytaxamount > 0 THEN 
         mytotalsaleitemtax := round(mytotalsaleitem * (mytaxamount / 100)) ;
      ELSE 
         mytotalsaleitemtax := 0 ;
      end if ;
       mytotalsaleitemamount := mytotalsaleitem + mytotalsaleitemtax ;
      update neweb_project set total_saleitem=mytotalsaleitem,total_saleitem_tax=mytotalsaleitemtax,
              total_saleitem_amount=mytotalsaleitemamount where id=proj_id ; 
       
       select sum(analysis_revenue),sum(analysis_cost) into mytotalanalysisrevenue,mytotalanalysiscost from 
                   neweb_projanalysis where  analysis_id=proj_id ;
        mytotalanalysisprofit := mytotalanalysisrevenue - mytotalanalysiscost ;
        if mytotalanalysisrevenue > 0 THEN 
           mytotalanalysisprofitrate := ((mytotalanalysisprofit/mytotalanalysisrevenue)*100) ;
        ELSE 
           mytotalanalysisprofitrate := 0.00 ;
        end if ; 
       /* update neweb_project set total_analysis_revenue=mytotalanalysisrevenue,
               total_analysis_cost = mytotalanalysiscost,
               total_analysis_profit = mytotalanalysisprofit,
               total_analysis_profitrate = mytotalanalysisprofitrate where id = proj_id ;  */      
   
       
              
    end ;
    $BODY$
    LANGUAGE plpgsql;
    """)

        self._cr.execute("""DROP FUNCTION IF EXISTS proj_drop_cost(projid int,costtypeid int) cascade;""")
        self._cr.execute("""create or replace function proj_drop_cost(projid int,costtypeid int) returns void as $BODY$
              BEGIN
                delete from neweb_projanalysis where analysis_id=projid and analysis_costtype=costtypeid;
              END ;
              $BODY$
              LANGUAGE  plpgsql;

        """)

        # 由專案內容產生採購明細資料copy
        self._cr.execute("""DROP FUNCTION IF EXISTS genprojline(projlineid int,purid int) cascade;""")
        self._cr.execute("""create or replace function genprojline(projlineid int,purid int) returns void as $BODY$
                declare
                  myprojno neweb_project.name%type;
                  mysaleitemid neweb_projsaleitem.saleitem_id%type;
                  myamountuntaxed purchase_order.amount_untaxed%type;
                  myamounttax purchase_order.amount_tax%type;
                  myamounttotal purchase_order.amount_total%type;
                  mytaxesid account_tax.id%type;
                  myamount account_tax.amount%type;
                begin
                 select saleitem_id into mysaleitemid from neweb_projsaleitem where id=projlineid;
                 select name into myprojno from neweb_project where id=mysaleitemid;
                 insert into neweb_pitem_list (pitem_id,pitem_model_type,pitem_prod_no,pitem_spec,pitem_num,pitem_price,pitem_sum,pitem_origin_no,pitem_origin_id,pitem_origin_type,pitem_warranty,pitem_stockin_num) select
                   purid,coalesce(prod_modeltype,' '),coalesce(prod_no,' '),coalesce(prod_desc,' '),(prod_num - coalesce(prod_purnum,0)),coalesce(prod_price,0),((prod_num-coalesce(prod_purnum,0))*prod_price),myprojno,id,'P',coalesce(warranty,' '),0 from neweb_projsaleitem
                   where id=projlineid ;
                 select sum(pitem_num * pitem_price) into myamountuntaxed from neweb_pitem_list where pitem_id = purid ;
                 select taxes_id into mytaxesid from purchase_order where id=purid ;
                 select amount into myamount from account_tax where id = mytaxesid ;
                 myamounttax := (myamountuntaxed * myamount /100) ;
                 myamounttotal := myamountuntaxed + myamounttax ;
                 update purchase_order set amount_untaxed=myamountuntaxed,amount_tax=myamounttax,amount_total=myamounttotal,
                      pitem_untax=myamountuntaxed,pitem_tax=myamounttax,pitem_amounttot=myamounttotal where id=purid ;

                end;
                $BODY$
                LANGUAGE plpgsql;""")


        # 設定系統日期時間格式
        mylangrec = self.env['res.lang'].search([('code', '=', 'zh_TW')])
        mylangrec.write({'date_format': '%Y-%m-%d',
                         'time_format': '%H:%M:%S'})

        mypararec = self.env['ir.config_parameter'].search([('key','=','web_m2x_options.create')])
        if mypararec:
           mypararec.write({'value': 'False'})
        else:
           mypararec.create({'key': 'web_m2x_options.create','value': 'False'})
        mypararec = self.env['ir.config_parameter'].search([('key', '=', 'web_m2x_options.create_edit')])
        if mypararec:
            mypararec.write({'value': 'False'})
        else:
            mypararec.create({'key': 'web_m2x_options.create_edit','value': 'False'})
        mypararec = self.env['ir.config_parameter'].search([('key', '=', 'web_m2x_options.limit')])
        if mypararec:
            mypararec.write({'value': '15'})
        else:
            mypararec.create({'key': 'web_m2x_options.limit','value': '15'})

        self._cr.execute("""DROP FUNCTION IF EXISTS projsaleid(p_id int) cascade;""")
        self._cr.execute("""create or replace function projsaleid(p_id int) returns void as $BODY$
            declare
              partner_user_cur cursor is select * from partner_user_tag_rel where partner_id = p_id ;
              p_u_row record;
            begin
             delete from user_partner_tag_rel where partner_id=p_id ;
             open partner_user_cur ;
             loop
               fetch partner_user_cur into p_u_row ;
               exit when not found;
               insert into user_partner_tag_rel(partner_id,user_id) values (p_u_row.partner_id,p_u_row.user_id);
             end loop;
             close partner_user_cur ;
            end;
            $BODY$
            LANGUAGE plpgsql ;
            """)

        self._cr.execute("""DROP FUNCTION IF EXISTS projsale_custom(proj_id int) cascade;""")
        self._cr.execute("""create or replace function projsale_custom(proj_id int) returns setof character varying as $BODY$
            declare
               refpartner refcursor ;
               refpartnerrow record ;
               ncount INTEGER ;
            begin
              select count(*) into ncount from neweb_projcontact where contact_id=proj_id ;
              if ncount > 0 then
                 open refpartner for select contact_name from neweb_projcontact where contact_id=proj_id ;
              ELSE
                 open refpartner for select id from res_partner where is_company=FALSE and customer_rank = 1 ;
              end if ;
    
              loop
                fetch refpartner into refpartnerrow ;
                exit when not found;
                if ncount > 0 THEN
                  return next refpartnerrow.contact_name ;
                ELSE
                  return next refpartnerrow.id ;
                end if ;
              end loop ;
              close refpartner ;
            end ; $BODY$ LANGUAGE plpgsql ;""")


        self._cr.execute("""DROP FUNCTION IF EXISTS unlinkproject(myprojid int) cascade;""")
        self._cr.execute("""create or replace function unlinkproject(myprojid int) returns void as $BODY$
            declare
              mysaleno sale_order.name%type;
            begin
              select substr(sale_no,1,10) into mysaleno from neweb_project where id = myprojid ;
              update neweb_salenocheck set trans_proj=FALSE where sale_no=mysaleno ;
            end;$BODY$
            LANGUAGE plpgsql;
            """)

        self._cr.execute("""DROP FUNCTION IF EXISTS proj_saletot(myprojid int) cascade;""")
        self._cr.execute("""create or replace function proj_saletot(myprojid int) returns FLOAT as $BODY$
            declare
              myrevenuetot neweb_projsaleitem.prod_revenue%type;
            begin
              select sum(prod_num * prod_revenue) into myrevenuetot from neweb_projsaleitem where saleitem_id = myprojid ;
              return myrevenuetot ;
            end;$BODY$
            LANGUAGE plpgsql;
            """)

        self._cr.execute("""DROP FUNCTION IF EXISTS proj_analysistot(myprojid int) cascade;""")
        self._cr.execute("""create or replace function proj_analysistot(myprojid int) returns FLOAT as $BODY$
                declare
                  myrevenuetot neweb_projanalysis.analysis_revenue%type;
                begin
                  select sum(analysis_revenue) into myrevenuetot from neweb_projanalysis where analysis_id = myprojid ;
                  return myrevenuetot ;
                end;$BODY$
                LANGUAGE plpgsql;
                """)

        self._cr.execute("""DROP FUNCTION IF EXISTS proj_analysistype(myprojid int) cascade;""")
        self._cr.execute("""create or replace function proj_analysistype(myprojid int) returns Boolean as $BODY$
            declare
              refanalysiscur refcursor;
              refanalysisrec record;
              ncount int;
              myrecdup boolean;
            begin
              myrecdup := FALSE ;
              open refanalysiscur for select distinct analysis_costtype from neweb_projanalysis where analysis_id = myprojid ;
              loop
                 fetch refanalysiscur into refanalysisrec ;
                 exit when not found ;
                 select count(*) into ncount from neweb_projanalysis where analysis_costtype=refanalysisrec.analysis_costtype and analysis_id = myprojid ;
                 if ncount > 1 then
                    myrecdup := TRUE ;
                 end if;
              end loop;
              close refanalysiscur ;
              return myrecdup ;
            end;$BODY$
            LANGUAGE plpgsql;
            """)

        self._cr.execute("""DROP FUNCTION IF EXISTS projsaleitemexport(myprojid int) cascade;""")
        self._cr.execute("""create or replace function projsaleitemexport(myprojid int) returns void as $BODY$
            declare
              scur refcursor;
              srec record;
              myprodset varchar ;
              mycosttype varchar ;
              myprodbrand varchar;
              mstartdate date ;
              menddate date ;
              mymaindate varchar ;
              mysupplier varchar ;
              myseqid int;
              mycostdept varchar ;
            begin
              myseqid := 1 ;
              delete from neweb_projsaleitem_export ;
              open scur for select * from neweb_projsaleitem where saleitem_id = myprojid order by id;
              loop
                 fetch scur into srec ;
                 exit when not found ;
                 if srec.neweb_start_date is not null and srec.neweb_end_date is not null then
                    mymaindate = concat(to_char(srec.neweb_start_date,'YYYYMMDD'),'-',to_char(srec.neweb_end_date,'YYYYMMDD')) ;
                 else
                    mymaindate = ' ' ;
                 end if ;
                 select comp_sname into mysupplier from res_partner where id = srec.supplier ;
                 select name into myprodset from neweb_prodset where id=srec.prod_set ;
                 select name into mycosttype from neweb_costtype where id=srec.cost_type;
                 select name into myprodbrand from neweb_prodbrand where id=srec.prod_brand;
                 select name into mycostdept from neweb_cost_dept where id = srec.cost_dept ;
                 insert into neweb_projsaleitem_export (seqid,prodset,prodmodeltype,proddesc,prodnum,prod_price,supplier,costtype,dis_price,prodbrand,prodserial,maintenance_term,saleitem_item,cost_dept,prodmodeltype1) VALUES
                  (myseqid,myprodset,srec.prod_modeltype,srec.prod_desc,srec.prod_num,srec.prod_price,mysupplier,mycosttype,srec.prod_revenue,myprodbrand,srec.prod_serial,mymaindate,srec.saleitem_item,mycostdept,srec.prod_modeltype1) ;
                  myseqid = myseqid + 1 ;
              end loop;
              close scur ;
            end;$BODY$
            LANGUAGE plpgsql;
            """)


        self._cr.execute("""DROP FUNCTION IF EXISTS proj_adjust_cost(projid int) cascade;""")
        self._cr.execute("""create or replace function proj_adjust_cost(projid int) returns void as $BODY$
           DECLARE
              maxrevenue neweb_projanalysis.analysis_revenue%type;
              myid neweb_projanalysis.id%type;
              totrevenue neweb_projanalysis.analysis_revenue%type;
              realrevenue neweb_projanalysis.analysis_revenue%type;
              mycost neweb_projanalysis.analysis_cost%type;
              myrevenue neweb_projanalysis.analysis_revenue%type;
              totcost neweb_projanalysis.analysis_cost%type;
              mysaleno varchar;

           BEGIN
              select sum(analysis_revenue) into totrevenue from neweb_projanalysis where analysis_id=projid ;
              select max(analysis_revenue) into maxrevenue from neweb_projanalysis where analysis_id=projid;
              select distinct id into myid from neweb_projanalysis  where analysis_id=projid and analysis_revenue=maxrevenue ;
              /*select sum(A.prod_num * A.prod_revenue) into realrevenue from neweb_projsaleitem A where A.saleitem_id=projid ;*/
              select sale_no into mysaleno from neweb_project where id = projid;
              select round(discount_amount/1.05) into realrevenue from sale_order where name like mysaleno ;
              update neweb_projanalysis set analysis_revenue = realrevenue - (totrevenue - maxrevenue) where id=myid;
              select analysis_cost,analysis_revenue into mycost,myrevenue from neweb_projanalysis where id=myid;
              if myrevenue > 0 THEN
                 update neweb_projanalysis set analysis_profit=(myrevenue - mycost),analysis_profitrate=(((myrevenue-mycost)/myrevenue)*100) where id=myid;
              end if;
              
              select sum(analysis_cost) into totcost from neweb_projanalysis where analysis_id=projid;
              select sum(analysis_revenue) into totrevenue from neweb_projanalysis where analysis_id=projid;
              if totrevenue = 0 THEN 
                 totrevenue := 1 ;
              end if;
             /* update neweb_project set total_analysis_cost=totcost,total_analysis_revenue=totrevenue,
                     total_analysis_profit=(totrevenue-totcost),total_analysis_profitrate=((totrevenue-totcost)*100/totrevenue)
                     where id=projid; */
           END;$BODY$
           LANGUAGE plpgsql;
        """)

        self._cr.execute("""DROP FUNCTION IF EXISTS updatecalcost(proj_id int) cascade;""")
        self._cr.execute("""create or replace function updatecalcost(proj_id int) returns Boolean as $BODY$
           declare
               projtotrevenue FLOAT ;
               projtotcost FLOAT ;
               myrevenue FLOAT ;
               mycost FLOAT ;
               myfirstgen INTEGER ;
               sitemid INTEGER ;
               csaleno VARCHAR ;
               mysaletotrevenue INTEGER ;
               mysaletotrevenue1 INTEGER ;
               ncount INTEGER ;
               ncount1 INTEGER ;
               untaxamount INTEGER ;
               tax INTEGER ;
               myimportstatus Boolean;
           BEGIN 
               select count(*) into ncount from neweb_projanalysis where analysis_id=proj_id;
               select count(*) into ncount1 from neweb_projsaleitem where saleitem_id=proj_id;
               select sum(analysis_revenue) into myrevenue from neweb_projanalysis where analysis_id=proj_id;
               select sum(analysis_cost) into mycost from neweb_projanalysis where analysis_id=proj_id;
               select sum(prod_num * prod_revenue) into projtotrevenue from neweb_projsaleitem where saleitem_id=proj_id;
               select sum(prod_num * prod_price) into projtotcost from neweb_projsaleitem where saleitem_id=proj_id;
               select sale_no,proj_import_status into csaleno,myimportstatus from neweb_project where id=proj_id ;
               select id,discount_amount into sitemid,mysaletotrevenue from sale_order where name like csaleno;
               select round(mysaletotrevenue/1.05) into untaxamount ;
               tax := mysaletotrevenue - untaxamount ;
               if myimportstatus=TRUE then 
                    return TRUE  ;
               else 
                    select sum(sitem_price*sitem_num) into mysaletotrevenue1 from neweb_sitem_list where sitem_id=sitemid ; 
                    if abs(myrevenue - untaxamount) <= 5  or ncount = 0 or ncount1 = 0 or projtotrevenue = 0  or myrevenue = 0  then
                      return TRUE ;
                    ELSE 
                      return FALSE ;
                    end if ; 
               end if ;     
           END ;$BODY$
           LANGUAGE plpgsql; 
                         """)


        self._cr.execute("""DROP FUNCTION IF EXISTS partner1_insert(myvat varchar,myname varchar,mcompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                        mycheckoutdate int,mypaymentdays int) cascade;""")
        self._cr.execute("""create or replace function partner1_insert(myvat varchar,myname varchar,mycompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                        mycheckoutdate int,mypaymentdays int) returns void as $BODY$
                             declare
                                ncount int ;
                                myparentid int;
                             BEGIN  
                             select count(*) into ncount from res_partner where name like myname;
                             if ncount = 0 then
                                 insert into res_partner(vat,name,comp_sname,street,phone,fax,customer,supplier,is_company,email,checkout_date,payment_days,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id,display_name) 
                                         values (myvat,myname,mycompsname,mystreet,myphone,myfax,true,false,true,myemail,mycheckoutdate,mypaymentdays,'no-message','no-message','no-message','no-message','always',true,1,myname) ;
                                       if LENGTH(mycontactname) > 0 THEN 
                                          select id into myparentid from res_partner where name like myname ;
                                          insert into res_partner (parent_id,name,phone,mobile,email,is_company,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id) 
                                             values (myparentid,mycontactname,myphone,mymobile,myemail,false,'no-message','no-message','no-message','no-message','always',true,1) ;
                                       end if ;
                             end if;          
                             END ; $BODY$
                             LANGUAGE plpgsql;
                       """)

        self._cr.execute("""DROP FUNCTION IF EXISTS partner2_insert(myvat varchar,myname varchar,mcompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                                mycheckoutdate int,mypaymentdays int) cascade;""")
        self._cr.execute("""create or replace function partner2_insert(myvat varchar,myname varchar,mycompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                                mycheckoutdate int,mypaymentdays int) returns void as $BODY$
                                     declare
                                        ncount int ;
                                        myparentid int;
                                     BEGIN  
                                     select count(*) into ncount from res_partner where name like myname;
                                     if ncount = 0 then
                                         insert into res_partner(vat,name,comp_sname,street,phone,fax,customer,supplier,is_company,email,checkout_date,payment_days,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id,display_name) 
                                                 values (myvat,myname,mycompsname,mystreet,myphone,myfax,false,true,true,myemail,mycheckoutdate,mypaymentdays,'no-message','no-message','no-message','no-message','always',true,1,myname) ;
                                               if LENGTH(mycontactname) > 0 THEN 
                                                  select id into myparentid from res_partner where name like myname ;
                                                  insert into res_partner (parent_id,name,phone,mobile,email,is_company,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id) 
                                                     values (myparentid,mycontactname,myphone,mymobile,myemail,false,'no-message','no-message','no-message','no-message','always',true,1) ;
                                               end if ;
                                     end if;          
                                     END ; $BODY$
                                     LANGUAGE plpgsql;
                               """)

        self._cr.execute("""DROP FUNCTION IF EXISTS partner3_insert(myvat varchar,myname varchar,mcompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                                mycheckoutdate int,mypaymentdays int) cascade;""")
        self._cr.execute("""create or replace function partner3_insert(myvat varchar,myname varchar,mycompsname varchar,mystreet varchar,mycontactname varchar,myphone varchar,mymobile varchar,myfax varchar,myemail varchar,
                                mycheckoutdate int,mypaymentdays int) returns void as $BODY$
                                     declare
                                        ncount int ;
                                        myparentid int;
                                     BEGIN  
                                     select count(*) into ncount from res_partner where name like myname;
                                     if ncount = 0 then
                                         insert into res_partner(vat,name,comp_sname,street,phone,fax,customer,supplier,is_company,email,checkout_date,payment_days,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id,display_name) 
                                                 values (myvat,myname,mycompsname,mystreet,myphone,myfax,true,true,true,myemail,mycheckoutdate,mypaymentdays,'no-message','no-message','no-message','no-message','always',true,1,myname) ;
                                               if LENGTH(mycontactname) > 0 THEN 
                                                  select id into myparentid from res_partner where name like myname ;
                                                  insert into res_partner (parent_id,name,phone,mobile,email,is_company,invoice_warn,picking_warn,purchase_warn,sale_warn,notify_email,active,company_id) 
                                                     values (myparentid,mycontactname,myphone,mymobile,myemail,false,'no-message','no-message','no-message','no-message','always',true,1) ;
                                               end if ;
                                     end if;          
                                     END ; $BODY$
                                     LANGUAGE plpgsql;
                               """)

        self._cr.execute("""DROP FUNCTION IF EXISTS updatevat() cascade;""")
        self._cr.execute("""create or replace function updatevat() returns void as $BODY$
                 DECLARE 
                   myvatprefix VARCHAR ;
                   partner_cur refcursor;
                   partner_rec record;
                   mylen INTEGER ;
                   mynetlen INTEGER ;
                 BEGIN 
                   open partner_cur for select id,vat from res_partner where substring(vat,1,2)='TW' ;
                   loop
                      fetch partner_cur into partner_rec;
                      exit when not found;
                      mylen := length(partner_rec.vat) ;
                      mynetlen := mylen - 2 ;
                      update res_partner set vat = substring(partner_rec.vat,3,mynetlen) where id=partner_rec.id ;
                   end loop;
                   close partner_cur;
                 END ;$BODY$
                 LANGUAGE plpgsql;
                   """)
        ## 採購變更進價單價更新用
        self._cr.execute("""DROP FUNCTION IF EXISTS proj_rcal_cost(proj_id int) cascade;""")
        self._cr.execute("""create or replace function proj_rcal_cost(proj_id int) returns void as $BODY$
         declare
           proj_saleitem_cur cursor is select * from neweb_projsaleitem where saleitem_id = proj_id and prod_num > 0 and cost_type is not null and cost_type != 13 ;
           saleitem_row record;
           proj_saleitem_cur1 refcursor ;
           proj_saleitem_row1 record ;
           ncount integer ;
           ncount1 integer ;
           ntotcost neweb_projanalysis.analysis_cost%type ;
           nsequence neweb_projanalysis.analysis_sequence%type ;
           ncosttype neweb_costtype.id%type ;
           ntotrevenue neweb_projanalysis.analysis_revenue%type ;
           myanalysiscost neweb_projanalysis.analysis_cost%type;
           myanalysisrevenue neweb_projanalysis.analysis_revenue%type;
           myanalysisrevenue1 neweb_projanalysis.analysis_revenue%type;
           myanalysisrevenue2 FLOAT ;
           myanalysisprofit FLOAT;
           myanalysisprofitrate FLOAT;
           mytotalsaleitem FLOAT ;
           mytotalsaleitemtax FLOAT ;
           mytotalsaleitemamount FLOAT ;
           ndiv int;
           mytaxesid INTEGER ;
           mytaxamount FLOAT ;
           mysaleno VARCHAR ;
           mydiscountamount FLOAT;
           mysalediscountamount FLOAT ;
           myminid INTEGER ;
           mytotalanalysisrevenue FLOAT ;
           mytotalanalysiscost FLOAT ;
           mytotalanalysisprofit FLOAT ;
           mytotalanalysisprofitrate FLOAT ;
         begin
          open proj_saleitem_cur ;
           nsequence = 0 ;
           loop
             nsequence = nsequence + 10 ;
             fetch proj_saleitem_cur into saleitem_row ;
             exit when not found ;
             select count(*) into ncount from neweb_projanalysis where analysis_id = proj_id and analysis_costtype = saleitem_row.cost_type ;
             select costtype_sequence into nsequence from neweb_costtype where id=saleitem_row.cost_type ;
             if ncount = 0 then
                insert into neweb_projanalysis(analysis_id,analysis_costtype,analysis_sequence) values (proj_id,saleitem_row.cost_type,nsequence) ;
             end if ;
           end loop ;
           close proj_saleitem_cur ; 
           update neweb_projanalysis set analysis_cost=0.00,analysis_profit=0.00,analysis_profitrate=0.00 where analysis_id=proj_id ;
           open proj_saleitem_cur1 for select distinct cost_type from neweb_projsaleitem  where saleitem_id = proj_id order by cost_type;
           loop
             fetch proj_saleitem_cur1 into proj_saleitem_row1 ;
             exit when not found ;
             select sum(A.prod_num * A.prod_price) into myanalysiscost from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ;
             select sum(analysis_revenue) into myanalysisrevenue from neweb_projanalysis where analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type ;
             select sum(analysis_revenue - analysis_cost) into myanalysisprofit from neweb_projanalysis where analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type ;
             if coalesce(myanalysisrevenue,0)=0 then
                select sum(A.prod_num * A.prod_revenue) into myanalysisrevenue from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ; 
                myanalysisprofit = myanalysisrevenue - myanalysiscost ;
             end if ;   
             
             if myanalysisrevenue=0 THEN 
                myanalysisprofitrate := 0 ;
             ELSE   
                myanalysisprofitrate := (myanalysisprofit/myanalysisrevenue) ;
             END if ;
             update neweb_projanalysis  set analysis_cost = myanalysiscost,analysis_profit=myanalysisprofit,
                    analysis_profitrate = myanalysisprofitrate * 100 ,analysis_revenue = myanalysisrevenue
                     where analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type ; 
           end loop ;
           close proj_saleitem_cur1 ;
           select sale_no into mysaleno from neweb_project where id=proj_id;
           /*select round(discount_amount/1.05) into ntotrevenue from sale_order where name like mysaleno;*/
           select sum(analysis_revenue) into ntotrevenue from neweb_projanalysis where analysis_id = proj_id ;
           select taxes_id,sale_no into mytaxesid,mysaleno from neweb_project where id=proj_id ;
           select sum(analysis_cost) into ntotcost from neweb_projanalysis where analysis_id = proj_id ;
           
          /* if ntotrevenue=0 THEN 
              update neweb_project set total_analysis_cost=ntotcost,total_analysis_revenue=ntotrevenue,total_analysis_profit = 0,
                   total_analysis_profitrate = 0,discount_amount=ntotrevenue where id = proj_id ;
           ELSE 
              update neweb_project set total_analysis_cost=ntotcost,total_analysis_revenue=ntotrevenue,total_analysis_profit = ntotrevenue - ntotcost,
                   total_analysis_profitrate = (((ntotrevenue-ntotcost)/ ntotrevenue) * 100),discount_amount=ntotrevenue where id = proj_id ;
           end if; */
           select sum(prod_num * prod_price) into mytotalsaleitem from neweb_projsaleitem where saleitem_id=proj_id ;
           select amount into mytaxamount from account_tax where id=mytaxesid ;
           if mytaxamount > 0 THEN 
              mytotalsaleitemtax := round(mytotalsaleitem * 0.05);
           ELSE 
              mytotalsaleitemtax := 0 ;
           end if ;
            mytotalsaleitemamount := mytotalsaleitem + mytotalsaleitemtax ;
            update neweb_project set total_saleitem=mytotalsaleitem,total_saleitem_tax=mytotalsaleitemtax,
                   total_saleitem_amount=mytotalsaleitemamount where id=proj_id ;
            select sum(analysis_revenue),sum(analysis_cost) into mytotalanalysisrevenue,mytotalanalysiscost from 
                   neweb_projanalysis where  analysis_id=proj_id ;
            mytotalanalysisprofit := mytotalanalysisrevenue - mytotalanalysiscost ;
            if mytotalanalysisrevenue > 0 THEN 
               mytotalanalysisprofitrate := ((mytotalanalysisprofit/mytotalanalysisrevenue)*100) ;
            ELSE 
               mytotalanalysisprofitrate := 0.00 ;
            end if ; 
            update neweb_projanalysis set analysis_profit=analysis_revenue - analysis_cost,
                   analysis_profitrate = (((analysis_revenue - analysis_cost) / analysis_revenue)*100) where 
                   analysis_id = proj_id and analysis_revenue > 0  ;
           /* update neweb_project set total_analysis_revenue=mytotalanalysisrevenue,
                   total_analysis_cost = mytotalanalysiscost,
                   total_analysis_profit = mytotalanalysisprofit,
                   total_analysis_profitrate = mytotalanalysisprofitrate where id = proj_id ;   */  
            delete from neweb_projanalysis where (analysis_cost=0 or analysis_cost is null) and (analysis_revenue is null or analysis_revenue=0) and analysis_id = proj_id ;            
         end ;
         $BODY$
         LANGUAGE plpgsql;
         """)

        ## 成本分析第一次匯入時運用
        self._cr.execute("""DROP FUNCTION IF EXISTS proj_rcal_cost1(proj_id int) cascade;""")
        self._cr.execute("""create or replace function proj_rcal_cost1(proj_id int) returns void as $BODY$
         declare
           proj_saleitem_cur cursor is select * from neweb_projsaleitem where saleitem_id = proj_id and prod_num > 0 and cost_type is not null ;
           saleitem_row record;
           proj_saleitem_cur1 refcursor ;
           proj_saleitem_row1 record ;
           ncount integer ;
           ncount1 integer ;
           ntotcost neweb_projanalysis.analysis_cost%type ;
           nsequence neweb_projanalysis.analysis_sequence%type ;
           ncosttype neweb_costtype.id%type ;
           ntotrevenue neweb_projanalysis.analysis_revenue%type ;
           myanalysiscost neweb_projanalysis.analysis_cost%type;
           myanalysisrevenue neweb_projanalysis.analysis_revenue%type;
           myanalysisrevenue1 neweb_projanalysis.analysis_revenue%type;
           myanalysisrevenue2 FLOAT ;
           myanalysisprofit FLOAT;
           myanalysisprofitrate FLOAT;
           mytotalsaleitem FLOAT ;
           mytotalsaleitemtax FLOAT ;
           mytotalsaleitemamount FLOAT ;
           ndiv int;
           mytaxesid INTEGER ;
           mytaxamount FLOAT ;
           mysaleno VARCHAR ;
           mydiscountamount FLOAT;
           mysalediscountamount FLOAT ;
           myminid INTEGER ;
           mytotalanalysisrevenue FLOAT ;
           mytotalanalysiscost FLOAT ;
           mytotalanalysisprofit FLOAT ;
           mytotalanalysisprofitrate FLOAT ;
         begin
           open proj_saleitem_cur ;
           nsequence = 0 ;
           loop
             nsequence = nsequence + 10 ;
             fetch proj_saleitem_cur into saleitem_row ;
             exit when not found ;
             select count(*) into ncount from neweb_projanalysis where analysis_id = proj_id and analysis_costtype = saleitem_row.cost_type ;
             select costtype_sequence into nsequence from neweb_costtype where id=saleitem_row.cost_type ;
             if ncount = 0 then
                insert into neweb_projanalysis(analysis_id,analysis_costtype,analysis_sequence) values (proj_id,saleitem_row.cost_type,nsequence) ;
             end if ;
           end loop ;
           close proj_saleitem_cur ;
           update neweb_projanalysis set analysis_cost=0.00,analysis_profit=0.00,analysis_profitrate=0.00 where analysis_id=proj_id ;
           open proj_saleitem_cur1 for select distinct cost_type from neweb_projsaleitem  where saleitem_id = proj_id and cost_type != 13 order by cost_type;
           loop
             fetch proj_saleitem_cur1 into proj_saleitem_row1 ;
             exit when not found ;
             select sum(A.prod_num * A.prod_price) into myanalysiscost from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ;
             select sum(A.prod_num * A.prod_revenue) into myanalysisrevenue from neweb_projsaleitem A where A.saleitem_id = proj_id and A.cost_type = proj_saleitem_row1.cost_type ; 
             myanalysisprofit = myanalysisrevenue - myanalysiscost ;
             if myanalysisrevenue=0 THEN 
                myanalysisprofitrate := 0 ;
             ELSE   
                myanalysisprofitrate := (myanalysisprofit/myanalysisrevenue) ;
             END if ;
             update neweb_projanalysis  set analysis_cost = myanalysiscost,analysis_profit=myanalysisprofit,
                    analysis_profitrate = myanalysisprofitrate * 100 ,analysis_revenue = myanalysisrevenue
                     where analysis_id=proj_id and analysis_costtype = proj_saleitem_row1.cost_type ; 
           end loop ;
           close proj_saleitem_cur1 ;
           select sale_no into mysaleno from neweb_project where id=proj_id;
           select sum(analysis_revenue) into ntotrevenue from neweb_projanalysis where analysis_id = proj_id ;
           select taxes_id,sale_no into mytaxesid,mysaleno from neweb_project where id=proj_id ;
           select sum(analysis_cost) into ntotcost from neweb_projanalysis where analysis_id = proj_id ;


           select sum(prod_num * prod_price) into mytotalsaleitem from neweb_projsaleitem where saleitem_id=proj_id ;
           select amount into mytaxamount from account_tax where id=mytaxesid ;
           if mytaxamount > 0 THEN 
              mytotalsaleitemtax := round(mytotalsaleitem * 0.05);
           ELSE 
              mytotalsaleitemtax := 0 ;
           end if ;
            mytotalsaleitemamount := mytotalsaleitem + mytotalsaleitemtax ;
            update neweb_project set total_saleitem=mytotalsaleitem,total_saleitem_tax=mytotalsaleitemtax,
                   total_saleitem_amount=mytotalsaleitemamount where id=proj_id ;
            select sum(analysis_revenue),sum(analysis_cost) into mytotalanalysisrevenue,mytotalanalysiscost from 
                   neweb_projanalysis where  analysis_id=proj_id ;
            mytotalanalysisprofit := mytotalanalysisrevenue - mytotalanalysiscost ;
            if mytotalanalysisrevenue > 0 THEN 
               mytotalanalysisprofitrate := ((mytotalanalysisprofit/mytotalanalysisrevenue)*100) ;
            ELSE 
               mytotalanalysisprofitrate := 0.00 ;
            end if ; 
            update neweb_projanalysis set analysis_profit=analysis_revenue - analysis_cost,
                   analysis_profitrate = (((analysis_revenue - analysis_cost) / analysis_revenue)*100) where 
                   analysis_id = proj_id and analysis_revenue > 0  ; 
            delete from neweb_projanalysis where (analysis_cost=0 or analysis_cost is null) and (analysis_revenue is null or analysis_revenue=0) and analysis_id = proj_id ;            
         end ;
         $BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists get_discount_amount(projid int) cascade""")
        self._cr.execute("""create or replace function get_discount_amount(projid int) returns FLOAT as $BODY$
             DECLARE 
               ncount INT ;
               myamountexcludetax FLOAT ;
               mysaleno VARCHAR ;
               mytaxamount FLOAT ;
               mytaxesid INT ;
               mytax FLOAT ;
             BEGIN 
               select taxes_id,sale_no into mytaxesid,mysaleno from neweb_project where id=projid ;
               select coalesce(amount,0) into mytaxamount from account_tax where id=mytaxesid ;
               select count(*) into ncount from sale_order where name like mysaleno;
               if ncount > 0 then
                   select round(discount_amount/(1 + (mytaxamount/100))) into myamountexcludetax from sale_order where name like mysaleno ;
               ELSE 
                   myamountexcludetax = 0 ;  
               end if ;    
               return myamountexcludetax ;
             END ; $BODY$
             LANGUAGE plpgsql; 
                """)

        self._cr.execute("""drop function if exists getcostdept(costdept varchar) cascade""")
        self._cr.execute("""create or replace function getcostdept(costdept varchar) returns int as $BODY$
            DECLARE
              ncount int ;
              myres int ;
            BEGIN
              /* select id into myres from neweb_cost_dept where name like '%%'|| costdept ||'%%' ; */
              select id into myres from neweb_cost_dept where name=costdept;
              if myres is null then
                 myres = 0 ;
              end if ;   
              return myres ;
            END;$BODY$
            LANGUAGE plpgsql;""")
