# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime


class mainhispivotwizard(models.TransientModel):
    _name = "main_his_pivot.wizard"

    department_id = fields.Many2one('department', 'Department', track_visibility='onchange')
    equipment_id = fields.Many2one('maintenance.equipment', 'Equipment')
    start_date = fields.Datetime()
    end_date = fields.Datetime()

    @api.onchange("department_id")
    def onchange_department_id(self):
        res = {}
        if self.department_id:
            res['domain'] = {'equipment_id': [('department_id', '=', self.department_id.id)]}
        return res

    @api.multi
    def main_his_export(self):
        self.env.cr.execute("delete from maintenance_his_pivot")
        # raise except_orm(u'TEST','%s %s %s' % (self.department_id.id,self.equipment_id.id,self.start_date))
        if self.department_id.id == False and self.equipment_id.id == False and self.start_date == False and self.end_date == False:
            raise except_orm(u'條件不符', u'沒有設定過濾資料,請確認....')
        self.ensure_one()

        mydepartment_id = self.department_id.id
        myequipment_id = self.equipment_id.id
        mystart_date = self.start_date
        myend_date = self.end_date

        domain = [('repaired_date', '!=', False), ('department_id', '!=', False)]

        if mydepartment_id:
            domain.append(('department_id', '=', mydepartment_id))
        if myequipment_id:
            domain.append(('equipment_id', '=', myequipment_id))
        if mystart_date:
            domain.append(('request_date', '>=', mystart_date))
        if myend_date:
            domain.append(('request_date', '<=', myend_date))

        main_request_data = self.env['maintenance.request'].search(domain)

        mydata = main_request_data.sorted(
            key=lambda r: ((r.department_id.name), (r.equipment_id.name), (r.request_date)))


        for main_info in mydata:
            main_text = ""
            for rec2 in main_info.maintenance_content_ids:
                # main_text_map = rec2.mapped(lambda r:r.name)
                main_text_map = rec2.name
                if main_text == "":
                    main_text = u'<< %s >>' % (main_text_map)
                else:
                    main_text = u'%s / << %s >>' % (main_text, main_text_map)
            # raise except_orm(u"INFO", u"%s" % (main_text))
            myfaulttext=""
            for rec4 in main_info.fault_cause_ids:
                fault_text= rec4.name
                if myfaulttext=="":
                    mytext = u'<< %s >>' % (fault_text)
                else:
                    mytext = u'%s / << %s >>' % (mytext,fault_text)

            parts_text = ""
            parts_rec = self.env['maintenance.request.part_line'].search([('request_id', '=', main_info.id)])

            for rec3 in parts_rec:
                parts_defaultcode = rec3.part_id.default_code
                parts_name = rec3.part_id.name
                parts_desc = rec3.part_id.description_purchase
                parts_text_map = u'[%s] %s %s' % (parts_defaultcode, parts_name, parts_desc)
                # parts_num_map = str(rec3.quantity).strip()
                # parts_text_map = u"%s (%s)" % (parts_text_map, parts_num_map)
                if parts_text == "":
                    parts_text = u'<< %s >>' % (parts_text_map)
                else:
                    parts_text = u'%s / << %s >>' % (parts_text, parts_text_map)

            mydepartment_value = main_info.department_id.name
            myequipment_value = main_info.equipment_id.name
            myequipmentdesc = main_info.equipment_id.name_desc
            mybrokentime = main_info.broken_time
            myreqdate = fields.Datetime.from_string(main_info.request_date)
            myrepdate = fields.Datetime.from_string(main_info.repaired_date)
            mainhis_rec = self.env['maintenance_his.pivot'].search([])
            mainhis_rec.create({"department_name": mydepartment_value,
                                "equipment_name": myequipment_value,
                                "equipment_desc" : myequipmentdesc,
                                "request_date": myreqdate,
                                "repaired_date": myrepdate,
                                "broken_time" : mybrokentime,
                                "technician": main_info.technician_user_id.name,
                                "maintenance_content": main_text,
                                "parts_name": parts_text,
                                "faulttext" : mytext,

                                })
        return {'view_name': 'Mainhispivot',
                'name': (u'設備維修履歷記錄EXCEL匯出'),
                'views': [[False, 'tree'], [False, 'Form']],
                'res_model': 'maintenance_his.pivot',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'view_mode': 'tree,form',
                'view_type': 'form',
                }
