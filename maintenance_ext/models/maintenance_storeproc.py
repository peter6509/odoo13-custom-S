# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,api

class MaintenanceStoreproc(models.Model):
    _name = "maintenance.storeproc"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists gentempchecklist(mainid int,tempname varchar) cascade""")
        self._cr.execute("""create or replace function gentempchecklist(mainid int,tempname varchar) returns void as $BODY$
         DECLARE
           c_cur refcursor ;
           c_rec record ;
           ncount int ;
           maxid int ;
         BEGIN
           select count(*),max(id) into ncount,maxid from maintenance_equipment where name=tempname ;
           if ncount > 0 then
              open c_cur for select * from maintenance_equipment_check_list where equip_id=maxid ;
              loop
                 fetch c_cur into c_rec ;
                 exit when not found ;
                 insert into maintenance_equipment_check_list(equip_id,check_item,check_active,check_value,h_value,l_value) values
                  (mainid,c_rec.check_item,c_rec.check_active,c_rec.check_value,c_rec.h_value,c_rec.l_value) ;
              end loop ;
              close c_cur ;
           end if ;
         END;$BODY$
         LANGUAGE plpgsql;""")

        self._cr.execute("""drop function if exists gentempchecklist1(mainid int,tempname varchar) cascade""")
        self._cr.execute("""create or replace function gentempchecklist1(mainid int,tempname varchar) returns void as $BODY$
             DECLARE
               c_cur refcursor ;
               c_rec record ;
               ncount int ;
               maxid int ;
             BEGIN
               select count(*),max(id) into ncount,maxid from maintenance_equipment where name=tempname ;
               if ncount > 0 then
                  open c_cur for select * from maintenance_equipment_check_list1 where equip_id=maxid ;
                  loop
                     fetch c_cur into c_rec ;
                     exit when not found ;
                     insert into maintenance_equipment_check_list1(equip_id,check_item,check_active) values
                      (mainid,c_rec.check_item,c_rec.check_active) ;
                  end loop ;
                  close c_cur ;
               end if ;
             END;$BODY$
             LANGUAGE plpgsql;""")
