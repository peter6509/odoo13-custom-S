# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError
import psycopg2,sys



class NewebReGetPartnerWizard(models.TransientModel):
    _name = "neweb_purchase.reget_partner_wizard"

    partner_id = fields.Many2one('res.partner',string="廠商",domain="[('is_company','=',True)]")

    def run_reget_partner(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        oldcur_PROD = old_PROD.cursor()
        myparnamne = self.partner_id.name
        oldcur_PROD.execute("select id,parent_id,contact_type,name,title,function,email,survey_mark,phone,fax,mobile,comment,birthday_month,birthday_day from res_partner where parent_id in (select id from res_partner where name='%s' and is_company=True)" % myparnamne)
        myrec = oldcur_PROD.fetchall()
        oldcur_PROD.close()
        nnum = 1
        for line in myrec:
            s1 = line[0]  # id
            s2 = line[1]  # parent_id
            s3 = line[2]  # contact_type
            s4 = line[3]  # name
            s5 = line[4]  # title
            s6 = line[5]  # function
            s7 = line[6]  # email
            s8 = line[7]  # survey_mark
            s9 = line[8]  # phone
            s10 = line[9]  # fax
            s11 = line[10]  # mobile
            s12 = line[11]  # comment
            s13 = line[12]  # birthday_month
            s14 = line[13]  # birthday_day



            self.env.cr.execute("""select check_partner_status1(%d,%d,'%s')""" % (s1, s2, s4))
            myres = self.env.cr.fetchone()[0]
            if myres > 0:
                self.env.cr.execute("""insert into res_partner(parent_id,name,function,email,survey_mark,phone,fax,mobile,comment,active) 
                          values (%d,'%s','%s','%s','%s','%s','%s','%s','%s',True)""" % (myres, s4, s6, s7, s8, s9, s10, s11, s12))
                self.env.cr.execute("""commit""")
                self.env.cr.execute("""select max(id) from res_partner""")
                mymaxid = self.env.cr.fetchone()[0]
                if s3 :
                    self.env.cr.execute("""update res_partner set contact_type=%d where id=%d""" % (s3,mymaxid))
                    self.env.cr.execute("""commit""")
                if s5 :
                    self.env.cr.execute("""update res_partner set title=%d where id=%d""" % (s5, mymaxid))
                    self.env.cr.execute("""commit""")
                if s13 and s14 :
                    self.env.cr.execute("""update res_partner set birthday_month=%d,birthday_day=%d where id=%d""" % (s13,s14, mymaxid))
                    self.env.cr.execute("""commit""")
                nnum = nnum + 1

        print("OK_RUN:%d" % nnum)

    def run_get_fax(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        oldcur_PROD = old_PROD.cursor()
        myparnamne = self.partner_id.name
        oldcur_PROD.execute("select id,fax from res_partner where is_company=True and fax is not null")
        myrec = oldcur_PROD.fetchall()
        oldcur_PROD.close()
        nnum = 1
        for line in myrec:
            s1 = line[0]  # id
            s2 = line[1]  # fax
            self.env.cr.execute("""update res_partner set fax='%s' where id=%d and fax is null""" % (s2,s1))
            self.env.cr.execute("""commit""")