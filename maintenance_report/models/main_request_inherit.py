# _*_ coding: utf-8 _*_
# Author: Peter Wu

from __future__ import division
from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime



class mainrequestinherit(models.Model):
    _inherit = "maintenance.request"

    faultcauseids = fields.Char(size=20, compute='_get_fault_cause', store=False)
    keyin_wait_time = fields.Integer(string=u"待料時間")
    pending_time = fields.Float(digits=(6,1),default=False,string=u"待復機時間(天)",compute='_get_pending_time',track_visibility='always',store=False)


    @api.depends('request_date','stage_sequence')
    def _get_pending_time(self):
        for rec in self:
            pendingtime = datetime.datetime.utcnow() - fields.Datetime.from_string(rec.request_date)
            pending_day = pendingtime.days
            pending_hours = round(((pendingtime.seconds/3600)/24),2)
            if rec.stage_sequence < 3 :
               rec.update({'pending_time': pending_day + pending_hours})
            else:
               rec.update({'pending_time': False})


    @api.model_cr
    def init(self):
        self._cr.execute("""DROP FUNCTION IF EXISTS change_equipmentid(myequipmentid integer) cascade;""")
        self._cr.execute("""create or replace function change_equipmentid(myequipmentid integer) returns integer as $BODY$
declare
  myequipmentname maintenance_equipment.name%type;
  myid maintenance_equipment.id%type;
  myequip_cur refcursor;
  myequio_rec RECORD;
  myequip_rec RECORD;
BEGIN
  myid := myequipmentid ;
  if myequipmentid > 627 then
    select name into myequipmentname from maintenance_equipment where id=myequipmentid;
    open myequip_cur for select id,name from maintenance_equipment where id <= 627;
    LOOP
      fetch myequip_cur into myequip_rec;
      exit when not found;
      if concat(upper(substr(myequipmentname,1,2)),substr(myequipmentname,3,3))=substr(myequip_rec.name,1,5) then
         myid := myequip_rec.id;
      end if;
    END LOOP;
    close myequip_cur;
  end if;
  return myid;
END;
$BODY$
LANGUAGE plpgsql;""")

        self._cr.execute("""DROP FUNCTION IF EXISTS change_departmentid(mydepartmentid integer) cascade;""")
        self._cr.execute("""create or replace function change_departmentid(mydepartmentid integer) returns integer as $BODY$
declare
  mydepartmentname department.name%type;
  myid department.id%type;
  mydepart_cur refcursor;
  mydepart_rec RECORD;
  mycount integer;
BEGIN
  myid := mydepartmentid ;
  if mydepartmentid > 32 then
    select name into mydepartmentname from department where id=mydepartmentid;
    if length(mydepartmentname) = 5 then
       select count(*) into mycount from maintenance_equipment where substr(name,1,5)=concat(upper(substr(mydepartmentname,1,2)),substr(mydepartmentname,3,3)) and id <= 627;
       if mycount >0 then
          select department_id into myid from maintenance_equipment where substr(name,1,5)=concat(upper(substr(mydepartmentname,1,2)),substr(mydepartmentname,3,3)) and id <= 627;
       end if;
    else
      open mydepart_cur for select id,name from department where id <= 32;
      LOOP
        fetch mydepart_cur into mydepart_rec;
        exit when not found;
        if mydepartmentname=mydepart_rec.name then
          myid := mydepart_rec.id;
        end if;
      END LOOP;
      close mydepart_cur;
    end if;
  end if;
  return myid;
END;
$BODY$
LANGUAGE plpgsql;
""")

    @api.one
    @api.depends('fault_cause_ids')
    def _get_fault_cause(self):
        res = ""
        for rec in self.fault_cause_ids:
            # print "%s" % rec.name
            res = res + "%s ;" % rec.name
        self.faultcauseids = res
        return res

    @api.model
    def create(self, vals):

        if 'keyin_wait_time' in vals and vals['keyin_wait_time']:
            if vals['keyin_wait_time'] < 0:
                raise except_orm(u"數據錯誤", u"待料時間必須大於0")
        if 'department_id' in vals and not vals['department_id']:
            raise except_orm(u"资料不完整", u"必须輸入部門資訊")
        if 'equipment_id' in vals and not vals['equipment_id']:
            raise except_orm(u"资料不完整", u"必须輸入設備名稱")
        if 'fault_type_ids' in vals and not vals['fault_type_ids']:
            raise except_orm(u"资料不完整", u"必须輸入故障類型")
        if 'fault_cause_ids' in vals and not vals['fault_cause_ids']:
            raise except_orm(u"资料不完整", u"必须輸入故障原因")
        res = super(mainrequestinherit, self).create(vals)
        return res

    @api.multi
    def write(self, vals):

        if 'keyin_wait_time' in vals and vals['keyin_wait_time']:
            if vals['keyin_wait_time'] < 0:
                raise except_orm(u"數據錯誤", u"待料時間必須大於0")
        if 'department_id' in vals and not vals['department_id']:
            raise except_orm(u"资料不完整", u"必须輸入部門資訊")
        if 'equipment_id' in vals and not vals['equipment_id']:
            raise except_orm(u"资料不完整", u"必须輸入設備名稱")
        if 'fault_type_ids' in vals and not vals['fault_type_ids']:
            raise except_orm(u"资料不完整", u"必须輸入故障類型")
        if 'fault_cause_ids' in vals and not vals['fault_cause_ids']:
            raise except_orm(u"资料不完整", u"必须輸入故障原因")
        res = super(mainrequestinherit, self).write(vals)
        return res

    def go_backward(self):
        myid = self.env.context.get('own_main_id')
        myrec = self.env['maintenance.request'].search([('id','=',myid)])
        self.env.cr.execute("""select get_stageid(%d,%d)""" % (myrec.stage_id, 1))
        mystageid = self.env.cr.fetchone()
        my_sequence = self.stage_sequence

        if my_sequence == 0 :
           raise UserWarning("目前是 新請求階段,沒有往回階段")
        if my_sequence == 1 :
           myrec.write({'stage_id': mystageid[0],'stage_sequence':0})
        if my_sequence == 2 :
           myrec.write({'stage_id': mystageid[0], 'stage_sequence': 1})
        if my_sequence == 3  :
           myrec.write({'stage_id': mystageid[0], 'stage_sequence': 2})
        if my_sequence == 4  :
           myrec.write({'stage_id': mystageid[0], 'stage_sequence': 3})

    def go_forward(self):
        myid = self.env.context.get('own_main_id')
        myrec = self.env['maintenance.request'].search([('id', '=', myid)])
        self.env.cr.execute("""select get_stageid(%d,%d)""" % (myrec.stage_id,2))
        mystageid = self.env.cr.fetchone()
        my_sequence = self.stage_sequence

        if my_sequence == 0  :
            myrec.write({'stage_id': mystageid[0], 'stage_sequence': 1})
        if my_sequence == 1  :
            myrec.write({'stage_id': mystageid[0], 'stage_sequence': 2})
        if my_sequence == 2  :
            myrec.write({'stage_id': mystageid[0], 'stage_sequence': 3})
        if my_sequence == 3  :
            myrec.write({'stage_id': mystageid[0], 'stage_sequence': 4})
        if my_sequence == 4:
            raise UserWarning("目前是 驗証階段,沒有往後的階段了")


