# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import UserError


class migrationcontractline(models.TransientModel):
    _name = "neweb.contractline_migration"


    project_no = fields.Char(string="專案編號")


    # def contractmaxid(self):
    #     conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
    #     conn_PROD = psycopg2.connect(conn2_string)
    #     cur_PROD = conn_PROD.cursor()
    #     cur_PROD.execute("select max(id) from neweb_contract_contract ")
    #     mymaxid = cur_PROD.fetchone()
    #     mymaxid1 = int(mymaxid[0]) + 1
    #     cur_PROD.execute("alter sequence neweb_contract_contract_id_seq restart with %d" % mymaxid1)
    #     cur_PROD.execute("commit")
    #     cur_PROD.execute("select max(id) from neweb_contract_contract_line ")
    #     mymaxid = cur_PROD.fetchone()
    #     mymaxid1 = int(mymaxid[0]) + 1
    #     cur_PROD.execute("alter sequence neweb_contract_contract_line_id_seq restart with %d" % mymaxid1)
    #     cur_PROD.execute("commit")
    #
    #
    # def proj_contractline_prod(self):
    #     conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
    #     conn_PROD = psycopg2.connect(conn2_string)
    #     cur_PROD = conn_PROD.cursor()
    #     cur_PROD.execute("select contractgetprodname('%s')" % self.project_no)
    #     cur_PROD.execute("commit")
    #
    #
    # def proj_contractline(self):
    #     conn1_string = "host='192.168.1.182' dbname='neweb' user='biznavi' password='erp2Passw0rd!@'"
    #     conn_biznavi = psycopg2.connect(conn1_string)
    #     cur_biznavi = conn_biznavi.cursor()
    #     conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
    #     conn_PROD = psycopg2.connect(conn2_string)
    #     cur_PROD = conn_PROD.cursor()
    #     #conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
    #     #cur_PROD = conn_PROD.cursor()
    #     if self.project_no :
    #        cur_biznavi.execute("select id from neweb_contract_contract where project_no='%s'" % self.project_no)
    #        #print "%s" % rec
    #        mycontractlineid = cur_biznavi.fetchone()
    #        print ("%s" % mycontractlineid[0])
    #        cur_biznavi.execute("select id,contract_id,sequence,machine_serial_no,special_warn,x_locked,prod,special_warn_days from neweb_contract_contract_line where contract_id = %d" % mycontractlineid[0])
    #        myrec1 = cur_biznavi.fetchall()
    #        for line in myrec1:
    #            s1 = line[0]
    #            s2 = line[1]
    #            s3 = line[2]
    #            s4 = line[3]
    #            s5 = line[4]
    #            s6 = line[5]
    #            s7 = line[6]
    #            s8 = line[7]
    #            # print "%s" %
    #            try:
    #                cur_PROD.execute("""insert into neweb_contract_contract_line(id,sequence,machine_serial_no,special_warn,x_locked,prod) values ('%s','%s','%s','%s','%s','%s')""" %
    #                                 (s1, s3, s4, s5, s6, s7))
    #            except Exception as inst:
    #                print ("fail:")
    #            cur_PROD.execute("commit")
    #        cur_biznavi.execute("select id,special_warn_date,maintain_partner,memo,prod_sla,special_warn_days,contract_id from neweb_contract_contract_line where contract_id = %d" %
    #            mycontractlineid[0])
    #        myrec1 = cur_biznavi.fetchall()
    #        for line in myrec1:
    #            s1 = line[0]
    #            s2 = line[1]
    #            s3 = line[2]
    #            s4 = line[3]
    #            s5 = line[4]
    #            s6 = line[5]
    #            s7 = line[6]
    #            # print "update %s %s %s %s %s" % (s1, s2, s3, s4, s5)
    #            if s2:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set special_warn_date='%s' where id='%s'" % (s2, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: special_warn_date")
    #            if s3:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set maintain_partner='%s' where id='%s'" % (s3, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: maintain_partner")
    #            if s4:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set memo='%s' where id='%s'" % (s4, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: memo")
    #            if s5:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set prod_sla='%s' where id='%s'" % (s5, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: prod_sla")
    #            if s6:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set special_warn_days='%s' where id='%s'" % (
    #                            s6, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: special_warn_days")
    #            if s7:
    #                try:
    #                    cur_PROD.execute(
    #                        "update neweb_contract_contract_line set contract_id='%s' where id='%s'" % (s7, s1))
    #                    cur_PROD.execute("commit")
    #                except Exception as inst:
    #                    print ("NO Update: contract_id")

        #mymaxid1 = int(mymaxid[0]) + 1
        #cur_PROD.execute("alter sequence neweb_contract_contract_line_id_seq restart with %d" % mymaxid1)
        #cur_PROD.execute("commit")

    def proj_engassign_resuser(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        conn2_string = "host='192.168.1.195' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        oldcur_PROD = old_PROD.cursor()
        oldcur_PROD.execute("select * from neweb_proj_eng_assign_res_users_rel")
        myrec = oldcur_PROD.fetchall()

        cur_PROD = conn_PROD.cursor()
        for line in myrec:
            s1 = line[0]
            s2 = line[1]
            try:
                cur_PROD.execute("""insert into neweb_proj_eng_assign_res_users_rel(neweb_proj_eng_assign_id,res_users_id) values (%d,%d)""" % (s1,s2))
                cur_PROD.execute("commit")
            except:
                A=1

    def partner_contact_user(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        # conn2_string = "host='192.168.1.195' dbname='PROD' user='odoo' password='odoo'"
        # conn_PROD = psycopg2.connect(conn2_string)
        oldcur_PROD = old_PROD.cursor()
        oldcur_PROD.execute("select id,parent_id,contact_type,name,title,function,email,survey_mark,phone,fax,mobile,comment,birthday_month,birthday_day from res_partner where is_company=False and parent_id is not null")
        myrec = oldcur_PROD.fetchall()
        oldcur_PROD.close()
        # cur_PROD = conn_PROD.cursor()
        nnum = 1
        for line in myrec:
            s1 = line[0] # id
            s2 = line[1] # parent_id
            s3 = line[2] # contact_type
            s4 = line[3] # name
            s5 = line[4] # title
            s6 = line[5] # function
            s7 = line[6] # email
            s8 = line[7] # survey_mark
            s9 = line[8] # phone
            s10 = line[9] # fax
            s11 = line[10] # mobile
            s12 = line[11]  # comment
            s13 = line[12]  # birthday_month
            s14 = line[13]  # birthday_day

            try:
                self.env.cr.execute("""select check_partner_status1(%d,%d,'%s')""" % (s1,s2,s4))
                myres = self.env.cr.fetchone()[0]
                if myres > 0 :
                    self.env.cr.execute("""insert into res_partner(parent_id,contact_type,name,title,function,email,survey_mark,phone,fax,mobile,comment,birthday_month,birthday_day) 
                       values (%d,'%s','%s',%d,'%s','%s','%s','%s','%s','%s','%s',%d,%d)""" % (myres,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14))
                    self.env.cr.execute("""commit""")
                    nnum = nnum + 1
            except:
                A = 1
        print("OK_RUN:%d" % nnum)


    def purchase_reciver(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        # conn2_string = "host='192.168.1.195' dbname='PROD' user='odoo' password='odoo'"
        # conn_PROD = psycopg2.connect(conn2_string)
        oldcur_PROD = old_PROD.cursor()
        oldcur_PROD.execute("select id,purchase_reciver from purchase_order")
        myrec = oldcur_PROD.fetchall()
        oldcur_PROD.close()
        # cur_PROD = conn_PROD.cursor()
        nnum = 1
        for line in myrec:
            s1 = line[0] # id
            s2 = line[1] # purchase_reciver
            # print("ID:%d RECIVER:%s" % (s1,s2))
            try:
                self.env.cr.execute("""select check_purchase_reciver(%d,'%s')""" % (s1,s2))
                self.env.cr.execute("""commit""")

                nnum = nnum + 1
            except:
                A = 1
        print("OK_RUN:%d" % nnum)

    def invoice_open_ret(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        oldcur_PROD = old_PROD.cursor()
        oldcur_PROD.execute("select id,invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,invoicetype,invoice_no,invoice_date,invoice_state,purchase_no from neweb_invoice_invoiceopen_line where invoice_id in (210,207)")
        myrec = oldcur_PROD.fetchall()
        oldcur_PROD.close()
        nnum = 1
        for line in myrec:
            s1 = line[0]   # id
            s2 = line[1]   # invoice_id
            s3 = line[2]   # invoice_costtype
            s4 = line[3]   # invoice_spec
            s5 = line[4]   # invoice_num
            s6 = line[5]   # invoice_unit_price
            s7 = line[6]   # invoice_unit_price1
            s8 = line[7]   # invoice_taxtype
            s9 = line[8]   # invoicetype
            s10 = line[9]  # invoice_no
            s11 = line[10] # invoice_date
            s12 = line[11] # invoice_state
            s13 = line[12] # purchase_no
            self.env.cr.execute("""insert into neweb_invoice_invoiceopen_line(id,invoice_id,invoice_costtype,invoice_spec,invoice_num,invoice_unit_price,invoice_unit_price1,invoice_taxtype,invoicetype,invoice_no,invoice_date,invoice_state,purchase_no)
              values (%d,%d,%d,'%s',%d,'%s','%s',%d,'%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13))
            self.env.cr.execute("""commit""")

    def picking_min_date(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        old_PROD = psycopg2.connect(conn1_string)
        oldcur_PROD = old_PROD.cursor()
        oldcur_PROD.execute("select id,name,min_date from stock_picking where min_date is not null")
        myrec = oldcur_PROD.fetchall()
        nnum = 1
        for line in myrec:
            s1 = line[0]   # id
            s2 = line[1]   # name
            s3 = line[2]   # min_date

            self.env.cr.execute("""update stock_picking set scheduled_date='%s'::DATE where name='%s'""" % (s3,s2))
            self.env.cr.execute("""commit""")
