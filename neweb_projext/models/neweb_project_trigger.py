# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class NewebProjectTrigger(models.Model):
    _name = "neweb.project_trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_recal_projanalysis() cascade""")
        self._cr.execute("""create  or replace function insert_recal_projanalysis() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            execute proj_cal_cost(NEW.saleitem_id) ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists update_recal_projanalysis() cascade""")
        self._cr.execute("""create  or replace function update_recal_projanalysis() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            if NEW.prod_num != OLD.prod_num or NEW.prod_price != OLD.prod_price or NEW.prod_revenue != OLD.prod_revenue then
               execute proj_cal_cost(NEW.saleitem_id) ;
            end if ;  
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        # 針對每次新增 neweb_projsaleitem 作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_on_neweb_projsaleitem on neweb_projsaleitem ;""")
        # self._cr.execute("""create trigger insert_on_neweb_projsaleitem after insert on neweb_projsaleitem
        #                          for each row execute procedure insert_recal_projanalysis();""")

        self._cr.execute("""drop trigger if exists update_on_neweb_projsaleitem on neweb_projsaleitem""")
        # self._cr.execute("""create trigger update_on_neweb_projsaleitem after update on neweb_projsaleitem
        #                                  for each row execute procedure update_recal_projanalysis();""")

        self._cr.execute("""drop function if exists recal_profit() cascade""")
        self._cr.execute("""create  or replace function recal_profit() returns trigger as $BODY$
          DECLARE
            ncount int ;
            ana_cur refcursor ;
            ana_rec record ;
            anaprofit float ;
            anaprofitrate float ;
          BEGIN
            open ana_cur for select * from neweb_projanalysis where analysis_id=NEW.id ;
            loop
              fetch ana_cur into ana_rec ;
              exit when not found ;
              anaprofit = coalesce(ana_rec.analysis_revenue,0) - coalesce(ana_rec.analysis_cost) ;
              if coalesce(ana_rec.analysis_revenue,0) > 0 then
                 anaprofitrate = round((anaprofit::numeric/ana_rec.analysis_revenue::numeric)*100::numeric,2) ;
              else
                 anaprofitrate = 0 ;
              end if ;   
              update neweb_projanalysis set analysis_profit=anaprofit,analysis_profitrate=anaprofitrate where id = ana_rec.id ;
            end loop ;
            close ana_cur ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_on_neweb_project on neweb_project ;""")
        self._cr.execute("""create trigger update_on_neweb_project after update on neweb_project
                                         for each row execute procedure recal_profit();""")

        self._cr.execute("""drop function if exists genprojchiprodno1(sitemid int) cascade""")
        self._cr.execute("""create or replace function genprojchiprodno1(sitemid int) returns void as $BODY$
          DECLARE
            code_len int ;
            myyear varchar ;
            myyear1 varchar ;
            mysname varchar ;
            mychiseq int ;
            mychiseqid int ;
            ncount int ;
            ncount1 int ;
            mychiprodcode varchar ;
            proj_cur refcursor ;
            proj_rec record ;
            mysnamelen int ;
            descpid int ;
          BEGIN
            select max(id) into descpid from neweb_costtype where name ilike '%說明%' ;
            open proj_cur for select id,prod_set,create_date,cost_type from neweb_projsaleitem where id=sitemid and chi_product_no is null and 
                 not_chiout != True and prod_set is not null and create_date is not null  ;
            loop
                fetch proj_cur into proj_rec ;
                exit when not found ;
                if proj_rec.cost_type=3 then   /* 建置 */
                   update neweb_projsaleitem set chi_product_no='ZZC00000001' where id = proj_rec.id ;
                elsif proj_rec.cost_type=2 then   /* 專案合作 */
                   update neweb_projsaleitem set chi_product_no='ZZA00000001' where id = proj_rec.id ;
                elsif proj_rec.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                   update neweb_projsaleitem set chi_product_no='ZZB00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=5 then   /* 維運人力 */
                   update neweb_projsaleitem set chi_product_no='ZZD00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=7 then   /* 租賃 */
                   update neweb_projsaleitem set chi_product_no='ZZE00000001' where id = proj_rec.id ;   
                elsif proj_rec.cost_type=11 then   /* 行銷獎勵 */
                   update neweb_projsaleitem set chi_product_no='ZZG00000001' where id = proj_rec.id ; 
                elsif proj_rec.cost_type in (6,8) then   /* 利息,其他 */
                   update neweb_projsaleitem set chi_product_no='ZZH00000001' where id = proj_rec.id ; 
                elsif proj_rec.cost_type=12 then   /* 保固維護 */
                   update neweb_projsaleitem set chi_product_no='ZZW00000001' where id = proj_rec.id ;
                elsif proj_rec.cost_type=descpid then   /* 說明*/ 
                   update neweb_projsaleitem set chi_product_no='ZZI00000001' where id = proj_rec.id ;         
                else
                   select date_part('year',proj_rec.create_date::DATE)::TEXT into myyear ;
                   select substring(myyear,3,2) into myyear1 ;
                   select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                   select length(mysname) into code_len ;
                   select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                   if ncount > 0 then
                      select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                      select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                      update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                      update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                   else
                      select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                      update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                      insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                   end if ; 
                end if ;   
            end loop ;
            close proj_cur ;  
            open proj_cur for select id,prod_set,create_date,chi_product_no,cost_type from neweb_projsaleitem where id=sitemid and prod_set is not null and create_date is not null
                and not_chiout != True  ;
            loop
              fetch proj_cur into proj_rec ;
              exit when not found ;
              if proj_rec.cost_type=3 then
                  update neweb_projsaleitem set chi_product_no='ZZC00000001' where id = proj_rec.id and chi_product_no != 'ZZC00000001' ;
              elsif proj_rec.cost_type=2 then   /* 專案合作 */
                   update neweb_projsaleitem set chi_product_no='ZZA00000001' where id = proj_rec.id and chi_product_no != 'ZZA00000001';
              elsif proj_rec.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                  update neweb_projsaleitem set chi_product_no='ZZB00000001' where id = proj_rec.id and chi_product_no != 'ZZB00000001' ;   
              elsif proj_rec.cost_type=5 then   /* 維運人力 */
                  update neweb_projsaleitem set chi_product_no='ZZD00000001' where id = proj_rec.id and chi_product_no != 'ZZD00000001' ;   
              elsif proj_rec.cost_type=7 then   /* 租賃 */
                  update neweb_projsaleitem set chi_product_no='ZZE00000001' where id = proj_rec.id and chi_product_no != 'ZZE00000001' ;   
              elsif proj_rec.cost_type=11 then   /* 行銷獎勵 */
                  update neweb_projsaleitem set chi_product_no='ZZG00000001' where id = proj_rec.id and chi_product_no != 'ZZG00000001' ; 
              elsif proj_rec.cost_type in (6,8) then   /* 利息,其他 */
                  update neweb_projsaleitem set chi_product_no='ZZH00000001' where id = proj_rec.id and chi_product_no != 'ZZH00000001' ;    
              elsif proj_rec.cost_type=12 then   /* 保固維護 */
                   update neweb_projsaleitem set chi_product_no='ZZW00000001' where id = proj_rec.id and chi_product_no != 'ZZW00000001' ;   
              elsif proj_rec.cost_type=descpid then   /* 說明*/ 
                   update neweb_projsaleitem set chi_product_no='ZZI00000001' where id = proj_rec.id and chi_product_no != 'ZZI00000001' ;       
              else
                 select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                 select length(trim(mysname)) into mysnamelen ;
                 if mysnamelen > 0 and substring(proj_rec.chi_product_no,1,mysnamelen) != mysname then
                    select date_part('year',proj_rec.create_date::DATE)::TEXT into myyear ;
                    select substring(myyear,3,2) into myyear1 ;
                    select sname into mysname from neweb_prodset where id = proj_rec.prod_set ;
                    select length(mysname) into code_len ;
                    select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                    if ncount > 0 then
                       select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                       select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                       update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                    else
                       select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       update neweb_projsaleitem set chi_product_no=mychiprodcode where id = proj_rec.id ;
                       insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                    end if ; 
                 end if ;
              end if ;   
            end loop ;
            close proj_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists regen_projsaleitem_prodno() cascade""")
        self._cr.execute("""create  or replace function regen_projsaleitem_prodno() returns trigger as $BODY$
          DECLARE
            code_len int ;
            myyear varchar ;
            myyear1 varchar ;
            mysname varchar ;
            mychiseq int ;
            mychiseqid int ;
            ncount int ;
            ncount1 int ;
            mychiprodcode varchar ;
            mysnamelen int ;
            descpid int ;
          BEGIN
              select max(id) into descpid from neweb_costtype where name ilike '%說明%' ;
              if NEW.cost_type=3 then  /* 建置 */
                  NEW.chi_product_no='ZZC00000001' ; 
              elsif NEW.cost_type=2 then   /* 專案合作 */
                  NEW.chi_product_no='ZZA00000001' ; 
              elsif NEW.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                  NEW.chi_product_no='ZZB00000001' ;  
              elsif NEW.cost_type=5 then   /* 維運人力 */
                  NEW.chi_product_no='ZZD00000001' ;  
              elsif NEW.cost_type=7 then   /* 租賃 */
                  NEW.chi_product_no='ZZE00000001' ;  
              elsif NEW.cost_type=11 then   /* 行銷獎勵 */
                  NEW.chi_product_no='ZZG00000001' ; 
              elsif NEW.cost_type in (6,8) then   /* 利息,其他 */
                  NEW.chi_product_no='ZZH00000001' ;
              elsif NEW.cost_type = 12 then   /* 保固維護 */
                  NEW.chi_product_no='ZZW00000001' ;    
              elsif NEW.cost_type = descpid then   /* 說明 */ 
                  NEW.chi_product_no='ZZI00000001' ;  
              else
                 select sname into mysname from neweb_prodset where id = NEW.prod_set ;
                 select length(trim(mysname)) into mysnamelen ;
                 if mysnamelen > 0 and substring(NEW.chi_product_no,1,mysnamelen) != mysname then
                    select date_part('year',NEW.create_date::DATE)::TEXT into myyear ;
                    select substring(myyear,3,2) into myyear1 ;
                    select sname into mysname from neweb_prodset where id = NEW.prod_set ;
                    select length(mysname) into code_len ;
                    select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                    if ncount > 0 then
                       select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                       select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       NEW.chi_product_no = mychiprodcode ;
                       update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                    else
                       select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       NEW.chi_product_no = mychiprodcode ;
                       insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                    end if ; 
                 end if ;
              end if ; 
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_prodset_projsaleitem on neweb_projsaleitem""")
        self._cr.execute("""create trigger update_prodset_projsaleitem before update of prod_set on neweb_projsaleitem
                            for each row execute procedure regen_projsaleitem_prodno();""")

        self._cr.execute("""drop function if exists regen_setupcost() cascade""")
        self._cr.execute("""create  or replace function regen_setupcost() returns trigger as $BODY$
          DECLARE
            mysum float ;
          BEGIN
            mysum = coalesce(NEW.r6_revenue,0) + coalesce(NEW.nt_revenue,0) + coalesce(NEW.networking_revenue,0) + coalesce(NEW.pm_revenue,0) ;
            if mysum > 0 then
               NEW.r6_percent = round((coalesce(NEW.r6_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.nt_percent = round((coalesce(NEW.nt_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.networking_percent = round((coalesce(NEW.networking_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.pm_percent = round((coalesce(NEW.pm_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
            else
               NEW.r6_percent = 0.0 ;
               NEW.nt_percent = 0.0 ;
               NEW.networking_percent = 0.0 ;
               NEW.pm_percent = 0.0 ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_setupcost_r6 on neweb_setupcost_line""")
        self._cr.execute("""create trigger update_setupcost_r6 before update of r6_revenue on neweb_setupcost_line
                            for each row execute procedure regen_setupcost();""")

        self._cr.execute("""drop trigger if exists update_setupcost_nt on neweb_setupcost_line""")
        self._cr.execute("""create trigger update_setupcost_nt before update of nt_revenue on neweb_setupcost_line
                            for each row execute procedure regen_setupcost();""")

        self._cr.execute("""drop trigger if exists update_setupcost_networking on neweb_setupcost_line""")
        self._cr.execute("""create trigger update_setupcost_networking before update of networking_revenue on neweb_setupcost_line
                            for each row execute procedure regen_setupcost();""")

        self._cr.execute("""drop trigger if exists update_setupcost_pm on neweb_setupcost_line""")
        self._cr.execute("""create trigger update_setupcost_pm before update of pm_revenue on neweb_setupcost_line
                                    for each row execute procedure regen_setupcost();""")

        self._cr.execute("""drop function if exists regen_maincost() cascade""")
        self._cr.execute("""create  or replace function regen_maincost() returns trigger as $BODY$
          DECLARE
            mysum float ;
          BEGIN
            mysum = coalesce(NEW.r6_revenue,0) + coalesce(NEW.nt_revenue,0) + coalesce(NEW.networking_revenue,0) + coalesce(NEW.support_revenue,0)  ;
            if mysum > 0 then
               NEW.r6_percent = round((coalesce(NEW.r6_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.nt_percent = round((coalesce(NEW.nt_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.networking_percent = round((coalesce(NEW.networking_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
               NEW.support_percent = round((coalesce(NEW.support_revenue,0)::numeric/mysum::numeric) * 100 ,2) ;
            else
               NEW.r6_percent = 0.0 ;
               NEW.nt_percent = 0.0 ;
               NEW.networking_percent = 0.0 ;
               NEW.support_percent = 0.0 ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")



        self._cr.execute("""drop trigger if exists update_maincost_r6 on neweb_maincost_line""")
        self._cr.execute("""create trigger update_maincost_r6 before update of r6_revenue on neweb_maincost_line
                            for each row execute procedure regen_maincost();""")

        self._cr.execute("""drop trigger if exists update_maincost_nt on neweb_maincost_line""")
        self._cr.execute("""create trigger update_maincost_nt before update of nt_revenue on neweb_maincost_line
                            for each row execute procedure regen_maincost();""")

        self._cr.execute("""drop trigger if exists update_maincost_networking on neweb_maincost_line""")
        self._cr.execute("""create trigger update_maincost_networking before update of networking_revenue on neweb_maincost_line
                            for each row execute procedure regen_maincost();""")

        self._cr.execute("""drop trigger if exists update_maincost_support on neweb_maincost_line""")
        self._cr.execute("""create trigger update_maincost_support before update of support_revenue on neweb_maincost_line
                            for each row execute procedure regen_maincost();""")

        self._cr.execute("""drop function if exists regen_ownerman() cascade""")
        self._cr.execute("""create  or replace function regen_ownerman() returns trigger as $BODY$
          DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            nitem int ;
            empid int ;
          BEGIN
            update neweb_proj_eng_assign set owner_man1=null,owner_man2=null,owner_man3=null,owner_man4=null,owner_man5=null,owner_man6=null where id = NEW.neweb_proj_eng_assign_id ;
            nitem=1 ;
            open emp_cur for select * from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id=NEW.neweb_proj_eng_assign_id ;
            loop
              fetch emp_cur into emp_rec ;
              exit when not found ;
              select id into empid from hr_employee where user_id=emp_rec.res_users_id and active=True ; 
              if nitem = 1 then
                 update neweb_proj_eng_assign set owner_man1=empid where id = NEW.neweb_proj_eng_assign_id ;
              elsif nitem = 2 then
                 update neweb_proj_eng_assign set owner_man2=empid where id = NEW.neweb_proj_eng_assign_id ;
              elsif nitem = 3 then
                 update neweb_proj_eng_assign set owner_man3=empid where id = NEW.neweb_proj_eng_assign_id ;
              elsif nitem = 4 then
                 update neweb_proj_eng_assign set owner_man4=empid where id = NEW.neweb_proj_eng_assign_id ;
              elsif nitem = 5 then
                 update neweb_proj_eng_assign set owner_man5=empid where id = NEW.neweb_proj_eng_assign_id ;
              elsif nitem = 6 then
                 update neweb_proj_eng_assign set owner_man6=empid where id = NEW.neweb_proj_eng_assign_id ;
              end if ;
              nitem = nitem + 1 ;
            end loop ;
            close emp_cur ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_eng_assign_rel on neweb_ass_service_type_neweb_proj_eng_assign_rel""")
        self._cr.execute("""drop trigger if exists insert_eng_assign_rel on neweb_proj_eng_assign_res_users_rel""")
        self._cr.execute("""create trigger insert_eng_assign_rel after insert on neweb_proj_eng_assign_res_users_rel
                                    for each row execute procedure regen_ownerman();""")

        self._cr.execute("""drop function if exists genpartnertype() cascade""")
        self._cr.execute("""create  or replace function genpartnertype() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            if NEW.customer=True or NEW.customer_rank=1 then
               NEW.customer=True ;
               NEW.customer_rank=1 ;
            end if ;
            if NEW.supplier=True or NEW.supplier_rank=1 then
               NEW.supplier=True ;
               NEW.supplier_rank=1 ;
            end if ;
            return NEW;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpartnertype1() cascade""")
        self._cr.execute("""create  or replace function genpartnertype1() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            if NEW.customer=True  then
               NEW.customer_rank=1 ;
            else
               NEW.customer_rank=0 ;   
            end if ;
            return NEW;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpartnertype2() cascade""")
        self._cr.execute("""create  or replace function genpartnertype2() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            if NEW.supplier=True  then
               NEW.supplier_rank=1 ;
            else
               NEW.supplier_rank=0 ;   
            end if ;
            return NEW;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_res_partner_type on res_partner""")
        self._cr.execute("""create trigger insert_res_partner_type before insert on res_partner
                                            for each row execute procedure genpartnertype();""")

        self._cr.execute("""drop trigger if exists update_res_partner_type1 on res_partner""")
        self._cr.execute("""create trigger update_res_partner_type1 before update of customer on res_partner
                                                    for each row execute procedure genpartnertype1();""")

        self._cr.execute("""drop trigger if exists update_res_partner_type2 on res_partner""")
        self._cr.execute("""create trigger update_res_partner_type2 before update of supplier on res_partner
                                                            for each row execute procedure genpartnertype2();""")

        self._cr.execute("""drop function if exists genallpartnertype() cascade""")
        self._cr.execute("""create or replace function genallpartnertype() returns void as $BODY$
         DECLARE
           par_cur refcursor ;
           par_rec record ;
         BEGIN
           open par_cur for select id,customer_rank,supplier_rank from res_partner ;
           loop
             fetch par_cur into par_rec ;
             exit when not found ;
             if par_rec.customer_rank=1 then
                update res_partner set customer=True where id = par_rec.id ;
             else
                update res_partner set customer=False where id = par_rec.id ;
             end if ;
             if par_rec.supplier_rank=1 then
                update res_partner set supplier=True where id = par_rec.id ;
             else
                update res_partner set supplier=False where id = par_rec.id ;
             end if ;
           end loop ;
           close par_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists regen_projsaleitem_prodno1() cascade""")
        self._cr.execute("""create  or replace function regen_projsaleitem_prodno1() returns trigger as $BODY$
          DECLARE
            code_len int ;
            myyear varchar ;
            myyear1 varchar ;
            mysname varchar ;
            mychiseq int ;
            mychiseqid int ;
            ncount int ;
            ncount1 int ;
            mychiprodcode varchar ;
            mysnamelen int ;
            descpid int ;
          BEGIN
              select max(id) into descpid from neweb_costtype where name ilike '%說明%' ;
              if NEW.cost_type=3 then  /* 建置 */
                  NEW.chi_product_no='ZZC00000001' ; 
              elsif NEW.cost_type=2 then   /* 專案合作 */
                  NEW.chi_product_no='ZZA00000001' ; 
              elsif NEW.cost_type in (4,9) then   /* 維護舊約,維護新約 */
                  NEW.chi_product_no='ZZB00000001' ;  
              elsif NEW.cost_type=5 then   /* 維運人力 */
                  NEW.chi_product_no='ZZD00000001' ;  
              elsif NEW.cost_type=7 then   /* 租賃 */
                  NEW.chi_product_no='ZZE00000001' ;  
              elsif NEW.cost_type=11 then   /* 行銷獎勵 */
                  NEW.chi_product_no='ZZG00000001' ; 
              elsif NEW.cost_type in (6,8) then   /* 利息,其他 */
                  NEW.chi_product_no='ZZH00000001' ;
              elsif NEW.cost_type = 12 then   /* 保固維護 */
                  NEW.chi_product_no='ZZW00000001' ;    
              elsif NEW.cost_type = descpid then   /* 說明 */ 
                  NEW.chi_product_no='ZZI00000001' ;  
              else
                 select sname into mysname from neweb_prodset where id = NEW.prod_set ;
                 select length(trim(mysname)) into mysnamelen ;
                 if mysnamelen > 0 and substring(NEW.chi_product_no,1,mysnamelen) != mysname then
                    select date_part('year',NEW.create_date::DATE)::TEXT into myyear ;
                    select substring(myyear,3,2) into myyear1 ;
                    select sname into mysname from neweb_prodset where id = NEW.prod_set ;
                    select length(mysname) into code_len ;
                    select count(*) into ncount from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                    if ncount > 0 then
                       select id,chi_seq into mychiseqid,mychiseq from neweb_chi_invoicing_productset_seq where chi_year=myyear and chi_sname=mysname ;
                       select concat(mysname,myyear1,lpad(mychiseq::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       NEW.chi_product_no = mychiprodcode ;
                       update neweb_chi_invoicing_productset_seq set chi_seq=chi_seq + 1 where id =  mychiseqid ;
                    else
                       select concat(mysname,myyear1,lpad(1::TEXT,(11 - code_len - 2),'0')) into mychiprodcode ;
                       NEW.chi_product_no = mychiprodcode ;
                       insert into neweb_chi_invoicing_productset_seq(chi_year,chi_sname,chi_seq) values (myyear,mysname,2) ;
                    end if ; 
                 end if ;
              end if ; 
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_prodset_projsaleitem1 on neweb_projsaleitem""")
        self._cr.execute("""create trigger update_prodset_projsaleitem1 before update of cost_type on neweb_projsaleitem
                                    for each row execute procedure regen_projsaleitem_prodno1();""")

        self._cr.execute("""drop function if exists ins_open_account_day1() cascade""")
        self._cr.execute("""create  or replace function ins_open_account_day1() returns trigger as $BODY$
          DECLARE
            ncount int ;
            mymaxseq int ;
          BEGIN
            select max(day_seq) into mymaxseq from neweb_open_account_day1 ; 
            NEW.day_seq = coalesce(mymaxseq,0) + 1 ; 
            return NEW;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists insert_open_account_day1 on neweb_open_account_day1""")
        self._cr.execute("""create trigger insert_open_account_day1 before insert on neweb_open_account_day1
                                    for each row execute procedure ins_open_account_day1()""")

        self._cr.execute("""drop function if exists ins_so_openaccountday() cascade""")
        # self._cr.execute("""create  or replace function ins_so_openaccountday() returns trigger as $BODY$
        #   DECLARE
        #     ncount int ;
        #     mymaxseq int ;
        #   BEGIN
        #     if NEW.partner_id is not null then
        #     end if ;
        #     select max(day_seq) into mymaxseq from neweb_open_account_day1 ;
        #     NEW.day_seq = coalesce(mymaxseq,0) + 1 ;
        #     return NEW;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")
        #
        self._cr.execute("""drop trigger if exists ins_so_openaccountday on sale_order""")
        # self._cr.execute("""create trigger ins_so_openaccountday before insert on sale_order
        #                             for each row execute procedure ins_so_openaccountday()""")

        self._cr.execute("""drop function if exists update_proj_openaccountday1() cascade""")
        self._cr.execute("""create  or replace function update_proj_openaccountday1() returns trigger as $BODY$
         DECLARE
           sday1 int ;
           pday1 int ;
         BEGIN
           select open_account_day1 into sday1 from sale_order where name=NEW.sale_no ;
           if NEW.open_account_day1 != sday1 then
              update sale_order set open_account_day1=NEW.open_account_day1 where name = NEW.sale_no ;
           end if ;
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 針對每次更新 neweb.project open_account_day1 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_proj_openaccountday1 on neweb_project ;""")
        self._cr.execute("""create trigger update_proj_openaccountday1 after update of open_account_day1 on neweb_project
                                                for each row execute procedure update_proj_openaccountday1();""")

        self._cr.execute("""drop function if exists update_proj_openaccountday2() cascade""")
        self._cr.execute("""create  or replace function update_proj_openaccountday2() returns trigger as $BODY$
         DECLARE
           sday2 int ;
           pday2 int ;
         BEGIN
           select open_account_day2 into sday2 from sale_order where name=NEW.sale_no ;
           if NEW.open_account_day2 != sday2 then
              update sale_order set open_account_day2=NEW.open_account_day2 where name = NEW.sale_no ;
           end if ;
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        # 針對每次更新 neweb.project open_account_day2 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_proj_openaccountday2 on neweb_project ;""")
        self._cr.execute("""create trigger update_proj_openaccountday2 after update of open_account_day2 on neweb_project
                                                        for each row execute procedure update_proj_openaccountday2();""")

        self._cr.execute("""drop function if exists update_on_setupdate() cascade""")
        self._cr.execute("""create  or replace function update_on_setupdate() returns trigger as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           if NEW.setup_date is not null then
              update neweb_proj_eng_assign set assign_man_date = NEW.setup_date where id = NEW.id and assign_man_date is null ;
           end if ;
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists update_on_setupdate on neweb_proj_eng_assign ;""")
        self._cr.execute("""create trigger update_on_setupdate after update of setup_date on neweb_proj_eng_assign
                                                 for each row execute procedure update_on_setupdate();""")

        self._cr.execute("""update neweb_proj_eng_assign set assign_man_date=setup_date where assign_man_date is null ;""")

