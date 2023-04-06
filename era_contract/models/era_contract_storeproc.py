# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, api
from odoo.exceptions import UserError

class EraContractStoreproc(models.Model):
    _name = "era.contract_storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists chk_member(projid int,pid varchar) cascade""")
        self._cr.execute("""create  or replace function chk_member(projid int,pid varchar) returns varchar as $BODY$
          DECLARE
            ncount int ;
            ncount1 int ;
            houseid int ;
            mainhouseid int ;
            isused Boolean ;
            myres varchar ;
            /* mres '1'表新member  '2'已建檔 member但此案場不存在 '3'已建檔 member但此案場已存在且入住 '4'已建檔 member但此案場已存在但未入住 */
          BEGIN           
            select count(*) into ncount from era_household_member where member_pid=pid ;
            if ncount > 0 then
               select house_id into houseid from era_household_member where member_pid=pid ;
               select house_id,in_used into mainhouseid,isused from era_household_house_line where id = houseid ;
               if mainhouseid = projid and isused = true then
                  myres = '3' ;
               elsif mainhouseid = projid and (isused = false or isused is null) then  
                  myres = '4' ;  
               else
                  myres = '2' ;
               end if ;
            else
               myres = '1' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractmember(conid int,contype varchar) cascade""")
        self._cr.execute("""create or replace function gencontractmember(conid int,contype varchar) returns void as $BODY$
          DECLARE
            hl_cur refcursor ;
            hl_rec record ;
            pid varchar ;
            memberid int ;
            deposit float ;
            endrental date ;
          BEGIN
            select member_pid into pid from era_contract where id = conid ;
            select max(id) into memberid from era_household_member where member_pid=pid;
            open hl_cur for select * from era_household_member where id = memberid ;
            loop
               fetch hl_cur into hl_rec ;
               exit when not found ;
               update era_contract set member_name=hl_rec.member_name,member_email=hl_rec.member_email,house_rental_fee=hl_rec.house_rental_fee,
                      house_rental_desc=hl_rec.house_rental_desc,house_management_fee=hl_rec.house_management_fee,
                      house_management_desc=hl_rec.house_management_desc,parking_space_rent=hl_rec.parking_space_rent,
                      parking_rent_desc=hl_rec.parking_rent_desc,parking_management=hl_rec.parking_management,
                      parking_management_desc=hl_rec.parking_management_desc,lo_parking_management=hl_rec.lo_parking_management,
                      lo_parking_desc=hl_rec.lo_parking_desc,water_fee=hl_rec.water_fee,member_sex=hl_rec.member_sex,
                      member_age=hl_rec.member_age,member_amount=hl_rec.member_amount,member_address1=hl_rec.member_address1,
                      member_address2=hl_rec.member_address2,member_phone1=hl_rec.member_phone1,member_phone2=hl_rec.member_phone2,
                      member_phone3=hl_rec.member_phone3,member_phone4=hl_rec.member_phone4,member_desc=hl_rec.member_desc
                      where id = conid ;
               if hl_rec.user_id is not null then
                  update era_contract set user_id=hl_rec.user_id,member_deposit=deposit,member_no=hl_rec.member_no where id=conid;
               end if ;       
               if hl_rec.house_id is not null then
                  select hl_rec.end_rental::DATE + interval '1 year' into endrental ;
                  update era_contract set house_id=hl_rec.house_id,house_id1=hl_rec.house_id,start_rental=hl_rec.end_rental,end_rental=endrental where id=conid;
               end if ;
               if contype='3' then
                  select sum(deposit_amount) into deposit from era_member_deposit where account_id=memberid ;
                  update era_contract set income_date=hl_rec.income_date  where id=conid;
               end if ;       
            end loop ;
            close hl_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists run_contract_payment(conid int) cascade""")
        self._cr.execute("""create or replace function run_contract_payment(conid int) returns void as $BODY$
         DECLARE
           cym varchar ;
           ncount int ;
           srental date ;
           erental date ;
           mydate date ;
           cyear varchar ;
           cmonth varchar ;
           cnyear varchar ;
           cnmonth varchar ;
           cnym varchar ;
           rentalfee float ;
           rentaldesc varchar ;
           managementfee float ;
           managementdesc varchar ;
           parkspace float ;
           parkdesc varchar ;
           parkmanagement float ;
           parkmandesc varchar ;
           loparkmanagement float ;
           loparkdesc varchar ;
           waterfee float ;  
           ceyear varchar ;
           cemonth varchar ;
           ceym varchar ;
           emeter_cur refcursor ;
           emeter_rec record ;
           houseid int ;
           incomedate date ;
           nmonth int ;
           nnum int ;
           nday int ;
           ncount1 int ;
           memberpid varchar ;
           memberid int ;
           mynow timestamp ;
           memberdeposit int ;
         BEGIN
            select current_timestamp into mynow ;
            select member_pid into memberpid from era_contract where id = conid ;
            select max(id) into memberid from era_household_member where member_pid=memberpid ;
            select start_rental,end_rental,coalesce(house_rental_fee,0),coalesce(house_management_fee,0),coalesce(parking_space_rent,0),coalesce(parking_management,0),coalesce(water_fee,0),coalesce(lo_parking_management,0),coalesce(member_deposit,0) into 
             srental,erental,rentalfee,managementfee,parkspace,parkmanagement,waterfee,loparkmanagement,memberdeposit from era_contract where id=conid ;
            select coalesce(house_rental_desc,' '),coalesce(house_management_desc,' '),coalesce(parking_rent_desc,' '),coalesce(parking_management_desc,' '),coalesce(lo_parking_desc,' ') into
               rentaldesc,managementdesc,parkdesc,parkmandesc,loparkdesc from era_contract where id=conid ;
           update era_member_contract set contract_status='2' where contract_id=conid and member_id=memberid ;  
           insert into era_member_contract(member_id,contract_id,start_rental,end_rental,create_date,contract_status) values (memberid,conid,srental,erental,mynow,'1') ;  
           update era_household_member set start_rental=srental,end_rental=erental,house_rental_fee=rentalfee,house_management_fee=managementfee,parking_space_rent=parkspace,
              parking_management=parkmanagement,water_fee=waterfee,lo_parking_management=loparkmanagement,house_rental_desc=rentaldesc,house_management_desc=managementdesc,
              parking_rent_desc=parkdesc,parking_management_desc=parkmandesc,lo_parking_desc=loparkdesc,member_deposit=memberdeposit,contract_id=conid where id = memberid ;
           select date_part('year',now())::TEXT into cnyear ;
           select lpad(date_part('month',now())::TEXT,2,'0') into cnmonth ;
           cnym = concat(cnyear,'-',cnmonth) ;
           select date_part('year',erental)::TEXT into ceyear ;
           select lpad(date_part('month',erental)::TEXT,2,'0') into cemonth ;
           ceym = concat(ceyear,'-',cemonth) ;
           select (extract('day' from age(erental,srental)))::INT into nday ;
           select (extract('year' from age(erental,srental))*12 + extract('month' from age(erental,srental)))::INT into nmonth ;
           if nday > 15 then
              nmonth = nmonth + 1 ;
           end if ;
           nnum = 0 ;

           mydate = srental ;
           while nmonth > nnum loop 
             select date_part('year',mydate)::TEXT into cyear ;
             select lpad(date_part('month',mydate)::TEXT,2,'0') into cmonth ;
             cym = concat(cyear,'-',cmonth) ;
             select count(*) into ncount from era_member_account where account_ym=cym and member_id=memberid ;
             if ncount > 0 then
                if cym <= cnym then
                   update era_member_account set house_rental_fee=rentalfee,house_management_fee=managementfee,parking_space_rent=parkspace,parking_management=parkmanagement,water_fee=waterfee,account_active=True,lo_parking_management=loparkmanagement
                      where account_ym=cym and member_id=memberid ;
                else
                   update era_member_account set house_rental_fee=rentalfee,house_management_fee=managementfee,parking_space_rent=parkspace,parking_management=parkmanagement,water_fee=waterfee,account_active=False,lo_parking_management=loparkmanagement
                      where account_ym=cym and member_id=memberid ;
                end if ;
             else
                if cym <= cnym then
                   insert into era_member_account(member_id,account_ym,house_rental_fee,house_management_fee,parking_space_rent,parking_management,lo_parking_management,water_fee,account_active) values
                    (memberid,cym,rentalfee,managementfee,parkspace,parkmanagement,loparkmanagement,waterfee,True) ;
                else
                   insert into era_member_account(member_id,account_ym,house_rental_fee,house_management_fee,parking_space_rent,parking_management,lo_parking_management,water_fee,account_active) values
                    (memberid,cym,rentalfee,managementfee,parkspace,parkmanagement,loparkmanagement,waterfee,False) ;
                end if ;
             end if ;
             mydate = mydate + interval '1 month' ;
             nnum = nnum + 1 ;
           end loop ; 
           select id into houseid from era_household_house_line where member_id=memberid ;
           select income_date into incomedate from era_household_member where id = memberid ;
           open emeter_cur for select * from era_household_electric_meter where emeter_id=houseid ;
           loop
              fetch emeter_cur into emeter_rec ;
              exit when not found ;
              select count(*) into ncount from era_member_income_emeter where member_id=memberid and emeter_id=emeter_rec.id ;
              if ncount=0 then
                 insert into era_member_income_emeter(member_id,emeter_id,start_date) values (memberid,emeter_rec.id,incomedate) ;
              end if ;
           end loop ;
           close emeter_cur ;
          /* select count(*) into ncount1 from era_member_payment where member_id=memberid ;
           if ncount1 = 0 then
              insert into era_member_payment(member_id,house_id) values (memberid,houseid) ;
           end if ; */
           update era_contract set states='2' where id=conid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractemeter(conid int) cascade""")
        self._cr.execute("""create or replace function gencontractemeter(conid int) returns void as $BODY$
          DECLARE
            houseid int ;
            emeter_cur refcursor ;
            emeter_rec record ;
            ncount int ;
            startscale float ;
          BEGIN
            /* delete from era_contract_emeter where contract_id=conid ; */
            select house_id into houseid from era_contract where id=conid ;
            open emeter_cur for select * from era_household_electric_meter where emeter_id=houseid ;
            loop
              fetch emeter_cur into emeter_rec ;
              exit when not found ;
              select count(*) into ncount from era_contract_emeter where contract_id=conid and emeter_id=emeter_rec.id ;
              if ncount = 0 then
                 select max(used_scale) into startscale from era_household_used_line where used_emeter_id=emeter_rec.id ;
                 insert into era_contract_emeter(contract_id,emeter_id,start_scale) values (conid,emeter_rec.id,startscale) ;
              end if ;   
            end loop ;
            close emeter_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chkcontractemeter(conid int) cascade""")
        self._cr.execute("""create or replace function chkcontractemeter(conid int) returns Boolean as $BODY$
          DECLARE
            myres boolean ;
            ncount int ;
            newscale float ;
          BEGIN
            select count(*) into ncount from era_contract_emeter where contract_id=conid ;
            if ncount > 0 then
               select sum(start_scale) into newscale from era_contract_emeter where contract_id=conid ;
               if newscale > 0 then
                  myres = True ;
               else
                  myres = False ;
               end if ;
            else
               myres = True ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gennewcontractemeter(conid int) cascade""")
        self._cr.execute("""create or replace function gennewcontractemeter(conid int) returns void as $BODY$
          DECLARE
            ncount int ;
            emeter_cur refcursor ;
            emeter_rec record ;
            memberno varchar ;
            memberid int ;
            srental date ;
            erental date ;
            uscale Float ;
          BEGIN
            select coalesce(member_no,' '),start_rental,end_rental into memberno,srental,erental from era_contract where id=conid ;
            if memberno != ' ' then
               select id into memberid from era_household_member where member_no=memberno ;
               open emeter_cur for select * from era_contract_emeter where contract_id=conid ;
               loop
                 fetch emeter_cur into emeter_rec ;
                 exit when not found ;
                 select max(used_scale) into uscale from era_household_used_line where used_emeter_id=emeter_rec.emeter_id ;
                 update era_member_income_emeter set start_scale=emeter_rec.start_scale,
                 current_scale=uscale,start_date=srental,end_date=erental,in_used=True
                  where member_id=memberid and emeter_id=emeter_rec.emeter_id ;
               end loop ;
               close emeter_cur ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmemberemetercopynew(houseid int,houseid1 int,memberid int) cascade""")
        self._cr.execute("""drop function if exists genmemberemetercopynew(houseid int,houseid1 int,memberid int,conid int) cascade""")
        self._cr.execute("""create or replace function genmemberemetercopynew(houseid int,houseid1 int,memberid int,conid int) returns void as $BODY$
          DECLARE
            emeterid int ;
            ncount int ;
            houseid int ;
            em_cur refcursor ;
            em_rec record ;
            userid int ;
            maxid int ;
            currentscale float ;
            startscale float ;
            conincondate date ;
            constartdate date ;
            conenddate date ;
          BEGIN  
            select income_date,start_rental,end_rental into conincondate,constartdate,conenddate
               from era_contract where id = conid ;
            update era_member_income_emeter set in_used=FALSE where member_id=memberid ;
            update era_member_income_emeter set end_date=constartdate where end_date is null ;
           /* open em_cur for select * from era_household_electric_meter where emeter_id = houseid ;
            loop
              fetch em_cur into em_rec ;
              exit when not found ;
              select count(*) into ncount from era_member_income_emeter where member_id=memberid and emeter_id=em_rec.id ;   
              if ncount = 0 then
                insert into era_member_income_emeter(member_id,emeter_id,current_scale,start_scale,in_used) values (memberid,em_rec.id,currentscale,currentscale,FALSE) ;
              end if ;
            end loop ;
            close em_cur ;*/
            open em_cur for select * from era_household_electric_meter where emeter_id = houseid1 ;
            loop
              fetch em_cur into em_rec ;
              exit when not found ;
              select max(id) into maxid from era_household_used_line where used_id=houseid1 and used_emeter_id=em_rec.id ;
              select used_scale into currentscale from era_household_used_line where id = maxid ;
              select count(*) into ncount from era_member_income_emeter where member_id=memberid and emeter_id=em_rec.id ;   
              if ncount = 0 then
                insert into era_member_income_emeter(member_id,emeter_id,current_scale,start_scale,in_used,start_date,end_date) values (memberid,em_rec.id,currentscale,currentscale,TRUE,constartdate,conenddate) ;
              end if ;
            end loop ;
            close em_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractactiondone() cascade""")
        self._cr.execute("""create or replace function gencontractactiondone() returns void as $BODY$
          DECLARE
            con_cur refcursor ;
            con_rec record ;
            userid int ;
            memberno varchar ;
            houseid int ;
            houseid1 int ;
            nowtoday date ;
            houseno varchar ;
            memberpid varchar ;
            partnerid int ;
            newmemberno varchar ;
            m_cur refcursor ;
            m_rec record ;
            em_cur refcursor ;
            em_rec record ;
            currentscale float ;
            maxid int ;
          BEGIN
            select current_timestamp::DATE into nowtoday ;
            open con_cur for select * from era_contract_action_done where action_status='NO' and action_date <= nowtoday and active=True ;
            loop
               fetch con_cur into con_rec ;
               exit when not found ;
               select house_id,house_id1 into houseid,houseid1 from era_contract where id = con_rec.contract_id ;
               select member_no,member_pid into memberno,memberpid from era_household_member where id = con_rec.member_id ;
               select id,partner_id into userid,partnerid from res_users where login=memberno ;
               update era_household_house_line set member_id=con_rec.member_id,user_id=userid,in_used=True where id=houseid1 ;
               update era_household_member set user_id=userid where id = con_rec.member_id  ;
               if con_rec.action_type='IN' then          /*  租戶入住  */
                  update era_household_member set contract_id=con_rec.contract_id where id = con_rec.member_id;
                  if con_rec.change_houseid=TRUE then    /* 續約換房 */
                     select house_no into houseno from era_household_house_line where id = houseid1 ;
                     newmemberno = concat(houseno,'-',memberpid) ;
                     update res_users set login=newmemberno where id=userid ;
                     update res_partner set name=newmemberno where id = partnerid ;
                     update era_household_member set member_no=newmemberno,house_id=houseid1 where id = con_rec.member_id ;
                     update era_household_house_line set member_id=null,user_id=null,in_used=FALSE where id = houseid ;
                     execute genmemberemetercopynew(houseid,houseid1,con_rec.member_id,con_rec.contract_id) ;
                    /* open m_cur for select * from era_member_income_emeter where member_id=con_rec.member_id ;
                     loop
                       fetch m_cur into m_rec ;
                       exit when not found ;
                       select max(id) into maxid from era_household_used_line where used_emeter_id=m_rec.emeter_id ;
                       select used_scale into currentscale from era_household_used_line where id = maxid ;
                       update era_member_income_emeter set current_scale=currentscale where id=m_rec.id ;
                     end loop ;
                     close m_cur ;*/
                  end if ;   
                   
               elsif con_rec.action_type='OUT' then      /*  租戶退租  */
                  update era_household_house_line set member_id=null,user_id=null,in_used=False where id=houseid1 ;
                  update res_users set active=False where id=userid ;
                  update era_contract set states='3' where id = con_rec.contract_id ;
               end if ;
               update era_contract_action_done set action_status='YES' where id = con_rec.id ;
            end loop ;
            close con_cur ;  
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpaydeposit(payid int,conid int,payap float) cascade""")
        self._cr.execute("""create or replace function genpaydeposit(payid int,conid int,payap float) returns void as $BODY$
        DECLARE
          ncount int ;
          item_cur refcursor ;
          item_rec record ;
          myyear varchar ;
          conno varchar ;
          houseid int ;
          memberid int ;
          userid int ;
          accountdate date ;
        BEGIN
          select house_id into houseid from era_contract where id = conid ;
          select member_id into memberid from era_household_house_line where id =houseid ;
          update era_member_deposit set deposit_status='2' where account_id=memberid ;
          select payment_year,user_id,account_date into myyear,userid,accountdate from era_member_payment where id = payid ;
          open item_cur for select * from era_payment_item where pay_code='10' ;   /* 押金 */
          loop 
            fetch item_cur into item_rec ;
            exit when not found ;
            select count(*) into ncount from era_member_payment_line where payment_id=payid and pay_code=item_rec.pay_code ;
            if ncount=0 then
               insert into era_member_payment_line(payment_id,pay_name,pay_code,pay_year,pay_active,pay_ap,pay_status) values (payid,item_rec.name,item_rec.pay_code,myyear,True,payap,'2') ;
              /* insert into era_member_deposit(account_id,account_date,deposit_amount,user_id,member_payment_id,deposit_status)
                 values (memberid,accountdate,payap,userid,payid,'1') ;
            else
                update era_member_deposit set deposit_amount=payap,deposit_status='1' where account_id=memberid and member_payment_id=payid ; */
            end if ;   
          end loop ;
          close item_cur ;
          select name into conno from era_contract where id=conid ;
          update era_member_payment set payment_memo=concat('合約:',conno,'押金直接核銷入帳') where id = payid ;   
        END;$BODY$
        LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genconactdone(conid int,contype char) cascade""")
        self._cr.execute("""drop function if exists gencontractdone(conid int,contype char) cascade""")
        self._cr.execute("""create or replace function gencontractdone(conid int,contype char) returns void as $BODY$
          DECLARE
            memberid int ;
            memberno varchar ;
            srental date ;
            erental date ;
            erental1 date ;
            ncount int ;
            changehid Boolean ;
          BEGIN
            /* contype='1' 新約   contype='2' 續約  */
            select member_no into memberno from era_contract where id=conid ;
            select id into memberid from era_household_member where member_no=memberno ;
            select start_rental,end_rental into srental,erental from era_contract where id=conid ;
            select erental + interval '7 day' into erental1 ;
            if contype='1' then
                insert into era_contract_action_done(action_date,action_type,member_id,contract_id,action_status,active,change_houseid) values
                 (srental,'IN',memberid,conid,'NO',True,FALSE) ;
                insert into era_contract_action_done(action_date,action_type,member_id,contract_id,action_status,active,change_houseid) values
                 (erental1,'OUT',memberid,conid,'NO',True,FALSE) ;
            elsif contype='2' then
               select count(*) into ncount from era_contract where id=conid and house_id != house_id1 ;
               if ncount > 0 then
                  changehid = TRUE ;
               else
                  changehid = FALSE ;
               end if ;
               update era_contract_action_done set active=False where member_id=memberid ; 
               insert into era_contract_action_done(action_date,action_type,member_id,contract_id,action_status,active,change_houseid) values
                 (srental,'IN',memberid,conid,'NO',True,changehid) ;
               insert into era_contract_action_done(action_date,action_type,member_id,contract_id,action_status,active,change_houseid) values
                 (erental1,'OUT',memberid,conid,'NO',True,changehid) ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chk_landlord(lpid varchar) cascade""")
        self._cr.execute("""create or replace function chk_landlord(lpid varchar) returns CHAR as $BODY$
          DECLARE
            myres char ;
            ncount int ;
          BEGIN
            select count(*) into ncount from era_landlord_contract where landlord_pid = lpid ;
            if ncount > 0 then
               myres = '2' ;
            else
               myres = '1' ;
            end if ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractlandlord(conid int) cascade""")
        self._cr.execute("""create or replace function gencontractlandlord(conid int) returns void as $BODY$
         DECLARE
           cl_cur refcursor ;
           cl_rec record ;
           pid varchar ;
           landlordid int ;
           deposit float ;
           startrental date ;
           endrental date ;
           nowdate date ;
         BEGIN
           select current_timestamp::DATE into nowdate ;
           select landlord_pid into pid from era_landlord_contract where id = conid ;
           select max(id) into landlordid from era_household_landlord where landlord_pid=pid;
           open cl_cur for select * from era_household_landlord where id = landlordid ;
           loop
              fetch cl_cur into cl_rec ;
              exit when not found ;
              if cl_rec.ap_system_sd is null then
                 startrental = nowdate ;
              else
                 startrental = cl_rec.ap_system_sd ;
              end if ;   
              select startrental + interval '1 year' - interval '1 day' into endrental ;
              update era_landlord_contract set landlord_email=cl_rec.landlord_email,landlord_address1=cl_rec.landlord_address1,landlord_address2=cl_rec.landlord_address2,
                landlord_phone1=cl_rec.landlord_phone1,landlord_phone2=cl_rec.landlord_phone2,income_date=nowdate,start_rental=startrental,end_rental=endrental,
                month_fee=cl_rec.month_fee,have_contract_data=cl_rec.have_contract_data,contract_data_fee=cl_rec.contract_data_fee,
                have_emeter=cl_rec.have_emeter,emeter_fee=cl_rec.emeter_fee,have_account_push=cl_rec.have_account_push,account_push_fee=cl_rec.account_push_fee,
                have_call_notice=cl_rec.have_call_notice,call_notice_fee=cl_rec.call_notice_fee,have_repair_message=cl_rec.have_repair_message,
                repair_message_fee=cl_rec.repair_message_fee where id = conid ;           
           end loop ;
           close cl_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genhouseholdemeter(houseid int) cascade""")
        self._cr.execute("""create or replace function genhouseholdemeter(houseid int) returns void as $BODY$
          DECLARE
            em_cur refcursor ;
            em_rec record ;
            memberid int ;
          BEGIN
            open em_cur for select * from era_household_electric_meter where emeter_id=houseid ;
            loop
               fetch em_cur into em_rec ;
               exit when not found ;
               select member_id into memberid from era_household_house_line where id = em_rec.emeter_id ;
               
            end loop ;
            close em_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_110v_cscale(memberid int) cascade""")
        self._cr.execute("""create or replace function get_110v_cscale(memberid int) returns float as $BODY$
          DECLARE
            myres float ;
            houseid int ;
          BEGIN
            select house_id into houseid from era_household_member where id = memberid ;
            select current_scale into myres from era_member_income_emeter where member_id=memberid and in_used=True and emeter_id=(select id from era_household_electric_meter where emeter_name like '%110V%' and emeter_id=houseid ) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_220v_cscale(memberid int) cascade""")
        self._cr.execute("""create or replace function get_220v_cscale(memberid int) returns float as $BODY$
          DECLARE
            myres float ;
            houseid int ;
          BEGIN
            select house_id into houseid from era_household_member where id = memberid ;
            select current_scale into myres from era_member_income_emeter where member_id=memberid and in_used=True and emeter_id=(select id from era_household_electric_meter where emeter_name like '%220V%' and emeter_id=houseid) ;
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_emeter_complete(contractid int) cascade""")
        self._cr.execute("""create or replace function get_emeter_complete(contractid int) returns float as $BODY$
          DECLARE
            myres float ;
            houseid int ;
            memberid int ;
          BEGIN
            select house_id into houseid from era_contract where id = contractid ;
            select id into memberid from era_household_member where house_id=houseid ;
            select sum(account_amount) into myres from era_member_emeter where account_id=memberid and member_payment_id in (select id from era_member_payment where house_id=houseid) ;
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get_member_deposit(contractid int) cascade""")
        self._cr.execute("""create or replace function get_member_deposit(contractid int) returns float as $BODY$
          DECLARE
            myres float ;
            houseid int ;
            memberid int ;
          BEGIN
            select house_id into houseid from era_contract where id = contractid ;
            select id into memberid from era_household_member where house_id = houseid ;
            /* deposit_status='1' 有效   deposit_status='2' 無效 */
            select sum(deposit_amount) into myres from era_member_deposit where account_id=memberid 
                and member_payment_id in (select id from era_member_payment where house_id=houseid) 
                and deposit_status='1' ;
            return myres ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get110vstart(conid int) cascade""")
        self._cr.execute("""create or replace function get110vstart(conid int) returns float as $BODY$
          DECLARE
            v110start float ;
            houseid int ;
            v110emeterid int ;
          BEGIN
            select house_id into houseid from era_contract where id = conid ;
            select id into v110emeterid from era_household_electric_meter where emeter_id=houseid and emeter_name like '%110V%' ;
            select start_scale into v110start from era_contract_emeter where contract_id=conid and emeter_id=v110emeterid ;
            return v110start ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists get220vstart(conid int) cascade""")
        self._cr.execute("""create or replace function get220vstart(conid int) returns float as $BODY$
          DECLARE
            v220start float ;
            houseid int ;
            v220emeterid int ;
          BEGIN
            select house_id into houseid from era_contract where id = conid ;
            select id into v220emeterid from era_household_electric_meter where emeter_id=houseid and emeter_name like '%220V%' ;
            select start_scale into v220start from era_contract_emeter where contract_id=conid and emeter_id=v220emeterid ;
            return v220start ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gencontractclose() cascade""")
        self._cr.execute("""create or replace function gencontractclose() returns void as $BODY$
          DECLARE
            con_cur refcursor ;
            con_rec record ;
            ncount int ;
          BEGIN
            open con_cur for select id from era_contract ;
            loop
              fetch con_cur into con_rec ;
              exit when not found ;
              select count(*) into ncount from era_contract_close where contract_id=con_rec.id ;
              if ncount = 0 then
                 insert into era_contract_close(contract_id,household_clean_fee) values
                   (con_rec.id,0) ;
              end if ;
            end loop ;
            close con_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getnonmanagementfee(conid int) cascade""")
        self._cr.execute("""create or replace function getnonmanagementfee(conid int) returns INTEGER  as $BODY$
          DECLARE
            sdate date ;
            edate date ;
            syear varchar ;
            smonth varchar ;
            sym varchar ;
            eym varchar ;
            eyear varchar ;
            emonth varchar ;
            manfee float ;
            manpay float ;
            houseid int ;
            memberid int ;
            myres int ;
          BEGIN
            select start_rental,end_rental,coalesce(house_id1,house_id) into sdate,edate,houseid from era_contract where id = conid ;
            select member_id into memberid from era_household_house_line where id = houseid ;
            select date_part('year',sdate)::TEXT into syear ;
            select lpad(date_part('month',sdate)::TEXT,2,'0') into smonth ;
            select date_part('year',edate)::TEXT into eyear ;
            select lpad(date_part('month',edate)::TEXT,2,'0') into emonth ;
            sym = concat(syear,'-',smonth) ;
            eym = concat(eyear,'-',emonth) ;
            select sum(coalesce(house_management_fee,0)+coalesce(parking_management,0)+coalesce(lo_parking_management,0)),
                   sum(coalesce(house_management_pay,0)+coalesce(parking_management_pay,0)+coalesce(lopark_management_pay,0)) 
                   into manfee,manpay from era_member_account where member_id=memberid and account_active=True 
                   and account_ym >= sym and account_ym <= eym ;
            myres = (manfee::numeric - manpay::numeric)::numeric::INTEGER ;
            return myres ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmembercontract() cascade""")
        self._cr.execute("""create or replace function genmembercontract() returns void as $BODY$
          DECLARE
            con_cur refcursor ;
            con_rec record ;
            houseid int ;
            memberid int ;
          BEGIN
            open con_cur for select * from era_contract where active=True ;
            loop
              fetch con_cur into con_rec ;
              exit when not found ;
              select coalesce(con_rec.house_id1,con_rec.house_id) into houseid ;
              select member_id into memberid from era_household_house_line where id = houseid ;
              update era_household_member set contract_id = con_rec.id where id = memberid ;
            end loop ;
            close con_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genmembernoncomplete(memberid int,paymentid int,emamount int,clfee int,imfee int) cascade""")
        self._cr.execute("""create or replace function genmembernoncomplete(memberid int,paymentid int,emamount int,clfee int,imfee int) returns void as $BODY$
          DECLARE
            /* memberid,paymentid,emeter_amount,clean_fee,impairment_fee */
            pay_cur refcursor ;
            pay_rec record ;
            accy varchar ;  /* 西元年 */
            accm varchar ;  /* 月份 */
            maxid int ;
            ncount int ;
            ncount1 int ;
            payap float ;
            paylineid int ;
            monthid int ;
           BEGIN
            accy=' ' ;
            accm=' ' ;
            open pay_cur for select * from era_member_account where member_id=memberid and account_active=True and 
             ((coalesce(house_rental_fee,0) - coalesce(house_rental_pay,0))>0 or (coalesce(house_management_fee,0) - coalesce(house_management_pay,0) > 0 ) or
               (coalesce(parking_management,0) - coalesce(parking_management_pay,0) > 0) or (coalesce(lo_parking_management,0) - coalesce(lopark_management_pay,0)) > 0  ) ;
            loop
              fetch pay_cur into pay_rec ;
              exit when not found ;

                 select substring(pay_rec.account_ym,1,4) into accy ;
                 select substring(pay_rec.account_ym,6,2) into accm ;
                 select id into monthid from era_payment_month where value=accm ;
                 /* 房屋租金扣押金自動生成 */
                 if (coalesce(pay_rec.house_rental_fee,0) - coalesce(pay_rec.house_rental_pay,0))>0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='01';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'房屋租金扣押金','01',accy,1,pay_rec.house_rental_fee) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='01';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ; 
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='01';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0)+pay_rec.house_rental_fee where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;   
                 /* 租屋管理費扣押金自動生成 */
                 if (coalesce(pay_rec.house_management_fee,0) - coalesce(pay_rec.house_management_pay,0))>0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='02';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'租房管理費扣押金','02',accy,1,pay_rec.house_management_fee) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='02';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='02';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0)+pay_rec.house_management_fee where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
                 /* 汽車位租金扣押金自動生成 */
                 if (coalesce(pay_rec.parking_space_rent,0) - coalesce(pay_rec.parking_space_pay,0))>0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='03';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'汽車位租金扣押金','03',accy,1,pay_rec.parking_space_rent) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='03';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='03';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0)+pay_rec.parking_space_rent where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
                 /* 機車位租金扣押金自動生成 */
                 if (coalesce(pay_rec.lo_parking_management,0) - coalesce(pay_rec.lopark_management_pay,0))>0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='04';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'機車位租金扣押金','04',accy,1,pay_rec.lo_parking_management) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='04';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='04';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0)+pay_rec.lo_parking_management where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
                 /* 電費扣押金自動生成 */
                 if emamount > 0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='05';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'電費扣押金','05',accy,1,emamount) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='05';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='05';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0) + emamount where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
                  /* 其他減損扣押金自動生成 */
                 if imfee > 0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='08';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'其他減損扣押金','11',accy,1,imfee) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='08';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='08';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0) + imfee where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
                 /* 房務清潔費扣押金自動生成 */
                 if clfee > 0 then
                    select count(*) into ncount from era_member_payment_line where payment_id=paymentid and pay_year=accy and paycode='11';
                    if ncount = 0 then
                       insert into era_member_payment_line(payment_id,pay_status,pay_active,pay_name,pay_code,pay_year,month_num,pay_ap) values
                         (paymentid,'2',True,'房務清潔費扣押金','11',accy,1,clfee) ;
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='11';
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ;  
                       end if ;   
                    else
                       select max(id) into paylineid from era_member_payment_line where payment_id=paymentid and pay_year=accy and pay_code='11';
                       update era_member_payment_line set month_num=coalesce(month_num,0)+1,pay_ap=coalesce(pay_ap,0) + clfee where id = paylineid ;
                       select count(*) into ncount1 from era_month_payline_rel where payment_id=paylineid and month_id=monthid ;
                       if ncount1 = 0 then
                          insert into era_month_payline_rel(payment_id,month_id) values (paylineid,monthid) ; 
                       end if ;
                    end if ;
                 end if ;
            end loop ;
            close pay_cur ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists activememberuser(conid int) cascade""")
        self._cr.execute("""create or replace function activememberuser(conid int) returns void as $BODY$
          DECLARE
            memberno varchar ;
            memberpid varchar ;
            memberid int ;
            membername varchar ;
            houseno varchar ;
            houseid int ;
            mylogin varchar ;
            mylogin1 varchar ;
            ncount int ;
            userid int ;
            srental date ;
            erental date ;
            mynow timestamp ;
            ncount1 int ;
          BEGIN
            select current_timestamp into mynow ;
            select member_no,member_pid,house_id,start_rental,end_rental,member_name into memberno,memberpid,houseid,srental,erental,membername from era_contract where id = conid ;
            select id into memberid from era_household_member where member_pid=memberpid and active=True ;
            select house_no into houseno from era_household_house_line where id=houseid ;
            mylogin = concat(houseno,'-',memberpid) ;
            mylogin1 = memberno ;
            select count(*) into ncount from res_users where login=mylogin and active=True ;
            if ncount = 0 then
               select count(*) into ncount from res_users where login=mylogin1 and active=True ;
               if ncount > 0 then
                  select id into userid from res_users where login=mylogin1 and active=True ;
               end if ;
            else
               select id into userid from res_users where login=mylogin and active=True ;
            end if ;
            update era_household_house_line set member_id=memberid,user_id=userid,in_used=True where id = houseid ;
            insert into era_member_contract(member_id,contract_id,start_rental,end_rental,create_date,contract_status) values
             (memberid,conid,srental,erental,mynow,'1') ;
             select count(*) into ncount1 from era_member_line_user where member_pid = memberpid and active=True ;
             if ncount1 > 0 then
                update era_member_line_user set active=False where member_pid = memberpid and active=True ;
             end if ;
             insert into era_member_line_user(member_id,member_pid,member_name,send_acc_bill,send_announcement,active) values 
                 (memberid,memberpid,membername,True,True,True) ;
          END;$BODY$
          LANGUAGE plpgsql;""")


