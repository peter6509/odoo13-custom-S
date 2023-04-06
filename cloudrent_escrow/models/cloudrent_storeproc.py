# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class CloudRentStoreProc(models.Model):
    _name = "cloudrent.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists gencrmstage() cascade""")
        self._cr.execute("""create or replace function gencrmstage() returns void as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           delete from crm_stage ; 
           select count(*) into ncount from crm_stage where name='場勘' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (10,'場勘',FALSE,FALSE) ;
           end if ; 
           select count(*) into ncount from crm_stage where name='申請書' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (20,'申請書',FALSE,FALSE) ;
           end if ; 
           select count(*) into ncount from crm_stage where name='招租' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (30,'招租',FALSE,FALSE) ;
           end if ;
           select count(*) into ncount from crm_stage where name='帶看' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (40,'帶看',FALSE,FALSE) ;
           end if ;
           select count(*) into ncount from crm_stage where name='收訂' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (50,'收訂',FALSE,FALSE) ;
           end if ;
           select count(*) into ncount from crm_stage where name='預簽' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (60,'預簽',FALSE,FALSE) ;
           end if ;
           select count(*) into ncount from crm_stage where name='簽約' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (70,'簽約',TRUE,FALSE) ;
           end if ;
           select count(*) into ncount from crm_stage where name='LOSE' ;
           if ncount = 0 then
              insert into crm_stage(sequence,name,is_won,fold) values (0,'LOSE',FALSE,TRUE) ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getbuildage(build_date date) cascade""")
        self._cr.execute("""create or replace function getbuildage(build_date date) returns INT as $BODY$
          DECLARE
            myres int ;
            nowdate date ;
          BEGIN
            select current_timestamp::DATE into nowdate ;
            select date_part('year',age(nowdate::DATE,build_date::DATE))::INT into myres ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_contract_match(leadid int) cascade""")
        self._cr.execute("""create or replace function gen_contract_match(leadid int) returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           ncount3 int ;
           l_cur refcursor ;
           l_rec record ;
           pic_cur refcursor ;
           pic_rec record ;
           e_cur refcursor ;
           e_rec record ;
           maxbuildid int ;
           objno varchar ;
           lesseeno varchar ;
           maxmemberid int ;
           weekseq int ;
           matchyear varchar ;
           matchmonth varchar ;
         BEGIN
           select object_no,lessee_no into objno,lesseeno from crm_lead where id=leadid ;
           select count(*) into ncount from cloudrent_build where object_no=objno ; 
           open l_cur for select * from crm_lead where id = leadid ;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             /* 將crm lead 新增到 cloudrent_build 建物明細主檔 */
             if ncount = 0 then
                insert into cloudrent_build(object_no,escrow_agent,case_type,admin_area,build_sec,build_msec,build_number,build_createdate,build_area,build_for_rent,
                 general_build,build_type,build_pattern,build_lessor,is_rent,build_evelator,build_pet,house_number,place_number,build_rent_situation) values (l_rec.object_no,l_rec.escrow_agent,l_rec.case_type,l_rec.admin_area,l_rec.build_sec,
                 l_rec.build_msec,l_rec.build_number,l_rec.build_createdate,l_rec.build_area,l_rec.build_for_rent,
                 l_rec.general_build,l_rec.build_type,l_rec.build_pattern,l_rec.build_lessor,TRUE,l_rec.build_evelator,l_rec.build_pet,l_rec.house_number,l_rec.place_number,l_rec.build_rent_situation) ;
                select max(id) into maxbuildid from cloudrent_build where object_no=objno ;
                open pic_cur for select * from cloudrent_sitecheck_pic_line where sitecheck_id=leadid ;
                loop
                    fetch pic_cur into pic_rec ;
                    exit when not found ;
                    insert into cloudrent_build_line(build_id,sequence,build_pic,build_desc) values (maxbuildid,pic_rec.sequence,pic_rec.build_pic,pic_rec.build_desc) ;
                end loop ;
                close pic_cur ; 
             else
                select id into maxbuildid from cloudrent_build where object_no=objno ;
                update cloudrent_build set escrow_agent=l_rec.escrow_agent,build_for_rent=l_rec.build_for_rent where id = maxbuildid ;
                update cloudrent_build_line set active=FALSE where build_id=maxbuildid ;
                open pic_cur for select * from cloudrent_sitecheck_pic_line where sitecheck_id=leadid ;
                loop
                    fetch pic_cur into pic_rec ;
                    exit when not found ;
                    insert into cloudrent_build_line(build_id,sequence,build_pic,build_desc) values (maxbuildid,pic_rec.sequence,pic_rec.build_pic,pic_rec.build_desc) ;
                end loop ;
                close pic_cur ;
             end if ;
             /* 將 crm lead 新增到 cloudrent_escrow_member 房客資料 */
             select count(*) into ncount1 from cloudrent_escrow_member where lessee_no=lesseeno ;
             if ncount1 = 0 then
                open e_cur for select * from cloudrent_lessee_sitecheck where lessee_id=leadid and rent_success=TRUE ;
                loop
                  fetch e_cur into e_rec ;
                  exit when not found ;
                  insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,fin_instno,fin_branch,fin_name,fin_account,lessee_no,
                   member_sex,lessee_age,member_phone1,member_phone2,member_cell,member_email,build_pattern,elevator,lessee_expected_value,lessee_expected_value1,build_area,
                   pet,worship_god,member_number,member_memo,member_birthday,lessee_type) values (e_rec.lessee_man,e_rec.lessee_pid,l_rec.escrow_agent,'2',l_rec.lessee_fin_instno,
                   l_rec.lessee_fin_branch,l_rec.lessee_fin_name,l_rec.lessee_fin_account,l_rec.lessee_no,e_rec.lessee_sex,e_rec.lessee_age,e_rec.lessee_phone1,e_rec.lessee_phone2,
                   e_rec.lessee_cell,e_rec.lessee_email,e_rec.build_pattern,e_rec.elevator,e_rec.lessee_expected_value,e_rec.lessee_expected_value1,e_rec.build_area,e_rec.pet,e_rec.worship_god,
                   e_rec.member_number,e_rec.lessee_memo,e_rec.lessee_birthday,l_rec.lessee_type) ;
                end loop ;
                close e_cur ;
             else
                select id into maxmemberid from cloudrent_escrow_member where lessee_no=lesseeno ;
                open e_cur for select * from cloudrent_lessee_sitecheck where lessee_id=leadid and rent_success=TRUE ;
                loop
                  fetch e_cur into e_rec ;
                  exit when not found ;
                       update cloudrent_escrow_member set escrow_man=e_rec.lessee_man,escrow_pid=e_rec.lessee_pid,lessee_age=e_rec.lessee_age,build_pattern=e_rec.build_pattern,
                        escrow_type='2',fin_instno=l_rec.lessee_fin_instno,fin_branch=l_rec.lessee_fin_branch,fin_name=l_rec.lessee_fin_name,fin_account=l_rec.lessee_fin_account,lessee_no=l_rec.lessee_no,
                        member_sex=e_rec.lessee_sex,lessee_age=e_rec.lessee_age,member_birthday=e_rec.lessee_birthday,member_phone1=e_rec.lessee_phone1,member_phone1=e_rec.lessee_phone2,
                        member_cell=e_rec.lessee_cell,member_email=e_rec.lessee_email,build_pattern=e_rec.build_pattern,elevator=e_rec.elevator,
                        lessee_expected_value=e_rec.lessee_expected_value,lessee_expected_value1=
                        e_rec.lessee_expected_value1,build_area=e_rec.build_area,pet=e_rec.pet,worship_god=e_rec.worship_god,
                        member_number=e_rec.member_number,member_memo=e_rec.lessee_memo,lessee_type=l_rec.lessee_type where id=maxmemberid ;
                end loop ;
                close e_cur ;   
             end if ;
             /* 將 crm lead 新增到 cloudrent_escrow_member 房東資料 */
             select count(*) into ncount2 from cloudrent_escrow_member where escrow_pid=l_rec.lessor_pid ;
             if ncount2 = 0 then
                insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,fin_instno,fin_branch,fin_name,
                 fin_account,member_sex,member_phone1,member_cell,member_phone2,member_addr,member_addr1,member_memo) values (l_rec.build_lessor_name,l_rec.lessor_pid,
                 l_rec.escrow_agent,'1',l_rec.lessor_fin_instno,l_rec.lessor_fin_branch,l_rec.lessor_fin_name,l_rec.lessor_fin_account,l_rec.lessor_sex,
                 l_rec.lessor_phone1,l_rec.lessor_phone2,l_rec.lessor_addr,l_rec.lessor_addr1,l_rec.lessor_memo) ;
             else
                 update cloudrent_escrow_member set member_memo=l_rec.lessor_memo where escrow_pid=l_rec.lessor_pid ;
             end if ;
             /* 將 crm lead 新增到 cloudrent_contact_match 媒合合約資料 */
             select count(*) into ncount3 from cloudrent_contract_match where match_no=l_rec.match_no ;
             if ncount3 = 0 then
                select date_part('week',current_timestamp::DATE)::INT into weekseq ;
                select (date_part('year',current_timestamp::DATE)::INT - 1911)::TEXT into matchyear ;
                select lpad(date_part('month',current_timestamp::DATE)::TEXT,2,'0') into matchmonth ;
                insert into cloudrent_contract_match(escrow_no,crm_lead_id,match_no,object_no,lessee_no,case_type,admin_area,
                 build_sec,build_msec,build_number,build_createdate,build_area,build_for_rent,build_contract_rent,general_build,
                 build_type,build_lessor,lessor_fin_instno,lessor_fin_branch,lessor_fin_name,lessor_fin_account,build_lessee,lessee_fin_instno,
                 lessee_fin_branch,lessee_fin_account,lessee_type,is_send,week_seq,match_year,match_month) values (l_rec.escrow_agent,leadid,l_rec.match_no,
                 l_rec.object_no,l_rec.lessee_no,l_rec.case_type,l_rec.admin_area,l_rec.build_sec,l_rec.build_msec,l_rec.build_number,
                 l_rec.build_createdate,l_rec.build_area,l_rec.build_for_rent,l_rec.build_contract_rent,l_rec.general_build,l_rec.build_type,
                 l_rec.build_lessor,l_rec.lessor_fin_instno,l_rec.lessor_fin_branch,l_rec.lessor_fin_name,l_rec.lessor_fin_account,l_rec.build_lessee,
                 l_rec.lessee_fin_instno,l_rec.lessee_fin_branch,l_rec.lessee_fin_account,l_rec.lessee_type,FALSE,weekseq,matchyear,matchmonth) ;
             end if ;
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getreportweek(mydate date) cascade""")
        self._cr.execute("""create or replace function getreportweek(mydate date) returns INT as $BODY$
          DECLARE
            myres int ;
          BEGIN
            select date_part('week',mydate)::INT into myres ;
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getreportyear(mydate date) cascade""")
        self._cr.execute("""create or replace function getreportyear(mydate date) returns varchar as $BODY$
          DECLARE
            myres varchar ;
          BEGIN
            select date_part('year',mydate)::TEXT into myres ;
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists entrust_year(edate1 date,edate2 date) cascade""")
        self._cr.execute("""create or replace function entrust_year(edate1 date,edate2 date) returns INT as $BODY$
         DECLARE
           myres INT ;
         BEGIN
           if edate1 is not null and edate2 is not null then
              select date_part('year',age(edate2,edate1))::INT into myres ;
           else
             myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists entrust_month(edate1 date,edate2 date) cascade""")
        self._cr.execute("""create or replace function entrust_month(edate1 date,edate2 date) returns INT as $BODY$
         DECLARE
           myres INT ;
         BEGIN
           if edate1 is not null and edate2 is not null then
              select date_part('month',age(edate2,edate1))::INT into myres ;
           else
             myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_cloudrent_seqno(escrowid int,escrowtype varchar) cascade""")
        self._cr.execute("""create or replace function get_cloudrent_seqno(escrowid int,escrowtype varchar) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           nseq int ;
           ncount int ;
           nyear int ;
           nmonth int ;
         BEGIN
           select date_part('year',current_timestamp::DATE)::INT into nyear ;
           select date_part('month',current_timestamp::DATE)::INT into nmonth ;  
           select count(*) into ncount from cloudrent_sequence_no where escrow_no=escrowid and seq_type=escrowtype and seq_year=nyear and seq_month=nmonth ;
           if ncount = 0 then
              myres = concat(escrowtype,'-',nyeay::TEXT,lpad(nmonth::TEXT,2,'0'),'001') ;
              insert into cloudrent_sequence_no(escrow_no,seq_type,seq_year,seq_month_seq_num) values (escrowid,escrowtype,nyear,nmonth,1) ;
           else
              select coalesce(seq_num,0)+1 into nseq from cloudrent_sequence_no where escrow_no=escrowid and seq_type=escrowtype and seq_year=nyear and seq_month=nmonth ;
              myres = concat(escrowtype,'-',nyeay::TEXT,lpad(nmonth::TEXT,2,'0'),lpad(nseq::TEXT,3,'0')) ;
              update cloudrent_sequence_no set seq_num=coalesce(seq_num,0)+1 where escrow_no=escrowid and seq_type=escrowtype and seq_year=nyear and seq_month=nmonth ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_escrow_build(leadid1 int) cascade""")
        self._cr.execute("""create or replace function gen_escrow_build(leadid1 int) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
           l_cur refcursor ;
           l_rec record ;
           buildlid int ;
         BEGIN
           open l_cur for select * from crm_lead where id = leadid1 ;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_build where leadid=leadid1 ;
             if ncount = 0 then
                /* 建立建物基本資料主檔 */
                insert into cloudrent_build(object_no,escrow_agent,case_type,admin_area,build_sec,build_msec,build_number,house_number,place_number,
                  parking_space,ancillary_equipment,build_rent_situation,rent_man,rent_duedate,rent_other_desc,entrust_start_date,entrust_end_date,
                  build_createdate,build_area,build_for_rent,general_build,build_type,build_pattern,build_elevator,build_pet,leadid) values 
                  (l_rec.object_no,l_rec.escrow_agent,l_rec.case_type,l_rec.admin_area,l_rec.build_sec,l_rec.build_msec,l_rec.build_number,l_rec.house_number,l_rec.place_number,
                  l_rec.parking_space,l_rec.ancillary_equipment,l_rec.build_rent_situation,l_rec.rent_man,l_rec.rent_duedate,l_rec.rent_other_desc,l_rec.entrust_start_date,l_rec.entrust_end_date,
                  l_rec.build_createdate,l_rec.build_area,l_rec.build_for_rent,l_rec.general_build,l_rec.build_type,l_rec.build_pattern,l_rec.build_elevator,l_rec.build_pet,leadid1);
                select max(id) into buildlid from cloudrent_build ;  
             else
                update cloudrent_build set object_no=l_rec.object_no,escrow_agent=l_rec.escrow_agent,case_type=l_rec.case_type,admin_area=l_rec.admin_area,
                   build_sec=l_rec.build_sec,build_msec=l_rec.build_msec,build_number=l_rec.build_number,house_number=l_rec.house_number,place_number=l_rec.place_number,
                   parking_space=l_rec.parking_space,ancillary_equipment=l_rec.ancillary_equipment,build_rent_situation=l_rec.build_rent_situation,rent_man=l_rec.rent_man,
                   rent_duedate=l_rec.rent_duedate,rent_other_desc=l_rec.rent_other_desc,entrust_start_date=l_rec.entrust_start_date,entrust_end_date=l_rec.entrust_end_date,
                   build_createdate=l_rec.build_createdate,build_area=l_rec.build_area,build_for_rent=l_rec.build_for_rent,general_build=l_rec.general_build,build_type=l_rec.build_type,
                   build_pattern=l_rec.build_pattern,build_elevator=l_rec.build_elevator,build_pet=l_rec.build_pet where leadid=leadid1 ;
                select max(id) into buildlid from cloudrent_build where leadid = leadid1 ;   
             end if ;
           end loop ;
           close l_cur ;
           myres = buildlid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_build_line_pic(leadid int) cascade""")
        self._cr.execute("""create or replace function gen_build_line_pic(leadid int) returns void as $BODY$
         DECLARE
           pic_cur refcursor ;
           pic_rec record ;
           buildid int ;
           ncount1 int ;
         BEGIN
           select object_no1 into buildid from crm_lead where id = leadid ;
           if buildid is not null then
               open pic_cur for select * from cloudrent_sitecheck_pic_line where sitecheck_id=leadid ;
               loop
                 fetch pic_cur into pic_rec ;
                 exit when not found ;
                 select count(*) into ncount1 from cloudrent_build_line where build_id=buildid and sequence=pic_rec.sequence ;
                 if ncount1 = 0 then
                    /* 主檔照片檔 */
                    insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc,build_pic,build_pic1,build_pic2,originid) values 
                       (buildid,pic_rec.sequence,pic_rec.sitecheck_type,pic_rec.sitecheck_desc,pic_rec.sitecheck_pic,pic_rec.sitecheck_pic1,pic_rec.sitecheck_pic2,pic_rec.id) ;
                 else
                    update  cloudrent_build_line set pic_type=pic_rec.sitecheck_type,build_desc=pic_rec.sitecheck_desc,
                            build_pic=pic_rec.sitecheck_pic,build_pic1=pic_rec.sitecheck_pic1,build_pic2=pic_rec.sitecheck_pic2,
                            originid=pic_rec.id where build_id=buildid and sequence=pic_rec.sequence ;   
                 end if ;
               end loop ;
               close pic_cur ;
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_build_equip_part(leadid int) cascade""")
        self._cr.execute("""create or replace function gen_build_equip_part(leadid int) returns void as $BODY$
         DECLARE
           e_cur refcursor ;
           e_rec record ;
           buildid int ;
           ncount int ;
         BEGIN
           select object_no1 into buildid from crm_lead where id = leadid ;
           open e_cur for select * from cloudrent_crm_lead_equip_part where equip_id=leadid ;
           loop
             fetch e_cur into e_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_build_equip_part where equip_id=buildid and equip_no=e_rec.equip_no ;
             if ncount = 0 then
                insert into cloudrent_build_equip_part(equip_id,equip_categ,equip_no,equip_qty,equip_status,equip_image1,equip_image2,equip_image3) values 
                 (buildid,e_rec.equip_categ,e_rec.equip_no,e_rec.equip_qty,e_rec.equip_status,e_rec.equip_image1,e_rec.equip_image2,e_rec.equip_image3) ;
             else
                update cloudrent_build_equip_part set equip_categ=e_rec.equip_categ,equip_qty=e_rec.equip_qty,equip_status=e_rec.equip_status,
                   equip_image1=e_rec.equip_image1,equip_image2=e_rec.equip_image2,equip_image3=e_rec.equip_image3
                   where equip_id=buildid and equip_no=e_rec.equip_no ;
             end if ;
           end loop ;
           close e_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_member_lessor(leadid1 int) cascade""")
        self._cr.execute("""create or replace function gen_member_lessor(leadid1 int) returns INT as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           ncount int ;
           myres int ;
         BEGIN
           open l_cur for select * from crm_lead where id = leadid1 ;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             if l_rec.lessor_pid is not null then
                select count(*) into ncount from cloudrent_escrow_member where escrow_pid = l_rec.lessor_pid ;
                if ncount = 0 then
                   insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,fin_instno,fin_branch,fin_name,fin_account,member_sex,
                     member_phone1,member_phone2,member_cell,member_addr,member_addr1,member_email,member_birthday,member_memo,leadid) values (l_rec.build_lessor_name,l_rec.lessor_pid,l_rec.escrow_agent,'1',
                     l_rec.lessor_fin_instno,l_rec.lessor_fin_branch,l_rec.lessor_fin_name,l_rec.lessor_fin_account,l_rec.lessor_sex,l_rec.lessor_phone1,l_rec.lessor_phone2,l_rec.lessor_cell,
                     l_rec.lessor_addr,l_rec.lessor_addr1,l_rec.lessor_email,l_rec.lessor_birthday,l_rec.lessor_memo,leadid1) ;
                else
                   update cloudrent_escrow_member set escrow_man=l_rec.build_lessor_name,escrow_agent=l_rec.escrow_agent,escrow_type='1',fin_instno=l_rec.lessor_fin_instno,
                     fin_branch=l_rec.lessor_fin_branch,fin_name=l_rec.lessor_fin_name,fin_account=l_rec.lessor_fin_account,member_sex=l_rec.lessor_sex,member_phone1=l_rec.lessor_phone1,member_phone2=l_rec.lessor_phone2,
                     member_cell=l_rec.lessor_cell,member_addr=l_rec.lessor_addr,member_addr1=l_rec.lessor_addr1,member_email=l_rec.lessor_email,member_birthday=l_rec.lessor_birthday,member_memo=l_rec.lessor_memo,leadid=leadid1 where escrow_pid=l_rec.lessor_pid ;
                end if ;
                select max(id) into myres from cloudrent_escrow_member where escrow_pid = l_rec.lessor_pid ;
             end if ;   
           end loop ;
           close l_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_member_lessee(leadid1 int) cascade""")
        self._cr.execute("""create or replace function gen_member_lessee(leadid1 int) returns INT as $BODY$
         DECLARE
           s_cur refcursor ;
           s_rec record ;
           ncount int ;
           myres int ;
           lesseeno varchar ;
           escrowagent int ;
           fininstno varchar ;
           finbranch varchar ;
           finname varchar ;
           finaccount varchar ;
           leemail varchar ;
           lebirthday date ;
           lesseetype varchar ;
           lesseepid varchar ;
           lesseeaddr varchar ;
           lesseeaddr1 varchar ;
         BEGIN
           select coalesce(lessee_no,' '),escrow_agent,lessee_fin_instno,lessee_fin_branch,lessee_fin_name,lessee_fin_account,lessee_email,lessee_birthday,lessee_type,lessee_pid,lessee_addr1,lessee_addr
             into lesseeno,escrowagent,fininstno,finbranch,finname,finaccount,leemail,lebirthday,lesseetype,lesseepid,lesseeaddr1,lesseeaddr from crm_lead where id = leadid1 ;
           open s_cur for select * from cloudrent_lessee_sitecheck where lessee_id = leadid1 ;
           loop
             fetch s_cur into s_rec ;
             exit when not found ;
             if s_rec.lessee_pid is not null and s_rec.rent_sucess then
                select count(*) into ncount from cloudrent_escrow_member where escrow_pid = s_rec.lessee_pid ;
                if ncount = 0 then
                   insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,fin_instno,fin_branch,fin_name,fin_account,member_sex,
                     member_phone1,member_phone2,member_cell,member_email,member_birthday,member_memo,lessee_no,lessee_age,build_pattern,elevator,lessee_expected_value,lessee_expected_value1,
                     build_area,pet,worship_god,member_number,lessee_type,member_addr,member_addr1,leadid) values (s_rec.lessee_name,lesseepid,escrowagent,'2',fininstno,finbranch,finname,finaccount,s_rec.lessee_sex,
                     s_rec.lessee_phone1,s_rec.lessee_phone2,s_rec.lessee_cell,leemail,lebirthday,s_rec.lessee_memo,lesseeno,s_rec.lessee_age,s_rec.build_pattern,s_rec.elevator,s_rec.lessee_expected_value,s_rec.lessee_expected_value1,
                     s_rec.build_area,s_rec.pet,s_rec.worship_god,s_rec.member_number,lesseetype,lesseeaddr1,lesseeaddr,leadid1) ;
                else
                   update cloudrent_escrow_member set escrow_man=s_rec.lessee_name,escrow_agent=escrowagent,escrow_type='2',fin_instno=fininstno,fin_branch=finbranch,fin_name=finname,fin_account=finaccount,member_sex=s_rec.lessee_sex,
                     member_phone1=s_rec.lessee_phone1,member_phone2=s_rec.lessee_phone2,member_cell=s_rec.lessee_cell,member_birthday=lebirthday,member_email=leemail,member_memo=s_rec.lessee_memo,lessee_no=lesseeno,lessee_age=s_rec.lessee_age,build_pattern=s_rec.build_pattern,elevator=s_rec.elevator,
                     lessee_expected_value=s_rec.lessee_expected_value,lessee_expected_value1=s_rec.lessee_expected_value1,build_area=s_rec.build_area,pet=s_rec.pet,worship_god=s_rec.worship_god,member_number=s_rec.member_number,
                     leadid=leadid1,lessee_type=lesseetype,member_addr=lesseeaddr1,member_addr1=lesseeaddr where escrow_pid = s_rec.lessee_pid ;
                end if ;
                select max(id) into myres from cloudrent_escrow_member where escrow_pir=s_rec.lessee_pid ;
             end if ;   
           end loop ;
           close s_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_renew_ym(msdate date) cascade""")
        self._cr.execute("""create or replace function get_renew_ym(msdate date) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           msdate1 date ;
           cmonth varchar ;
           cyear varchar ;
         BEGIN
           msdate1 =  msdate + interval '1 year' - interval '3 month' ; 
           select date_part('year',msdate1)::TEXT into cyear ;
           select lpad(date_part('month',msdate1)::TEXT,2,'0') into cmonth ;
           myres = concat(cyear,'-',cmonth) ;
           return myres ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_lessor(myagent int,mylessor varchar,mycell varchar,myaddr varchar) cascade""")
        self._cr.execute("""drop function if exists import_lessor(myagent int,mylessor varchar,mycell varchar,myaddr varchar,escrowpid varchar) cascade""")
        self._cr.execute("""create or replace function import_lessor(myagent int,mylessor varchar,mycell varchar,myaddr varchar,escrowpid varchar) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select count(*) into ncount from cloudrent_escrow_member where escrow_agent=myagent and escrow_man=mylessor and escrow_type='1' ;
            if ncount = 0 then
               insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,member_cell,member_addr,member_addr1) values (mylessor,escrowpid,myagent,'1',mycell,myaddr,myaddr) ;
               select max(id) into myres from cloudrent_escrow_member ;
            else
               select id into myres from cloudrent_escrow_member where escrow_man=mylessor  and escrow_type='1' and escrow_agent=myagent  ;
               update cloudrent_escrow_member set escrow_pid=escrowpid,member_cell=mycell,member_addr=myaddr,member_addr1=myaddr where id = myres ;   
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_lessee(myagent int,mylessee varchar,mycell varchar,mylesseeno varchar,mybuildloc varchar) cascade""")
        self._cr.execute("""drop function if exists import_lessee(myagent int,mylessee varchar,mycell varchar,mylesseeno varchar,mybuildloc varchar,escrowpid varchar) cascade""")
        self._cr.execute("""create or replace function import_lessee(myagent int,mylessee varchar,mycell varchar,mylesseeno varchar,mybuildloc varchar,escrowpid varchar) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
         BEGIN
           select count(*) into ncount from cloudrent_escrow_member where escrow_type='2' and lessee_no=mylesseeno ;
           if ncount = 0 then
              insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type,member_cell,lessee_no,build_area) values
                (mylessee,escrowpid,myagent,'2',mycell,mylesseeno,mybuildloc) ;
              select max(id) into myres from cloudrent_escrow_member ;  
           else
              select id into myres from cloudrent_escrow_member where escrow_type='2' and lessee_no=mylesseeno ;
              update cloudrent_escrow_member set escrow_pid=escrowpid,member_cell=mycell,build_area=mybuildloc where id=myres ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_sale(myagent int,mysale varchar) cascade""")
        self._cr.execute("""create or replace function import_sale(myagent int,mysale varchar) returns INT as $BODY$
          DECLARE
            ncount int ;
            myres int ;
          BEGIN
            select count(*) into ncount from cloudrent_escrow_member where escrow_man=mysale and escrow_type='5' and escrow_agent=myagent ;
            if ncount = 0 then
               insert into cloudrent_escrow_member(escrow_man,escrow_pid,escrow_agent,escrow_type) values (mysale,'New',myagent,'5') ;
               select max(id) into myres from cloudrent_escrow_member ;
            else
               select id into myres from cloudrent_escrow_member where escrow_man=mysale and escrow_type='5' and escrow_agent=myagent ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists import_build(myagent int,myobjno varchar,mywaddr varchar,mybloc varchar,mymsd date,mymed date,mybpatt varchar,mybcomm varchar,mylessor int) cascade""")
        self._cr.execute("""create or replace function import_build(myagent int,myobjno varchar,mywaddr varchar,mybloc varchar,mymsd date,mymed date,mybpatt varchar,mybcomm varchar,mylessor int) returns INT as $BODY$
         DECLARE
           ncount int ;
           myres int ;
         BEGIN
           select count(*) into ncount from cloudrent_build where object_no=myobjno ;
           if ncount = 0 then
              insert into cloudrent_build(object_no,escrow_agent,house_number,build_loc,build_community,entrust_start_date,entrust_end_date,build_lessor) values
               (myobjno,myagent,mywaddr,mybloc,mybcomm,mymsd,mymed,mylessor) ;
               select max(id) into myres from cloudrent_build ;
           else
              select id into myres from cloudrent_build where object_no=myobjno ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_cdate(cdate varchar) cascade""")
        self._cr.execute("""create or replace function get_cdate(cdate varchar) returns date as $BODY$
         DECLARE
           myres date ;
           yp int ;
           mp int ;
           cdatelen int ;
           cdate1 varchar ;
           cy varchar ;
           cm varchar ;
           cd varchar ;
         BEGIN
           select replace(cdate,'-','.') into cdate ;
           select replace(cdate,'/','.') into cdate ;
           select length(cdate) into cdatelen ; /* 日期總長度 */ 
           select position('.' in cdate) into yp ; /* 第一個.的位置 */
           select substring(cdate,1,yp - 1) into cy ; /* 年 */
           select substring(cdate,yp+1,cdatelen) into cdate1 ; /* 扣除年.之後的字串*/
           select position('.' in cdate1) into mp ; /* cdate1 .的位置 */
           select substring(cdate1,1,mp - 1) into cm ;  /* 月 */
           select substring(cdate,yp + mp + 1,cdatelen) into cd ; /* 日 */
           if length(cy)=3 then
               myres = concat((cy::INT + 1911)::TEXT,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;
           elsif length(cy)=4 and cy::INT > 1911 then
               myres = concat(cy,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;
           elsif length(cy)=4 and cy::INT < 1911 then
               myres = concat((cy::INT + 1911)::TEXT,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;  
           else
               myres = False ;      
           end if ;    
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_cymddate(cy varchar,cm varchar,cd varchar) cascade""")
        self._cr.execute("""create or replace function get_cymddate(cy varchar,cm varchar,cd varchar) returns DATE as $BODY$
         DECLARE
           myres DATE ;
         BEGIN
           if cd::INT = 0 then
              cd='1' ;
           end if ;
           if length(cy)=3 then
               myres = concat((cy::INT+1911)::TEXT,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;
           elsif length(cy)=4 and cy::INT > 1911 then
               myres = concat(cy,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;
           elsif length(cy)=4 and cy::INT < 1911 then    
               myres = concat((cy::INT+1911)::TEXT,'-',lpad(cm,2,'0'),'-',lpad(cd,2,'0'))::DATE ;
           end if ;    
           if cy::INT=0 or cm::INT=0 or cd::INT=0 then
              myres = null ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;
         """)

        self._cr.execute("""drop function if exists gen_new_build(matchid int) cascade""")
        self._cr.execute("""create or replace function gen_new_build(matchid int) returns void as $BODY$
         DECLARE
            m_cur refcursor ;
            m_rec record ;
         BEGIN
            open m_cur for select * from cloudrent_contract_match where id = matchid ;
            loop
               fetch m_cur into m_rec ;
               exit when not found ;
               update cloudrent_build set case_type=m_rec.case_type,admin_area=m_rec.admin_area,build_loc=m_rec.build_loc,
                      build_community=m_rec.build_community,build_sec=m_rec.build_sec,build_msec=m_rec.build_msec,
                      build_number=m_rec.build_number,house_number=m_rec.house_number,build_createdate=m_rec.build_createdate,
                      place_number=m_rec.place_number,build_area=m_rec.build_area,build_for_rent=m_rec.build_for_rent,
                      general_build=m_rec.general_build,build_type=m_rec.build_type,build_pattern=m_rec.build_pattern,
                      build_pattern1=m_rec.build_pattern1 where id = m_rec.object_no1 ;
            end loop ;
            close m_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_grant_repair(matchid int) cascade""")
        self._cr.execute("""create or replace function chk_grant_repair(matchid int) returns Boolean as $BODY$
          DECLARE
            myres boolean ;
            sdate date ;
            edate date ;
            sy varchar ;
            ey varchar ;
            sm varchar ;
            em varchar ;
            maxgrant int ;
            myarea varchar ;
            insurfee int ;
            repairfee int ;
          BEGIN
            select admin_area,match_start_date,match_end_date into myarea,sdate,edate from cloudrent_contract_match where id = matchid ;
            select grant_max_value into maxgrant from cloudrent_grant_fee where admin_area=myarea and grant_item=3 ;
            select sum(coalesce(real_insurance_fee,0)) into insurfee from cloudrent_safe_insurance_fee where safe_id = matchid ;
            select sum(coalesce(real_repair_fee,0)) into repairfee from cloudrent_repair_fee where repair_id = matchid ;
            if (coalesce(insurfee,0)::numeric + coalesce(repairfee,0)::numeric) <= maxgrant then
               myres = TRUE ;   /*  申請金額未超過上限  */
            else
               myres = FALSE ;  
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmatchfee(matchid int) cascade""")
        self._cr.execute("""create or replace function genmatchfee(matchid int) returns void as $BODY$
         DECLARE
           itemkey int ;
           adminarea varchar ;
           grantid int ;
           gfreq int ;
           gtime int ;
           gvalue int ;
           msd date ;
           med date ;
           startdate date ;
           nseq int ;
           cyear varchar ;
           cmonth varchar ;
           lessortype varchar ;
           lesseetype varchar ;
           casetype varchar ;
           b_c_rent int ;
           lesseegrant int ;
           maxseq int ;
           cym varchar ;
           weekseq int ;
           disrate float ;
         BEGIN
           delete from cloudrent_safe_insurance_fee ;
           delete from cloudrent_notarial_fee ;
           delete from cloudrent_repair_fee ;
           delete from cloudrent_grant_rent ;
           delete from cloudrent_escrow_develop ;
           delete from cloudrent_guarantee_fee ;
           delete from cloudrent_contract_match_fee ;
           delete from cloudrent_escrow_fee ;
           select admin_area,match_start_date,match_end_date,case_type,lessee_type,build_contract_rent,lessee_grant,case_type into 
              adminarea,msd,med,lessortype,lesseetype,b_c_rent,lesseegrant,casetype from cloudrent_contract_match where id = matchid ;
            /* 生成 公證費 itemkey=2 */
           itemkey = 2 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=adminarea ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',msd)::TEXT into cyear ;
              select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (matchid,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (matchid,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_notarial_fee(notarial_id,notarial_seq,notarial_applyfor_fee,notarial_applyfor_year,notarial_applyfor_month) values (matchid,nseq,gvalue) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ;
         
           /* 生成 租金補助 itemkey=4 */
           itemkey = 4 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
              admin_area=adminarea and lessor_type=lessortype and lessee_type=lesseetype ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value,discount_rate into gfreq,gtime,gvalue,disrate from cloudrent_grant_fee where id = grantid ;
              if round(b_c_rent::numeric * disrate::numeric) > gvalue then
                 lesseegrant = gvalue ;     /* if 租金*補助比率;如 > 最大上限 => 補助=最大上限 */
              else
                 lesseegrant = round(b_c_rent::numeric * disrate::numeric) ; /* 否則 租金*補助比率  */
              end if ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              select date_part('year',msd)::TEXT into cyear ;
              select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
              if gfreq='1' then       /* By件 */
                 insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (matchid,1,b_c_rent,lesseegrant,1,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = msd ;
                 cym = concat(cyear,'-',cmonth) ;
                 loop
                  select date_part('year',startdate)::TEXT into cyear ;
                  select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med or nseq > 12 ;
                   insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (matchid,nseq,b_c_rent,lesseegrant,nseq,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_grant_rent(grant_id,rent_seq,contract_rent_fee,applyfor_rent_fee,rent_period,applyfor_rent_year,applyfor_rent_month) values (matchid,nseq,b_c_rent,lesseegrant,nseq,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                   select date_part('year',startdate)::TEXT into cyear ;
                 end loop ;
              end if ;
              select max(rent_seq) into maxseq from cloudrent_grant_rent where grant_id=matchid ;
              update cloudrent_grant_rent set tot_rent_period=maxseq where grant_id=matchid ;
              
           end if ;   
           
           /* 生成 開發費 itemkey=5 */
           itemkey = 5 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=adminarea  ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              if gfreq='1' then       /* By件 */
                 select date_part('year',msd)::TEXT into cyear ;
                 select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
                 insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (matchid,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (matchid,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_escrow_develop(develop_id,develop_seq,develop_applyfor_fee,develop_applyfor_year,develop_applyfor_month) values (matchid,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ;   
           if casetype='1' then
              /* 生成 包管費 itemkey=6 */
               itemkey = 6 ;
               select id into grantid from cloudrent_grant_fee where grant_item=itemkey and 
                  admin_area=adminarea  ;
               if grantid is not null then
                  select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
                  if gtime=-1 then
                     gtime=10000 ;
                  end if ;
                  if gfreq='1' then       /* By件 */
                     select date_part('year',msd)::TEXT into cyear ;
                     select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
                     insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (matchid,1,gvalue,1,cyear,cmonth) ;
                  elsif gfreq='2' then    /* By月 */
                     nseq = 1 ;
                     startdate = msd ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > med ;
                       insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (matchid,nseq,gvalue,nseq,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 month' ;
                     end loop ;
                  else                    /* By年 */  
                     nseq = 1 ;
                     startdate = msd ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > med ;
                       insert into cloudrent_guarantee_fee(guarantee_id,guarantee_seq,guarantee_applyfor_fee,guarantee_period,guarantee_applyfor_year,guarantee_applyfor_month) values (matchid,nseq,gvalue,nseq,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 year' ;
                     end loop ;
                  end if ;
                  select max(guarantee_seq) into maxseq from cloudrent_guarantee_fee where guarantee_id=matchid ;
                  update cloudrent_guarantee_fee set guarantee_tot_period=maxseq where guarantee_id=matchid ;
               end if ;   
           else
               /* 生成 代管費 itemkey=8 */
               itemkey = 8 ;
               select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=adminarea  ;
               if grantid is not null then
                  select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
                  if gtime=-1 then
                     gtime=10000 ;
                  end if ;
                  if gfreq='1' then       /* By件 */
                     select date_part('year',msd)::TEXT into cyear ;
                     select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
                     insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values 
                       (matchid,1,1,gvalue,cyear,cmonth) ;
                  elsif gfreq='2' then    /* By月 */
                     nseq = 1 ;
                     startdate = msd ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > med ;
                       insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values 
                          (matchid,nseq,nseq,gvalue,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 month' ;
                     end loop ;
                  else                    /* By年 */  
                     nseq = 1 ;
                     startdate = msd ;
                     loop
                       select date_part('year',startdate)::TEXT into cyear ;
                       select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                       exit when nseq > gtime or startdate > med ;
                       insert into cloudrent_escrow_fee(escrow_id,escrow_seq,escrow_period,escrow_applyfor_fee,escrow_applyfor_year,escrow_applyfor_month) values 
                        (matchid,nseq,nseq,gvalue,cyear,cmonth) ;
                       nseq = nseq + 1 ;
                       startdate = startdate + interval '1 year' ;
                     end loop ;
                  end if ;
                  select max(escrow_seq) into maxseq from cloudrent_escrow_fee where escrow_id=matchid ;
                  update cloudrent_escrow_fee set escrow_tot_period=maxseq where escrow_id=matchid ;
               end if ; 
           end if ;
           
           /* 生成 媒合費 itemkey=7 */
           itemkey = 7 ;
           select id into grantid from cloudrent_grant_fee where grant_item=itemkey and admin_area=adminarea  ;
           if grantid is not null then
              select grant_freq,grant_time,grant_max_value into gfreq,gtime,gvalue from cloudrent_grant_fee where id = grantid ;
              if gtime=-1 then
                 gtime=10000 ;
              end if ;
              if gfreq='1' then       /* By件 */
                 select date_part('year',msd)::TEXT into cyear ;
                 select lpad(date_part('month',msd)::TEXT,2,'0') into cmonth ;
                 insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,match_applyfor_month) values 
                   (matchid,1,gvalue,cyear,cmonth) ;
              elsif gfreq='2' then    /* By月 */
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,match_applyfor_month) values 
                     (matchid,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 month' ;
                 end loop ;
              else                    /* By年 */  
                 nseq = 1 ;
                 startdate = msd ;
                 loop
                   select date_part('year',startdate)::TEXT into cyear ;
                   select lpad(date_part('month',startdate)::TEXT,2,'0') into cmonth ;
                   exit when nseq > gtime or startdate > med ;
                   insert into cloudrent_contract_match_fee(match_id,match_seq,match_applyfor_fee,match_applyfor_year,macth_applyfor_month) values 
                     (matchid,nseq,gvalue,cyear,cmonth) ;
                   nseq = nseq + 1 ;
                   startdate = startdate + interval '1 year' ;
                 end loop ;
              end if ;
           end if ; 
           if msd is not null then
              select date_part('week',msd)::INT into weekseq ;
              update cloudrent_contract_match set week_seq=weekseq where id = matchid ; 
           end if ;    
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_lessee_grant(matchid int) cascade""")
        self._cr.execute("""create or replace function gen_lessee_grant(matchid int) returns void as $BODY$
         DECLARE
           lesseetype varchar ;
           lesseetype0rent int ;
           lesseetype1rent int ;
           lesseetype2rent int ;
           lesseegrant int ;
         BEGIN
           select lessee_type,lesseetype0_rent,lesseetype1_rent,lesseetype2_rent into
              lesseetype,lesseetype0rent,lesseetype1rent,lesseetype2rent from cloudrent_contract_match
                where id = matchid ;
            if lesseetype='1' then
               lesseegrant = 0 ;
            elsif lesseetype='2' then
               lesseegrant = coalesce(lesseetype0rent,0) - coalesce(lesseetype1rent,0) ;
            elsif lesseetype='3' then
               lesseegrant = coalesce(lesseetype0rent,0) - coalesce(lesseetype2rent,0) ;
            end if ;   
            update cloudrent_contract_match set lessee_grant=lesseegrant where id = matchid ;  
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_all_lessee_grant() cascade""")
        self._cr.execute("""create or replace function gen_all_lessee_grant() returns void as $BODY$
         DECLARE
           m_cur refcursor ;
           m_rec record ;
         BEGIN
           open m_cur for select id from cloudrent_contract_match ;
           loop
              fetch m_cur into m_rec ;
              exit when not found ;
              execute gen_lessee_grant(m_rec.id) ;
           end loop ;
           close m_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_xlsxtemp() cascade""")
        self._cr.execute("""create or replace function get_xlsxtemp() returns varchar as $BODY$
         DECLARE
           myres varchar ;
           myday varchar ;
           mysec varchar ;
         BEGIN
           select date_part('second',current_timestamp)::TEXT into mysec ;
           select REPLACE(mysec,'.','') into mysec ;
           select lpad(date_part('day',current_timestamp)::TEXT,2,'0') into myday ;
           myres = concat(myday,'_',mysec,'.xlsx') ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists get_docxtemp() cascade""")
        self._cr.execute("""create or replace function get_docxtemp() returns varchar as $BODY$
         DECLARE
           myres varchar ;
           myday varchar ;
           mysec varchar ;
         BEGIN
           select date_part('second',current_timestamp)::TEXT into mysec ;
           select REPLACE(mysec,'.','') into mysec ;
           select lpad(date_part('day',current_timestamp)::TEXT,2,'0') into myday ;
           myres = concat(myday,'_',mysec,'.docx') ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists get_report_twdate() cascade""")
        self._cr.execute("""drop function if exists get_report_twdate(reportdate date) cascade""")
        self._cr.execute("""create or replace function get_report_twdate(reportdate date) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            ty varchar ;
            tm varchar ;
            td varchar ;
          BEGIN
            select (date_part('year',reportdate)::INT - 1911)::TEXT into ty ;
            select date_part('month',reportdate)::TEXT into tm ;
            select date_part('day',reportdate)::TEXT into td ;
            myres = concat('製表日期: ',ty,' 年 ',tm,' 月 ',td,' 日') ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_enddate(mydate date) cascade""")
        self._cr.execute("""create or replace function get_enddate(mydate date) returns DATE as $BODY$
         DECLARE
           myres date ;
         BEGIN
           select mydate + interval '1 year' - interval '1 day' into myres ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_twymd(mydate date) cascade""")
        self._cr.execute("""create or replace function get_twymd(mydate date) returns varchar as $BODY$
          DECLARE
            myres varchar ;
            twy varchar ;
            twm varchar ;
            twd varchar ;
          BEGIN
            select (date_part('year',mydate)::INT - 1911)::TEXT into twy ;
            select lpad(date_part('month',mydate)::TEXT,2,'0') into twm ;
            select lpad(date_part('day',mydate)::TEXT,2,'0') into twd ;
            myres = concat(twy,'/',twm,'/',twd) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_ndmfee(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) cascade""")
        self._cr.execute("""create or replace function get_ndmfee(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) returns INT as $BODY$
         DECLARE
           myres int ;
         BEGIN
           if mytype = 'N' then       /* 公證費 */
              select sum(notarial_applyfor_fee) into myres from cloudrent_notarial_fee where notarial_id=mymatchid and
                 notarial_applyfor_year=myyear and notarial_applyfor_month=mymonth and is_applyfor != TRUE ;
           elsif mytype = 'D' then    /* 開發費 */
              select sum(develop_applyfor_fee) into myres from cloudrent_escrow_develop where develop_id=mymatchid and 
                 delevop_applyfor_year=myyear and develop_applyfor_month=mymonth and is_applyfor != TRUE ;
           elsif mytype = 'M' then    /* 媒合費 */
              select sum(match_applyfor_fee) into myres from cloudrent_contract_match_fee where match_id=mymatchid and 
                 match_applyfor_year=myyear and match_applyfor_month=mymonth and is_applyfor != TRUE ;  
           end if ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_gefee(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) cascade""")
        self._cr.execute("""create or replace function get_gefee(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) returns setof INT as $BODY$
         DECLARE
           myres int ;
           myres1 int ;
           myres2 int ;
         BEGIN
           if mytype = 'G' then          /*  包管費  */
              select sum(guarantee_applyfor_fee) into myres from cloudrent_guarantee_fee where guarantee_id=mymatchid and 
                guarantee_applyfor_year=myyear and guarantee_applyfor_month=mymonth and is_applyfor != TRUE ;
              select guarantee_period,guarantee_tot_period into myres1,myres2 from cloudrent_guarantee_fee where guarantee_id=mymatchid and 
                guarantee_applyfor_year=myyear and guarantee_applyfor_month=mymonth and is_applyfor != TRUE ;    
           elsif mytype = 'E' then       /*  代管費  */
              select sum(escrow_applyfor_fee) into myres from cloudrent_escrow_fee where escrow_id=mymatchid and 
                escrow_applyfor_year=myyear and escrow_applyfor_month=mymonth and is_applyfor != TRUE ;
              select escrow_applyfor_period,escrow_tot_period into myres1,myres2 from cloudrent_escrow_fee where escrow_id=mymatchid and 
                escrow_applyfor_year=myyear and escrow_applyfor_month=mymonth and is_applyfor != TRUE ;  
           end if ;
           if myres is null then
              myres = 0 ;
              myres1 = 0 ;
              myres2 = 0 ;
           end if ;
           return next myres ;
           return next myres1 ;
           return next myres2 ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists get_lessorgrant(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) cascade""")
        self._cr.execute("""create or replace function get_lessorgrant(mymatchid int,myyear varchar,mymonth varchar,mytype varchar) returns setof INT as $BODY$
        DECLARE
          myres int ;
          myres1 int ;
        BEGIN
          if mytype = 'S' then          /*  保險費  */
             select sum(real_insurance_fee),sum(ins_applyfor_fee) into myres,myres1 from cloudrent_safe_insurance_fee where safe_id=mymatchid and 
               ins_applyfor_year=myyear and ins_applyfor_month=mymonth and is_applyfor != TRUE ;    
          elsif mytype = 'G' then       /*  公證費  */
             select sum(real_notarial_fee),sum(notarial_applyfor_fee) into myres,myres1 from cloudrent_notarial_fee where notarial_id=mymatchid and 
               notarial_applyfor_year=myyear and notarial_applyfor_month=mymonth and is_applyfor != TRUE ;  
          elsif mytype = 'R' then       /* 修繕費 */
             select sum(real_repair_fee),sum(repair_applyfor_fee) into myres,myres1 from cloudrent_repair_fee where repair_id=mymatchid and 
               repair_year=myyear and repair_month=mymonth and is_applyfor != TRUE ;    
          end if ;    
          if myres is null then
             myres = 0 ;
             myres1 = 0 ;
          end if ;
          return next myres ;
          return next myres1 ;
        END;$BODY$
        LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists gen_agent_applyfor_report(agentid int,rdate date,ry varchar,rm varchar) cascade""")
        self._cr.execute("""create or replace function gen_agent_applyfor_report(agentid int,rdate date,ry varchar,rm varchar) returns void as $BODY$
         DECLARE
           m_cur refcursor ;
           m_rec record ;
           notarialfee float ;
           developfee float ;
           guaranteefee float ;
           matchfee float ;
           escrowfee float ;
           twy varchar ;
           twm varchar ;
           repy varchar ;
           repm varchar ;
           repd varchar ;
         BEGIN
             delete from cloudrent_agent_applyfor_report where escrow_no=agentid ;
             select sum(notarial_applyfor_fee) into notarialfee from cloudrent_notarial_fee 
                 where notarial_id in (select id from cloudrent_contract_match where match_year=ry and match_month=rm and escrow_no = agentid) 
                 and notarial_applyfor_year=ry and notarial_applyfor_month=rm and is_applyfor != TRUE ;
             select sum(develop_applyfor_fee) into developfee from cloudrent_escrow_develop 
                 where develop_id in (select id from cloudrent_contract_match where match_year=ry and match_month=rm and escrow_no = agentid)
                  and develop_applyfor_year=ry and develop_applyfor_month=rm  and is_applyfor != TRUE ;    
             select sum(guarantee_applyfor_fee) into guaranteefee from cloudrent_guarantee_fee 
                 where guarantee_id in (select id from cloudrent_contract_match where match_year=ry and match_month=rm and escrow_no = agentid)
                  and guarantee_applyfor_year=ry and guarantee_applyfor_month=rm  and is_applyfor != TRUE ;   
             select sum(match_applyfor_fee) into matchfee from cloudrent_contract_match_fee
                 where match_id in (select id from cloudrent_contract_match where match_year=ry and match_month=rm and escrow_no = agentid)
                  and match_applyfor_year=ry and match_applyfor_month=rm and is_applyfor != TRUE ;    
             select sum(escrow_applyfor_fee) into escrowfee from cloudrent_escrow_fee
                 where escrow_id in (select id from cloudrent_contract_match where match_year=ry and match_month=rm and escrow_no = agentid)
                  and escrow_applyfor_year=ry and escrow_applyfor_month=rm  and is_applyfor != TRUE ;     
             if notarialfee is null then
                notarialfee = 0 ;
             end if ;    
             if developfee is null then
                developfee = 0 ;
             end if ;
             if guaranteefee is null then
                guaranteefee = 0 ;
             end if ;
             if matchfee is null then
                matchfee = 0 ;
             end if ;
             if escrowfee is null then
                escrowfee = 0 ;
             end if ;
             twy = ry::INT - 1911 ;
             twm = rm ;
             select (date_part('year',rdate)::INT - 1911)::TEXT into repy ;
             select date_part('month',rdate)::TEXT into repm ;
             select date_part('day',rdate)::TEXT into repd ; 
             insert into cloudrent_agent_applyfor_report(tw_y,tw_m,tw_period,escrow_no,notarial_fee,
             develop_fee,guarantee_fee,match_fee,escrow_fee,report_y,report_m,report_d) values 
             (twy,twm,'',agentid,notarialfee,developfee,guaranteefee,matchfee,escrowfee,repy,repm,repd) ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_match_equip_part(leadid int) cascade""")
        self._cr.execute("""create or replace function gen_match_equip_part(leadid int) returns void as $BODY$
         DECLARE
           c_cur refcursor ;
           c_rec record ;
           matchid int ;
           ncount int ;
           eid int ;
         BEGIN
           select id into matchid from cloudrent_contract_match where crm_lead_id=leadid ;
           open c_cur for select * from cloudrent_crm_lead_equip_part where equip_id=leadid ;
           loop
              fetch c_cur into c_rec;
              exit when not found ;
              select count(*) into ncount from cloudrent_match_equip_part where equip_id = matchid and equip_no=c_rec.equip_no ;
              if ncount = 0 then
                  insert into cloudrent_match_equip_part(equip_id,equip_categ,equip_no,equip_qty,equip_status,equip_image1,equip_image2,equip_image3) values
                   (matchid,c_rec.equip_categ,c_rec.equip_no,c_rec.equip_qty,c_rec.equip_status,c_rec.equip_image1,c_rec.equip_image2,c_rec.equip_image3) ;
              else
                 select id into eid from cloudrent_match_equip_part where equip_id = matchid and equip_no=c_rec.equip_no ;
                 update cloudrent_match_equip_part set equip_categ=c_rec.equip_categ,equip_qty=c_rec.equip_qty,equip_status=c_rec.equip_status,
                       equip_image1=c_rec.equip_image1,equip_image2=c_rec.equip_image2,equip_image3=c_rec.equip_image3 where id = eid ;
              end if ;     
           end loop ;
           close c_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_applyfor_repair_fee(matchid int) cascade""")
        self._cr.execute("""create or replace function get_applyfor_repair_fee(matchid int) returns varchar as $BODY$
         DECLARE
           ncount int ;
           myres varchar ;
         BEGIN
           select count(*) into ncount from cloudrent_repair_fee where repair_id=matchid and repair_applyfor_fee > 0 and is_applyfor=TRUE ;
           if ncount > 0 then
              myres = '√' ;
           else
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_applyfor_rgrant_fee(matchid int) cascade""")
        self._cr.execute("""create or replace function get_applyfor_grant_fee(matchid int) returns varchar as $BODY$
         DECLARE
           ncount int ;
           myres varchar ;
         BEGIN
           select count(*) into ncount from cloudrent_grant_rent where grant_id=matchid and applyfor_rent_fee > 0 and is_applyfor=TRUE ;
           if ncount > 0 then
              myres = '√' ;
           else
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genfamilyline(memberid int) cascade""")
        self._cr.execute("""create or replace function genfamilyline(memberid int) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           nseq int ;
         BEGIN
           nseq = 1 ;
           open l_cur for select id,family_seq from cloudrent_lessee_family_line where family_id=memberid order by id;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             update cloudrent_lessee_family_line set family_seq = nseq where id = l_rec.id ;
             nseq = nseq + 1 ; 
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genfamilyrealestate(memberid int) cascade""")
        self._cr.execute("""create or replace function genfamilyrealestate(memberid int) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           nseq int ;
         BEGIN
           nseq = 1 ;
           open l_cur for select id,family_seq from cloudrent_lessee_family_realestate where family_id=memberid order by id;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             update cloudrent_lessee_family_realestate set family_seq = nseq where id = l_rec.id ;
             nseq = nseq + 1 ; 
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genfamilyassets(memberid int) cascade""")
        self._cr.execute("""create or replace function genfamilyassets(memberid int) returns void as $BODY$
         DECLARE
           l_cur refcursor ;
           l_rec record ;
           nseq int ;
         BEGIN
           nseq = 1 ;
           open l_cur for select id,family_seq from cloudrent_lessee_family_assets where family_id=memberid order by id;
           loop
             fetch l_cur into l_rec ;
             exit when not found ;
             update cloudrent_lessee_family_assets set family_seq = nseq where id = l_rec.id ;
             nseq = nseq + 1 ; 
           end loop ;
           close l_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_twyy_mm_dd(mydate date) cascade""")
        self._cr.execute("""create or replace function gen_twyy_mm_dd(mydate date) returns setof varchar as $BODY$
          DECLARE
            yy varchar ;
            mm varchar ;
            dd varchar ;
          BEGIN
            if mydate is not null then
               select (date_part('year',mydate)::INT - 1911)::TEXT into yy ;
               select date_part('month',mydate)::TEXT into mm ;
               select date_part('day',mydate)::TEXT into dd ;
            else
               yy = ' ' ;
               mm = ' ' ;
               dd = ' ' ;
            end if ;
            return next yy ;
            return next mm ;
            return next dd ;
          END;$BODY$
          LANGUAGE plpgsql;
           """)

        self._cr.execute("""drop function if exists gendocline(leadid int,docid int) cascade""")
        self._cr.execute("""create or replace function gendocline(leadid int,docid int) returns INT as $BODY$
         DECLARE
           myres int ;
           ncount int ;
         BEGIN
           select count(*) into ncount from cloudrent_lessor_doc_line where doc_id=leadid and doc_name=docid ;
           if ncount = 0 then
              insert into cloudrent_lessor_doc_line(doc_id,doc_name) values (leadid,docid) ;
           end if ;
           select max(id) into myres from cloudrent_lessor_doc_line where doc_id=leadid and doc_name=docid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gendocline1(matchid int,docid int) cascade""")
        self._cr.execute("""create or replace function gendocline1(matchid int,docid int) returns INT as $BODY$
         DECLARE
           myres int ;
           ncount int ;
         BEGIN
           select count(*) into ncount from cloudrent_match_doc_line where doc_id=matchid and doc_name=docid ;
           if ncount = 0 then
              insert into cloudrent_match_doc_line(doc_id,doc_name) values (matchid,docid) ;
           end if ;
           select max(id) into myres from cloudrent_match_doc_line where doc_id=matchid and doc_name=docid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_grant4_value(lesseetype varchar,adminarea varchar) cascade""")
        self._cr.execute("""create or replace function get_grant4_value(lesseetype varchar,adminarea varchar) returns setof float as $BODY$
         DECLARE
           ncount int ;
           myres float ;
         BEGIN
           select count(*) into ncount from cloudrent_grant_fee where grant_item=4 and lessee_type=lesseetype and admin_area=adminarea ;
           if ncount > 0 then
              select discount_rate into myres from cloudrent_grant_fee where grant_item=4 and lessee_type=lesseetype and admin_area=adminarea ;
              return next myres ;
              select grant_max_value into myres from cloudrent_grant_fee where grant_item=4 and lessee_type=lesseetype and admin_area=adminarea ;
              return next myres ;
           else
              return next 0.000 ;
              return next 0 ;
           end if ; 
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpicrec() cascade""")
        self._cr.execute("""create or replace function genallpicrec() returns void as $BODY$
         DECLARE
           s_cur refcursor ;
           s_rec record ;
           b_cur refcursor ;
           b_rec record ;
           ncount int ;
         BEGIN
           open s_cur for select id from crm_lead ;
           loop
             fetch s_cur into s_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_sitecheck_pic_line where sitecheck_id = s_rec.id ;
             if ncount = 0 then
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,1,'1','門牌及大門') ;
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,2,'1','衛浴設備[馬桶/洗面盆/浴缸]') ;
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,3,'1','出入口及樓梯間') ;
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,4,'1','滅火器/獨立型偵煙器/火警警報器') ;  
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,5,'1','熱水器') ; 
                insert into cloudrent_sitecheck_pic_line(sitecheck_id,sequence,sitecheck_type,sitecheck_desc) values
                 (s_rec.id,6,'1','室內設備') ; 
             end if ;
           end loop ;
           close s_cur ;
           open b_cur for select id from cloudrent_build ;
           loop
             fetch b_cur into b_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_build_line where build_id = b_rec.id ;
             if ncount = 0 then
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,1,'1','門牌及大門') ;
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,2,'1','衛浴設備[馬桶/洗面盆/浴缸]') ;
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,3,'1','出入口及樓梯間') ;
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,4,'1','滅火器/獨立型偵煙器/火警警報器') ;  
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,5,'1','熱水器') ; 
                insert into cloudrent_build_line(build_id,sequence,pic_type,build_desc) values
                 (b_rec.id,6,'1','室內設備') ; 
             end if ;
           end loop ;
           close b_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_tot_repair_fee(repdate date,matchid int) cascade""")
        self._cr.execute("""create or replace function get_tot_repair_fee(repdate date,matchid int) returns INT as $BODY$
        DECLARE
          myres int ;
          cyear varchar ;
          buildid int ;
        BEGIN
          select object_no1 into buildid from cloudrent_contract_match where id = matchid ;
          if buildid is not null then 
              select date_part('year',repdate)::TEXT into cyear ;
              select sum(repair_fee) into myres from cloudrent_build_repair_line where repair_id=buildid and repair_year=cyear ;
          end if ;   
          if myres is null then
             myres = 0 ;  
          end if ;
          return myres ;
        END;$BODY$
        LANGUAGE plpgsql;
        """)

        self._cr.execute("""drop function if exists get_contract_tag(docid int) cascade""")
        self._cr.execute("""create or replace function get_contract_tag(docid int) returns INT as $BODY$
         DECLARE
           myres int ;
           mydocid int ;
         BEGIN
           select name1 into mydocid from cloudrent_doc_filename where id = docid ;
           select contract_tag into myres from cloudrent_contract_data where id = mydocid ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_btom_equip_part(objno1 int,matchid int) cascade""")
        self._cr.execute("""create or replace function gen_btom_equip_part(objno1 int,matchid int) returns void as $BODY$
         DECLARE
           b_cur refcursor ;
           b_rec record ;
           ncount int ;
           eid int ;
         BEGIN
           open b_cur for select * from cloudrent_build_equip_part where equip_id=objno1 ;
           loop
             fetch b_cur into b_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_match_equip_part where equip_no=b_rec.equip_no and equip_id=matchid ;
             if ncount = 0 then
                insert into cloudrent_match_equip_part(equip_id,equip_categ,equip_no,equip_qty,equip_status,equip_image1,equip_image2,equip_image3) values
                 (matchid,b_rec.equip_categ,b_rec.equip_no,b_rec.equip_qty,b_rec.equip_status,b_rec.equip_image1,b_rec.equip_image2,b_rec.equip_image3) ;
             else
                select id into eid from cloudrent_match_equip_part where equip_no=b_rec.equip_no and equip_id=matchid ;
                update cloudrent_match_equip_part set equip_categ=b_rec.equip_categ,equip_qty=b_rec.equip_qty,equip_status=b_rec.equip_status,
                   equip_image1=b_rec.equip_image1,equip_image2=b_rec.equip_image2,equip_image3=b_rec.equip_image3 where id = eid ;
             end if ;
           end loop ;
           close b_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_ctob_equip_part(buildid int,leadid int) cascade""")
        self._cr.execute("""create or replace function gen_ctob_equip_part(buildid int,leadid int) returns void as $BODY$
         DECLARE
           c_cur refcursor ;
           c_rec record ;
           ncount int ;
           eid int ;
         BEGIN
           open c_cur for select * from cloudrent_crm_lead_equip_part where equip_id=leadid ;
           loop
             fetch c_cur into c_rec ;
             exit when not found ;
             select count(*) into ncount from cloudrent_build_equip_part where equip_no=c_rec.equip_no and equip_id=buildid ;
             if ncount = 0 then
                insert into cloudrent_build_equip_part(equip_id,equip_categ,equip_no,equip_qty,equip_status,equip_image1,equip_image2,equip_image3) values
                 (buildid,c_rec.equip_categ,c_rec.equip_no,c_rec.equip_qty,c_rec.equip_status,c_rec.equip_image1,c_rec.equip_image2,c_rec.equip_image3) ;
             else
                select id into eid from cloudrent_build_equip_part where equip_no=c_rec.equip_no and equip_id=buildid ;
                update cloudrent_build_equip_part set equip_categ=c_rec.equip_categ,equip_qty=c_rec.equip_qty,equip_status=c_rec.equip_status,
                   equip_image1=c_rec.equip_image1,equip_image2=c_rec.equip_image2,equip_image3=c_rec.equip_image3 where id = eid ;
             end if ;
           end loop ;
           close c_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkrenewstatus(matchid int) cascade""")
        self._cr.execute("""create or replace function checkrenewstatus(matchid int) returns CHAR as $BODY$
          DECLARE
            myres CHAR ;
            renew1 Boolean ;
            renew2 Boolean ;
          BEGIN
            select coalesce(lessee_renew1,FALSE),coalesce(lessee_renew2,FALSE) into renew1,renew2 from cloudrent_contract_match where id=matchid ;
            if (renew1 is null or renew1=FALSE) and (renew2 is null or renew2=FALSE) then
                myres = '0' ;
            elsif renew1=TRUE and (renew2 is null or renew2=FALSE) then
                myres = '1';
            elsif renew2 = TRUE then
                myres = '2';
            end if ;  
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gen_contract_renew(cid int,cid1 int) cascade""")
        self._cr.execute("""create or replace function gen_contract_renew(cid int,cid1 int) returns void as $BODY$
         DECLARE
           renew1 Boolean ;
           renew2 Boolean ;
           msdate date ;
           msdate1 date ;
           medate1 date ;
           msdate2 date ;
           medate2 date ;
           renewym varchar ;
           lesseetype char ;
           renewd date ;
           renewy varchar ;
           renewm varchar ;
           renewname varchar ;
         BEGIN
           select coalesce(lessee_renew1,FALSE),coalesce(lessee_renew2,FALSE),match_start_date,lessee_type,match_no into renew1,renew2,msdate,lesseetype,renewname from cloudrent_contract_match where id = cid ;
           if msdate is not null then
                 select (msdate + interval '1 year') into msdate1 ;
                 
                 select (msdate1 + interval '1 year' - interval '1 day') into medate1 ;
                 select (medate1 - interval '3 month') into renewd ;
                 select date_part('year',renewd)::TEXT into renewy ;
                 select lpad(date_part('month',renewd)::TEXT,2,'0') into renewm ;
                 renewym = concat(renewy,'-',renewm) ;
                 select (msdate1 + interval '1 year') into msdate2 ;
                 select (msdate2 + interval '1 year' - interval '1 day') into medate2 ;
              if renew1=FALSE and renew2=FALSE then   /* 續約第一年  */
                 renewname = concat('RENEW1_',renewname) ;
                 update cloudrent_contract_match set match_no=renewname,lessee_renew1=TRUE ,lessee_renew2=FALSE,match_start_date=msdate1,match_end_date=medate1,lessee_visit=null,
                   lessee_visit1=null,lessee_visit2=null,lessee_visit3=null,entrust_start_date=msdate1,entrust_end_date=medate1,origin_lessee_type=lesseetype,new_lessee_type=lesseetype,
                   renew_start_date=msdate2,renew_end_date=medate2,renew_ym=renewym where id = cid1 ; 
              elsif renew1=TRUE and renew2=FALSE then /* 續約第二年  */
                 renewname = concat('RENEW2_',renewname) ;
                 update cloudrent_contract_match set match_no=renewname,lessee_renew1=FALSE ,lessee_renew2=TRUE ,match_start_date=msdate1,match_end_date=medate1,lessee_visit=null,
                   lessee_visit1=null,lessee_visit2=null,lessee_visit3=null,entrust_start_date=msdate1,entrust_end_date=medate1,origin_lessee_type=lesseetype,new_lessee_type=lesseetype,
                   renew_ym=renewym,renew_start_date=null,renew_end_date=null  where id = cid1 ;
              end if ;
           end if ;   
           update cloudrent_contract_match set renew1=cid where id = cid1 ;
           execute renew_match_line(cid1) ;
           execute genmatchfee(cid1) ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists renew_match_line(matchid int) cascade""")
        self._cr.execute("""create or replace function renew_match_line(matchid int) returns void as $BODY$
         DECLARE
           ncount int ;
         BEGIN
           delete from cloudrent_safe_insurance_fee where safe_id=matchid ;
           delete from cloudrent_notarial_fee where notarial_id=matchid ;
           delete from cloudrent_repair_fee where repair_id=matchid ;
           delete from cloudrent_grant_rent where grant_id=matchid ;
           delete from cloudrent_escrow_develop where develop_id=matchid ;
           delete from cloudrent_guarantee_fee where guarantee_id=matchid ;
           delete from cloudrent_contract_match_fee where match_id=matchid ;
           delete from cloudrent_escrow_fee where escrow_id=matchid ;
           delete from cloudrent_match_doc_line where doc_id=matchid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getonlinematch() cascade""")
        self._cr.execute("""create or replace function getonlinematch() returns setof INT as $BODY$
         DECLARE
           m_cur refcursor ;
           m_rec record ;
           mynowday date ;
         BEGIN
           select current_timestamp::DATE into mynowday ;
           open m_cur for select id from cloudrent_contract_match where quit_date is null and id not in 
              (select renew1 from cloudrent_contract_match where renew1 is not null) and 
              (match_start_date <= mynowday and match_end_date >= mynowday) order by id;
           loop
             fetch m_cur into m_rec ;
             exit when not found ;
             return next m_rec.id ;
           end loop ;
           close m_cur ;   
         END;$BODY$
         language plpgsql;""")

        self._cr.execute("""drop function if exists getmatchenable(matchid int) cascade""")
        self._cr.execute("""create or replace function getmatchenable(matchid int) returns Boolean as $BODY$
         DECLARE
           msd date ;
           med date ;
           lt Boolean ;
           myres Boolean ;
         BEGIN
           select match_start_date,match_end_date,lessee_terminate into msd,med,lt 
              from cloudrent_contract_match where id = matchid ;
           if msd <= current_timestamp::DATE and med >= current_timestamp::DATE and 
                (lt is null or lt = FALSE) then
              myres = TRUE ;
           else
              myres = FALSE ;
           end if ;  
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


