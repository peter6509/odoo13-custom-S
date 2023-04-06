# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api

class cloudrenthouseholdmemberstoreproc(models.Model):
    _name = "cloudrent.jousehold_member_storeproc"

    @api.model
    def init(self):
        self.env.cr.execute("""drop function if exists memberlineuser() cascade""")
        self.env.cr.execute("""create or replace function memberlineuser() returns void as $BODY$
          DECLARE
            ncount int ;
            m_cur refcursor ;
            m_rec record ;
          BEGIN
            open m_cur for select * from cloudrent_household_member where active=True ;
            loop
              fetch m_cur into m_rec ;
              exit when not found ;
              select count(*) into ncount from cloudrent_member_line_user where member_id=m_rec.id ;
              if ncount = 0 then
                 insert into cloudrent_member_line_user(member_id,member_name,line_user_id,member_pid,active,send_announcement,send_acc_bill) values
                  (m_rec.id,m_rec.member_name,m_rec.line_user_id,m_rec.member_pid,TRUE,TRUE,TRUE) ;
              else
                 update cloudrent_member_line_user set member_name=m_rec.member_name where member_id=m_rec.id and member_pid=m_rec.member_pid ; 
              end if ;
            end loop ;
            close m_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")
