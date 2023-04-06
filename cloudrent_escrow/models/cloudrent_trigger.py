# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class cloudrentTrigger(models.Model):
    _name = "cloudrent.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_cloudrent_escrow() cascade""")
        self._cr.execute("""create  or replace function insert_cloudrent_escrow() returns trigger as $BODY$
          DECLARE
            ncount int ;
            maxseq int ;
            maxid int ;
            emetername varchar ;
            emeterhubid int ;
          BEGIN
            select max(sequence) into maxseq from crm_team where active=TRUE  ;
            if maxseq is null then
               maxseq = 10 ;
            else
               maxseq = maxseq  + 10 ;    
            end if ;
            select max(id) into maxid from mail_alias ;
            select count(*) into ncount from crm_team where name=NEW.bus_name ;
            if ncount = 0 then
               insert into crm_team (name,escrow_no,sequence,use_opportunities,active,alias_id) values (NEW.bus_name,NEW.id,maxseq,TRUE,TRUE,maxid) ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 cloudrent_escrow  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_cloudrent_escrow on cloudrent_escrow ;""")
        self._cr.execute("""create trigger insert_cloudrent_escrow  after insert on cloudrent_escrow
                                 for each row execute procedure insert_cloudrent_escrow();""")

        self._cr.execute("""drop function if exists update_cloudrent_escrow_busname() cascade""")
        self._cr.execute("""create  or replace function update_cloudrent_escrow_busname() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update crm_team set name = NEW.bus_name where escrow_no = NEW.id ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次變更 cloudrent_escrow bus_name 作動一次 trigger
        self._cr.execute("""drop trigger if exists update_cloudrent_escrow_busname on cloudrent_escrow ;""")
        self._cr.execute("""create trigger update_cloudrent_escrow_busname  after update of bus_name on cloudrent_escrow
                                         for each row execute procedure update_cloudrent_escrow_busname();""")

        self._cr.execute("""drop function if exists delete_cloudrent_escrow() cascade""")
        self._cr.execute("""create  or replace function delete_cloudrent_escrow() returns trigger as $BODY$
          DECLARE
            ncount int ;
          BEGIN
            update crm_team set active = FALSE where escrow_no = NEW.id ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次變更 cloudrent_escrow bus_name 作動一次 trigger
        self._cr.execute("""drop trigger if exists delete_cloudrent_escrow on cloudrent_escrow ;""")
        self._cr.execute("""create trigger delete_cloudrent_escrow  before delete on cloudrent_escrow
                                                 for each row execute procedure delete_cloudrent_escrow();""")

        self._cr.execute("""drop function if exists update_crm_lead_stage() cascade""")
        self._cr.execute("""create  or replace function update_crm_lead_stage() returns trigger as $BODY$
          DECLARE
            ncount int ;
            nseq int ;
          BEGIN
            select sequence into nseq from crm_stage where id = NEW.stage_id ;
            if nseq = 999 then
               NEW.probability = 0 ;
            end if ;
            if nseq = 10 then
               NEW.probability = 10 ;
            end if ;
            if nseq = 20 then
               NEW.probability = 20 ;
            end if ;
            if nseq = 30 then
               NEW.probability = 30 ;
            end if ;
            if nseq = 40 then
               NEW.probability = 40 ;
            end if ;
            if nseq = 50 then
               NEW.probability = 50 ;
            end if ;
            if nseq = 60 then
               NEW.probability = 70 ;
            end if ;
            if nseq = 70 then
               NEW.probability = 100 ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_crm_lead_stage on crm_lead ;""")
        self._cr.execute("""create trigger update_crm_lead_stage  before update of stage_id on crm_lead
                                                         for each row execute procedure update_crm_lead_stage();""")

        self._cr.execute("""drop function if exists ins_contract_match() cascade""")
        self._cr.execute("""create  or replace function ins_contract_match() returns trigger as $BODY$
         DECLARE
           itemkey int ;
           grantid int ;
           gfreq char ;
           gtime int ;
           gvalue int ;
           nseq int ;
           startdate date ;
           cyear varchar ;
           cmonth varchar ;
           cym varchar ;
           maxseq int ;
           weekseq int ;
         BEGIN
           
           /* 生成 居家安全保險費 itemkey=1 */
          /* itemkey = 1 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
              coalesce(admin_area,NEW.admin_area)=NEW.admin_area and coalesce(lessor_type,NEW.case_type)=NEW.case_type and 
              coalesce(lessee_type,NEW.lessee_type)=NEW.lessee_type ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',NEW.match_start_date)::TEXT into cyear ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_safe_insurance_fee(safe_id,safe_seq,ins_applyfor_year,ins_applyfor_fee) values (NEW.id,1,cyear,gvalue) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 select date_part('year',startdate)::TEXT into cyear ;
                 select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                 cym = concat(cyear,'-',cmonth) ;
                 loop
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_safe_insurance_fee(safe_id,safe_seq,ins_applyfor_year,ins_applyfor_fee) values (NEW.id,nseq,cym,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   cym = concat(cyear,'-',cmonth) ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 select date_part('year',startdate)::TEXT into cyear ;
                 loop
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_safe_insurance_fee(safe_id,safe_seq,ins_applyfor_year,ins_applyfor_fee) values (NEW.id,nseq,cyear,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                 end loop ;
              end if ;
           end if ;   */
           
           /* 生成 公證費 itemkey=2 */
           itemkey = 2 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=NEW.admin_area ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',NEW.match_start_date)::TEXT into cyear ;
              select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (NEW.id,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (NEW.id,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (NEW.id,nseq,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ;
           
            /* 生成 修繕費 itemkey=3 */
          /* itemkey = 3 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
              coalesce(admin_area,NEW.admin_area)=NEW.admin_area and coalesce(lessor_type,NEW.case_type)=NEW.case_type and 
              coalesce(lessee_type,NEW.lessee_type)=NEW.lessee_type ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',NEW.match_start_date)::TEXT into cyear ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_repair_fee(repair_id,repair_seq,repair_year,repair_applyfor_fee) values (NEW.id,1,cyear,gvalue) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_repair_fee(repair_id,repair_seq,repair_year,repair_applyfor_fee) values (NEW.id,nseq,cyear,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_repair_fee(repair_id,repair_seq,repair_year,repair_applyfor_fee) values (NEW.id,nseq,cyear,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                 end loop ;
              end if ;
           end if ; */
           
           /* 生成 租金補助 itemkey=4 */
           itemkey = 4 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
              admin_area=NEW.admin_area and lessor_type=NEW.case_type and lessee_type=NEW.lessee_type ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',NEW.match_start_date)::TEXT into cyear ;
              select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (NEW.id,1,NEW.build_contract_rent,NEW.lessee_grant,1,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 cym = concat(cyear,'-',cmonth) ;
                 loop
                  select date_part('year',startdate)::TEXT into cyear ;
                  select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date or nseq > 12 ;
                   insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (NEW.id,nseq,NEW.build_contract_rent,NEW.lessee_grant,nseq,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (NEW.id,nseq,NEW.build_contract_rent,NEW.lessee_grant,nseq,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                 end loop ;
              end if ;
              select max(rent_seq) into maxseq from cloudrent_grant_rent where grant_id=NEW.id ;
              update cloudrent_grant_rent set tot_rent_period=maxseq where grant_id=NEW.id ;
           end if ;   
           
           /* 生成 開發費 itemkey=5 */
           itemkey = 5 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=NEW.admin_area  ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              if gfreq='1' then       /* By件 */
                 select date_part('year',NEW.match_start_date)::TEXT into cyear ;
                 select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
                 insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (NEW.id,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (NEW.id,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (NEW.id,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ;   
           if NEW.case_type='1' then
              /* 生成 包管費 itemkey=6 */
               itemkey = 6 ;
               select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
                  admin_area=NEW.admin_area  ;
               if grantid is not null then
                  select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
                  if gtime=-1 then
                     gtime=10000 ;
                  end if ;
                  if gfreq='1' then       /* By件 */
                     select date_part('year',NEW.match_start_date)::TEXT into cyear ;
                     select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
                     insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (NEW.id,1,gvalue,1,cyear,cmonth) ;
                  elsif gfreq='2' then    /* By月 */
                     nseq = 1 ;
                     startdate = NEW.match_start_date ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > NEW.match_end_date ;
                       insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (NEW.id,nseq,gvalue,nseq,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 month' ;
                     end loop ;
                  else                    /* By年 */  
                     nseq = 1 ;
                     startdate = NEW.match_start_date ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > NEW.match_end_date ;
                       insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (NEW.id,nseq,gvalue,nseq,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 year' ;
                     end loop ;
                  end if ;
                  select max(guarantee_seq) into maxseq from cloudrent_guarantee_fee where guarantee_id=NEW.id ;
                  update cloudrent_guarantee_fee set guarantee_tot_period=maxseq where guarantee_id=NEW.id ;
               end if ;   
           else
               /* 生成 代管費 itemkey=8 */
               itemkey = 8 ;
               select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=NEW.admin_area  ;
               if grantid is not null then
                  select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
                  if gtime=-1 then
                     gtime=10000 ;
                  end if ;
                  if gfreq='1' then       /* By件 */
                     select date_part('year',NEW.match_start_date)::TEXT into cyear ;
                     select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
                     insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values (NEW.id,1,1,gvalue,cyear,cmonth) ;
                  elsif gfreq='2' then    /* By月 */
                     nseq = 1 ;
                     startdate = NEW.match_start_date ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > NEW.match_end_date ;
                       insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values (NEW.id,nseq,nseq,gvalue,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 month' ;
                     end loop ;
                  else                    /* By年 */  
                     nseq = 1 ;
                     startdate = NEW.match_start_date ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > NEW.match_end_date ;
                       insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values (NEW.id,nseq,nseq,gvalue,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 year' ;
                     end loop ;
                  end if ;
                  select max(escrow_seq) into maxseq from cloudrent_escrow_fee where escrow_id=NEW.id ;
                  update cloudrent_escrow_fee set escrow_tot_period=maxseq where escrow_id=NEW.id ;
               end if ; 
           end if ;
           
           /* 生成 媒合費 itemkey=7 */
           itemkey = 7 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=NEW.admin_area  ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              if gfreq='1' then       /* By件 */
                 select date_part('year',NEW.match_start_date)::TEXT into cyear ;
                 select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
                 insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,match_applyfor_month) values (NEW.id,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,match_applyfor_month) values (NEW.id,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = NEW.match_start_date ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > NEW.match_end_date ;
                   insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,macth_applyfor_month) values (NEW.id,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ; 
           if NEW.match_start_date is not null then
              select date_part('week',NEW.match_start_date)::INT into weekseq ;
              select date_part('year',NEW.match_start_date)::TEXT into cyear ;
              select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into cmonth ;
              update cloudrent_contract_match set week_seq=weekseq,match_year=cyear,match_month=cmonth where id = NEW.id ; 
           end if ;    
           return NEW ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_contract_match on cloudrent_contract_match ;""")
        self._cr.execute("""create trigger ins_contract_match after insert on cloudrent_contract_match
                                                         for each row execute procedure ins_contract_match()""")

        self._cr.execute("""drop function if exists update_match_sdate() cascade""")
        self._cr.execute("""create  or replace function update_match_sdate() returns trigger as $BODY$
          DECLARE
            weekseq int ;
            matchyear varchar ;
            matchmonth varchar ;
          BEGIN
            if NEW.match_start_date is not null then
               select date_part('week',NEW.match_start_date)::INT into weekseq ;
               select date_part('year',NEW.match_start_date)::TEXT into matchyear ;
               select lpad(date_part('month',NEW.match_start_date)::TEXT,2,'0') into matchmonth ;
               NEW.week_seq = weekseq ;
               NEW.match_year = matchyear ;
               NEW.match_month = matchmonth ;
            end if ;
            return NEW ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_match_sdate on cloudrent_contract_match ;""")
        self._cr.execute("""create trigger update_match_sdate before update of match_start_date on cloudrent_contract_match
                                                        for each row execute procedure update_match_sdate()""")

        self._cr.execute("""drop function if exists ins_lessor_doc_line() cascade""")
        # self._cr.execute("""create  or replace function ins_lessor_doc_line() returns trigger as $BODY$
        #   DECLARE
        #     escrowid int ;
        #     myname varchar ;
        #     buildno int ;
        #     buildlessor int ;
        #     buildlessee int ;
        #     myfilename varchar ;
        #     escrowman varchar ;
        #     maxid int ;
        #   BEGIN
        #     select escrow_agent,build_no1,build_lessor,build_lessee into escrowid,buildno,buildlessor,buildlessee from crm_lead where id = NEW.doc_id ;
        #     if NEW.doc_type='1' then     /* 出租人出租住宅申請書(代管) A2 */
        #        select get_cloudrent_seqno(escrowid,'A2') into myname ;
        #        select escrow_man into escrowman from ccloudrent_escrow_member where id = buildlessor ;
        #        myfilename = concat('出租人出租住宅申請書(代管)-',escrowman) ;
        #        insert into cloudrent_applyfor_escrow1(name,build_no,lessor_no,escrow_no,applyfor_filename,applyfor_attach,leadid,doclineid)
        #          values (myname,buildno,buildlessor,escrowid,myfilename,NEW.doc_file,NEW.doc_id,NEW.id) ;
        #        select max(id) into maxid from cloudrent_applyfor_escrow1 ;
        #     elsif NEW.doc_type='2' then  /* 出租人出租住宅申請書(包租) A3 */
        #        select get_cloudrent_seqno(escrowid,'A3') into myname ;
        #        select escrow_man into escrowman from ccloudrent_escrow_member where id = buildlessor ;
        #        myfilename = concat('出租人出租住宅申請書(包租)-',escrowman) ;
        #        insert into cloudrent_applyfor_escrow2(name,build_no,lessor_no,escrow_no,applyfor_filename,applyfor_attach,leadid,doclineid)
        #          values (myname,buildno,buildlessor,escrowid,myfilename,NEW.doc_file,NEW.doc_id,NEW.id) ;
        #        select max(id) into maxid from cloudrent_applyfor_escrow2 ;
        #     elsif NEW.doc_type='3' then  /* 民眾(房客)承租住宅申請書(代管) A4 */
        #        select get_cloudrent_seqno(escrowid,'A4') into myname ;
        #        select escrow_man into escrowman from ccloudrent_escrow_member where id = buildlessee ;
        #        myfilename = concat('民眾(房客)承租住宅申請書(代管)-',escrowman) ;
        #        insert into cloudrent_applyfor_escrow3(name,lessee_no,escrow_no,applyfor_filename,applyfor_attach,leadid,doclineid) values
        #         (myname,buildlessee,escrowid,myfilename,NEW.doc_file,NEW.doc_id,NEW.id) ;
        #        select max(id) into maxid from cloudrent_applyfor_escrow3 ;
        #     else                         /* 民眾(房客)承租住宅申請書(包租) A5 */
        #        select get_cloudrent_seqno(escrowid,'A5') into myname ;
        #        select escrow_man into escrowman from ccloudrent_escrow_member where id = buildlessee ;
        #        myfilename = concat('民眾(房客)承租住宅申請書(包管)-',escrowman) ;
        #        insert into cloudrent_applyfor_escrow3(name,lessee_no,escrow_no,applyfor_filename,applyfor_attach,leadid,doclineid) values
        #         (myname,buildlessee,escrowid,myfilename,NEW.doc_file,NEW.doc_id,NEW.id) ;
        #         select max(id) into maxid from cloudrent_applyfor_escrow4 ;
        #     end if ;
        #     update cloudrent_lessor_doc_line set doc_applyfor_id=maxid where id=NEW.id ;
        #     return NEW ;
        #   END;$BODY$
        #   LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists ins_lessor_doc_line on cloudrent_lessor_doc_line ;""")
        # self._cr.execute("""create trigger ins_lessor_doc_line after insert on cloudrent_lessor_doc_line
        #                                                 for each row execute procedure ins_lessor_doc_line()""")

        self._cr.execute("""drop function if exists ins_safe_insurance() cascade""")
        self._cr.execute("""create  or replace function ins_safe_insurance() returns trigger as $BODY$
          DECLARE
            msd date ;
            med date ;
            sy varchar ;
            ey varchar ;
            sm varchar ;
            em varchar ;
          BEGIN
            select match_start_date,match_end_date into msd,med from cloudrent_contract_match where id = NEW.safe_id ;
            select date_part('year',msd)::TEXT into sy ; 
            select date_part('year',med)::TEXT into ey ;
            select date_part('month',msd)::TEXT into sm ;
            select date_part('month',med)::TEXT into em ;
            if NEW.ins_applyfor_year::INT < sy::INT or NEW.ins_applyfor_year::INT > ey::INT then
               raise info 'ERROR' ;
               return NULL ;
            elsif NEW.ins_applyfor_year::INT >= ey::INT and NEW.ins_applyfor_month::INT > em::INT then
               raise info 'ERROR1' ;
               return NULL ;
            else
               return NEW ;
            end if ; 
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists ins_safe_insurance on cloudrent_safe_insurance_fee ;""")
        #self._cr.execute("""create trigger ins_safe_insurance before insert on cloudrent_safe_insurance_fee
        #                                                for each row execute procedure ins_safe_insurance()""")


        self._cr.execute("""drop function if exists ins_visit_calendar() cascade""")
        self._cr.execute("""create or replace function ins_visit_calendar() returns trigger as $BODY$
         DECLARE
            ncount int ;
         BEGIN
            select count(*) into ncount from cloudrent_agent_visit_service where calendar_id=NEW.id ;
            if ncount = 0 then
               insert into cloudrent_agent_visit_service(escrow_no,member_no,match_no,visit_start_date,visit_end_date,state,calendar_id) values 
                  (NEW.escrow_no,NEW.member_no,NEW.match_no,NEW.visit_start_date,NEW.visit_end_date,NEW.state,NEW.id) ;
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_visit_calendar on cloudrent_visit_calendar ;""")
        self._cr.execute("""create trigger ins_visit_calendar after insert on cloudrent_visit_calendar
                                                       for each row execute procedure ins_visit_calendar()""")


        self._cr.execute("""drop function if exists ins_agent_visit_service() cascade""")
        self._cr.execute("""create or replace function ins_agent_visit_service() returns trigger as $BODY$
         DECLARE
            ncount int ;
            cmonth varchar ;
         BEGIN
            select lpad(date_part('month',NEW.visit_start_date)::TEXT,2,'0') into cmonth ;
            if cmonth in ('01','02','03') then
               update cloudrent_contract_match set lessee_visit=NEW.visit_start_date::DATE where id = NEW.match_no;
            elsif cmonth in ('04','05','06') then
               update cloudrent_contract_match set lessee_visit1=NEW.visit_start_date::DATE where id = NEW.match_no;
            elsif cmonth in ('07','08','09') then
               update cloudrent_contract_match set lessee_visit2=NEW.visit_start_date::DATE where id = NEW.match_no;
            else
               update cloudrent_contract_match set lessee_visit3=NEW.visit_start_date::DATE where id = NEW.match_no;
            end if ;
            /*select count(*) into ncount from cloudrent_visit_calendar where visit_id=NEW.id ;
            if ncount = 0 then
               insert into cloudrent_visit_calendar(escrow_no,member_no,match_no,visit_start_date,visit_end_date,state,visit_id) values 
                  (NEW.escrow_no,NEW.member_no,NEW.match_no,NEW.visit_start_date,NEW.visit_end_date,NEW.state,NEW.id) ;
            end if ;*/
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists ins_agent_visit_service on cloudrent_agent_visit_service ;""")
        self._cr.execute("""create trigger ins_agent_visit_service after insert on cloudrent_agent_visit_service
                                                   for each row execute procedure ins_agent_visit_service()""")

        self._cr.execute("""drop function if exists update_state_visit_service() cascade""")
        self._cr.execute("""create or replace function update_state_visit_service() returns trigger as $BODY$
         DECLARE
            ncount int ;
         BEGIN
            select count(*) into ncount from cloudrent_visit_calendar where visit_id=NEW.id ;
            if ncount > 0 then
               update cloudrent_visit_calendar set state=NEW.state where visit_id=NEW.id ;
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_state_visit_service on cloudrent_agent_visit_service ;""")
        self._cr.execute("""create trigger update_state_visit_service after update of state on cloudrent_agent_visit_service
                                                           for each row execute procedure update_state_visit_service()""")

        self._cr.execute("""drop function if exists ins_lessee_sitecheck() cascade""")
        self._cr.execute("""create or replace function ins_lessee_sitecheck() returns trigger as $BODY$
         DECLARE
            ncount int ;
         BEGIN
            select count(*) into ncount from cloudrent_lessee_deposit_line where deposit_id=NEW.lessee_id and deposit_name=NEW.lessee_name  ;
            if ncount = 0 and NEW.rent_success = TRUE then
               insert into cloudrent_lessee_deposit_line(deposit_id,deposit_name) values (NEW.lessee_id,NEW.lessee_name) ;
               update crm_lead set lessee_name=NEW.lessee_name,lessee_pid=NEW.lessee_pid where id=NEW.lessee_id ;
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_lessee_sitecheck on cloudrent_lessee_sitecheck ;""")
        self._cr.execute("""create trigger ins_lessee_sitecheck after insert on cloudrent_lessee_sitecheck
                                                   for each row execute procedure ins_lessee_sitecheck()""")

        self._cr.execute("""drop function if exists update_sitecheck_success() cascade""")
        self._cr.execute("""create or replace function update_sitecheck_success() returns trigger as $BODY$
         DECLARE
            ncount int ;
         BEGIN
            if NEW.rent_success = TRUE then
               select count(*) into ncount from cloudrent_lessee_deposit_line where deposit_id=NEW.lessee_id and deposit_name=NEW.lessee_name  ;
               if ncount = 0 then
                  insert into cloudrent_lessee_deposit_line(deposit_id,deposit_name) values (NEW.lessee_id,NEW.lessee_name) ;  
               end if ;   
               update crm_lead set lessee_name=NEW.lessee_name,lessee_pid=NEW.lessee_pid where id=NEW.lessee_id ;
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists update_sitecheck_success on cloudrent_lessee_sitecheck ;""")
        self._cr.execute("""create trigger update_sitecheck_success after update of rent_success on cloudrent_lessee_sitecheck
                                                           for each row execute procedure update_sitecheck_success()""")

        self._cr.execute("""drop function if exists ins_visit_date() cascade""")
        self._cr.execute("""create or replace function ins_visit_date() returns trigger as $BODY$
         DECLARE
            cy varchar ; 
            cm varchar ;
         BEGIN
            if NEW.visit_start_date is not null then
               select date_part('year',NEW.visit_start_date)::TEXT into NEW.visit_year ;
               select lpad(date_part('month',NEW.visit_start_date)::TEXT,2,'0')::TEXT into NEW.visit_month ; 
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_visit_date on cloudrent_agent_visit_service ;""")
        self._cr.execute("""create trigger ins_visit_date before insert on cloudrent_agent_visit_service
                            for each row execute procedure ins_visit_date()""")

        self._cr.execute("""drop function if exists ins_quit_date() cascade""")
        self._cr.execute("""create or replace function ins_quit_date() returns trigger as $BODY$
         DECLARE
            cy varchar ; 
            cm varchar ;
         BEGIN
            if NEW.quit_date is not null then
               select date_part('year',NEW.quit_date)::TEXT into NEW.quit_year ;
               select lpad(date_part('month',NEW.quit_date)::TEXT,2,'0')::TEXT into NEW.quit_month ; 
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_quit_date on cloudrent_quit_lease ;""")
        self._cr.execute("""create trigger ins_quit_date before insert on cloudrent_quit_lease
                                    for each row execute procedure ins_quit_date()""")

        self._cr.execute("""drop function if exists after_ins_quit_lease() cascade""")
        self._cr.execute("""create or replace function after_ins_quit_lease() returns trigger as $BODY$
         DECLARE
            renewid1 int ;
            renewid2 int ;
            e_cur refcursor ;
            e_rec record ;
            objno int ;
         BEGIN
            select renew1,object_no1 into renewid1,objno from cloudrent_contract_match where id = NEW.match_no ;
            if renewid1 is not null then
               update cloudrent_contract_match set match_status='2',quit_date=NEW.quit_date,quit_line=NEW.id where id = renewid1 ;
               select renew1 into renewid2 from cloudrent_contract_match where id = renewid1 ; 
               if renewid2 is not null then
                  update cloudrent_contract_match set match_status='2',quit_date=NEW.quit_date,quit_line=NEW.id where id = renewid2 ;
               end if ;
            end if ;
            update cloudrent_contract_match set match_status='2',quit_date=NEW.quit_date,quit_line=NEW.id where id = NEW.match_no ;
            if objno is not null then
               open e_cur for select * from cloudrent_build_equip_part where equip_id=objno order by id;
               loop
                  fetch e_cur into e_rec ;
                  exit when not found ;
                  insert into cloudrent_quit_equip_part(equip_id,equip_categ,equip_no,equip_qty,equip_status,equip_image1,equip_image2,equip_image3) values
                   (NEW.id,e_rec.equip_categ,e_rec.equip_no,e_rec.equip_qty,e_rec.equip_status,e_rec.equip_image1,e_rec.equip_image2,e_rec.equip_image3) ;
               end loop ;
               close e_cur ;
            end if ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists after_ins_quit_lease on cloudrent_quit_lease ;""")
        self._cr.execute("""create trigger after_ins_quit_lease after insert on cloudrent_quit_lease
                                            for each row execute procedure after_ins_quit_lease()""")

        self._cr.execute("""drop function if exists before_del_quit_lease() cascade""")
        self._cr.execute("""create or replace function before_del_quit_lease() returns trigger as $BODY$
         DECLARE
            renewid1 int ;
            renewid2 int ;
         BEGIN
            select renew1 into renewid1 from cloudrent_contract_match where id = OLD.match_no ;
            if renewid1 is not null then
               update cloudrent_contract_match set match_status='1',quit_date=null,quit_line=null where id = renewid1 ;
               select renew1 into renewid2 from cloudrent_contract_match where id = renewid1 ; 
               if renewid2 is not null then
                  update cloudrent_contract_match set match_status='1',quit_date=null,quit_line=null where id = renewid2 ;
               end if ;
            end if ;
            update cloudrent_contract_match set match_status='1',quit_date=null,quit_line=null where id = OLD.match_no ;
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop trigger if exists before_del_quit_lease on cloudrent_quit_lease ;""")
        self._cr.execute("""create trigger before_del_quit_lease before delete on cloudrent_quit_lease
                                            for each row execute procedure before_del_quit_lease()""")

        self._cr.execute("""drop function if exists ins_lessor_doc_line() cascade""")
        # self._cr.execute("""create or replace function ins_lessor_doc_line() returns trigger as $BODY$
        #  DECLARE
        #     nid int ;
        #  BEGIN
        #     NEW.doc_seq = NEW.doc_name ;
        #     return NEW ;
        #  END;$BODY$
        #  LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_lessor_doc_line on cloudrent_lessor_doc_line ;""")
        # self._cr.execute("""create trigger ins_lessor_doc_line before insert on cloudrent_lessor_doc_line
        #                                     for each row execute procedure ins_lessor_doc_line()""")

        self._cr.execute("""drop function if exists ins_sitecheck_pic_line() cascade""")
        self._cr.execute("""create or replace function ins_sitecheck_pic_line() returns trigger as $BODY$
         DECLARE
            seq int ;
         BEGIN
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,1,'1','門牌及大門') ;
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,2,'1','衛浴設備[馬桶/洗面盆/浴缸]') ;
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,3,'1','出入口及樓梯間') ;
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,4,'1','滅火器/獨立型偵煙器/火警警報器') ;  
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,5,'1','熱水器') ; 
            insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
             (NEW.id,6,'1','室內設備') ; 
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_sitecheck_pic_line on crm_lead ;""")
        self._cr.execute("""create trigger ins_sitecheck_pic_line after insert on crm_lead
                                            for each row execute procedure ins_sitecheck_pic_line()""")

        self._cr.execute("""drop function if exists ins_build_pic_line() cascade""")
        self._cr.execute("""create or replace function ins_build_pic_line() returns trigger as $BODY$
         DECLARE
            seq int ;
         BEGIN
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,1,'1','門牌及大門') ;
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,2,'1','衛浴設備[馬桶/洗面盆/浴缸]') ;
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,3,'1','出入口及樓梯間') ;
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,4,'1','滅火器/獨立型偵煙器/火警警報器') ;  
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,5,'1','熱水器') ; 
            insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
             (NEW.id,6,'1','室內設備') ; 
            return NEW ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists ins_build_pic_line on cloudrent_build ;""")
        self._cr.execute("""create trigger ins_build_pic_line after insert on cloudrent_build
                                            for each row execute procedure ins_build_pic_line()""")

        self._cr.execute("""drop function if exists before_ins_secretary_calendar() cascade""")
        self._cr.execute("""create or replace function before_ins_secretary_calendar() returns trigger as $BODY$
        DECLARE
           escrowtype char ;
        BEGIN
           select escrow_type into escrowtype from cloudrent_escrow_member where id = NEW.member_no ;
           if escrowtype='3' then
              NEW.assign_type='1' ;   /* 管理師 */
           elsif escrowtype='5' then
              NEW.assign_type='2' ;   /* 業務 */
           elsif escrowtype='6' then
              NEW.assign_type='3' ;   /* 修繕廠商 */
           end if ;
           if NEW.sec_start_date is not null then
              NEW.assign_date = NEW.sec_start_date ;
           else
              NEW.sec_start_date = current_timestamp ;
              NEW.sec_end_date = current_timestamp + interval '4 hour' ;
              NEW.assign_date = current_timestamp ;
           end if ;
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists before_ins_secretary_calendar on cloudrent_secretary_calendar ;""")
        self._cr.execute("""create trigger before_ins_secretary_calendar before insert on cloudrent_secretary_calendar
                                                                      for each row execute procedure before_ins_secretary_calendar()""")

        self._cr.execute("""drop function if exists after_ins_secretary_calendar() cascade""")
        self._cr.execute("""create or replace function after_ins_secretary_calendar() returns trigger as $BODY$
        DECLARE
           ncount int ;
           maxid int ;
           stageid int ;
        BEGIN
          if NEW.assign_type='1' then   /* 管理師行事曆  */
             insert into cloudrent_visit_calendar(subject,escrow_no,member_no,match_no,visit_start_date,visit_end_date,state,memo,sec_id,set_priority,assign_date) values 
              (NEW.subject,NEW.escrow_no,NEW.member_no,NEW.match_no,NEW.sec_start_date,NEW.sec_end_date,NEW.state,NEW.memo,NEW.id,NEW.set_priority,NEW.assign_date) ;
             select max(id) into maxid from cloudrent_visit_calendar ;
             update cloudrent_secretary_calendar set target_id=maxid where id = NEW.id ;
          elsif NEW.assign_type='2' then   /* 業務行事曆 */
             select id into stageid from crm_stage where sequence=10 ; /* 場勘 */
             insert into cloudrent_sale_calendar(subject,escrow_no,lead_start_date,lead_end_date,member_no,match_no,stage_id,set_priority,assign_date,state,sec_id) values
               (NEW.subject,NEW.escrow_no,NEW.sec_start_date,NEW.sec_end_date,NEW.member_no,NEW.match_no,stageid,NEW.set_priority,NEW.assign_date,NEW.state,NEW.id) ;
             select max(id) into maxid from cloudrent_sale_calendar ;
             update cloudrent_secretary_calendar set target_id=maxid where id = NEW.id ;
          elsif NEW.assign_type='3' then  /* 修繕廠商行事曆 */  
             insert into cloudrent_repair_calendar(subject,escrow_no,member_no,match_no,repair_start_date,repair_end_date,state,memo,sec_id,set_priority,assign_date) values 
              (NEW.subject,NEW.escrow_no,NEW.member_no,NEW.match_no,NEW.sec_start_date,NEW.sec_end_date,NEW.state,NEW.memo,NEW.id,NEW.set_priority,NEW.assign_date) ;
             select max(id) into maxid from cloudrent_repair_calendar ;
             update cloudrent_secretary_calendar set target_id=maxid where id = NEW.id ; 
          end if ;
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists after_ins_secretary_calendar on cloudrent_secretary_calendar ;""")
        self._cr.execute("""create trigger after_ins_secretary_calendar after insert on cloudrent_secretary_calendar
                                                              for each row execute procedure after_ins_secretary_calendar()""")

        self._cr.execute("""drop function if exists after_update_sale_calendar() cascade""")
        self._cr.execute("""create or replace function after_update_sale_calendar() returns trigger as $BODY$
        DECLARE
           ncount int ;
           secid int ;
           stageid int ;
           tag_cur refcursor ;
           tag_rec record ;
        BEGIN
           if NEW.state='2' then
              update cloudrent_secretary_calendar set state=NEW.state,process_start_date=NEW.process_start_date where id = NEW.sec_id ;
           elsif NEW.state='3' then
              update cloudrent_secretary_calendar set state=NEW.state,process_end_date=NEW.process_end_date,close_date=NEW.close_date where id = NEW.sec_id ;
           end if ;
           open tag_cur for select * from  saletag_sale_calendar_rel where sale_id=NEW.id ;
           loop 
             fetch tag_cur into tag_rec;
             exit when not found ;
             select count(*) into ncount from saletag_secretary_calendar_rel where secretary_id=NEW.sec_id and tag_id=tag_rec.tag_id ;
             if ncount = 0 then
                insert into saletag_secretary_calendar_rel(secretary_id,tag_id) values (NEW.sec_id,tag_rec.tag_id) ;
             end if ;
           end loop ;
           close tag_cur ;
           delete from saletag_secretary_calendar_rel where secretary_id=NEW.sec_id and 
              tag_id not in (select tag_id from saletag_sale_calendar_rel where sale_id=NEW.id) ;
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists after_update_sale_calendar on cloudrent_sale_calendar ;""")
        self._cr.execute("""create trigger after_update_sale_calendar after update of state on cloudrent_sale_calendar
                                                                      for each row execute procedure after_update_sale_calendar()""")

        self._cr.execute("""drop function if exists after_update_visit_calendar() cascade""")
        self._cr.execute("""create or replace function after_update_visit_calendar() returns trigger as $BODY$
        DECLARE
           ncount int ;
           secid int ;
           stageid int ;
           tag_cur refcursor ;
           tag_rec record ;
        BEGIN
           if NEW.state='2' then
              update cloudrent_secretary_calendar set state=NEW.state,process_start_date=NEW.process_start_date where id = NEW.sec_id ;
           elsif NEW.state='3' then
              update cloudrent_secretary_calendar set state=NEW.state,process_end_date=NEW.process_end_date,close_date=NEW.close_date where id = NEW.sec_id ;
           end if ;
           open tag_cur for select * from visittag_visit_calendar_rel where visit_id=NEW.id ;
           loop 
             fetch tag_cur into tag_rec;
             exit when not found ;
             select count(*) into ncount from visittag_secretary_calendar_rel where secretary_id=NEW.sec_id and tag_id=tag_rec.tag_id ;
             if ncount = 0 then
                insert into visittag_secretary_calendar_rel(secretary_id,tag_id) values (NEW.sec_id,tag_rec.tag_id) ;
             end if ;
           end loop ;
           close tag_cur ;
           delete from visittag_secretary_calendar_rel where secretary_id=NEW.sec_id and 
              tag_id not in (select tag_id from visittag_visit_calendar_rel where visit_id=NEW.id) ;
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists after_update_visit_calendar on cloudrent_visit_calendar ;""")
        self._cr.execute("""create trigger after_update_visit_calendar after update of state on cloudrent_visit_calendar
                                                      for each row execute procedure after_update_visit_calendar()""")

        self._cr.execute("""drop function if exists after_update_repair_calendar() cascade""")
        self._cr.execute("""create or replace function after_update_repair_calendar() returns trigger as $BODY$
        DECLARE
           ncount int ;
           secid int ;
           stageid int ;
           tag_cur refcursor ;
           tag_rec record ;
        BEGIN
           if NEW.state='2' then
              update cloudrent_secretary_calendar set state=NEW.state,process_start_date=NEW.process_start_date where id = NEW.sec_id ;
           elsif NEW.state='3' then
              update cloudrent_secretary_calendar set state=NEW.state,process_end_date=NEW.process_end_date,close_date=NEW.close_date where id = NEW.sec_id ;
           end if ;
           open tag_cur for select * from repairtag_repair_calendar_rel where repair_id=NEW.id ;
           loop 
             fetch tag_cur into tag_rec;
             exit when not found ;
             select count(*) into ncount from repairtag_secretary_calendar_rel where secretary_id=NEW.sec_id and tag_id=tag_rec.tag_id ;
             if ncount = 0 then
                insert into repairtag_secretary_calendar_rel(secretary_id,tag_id) values (NEW.sec_id,tag_rec.tag_id) ;
             end if ;
           end loop ;
           close tag_cur ;
           delete from repairtag_secretary_calendar_rel where secretary_id=NEW.sec_id and 
              tag_id not in (select tag_id from repairtag_repair_calendar_rel where repair_id=NEW.id) ;
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists after_update_repair_calendar on cloudrent_repair_calendar ;""")
        self._cr.execute("""create trigger after_update_repair_calendar after update of state on cloudrent_repair_calendar
                                                              for each row execute procedure after_update_repair_calendar()""")

        self._cr.execute("""drop function if exists bfins_vendor_repair_service() cascade""")
        self._cr.execute("""create or replace function bfins_vendor_repair_service() returns trigger as $BODY$
        DECLARE
           repyear varchar ;
           repmonth varchar ;
        BEGIN
           if NEW.repair_end_date is not null then
             select date_part('year',NEW.repair_start_date)::TEXT into NEW.repair_year ;
             select lpad(date_part('month',NEW.repair_start_date)::TEXT,2,'0')::TEXT into NEW.repair_month ;
           end if ;
             
           return NEW ;
        END;$BODY$
        LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists bfins_vendor_repair_service on cloudrent_vendor_repair_service ;""")
        self._cr.execute("""create trigger bfins_vendor_repair_service before insert on cloudrent_vendor_repair_service
                                                       for each row execute procedure bfins_vendor_repair_service()""")



















