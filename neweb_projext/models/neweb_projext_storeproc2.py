# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, fields, api


class newebprojextstoreproc2(models.Model):
    _name = "neweb_projext.storeproc2"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists genengmaillist(assignid int) cascade""")
        self._cr.execute("""create or replace function genengmaillist(assignid int) returns setof INT as $$
        declare
          myres int ;
          m_cur refcursor ;
          m_rec record ;
          resourceid int ;
        begin
          open m_cur for select res_users_id from neweb_proj_eng_assign_res_users_rel where neweb_proj_eng_assign_id = assignid ;
          loop
            fetch m_cur into m_rec ;
            exit when not found ;
            select id into resourceid from resource_resource where user_id = m_rec.res_users_id ;
            select id into myres from hr_employee where resource_id = resourceid ;
            return next myres ;
            select parent_id into myres from hr_employee where id = myres ;
            return next myres ;
          end loop ;
          close m_cur ;
          open m_cur for select emp_no from neweb_support_maillist ;
          loop
            fetch m_cur into m_rec ;
            exit when not found ;
            return next m_rec.emp_no ;
          end loop;
          close m_cur ;
        end;$$
        language plpgsql;""")
