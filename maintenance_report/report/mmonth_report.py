# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.osv.orm import except_orm
import datetime, pytz


class mmonth_report(models.AbstractModel):
    _name = "report.maintenance_report.mmonth_report"

    @api.multi
    def render_html(self, docids, data=None):

        mydepartment_id = data.get("department_id", None)
        mystart_date = data.get("start_date", None)
        myend_date = data.get("end_date", None)
        mreport_year = data.get("report_year", None)
        mreport_month = data.get("report_month", None)

        domain = [('request_date', '>=', mystart_date), ('request_date', '<', myend_date),
                  ('repaired_date', '!=', False), ('department_id', '!=', False)]

        if mydepartment_id:
            domain.append(('department_id', '=', mydepartment_id))

        # raise except_orm(u"INFO",u"%s" % (domain))
        report_obj = self.env['report']
        data_array = list()
        main_request_data = self.env['maintenance.request'].search(domain)
        # raise except_orm('KEY', 'KEY')

        mydata = main_request_data.sorted(key=lambda r: (int(r.department_id.name), (r.equipment_id.name)))
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
            # raise except_orm(u"INFO", u"%s" % (main_text))
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
            # raise except_orm(u"INFO", u"%s" % (parts_text))
            if mydepartment_key == main_info.department_id.name:
                mydepartment_value = "-"
            else:
                mydepartment_value = main_info.department_id.name
                mydepartment_key = main_info.department_id.name
            if myequipment_key == main_info.equipment_id.name:
                myequipment_value = "-"
            else:
                myequipment_value = main_info.equipment_id.name
                myequipment_key = main_info.equipment_id.name

            myreqdate = fields.Datetime.from_string(main_info.request_date)
            myreqdate1 = (myreqdate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')

            myrepdate = fields.Datetime.from_string(main_info.repaired_date)
            myrepdate1 = (myrepdate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M')

            data_array.append({"department": mydepartment_value,
                               "equipment": myequipment_value,
                               "request_date": myreqdate1,
                               "repaired_date": myrepdate1,
                               "technician": main_info.technician_user_id.name,
                               "maintenance_content": main_text,
                               "faulttext": fault_text,
                               "parts": parts_text,
                               "brokentime": main_info.broken_time,
                               # "waittime" : main_info.wait_time,
                               "waittime": main_info.keyin_wait_time,
                               "maintenancetime": main_info.maintenance_time,
                               })

        if len(data_array) == 0:
            # print "沒有任何資料可以列印....."
            data_array.append({"department": u'沒有符合的資料可供列印',
                               "equipment": '----------',
                               "request_date": '',
                               "repaired_date": '',
                               "technician": '',
                               "maintenance_content": '',
                               "faulttext": '',
                               "parts": '',
                               "brokentime": '',
                               "waittime": '',
                               "maintenancetime": '',
                               })

        docargs = {"maintenance": data_array,
                   "mreportyear": mreport_year,
                   "mreportmonth": mreport_month,
                   }

        return report_obj.render('maintenance_report.mmonth_report', values=docargs)
