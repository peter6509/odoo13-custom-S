# -*- coding: utf-8 -*-
# Author: Peter Wu


from odoo import models, fields, api
from odoo.osv.orm import except_orm


class mproduct_report(models.AbstractModel):
    _name = "report.maintenance_report.mproduct_report"

    @api.multi
    def render_html(self, docids, data=None):
        mydefaultcode = data.get("defaultcode", None)
        myprodname = data.get("prodname", None)
        myqtystatus = data.get("qtystatus", None)
        myqtyvalue = data.get("qtyvalue", None)

        mysql = "select * from dana_prod where  "
        if mydefaultcode:
            mysql += "default_code like \'%%%s%%\' " % mydefaultcode
        else:
            mysql += "TRUE "
        if myprodname:
            mysql += "and name like \'%%%s%%\' " % myprodname
        else:
            mysql += "and TRUE "
        if myqtyvalue == False:
            myqtyvalue = 0
        if myqtystatus == '1':  # 小於
            mysql += "and qty <= %d ;" % myqtyvalue
        elif myqtystatus == '2':
            mysql += "and qty is null or qty = 0 ;"
        else:
            mysql += "and qty >= %d ;" % myqtyvalue

        # print u"%s" % mysql
        self.env.cr.execute("%s" % mysql)
        domain_rec = self.env.cr.fetchall()
        report_obj = self.env['report']
        data_array = list()
        # raise except_orm('KEY', 'KEY')
        if len(domain_rec) == 0:
            print u"沒有任何資料可供列印...."
        else:
            rec_num = 0
            for i_rec in domain_rec:
                mylocid = domain_rec[rec_num][5]
                myloc = self.env['stock.location'].search([('id', '=', mylocid)])
                data_array.append({"default_code": domain_rec[rec_num][1],
                                   "name": domain_rec[rec_num][2],
                                   "description_purchase": domain_rec[rec_num][3],
                                   "location": myloc.name,
                                   "qty": domain_rec[rec_num][4],
                                   })
                rec_num += 1

        if len(data_array) == 0:
            # print "沒有任何資料可以列印....."
            data_array.append({"default_code": u'沒有符合的資料可供列印',
                               "name": '----------',
                               "description_purchase": '----------',
                               "location": '----------',
                               "qty": '----------',
                               })

        docargs = {"mproduction": data_array,
                   }
        return report_obj.render('maintenance_report.mproduct_report', values=docargs)
