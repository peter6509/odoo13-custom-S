# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
from odoo.exceptions import UserError


class newebcontractstoreproc(models.Model):
    _name = "neweb_contract.store_proc"


    @api.model
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS gen_security_category() cascade;""")
        self._cr.execute("""create or replace function gen_security_category() returns void as $BODY$
              DECLARE 
                 cate_cur refcursor ;
                 cate_rec record ;
                 grp_cur refcursor ;
                 grp_rec record ;
                 num int ;
                 myseq int ;
              BEGIN
                 delete from neweb_enhancement_security_category ;
                 delete from neweb_enhancement_security_group ;
                 num := 1 ;
                 open cate_cur for select A.id as Aid,A.name as Aname,B.category_id,B.id as Bid,B.name as Bname from ir_module_category A left join res_groups B on A.id = B.category_id where A.id in (75,76,77,78,79,80,82,83) order by A.id,B.id ;
                 loop
                   fetch cate_cur into cate_rec ;
                   exit when not found ;
                   insert into neweb_enhancement_security_category(category_name,category_id,group_id,group_name,seq) values (cate_rec.aname,cate_rec.category_id,cate_rec.Bid,cate_rec.Bname,num) ;
                   num = num +  1 ;
                 end loop ;
                 close cate_cur ;
                 open grp_cur for select A.login,A.id as Aid,A.active,A.partner_id,B.id as Bid,B.name as Bname,C.id as Cid,C.name as Cname,C.category_id,E.name as Ename,D.gid as group_id from res_users A left join res_groups_users_rel D on D.uid=A.id left join res_groups C on C.id = D.gid left join ir_module_category B on B.id = C.category_id  left join res_partner E on A.partner_id = E.id 
where A.active=True and B.id in (75,76,77,78,79,80,82,83) order by A.id,C.id ;
                 loop
                   fetch grp_cur into grp_rec ;
                   exit when not found ;
                   select seq into myseq from neweb_enhancement_security_category where group_id = grp_rec.group_id ;
                   insert into neweb_enhancement_security_group (login,group_id,user_id,partner_id,category_name,group_name,emp_name,seq) values (grp_rec.login,grp_rec.Cid,grp_rec.Aid,grp_rec.partner_id,grp_rec.Bname,grp_rec.Cname,grp_rec.Ename,myseq) ;
                 end loop ;
                 close grp_cur ;
                 delete from  neweb_enhancement_security_group where login = 'admin' ;
              END;$BODY$
              LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists genemppostype() cascade""")
        self._cr.execute("""create or replace function genemppostype() returns void as $BODY$
          DECLARE
            emp_cur refcursor ;
            emp_rec record ;
            ncount int ;
            ntime int ;
            jobid int ;
            parentid int ;
            parentid1 int ;
            postype char ;
            flowman5 int ;
          BEGIN
            select id into flowman5 from hr_employee where user_id=448 ;
            update hr_employee_postype set flow_man1=null,flow_man2=null,flow_man3=null,flow_man4=null,flow_man5=null ;
            open emp_cur for select id,parent_id,active from hr_employee where active=True ;
            loop
              fetch emp_cur into emp_rec ;
              exit when not found ;
              ntime = 1 ;
              select count(*) into ncount from hr_employee_postype where emp_id = emp_rec.id ;
              if ncount = 0 then
                 insert into hr_employee_postype (emp_id,flow_man5) values (emp_rec.id,flowman5) ;
              end if ;
              jobid = 0 ;
              if emp_rec.parent_id is not null then
                  /* 第ㄧ層 */
                  postype=' ' ;
                  parentid = 0 ;
                  jobid = 0 ;
                  parentid1 = emp_rec.parent_id ;
                  select coalesce(job_id,0),coalesce(parent_id,0) into jobid,parentid from hr_employee where id = parentid1 ;
                  select coalesce(pos_type,' ') into postype from hr_job where id = jobid ;
                  if postype='2' then
                     update hr_employee_postype set flow_man1=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                  elsif postype='3' then
                     update hr_employee_postype set flow_man2=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                  elsif postype='4' then
                     update hr_employee_postype set flow_man3=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                  elsif postype='5' then
                     update hr_employee_postype set flow_man4=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                  end if ; 
                  /* 第二層 */
                  if parentid > 0 then
                     parentid1 = parentid ;
                     postype=' ' ;
                     parentid = 0 ;
                     jobid = 0 ;
                     select coalesce(job_id,0),coalesce(parent_id,0) into jobid,parentid from hr_employee where id = parentid1 ;
                      select coalesce(pos_type,' ') into postype from hr_job where id = jobid ;
                      if postype='2' then
                         update hr_employee_postype set flow_man1=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                      elsif postype='3' then
                         update hr_employee_postype set flow_man2=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                      elsif postype='4' then
                         update hr_employee_postype set flow_man3=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                      elsif postype='5' then
                         update hr_employee_postype set flow_man4=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                      end if ; 
                      /* 第三層 */
                      if parentid > 0 then
                         parentid1 = parentid ;
                         parentid = 0 ;
                         postype=' ' ;
                         jobid = 0 ;
                         select coalesce(job_id,0),coalesce(parent_id,0) into jobid,parentid from hr_employee where id = parentid1 ;
                          select coalesce(pos_type,' ') into postype from hr_job where id = jobid ;
                          if postype='2' then
                             update hr_employee_postype set flow_man1=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                          elsif postype='3' then
                             update hr_employee_postype set flow_man2=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                          elsif postype='4' then
                             update hr_employee_postype set flow_man3=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                          elsif postype='5' then
                             update hr_employee_postype set flow_man4=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                          end if ; 
                          /* 第四層 */
                          if parentid > 0 then
                             parentid1 = parentid ;
                             postype=' ' ;
                             jobid = 0 ;
                             select coalesce(job_id,0),coalesce(parent_id,0) into jobid,parentid from hr_employee where id = parentid1 ;
                              select coalesce(pos_type,' ') into postype from hr_job where id = jobid ;
                              if postype='2' then
                                 update hr_employee_postype set flow_man1=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                              elsif postype='3' then
                                 update hr_employee_postype set flow_man2=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                              elsif postype='4' then
                                 update hr_employee_postype set flow_man3=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                              elsif postype='5' then
                                 update hr_employee_postype set flow_man4=parentid1,flow_man5=flowman5 where emp_id=emp_rec.id ;
                              end if ;  
                          end if ;
                      end if ;
                  end if ;
              end if ;    
            end loop ;
            close emp_cur ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists cktaxdisplay() cascade""")
        self._cr.execute("""create or replace function cktaxdisplay() returns void as $BODY$
         DECLARE
          user_cur refcursor ;
          user_rec record ;
          ncount int ;
         BEGIN
          open user_cur for select id from res_users where id >= 259 ;
          loop
            fetch user_cur into user_rec ;
            exit when not found ;
            delete from res_groups_users_rel where uid=user_rec.id ;
            insert into res_groups_users_rel(gid,uid) values (1,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (5,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (6,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (7,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (10,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (14,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (15,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (20,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (33,user_rec.id) ;
            insert into res_groups_users_rel(gid,uid) values (34,user_rec.id) ;
          end loop ;
          close user_cur ;
         END;$BODY$
         LANGUAGE plpgsql;""")