# -*- coding: utf-8 -*-
# Author: Peter Wu

from odoo import models, fields, api
from odoo.exceptions import UserError
import datetime, pytz


class era_mmonth_report(models.AbstractModel):
    _name = "report.era_household.mmonth_report"

    @api.model
    def _get_report_values(self, docids, data):


        mbill_ym = data.get("bill_ym", None)    # 減 1 month
        mbill_ym1 = data.get("bill_ym1",None)   # 沒減
        mhouse_id = data.get("house_id", None)
        mproject_no = data.get('project_no',None)


        self.env.cr.execute("""select ckcurym('%s')""" % mbill_ym)
        myres = self.env.cr.fetchone()[0]
        domain = [('house_id', '=', mhouse_id),('in_used','=',True)]



        # report_obj = self.env['report']
        data_array = []

        era_month_data = self.env['era.household_house_line'].search(domain)


        mydata = era_month_data.sorted(key=lambda r: r.house_no)
        myprojectno=''
        mybillym=''
        if myres:
            for month_info in mydata:
                startdate=''
                enddate=''
                myemeterfee = 0
                for bill_info in month_info.bill_line:
                    startdate = bill_info.bill_start_date
                    enddate = bill_info.bill_end_date
                    myemeterfee = myemeterfee + int(round(((bill_info.emeter_end_scale - bill_info.emeter_start_scale) * bill_info.emeter_price_unit),0))
                if startdate=='':
                    mystartdate = ' '
                else:
                    mystartdate = (startdate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
                if enddate == '':
                    myenddate = ' '
                else:
                    myenddate = (enddate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
                paymentdate=''
                paymentamount=0
                paymentdesc=''
                mypaymentamount = 0
                if month_info.is_payment:
                    self.env.cr.execute("""select getpaymentamount('%s',%d)""" % (mbill_ym1,month_info.id))
                    paymentamount = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""select getpaymentdate('%s',%d)""" % (mbill_ym1, month_info.id))
                    paymentdate = self.env.cr.fetchone()[0]
                    self.env.cr.execute("""select getpaymentdesc('%s',%d)""" % (mbill_ym1, month_info.id))
                    paymentdesc = self.env.cr.fetchone()[0]

                if month_info.house_rental_fee=='':
                    myhouserentalfee=0
                else:
                    myhouserentalfee = month_info.house_rental_fee
                if month_info.house_management_fee=='':
                    myhousemanagementfee=0
                else:
                    myhousemanagementfee = month_info.house_management_fee
                if month_info.parking_space_rent=='':
                    myparkingspacerent=0
                else:
                    myparkingspacerent = month_info.parking_space_rent
                if month_info.parking_management=='':
                    myparkingmanagement=0
                else:
                    myparkingmanagement = month_info.parking_management
                if month_info.lo_parking_management=='':
                    myloparkingmanagement=0
                else:
                    myloparkingmanagement = month_info.lo_parking_management
                if month_info.uncomplete_fee=='':
                    myuncompletefee=0
                else:
                    myuncompletefee = month_info.uncomplete_fee
                mycurrenttotalfee = (myemeterfee + month_info.house_rental_fee + month_info.house_management_fee + month_info.parking_space_rent + month_info.parking_management + month_info.lo_parking_management + month_info.uncomplete_fee + month_info.water_fee)
                if month_info.is_payment:
                    myispayment = '已繳'
                else:
                    myispayment = ' '
                mybillym = month_info.bill_ym
                mystartrental = month_info.start_rental
                myhouseno = month_info.house_no
                mymembername = month_info.member_id.member_name
                mywaterfee = month_info.member_id.water_fee


                data_array.append({"houseno": myhouseno,
                                   "membername": mymembername,
                                   "startrental": mystartrental,
                                   "startdate": mystartdate,
                                   "enddate": myenddate,
                                   "emeterfee": myemeterfee,
                                   "houserentalfee": myhouserentalfee,
                                   "housemanagementfee": myhousemanagementfee,
                                   "parkingspacerent" : myparkingspacerent,
                                   "parkingmanagement": myparkingmanagement,
                                   "loparkingmanagement" : myloparkingmanagement,
                                   "waterfee":mywaterfee,
                                   "currenttotalfee": mycurrenttotalfee,
                                   "ispayment": myispayment,
                                   "paymentamount": paymentamount,
                                   "paymentdate": paymentdate,
                                   "paymentdesc": paymentdesc,
                                   "uncompletefee":myuncompletefee,
                                   })
        else:
            for month_info in mydata:
                startdate = ''
                enddate = ''
                myemeterfee = 0
                for bill_info in month_info.bill_line_his:
                    if bill_info.bill_ym == mbill_ym:
                        startdate = bill_info.bill_start_date
                        enddate = bill_info.bill_end_date
                        myemeterfee = myemeterfee + int(round(((bill_info.emeter_end_scale - bill_info.emeter_start_scale) * bill_info.emeter_price_unit),0))
                    if startdate == '':
                        mystartdate = ' '
                    else:
                        mystartdate = (startdate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
                    if enddate == '':
                        myenddate = ' '
                    else:
                        myenddate = (enddate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
                paymentdate = ''
                paymentamount = 0
                paymentdesc = ''
                mypaymentamount = 0
                mypaymentdate = ' '
                mypaymentdesc = ' '
                for payment_info in month_info.payment_line:
                    if payment_info.payment_ym == mbill_ym:
                        paymentdate = payment_info.payment_date
                        paymentamount = payment_info.payment_amount
                        paymentdesc = payment_info.payment_desc

                    if paymentdate == '':
                        mypaymentdate = ' '
                    else:
                        mypaymentdate = (paymentdate + datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
                    if paymentamount == 0:
                        mypaymentamount = ' '
                    else:
                        mypaymentamount = paymentamount
                    if paymentdesc == '':
                        mypaymentdesc = ' '
                    else:
                        mypaymentdesc = paymentdesc

                # myemeterfee = month_info.current_emeter_fee
                if month_info.house_rental_fee=='':
                    myhouserentalfee=0
                else:
                    myhouserentalfee = month_info.house_rental_fee
                if month_info.house_management_fee=='':
                    myhousemanagementfee=0
                else:
                    myhousemanagementfee = month_info.house_management_fee
                if month_info.parking_space_rent=='':
                    myparkingspacerent=0
                else:
                    myparkingspacerent = month_info.parking_space_rent
                if month_info.parking_management=='':
                    myparkingmanagement=0
                else:
                    myparkingmanagement = month_info.parking_management
                if month_info.lo_parking_management=='':
                    myloparkingmanagement=0
                else:
                    myloparkingmanagement = month_info.lo_parking_management
                myuncompletefee = 0
                mycurrenttotalfee = (myemeterfee + month_info.house_rental_fee + month_info.house_management_fee + month_info.parking_space_rent + month_info.parking_management + month_info.lo_parking_management + month_info.water_fee)
                if month_info.is_payment:
                    myispayment = '已繳'
                else:
                    myispayment = ' '
                mybillym = month_info.bill_ym
                mystartrental = month_info.start_rental
                myhouseno = month_info.house_no
                mymembername = month_info.member_id.member_name
                mywaterfee = month_info.member_id.water_fee

                data_array.append({"houseno": myhouseno,
                                   "membername": mymembername,
                                   "startrental": mystartrental,
                                   "startdate": mystartdate,
                                   "enddate": myenddate,
                                   "emeterfee": myemeterfee,
                                   "houserentalfee": myhouserentalfee,
                                   "housemanagementfee": myhousemanagementfee,
                                   "parkingspacerent": myparkingspacerent,
                                   "parkingmanagement": myparkingmanagement,
                                   "loparkingmanagement": myloparkingmanagement,
                                   "waterfee":mywaterfee,
                                   "currenttotalfee": mycurrenttotalfee,
                                   "ispayment": myispayment,
                                   "paymentamount": mypaymentamount,
                                   "paymentdate": mypaymentdate,
                                   "paymentdesc": mypaymentdesc,
                                   "uncompletefee": myuncompletefee,
                                   })
        if len(data_array) == 0:
            # print "沒有任何資料可以列印....."
            data_array.append({"houseno": '沒有符合的資料可供列印',
                               "membername": '----------',
                               "startrental": ' ',
                               "startdate": ' ',
                               "enddate": ' ',
                               "emeterfee": ' ',
                               "houserentalfee": ' ',
                               "housemanagementfee": ' ',
                               "parkingspacerent" : ' ',
                               "parkingmanagement": ' ',
                               "loparkingmanagement" : ' ',
                               "waterfee": ' ',
                               "currenttotalfee": ' ',
                               "ispayment": ' ',
                               "paymentamount": ' ',
                               "paymentdate": ' ',
                               "paymentdesc": ' ',
                               "uncompletefee":' ',
                               })

        return {
            # 'doc_model':
            'projectno': mproject_no,
            'billym': mbill_ym1,
            'date': datetime.date.today(),
            'docs': data_array,
        }
        # docs = {"projectno":myprojectno,
        #         "monthdata": data_array,
        #         "billym": mybillym,
        #
        #            }

        # return docs
