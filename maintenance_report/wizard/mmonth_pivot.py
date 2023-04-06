# _*_ coding: utf-8 _*_
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime, json


class mmonthpivot(models.TransientModel):
    _name = "mmonth.pivot"  # 月統計報表

    department_id = fields.Many2one('department', 'Department')
    report_year = fields.Char(size=4, default=str(datetime.datetime.today().year))
    report_month = fields.Selection([('1', u'一月'), ('2', u'二月'), ('3', u'三月'), ('4', u'四月'), ('5', u'五月'),
                                     ('6', u'六月'), ('7', u'七月'), ('8', u'八月'), ('9', u'九月'), ('10', u'十月'),
                                     ('11', u'十一月'), ('12', u'十二月')], default=str(datetime.datetime.today().month))

    @api.multi
    def main_month_pivot(self):
        if int(self.report_year) <= 1900:
            raise except_orm(u"條件不符", u"年度條件必須大於1900年")
        if self.report_year == False:
            raise except_orm(u"條件不符", u"年度條件不可空白")
        if self.report_month == False:
            raise except_orm(u"條件不符", u"月份條件不可空白")
        if self.report_month == '12':
            mystart_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month), 1))
            myend_date = fields.Datetime.to_string(datetime.datetime(int(self.report_year) + 1, 1, 1))
        else:
            mystart_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month), 1))
            myend_date = fields.Datetime.to_string(
                datetime.datetime(int(self.report_year), int(self.report_month) + 1, 1))

        self.env.cr.execute("delete from maintenance_month_pivot")

        domain = [('request_date', '>=', mystart_date), ('request_date', '<', myend_date),
                  ('repaired_date', '!=', False), ('department_id', '!=', False)]

        if self.department_id:
            domain.append(('department_id', '=', self.department_id.id))

        main_mmonth_data = self.env['maintenance.request'].search(domain)
        mydata = main_mmonth_data.sorted(key=lambda r: ((r.department_id.name), (r.equipment_id.name)))

        mydepartment_key = ""
        mydepartment_value = ""
        myequipment_key = ""
        myequipment_value = ""


        for main_info in mydata:
            fault_text = ""
            for rec1 in main_info.fault_cause_ids:
                # fault_text_map = rec1.mapped(lambda r: r.name)
                fault_text_map = rec1.name
                if fault_text == "":
                    fault_text = u'<< %s >>' % (fault_text_map)
                else:
                    fault_text = u'%s / << %s >>' % (fault_text, fault_text_map)
                    # raise except_orm(u"INFO",u"%s" % (fault_text))
            main_text = ""
            for rec2 in main_info.maintenance_content_ids:
                # main_text_map = rec2.mapped(lambda r:r.name)
                main_text_map = rec2.name
                if main_text == "":
                    main_text = u'<< %s >>' % (main_text_map)
                else:
                    main_text = u'%s / << %s >>' % (main_text, main_text_map)

            parts_text = ""
            parts_rec = self.env['maintenance.request.part_line'].search([('request_id', '=', main_info.id)])

            for rec3 in parts_rec:
                parts_defaultcode = rec3.part_id.default_code
                parts_name = rec3.part_id.name
                parts_desc = rec3.part_id.description_purchase
                parts_text_map = u'[%s] %s %s' % (parts_defaultcode, parts_name, parts_desc)

                if parts_text == "":
                    parts_text = u'<< %s >>' % (parts_text_map)
                else:
                    parts_text = u'%s / << %s >>' % (parts_text, parts_text_map)

            myname_value = main_info.name
            mydepartment_value = main_info.department_id.name
            myequipment_value = main_info.equipment_id.name
            myequipmentdesc = main_info.equipment_id.name_desc
            myreqdate = fields.Datetime.from_string(main_info.request_date)
            # myreqdate1 = (myreqdate + datetime.timedelta(hours=0)).strftime('%Y-%m-%d %H:%M')
            myrepdate = fields.Datetime.from_string(main_info.repaired_date)
            # myrepdate1 = (myrepdate + datetime.timedelta(hours=0)).strftime('%Y-%m-%d %H:%M')
            myprocdate = fields.Datetime.from_string(main_info.process_date)
            # myprocdate1 = (myprocdate + datetime.timedelta(hours=0)).strftime('%Y-%m-%d %H:%M')
            month_pivot_rec = self.env['maintenance_month.pivot'].search([])
            month_pivot_rec.create({
                                    "department_name": mydepartment_value,
                                    "equipment_name": myequipment_value,
                                    "equipment_desc": myequipmentdesc,
                                    "maintenance_type" : main_info.maintenance_type,
                                    "brokentime": main_info.broken_time,
                                    "waittime": main_info.keyin_wait_time,
                                    "maintenancetime": main_info.maintenance_time,
                                    "request_date": myreqdate,
                                    "repaired_date": myrepdate,
                                    "process_date": myprocdate,
                                    "technician": main_info.technician_user_id.name,
                                    "maintenance_content": main_text,
                                    "faulttext": fault_text,
                                    "parts_name": parts_text,
                                    "name": main_info.name,
                                    })


        return {'view_name': 'Mainmonthpivot',
                'name': (u'設備維修月統計資料分析'),
                'views': [[False, 'tree'], [False, 'form']],
                'res_model': 'maintenance_month.pivot',
                'context': self._context,
                'type': 'ir.actions.act_window',
                'target': 'self',
                'view_mode': 'tree,form',
                'view_type': 'form',
                }
