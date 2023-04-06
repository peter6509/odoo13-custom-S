# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError




class eralinemessagestoreproc(models.Model):
    _name = "era.linemessage_storeproc"

    @api.model
    def init(self):
        self.env.cr.execute("""drop function if exists gensendmessage(projid int,wizardid int,senddate date,linemsg varchar) cascade""")
        self.env.cr.execute("""create or replace function gensendmessage(projid int,wizardid int,senddate date,linemsg varchar) returns void as $BODY$
          DECLARE
            u_cur refcursor ;
            u_rec record ;
            rel_cur refcursor ;
            rel_rec record ;
            m_cur refcursor ;
            m_rec record ;
            ncount int ;
          BEGIN
            select count(*) into ncount from era_manual_line_member_rel where message_id=wizardid ;
            if ncount > 0 then
               open rel_cur for select * from era_manual_line_member_rel where message_id=wizardid ;
               loop
                  fetch rel_cur into rel_rec ;
                  exit when not found ;
                  open u_cur for select * from era_member_line_user where member_id=rel_rec.member_id and send_announcement=TRUE ;
                  loop
                    fetch u_cur into u_rec ;
                    exit when not found ;
                    insert into era_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,message_text,active) values
                        (senddate,projid,u_rec.line_user_id,u_rec.member_id,FALSE,'1',linemsg,TRUE) ;
                  end loop ;
                  close u_cur ;
               end loop ;
               close rel_cur ;
            else
               open m_cur for select * from era_household_member where house_id in (select id from era_household_house_line where house_id=projid) ;
               loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  open u_cur for select * from era_member_line_user where member_id=m_rec.id and send_announcement=TRUE ;
                  loop
                    fetch u_cur into u_rec ;
                    exit when not found ;
                    insert into era_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,message_text,active) values
                     (senddate,projid,u_rec.line_user_id,m_rec.id,FALSE,'1',linemsg,TRUE) ;
                  end loop ;
                  close u_cur ;
               end loop ;
               close m_cur ;
            end if ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genlinemsgarchive() cascade""")
        self._cr.execute("""create or replace function genlinemsgarchive() returns void as $BODY$
          DECLARE
            duedate date ;
          BEGIN
            select current_timestamp::DATE - interval '7 day' into duedate ;
            update era_send_line_message set active=FALSE where active=TRUE and send_status=TRUE and send_date <= duedate ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genaccbillmsg() cascade""")
        self._cr.execute("""create or replace function genaccbillmsg() returns void as $BODY$
          DECLARE
            m_cur refcursor ;
            m_rec record ;
            lu_cur refcursor ;
            lu_rec record ;
            senddate date ;
            dueday varchar ;
            dueym varchar ;
            dueym1 varchar ;
            ncount int ;
            houseid int ;
            cym varchar ;
          BEGIN
            open m_cur for select * from era_household_member where active=TRUE and start_rental is not null ;
            loop
               fetch m_cur into m_rec ;
               exit when not found ;
               select house_id into houseid from era_household_house_line where id = m_rec.house_id ;
               select substring(current_timestamp::DATE::TEXT,1,8) into dueym ; /* 2022-04- */
               select substring(current_timestamp::DATE::TEXT,1,7) into dueym1 ; /* 2022-04 */
               /* senddate = concat(dueym,'01')::DATE + interval '1 month' - interval '1 day' ;*/
               select lpad(date_part('month',current_timestamp::DATE)::TEXT,2,'0') into cym ;
               select lpad(date_part('day',m_rec.start_rental::DATE)::TEXT,2,'0') into dueday ;
               if cym = '02' and dueday in ('29','30','31') then
                  dueday = '28' ;
               elsif cym not in ('01','03','05','07','08','10','12') and dueday='31' then
                  dueday = '30' ;
               end if ;   
               senddate = concat(dueym,dueday)::DATE ;
               update era_household_member set ar_date=senddate where id = m_rec.id ;
               if dueday::INT > 3 then
                  select senddate - interval '3 day' into senddate ;  /* 帳單日前3天 */
               else
                  execute checkconfig();
                  execute genmemberlineinfo();   
               end if ;   
               select count(*) into ncount from era_send_line_message where send_date=senddate and member_id=m_rec.id and send_message_type='2';
               if ncount = 0 then
                  open lu_cur for select * from era_member_line_user where member_id = m_rec.id and send_acc_bill=TRUE ;
                  loop
                    fetch lu_cur into lu_rec ;
                    exit when not found ;
                    insert into era_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,active) values 
                      (senddate,houseid,lu_rec.line_user_id,m_rec.id,FALSE,'2',TRUE) ;
                  end loop ;
                  close lu_cur ;
               end if ;
            end loop ;
            close m_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists ckcando() cascade""")
        self._cr.execute("""create or replace function ckcando() returns void as $BODY$
          DECLARE
            mytoday date ;
          BEGIN
            select (current_timestamp + interval '8 hours')::DATE into mytoday ;
            update era_send_line_message set can_do=True,send_status=False where (send_status=FALSE or send_status is null) and send_date::DATE <= mytoday::DATE ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # self._cr.execute("""drop function if exists chk_special_material(prodid int) cascade""")
        # self._cr.execute("""create or replace function chk_special_material(prodid int) returns Boolean as $BODY$
        #    /* return : True 代表是專用料   False 代表非專用料 */
        #  DECLARE
        #    myres Boolean ;
        #    l_cur refcursor ;
        #    l_rec record ;
        #    pprodtmplid int ;
        #    pprodid int ;
        #    maxparentprod int ; /* 最終產品 */
        #    maxpprod integer[]; /* 最終產品 陣列 */
        #    haveparent Boolean ;
        #    mybomid int ;
        #    ncount int ;
        #    ncount1 int ;
        #    lbomid int ;
        #    lprodid int ;
        #  BEGIN
        #    myres = True ; /* True 表示專用料  False 表示非專用料 */
        #    haveparent = True ;
        #    maxparentprod = 0 ;
        #    select maxpprod[]::INT[] ; /* 賦予 maxpprod 空陣列 */
        #    open l_cur for select bom_id,product_id from mrp_bom_line where product_id = prodid ;
        #    loop
        #       fetch l_cur into l_rec ;
        #       exit when not found ;
        #       mybomid = l_rec.bom_id ;
        #       loop
        #          exit when haveparent=False ;
        #          select count(*) into ncount from mrp_bom where id = mybomid ;
        #          if ncount = 0 then
        #             haveparent = False ;
        #          end if ;
        #          select product_tmpl_id into pprodtmplid from mrp_bom where id = mybomid ;
        #          select id into pprodid from product_product where product_tmpl_id = pprodtmplid ;
        #          select count(*) into ncount1 from mrp_bom_line where product_id = pprodid ;
        #          if ncount1 = 0 then   /* 已再無上階 parts */
        #             haveparent = False ;
        #             if maxparentprod = 0 then
        #                 maxparentprod = pprodid ;
        #                 select array_append(maxpprod,pprodid) ; /* 新增新的 pprodid */
        #             else
        #                 if maxparentprod != pprodid then
        #                    select array_remove(maxpprod,pprodid) ; /* 去除存在的 pprodid */
        #                    select array_append(maxpprod,pprodid) ; /* 新增新的 pprodid */
        #                end if ;
        #             end if ;
        #          else
        #             select bom_id into mybomid from mrp_bom_line where product_id = pprodid ;
        #          end if ;
        #       end loop ;
        #    end loop ;
        #    close l_cur ;
        #    if array_length(maxpprod,1) is null then
        #       myres = True ;
        #    else
        #       if array_length(maxpprod,1) > 1 then
        #          myres = False ;
        #       else
        #          myres = True ;
        #       end if ;
        #    end if ;
        #    return myres ;
        #  END;$BODY$
        #  LANGUAGE plpgsql;""")
        #
        # self._cr.execute("""drop function if exists get_categ_special_prod(categid int) cascade""")
        # self._cr.execute("""create or replace function get_categ_special_prod(categid int) returns SETOF varchar as $BODY$
        #  DECLARE
        #    categ_cur refcursor ;
        #    categ_rec record ;
        #    ppid int ;  /* product_product id */
        #    spec_prod Boolean ;
        #    myres varchar ;
        #  BEGIN
        #     open categ_cur for select id,categ_id,default_code from product_template where categ_id=categid and active=True ;
        #     loop
        #       fetch categ_cur into categ_rec ;
        #       exit when not found ;
        #       select id into ppid from product_product where product_tmpl_id=categ_rec.id ;
        #       select chk_special_material(ppid) into spec_prod ;
        #       if spec_prod=True then
        #          return next categ_rec.default_code ;
        #       end if ;
        #     end loop ;
        #     close categ_cur ;
        #  END;$BODY$
        #  LANGUAGE plpgsql;
        #  """)
