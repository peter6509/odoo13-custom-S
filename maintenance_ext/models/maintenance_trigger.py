# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models, api


class MaintenanceExtTrigger(models.Model):
    _name = "maintenance_ext.trigger"

    @api.model
    def init(self):
        self._cr.execute("""drop function if exists insert_main_req_chklist() cascade""")
        self._cr.execute("""create  or replace function insert_main_req_chklist() returns trigger as $BODY$
          DECLARE
            l1_cur refcursor ;
            l1_rec record ;
            l2_cur refcursor ;
            l2_rec record ;
            nseq int ;
            ncount int ;
          BEGIN
           nseq = 1 ;
            open l1_cur for select * from maintenance_equipment_check_list where check_active=True and equip_id=NEW.equipment_id ;
            loop
              fetch l1_cur into l1_rec ;
              exit when not found ;
              insert into maintenance_request_check_list(request_id,check_seq,check_item,check_value) values
               (NEW.id,nseq,l1_rec.check_item,l1_rec.check_value) ;
            end loop ;
            nseq = nseq + 1 ;
            close l1_cur ;
            nseq = 1 ;
            open l2_cur for select * from maintenance_equipment_check_list1 where check_active=True and equip_id=NEW.equipment_id ;
            loop
              fetch l2_cur into l2_rec ;
              exit when not found ;
              insert into maintenance_request_check_list1(request_id,check_seq,check_item) values (NEW.id,nseq,l2_rec.check_item) ;
              nseq = nseq + 1 ;
            end loop ;
            close l2_cur ;
            return NEW ;
          END;$BODY$
          LANGUAGE plpgsql;""")

        # 針對每次新增 maintenance_request  作動一次 trigger
        self._cr.execute("""drop trigger if exists insert_main_req_chklist on maintenance_request ;""")
        self._cr.execute("""create trigger insert_main_req_chklist after insert on maintenance_request
                                 for each row execute procedure insert_main_req_chklist();""")

