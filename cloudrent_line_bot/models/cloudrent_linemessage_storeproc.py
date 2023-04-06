# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class cloudrentlinemessagestoreproc(models.Model):
    _name = "cloudrent.linemessage_storeproc"

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
            nowdate timestamp ;
          BEGIN
            select current_timestamp into nowdate ;
            select count(*) into ncount from cloudrent_manual_line_member_rel where message_id=wizardid ;
            if ncount > 0 then
               open rel_cur for select * from cloudrent_manual_line_member_rel where message_id=wizardid ;
               loop
                  fetch rel_cur into rel_rec ;
                  exit when not found ;
                  open u_cur for select * from cloudrent_member_line_user where member_id=rel_rec.member_id and send_announcement=TRUE ;
                  loop
                    fetch u_cur into u_rec ;
                    exit when not found ;
                    insert into cloudrent_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,message_text,active,create_uid,create_date) values
                        (senddate,projid,u_rec.line_user_id,u_rec.member_id,FALSE,'1',linemsg,TRUE,2,nowdate) ;
                  end loop ;
                  close u_cur ;
               end loop ;
               close rel_cur ;
            else
               open m_cur for select * from cloudrent_household_member where house_id in (select id from cloudrent_household_house_line where house_id=projid) ;
               loop
                  fetch m_cur into m_rec ;
                  exit when not found ;
                  open u_cur for select * from cloudrent_member_line_user where member_id=m_rec.id and send_announcement=TRUE ;
                  loop
                    fetch u_cur into u_rec ;
                    exit when not found ;
                    insert into cloudrent_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,message_text,active,create_uid,create_date) values
                     (senddate,projid,u_rec.line_user_id,m_rec.id,FALSE,'1',linemsg,TRUE,2,nowdate) ;
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
            update cloudrent_send_line_message set active=FALSE where active=TRUE and send_status=TRUE and send_date <= duedate ;
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
            ncount int ;
            houseid int ;
          BEGIN
            open m_cur for select * from cloudrent_household_member where active=TRUE and start_rental is not null ;
            loop
               fetch m_cur into m_rec ;
               exit when not found ;
               select house_id into houseid from cloudrent_household_house_line where id = m_rec.house_id ;
               select substring(current_timestamp::DATE::TEXT,1,8) into dueym ; /* 2022-04- */
               select lpad(date_part('day',m_rec.start_rental::DATE)::TEXT,2,'0') into dueday ;
               senddate = concat(dueym,dueday)::DATE ;
               update cloudrent_household_member set ar_date=senddate where id = m_rec.id ;
               select senddate - interval '3 day' into senddate ;  /* 帳單日前3天 */
               select count(*) into ncount from cloudrent_send_line_message where send_date=senddate and member_id=m_rec.id and send_message_type='2' ;
               if ncount = 0 then
                  open lu_cur for select * from cloudrent_member_line_user where member_id = m_rec.id and send_acc_bill=TRUE ;
                  loop
                    fetch lu_cur into lu_rec ;
                    exit when not found ;
                    insert into cloudrent_send_line_message(send_date,project_no,line_user_id,member_id,send_status,send_message_type,active) values 
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
            update cloudrent_send_line_message set can_do=True,send_status=False where (send_status=FALSE or send_status is null) and send_date::DATE <= mytoday::DATE ;
          END;$BODY$
          LANGUAGE plpgsql;""")
