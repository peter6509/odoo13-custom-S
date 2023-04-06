# -*- coding: utf-8 -*-
# Author : Peter Wu


from odoo import models, fields, api
from odoo.exceptions import UserError
import psycopg2


class migrationdeptwizard(models.TransientModel):
    _name = "neweb_enhancement.migration_dept_wizard"

    sourceip = fields.Char(string="DEMO IP",default='localhost',required=True)
    dbname = fields.Char(string="DB NAME",default='DEMO',required=True)
    dbuser = fields.Char(string="DB USER",default='odoo',required=True)
    dbpasswd = fields.Char(string="DB PASSWD",default='odoo',required=True)
    passcode = fields.Char(string="PASSCODE",required=True)


    def run_connect_status(self):

        if self.passcode != '!99999ibm':
            raise UserError('錯誤的PASSCODE!')

        conn1_string = "host='127.0.0.1' dbname='DEMO' user='odoo' password='odoo'"


        conn_demo = psycopg2.connect(conn1_string)
        cur_demo = conn_demo.cursor()
        cur_demo.execute("""select count(*) from hr_department""")
        myres = cur_demo.fetchone()[0]
        raise UserError("DEPT Record count:%d" % myres)



    def run_dept_migration(self):

        if self.passcode != '!99999ibm':
            raise UserError('錯誤的PASSCODE!')

        conn1_string = "host='127.0.0.1' dbname='DEMO' user='odoo' password='odoo'"

        conn_demo = psycopg2.connect(conn1_string)
        cur_demo = conn_demo.cursor()
        cur_demo.execute("select max(id) from hr_department")
        mymaxid = cur_demo.fetchone()
        cur_demo.execute("select id,name,active,parent_id from hr_department")
        myrec = cur_demo.fetchall()
        for line in myrec:
            S1 = line[0]
            S2 = line[1]
            if not S2:
                S2 = ' '
            S3 = line[2]
            if not S3:
                S3 = False
            self.env.cr.execute("select count(*) from hr_department where id=%d" % S1)
            myres = self.env.cr.fetchone()
            if myres[0] > 0 :
                self.env.cr.execute("update hr_department set name='%s',active='%s' where id=%d" % (S2,S3,S1))
            else:
                self.env.cr.execute("insert into hr_department(id,name,active) values (%d,'%s','%s')" % (S1,S2,S3))
            self.env.cr.execute("commit")
        for line in myrec:
            S1 = line[0]
            S4 = line[3]
            if S4:
                self.env.cr.execute("update hr_department set parent_id=%d where id=%d" % (S4,S1))
                self.env.cr.execute("commit")

        if not mymaxid[0]:
            self.env.cr.execute("select max(id) from hr_department")
            mymaxid = self.env.cr.fetchone()
        mymaxid1 = int(mymaxid[0]) + 1
        self.env.cr.execute("alter sequence hr_department_id_seq restart with %d" % mymaxid1)
        self.env.cr.execute("commit")

        cur_demo.execute("select id,work_location,department_id,parent_id from hr_employee")
        myrec = cur_demo.fetchall()
        for line in myrec:
            S1 = line[0]
            S2 = line[1]
            S3 = line[2]
            S4 = line[3]


            if S2:
                try:
                    self.env.cr.execute("update hr_employee set work_location='%s' where id=%d " % (S2,S1))
                    self.env.cr.execute("commit")
                except Exception as inst:
                    print("No Update Employee")
            # if S3:
            #     try:
            #         self.env.cr.execute("update hr_employee set work_location='%s' where id=%d " % (S3,S1))
            #         self.env.cr.execute("commit")
            #     except Exception as inst:
            #         print("No Update Employee")
            if S3:
                try:
                    self.env.cr.execute("update hr_employee set department_id=%d where id=%d " % (S3,S1))
                    self.env.cr.execute("commit")
                except Exception as inst:
                    print("No Update Employee")
            if S4:
                try:
                    self.env.cr.execute("update hr_employee set parent_id=%d where id=%d " % (S4,S1))
                    self.env.cr.execute("commit")
                except Exception as inst:
                    print("No Update Employee")

