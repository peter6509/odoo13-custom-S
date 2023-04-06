# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime, pytz


class cloudrent_maintenance_report(models.AbstractModel):
    _name = "report.cloudrent_household.maintenance_report"

    @api.model
    def _get_report_values(self, docids, data):


        startdate = data.get("startdate", None)
        enddate = data.get("enddate", None)



        domain = [('main_require_date', '>=', startdate), ('main_require_date', '<=', enddate)]

        # report_obj = self.env['report']
        data_array = []
        cloudrent_maintenance_data = self.env['cloudrent.household_maintenance'].search(domain)

        mydata = cloudrent_maintenance_data.sorted(key=lambda r: (r.main_require_date,r.main_house_id))

        mybillym=''
        for main_info in mydata:
            mymainhouseno = main_info.main_house_id.house_no
            mymainreqdate = main_info.main_require_date
            mymainmemo = main_info.main_memo

            if main_info.state == '1':
                mystate = '報修發起'
            elif main_info.state=='2':
                mystate = '處理中'
            elif main_info.state=='3':
                mystate = '處理完成'
            if main_info.main_rating=='1':
                mymainrating = '一般'
            elif main_info.main_rating=='2':
                mymainrating='中等'
            elif main_info.main_rating=='3':
                mymainrating='緊急'
            myrepairmemo = main_info.repair_memo
            myrepairdate = main_info.repair_date
            mycompletememo = main_info.complete_memo
            mycompletedate = main_info.complete_date


            data_array.append({"houseno": mymainhouseno,
                               "requiredate": mymainreqdate,
                               "mainmemo": mymainmemo,
                               "mainrating": mymainrating,
                               "state": mystate,
                               "repairmemo": myrepairmemo,
                               "repairdate": myrepairdate,
                               "completememo": mycompletememo,
                               "completedate" : mycompletedate,
                               })

        if len(data_array) == 0:
            # print "沒有任何資料可以列印....."
            data_array.append({"houseno": '沒有符合的資料可供列印',
                               "requiredate": ' ',
                               "mainmemo": ' ',
                               "mainrating": ' ',
                               "state": ' ',
                               "repairmemo": ' ',
                               "repairdate": ' ',
                               "completememo": ' ',
                               "completedate": ' ',

                               })

        return {
            # 'doc_model':

            'startdate': startdate,
            'enddate':enddate,
            'date': datetime.date.today(),
            'docs': data_array,
        }
