# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class erastoreproc(models.Model):
    _name = "era.storeproc"

    @api.model
    def init(self):
        self.env.cr.execute("""drop function if exists rundailyamount() cascade""")
        self.env.cr.execute("""create or replace function rundailyamount() returns void as $BODY$
          DECLARE
            house_cur refcursor ;
            house_rec record ;
            emeter_cur refcursor ;
            emeter_rec record ;
            myres float ;
            powerstore float ;
            minusedvalue float ;
            maxusedvalue float ;
            totamount float ;
            mymaxid int ;
            mymaxid1 int ;
            endvalue float ;
            currentvalue float ;
          BEGIN
            open house_cur for select * from era_household_house_line where in_used=True ;
            loop
               fetch house_cur into house_rec ;
               exit when not found ;
               select max(id) into mymaxid from era_household_prepaid_line where prepaid_id = house_rec.id ;
               select coalesce(end_value,0) into endvalue from era_household_prepaid_line where id = mymaxid ;
               if endvalue is null then
                  endvalue = 0 ;
               end if ;
               select max(id) into mymaxid1 from era_household_used_line where used_id = house_rec.id ;
               select coalesce(used_scale,0) into currentvalue from era_household_used_line where id = mymaxid1 ;  
               if currentvalue is null then
                  currentvalue = 0 ;
               end if ;    
               update era_household_house_line set store_amount = endvalue::numeric - currentalue::numeric
                  where id = house_rec.id ; 
            end loop ;
            close house_cur ;
          END;$BODY$
          LANGUAGE plpgsql;
          """)

        self._cr.execute("""drop function if exists gendevicevalue(machine varchar,did varchar,myvalue float) cascade""")
        self._cr.execute("""create or replace function gendevicevalue(machine varchar,did varchar,myvalue float) returns void as $BODY$
         DECLARE
          ncount int ;
          emeterid int ;
          lineid int ;
          mynowdatetime timestamp ;
          maxscaleid int ;
          maxusedscale float ;
         BEGIN
          select current_timestamp into mynowdatetime ;        
          select count(*) into ncount from era_household_electric_meter where ig8000_id=machine and modbus_id=did ;
         if ncount > 0 then 
             select id,emeter_id into emeterid,lineid from era_household_electric_meter where ig8000_id=machine and modbus_id=did ;
             select max(id) into maxscaleid from era_household_used_line where used_id=lineid and used_emeter_id=emeterid ;
             select used_scale into maxusedscale from era_household_used_line where id = maxscaleid ;
             /* if myvalue < (maxusedscale + 100) then */
             if myvalue < 10000 then
             /* select id into lineid from era_household_electric_meter where ig8000_id=machine and modbus_id=did ; */
                insert into era_household_used_line(used_id,used_emeter_id,used_datetime,used_scale) values (lineid,emeterid,mynowdatetime,myvalue) ;
             end if ;   
          end if ; 
         END;$BODY$
         LANGUAGE plpgsql;
         
         """)

        self._cr.execute("""drop function if exists run_modbus(machine varchar,did varchar,myvalue float) cascade""")
        self._cr.execute("""create or replace function run_modbus(machine varchar,did varchar,myvalue float) returns void as $BODY$
             DECLARE
              ncount int ;
              ncount1 int ;
              ncount2 int ;
              emeterid int ;
              lineid int ;
              mynowdatetime timestamp ;
              maxscaleid int ;
              maxusedscale float ;
              emeterstatus varchar ;
              ngcount int ;
              statusid int ;
             BEGIN
              select current_timestamp into mynowdatetime ;  
              select count(*) into ncount2 from era_emeterhub_status where pi_id=machine ;
              if ncount2 = 0 then
                 insert into era_emeterhub_status(pi_id,last_update) values (machine,mynowdatetime);
              else
                 update era_emeterhub_status set last_update=mynowdatetime where pi_id=machine ;
              end if ;      
              select count(*) into ncount from era_household_electric_meter where pi_id=machine and modbus10_id=did ;
              if ncount > 0 then 
                 select id,emeter_id into emeterid,lineid from era_household_electric_meter where pi_id=machine and modbus10_id=did ;
                 select max(id) into maxscaleid from era_household_used_line where used_id=lineid and used_emeter_id=emeterid ;
                 select used_scale into maxusedscale from era_household_used_line where id = maxscaleid ;
                 if myvalue::numeric = -1 then
                    myvalue = maxusedscale::numeric ;
                    insert into era_household_emeter_line(emeter_id,emeter_dt,emeter_status) values (emeterid,mynowdatetime,'NG') ;
                    select count(*) into ncount1 from era_emeter_status where emeter_id=emeterid ;
                    if ncount1=0 then
                       insert into era_emeter_status(emeter_id,last_update,ng_count,emeter_status) values (emeterid,mynowdatetime,1,'NG') ;
                    else
                       select id,ng_count,emeter_status into statusid,ngcount,emeterstatus from era_emeter_status
                         where emeter_id=emeterid ;
                       if emeterstatus='OK' then
                          update era_emeter_status set last_update=mynowdatetime,ng_count=1,emeter_status='NG' where id=emeterid ;
                       else
                          update era_emeter_status set last_update=mynowdatetime,ng_count=coalesce(ngcount,0)+1,emeter_status='NG' where id=emeterid ;
                       end if ;  
                    end if ;
                 else
                    insert into era_household_emeter_line(emeter_id,emeter_dt,emeter_status) values (emeterid,mynowdatetime,'OK') ;
                    select count(*) into ncount1 from era_emeter_status where emeter_id=emeterid ;
                    if ncount1 = 0 then
                       insert into era_emeter_status(emeter_id,last_update,ng_count,emeter_status) values (emeterid,mynowdatetime,0,'OK') ;
                    else
                       update era_emeter_status set last_update=mynowdatetime,ng_count=0,emeter_status='OK' where emeter_id=emeterid ;
                    end if ;
                 end if ;
                 insert into era_household_used_line(used_id,used_emeter_id,used_datetime,used_scale) values (lineid,emeterid,mynowdatetime,myvalue::numeric) ;  
              end if ; 
             END;$BODY$
             LANGUAGE plpgsql;
             """)

        self._cr.execute("""drop function if exists checkconfig() cascade""")
        self._cr.execute("""create or replace function checkconfig() returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           mynowdate date ;
           myyear varchar ;
           mymonth varchar ;
           myym varchar ;
         BEGIN
           select date_part('year',now())::TEXT into myyear ;
           select lpad(date_part('month',now())::TEXT,2,'0') into mymonth ;
           myym = concat(myyear,'-',mymonth) ;
           select count(*) into ncount from era_household_config ;
           if ncount = 0 then
              insert into era_household_config(bill_ym,price_unit) values (myym,5.0) ;
           else
              select count(*) into ncount1 from era_household_config where bill_ym != myym ;
              if ncount1 > 0 then
                 update era_household_config set bill_ym=myym ;
              end if ;   
           end if ;
           update era_member_account set account_active=True where account_active=False and account_ym <= myym ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists runemeterscale() cascade""")
        self._cr.execute("""create or replace function runemeterscale() returns void as $BODY$
         DECLARE
           ncount int ;
           ncount1 int ;
           ncount2 int ;
           ncount3 int ;
           myym varchar ;
           house_cur refcursor ;
           house_rec record ;
           startdate date ;
           enddate date ;
           myyear varchar ;
           mymonth varchar ;
           mynewdate date ;
           meter_cur refcursor ;
           meter_rec record ;
           startscale float ;
           endscale float ;
           houseno varchar ;
           priceunit float ;
           priceunit1 float ;
           startid int ;
           startid_scale float ;
           start1id int ;
           start1id_scale float ;
           endid int ;
           endid_scale float ;
           end1id int ;
           end1id_scale float ;
           maxcurrentscale float ;
           maxid int ;
           maxcurrentscale1 float ;
           maxid1 int ;
           is220v boolean ;
           myemeterid int ;
           mymemberid int ;
           h_startdate date ;
           h_day varchar ;
           h_day1 varchar ;
           h_cstartdate varchar ;
           h_cstartdate1 varchar ;
           incomedate date ;
           incomedate1 date ;
           h_incomey varchar ;
           h_incomem varchar ;
           h_incomeym varchar ;
           myy varchar ;
           mym varchar ;
           waterfee float ;        
           ncount4 int ; 
           inused boolean ;
           mynowdate date ;
         BEGIN
           select (current_timestamp + interval '8 hour')::DATE into mynowdate ; 
           select count(*) into ncount from era_household_config ;
           if ncount = 0 then
              execute checkconfig() ;
           end if ;
           select max(bill_ym),max(price_unit) into myym,priceunit from era_household_config ;
           select substring(myym,1,4) into myy ;
           select substring(myym,6,2) into mym ;
           select substring(myym,1,4) into myyear ;
           select substring(myym,6,2) into mymonth ;
           if mym = '01' then
              myym = concat((myy::INT - 1)::TEXT,'-12') ;
           else
              myym = concat(myy,'-',lpad((mym::INT - 1)::TEXT,2,'0')) ;
           end if ;
           select concat(myym,'-01')::DATE into startdate ;
           select startdate + interval '1 month' - interval '1 days' into enddate ;
          
           select count(*) into ncount2 from era_household_bill_line ;
           select count(*) into ncount1 from era_household_bill_line where bill_ym=myym ;
           select count(*) into ncount3 from era_household_bill_line_his where bill_ym=myym ;
          /* if ncount1 = 0 and ncount2 > 0  then  /* 有記錄但非當期 */
              if ncount3 = 0 then
                  insert into era_household_bill_line_his(bill_id,house_no,emeter_id,bill_ym,bill_start_date,bill_end_date,emeter_start_scale,emeter_end_scale,emeter_used_scale,emeter_current_scale,emeter_price_unit,emeter_amount,create_uid,create_date,write_uid,write_date)
                   select bill_id,house_no,emeter_id,bill_ym,bill_start_date,bill_end_date,emeter_start_scale,emeter_end_scale,emeter_used_scale,emeter_current_scale,emeter_price_unit,emeter_amount,create_uid,create_date,write_uid,write_date from 
                    era_household_bill_line ;
              end if ;      
              delete from era_household_bill_line ;  
           elsif ncount1 > 0 then      
               update era_household_bill_line set emeter_start_scale=0,emeter_end_scale=0,emeter_used_scale=0,emeter_current_scale=0,emeter_price_unit=0,emeter_amount=0 ;
           end if ; */
           open meter_cur for select id,emeter_id,emeter_name from era_household_electric_meter order by emeter_id ;
           loop
             fetch meter_cur into meter_rec ;
             exit when not found ;
             select coalesce(price_unit,0) into priceunit1 from era_household_house_line where id = meter_rec.emeter_id ;
             if priceunit1 > 0 then
                priceunit = priceunit1 ;   /*  用個別房間之電費單價 */
             end if ;
             select coalesce(member_id,0) into mymemberid from era_household_house_line where id = meter_rec.emeter_id ;
             if mymemberid > 0 then
                waterfee=0 ;
                select coalesce(start_rental,startdate),coalesce(income_date,startdate),coalesce(water_fee,0) into h_startdate,incomedate,waterfee from era_household_member where id = mymemberid ;
                incomedate1 = incomedate ;
                select date_part('year',incomedate)::TEXT into h_incomey ;
                select lpad(date_part('month',incomedate)::TEXT,2,'0') into h_incomem ;
                h_incomeym = concat(h_incomey,'-',h_incomem) ;
                select lpad(date_part('day',h_startdate)::TEXT,2,'0') into h_day ;
                select lpad(date_part('day',incomedate)::TEXT,2,'0') into h_day1 ;
                if (substring(myym,6,2)='04' or substring(myym,6,2)='06' or substring(myym,6,2)='09' or substring(myym,6,2)='11') and h_day='31' then
                   h_cstartdate = concat(myym,'-30') ;
                elsif substring(myym,6,2)='02' then
                   h_cstartdate = concat(myym,'-28') ;
                else   
                   h_cstartdate = concat(myym,'-',h_day) ;
                end if ;
                if (substring(myym,6,2)='04' or substring(myym,6,2)='06' or substring(myym,6,2)='09' or substring(myym,6,2)='11') and h_day1='31' then
                   h_cstartdate1 = concat(myym,'-30') ;
                elsif substring(myym,6,2)='02' then
                   h_cstartdate1 = concat(myym,'-28') ;
                else
                   h_cstartdate1 = concat(myym,'-',h_day1) ;
                end if ;
                
                incomedate = h_cstartdate1::DATE ;
                startdate = h_cstartdate::DATE ;
                select startdate + interval '1 month' - interval '1 days' into enddate ;
                if trim(h_incomeym) = trim(myym) then
                   startdate = incomedate ;                  
                end if ;
             end if ;
             select meter_rec.emeter_name ilike '%220V' into is220V ;
             select count(*) into ncount4 from era_household_used_line where (used_datetime + interval '8 hours')::DATE >=startdate and (used_datetime + interval '8 hours')::DATE <= enddate and used_emeter_id=meter_rec.id ;
             select min(id) into startid from era_household_used_line where (used_datetime + interval '8 hours')::DATE >=startdate and used_emeter_id=meter_rec.id ;
             select min(id) into start1id from era_household_used_line where (used_datetime + interval '8 hours')::DATE>=startdate and used_emeter_id=meter_rec.id and id > startid ;
             select max(id) into maxid from era_household_used_line where used_emeter_id=meter_rec.id ;
             select used_scale into maxcurrentscale from era_household_used_line where id = maxid ;
             select max(id) into maxid1 from era_household_used_line where used_emeter_id=meter_rec.id and id < maxid ;
             select used_scale into maxcurrentscale1 from era_household_used_line where id = maxid1 ;
             if maxcurrentscale > (maxcurrentscale1 + 100) then
                maxcurrentscale = maxcurrentscale1 ;
             end if ;
             select used_scale into startid_scale from era_household_used_line where id = startid ;
             select used_scale into start1id_scale from era_household_used_line where id = start1id ;
             if start1id_scale >= startid_scale then
                startscale = startid_scale ;
             else
                startscale = start1id_scale ;
             end if ;
             if coalesce(startscale,0) = 0 then
                select max(emeter_end_scale) into startscale from era_household_bill_line_his where emeter_id=meter_rec.id ;
             end if ;
             select max(id) into endid from era_household_used_line where (used_datetime + interval '8 hours')::DATE<=enddate and used_emeter_id=meter_rec.id ;
             select max(id) into end1id from era_household_used_line where (used_datetime + interval '8 hours')::DATE<=enddate and used_emeter_id=meter_rec.id and id < endid ;
             select used_scale into endid_scale from era_household_used_line where id = endid ;
             select used_scale into end1id_scale from era_household_used_line where id = end1id ;
             if end1id_scale >= endid_scale then
                endscale = endid_scale ;
             else
                endscale = end1id_scale ;
             end if ;
             select count(*) into ncount3 from era_household_bill_line where bill_ym=myym and bill_id=meter_rec.emeter_id and emeter_id=meter_rec.id ;
              if ncount3 = 0 then
                 select house_no into houseno from era_household_house_line where id = meter_rec.emeter_id ;
                 insert into era_household_bill_line(bill_id,house_no,emeter_id,bill_ym,bill_start_date,bill_end_date,emeter_price_unit,emeter_start_scale,emeter_end_scale,is_payment) 
                   values (meter_rec.emeter_id,houseno,meter_rec.id,myym,startdate,enddate,priceunit,startscale,endscale,False) ; 
              end if ; 
             select coalesce(start_scale,0) into startscale from era_member_income_emeter where emeter_id=meter_rec.id ; 
             if is220v=True then
                update era_household_house_line set start_date=incomedate1,start220_scale=startscale,current220_scale=maxcurrentscale where id = meter_rec.emeter_id ;
              else
                 update era_household_house_line set start_date=incomedate1,start110_scale=startscale,current110_scale=maxcurrentscale where id = meter_rec.emeter_id ;
              end if ;   
              
              select in_used into inused from era_household_house_line where id=meter_rec.emeter_id ;
              if mymemberid > 0 and inused=True then
                 update era_member_income_emeter set current_scale=maxcurrentscale,start_date=incomedate1 where emeter_id=meter_rec.id  and member_id=mymemberid and in_used=True ;  
              end if ;      
           end loop ;
           close meter_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        # self._cr.execute("""drop function if exists genusermember(userid int) cascade""")
        # self._cr.execute("""create or replace function genusermember(userid int) returns void as $BODY$
        #  DECLARE
        #    hid int ;
        #    mid int ;
        #  BEGIN
        #    select coalesce(house_id,0),coalesce(member_id,0) into hid,mid from res_users where id = userid ;
        #    if hid > 0 then
        #       update era_household_house set user_id=userid where id = hid ;
        #    end if ;
        #    if mid > 0 then
        #       update era_household_member set user_id=userid where id = mid ;
        #    end if ;
        #  END;$BODY$
        #  LANGUAGE plpgsql;""")

        self._cr.execute("""create or replace function changememberpasswd() returns trigger as $BODY$
          BEGIN
            if OLD.member_pid is not null and OLD.user_id is not null then
               update res_users set password=OLD.member_pid where id=OLD.user_id ;
            end if ;
            if NEW.member_pid <> OLD.member_pid and NEW.user_id is not null then
               update res_users set password=NEW.member_pid where id=NEW.user_id ;
            end if ;
            if NEW.member_pid <> OLD.member_pid and OLD.user_id is not null then
               update res_users set password=NEW.member_pid where id=OLD.user_id ;
            end if ;
            if OLD.member_pid is not null and NEW.user_id <> OLD.user_id then
               update res_users set password=OLD.member_pid where id=NEW.user_id ;
            end if ;
            
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop trigger if exists change_member_password on era_household_member ;""")
        self._cr.execute("""create Trigger change_member_password 
        after update of member_pid on era_household_member 
        for each row 
        execute procedure changememberpasswd()""")

        self._cr.execute("""drop function if exists checkpayment(hl_id int,p_ym varchar) cascade""")
        self._cr.execute("""create or replace function checkpayment(hl_id int,p_ym varchar) returns Boolean as $BODY$
         DECLARE
           myres Boolean ;
           ncount int ;
         BEGIN
           select count(*) into ncount from era_household_payment_line where payment_id=hl_id and payment_ym=p_ym ;
           if ncount > 0 then
              myres = True ;
           else
              myres = False ;   
           end if ; 
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists generapayment(wizid int) cascade""")
        self._cr.execute("""create or replace function generapayment(wizid int) returns void as $BODY$
         DECLARE
           payacc int ;
           payym varchar ;
           payym1 varchar ;
           payamount float ;
           uncompletefee float ;
           paydesc varchar ;
           paydate date ;
           b1 boolean ;
           b2 boolean ;
           b3 boolean ;
           b4 boolean ;
           b5 boolean ;
           b6 boolean ; 
           ncount int ;
           startdate date ;
           enddate date ;
           houseno varchar ;
           currenttotalfee float ;
           currentuncomplete float ;
           payy varchar ;
           paym varchar ;
           ncount1 int ;
         BEGIN
           select coalesce(payment_account,0),coalesce(payment_ym,' '),coalesce(payment_amount,0),coalesce(payment_desc,' '),payment_date,
             emeter_scale,house_rental,house_management,parking_space_rent,parking_management,lo_parking_management,coalesce(uncomplete_fee,0),coalesce(current_total_fee,0) into
              payacc,payym,payamount,paydesc,paydate,b1,b2,b3,b4,b5,b6,uncompletefee,currenttotalfee from era_era_payment_wizard where id = wizid ;
           currentuncomplete = currenttotalfee - payamount ;
           if currentuncomplete < 0 then
              currentuncomplete = 0 ;
           end if ;
           payy = substring(payym,1,4) ;
           paym = substring(payym,6,2) ;
           if paym='01' then
              payy = (payy::INT - 1)::TEXT ;
              payym1 = concat(payy,'-12') ;
           else
              payym1 = concat(payy,'-',lpad((paym::INT - 1)::TEXT,2,'0')) ;
           end if ;
           select count(*) into ncount from  era_household_payment_line where payment_id=payacc and payment_ym=payym ;
           select count(*) into ncount1 from era_household_bill_line where bill_id=payacc and bill_ym=payym1 ;
           if ncount1 > 0 then
                select bill_start_date,bill_end_date,house_no into startdate,enddate,houseno from era_household_bill_line where bill_id=payacc and
                    bill_ym=payym1 ;
           else
                select bill_start_date,bill_end_date,house_no into startdate,enddate,houseno from era_household_bill_line_his where bill_id=payacc and
                    bill_ym=payym1 ;
           end if ;         
           /*if ncount > 0 then  
              update era_household_payment_line set payment_start_date=startdate,payment_end_date=enddate,payment_amount=payamount,payment_desc=paydesc,
                 emeter_scale=b1,house_rental=b2,house_management=b3,parking_space_rent=b4,parking_management=b5,
                 lo_parking_management=b6,uncomplete_fee=currentuncomplete where payment_id=payacc and payment_ym=payym ;    
           else */
              insert into era_household_payment_line(payment_id,house_no,payment_ym,payment_start_date,payment_end_date,payment_amount,emeter_scale,
               house_rental,house_management,parking_space_rent,parking_management,lo_parking_management,payment_date,payment_desc,uncomplete_fee) values
               (payacc,houseno,payym,startdate,enddate,payamount,b1,b2,b3,b4,b5,b6,paydate,paydesc,currentuncomplete) ;
          /* end if ; */
           update era_household_bill_line set is_payment=True where bill_id=payacc and bill_ym=payym1 ;       
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists ckcurym(ym varchar) cascade""")
        self._cr.execute("""create or replace function ckcurym(ym varchar) returns Boolean as $BODY$
         DECLARE
           ncount int ;
           myres Boolean ;
           maxid int ;
           cym varchar ;
         BEGIN
           select max(id) into maxid from era_household_bill_line ;
           select bill_ym into cym from era_household_bill_line where id = maxid ;
           if ym=cym then
              myres = True ;
           else
              myres = False ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genemeterchange(wizid int) cascade""")
        self._cr.execute("""create or replace function genemeterchange(wizid int) returns void as $BODY$
          DECLARE
            projectno int ;
            houseno int ;
            emeterid int ;
            billym varchar ;
            changescale float ;
            memberid int ;
            incomedate date ;
            startrental date ;
            cyy1 varchar ;
            cmm1 varchar ;
            cym1 varchar ;
            cyy2 varchar ;
            cmm2 varchar ;
            cym2 varchar ;
            cym3 varchar ;
            cdd varchar ;
            startdate date ;
            enddate date ;
            sdate timestamp ;
            edate timestamp ;
            usedscale float ;
            maxid int ;
            ncount int ;
            chouseno varchar ;
            priceunit float ;
          BEGIN
            select project_no,house_no,emeter_id,bill_ym,coalesce(change_scale,0) into projectno,houseno,emeterid,billym,changescale from
              era_household_start_scale_wizard where id = wizid ;
            select member_id,house_no,price_unit into  memberid,chouseno,priceunit from era_household_house_line where id = houseno ;
            select income_date,start_rental into incomedate,startrental from era_household_member where id = memberid ;
            if incomedate is not null then
               select date_part('year',incomedate)::TEXT into cyy1 ;
               select lpad(date_part('month',incomedate)::TEXT,2,'0') into cmm1 ;
               cym1 = concat(cyy1,'-',cmm1) ;
            end if ;
            if startrental is not null then
                select date_part('year',startrental)::TEXT into cyy2 ;
               select lpad(date_part('month',startrental)::TEXT,2,'0') into cmm2 ;
               cym2 = concat(cyy2,'-',cmm2) ;
            end if ;
            select max(id) into maxid from era_household_bill_line where bill_id = houseno ;
            select bill_ym into cym3 from era_household_bill_line where id = maxid ;
            if cym3 = cym2 then  /* 要從 income_date 開始 */
               select lpad(date_part('day',incomedate)::TEXT,2,'0') into cdd ; 
            else                 /* 從 start_rental 開始 */
               select lpad(date_part('day',startrental)::TEXT,2,'0') into cdd ;
            end if ; 
            if cdd is null then
               cdd = '01' ;
            end if ;
            select concat(billym,'-',cdd)::timestamp into sdate ;
            select sdate + interval '1 month' - interval '1 days' into edate ;
            insert into era_household_used_line(used_id,used_emeter_id,used_datetime,used_scale) values
             (houseno,emeterid,sdate,changescale) ;
            if cym3 > billym then  /* in history */ 
               select count(*) into ncount from era_household_bill_line_his where bill_id=houseno and  emeter_id=emeterid and bill_ym=billym ;
               if ncount > 0 then
                  update era_household_bill_line_his set emeter_start_scale=changescale,emeter_used_scale=(coalesce(emeter_end_scale,changescale) - changescale),
                    emeter_amount=(coalesce(emeter_end_scale,changescale) - changescale)*emeter_price_unit where bill_id=houseno and 
                     emeter_id=emeterid and bill_ym=billym ;
               else
                  select max(used_scale) into usedscale from era_household_used_line where used_id=houseno and used_emeter_id=emeterid and used_datetime::DATE <= edate ;
                  insert into era_household_bill_line_his(bill_id,house_no,bill_ym,bill_start_date,bill_end_date,emeter_id,emeter_start_scale,emeter_end_scale,emeter_used_scale,emeter_current_scale,emeter_price_unit,emeter_amount) values
                   (houseno,chouseno,billym,sdate,edate,emeterid,changescale,usedscale,(usedscale - changescale),usedscale,priceunit,(usedscale - changescale)* priceunit) ;
               end if ;      
            else
               select count(*) into ncount from era_household_bill_line where bill_id=houseno and  emeter_id=emeterid and bill_ym=billym ;
               if ncount > 0 then
                  update era_household_bill_line set emeter_start_scale=changescale,emeter_used_scale=(coalesce(emeter_end_scale,changescale) - changescale),
                    emeter_amount=(coalesce(emeter_end_scale,changescale) - changescale)*emeter_price_unit where bill_id=houseno and 
                     emeter_id=emeterid and bill_ym=billym ;
               else
                  select max(used_scale) into usedscale from era_household_used_line where used_id=houseno and used_emeter_id=emeterid and used_datetime::DATE <= edate ;
                  insert into era_household_bill_line(bill_id,house_no,bill_ym,bill_start_date,bill_end_date,emeter_id,emeter_start_scale,emeter_end_scale,emeter_used_scale,emeter_current_scale,emeter_price_unit,emeter_amount) values
                   (houseno,chouseno,billym,sdate,edate,emeterid,changescale,usedscale,(usedscale - changescale),usedscale,priceunit,(usedscale - changescale)* priceunit) ; 
               end if ;      
            end if ; 
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmemberline(projid int,billym varchar) cascade""")
        self._cr.execute("""create or replace function genmemberline(projid int,billym varchar) returns void as $BODY$
          DECLARE
            h_cur refcursor ;
            h_rec record ; 
            ncount int ;
            pre_arrears int ;
            per_addition int ;
            per_electric int ;
            per_house_rent int ;
            per_house_man int ;
            per_park_rent int ;
            per_park_man int ;
            per_moto_park_man int ;
            per_water_fee int ;
            per_total int ;
            cy varchar ;
            cm varchar ;
            cym varchar ;
            myid int ;
          BEGIN
            select substring(billym,1,4) into cy ;
            select substring(billym,6,2) into cm ;
            if cm = '01' then
               cym = concat((cy::INT - 1)::TEXT,'-12') ;
            else
               cym = concat(cy,'-',lpad((cm::INT - 1)::TEXT,2,'0')) ;
            end if ;
             
            select count(*) into ncount from era_household_bill_line where bill_ym=cym ;
            open h_cur for select * from era_household_house_line where house_id=projid ;
            loop
              fetch h_cur into h_rec ;
              exit when not found ;
              select max(id) into myid from era_household_payment_line where payment_id=h_rec.id and payment_ym<=cym ;
              /* select coalesce(uncomplete_fee,0)::INT into pre_arrears from era_household_payment_line where payment_id=h_rec.id and payment_ym=cym ; */
              select coalesce(uncomplete_fee,0)::INT into pre_arrears from era_household_payment_line where id = myid ;
              if pre_arrears is null then
                 pre_arrears = 0 ;
              end if ;
              if ncount > 0 then
                 select sum(round(coalesce(emeter_amount,0),0))::INTEGER into per_electric from era_household_bill_line where
                    bill_id=h_rec.id and bill_ym=cym ;
                 select coalesce(house_rental_fee,0)::INT,coalesce(house_management_fee,0)::INT,coalesce(parking_space_rent,0)::INT,coalesce(parking_management,0)::INT,coalesce(lo_parking_management,0)::INT,coalesce(water_fee,0)::INT into
                  per_house_rent,per_house_man,per_park_rent,per_park_man,per_moto_park_man,per_water_fee from era_household_member where id = h_rec.member_id ;
                 per_addition = (per_electric + per_house_rent + per_house_man + per_park_rent + per_park_man + per_moto_park_man + per_water_fee) ; 
                 per_total = (pre_arrears + per_addition) ;
              else
                 select sum(round(coalesce(emeter_amount,0),0))::INTEGER into per_electric from era_household_bill_line_his where
                    bill_id=h_rec.id and bill_ym=cym ;
                 select coalesce(house_rental_fee,0)::INT,coalesce(house_management_fee,0)::INT,coalesce(parking_space_rent,0)::INT,coalesce(parking_management,0)::INT,coalesce(lo_parking_management,0)::INT,coalesce(water_fee,0)::INT into
                  per_house_rent,per_house_man,per_park_rent,per_park_man,per_moto_park_man,per_water_fee from era_household_member where id = h_rec.member_id ;
                 per_addition = (per_electric + per_house_rent + per_house_man + per_park_rent + per_park_man + per_moto_park_man + per_water_fee) ; 
                 per_total = (pre_arrears + per_addition) ;
              end if ;
              update era_household_member set previous_arrears=pre_arrears,period_addition=per_addition,period_electric=per_electric,period_house_rent=per_house_rent,
                 period_house_manage=per_house_man,period_park_rent=per_park_rent,period_park_manage=per_park_man,period_moto_park_manage=per_moto_park_man,
                 period_total=per_total,period_water_fee=per_water_fee where id = h_rec.member_id ;
            end loop ;
            close h_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpreviousbalance(houseid int,myym varchar,uncompletefee float) cascade""")
        self._cr.execute("""create or replace function genpreviousbalance(houseid int,myym varchar,uncompletefee float) returns void as $BODY$
          DECLARE
            ncount int ;
            houseno varchar ;
            memberid int ;
            maxid int ;
          BEGIN
            select count(*) into ncount from era_household_payment_line where payment_id=houseid and payment_ym=myym ;
            if ncount = 0 then
               select house_no into houseno from era_household_house_line where id = houseid ;
               insert into era_household_payment_line(payment_id,house_no,payment_ym,uncomplete_fee) values (houseid,houseno,myym,uncompletefee) ;
            else
               select max(id) into maxid from era_household_payment_line where payment_id=houseid and payment_ym<=myym ;
               update era_household_payment_line set uncomplete_fee=uncompletefee where id = maxid ;
            end if ;
            select member_id into memberid from era_household_house_line where id = houseid ;
            if memberid is not null and uncompletefee > 0 then
               update era_household_member set previous_arrears=uncompletefee where id = memberid ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmemberlineinfo() cascade""")
        self._cr.execute("""create or replace function genmemberlineinfo() returns void as $BODY$
          DECLARE
            myym varchar ;
            myym1 varchar ;
            myy varchar ;
            myy1 varchar ;
            mym1 varchar ;
            mym varchar ;
            myym2 varchar ;
            myny int ;
            mynm int ;
            ncount int ;
            ncount1 int ;
            payamount float ;
            h_cur refcursor ;
            h_rec record ;
            maxid int ;
            uncompletefee float ;
            periodtot int ;
            periodsubtot int ;
            periodstart varchar ;
            periodend varchar ;
            periodtotrent int ;
            periodtotrentpay int ;
            nowtotrentbalance int ;
            priceunit float ;
            nowtotscale float ;
            nowtotscalepay float ;
            totscalebalance int ;
          BEGIN
            select max(bill_ym) into myym from era_household_config ;
            myy1 = substring(myym,1,4) ;
            mym1 = substring(myym,6,2) ;
            if mym1='01' then
               myy1 = (myy1::INT - 1)::TEXT ;
               myym1 = concat(myy1,'-12') ;
            else
               mym1 = LPAD((mym1::INT - 1)::TEXT,2,'0') ;
               myym1 = concat(myy1,'-',mym1) ;
            end if ;
            select date_part('year',now())::TEXT into myy ;
            select LPAD(date_part('month',now())::TEXT,2,'0') into mym ;
            myym2 = concat(myy,'-',mym) ;
            execute checkconfig();
            open h_cur for select id,member_id from era_household_house_line ;
            loop
              fetch h_cur into h_rec ;
              exit when not found ;
              select start_rental::TEXT,end_rental::TEXT,(coalesce(house_rental_fee,0)+coalesce(house_management_fee,0)+coalesce(parking_space_rent,0)+coalesce(parking_management,0)+coalesce(lo_parking_management,0)+coalesce(water_fee,0))::INT 
                into periodstart,periodend,periodsubtot from era_household_member where id=h_rec.member_id ;
              select sum(coalesce(house_rental_fee,0)+coalesce(house_management_fee,0)+coalesce(parking_space_rent,0)+coalesce(parking_management,0)+coalesce(lo_parking_management,0)+coalesce(water_fee,0))::INT into
                     periodtotrent from era_member_account where member_id=h_rec.member_id and account_active=True ;
              select sum(coalesce(house_rental_pay,0)+coalesce(house_management_pay,0)+coalesce(parking_space_pay,0)+coalesce(parking_management_pay,0)+coalesce(lopark_management_pay,0)+coalesce(water_pay,0))::INT into
                     periodtotrentpay from era_member_account where member_id=h_rec.member_id ;
              select price_unit into priceunit from era_household_house_line where member_id=h_rec.member_id ;              
              nowtotrentbalance = coalesce(periodtotrent,0) - coalesce(periodtotrentpay,0) ;  
              select sum((coalesce(current_scale,0)-coalesce(start_scale,0)) * priceunit) into nowtotscale from era_member_income_emeter where member_id=h_rec.member_id ;
              select sum(coalesce(account_amount,0)) into nowtotscalepay from era_member_emeter where account_id=h_rec.member_id ;      
              totscalebalance = (nowtotscale - nowtotscalepay)::INT ;  
              select count(*) into ncount from era_household_bill_line where bill_id=h_rec.id and bill_ym=myym1 ;
              select count(*) into ncount1 from era_household_payment_line where payment_id=h_rec.id and payment_ym=myym ;
              if ncount > 0 and ncount1 > 0 then
                 select getlastuncompletefee(h_rec.id,myym) into uncompletefee ;
                 select sum(coalesce(payment_amount,0)) into payamount from era_household_payment_line where payment_id=h_rec.id and payment_ym=myym ;
                 if payamount is not null then
                    update era_household_member set period_complete_total=payamount,period_water_fee=coalesce(water_fee,0),previous_arrears=uncompletefee
                       where id = h_rec.member_id ;
                 else
                    update era_household_member set period_complete_total=0,period_water_fee=coalesce(water_fee,0),previous_arrears=uncompletefee
                       where id = h_rec.member_id ;  
                 end if ;
              else
                 update era_household_member set period_complete_total=0,period_water_fee=coalesce(water_fee,0),previous_arrears=uncompletefee
                       where id = h_rec.member_id ;  
              end if ;
              update era_household_member set period_start=periodstart,period_end=periodend,now_ym=myym2,period_subtot=periodsubtot,period_totrent=periodtotrent,
                     period_totrentpay=periodtotrentpay,now_totrent_balance=nowtotrentbalance,period_totscale=nowtotscale,period_totscalepay=nowtotscalepay,
                     now_totscalebalance=(coalesce(nowtotscale,0)-coalesce(nowtotscalepay,0))::INT,now_totbalance=(nowtotrentbalance + (coalesce(nowtotscale,0)-coalesce(nowtotscalepay,0)))::INT where id = h_rec.member_id ;
            end loop ;
            close h_cur ;
            update era_household_member set period_total=period_addition + previous_arrears ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genemetermixsearch(h_id int,s_date date,e_date date) cascade""")
        self._cr.execute("""create or replace function genemetermixsearch(h_id int,s_date date,e_date date) returns void as $BODY$
          DECLARE
            minid int ;
            minid1 int ;
            maxid int;
            maxid1 int ;
            start_scale float ;
            start_scale1 float ;
            end_scale float ;
            end_scale1 float ;
            s_scale float ;
            e_scale float ;
            e_used float ;
            e_used_amount float ;
            scale_price float ;
            emeter_cur refcursor ;
            emeter_rec record ;
            cstartdate varchar ;
            cenddate varchar ;
            s_dt timestamp ;
            e_dt timestamp ;
            priceunit float ;
            houseno varchar ;
          BEGIN
            delete from era_household_emeter_mixsearch_line ;
            select s_date::TEXT into cstartdate ;
            select e_date::TEXT into cenddate ;
            s_dt = concat(cstartdate,' 00:00:00')::timestamp ;
            e_dt = concat(cenddate,' 23:59:59')::timestamp ;
            select coalesce(price_unit,0),house_no into priceunit,houseno from era_household_house_line where id = h_id ;
            open emeter_cur for select id from era_household_electric_meter where emeter_id = h_id ;
            loop
              fetch emeter_cur into emeter_rec ;
              exit when not found ;
              start_scale = 0 ;
              start_scale1 = 0 ;
              end_scale = 0 ;
              end_scale1 = 0 ;
             /* select min(id) into minid from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime >= s_dt ;
              select min(id) into minid1 from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime >= s_dt and id > minid ; */
              select min(id) into minid from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime::DATE = s_date::DATE ;
              select min(id) into minid1 from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime::DATE = s_date::DATE and id > minid ;
              
              select coalesce(used_scale,0) into start_scale from era_household_used_line where id = minid ;
              select coalesce(used_scale,0) into start_scale1 from era_household_used_line where id = minid1 ;
              /*select max(id) into maxid from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime <= e_dt ;
              select max(id) into maxid1 from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime <= e_dt and id < maxid ;*/
              
              select min(id) into maxid from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime::DATE = e_date::DATE ;
              select min(id) into maxid1 from era_household_used_line where used_emeter_id = emeter_rec.id and used_datetime::DATE = e_date::DATE and id > maxid ;
              
              select coalesce(used_scale,0) into end_scale from era_household_used_line where id = maxid ;
              select coalesce(used_scale,0) into end_scale1 from era_household_used_line where id = maxid1 ;
            
              if abs(start_scale - start_scale1) > 100 and start_scale > start_scale1 then
                 s_scale = start_scale1 ;
              else
                 s_scale = start_scale ;
              end if ; 
              if abs(end_scale - end_scale1) > 100 and end_scale > end_scale1 then
                 e_scale = end_scale1 ;
              else
                 e_scale = end_scale ;
              end if ;
              e_used = e_scale - s_scale ;
              e_used_amount = e_used * priceunit ;
              insert into era_household_emeter_mixsearch_line(house_no,start_date,end_date,emeter_id,emeter_start_scale,emeter_end_scale,emeter_used_scale,emeter_price_unit,emeter_amount) values
               (houseno,s_date,e_date,emeter_rec.id,s_scale,e_scale,e_used,priceunit,e_used_amount) ;
            end loop ;
            close emeter_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpaymentamount(myym varchar,h_id int) cascade""")
        self._cr.execute("""create or replace function getpaymentamount(myym varchar,h_id int) returns float as $BODY$
         DECLARE
           myres float ;
         BEGIN
           select sum(coalesce(payment_amount,0)) into myres from era_household_payment_line where payment_ym=myym and payment_id=h_id ;
           if myres is null then
              myres = 0 ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpaymentdate(myym varchar,h_id int) cascade""")
        self._cr.execute("""create or replace function getpaymentdate(myym varchar,h_id int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           maxid int ;
         BEGIN
           select max(id) into maxid from era_household_payment_line where payment_ym=myym and payment_id=h_id ;
           select coalesce(payment_date::TEXT,' ') into myres from era_household_payment_line where id = maxid ;
           if myres is null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpaymentdesc(myym varchar,h_id int) cascade""")
        self._cr.execute("""create or replace function getpaymentdesc(myym varchar,h_id int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           maxid int ;
         BEGIN
           select max(id) into maxid from era_household_payment_line where payment_ym=myym and payment_id=h_id ;
           select coalesce(payment_desc,' ') into myres from era_household_payment_line where id = maxid ;
           if myres is null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getstartrental(h_id int) cascade""")
        self._cr.execute("""create or replace function getstartrental(h_id int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           memberid int ;
         BEGIN
           select coalesce(member_id,0) into memberid from era_household_house_line where id = h_id ;
           select start_rental::TEXT into myres from era_household_member where id = memberid ;
           if myres is null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getbsdate(h_id int) cascade""")
        self._cr.execute("""create or replace function getbsdate(h_id int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           memberid int ;
         BEGIN
           select max(bill_start_date)::TEXT into myres from era_household_bill_line where bill_id=h_id ;
           if myres is  null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getbedate(h_id int) cascade""")
        self._cr.execute("""create or replace function getbedate(h_id int) returns varchar as $BODY$
         DECLARE
           myres varchar ;
           memberid int ;
         BEGIN
           select max(bill_end_date)::TEXT into myres from era_household_bill_line where bill_id=h_id ;
           if myres is  null then
              myres = ' ' ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getlastuncompletefee(payid int,payym varchar) cascade""")
        self._cr.execute("""create or replace function getlastuncompletefee(payid int,payym varchar) returns float as $BODY$
         DECLARE
           myres float ;
           ncount int ;
           myid int ;
           myy varchar ;
           mym varchar ;
           myym varchar ;
         BEGIN
            myy = substring(payym,1,4) ;
            mym = substring(payym,6,2) ;
            if mym='01' then
               myy = (myy::INT - 1)::TEXT ;
               myym = concat(myy,'-12') ;
            else
               mym = LPAD((mym::INT - 1)::TEXT,2,'0') ;
               myym = concat(myy,'-',mym) ;
            end if ;
           select count(*) into ncount from era_household_payment_line where payment_id=payid and payment_ym=myym  ;
           if ncount = 0 then
             select max(id) into myid from era_household_payment_line where payment_id=payid and payment_ym < myym ;
           else
             select max(id) into myid from era_household_payment_line where payment_id=payid and payment_ym=myym  ;
           end if ;
           
           select uncomplete_fee into myres from era_household_payment_line where id = myid ;
           return coalesce(myres,0) ;
         END;$BODY$
         LANGUAGE plpgsql ;""")

        self._cr.execute("""drop function if exists gethashousrental(payid int,payym varchar) cascade""")
        self._cr.execute("""create or replace function gethashousrental(payid int,payym varchar) returns Boolean as $BODY$
          DECLARE
            ncount int ;
            myres Boolean ;
          BEGIN
            select count(*) into ncount from era_household_payment_line where payment_id=payid and payment_ym=payym 
                 and house_rental=True ;
            if ncount > 0 then
               myres = True ;
            else
               myres = False ;
            end if ;     
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists run_account_payment(memberid int) cascade""")
        self._cr.execute("""create or replace function run_account_payment(memberid int) returns void as $BODY$
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
            managementfee float ;
            parkspace float ;
            parkmanagement float ;
            loparkmanagement float ;
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
          BEGIN
            select start_rental,end_rental,coalesce(house_rental_fee,0),coalesce(house_management_fee,0),coalesce(parking_space_rent,0),coalesce(parking_management,0),coalesce(water_fee,0),coalesce(lo_parking_management,0) into 
              srental,erental,rentalfee,managementfee,parkspace,parkmanagement,waterfee,loparkmanagement from era_household_member where id=memberid ;
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
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists recall_account_payment(memberid int) cascade""")
        self._cr.execute("""create or replace function recall_account_payment(memberid int) returns void as $BODY$
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
           managementfee float ;
           parkspace float ;
           parkmanagement float ;
           loparkmanagement float ;
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
         BEGIN
           select start_rental,end_rental,coalesce(house_rental_fee,0),coalesce(house_management_fee,0),coalesce(parking_space_rent,0),coalesce(parking_management,0),coalesce(water_fee,0),coalesce(lo_parking_management,0) into 
             srental,erental,rentalfee,managementfee,parkspace,parkmanagement,waterfee,loparkmanagement from era_household_member where id=memberid ;
            update era_member_account set house_rental_fee=rentalfee,house_management_fee=managementfee,parking_space_rent=parkspace,parking_management=parkmanagement,lo_parking_management=loparkmanagement,water_fee=waterfee where member_id=memberid ;  
             select id into houseid from era_household_house_line where member_id=memberid ;
           /* select count(*) into ncount1 from era_member_payment where member_id=memberid ;
            if ncount1 = 0 then
               insert into era_member_payment(member_id,house_id) values (memberid,houseid) ;
            end if ;  */
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genmemberemeter(memberid int) cascade""")
        self._cr.execute("""create or replace function genmemberemeter(memberid int) returns void as $BODY$
          DECLARE
            emeterid int ;
            ncount int ;
            houseid int ;
            emeter_cur refcursor ;
            emeter_rec record ;
            mactive Boolean ;
            userid int ;
          BEGIN
            select active into mactive from era_household_member where id = memberid ;
            select house_id into houseid from era_household_member where id = memberid and active=True; 
            select user_id into userid from era_household_house_line where id = houseid ; 
            /*select max(id) into userid from res_users ; */
            /* update era_household_member set user_id=userid where id = memberid ; */
            if houseid is not null then
               open emeter_cur for select * from era_household_electric_meter where emeter_id = houseid ;
               loop
                 fetch emeter_cur into emeter_rec ;
                 exit when not found ;
                 select count(*) into ncount from era_member_income_emeter where member_id=memberid and emeter_id=emeter_rec.id ;
                 if ncount = 0 then
                    insert into era_member_income_emeter(member_id,emeter_id,start_scale,in_used) values (memberid,emeter_rec.id,0,True) ;
                 end if ;
               end loop ;
               close emeter_cur ;
               /* update era_household_house_line set member_id=memberid,user_id=userid,in_used=True where id = houseid ; */
            end if ;   
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genpayitem(payid int) cascade""")
        self._cr.execute("""create or replace function genpayitem(payid int) returns void as $BODY$
         DECLARE
           ncount int ;
           item_cur refcursor ;
           item_rec record ;
           myyear varchar ;
         BEGIN
           select payment_year into myyear from era_member_payment where id = payid ;
           /* select date_part('year',now())::TEXT into myyear ; */
           open item_cur for select * from era_payment_item order by pay_code ;
           loop 
             fetch item_cur into item_rec ;
             exit when not found ;
             select count(*) into ncount from era_member_payment_line where payment_id=payid and pay_code=item_rec.pay_code ;
             if ncount = 0 then
                insert into era_member_payment_line(payment_id,pay_name,pay_code,pay_year) values (payid,item_rec.name,item_rec.pay_code,myyear) ;
             end if ; 
           end loop ;
           close item_cur ;
           
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpayar(paylineid int) cascade""")
        self._cr.execute("""create or replace function getpayar(paylineid int) returns float as $BODY$
         DECLARE
           myres float ;
           paycode varchar ;
           paymentid int ;
           ncount int ;
           memberid int ;
           rentalfee float ;
           managementfee float ;
           parkspace float ;
           parkmanagement float ;
           loparkspace float ;
           waterfee float ;
           artot float ;
           aptot float ;
           startscale float ;
           currentscale float ;
           priceunit float ;
           memberdeposit float ;
         BEGIN
           
           select count(*) into ncount from era_month_payline_rel where payment_id=paylineid ;  
           select pay_code,payment_id into paycode,paymentid from era_member_payment_line where id=paylineid ;
           select member_id into memberid from era_member_payment where id = paymentid ;
           select coalesce(start_scale,0),coalesce(current_scale,0) into startscale,currentscale from era_member_income_emeter where member_id=memeberid ;
           select coalesce(price_unit,0) into priceunit from era.household_house_line where member_id=memberid ;
           select sum((currentscale-startscale)*priceunit) into artot from era_member_income_emeter where member_id=memeberid ;
           select sum(account_amount) into aptot from era_member_emeter where account_id=memberid ;
           select house_rental_fee,house_management_fee,parking_space_rent,parking_management,lo_parking_management,water_fee,member_deposit into
             rentalfee,managementfee,parkspace,parkmanagement,loparkspace,waterfee,memberdeposit from era_household_member where id = memberid ;
        
           if paycode='01' then    /* 房租 */
              myres = rentalfee * ncount ;
           elsif paycode='02' then   /* 房屋管理費 */
              myres = managementfee * ncount ;
           elsif paycode='03' then  /* 汽車位 */ 
              myres = (parkspace + parkmanagement) * ncount ;
           elsif paycode='04' then  /* 機車位  */
              myres = loparkspace * ncount ;
           elsif paycode='05' then  /* 電費 */
              myres = artot - aptot ;   
           elsif paycode='06' then  /* 水費 */
              myres = waterfee * ncount ;
           elsif paycode='10' then   /* 押金 */
              myres = memberdeposit ;  
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")


        self._cr.execute("""drop function if exists genpaymentinfo(payid int) cascade""")
        self._cr.execute("""create or replace function genpaymentinfo(payid int) returns void as $BODY$
          DECLARE
           pl_cur refcursor ;
           pl_rec record ;
           mon_cur refcursor ;
           mon_rec record ;
           cyear varchar ;
           cmonth varchar ;
           cym varchar ;
           ncount int ;
           payap float ;
           memberid int ;
           paymentid int ;
           mynowdate date ;
           ncount1 int ;
           userid int ;
           hasconfirm Boolean ;
           accid int ;
           ncount2 int ;
          BEGIN
           select now()::DATE into mynowdate ;
           select member_id,user_id,has_confirm into memberid,userid,hasconfirm from era_member_payment where id = payid ;
           open pl_cur for select * from era_member_payment_line where payment_id=payid and pay_active=True;
           loop
             fetch pl_cur into pl_rec ;
             exit when not found ;
             if pl_rec.month_num is null or pl_rec.month_num=0 then
                payap = coalesce(pl_rec.pay_ap,0)::numeric ;
             else
                payap =  round((coalesce(pl_rec.pay_ap,0)::numeric/coalesce(pl_rec.month_num,1)::numeric),0) ;
             end if ;
             if pl_rec.pay_code='05' then   /* 電費 */
                  select count(*) into ncount1 from era_member_emeter where account_id=memberid and member_payment_id=payid ;
                  if ncount1=0 then
                     insert into era_member_emeter(account_id,account_date,account_amount,user_id,member_payment_id)
                      values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid) ;
                  else
                     update era_member_emeter set account_amount=pl_rec.pay_ap where account_id=memberid and member_payment_id=payid ;
                  end if ;   
             end if ;
             if pl_rec.pay_code='07' then   /* 一般違約金 */
                  select count(*) into ncount1 from era_member_emeter where account_id=memberid and member_payment_id=payid ;
                  if ncount1=0 then
                     insert into era_member_breach_contract(account_id,account_date,breach_07_amount,user_id,member_payment_id)
                      values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid) ;
                  else
                     update era_member_breach_contract set breach_07_amount=coalesce(pl_rec.pay_ap,0) where account_id=memberid and member_payment_id=payid ;
                  end if ;   
             end if ;
             if pl_rec.pay_code='08' then   /* 損壞違約金 */
                  select count(*) into ncount1 from era_member_emeter where account_id=memberid and member_payment_id=payid ;
                  if ncount1=0 then
                     insert into era_member_breach_contract(account_id,account_date,breach_08_amount,user_id,member_payment_id)
                      values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid) ;
                  else
                     update era_member_breach_contract set breach_08_amount=coalesce(pl_rec.pay_ap,0) where account_id=memberid and member_payment_id=payid ;
                  end if ;   
             end if ;
             if pl_rec.pay_code='09' then   /* 提前解約違約金 */
                  select count(*) into ncount1 from era_member_emeter where account_id=memberid and member_payment_id=payid ;
                  if ncount1=0 then
                     insert into era_member_breach_contract(account_id,account_date,breach_09_amount,user_id,member_payment_id)
                      values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid) ;
                  else
                     update era_member_breach_contract set breach_09_amount=coalesce(pl_rec.pay_ap,0) where account_id=memberid and member_payment_id=payid ;
                  end if ;   
             end if ;
             if pl_rec.pay_code='10' then   /* 押金 */
                  select count(*) into ncount1 from era_member_deposit where account_id=memberid and member_payment_id=payid ;
                  if ncount1=0 then
                     if pl_rec.pay_ap < 0 then
                       insert into era_member_deposit(account_id,account_date,deposit_amount,user_id,member_payment_id,deposit_status)
                         values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid,'2') ;
                     else
                       insert into era_member_deposit(account_id,account_date,deposit_amount,user_id,member_payment_id,deposit_status)
                         values (memberid,mynowdate,coalesce(pl_rec.pay_ap,0),userid,payid,'1') ;
                     end if ;    
                  else
                     if pl_rec.pay_ap < 0 then
                       update era_member_deposit set deposit_amount=coalesce(pl_rec.pay_ap,0),deposit_status='2' where account_id=memberid and member_payment_id=payid ;
                     else
                       update era_member_deposit set deposit_amount=coalesce(pl_rec.pay_ap,0),deposit_status='1' where account_id=memberid and member_payment_id=payid ;
                     end if ;  
                  end if ;   
             end if ;
             open mon_cur for select * from era_month_payline_rel where payment_id = pl_rec.id ;
             loop
               fetch mon_cur into mon_rec ;
               exit when not found ;
               select value into cmonth from era_payment_month where id=mon_rec.month_id ;
               cym = concat(pl_rec.pay_year,'-',cmonth) ;
               select id into accid from era_member_account where account_ym=cym and member_id=memberid ;

               if pl_rec.pay_code='01' then    /*  房租  */
                  update era_member_account set house_rental_pay=coalesce(house_rental_pay,0)+payap where id=accid ;
               elsif pl_rec.pay_code='02' then  /* 房屋管理費  */
                  update era_member_account set house_management_pay=coalesce(house_management_pay,0)+payap where id=accid ;
               elsif pl_rec.pay_code='03' then  /* 汽車位管理費    */
                  update era_member_account set parking_space_pay=coalesce(parking_space_pay,0)+payap where id=accid ;
               elsif pl_rec.pay_code='04' then  /*  機車位管理費   */
                  update era_member_account set lopark_management_pay=coalesce(lopark_management_pay,0)+payap where id=accid ;
               elsif pl_rec.pay_code='06' then  /*  水費   */
                  update era_member_account set water_pay=coalesce(water_pay,0)+payap where id = accid ;
               end if ;
               select count(*) into ncount2 from era_member_account_payment_rel where acc_id=accid and payment_id=payid ;
               if ncount2=0 and accid is not null then   
                  insert into era_member_account_payment_rel(acc_id,payment_id) values (accid,payid) ;
               end if ;   
             end loop ;
             close mon_cur ;
           end loop ;
           close pl_cur ;
           update era_member_payment set has_confirm=True where id = payid ;
           update era_member_account set house_rental_pay=0 where house_rental_pay < 0 ;
           update era_member_account set house_management_pay=0 where house_management_pay < 0 ;
           update era_member_account set parking_space_pay=0 where parking_space_pay < 0 ;
           update era_member_account set lopark_management_pay=0 where lopark_management_pay < 0 ;
           update era_member_account set water_pay=0 where water_pay < 0 ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delpaymentinfo(payid int) cascade""")
        self._cr.execute("""create or replace function delpaymentinfo(payid int) returns void as $BODY$
         DECLARE
           pl_cur refcursor ;
           pl_rec record ;
           acc_cur refcursor ;
           acc_rec record ;
           memberid int ;
           hasconfirm Boolean ;
           ncount int ;
           npayap float ;
         BEGIN
          select count(*) into ncount from era_member_account_payment_rel where payment_id=payid ;
          select member_id,has_confirm into memberid,hasconfirm from era_member_payment where id = payid ;
          open pl_cur for select * from era_member_payment_line where payment_id=payid and pay_active=true ;
           loop
             fetch pl_cur into pl_rec ;
             exit when not found ;
             if pl_rec.month_num is null or pl_rec.month_num=0 then
                npayap = coalesce(pl_rec.pay_ap,0)::numeric ;
             else
                npayap = round(coalesce(pl_rec.pay_ap,0)::numeric/coalesce(pl_rec.month_num,1)::numeric);
             end if ;
             open acc_cur for select * from era_member_account_payment_rel where payment_id=payid ;
             loop
               fetch acc_cur into acc_rec ;
               exit when not found ;
               if pl_rec.pay_code='01' then    /*  房租  */
                  update era_member_account set house_rental_pay=coalesce(house_rental_pay,0) - npayap where id = acc_rec.acc_id ;
                  update era_member_account set house_rental_pay=0 where id = acc_rec.acc_id and house_rental_pay < 0 ;
               elsif pl_rec.pay_code='02' then  /* 房屋管理費  */
                  update era_member_account set house_management_pay=coalesce(house_management_pay,0) - npayap where id = acc_rec.acc_id ;
                  update era_member_account set house_management_pay=0 where id = acc_rec.acc_id and house_management_pay < 0 ;
               elsif pl_rec.pay_code='03' then  /* 汽車位管理費    */
                  update era_member_account set parking_space_pay=coalesce(parking_space_pay,0) - npayap where id = acc_rec.acc_id ;
                  update era_member_account set parking_space_pay=0 where id = acc_rec.acc_id and parking_space_pay < 0 ;
               elsif pl_rec.pay_code='04' then  /*  機車位管理費   */
                  update era_member_account set lopark_management_pay=coalesce(lopark_management_pay,0) - npayap where id = acc_rec.acc_id ;       
                  update era_member_account set lopark_management_pay=0 where id = acc_rec.acc_id and lopark_management_pay < 0 ; 
               end if ;             
             end loop ;
             close acc_cur ;
             
             if pl_rec.pay_code='05' then  /* 電費 */
                  update era_member_emeter set account_amount=0 where account_id=memberid and member_payment_id=payid ;        
             elsif pl_rec.pay_code='06' then  /*  水費   */
                  update era_member_account set water_pay=0 where member_payment_id=payid and member_id=memberid ;
             elsif pl_rec.pay_code='07' or pl_rec.pay_code='08' or pl_rec.pay_code='09' then /* 違約金 */
                  update era_member_breach_contract set breach_07_amount=0,breach_08_amount=0,breach_09_amount=0 
                     where member_payment_id=payid and account_id=memberid ;  
             elsif pl_rec.pay_code='10' then   /* 押金 */
                  /* update era_member_deposit set deposit_amount=0  where member_payment_id=payid and account_id=memberid ; */
                  delete from era_member_deposit where member_payment_id=payid and account_id=memberid ;    
             end if ;     
           end loop ;
           close pl_cur ;
           update era_member_payment set has_confirm=False where id = payid ;
           delete from era_member_account_payment_rel where payment_id = payid ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("drop function if exists gencontractstart(memberid int,em1 float,em2 float,mdep float) cascade")
        self._cr.execute("""create or replace function gencontractstart(memberid int,em1 float,em2 float,mdep float) returns void as $BODY$
         DECLARE
           houseid int ;
           em220v int ;
           em110v int ;
           ncount int ;
           ncount1 int ;
           ncount2 int ;
         BEGIN
           select id into houseid from era_household_house_line where member_id=memberid ;  
           if houseid is not null then
              select id into em220v from era_household_electric_meter where emeter_id=houseid and emeter_name like '%220%' ;
              select id into em110v from era_household_electric_meter where emeter_id=houseid and emeter_name like '%110%' ;
              if em220v is not null then
                 select count(*) into ncount from era_member_income_emeter where member_id=memberid and emeter_id=em220v ;
                 if ncount > 0 then
                    update era_member_income_emeter set start_scale=em1 where member_id=memberid and emeter_id=em220v ;
                 end if ;
              end if ;
               if em110v is not null then
                 select count(*) into ncount1 from era_member_income_emeter where member_id=memberid and emeter_id=em110v ;
                 if ncount1 > 0 then
                    update era_member_income_emeter set start_scale=em2 where member_id=memberid and emeter_id=em110v ;
                 end if ;
              end if ;
           end if ;
           /* update era_household_member set member_deposit=mdep where id = memberid ; */
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists getpaymentym() cascade""")
        self._cr.execute("""create or replace function getpaymentym() returns varchar as $BODY$
         DECLARE
            myyear varchar ;
         BEGIN
            select date_part('year',now())::TEXT into myyear ;
            return myyear ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists selmonth(memberid int,paycode varchar,payyear varchar) cascade""")
        self._cr.execute("""create or replace function selmonth(memberid int,paycode varchar,payyear varchar) returns setof INT as $BODY$
         DECLARE
           m_cur refcursor ;
           m_rec record ;
         BEGIN
           if paycode='01' then        /* 房屋租金 */
                open m_cur for select * from era_payment_month where "value" not in (select substring(account_ym,6,2) from 
                    era_member_account where substring(account_ym,1,4)=payyear and member_id=memberid and house_rental_pay > 0)
                    and "value" in (select substring(account_ym,6,2) from era_member_account where substring(account_ym,1,4)=payyear
                     and member_id=memberid and house_rental_fee > 0);
                loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  return next m_rec.id ;
                end loop ;
                close m_cur ;
             elsif paycode='02' then     /* 房屋管理費 */
                open m_cur for select * from era_payment_month where "value" not in (select substring(account_ym,6,2) from 
                    era_member_account where substring(account_ym,1,4)=payyear and member_id=memberid and house_management_pay > 0) 
                    and "value" in (select substring(account_ym,6,2) from era_member_account where substring(account_ym,1,4)=payyear
                    and member_id=memberid and house_management_fee > 0) ;
                loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  return next m_rec.id ;
                end loop ;
                close m_cur ;
             elsif paycode='03' then     /* 汽車位 */
                open m_cur for select * from era_payment_month where "value" not in (select substring(account_ym,6,2) from 
                    era_member_account where substring(account_ym,1,4)=payyear and member_id=memberid and parking_space_pay > 0)  
                    and "value" in (select substring(account_ym,6,2) from era_member_account where substring(account_ym,1,4)=payyear
                    and member_id=memberid and parking_space_rent > 0) ;
                loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  return next m_rec.id ;
                end loop ;
                close m_cur ;
             elsif paycode='04' then     /* 機車位 */
                open m_cur for select * from era_payment_month where "value" not in (select substring(account_ym,6,2) from 
                    era_member_account where substring(account_ym,1,4)=payyear and member_id=memberid and lopark_management_pay > 0) 
                     and "value" in (select substring(account_ym,6,2) from era_member_account where substring(account_ym,1,4)=payyear
                     and member_id=memberid and lo_parking_management > 0) ;
                loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  return next m_rec.id ;
                end loop ;
                close m_cur ;
             elsif paycode='06' then
                open m_cur for select * from era_payment_month where "value" not in (select substring(account_ym,6,2) from 
                    era_member_account where substring(account_ym,1,4)=payyear and member_id=memberid and water_pay > 0) 
                     and "value" in (select substring(account_ym,6,2) from era_member_account where substring(account_ym,1,4)=payyear
                     and member_id=memberid and water_fee > 0) ;
                loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  return next m_rec.id ;
                end loop ;
                close m_cur ;
             else
             end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists checkselmonth(paymentid int) cascade""")
        self._cr.execute("""create or replace function checkselmonth(paymentid int) returns Boolean as $BODY$
         DECLARE
           memberid int ;
           payl_cur refcursor ;
           payl_rec record ;
           m_cur refcursor ;
           m_rec record ;
           myres Boolean ;
           ncount int ;
         BEGIN
           myres = True ; 
           select member_id into memberid from era_member_payment where id = paymentid ;
           open payl_cur for select * from era_member_payment_line where payment_id=paymentid and pay_status='2' ;
           loop
             fetch payl_cur into payl_rec ;
             exit when not found ;
               if payl_rec.pay_code='01' then        /* 房屋租金 */
                    open m_cur for select * from era_payment_month where "value" in (select substring(account_ym,6,2) from 
                        era_member_account where substring(account_ym,1,4)=payl_rec.pay_year and member_id=memberid and house_rental_pay > 0) ;
                    loop
                      fetch m_cur into m_rec ;
                      exit when not found ;
                      ncount = 0 ;
                      select count(*) into ncount from era_month_payline_rel where payment_id=payl_rec.id and month_id=m_rec.id ;
                      if ncount > 0 then
                         myres = False ;
                      end if ;
                    end loop ;
                    close m_cur ;
               elsif payl_rec.pay_code='02' then     /* 房屋管理費 */
                    open m_cur for select * from era_payment_month where "value" in (select substring(account_ym,6,2) from 
                        era_member_account where substring(account_ym,1,4)=payl_rec.pay_year and member_id=memberid and house_management_pay > 0) ;
                    loop
                      fetch m_cur into m_rec ;
                      exit when not found ;
                      ncount = 0 ;
                      select count(*) into ncount from era_month_payline_rel where payment_id=payl_rec.id and month_id=m_rec.id ;
                      if ncount > 0 then
                         myres = False ;
                      end if ;
                    end loop ;
                    close m_cur ;
               elsif payl_rec.pay_code='03' then     /* 汽車位 */
                    open m_cur for select * from era_payment_month where "value" in (select substring(account_ym,6,2) from 
                        era_member_account where substring(account_ym,1,4)=payl_rec.pay_year and member_id=memberid and parking_space_pay > 0) ;
                    loop
                      fetch m_cur into m_rec ;
                      exit when not found ;
                      ncount = 0 ;
                      select count(*) into ncount from era_month_payline_rel where payment_id=payl_rec.id and month_id=m_rec.id ;
                      if ncount > 0 then
                         myres = False ;
                      end if ;
                    end loop ;
                    close m_cur ;
               elsif payl_rec.pay_code='04' then     /* 機車位 */
                    open m_cur for select * from era_payment_month where "value" in (select substring(account_ym,6,2) from 
                        era_member_account where substring(account_ym,1,4)=payl_rec.pay_year and member_id=memberid and lopark_management_pay > 0) ;
                    loop
                      fetch m_cur into m_rec ;
                      exit when not found ;
                      ncount = 0 ;
                      select count(*) into ncount from era_month_payline_rel where payment_id=payl_rec.id and month_id=m_rec.id ;
                      if ncount > 0 then
                         myres = False ;
                      end if ;
                    end loop ;
                    close m_cur ;
               elsif payl_rec.pay_code='06' then  /* 水費 */
                    open m_cur for select * from era_payment_month where "value" in (select substring(account_ym,6,2) from 
                        era_member_account where substring(account_ym,1,4)=payl_rec.pay_year and member_id=memberid and water_pay > 0) ;
                    loop
                      fetch m_cur into m_rec ;
                      exit when not found ;
                      ncount = 0 ;
                      select count(*) into ncount from era_month_payline_rel where payment_id=payl_rec.id and month_id=m_rec.id ;
                      if ncount > 0 then
                         myres = False ;
                      end if ;
                    end loop ;
                    close m_cur ;
               end if ;
           end loop ;
           close payl_cur ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genhousemember() cascade""")
        self._cr.execute("""create or replace function genhousemember() returns void as $BODY$
         DECLARE
           m_cur refcursor ;
           m_rec record ;
           houseid int ;
         BEGIN
           /* member_type='1' 租戶 */
           open m_cur for select * from era_household_member where house_id is null and active=True and member_type='1' ;
           loop
             fetch m_cur into m_rec ;
             exit when not found ;
             select id into houseid from era_household_house_line where member_id=m_rec.id ;
             update era_household_member set house_id=houseid where id=m_rec.id ;
           end loop ;
           close m_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists delmemberaccount(accid int) cascade""")
        self._cr.execute("""create or replace function delmemberaccount(accid int) returns void as $BODY$
          DECLARE
            amounttot float ;
          BEGIN
            select sum(coalesce(house_rental_pay,0)+coalesce(house_management_pay,0)+coalesce(parking_space_pay,0)+coalesce(parking_management_pay,0)+coalesce(lopark_management_pay,0)+coalesce(water_pay,0)) 
               into amounttot from era_member_account where member_id=accid ;
            if amounttot = 0 then
               delete from era_member_account where member_id=accid ;
            end if ;    
          END;$BODY$
          LANGUAGE plpgsql;""")

        self.env.cr.execute("""drop function if exists checkdbinfo() cascade""")
        self.env.cr.execute("""create or replace function checkdbinfo() returns Boolean as $BODY$
          DECLARE
            ncount int ;
            myres Boolean ;
          BEGIN
            myres = True ; 
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;  """)

        self.env.cr.execute("""drop function if exists get_emeter_status(emeterid int) cascade""")
        self.env.cr.execute("""create or replace function get_emeter_status(emeterid int) returns varchar as $BODY$
          DECLARE
            ncount int ;
            myres varchar ;
            maxid int ;
          BEGIN
            myres = 'NG' ;
            select max(id) into maxid from era_household_emeter_line where emeter_id=emeterid ;
            if maxid is not null then
               select emeter_status into myres from era_household_emeter_line where id=maxid ;
            end if ;   
            return myres ;
          END;$BODY$
          LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists genemeterhubid() cascade""")
        self._cr.execute("""create or replace function genemeterhubid() returns void as $BODY$
          DECLARE
            s_cur refcursor ;
            s_rec record ;
            emetername varchar ;
            emeterhubid int ;
          BEGIN
            open s_cur for select * from era_emeter_status where emeter_id1 is null ;
            loop
              fetch s_cur into s_rec ;
              exit when not found ;
              select substring(emeter_name,1,8) into emetername from era_household_electric_meter where id = s_rec.emeter_id ;
              select id into emeterhubid from era_emeterhub_status where pi_id=emetername ;
              if emeterhubid is not null then
                 update era_emeter_status set emeter_id1=emeterhubid where id = s_rec.id ;
              end if ;
            end loop ;
            close s_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists era_chkout_archive(memberid int) cascade""")
        self._cr.execute("""drop function if exists era_chkout_archive(memberid int,archtype Boolean) cascade""")
        self._cr.execute("""create or replace function era_chkout_archive(memberid int,archtype Boolean) returns void as $BODY$
          DECLARE
            ncount int ;
            userid int ;
          BEGIN
            select user_id into userid from era_household_member where id = memberid ;
            if userid is not null  then
               update res_users set active=False where id = userid ;
            end if ;
            if archtype=TRUE then
               update era_household_member set active=False where id=memberid ;
            end if ;   
            update era_member_income_emeter set in_used=FALSE where member_id=memberid ;
            update era_member_line_user set active=False where member_id=memberid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chnewuser(nuid int,nlogin varchar,npwd varchar) cascade""")
        self._cr.execute("""create or replace function chnewuser(nuid int,nlogin varchar,npwd varchar) returns void as $BODY$
          DECLARE
            parid int ;
            memberid int ;
          BEGIN
            update res_users set login=nlogin,password=npwd,active=True where id = nuid ;
            select partner_id into parid from res_users where id = nuid ;
            if parid is not null then
               update res_partner set name=nlogin,email=nlogin,display_name=nlogin where id = parid ;
            end if ;
            select max(id) into memberid from era_household_member where member_no=nlogin and active=TRUE ;
            update era_household_member set user_id=nuid where id = memberid ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists chkuser(nlogin varchar) cascade""")
        self._cr.execute("""create or replace function chkuser(nlogin varchar) returns Boolean as $BODY$
         DECLARE
           ncount int ;
           myres Boolean ;
         BEGIN
           select count(*) into ncount from res_users where login=nlogin ;
           if ncount = 0 then
              myres = False ;
           else
              myres = True ;
           end if ;
           return myres ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genescaletot(projno int,startdate date,enddate date) cascade""")
        self._cr.execute("""create or replace function genescaletot(projno int,startdate date,enddate date) returns void as $BODY$
          DECLARE
            h_cur refcursor ;
            h_rec record ;
            e_cur refcursor ;
            e_rec record ;
            mysdt timestamp ;
            mysid int ;
            mysscale float ;
            myedt timestamp ;
            myeid int ;
            myescale float ;
            myduration float ;
          BEGIN
            select concat(startdate::TEXT,' 00:00:00')::timestamp - interval '8 hours' into mysdt ;
            select concat(enddate::TEXT,' 23:59:59')::timestamp - interval '8 hours' into myedt ;
            delete from era_escaletot_line ;
            open h_cur for select id,house_id,member_id,house_no from era_household_house_line where house_id = projno ;
            loop
              fetch h_cur into h_rec ;
              exit when not found ;
              open e_cur for select id,emeter_id from era_household_electric_meter where emeter_id = h_rec.id ;
              loop
                fetch e_cur into e_rec ;
                exit when not found ;
                select min(id) into mysid from era_household_used_line where used_emeter_id=e_rec.id and used_datetime::timestamp >= mysdt::timestamp ;
                select used_scale into mysscale from era_household_used_line where id = mysid ;
                select max(id) into myeid from era_household_used_line where used_emeter_id=e_rec.id and used_datetime::timestamp <= myedt::timestamp ;
                select used_scale into myescale from era_household_used_line where id = myeid ;
                myduration = myescale - mysscale ;
                insert into era_escaletot_line(house_id,house_no,member_id,emeter_id,start_date,end_date,start_scale,end_scale,duration_scale) values
                  (projno,h_rec.house_no,h_rec.member_id,e_rec.id,startdate,enddate,mysscale,myescale,myduration) ;
              end loop ;
              close e_cur ;
            end loop ;
            close h_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genallpayment() cascade""")
        self._cr.execute("""create or replace function genallpayment() returns void as $BODY$
         DECLARE
           pay_cur refcursor ;
           pay_rec record ;
         BEGIN
         delete from era_member_account_payment_rel  ;
         update era_member_emeter set account_amount=0  ;        
         update era_member_account set water_pay=0  ;
         update era_member_breach_contract set breach_07_amount=0,breach_08_amount=0,breach_09_amount=0 ;    
         update era_member_account set house_rental_pay=0,house_management_pay=0,parking_space_pay=0,lopark_management_pay=0 ;
           update era_member_payment set has_confirm=False ;
           open pay_cur for select * from era_member_payment ;
           loop
             fetch pay_cur into pay_rec ;
             exit when not found ;
             execute genpaymentinfo(pay_rec.id) ;
           end loop ;
           close pay_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genemeterinused() cascade""")
        self._cr.execute("""create or replace function genemeterinused() returns void as $BODY$
         DECLARE
           ncount int ;
           in_cur refcursor ;
           in_rec record ;
           mynowdate date ;
           memberid int ;
           incomedate date ;
           startdate date ;
           enddate date ;
         BEGIN
           select (current_timestamp + interval '8 hour')::DATE into mynowdate ;
           open in_cur for select * from era_member_income_emeter ;
           loop
             fetch in_cur into in_rec ;
             exit when not found ;
             if in_rec.start_date is null or in_rec.end_date is null then
                select income_date,start_rental,end_rental into incomedate,startdate,enddate
                    from era_household_member where id = in_rec.member_id ;
                if in_rec.start_date is null then
                   update era_member_income_emeter set start_date = incomedate where id = in_rec.id ;
                end if ;    
                if in_rec.end_date is null then
                   update era_member_income_emeter set end_date = enddate where id = in_rec.id ;
                end if ;
                select count(*) into ncount from era_member_income_emeter where id = in_rec.id and 
                   (mynowdate between startdate and enddate) ; 
                if ncount > 0 then
                   update era_member_income_emeter set in_used=TRUE where id = in_rec.id ;
                else
                   update era_member_income_emeter set in_used=FALSE where id = in_rec.id ;
                end if ;   
             end if ;
           end loop ;
           close in_cur ;
         END;$BODY$
         LANGUAGE plpgsql;  """)

        self._cr.execute("""drop function if exists genhousememberisused() cascade""")
        self._cr.execute("""create or replace function genhousememberisused() returns void as $BODY$
          DECLARE
            houseno varchar ;
            mpid varchar ;
            mylogin varchar ;
            mymemberno varchar ;
            h_cur refcursor ;
            h_rec record ;
            m_cur refcursor ;
            m_rec record ;
            ncount int ;
          BEGIN
            delete from era_house_member_chk ;
            open m_cur for select id,user_id,member_no,active,house_id,member_pid from era_household_member where active=True ;
            loop
              fetch m_cur into m_rec ;
              exit when not found ;
              if m_rec.user_id is null then
                 select count(*) into ncount from era_house_member_chk where member_id=m_rec.id ;
                 insert into era_house_member_chk(member_id) values (m_rec.id) ;
              else
                 select login into mylogin from res_users where id = m_rec.user_id and active=True ;
                 if mylogin != m_rec.member_no then
                     select count(*) into ncount from era_house_member_chk where member_id=m_rec.id ;
                     insert into era_house_member_chk(member_id) values (m_rec.id) ;
                 end if ;   
              end if ;
              if m_rec.house_id is null then
                 select count(*) into ncount from era_house_member_chk where member_id=m_rec.id ;
                 insert into era_house_member_chk(member_id) values (m_rec.id) ;
              else
                 select house_no into houseno from era_household_house_line where id = m_rec.house_id and in_used=True;
                 mymemberno = concat(houseno,'-',m_rec.member_pid) ;
                 if m_rec.member_no != mymemberno then
                    select count(*) into ncount from era_house_member_chk where member_id=m_rec.id ;
                    insert into era_house_member_chk(member_id) values (m_rec.id) ;
                 end if ;
              end if ; 
            end loop ;
            close m_cur ;
            open h_cur for select id,member_id,house_no,user_id,in_used from era_household_house_line where in_used=True ;
            loop
              fetch h_cur into h_rec ;
              exit when not found ;
              /* select count(*) into ncount from era_household_house_line where member_id is null or user_id is null ; */
              if h_rec.member_id is null or h_rec.user_id is null then
                 insert into era_house_member_chk(house_id) values (h_rec.id) ;
              end if ; 
              select login into mylogin from res_users where id = h_rec.user_id and active=True ;
              if mylogin is not null then
                 select member_no into mymemberno from era_household_member where id = h_rec.member_id and active=TRUE ;
                 if mymemberno is not null and mymemberno != mylogin then
                 insert into era_house_member_chk(house_id) values (h_rec.id) ;
                 end if ;
              end if ;
            end loop ;
            close h_cur ;
          END;$BODY$
          LANGUAGE plpgsql;
          """)







