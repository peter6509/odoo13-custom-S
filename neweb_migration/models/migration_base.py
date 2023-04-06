# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import UserError


class NEWEB_Migration(models.TransientModel):
    _name = "neweb.base_migration"

    SOURCE_IP = fields.Char(string="SOURCE SERVER IP",default='192.168.1.182')
    DB_NAME = fields.Char(string="INSTANCE NAME",default='neweb')
    USER_NAME = fields.Char(string="USER NAME",default='neweb')
    PASSWORD = fields.Char(string="PASSWD",default='erp2Passw0rd!@')
    RUN_CODE = fields.Char(string='RUN CODE')










    def repair_migration(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
            self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB 正式環境導入 neweb_base_problem")
        print ("")

        cur_neweb.execute("select max(id) from neweb_base_problem")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,description,maintenance_category_id,name from neweb_base_problem")
        cur_PROD.execute("delete from neweb_repair_repair_care_call_log")
        cur_PROD.execute("delete from neweb_repair_repair_work_log")
        cur_PROD.execute("delete from neweb_repair_repair_questionnaire")
        cur_PROD.execute("delete from neweb_base_problem_solution")
        cur_PROD.execute("delete from neweb_base_problem")
        cur_PROD.execute("commit")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]

            print (s1,s2,s3,s4)
            cur_PROD.execute("""insert into neweb_base_problem(id,description,maintenance_category_id,name) VALUES
              ('%s','%s','%s','%s')""" % (s1,s2,s3,s4))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_base_problem_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,problem_category,memo,disabled,err_log,write_date,write_uid,create_date,create_uid from neweb_base_problem")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            s8=line[7]
            s9=line[8]
            print ("neweb_base_problem update: %s %s %s %s %s" % (s1,s2,s3,s4,s5))
            if s2:
               cur_PROD.execute("update neweb_base_problem set problem_category='%s' where id='%s'" % (s2,s1))
               cur_PROD.execute("commit")
            if s3:
               cur_PROD.execute("update neweb_base_problem set memo='%s' where id='%s'" % (s3, s1))
               cur_PROD.execute("commit")
            if s4:
               cur_PROD.execute("update neweb_base_problem set disabled='%s' where id='%s'" % (s4, s1))
               cur_PROD.execute("commit")
            if s5:
               cur_PROD.execute("update neweb_base_problem set err_log='%s' where id='%s'" % (s5, s1))
               cur_PROD.execute("commit")
            if s6:
               cur_PROD.execute("update neweb_base_problem set write_date='%s' where id='%s'" % (s6, s1))
               cur_PROD.execute("commit")
            if s7:
               cur_PROD.execute("update neweb_base_problem set write_uid='%s' where id='%s'" % (s7, s1))
               cur_PROD.execute("commit")
            if s8:
               cur_PROD.execute("update neweb_base_problem set create_date='%s' where id='%s'" % (s8, s1))
               cur_PROD.execute("commit")
            if s9:
               cur_PROD.execute("update neweb_base_problem set create_uid='%s' where id='%s'" % (s9, s1))
               cur_PROD.execute("commit")

        print ("neweb_base_problem complete")
        print ("")
        print ("NEWEB 正式環境導入 neweb_base_problem_solution")
        print ("")
        cur_neweb.execute("select max(id) from neweb_base_problem_solution")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,name,problem_id from neweb_base_problem_solution")
        # cur_PROD.execute("delete from neweb_base_problem_solution")
        # cur_PROD.execute("commit")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]

            print (s1,s2,s3)
            cur_PROD.execute("""insert into neweb_base_problem_solution(id,name,problem_id) VALUES
                 ('%s','%s','%s')""" % (s1,s2,s3))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_base_problem_solution_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,memo,disabled,write_date,write_uid,create_date,create_uid from neweb_base_problem_solution")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            print ("neweb_base_problem_solution update: %s %s %s" % (s1,s2,s3))
            if s2:
                cur_PROD.execute("update neweb_base_problem_solution set memo='%s' where id='%s'" % (s2,s1))
                cur_PROD.execute("commit")
            if s3:
                cur_PROD.execute("update neweb_base_problem_solution set disabled='%s' where id='%s'" % (s3, s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update neweb_base_problem_solution set write_date='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update neweb_base_problem_solution set write_uid='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update neweb_base_problem_solution set create_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_base_problem_solution set create_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")

        print ("Neweb_base_problem_solution complete")
        print ("")



        print ("NEWEB 正式環境導入 neweb_repair_repair")
        print ('')

        cur_neweb.execute("select max(id) from neweb_repair_repair")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,contact_user,customer_id,name,repair_datetime from neweb_repair_repair")
        myrec1=cur_neweb.fetchall()
        cur_PROD.execute("delete from neweb_repair_repair")
        cur_PROD.execute("commit")
        i=0
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]

            print (s1,s2,s3,s4,s5)
            try:
                cur_PROD.execute("""insert into neweb_repair_repair(id,contact_user,customer_id,name,repair_datetime) VALUES
                                ('%s','%s','%s','%s','%s')""" % (s1, s2, s3, s4, s5))
                cur_PROD.execute("commit")
            except Exception as inst:
                i += 1
                print ("Neweb_repair_repair No Insert : %d" % i)

        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_repair_repair_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        sql_string="""select id,ae_is_sla_delay,repair_type,ae_id,create_user,contract_id,state,ae_complete_datetime,
        customer_id,ae_response_datetime,part_ready,memo,contact_tel,num_of_repair_lines,ae_on_site_datetime,name,
        device_location,ae_total_ma_time,problem,write_date,write_uid,create_date,create_uid from neweb_repair_repair"""
        cur_neweb.execute(sql_string)
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            s8=line[7]
            s9=line[8]
            s10=line[9]
            s11=line[10]
            s12=line[11]
            s13=line[12]
            s14=line[13]
            s15=line[14]
            s16=line[15]
            s17=line[16]
            s18=line[17]
            s19=line[18]
            s20=line[19]
            s21=line[20]
            s22=line[21]
            s23=line[22]
            print ("repair update: %s %s %s %s" % (s2,s3,s4,s5))
            if s2:
               cur_PROD.execute("update neweb_repair_repair set ae_is_sla_delay='%s' where id='%s'" %(s2,s1))
               cur_PROD.execute("commit")
            if s3:
               cur_PROD.execute("update neweb_repair_repair set repair_type='%s' where id='%s'" % (s3,s1))
               cur_PROD.execute("commit")
            if s4:
               cur_PROD.execute("update neweb_repair_repair set ae_id='%s' where id='%s'" % (s4,s1))
               cur_PROD.execute("commit")
            if s5:
               cur_PROD.execute("update neweb_repair_repair set create_user='%s' where id='%d'" % (s5,s1))
               cur_PROD.execute("commit")
            if s6:
               cur_PROD.execute("update neweb_repair_repair set contract_id='%s' where id='%s'" % (s6,s1))
               cur_PROD.execute("commit")
            if s7:
               cur_PROD.execute("update neweb_repair_repair set state='%s' where id='%s'" % (s7,s1))
               cur_PROD.execute("commit")
            if s8:
               cur_PROD.execute("update neweb_repair_repair set ae_complete_datetime='%s' where id='%s'" % (s8,s1))
               cur_PROD.execute("commit")
            if s9:
               cur_PROD.execute("update neweb_repair_repair set customer_id='%s' where id='%s'" % (s9,s1))
               cur_PROD.execute("commit")
            if s10:
               cur_PROD.execute("update neweb_repair_repair set ae_response_datetime='%s' where id='%s'" % (s10,s1))
               cur_PROD.execute("commit")
            if s11:
               cur_PROD.execute("update neweb_repair_repair set part_ready='%s' where id='%s'" % (s11,s1))
               cur_PROD.execute("commit")
            if s12:
               cur_PROD.execute("update neweb_repair_repair set memo='%s' where id='%s'" % (s12,s1))
               cur_PROD.execute("commit")
            if s13:
               cur_PROD.execute("update neweb_repair_repair set contact_tel='%s' where id='%s'" % (s13,s1))
               cur_PROD.execute("commit")
            if s14:
               cur_PROD.execute("update neweb_repair_repair set num_of_repair_lines='%s' where id='%s'" % (s14,s1))
               cur_PROD.execute("commit")
            if s15:
               cur_PROD.execute("update neweb_repair_repair set ae_on_site_datetime='%s' where id='%s'" % (s15,s1))
               cur_PROD.execute("commit")
            if s16:
               cur_PROD.execute("update neweb_repair_repair set name='%s' where id='%s'" % (s16,s1))
               cur_PROD.execute("commit")
            if s17:
               cur_PROD.execute("update neweb_repair_repair set device_location='%s' where id='%s'" % (s17,s1))
               cur_PROD.execute("commit")
            if s18:
               cur_PROD.execute("update neweb_repair_repair set ae_total_ma_time='%s' where id='%s'" % (s18,s1))
               cur_PROD.execute("commit")
            if s19:
               cur_PROD.execute("update neweb_repair_repair set problem='%s' where id='%s'" % (s19,s1))
               cur_PROD.execute("commit")
            if s20:
               cur_PROD.execute("update neweb_repair_repair set write_date='%s' where id='%s'" % (s20,s1))
               cur_PROD.execute("commit")
            if s21:
               cur_PROD.execute("update neweb_repair_repair set write_uid='%s' where id='%s'" % (s21, s1))
               cur_PROD.execute("commit")
            if s22:
               cur_PROD.execute("update neweb_repair_repair set create_date='%s' where id='%s'" % (s22, s1))
               cur_PROD.execute("commit")
            if s23:
               cur_PROD.execute("update neweb_repair_repair set create_uid='%s' where id='%s'" % (s23, s1))
               cur_PROD.execute("commit")

        print ("NEWEB_REPAIR_REPAIR Completed")

        print ("NEWEB 正式環境導入  neweb_repair_repair_care_call_log")
        print ("")

        cur_neweb.execute("select max(id) from neweb_repair_repair_care_call_log")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id from neweb_repair_repair_care_call_log")
        # cur_PROD.execute("delete from neweb_repair_repair_care_call_log")
        # cur_PROD.execute("commit")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]

            print (s1)
            cur_PROD.execute("insert into neweb_repair_repair_care_call_log(id) values ('%s')" % (s1))
            cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence neweb_repair_repair_care_call_log_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute(
            "select id,repair_id,care_call_log,state,care_call_date,write_date,write_uid,create_date,create_uid from neweb_repair_repair_care_call_log")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            print (s1, s2, s3, s4, s5)
            if s2:
                try:
                    cur_PROD.execute(
                        "update neweb_repair_repair_care_call_log set repair_id='%s' where id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("neweb_repair_repair_care_call_log no update")
            if s3:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set care_call_log='%s' where id='%s'" % (s3, s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update neweb_repair_repair_care_call_log set state='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set care_call_date='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set write_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set write_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
            if s8:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set create_date='%s' where id='%s'" % (s8, s1))
                cur_PROD.execute("commit")
            if s9:
                cur_PROD.execute(
                    "update neweb_repair_repair_care_call_log set create_uid='%s' where id='%s'" % (s9, s1))
                cur_PROD.execute("commit")

        print ("neweb_repair_repair_care_call_log complete")
        print ("")


        print ("NEWEB 導入正式環境 neweb_repair_repair_work_log")
        print ("")
        cur_neweb.execute("select max(id) from neweb_repair_repair_work_log")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id from neweb_repair_repair_work_log")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]

            print (s1)
            cur_PROD.execute("insert into neweb_repair_repair_work_log(id) values ('%s')" % (s1))
            cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence neweb_repair_repair_work_log_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,repair_id,work_log,work_date,state,write_date,write_uid,create_date,create_uid from neweb_repair_repair_work_log")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            print (s1, s2, s3, s4, s5)
            if s2:
                try:
                    cur_PROD.execute("update neweb_repair_repair_work_log set repair_id='%s' where id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("repair_id no update")
            if s3:
                try:
                    cur_PROD.execute("update neweb_repair_repair_work_log set work_log='%s' where id='%s'" % (s3, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("work_log no update")
            if s4:
                cur_PROD.execute("update neweb_repair_repair_work_log set work_date='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update neweb_repair_repair_work_log set state='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update neweb_repair_repair_work_log set write_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_repair_repair_work_log set write_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
            if s8:
                cur_PROD.execute("update neweb_repair_repair_work_log set create_date='%s' where id='%s'" % (s8, s1))
                cur_PROD.execute("commit")
            if s9:
                cur_PROD.execute("update neweb_repair_repair_work_log set create_uid='%s' where id='%s'" % (s9, s1))
                cur_PROD.execute("commit")


        print ("neweb_repair_repair_work_log complete_")
        print ("")

        print ("NEWEB 導入正式環境 neweb_repair_questionnaire")
        print ("")
        cur_neweb.execute("select max(id) from neweb_repair_questionnaire")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,name from neweb_repair_questionnaire")
        myrec1=cur_neweb.fetchall()
        cur_PROD.execute("delete from neweb_repair_questionnaire")
        cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]

            print (s1,s2)
            cur_PROD.execute("insert into neweb_repair_questionnaire(id,name) values ('%s','%s')" % (s1,s2))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_repair_questionnaire_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,code,disabled,write_date,write_uid,create_date,create_uid from neweb_repair_questionnaire")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            print (s1,s2,s3)
            if s2:
                cur_PROD.execute("update neweb_repair_questionnaire set code='%s' where id='%s'" % (s2,s1))
                cur_PROD.execute("commit")
            if s3:
                cur_PROD.execute("update neweb_repair_questionnaire set disabled='%s' where id='%s'" % (s3,s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update neweb_repair_questionnaire set write_date='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update neweb_repair_questionnaire set write_uid='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update neweb_repair_questionnaire set create_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_repair_questionnaire set create_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")

        print ("neweb_repair_questionnaire complete")
        print ("")

        print ("NEWEB 導入正式環境 neweb_repair_question")
        print ("")
        cur_neweb.execute("select max(id) from neweb_repair_question")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,name from neweb_repair_question")
        myrec1=cur_neweb.fetchall()
        cur_PROD.execute("delete from neweb_repair_question")
        cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]

            print (s1,s2)
            cur_PROD.execute("insert into neweb_repair_question(id,name) values ('%s','%s')" % (s1,s2))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_repair_question_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,questionnaire_id,disabled,write_date,write_uid,create_date,create_uid from neweb_repair_question")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            print (s1,s2,s3)
            if s2:
                try:
                    cur_PROD.execute("update neweb_repair_question set questionnaire_id='%s' where id='%s'" % (s2,s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("questionnaire_id no update")
            if s3:
                cur_PROD.execute("update neweb_repair_question set disabled='%s' where id='%s'" % (s3,s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update neweb_repair_question set write_date='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update neweb_repair_question set write_uid='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update neweb_repair_question set create_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_repair_question set create_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
        print ("neweb_repair_question complete")
        print ("")

        print ("NEWEB 導入正式環境 neweb_repair_repair_questionnaire")
        print ("")
        cur_neweb.execute("select max(id) from neweb_repair_repair_questionnaire")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id from neweb_repair_repair_questionnaire")
        # cur_PROD.execute("delete from neweb_repair_repair_questionnaire")
        # cur_PROD.execute("commit")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]

            print (s1)
            cur_PROD.execute("insert into neweb_repair_repair_questionnaire(id) values ('%s')" % (s1))
            cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence neweb_repair_repair_questionnaire_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,rating,repair_id,state,question_id,write_date,write_uid,create_date,create_uid from neweb_repair_repair_questionnaire")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            print (s1, s2, s3, s4, s5)
            if s2:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set rating='%s' where id='%s'" % (s2, s1))
                cur_PROD.execute("commit")
            if s3:
                try:
                    cur_PROD.execute(
                        "update neweb_repair_repair_questionnaire set repair_id='%s' where id='%s'" % (s3, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("neweb_repair_repair_questionnaire no update")

            if s4:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set state='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                try:
                    cur_PROD.execute(
                        "update neweb_repair_repair_questionnaire set question_id='%s' where id='%s'" % (s5, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("neweb_repair_repair_questionnaire no update")
            if s6:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set write_date='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set write_uid='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
            if s8:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set create_date='%s' where id='%s'" % (s8, s1))
                cur_PROD.execute("commit")
            if s9:
                cur_PROD.execute("update neweb_repair_repair_questionnaire set create_uid='%s' where id='%s'" % (s9, s1))
                cur_PROD.execute("commit")

        print ("neweb_repair_repair_questionnaire complete")
        print ("")

        print ("NEWEB 正式環境導入 neweb_repair_repair_line")
        print ('')

        cur_neweb.execute("select max(id) from neweb_repair_repair_line")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id from neweb_repair_repair_line")
        cur_PROD.execute("delete from neweb_repair_repair_line")
        cur_PROD.execute("commit")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]

            print (s1)
            cur_PROD.execute("insert into neweb_repair_repair_line (id) values ('%s')" % (s1))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_repair_repair_line_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("""select id,sequence,repair_id,contract_line,problem_desc,asset_num,
        sla_delay_warn,state,write_date,write_uid,create_date,create_uid from neweb_repair_repair_line""")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            s8=line[7]
            s9=line[8]
            s10=line[9]
            s11=line[10]
            s12=line[11]
            print (s1,s2,s3,s4,s5,s6,s7,s8)
            if s2:
               cur_PROD.execute("update neweb_repair_repair_line set sequence='%s' where id='%s'" % (s2,s1))
               cur_PROD.execute("commit")
            if s3:
               try:
                   cur_PROD.execute("update neweb_repair_repair_line set repair_id='%s' where id='%s'" % (s3, s1))
                   cur_PROD.execute("commit")
               except Exception as inst:
                   print ("repair_id no update")
            if s4:
               try:
                   cur_PROD.execute("update neweb_repair_repair_line set contract_line='%s' where id='%s'" % (s4, s1))
                   cur_PROD.execute("commit")
               except Exception as inst:
                   print ("contract_line no update")
            if s5:
               cur_PROD.execute("update neweb_repair_repair_line set problem_desc='%s' where id='%s'" % (s5, s1))
               cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update neweb_repair_repair_line set asset_num='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update neweb_repair_repair_line set sla_delay_warn='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
            if s8:
                cur_PROD.execute("update neweb_repair_repair_line set state='%s' where id='%s'" % (s8, s1))
                cur_PROD.execute("commit")
            if s9:
                cur_PROD.execute("update neweb_repair_repair_line set write_date='%s' where id='%s'" % (s9, s1))
                cur_PROD.execute("commit")
            if s10:
                cur_PROD.execute("update neweb_repair_repair_line set write_uid='%s' where id='%s'" % (s10, s1))
                cur_PROD.execute("commit")
            if s11:
                cur_PROD.execute("update neweb_repair_repair_line set create_date='%s' where id='%s'" % (s11, s1))
                cur_PROD.execute("commit")
            if s12:
                cur_PROD.execute("update neweb_repair_repair_line set create_uid='%s' where id='%s'" % (s12, s1))
                cur_PROD.execute("commit")
        print ("neweb_repair_repair_line complete")
        print ("")

        print ("NEWEB 正式導入NEWEB_REPAIR_REPAIR_PART ")
        print ("")

        cur_neweb.execute("select max(id) from neweb_repair_repair_part")
        mymaxid=cur_neweb.fetchone()
        cur_neweb.execute("select id,prod from neweb_repair_repair_part")
        myrec1=cur_neweb.fetchall()
        cur_PROD.execute("delete from neweb_repair_repair_part")
        cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]

            print (s1,s2)
            try:
                cur_PROD.execute("""insert into neweb_repair_repair_part(id,prod) values
                           ('%s','%s')""" % (s1,s2))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No inert")


        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_repair_repair_part_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("""select id,used_parts_qty,required_parts_qty,
         repair_line_id,part_maintenance_category_id,state,write_date,write_uid,create_date,create_uid from neweb_repair_repair_part""")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            s8=line[7]
            s9=line[8]
            s10=line[9]
            print (s1,s2,s3,s4,s5,s6)
            if s2:
               cur_PROD.execute("update neweb_repair_repair_part set used_parts_qty='%s' where id='%s'" % (s2,s1))
               cur_PROD.execute("commit")
            if s3:
               cur_PROD.execute("update neweb_repair_repair_part set required_parts_qty='%s' where id='%s'" % (s3,s1))
               cur_PROD.execute("commit")
            if s4:
               try:
                  cur_PROD.execute("update neweb_repair_repair_part set repair_line_id='%s' where id='%s'" % (s4, s1))
                  cur_PROD.execute("commit")
               except Exception as inst:
                  print ("repair_line_id no update")
            if s5:
               try:
                  cur_PROD.execute("update neweb_repair_repair_part set part_maintenance_category_id='%s' where id='%s'" % (s5, s1))
                  cur_PROD.execute("commit")
               except Exception as inst:
                  print ("part_maintenance_category_id no update")
            if s6:
               cur_PROD.execute("update neweb_repair_repair_part set state='%s' where id='%s'" % (s6,s1))
               cur_PROD.execute("commit")
            if s7:
               cur_PROD.execute("update neweb_repair_repair_part set write_date='%s' where id='%s'" % (s7, s1))
               cur_PROD.execute("commit")
            if s8:
               cur_PROD.execute("update neweb_repair_repair_part set write_uid='%s' where id='%s'" % (s8, s1))
               cur_PROD.execute("commit")
            if s9:
               cur_PROD.execute("update neweb_repair_repair_part set create_date='%s' where id='%s'" % (s9, s1))
               cur_PROD.execute("commit")
            if s10:
               cur_PROD.execute("update neweb_repair_repair_part set create_uid='%s' where id='%s'" % (s10, s1))
               cur_PROD.execute("commit")

        print ("neweb_repair_repair_part complete")
        print ("")

        print ("NEWEB 正式導入NEWEB_BASE_PRODUCT_LINK ")
        print ("")

        cur_neweb.execute("select max(id) from neweb_base_product_link")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,prod from neweb_base_product_link")
        myrec1 = cur_neweb.fetchall()
        cur_PROD.execute("delete from neweb_base_product_link")
        cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]

            print (s1,s2)
            cur_PROD.execute("""insert into neweb_base_product_link(id,prod) values
               ('%s','%s')""" % (s1,s2))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_base_product_link_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,prod_tmp_id,quantity,write_date,write_uid,create_date,create_uid from neweb_base_product_link")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            print (s1,s2,s3)
            if s2:
               try:
                  cur_PROD.execute("update neweb_base_product_link set prod_tmp_id='%s' where id='%s'" % (s2,s1))
                  cur_PROD.execute("commit")
               except Exception as inst:
                  print ("prod_temp_id no update")
            if s3:
               cur_PROD.execute("update neweb_base_product_link set quantity='%s' where id='%s'" % (s3,s1))
               cur_PROD.execute("commit")
            if s4:
               cur_PROD.execute("update neweb_base_product_link set write_date='%s' where id='%s'" % (s4, s1))
               cur_PROD.execute("commit")
            if s5:
               cur_PROD.execute("update neweb_base_product_link set write_uid='%s' where id='%s'" % (s5, s1))
               cur_PROD.execute("commit")
            if s6:
               cur_PROD.execute("update neweb_base_product_link set create_date='%s' where id='%s'" % (s6, s1))
               cur_PROD.execute("commit")
            if s7:
               cur_PROD.execute("update neweb_base_product_link set create_uid='%s' where id='%s'" % (s7, s1))
               cur_PROD.execute("commit")

        print ("neweb_base_product_link complete")
        print ("")


    def warehouse_orderpoint(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
            self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        #conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo"
        #conn_PROD = psycopg2.connect(conn2_string)
        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB 正式環境導入 stock_warehouse_orderpoint")
        print ("")
        cur_neweb.execute("select max(id) from stock_warehouse_orderpoint")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("""select id,lead_type,location_id,name,product_id,product_max_qty,product_min_qty,qty_multiple,warehouse_id,company_id from stock_warehouse_orderpoint""")
        myrec1 = cur_neweb.fetchall()
        cur_PROD.execute("delete from stock_warehouse_orderpoint")
        #cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            s7=line[6]
            s8=line[7]
            s9=line[8]
            s10=line[9]
            cur_PROD.execute("select count(*) from product_product where id=%d" % s5)
            mycount=cur_PROD.fetchone()

            if int(mycount[0]) >= 1 :
               print ("%s" % mycount)
               print ("%s %s %s %s %s %s %s %s %s %s" % (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10))
               cur_PROD.execute("""insert into stock_warehouse_orderpoint(id,lead_type,location_id,name,product_id,product_max_qty,product_min_qty,qty_multiple,warehouse_id,company_id) VALUES (%s,'%s',%s,'%s',%s,%f,%f,%f,%s,%s)""" % (s1, s2, s3, s4, s5, s6, s7, s8, s9,s10))

        cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence stock_warehouse_orderpoint_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,company_id,write_uid,active,write_date,lead_days from stock_warehouse_orderpoint")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6=line[5]
            # try:
            #     cur_PROD.execute("update stock_warehouse_orderpoint set company_id='%s' where id='%s'" % (s2,s1))
            #     cur_PROD.execute("commit")
            # except Exception as inst:
            #     print "No update stock_warehouse_orderpoint => company_id"
            try:
                cur_PROD.execute("update stock_warehouse_orderpoint set write_uid='%s' where id='%s'" % (s3, s1))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No update stock_warehouse_orderpoint => write_uid")
            try:
                cur_PROD.execute("update stock_warehouse_orderpoint set active='%s' where id='%s'" % (s4,s1))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No update stock_warehouse_orderpoint => active")
            try:
                cur_PROD.execute("update stock_warehouse_orderpoint set write_date='%s' where id='%s'" % (s5,s1))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No update stock_warehouse_orderpoint => write_date")
            try:
                cur_PROD.execute("update stock_warehouse_orderpoint set lead_days='%s' where id='%s'" % (s6,s1))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No update stock_warehouse_orderpoint => lead_days")
        print ("NEWEB 正式環竟導入 stock_warehouse_orderpoint 完成")
        print ("")



    def stock_location(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB 正式環境導入 stock_location")
        print ("")
        cur_neweb.execute("select max(id) from stock_location")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("""select id,name,usage,active from stock_location""")
        myrec1 = cur_neweb.fetchall()
        cur_PROD.execute("delete from procurement_rule")
        cur_PROD.execute("delete from stock_warehouse")
        cur_PROD.execute("delete from stock_location")
        cur_PROD.execute("delete from stock_location_route")
        cur_PROD.execute("commit")
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            cur_PROD.execute("insert into stock_location(id,name,usage,active) values (%s,'%s','%s',%s)" % (s1,s2,s3,s4))
            cur_PROD.execute("commit")
            print ("%s %s %s %s" % (s1,s2,s3,s4))
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence stock_location_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,complete_name,parent_left,parent_right,location_id,scrap_location from stock_location")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            if s2:
                cur_PROD.execute("update stock_location set complete_name='%s' where id='%s'" % (s2,s1))
                cur_PROD.execute("commit")
            if s3:
                cur_PROD.execute("update stock_location set parent_left='%s' where id='%s'" % (s3, s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update stock_location set parent_right='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update stock_location set location_id='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update stock_location set scrap_location='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")

        cur_neweb.execute("select max(id) from stock_location_route")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,name,sequence,warehouse_selectable,company_id,product_selectable,product_categ_selectable,active from stock_location_route")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            cur_PROD.execute("""insert into stock_location_route(id,name,sequence,warehouse_selectable,company_id,product_selectable,product_categ_selectable,active) values 
                      (%s,'%s',%s,%s,%s,%s,%s,%s)""" % (s1, s2, s3, s4,s5,s6,s7,s8))
            cur_PROD.execute("commit")
            print ("%s %s %s %s" % (s1, s2, s3, s4))
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence stock_location_route_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("select id,sale_selectable from stock_location_route")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            if s2:
               cur_PROD.execute("update stock_location_route set sale_selectable='%s' where id='%s'" % (s2,s1))
               cur_PROD.execute("commit")
        print ("NEWEB 正式環竟導入 stock_location 完成")
        print ("")


    def stock_warehouse(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
        self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB 正式環境導入 ir_sequence")
        print ("")
        cur_neweb.execute("select max(id) from ir_sequence")
        mymaxid=cur_neweb.fetchone()
        cur_PROD.execute("select max(id) from ir_sequence")
        mynewebmaxid = cur_PROD.fetchone()
        myintmaxid = int(mynewebmaxid[0])
        cur_neweb.execute("select id,implementation,name,number_increment,number_next,padding from ir_sequence")
        myrec1=cur_neweb.fetchall()

        cur_PROD.execute("delete from account_journal")
        cur_PROD.execute("delete from procurement_rule")
        cur_PROD.execute("delete from stock_warehouse")
        #cur_PROD.execute("delete from procurement_rule")
        cur_PROD.execute("delete from stock_picking_type")
        # cur_PROD.execute("delete from account_journal")
        cur_PROD.execute("delete from ir_sequence")

        cur_PROD.execute("commit")
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            # s7 = line[6]
            # s8 = line[7]
            try:
                cur_PROD.execute("""insert into ir_sequence(id,implementation,name,number_increment,number_next,padding,reset_init_number,reset_period)
                             values (%s,'%s','%s',%s,%s,%s,1,'day')""" % (s1, s2, s3, s4, s5, s6))
                cur_PROD.execute("commit")
                print ("%s %s %s %s" % (s1, s2, s3, s4))
            except Exception as inst:
                print ("Insert fail")

        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence ir_sequence_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        print ("NEWEB 正式環境導入 ir_sequence 完成")
        print ("")

        print ("NEWEB 正式環境導入 stock_picking_type")
        print ("")
        cur_neweb.execute("select max(id) from stock_picking_type")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,code,name,sequence_id from stock_picking_type")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            try:
                cur_PROD.execute("""insert into stock_picking_type(id,code,name,sequence_id) values (%s,'%s','%s',%s)""" % (
                    s1, s2, s3, s4))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("Insert fail")
            print ("%s %s %s %s" % (s1,s2,s3,s4))
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence stock_picking_type_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("""select id,sequence,color,use_create_lots,default_location_dest_id,show_entire_packs,use_existing_lots,
               warehouse_id,active,return_picking_type_id,default_location_src_id from stock_picking_type""")
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]
            s11 = line[10]
            if s2:
                try:
                   cur_PROD.execute("""update stock_picking_type set sequence=%d where id=%d """ % (s2,s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type  sequence OK!")
                except Exception as inst:
                    print ("update sequence fail")
            if s3:
                try:
                   cur_PROD.execute("""update stock_picking_type set color=%d where id=%d """ % (s3, s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type color OK!")
                except Exception as inst:
                   print ("update color fail")
            if s4:
                try:
                   cur_PROD.execute("""update stock_picking_type set use_create_lots=%s where id=%d """ % (s4, s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type use_create_lots OK!")
                except Exception as inst:
                   print ("update use_create_lots fail")
            if s5:
                try:
                   cur_PROD.execute("""update stock_picking_type set default_location_dest_id=%d where id=%d """ % (s5, s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type default_location_dest_id OK!")
                except Exception as inst:
                   print ("update fail")
            if s6:
                try:
                   cur_PROD.execute("""update stock_picking_type set show_entire_packs=%s where id=%d """ % (s6, s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type show_entire_packs OK!")
                except Exception as inst:
                   print ("update show_entire_packs fail")
            if s7:
               try:
                   cur_PROD.execute("""update stock_picking_type set use_existing_lots=%s where id=%d """ % (s7, s1))
                   cur_PROD.execute("commit")
                   print ("UPDATE stock_picking_type use_existing_type OK!")
               except Exception as inst:
                   print ("update use_existing_type fail")
            # if s8:
            #    try:
            #       cur_PROD.execute("""update stock_picking_type set warehouse_id=%d where id=%d """ % (s8, s1))
            #       cur_PROD.execute("commit")
            #       print "UPDATE stock_picking_type warehouse_id OK!"
            #    except Exception as inst:
            #        print "update warehouse_id fail"
            if s9:
               try:
                  cur_PROD.execute("""update stock_picking_type set active=%s where id=%d """ % (s9, s1))
                  cur_PROD.execute("commit")
                  print ("UPDATE stock_picking_type active OK!")
               except Exception as inst:
                   print ("update active fail")
            if s10:
               try:
                  cur_PROD.execute("""update stock_picking_type set return_picking_type_id=%d where id=%d """ % (s10, s1))
                  cur_PROD.execute("commit")
                  print ("UPDATE stock_picking_type return_picking_type_id OK!")
               except Exception as inst:
                   print ("update return_picking_type_id fail")
            if s11:
               try:
                  cur_PROD.execute("""update stock_picking_type set default_location_src_id=%d where id=%d """ % (s11, s1))
                  cur_PROD.execute("commit")
                  print ("UPDATE stock_picking_type default_location_src_id OK!")
               except Exception as inst:
                   print ("update default_location_src_id fail")

        print ("")
        print ("NEWEB 正式環境導入 stock_picking_type 完成")
        print ("")

        print ("NEWEB 正式環境導入 stock_warehouse")
        print ("")
        cur_neweb.execute("select max(id) from stock_warehouse")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("""select id,code,company_id,delivery_steps,lot_stock_id,name,reception_steps,view_location_id,pick_type_id from stock_warehouse""")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            cur_PROD.execute("""insert into stock_warehouse(id,code,company_id,delivery_steps,lot_stock_id,name,reception_steps,view_location_id,active,pick_type_id) values 
                          (%s,'%s',%s,'%s',%s,'%s','%s',%s,TRUE,%s)""" % (s1, s2, s3, s4, s5, s6, s7, s8,s9))
            cur_PROD.execute("commit")
            print ("%s %s %s %s" % (s1, s2, s3, s4))
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence stock_warehouse_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        print ("NEWEB 正式環境導入stock_warehouse 完成")
        print ("")


        print ("NEWEB 正式環境導入 procurement_rule")
        print ("")
        cur_neweb.execute("select max(id) from procurement_rule")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,action,name,picking_type_id,procure_method from procurement_rule")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            cur_PROD.execute("""insert into procurement_rule(id,action,name,picking_type_id,procure_method) VALUES 
                    (%s,'%s','%s',%s,'%s')""" % (s1,s2,s3,s4,s5))
            cur_PROD.execute("commit")
            print ("%s %s %s %s" % (s1,s2,s3,s4))
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence procurement_rule_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        cur_neweb.execute("select id,warehouse_id from stock_picking_type")
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            if s2:
               try:
                  cur_PROD.execute("""update stock_picking_type set warehouse_id=%d where id=%d""" % (s2,s1))
                  cur_PROD.execute("commit")
                  print ("Update stock_picking_type warehouse_id OK!")
               except Exception as inst:
                   print ("Update stock_picking_type warehouse_id OK!")

    def neweb_to_prod(self):
        conn1_string = "host='192.168.1.222' dbname='NEWEB' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn1_string)
        cur_PROD = conn_PROD.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        cur_PROD = conn_PROD.cursor()
        cur_PROD.execute("select max(id) from hr_department")
        mynewebmaxid = cur_PROD.fetchone()
        cur_PROD.execute("select id,parent_id,active,name from hr_department")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            cur_PROD.execute("select count(*) from hr_department where id=%d " % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
                cur_PROD.execute("insert into hr_department (id,name) values ('%s','%s')" % (s1, s4))
            if s2:
                cur_PROD.execute("update hr_department set parent_id=%s  where id=%s" % (s2,s1))
            if s3:
                cur_PROD.execute("update hr_department set active=%s  where id=%s" % (s3, s1))
            if s4:
                cur_PROD.execute("update hr_department set name='%s'  where id=%s" % (s4, s1))
            cur_PROD.execute("commit")



        mymaxid1 = int(mynewebmaxid[0]) + 1
        cur_PROD.execute("alter sequence hr_department_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        print ("HR_DEPARTMENT UPDATE")
        print ("")
        print ("")

        cur_PROD.execute("select max(id) from hr_job")
        mymaxid=cur_PROD.fetchone()
        cur_PROD.execute("select id,name,state from hr_job")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1=line[0]
            s2=line[1]

            cur_PROD.execute("select count(*) from hr_job where id=%s" % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
               cur_PROD.execute("insert into hr_job (id,name,state) values (%s,'%s','recruit')" % (s1,s2))
            else :
               cur_PROD.execute("update hr_job set name='%s' where id=%s" % (s2,s1))
        mymaxid1 = int(mymaxid[0])+1
        cur_PROD.execute("alter sequence hr_job_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        print ("HR_JOB UPDATE")
        print ("")
        print ("")

        cur_PROD.execute("select max(id) from resource_resource")
        mymaxid = cur_PROD.fetchone()
        cur_PROD.execute("select id,name from resource_resource")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            s2 = line[1]

            cur_PROD.execute("select count(*) from resource_resource where id=%s" % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
                cur_PROD.execute("insert into resource_resource (id,name,resource_type,time_efficiency) values (%s,'%s','user',1)" % (s1, s2))
                cur_PROD.execute("commit")
            else:
                cur_PROD.execute("update resource_resource set name='%s' where id=%s" % (s2, s1))
                cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence resource_resource_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        print ("RESOURCE_RESOURCE UPDATE")
        print ("")
        print ("")




        cur_PROD.execute("select max(id) from hr_employee")
        mymaxid = cur_PROD.fetchone()
        cur_PROD.execute("select id,job_id,coach_id,parent_id,resource_id,department_id,work_email,work_location,employee_num from hr_employee")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            s2 = line[4]
            cur_PROD.execute("select count(*) from hr_employee where id=%d " % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
                sql_string2 = """insert into hr_employee(id,resource_id) values (%s,%s)""" % (s1,s2)
                cur_PROD.execute(sql_string2)
                cur_PROD.execute("commit")
        for line1 in myrec:
            s1 = line1[0]
            s2 = line1[1]
            s3 = line1[2]
            s4 = line1[3]
            s5 = line1[4]
            s6 = line1[5]
            s7 = line1[6]
            s8 = line1[7]
            s9 = line1[8]

            #print "%s %s %s %s %s" % (s1,s2,s3,s4,s5)
            # cur_PROD.execute("select count(*) from hr_employee where id=%d " % s1)
            # mycount = cur_PROD.fetchone()
            # if int(mycount[0]) == 0 :
            #     sql_string2 = """insert into hr_employee(id) values ('%s')""" % (s1)
            #     cur_PROD.execute(sql_string2)
            if s2:
                cur_PROD.execute("update hr_employee set job_id='%s'  where id='%s'" % (s2, s1))
            if s3:
                cur_PROD.execute("update hr_employee set coach_id='%s'  where id='%s'" % (s3,s1))
            if s4:
                cur_PROD.execute("update hr_employee set parent_id='%s'  where id='%s'" % (s4, s1))
            if s5:
                try:
                   cur_PROD.execute("update hr_employee set resource_id='%s'  where id='%s'" % (s5, s1))
                except Exception as inst:
                   print ("NO UPDATE ")
            if s6:
                cur_PROD.execute("update hr_employee set department_id='%s'  where id='%s'" % (s6, s1))
            if s7:
                cur_PROD.execute("update hr_employee set work_email='%s'  where id='%s'" % (s7, s1))
            if s8:
                cur_PROD.execute("update hr_employee set work_location='%s'  where id='%s'" % (s8, s1))
            if s9:
                cur_PROD.execute("update hr_employee set employee_num='%s'  where id='%s'" % (s9, s1))

        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence hr_employee_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        print ("HR_EMPLOYEE UPDATE")
        print ("")
        print ("")


        cur_PROD.execute("select max(id) from res_partner")
        mymaxid = cur_PROD.fetchone()
        cur_PROD.execute("select id,name,employee,street,display_name,email,lang,tz,vat from res_partner")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            #print "%s %s %s %s %s" % (s1,s2,s3,s4,s5)
            cur_PROD.execute("select count(*) from res_partner where id=%s" % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
               cur_PROD.execute("insert into res_partner(id,name,invoice_warn,notify_email,sale_warn,picking_warn,purchase_warn) values (%s,'%s','no-message','always','no-message','no-message','no-message')" % (s1,s2))
            if s3:
               cur_PROD.execute("update res_partner set employee=%s where id=%s" %(s3,s1))
            if s4:
               cur_PROD.execute("update res_partner set street='%s' where id=%s" %(s4,s1))
            if s5:
               cur_PROD.execute("update res_partner set display_name='%s' where id=%s" %(s5,s1))
            if s6:
               cur_PROD.execute("update res_partner set email='%s' where id=%s" %(s6,s1))
            if s7:
               cur_PROD.execute("update res_partner set lang='%s' where id=%s" %(s7,s1))
            if s8:
               cur_PROD.execute("update res_partner set tz='%s' where id=%s" %(s8,s1))
            if s9:
               cur_PROD.execute("update res_partner set vat='%s' where id=%s" %(s9,s1))
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence res_partner_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        print ("RES_PARTNER UPDATE")
        print ("")
        print ("")



        cur_PROD.execute("select max(id) from res_users")
        mymaxid = cur_PROD.fetchone()
        cur_PROD.execute("select id,partner_id,login from res_users")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            #print "%s %s %s" % (s1,s2,s3)
            cur_PROD.execute("select count(*) from res_users where id=%s" % s1)
            mycount = cur_PROD.fetchone()
            if int(mycount[0]) == 0:
               try :
                 cur_PROD.execute("insert into res_users(id,partner_id,login,company_id) values (%s,%s,'%s','1')" % (s1,s2,s3))
               except Exception as inst:
                 print ("NO UPDATE:")
        mymaxid1 = int(mymaxid[0])+1
        cur_PROD.execute("alter sequence res_users_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        print ("RES_USERS UPDATE")
        print ("")
        print ("")


        cur_PROD.execute("delete from res_groups_users_rel")
        cur_PROD.execute("commit")
        cur_PROD.execute("select gid,uid from res_groups_users_rel")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1=line[0]
            s2=line[1]
            try:
              cur_PROD.execute("insert into res_groups_users_rel(gid,uid) values (%s,%s)" % (s1,s2))
              cur_PROD.execute("commit")
            except Exception as inst:
              print ("NO INSERT :")

        print ("RES_GROUPS_USERS_REL UPDATE")
        print ("")
        print ("")


    def setsladisabled(self):
        conn1_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn1_string)
        cur_PROD = conn_PROD.cursor()
        print ("PROD SLA OLD DATA SET DISABLED")
        print ("")
        cur_PROD.execute("update neweb_base_sla set disabled=TRUE ;")
        cur_PROD.execute("commit")

        print ("PROD SLA DISABLED OLD DATA")
        print ("")
        print ("")



        ############# 合約異動轉資料

    def contract_newupdate_migration(self):

        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
            self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        # conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        # conn_PROD = psycopg2.connect(conn2_string)
        # cur_PROD = conn_PROD.cursor()
       
        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        cur_PROD.execute("select max(id) from product_template")
        myprodmaxid = cur_PROD.fetchone()
        print ("NEWEB 正式環境導入 neweb_base_maintenance_category")
        print ('')


        print ("NEWEB 正式環境導入product_template")
        print ('')
        cur_neweb.execute("select max(id) from product_template")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,categ_id,name,type,uom_id,uom_po_id from product_template where id > %d" % int(myprodmaxid[0]))
        myrec1 = cur_neweb.fetchall()

        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]

            print (s1, s2, s3, s4, s5, s6)
            cur_PROD.execute("""insert into product_template (id,categ_id,name,type,
                      uom_id,uom_po_id,purchase_line_warn,sale_line_warn,tracking,track_service,invoice_policy,purchase_method) VALUES
                     ('%s','%s','%s','%s','%s','%s','no-message','no-message','none','manual','order','receive')""" % (
            s1, s2, s3, s4, s5, s6))
            cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence product_template_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_neweb.execute("""select id,sale_ok,active,sale_delay,purchase_ok,serial,serial_num,maintenance_category_id,
                      specification,is_maintenance_target,brand,model from product_template where id > %d""" % int(myprodmaxid[0]))
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]
            s11 = line[10]
            s12 = line[11]
            print (s1, s2, s3, s4, s5, s6, s7)
            if s2:
                cur_PROD.execute("update product_template set sale_ok='%s' where id='%s'" % (s2, s1))
                cur_PROD.execute("commit")
            if s3:
                cur_PROD.execute("update product_template set active='%s' where id='%s'" % (s3, s1))
                cur_PROD.execute("commit")
            if s4:
                cur_PROD.execute("update product_template set sale_delay='%s' where id='%s'" % (s4, s1))
                cur_PROD.execute("commit")
            if s5:
                cur_PROD.execute("update product_template set purchase_ok='%s' where id='%s'" % (s5, s1))
                cur_PROD.execute("commit")
            if s6:
                cur_PROD.execute("update product_template set serial='%s' where id='%s'" % (s6, s1))
                cur_PROD.execute("commit")
            if s7:
                cur_PROD.execute("update product_template set serial_num='%s' where id='%s'" % (s7, s1))
                cur_PROD.execute("commit")
            if s8:
                cur_PROD.execute("update product_template set maintenance_category_id='%s' where id='%s'" % (s8, s1))
                cur_PROD.execute("commit")
            if s9:
                try:
                    cur_PROD.execute("update product_template set specification='%s' where id='%s'" % (s9, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("Specification NO update")
            if s10:
                cur_PROD.execute("update product_template set is_maintenance_target='%s' where id='%s'" % (s10, s1))
                cur_PROD.execute("commit")
            if s11:
                cur_PROD.execute("update product_template set brand='%s' where id='%s'" % (s11, s1))
                cur_PROD.execute("commit")
            if s12:
                cur_PROD.execute("update product_template set model='%s' where id='%s'" % (s12, s1))
                cur_PROD.execute("commit")
        print ("product template update OK!")

        print ("NEWEB 正式環境導入product_product")
        print ('')

        cur_PROD.execute("select max(id) from product_product")
        myprodmaxid = cur_PROD.fetchone()
        cur_neweb.execute("select max(id) from product_product")
        mymaxid = cur_neweb.fetchone()
        cur_neweb.execute("select id,product_tmpl_id,active from product_product where id > %d" % int(myprodmaxid[0]))
        myrec1 = cur_neweb.fetchall()

        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            print (s1, s2, s3)
            cur_PROD.execute(
                "insert into product_product(id,product_tmpl_id,active) values ('%s','%s','%s')" % (s1, s2, s3))
            cur_PROD.execute("commit")
        mymaxid1 = int(mymaxid[0]) + 1
        cur_PROD.execute("alter sequence product_product_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        cur_neweb.execute("select id,default_code,name_template from product_product where id > %d" % int(myprodmaxid[0]))
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            print (s1, s2, s3)
            if s2:
                try:
                    cur_PROD.execute("update product_product set default_code='%s' where id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print (" default_code no update")
            if s3:
                try:
                    cur_PROD.execute("update product_product set name_template='%s' where id='%s'" % (s3, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("name_template no update")
        cur_PROD.execute("select migration_prod_temp()")
        cur_PROD.execute("commit")
        print ("PRODUCT_PRODUCT update OK!")
        
        
        
        

        print ("PROD 異動資料導入環境 ")
        print ('')

        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
            self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        #conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        #conn_PROD = psycopg2.connect(conn2_string)
        #cur_PROD = conn_PROD.cursor()
        conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        cur_PROD = conn_PROD.cursor()


        cur_PROD.execute("select max(id) from res_partner")
        mymaxid = cur_PROD.fetchone()
        cur_neweb.execute("select max(id) from res_partner")
        mynewmaxid = cur_neweb.fetchone()
        cur_neweb.execute("select name,email,lang,tz,supplier,is_company,customer,id from res_partner where id > %d" % int(mymaxid[0]))
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            if not s2:
                s2 = '-'
            s3 = line[2]
            if not s3:
                s3 = 'zh_TW'
            s4 = line[3]
            if not s4:
                s4 = 'Asia/Taipei'
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            print (s1, s2, s3, s4, s5, s6, s7)
            if s5 and s6 and s7:
                sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s',%s,'%s','%s','1','%s','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                             s1, s2, s3, s4, s5, s6, s7, s1, s8)
            elif s5 and s6:
                sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s5, s6, s1, s8)
            elif s5 and s7:
                sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s5, s7, s1, s8)
            elif s6 and s7:
                sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s6, s7, s1, s8)
            elif s5:
                sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s5, s1, s8)
            elif s6:
                sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s6, s1, s8)
            elif s7:
                sql_string = "insert into res_partner(name,email,lang,tz,active,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s7, s1, s8)
            else:
                sql_string = "insert into res_partner(name,email,lang,tz,active,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                             "values ('%s','%s','%s','%s','1','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                 s1, s2, s3, s4, s1, s8)
            try:
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("NO Insert")
        mymaxid1 = int(mynewmaxid[0]) + 1
        cur_PROD.execute("alter sequence res_partner_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        cur_PROD.execute("update res_partner set company_id='1'")
        cur_PROD.execute("commit")

        cur_neweb.execute("""select id,street,zip,function,phone,mobile,fax,title,
                                             parent_id,use_parent_address,vat,commercial_partner_id,
                                             company_type,color,comment,website,type,employee
                                            from res_partner where id > %d""" % int(mymaxid[0]))
        myrec1 = cur_neweb.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            if not s2:
                s2 = '-'
            s3 = line[2]
            if not s3:
                s3 = '-'
            s4 = line[3]
            if not s4:
                s4 = '-'
            s5 = line[4]
            if not s5:
                s5 = '-'
            s6 = line[5]
            if not s6:
                s6 = '-'
            s7 = line[6]
            if not s7:
                s7 = '-'
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]
            if not s10:
                s10 = 'False'
            s11 = line[10]
            if not s11:
                s11 = '-'
            s12 = line[11]
            s13 = line[12]
            if not s13:
                s13 = '-'
            s14 = line[13]
            if not s14:
                s14 = 0
            s15 = line[14]
            if not s15:
                s15 = '-'
            s16 = line[15]
            if not s16:
                s16 = '-'
            s17 = line[16]
            if not s17:
                s17 = '-'
            s18 = line[17]
            if not s18:
                s18 = 'False'
            if s8 and s9 and s12:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                            phone='%s',mobile='%s',fax='%s',title='%s',parent_id='%s',
                                            vat='%s',commercial_partner_id='%s',color='%s',comment='%s',website='%s',
                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s8, s9, s11, s12, s14, s15, s16, s17, s18, s1)
            elif s8 and s9:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',title='%s',parent_id='%s',
                                                            vat='%s',color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s8, s9, s11, s14, s15, s16, s17, s18, s1)
            elif s9 and s12:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',parent_id='%s',
                                                            vat='%s',commercial_partner_id='%s',
                                                             color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s9, s11, s12, s14, s15, s16, s17, s18, s1)
            elif s8 and s12:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',title='%s',
                                                            vat='%s',commercial_partner_id='%s',
                                                             color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s8, s11, s12, s14, s15, s16, s17, s18, s1)
            elif s8:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',title='%s',
                                                            vat='%s',color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s8, s11, s14, s15, s16, s17, s18, s1)
            elif s9:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',parent_id='%s',
                                                            vat='%s',color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s9, s11, s14, s15, s16, s17, s18, s1)
            elif s12:
                sql_string = """update res_partner set street='%s',zip='%s',function='%s',
                                                            phone='%s',mobile='%s',fax='%s',
                                                            vat='%s',commercial_partner_id='%s',
                                                             color='%s',comment='%s',website='%s',
                                                 type='%s',employee='%s' where id='%s'""" % (
                    s2, s3, s4, s5, s6, s7, s11, s12, s14, s15, s16, s17, s18, s1)
            print (s1, s2, s3, s4, s5)
            try:
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("NO Update")
        
        
        
        
        
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        cur_PROD = conn_PROD.cursor()

        #conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        #conn_PROD = psycopg2.connect(conn2_string)
        #cur_PROD = conn_PROD.cursor()
        print ("PROD 合約異動資料導入 neweb_contract_contract")
        print ('')
        cur_PROD.execute("select max(id) from neweb_contract_contract")         # 目前PROD環境最大ID
        prodmaxid = cur_PROD.fetchone()
        myprodmaxid = int(prodmaxid[0])
        cur_neweb.execute("select max(id) from neweb_contract_contract")
        mymaxid = cur_neweb.fetchone()

        sql_string="""select id,daily_maintain_hour_end,daily_maintain_hour_start,is_maintenance_contract,
        inspection_warn,warranty_warn,customer_name,is_outsourcing_service,need_recovery_rehearsal,num_of_contract_lines,
        state,name,is_rental_contract,site_check,deployment,weekly_maintain_day,project_no,is_locked,project,site_check_upload,
        maintenance_warn,sla from neweb_contract_contract where id > %d""" % myprodmaxid
        cur_neweb.execute(sql_string)
        myrec1=cur_neweb.fetchall()
        #cur_PROD.execute("delete from neweb_contract_contract")
        #cur_PROD.execute("commit")
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]
            s11 = line[10]
            s12 = line[11]
            s13 = line[12]
            s14 = line[13]
            s15 = line[14]
            s16 = line[15]
            s17 = line[16]
            s18 = line[17]
            s19 = line[18]
            s20 = line[19]
            s21 = line[20]
            s22 = line[21]
            print (s1,s2,s3,s4,s5,s6,s7,s8)
            sql_string="""insert into neweb_contract_contract (id,daily_maintain_hour_end,daily_maintain_hour_start,
            is_maintenance_contract,inspection_warn,warranty_warn,is_outsourcing_service,need_recovery_rehearsal,
            num_of_contract_lines,state,name,is_rental_contract,site_check,deployment,weekly_maintain_day,project_no,
            is_locked,project,site_check_upload,maintenance_warn) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
            '%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
                       % (s1,s2,s3,s4,s5,s6,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18,s19,s20,s21)
            cur_PROD.execute(sql_string)
            cur_PROD.execute("commit")
        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_contract_contract_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")
        sql_string="""select id,ae,contract_memo,warranty_end_date,cur_inspection_date,penalties,sales,recovery_rehearsal_status,
        recovery_rehearsal_datetime,maintenance_warn_days,end_customer,inspection_warn_days,maintenance_start_date,clinch_date,
        maintenance_end_date,sales_dept,warranty_start_date,recovery_rehearsal_description,inspection_date,tx_price,warranty_warn_days,
        ae_dept,contact_person,sla,customer_name from neweb_contract_contract where id > %d""" % myprodmaxid
        cur_neweb.execute(sql_string)
        myrec1=cur_neweb.fetchall()
        for line in myrec1:
            s1=line[0]
            s2=line[1]
            s3=line[2]
            s4=line[3]
            s5=line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]
            s11 = line[10]
            s12 = line[11]
            s13 = line[12]
            s14 = line[13]
            s15 = line[14]
            s16 = line[15]
            s17 = line[16]
            s18 = line[17]
            s19 = line[18]
            s20 = line[19]
            s21 = line[20]
            s22 = line[21]
            s23 = line[22]
            s24 = line[23]
            s25 = line[24]
            print ("Update %s %s %s %s" % (s2,s3,s4,s5))
            if s2:
               cur_PROD.execute("update neweb_contract_contract set ae='%s' where id='%s'" % (s2,s1))
               cur_PROD.execute("commit")
            if s3:
               cur_PROD.execute("update neweb_contract_contract set contract_memo='%s' where id='%s'" % (s3,s1))
               cur_PROD.execute("commit")
            if s4:
               cur_PROD.execute("update neweb_contract_contract set warranty_end_date='%s' where id='%s'" % (s4,s1))
               cur_PROD.execute("commit")
            if s5:
               cur_PROD.execute("update neweb_contract_contract set cur_inspection_date='%s' where id='%s'" % (s5,s1))
               cur_PROD.execute("commit")
            if s6:
               cur_PROD.execute("update neweb_contract_contract set penalties='%s' where id='%s'" % (s6,s1))
               cur_PROD.execute("commit")
            if s7:
               cur_PROD.execute("update neweb_contract_contract set sales='%s' where id='%s'" % (s7,s1))
               cur_PROD.execute("commit")
            if s8:
               cur_PROD.execute("update neweb_contract_contract set recovery_rehearsal_status='%s' where id='%s'" % (s8,s1))
               cur_PROD.execute("commit")
            if s9:
               cur_PROD.execute("update neweb_contract_contract set recovery_rehearsal_datetime='%s' where id='%s'" % (s9,s1))
               cur_PROD.execute("commit")
            if s10:
               cur_PROD.execute("update neweb_contract_contract set maintenance_warn_days='%s' where id='%s'" % (s10,s1))
               cur_PROD.execute("commit")
            if s11:
                try:
                   cur_PROD.execute("update neweb_contract_contract set end_customer='%s' where id='%s'" % (s11, s1))
                   cur_PROD.execute("commit")
                except Exception as inst:
                   print ("NO Update: end_customer")

            if s12:
               cur_PROD.execute("update neweb_contract_contract set inspection_warn_days='%s' where id='%s'" % (s12,s1))
               cur_PROD.execute("commit")
            if s13:
               cur_PROD.execute("update neweb_contract_contract set maintenance_start_date='%s' where id='%s'" % (s13,s1))
               cur_PROD.execute("commit")
            if s14:
               cur_PROD.execute("update neweb_contract_contract set clinch_date='%s' where id='%s'" % (s14,s1))
               cur_PROD.execute("commit")
            if s15:
               cur_PROD.execute("update neweb_contract_contract set maintenance_end_date='%s' where id='%s'" % (s15,s1))
               cur_PROD.execute("commit")
            if s16:
                cur_PROD.execute("update neweb_contract_contract set sales_dept='%s' where id='%s'" % (s16, s1))
                cur_PROD.execute("commit")
            if s17:
               cur_PROD.execute("update neweb_contract_contract set warranty_start_date='%s' where id='%s'" % (s17,s1))
               cur_PROD.execute("commit")
            if s18:
               cur_PROD.execute("update neweb_contract_contract set recovery_rehearsal_description='%s' where id='%s'" % (s18,s1))
               cur_PROD.execute("commit")
            if s19:
               cur_PROD.execute("update neweb_contract_contract set inspection_date='%s' where id='%s'" % (s19,s1))
               cur_PROD.execute("commit")
            if s20:
                cur_PROD.execute("update neweb_contract_contract set tx_price='%s' where id='%s'" % (s20, s1))
                cur_PROD.execute("commit")
            if s21:
               cur_PROD.execute("update neweb_contract_contract set warranty_warn_days='%s' where id='%s'" % (s21,s1))
               cur_PROD.execute("commit")
            if s22:
               cur_PROD.execute("update neweb_contract_contract set ae_dept='%s' where id='%s'" % (s22, s1))
               cur_PROD.execute("commit")
            if s23:
               cur_PROD.execute("update neweb_contract_contract set contact_person='%s' where id='%s'" % (s23,s1))
               cur_PROD.execute("commit")
            if s24:
               cur_PROD.execute("update neweb_contract_contract set sla='%s' where id='%s'" % (s24,s1))
               cur_PROD.execute("commit")
            if s25:
                try:
                   cur_PROD.execute("update neweb_contract_contract set customer_name='%s' where id='%s'" % (s25, s1))
                   cur_PROD.execute("commit")
                except Exception as inst:
                   print ("NO Update: customer_name")
            cur_PROD.execute("update neweb_contract_contract set daily_maintain_hour_start='16' where daily_maintain_hour_start='None'")
            cur_PROD.execute("update neweb_contract_contract set daily_maintain_hour_end='38' where daily_maintain_hour_end='None'")
            cur_PROD.execute("update neweb_contract_contract set weekly_maintain_day='1' where weekly_maintain_day='None'")
            cur_PROD.execute("commit")
            cur_PROD.execute("select migration_contract_ae();")
            cur_PROD.execute("commit")


    def contract_line_newupdate_migration(self):

        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
            self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        cur_PROD = conn_PROD.cursor()

        conn_PROD = psycopg2.connect(database='NEWEB', user='odoo')
        cur_PROD = conn_PROD.cursor()
        cur_PROD.execute("select max(id) from product_template")
        myprodmaxid = cur_PROD.fetchone()

        #
        # print "NEWEB migration product_template"
        # print ''
        # cur_neweb.execute("select max(id) from product_template")
        # mymaxid = cur_neweb.fetchone()
        # cur_neweb.execute(
        #     "select id,categ_id,name,type,uom_id,uom_po_id from product_template where id > %d" % int(myprodmaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        #
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     s3 = line[2]
        #     s4 = line[3]
        #     s5 = line[4]
        #     s6 = line[5]
        #
        #     # print s1, s2, s3, s4, s5, s6
        #     cur_PROD.execute("""insert into product_template (id,categ_id,name,type,
        #                       uom_id,uom_po_id,purchase_line_warn,sale_line_warn,tracking,track_service,invoice_policy,purchase_method) VALUES
        #                      ('%s','%s','%s','%s','%s','%s','no-message','no-message','none','manual','order','receive')""" % (
        #         s1, s2, s3, s4, s5, s6))
        #     cur_PROD.execute("commit")
        # mymaxid1 = int(mymaxid[0]) + 1
        # cur_PROD.execute("alter sequence product_template_id_seq restart with %d" % mymaxid1)
        # cur_PROD.execute("commit")
        # cur_neweb.execute("""select id,sale_ok,active,sale_delay,purchase_ok,serial,serial_num,maintenance_category_id,
        #                       specification,is_maintenance_target,brand,model from product_template where id > %d""" % int(myprodmaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     s3 = line[2]
        #     s4 = line[3]
        #     s5 = line[4]
        #     s6 = line[5]
        #     s7 = line[6]
        #     s8 = line[7]
        #     s9 = line[8]
        #     s10 = line[9]
        #     s11 = line[10]
        #     s12 = line[11]
        #     # print s1, s2, s3, s4, s5, s6, s7
        #     if s2:
        #         cur_PROD.execute("update product_template set sale_ok='%s' where id='%s'" % (s2, s1))
        #         cur_PROD.execute("commit")
        #     if s3:
        #         cur_PROD.execute("update product_template set active='%s' where id='%s'" % (s3, s1))
        #         cur_PROD.execute("commit")
        #     if s4:
        #         cur_PROD.execute("update product_template set sale_delay='%s' where id='%s'" % (s4, s1))
        #         cur_PROD.execute("commit")
        #     if s5:
        #         cur_PROD.execute("update product_template set purchase_ok='%s' where id='%s'" % (s5, s1))
        #         cur_PROD.execute("commit")
        #     if s6:
        #         cur_PROD.execute("update product_template set serial='%s' where id='%s'" % (s6, s1))
        #         cur_PROD.execute("commit")
        #     if s7:
        #         cur_PROD.execute("update product_template set serial_num='%s' where id='%s'" % (s7, s1))
        #         cur_PROD.execute("commit")
        #     if s8:
        #         cur_PROD.execute("update product_template set maintenance_category_id='%s' where id='%s'" % (s8, s1))
        #         cur_PROD.execute("commit")
        #     if s9:
        #         try:
        #             cur_PROD.execute("update product_template set specification='%s' where id='%s'" % (s9, s1))
        #             cur_PROD.execute("commit")
        #         except Exception as inst:
        #             print "Specification NO update"
        #     if s10:
        #         cur_PROD.execute("update product_template set is_maintenance_target='%s' where id='%s'" % (s10, s1))
        #         cur_PROD.execute("commit")
        #     if s11:
        #         cur_PROD.execute("update product_template set brand='%s' where id='%s'" % (s11, s1))
        #         cur_PROD.execute("commit")
        #     if s12:
        #         cur_PROD.execute("update product_template set model='%s' where id='%s'" % (s12, s1))
        #         cur_PROD.execute("commit")
        # print "product template update OK!"
        #
        # print "NEWEB migration product_product"
        # print ''
        #
        # cur_PROD.execute("select max(id) from product_product")
        # myprodmaxid = cur_PROD.fetchone()
        # cur_neweb.execute("select max(id) from product_product")
        # mymaxid = cur_neweb.fetchone()
        # cur_neweb.execute("select id,product_tmpl_id,active from product_product where id > %d" % int(myprodmaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        #
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     s3 = line[2]
        #     # print s1, s2, s3
        #     cur_PROD.execute(
        #         "insert into product_product(id,product_tmpl_id,active) values ('%s','%s','%s')" % (s1, s2, s3))
        #     cur_PROD.execute("commit")
        # mymaxid1 = int(mymaxid[0]) + 1
        # cur_PROD.execute("alter sequence product_product_id_seq restart with %d" % mymaxid1)
        # cur_PROD.execute("commit")
        #
        # cur_neweb.execute(
        #     "select id,default_code,name_template from product_product where id > %d" % int(myprodmaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     s3 = line[2]
        #     #  s1, s2, s3
        #     if s2:
        #         try:
        #             cur_PROD.execute("update product_product set default_code='%s' where id='%s'" % (s2, s1))
        #             cur_PROD.execute("commit")
        #         except Exception as inst:
        #             print " default_code no update"
        #     if s3:
        #         try:
        #             cur_PROD.execute("update product_product set name_template='%s' where id='%s'" % (s3, s1))
        #             cur_PROD.execute("commit")
        #         except Exception as inst:
        #             print "name_template no update"
        # cur_PROD.execute("select migration_prod_temp()")
        # cur_PROD.execute("commit")
        # print "PRODUCT_PRODUCT update OK!"
        #
        # print "PROD upgrade "
        # print ''
        #
        # conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        # conn_neweb = psycopg2.connect(conn1_string)
        # cur_neweb = conn_neweb.cursor()
        # conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        # conn_PROD = psycopg2.connect(conn2_string)
        # cur_PROD = conn_PROD.cursor()
        # # conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        # # cur_PROD = conn_PROD.cursor()
        #
        # cur_PROD.execute("select max(id) from res_partner")
        # mymaxid = cur_PROD.fetchone()
        # cur_neweb.execute("select max(id) from res_partner")
        # mynewmaxid = cur_neweb.fetchone()
        # cur_neweb.execute("select name,email,lang,tz,supplier,is_company,customer,id from res_partner where id > %d" % int(mymaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     if not s2:
        #         s2 = '-'
        #     s3 = line[2]
        #     if not s3:
        #         s3 = 'zh_TW'
        #     s4 = line[3]
        #     if not s4:
        #         s4 = 'Asia/Taipei'
        #     s5 = line[4]
        #     s6 = line[5]
        #     s7 = line[6]
        #     s8 = line[7]
        #     #print s1, s2, s3, s4, s5, s6, s7
        #     if s5 and s6 and s7:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s',%s,'%s','%s','1','%s','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s5, s6, s7, s1, s8)
        #     elif s5 and s6:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s5, s6, s1, s8)
        #     elif s5 and s7:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s5, s7, s1, s8)
        #     elif s6 and s7:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s6, s7, s1, s8)
        #     elif s5:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s5, s1, s8)
        #     elif s6:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s6, s1, s8)
        #     elif s7:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s7, s1, s8)
        #     else:
        #         sql_string = "insert into res_partner(name,email,lang,tz,active,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
        #                      "values ('%s','%s','%s','%s','1','always','no-message','no-message','no-message','no-message','%s','%s')" % (
        #                          s1, s2, s3, s4, s1, s8)
        #     try:
        #         cur_PROD.execute(sql_string)
        #         cur_PROD.execute("commit")
        #     except Exception as inst:
        #         print "NO Insert"
        # mymaxid1 = int(mynewmaxid[0]) + 1
        # cur_PROD.execute("alter sequence res_partner_id_seq restart with %d" % mymaxid1)
        # cur_PROD.execute("commit")
        # cur_PROD.execute("update res_partner set company_id='1'")
        # cur_PROD.execute("commit")
        #
        # cur_neweb.execute("""select id,street,zip,function,phone,mobile,fax,title,
        #                                              parent_id,use_parent_address,vat,commercial_partner_id,
        #                                              company_type,color,comment,website,type,employee
        #                                             from res_partner where id > %d""" % int(mymaxid[0]))
        # myrec1 = cur_neweb.fetchall()
        # for line in myrec1:
        #     s1 = line[0]
        #     s2 = line[1]
        #     if not s2:
        #         s2 = '-'
        #     s3 = line[2]
        #     if not s3:
        #         s3 = '-'
        #     s4 = line[3]
        #     if not s4:
        #         s4 = '-'
        #     s5 = line[4]
        #     if not s5:
        #         s5 = '-'
        #     s6 = line[5]
        #     if not s6:
        #         s6 = '-'
        #     s7 = line[6]
        #     if not s7:
        #         s7 = '-'
        #     s8 = line[7]
        #     s9 = line[8]
        #     s10 = line[9]
        #     if not s10:
        #         s10 = 'False'
        #     s11 = line[10]
        #     if not s11:
        #         s11 = '-'
        #     s12 = line[11]
        #     s13 = line[12]
        #     if not s13:
        #         s13 = '-'
        #     s14 = line[13]
        #     if not s14:
        #         s14 = 0
        #     s15 = line[14]
        #     if not s15:
        #         s15 = '-'
        #     s16 = line[15]
        #     if not s16:
        #         s16 = '-'
        #     s17 = line[16]
        #     if not s17:
        #         s17 = '-'
        #     s18 = line[17]
        #     if not s18:
        #         s18 = 'False'
        #     if s8 and s9 and s12:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                             phone='%s',mobile='%s',fax='%s',title='%s',parent_id='%s',
        #                                             vat='%s',commercial_partner_id='%s',color='%s',comment='%s',website='%s',
        #                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s8, s9, s11, s12, s14, s15, s16, s17, s18, s1)
        #     elif s8 and s9:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',title='%s',parent_id='%s',
        #                                                             vat='%s',color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s8, s9, s11, s14, s15, s16, s17, s18, s1)
        #     elif s9 and s12:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',parent_id='%s',
        #                                                             vat='%s',commercial_partner_id='%s',
        #                                                              color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s9, s11, s12, s14, s15, s16, s17, s18, s1)
        #     elif s8 and s12:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',title='%s',
        #                                                             vat='%s',commercial_partner_id='%s',
        #                                                              color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s8, s11, s12, s14, s15, s16, s17, s18, s1)
        #     elif s8:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',title='%s',
        #                                                             vat='%s',color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s8, s11, s14, s15, s16, s17, s18, s1)
        #     elif s9:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',parent_id='%s',
        #                                                             vat='%s',color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s9, s11, s14, s15, s16, s17, s18, s1)
        #     elif s12:
        #         sql_string = """update res_partner set street='%s',zip='%s',function='%s',
        #                                                             phone='%s',mobile='%s',fax='%s',
        #                                                             vat='%s',commercial_partner_id='%s',
        #                                                              color='%s',comment='%s',website='%s',
        #                                                  type='%s',employee='%s' where id='%s'""" % (
        #             s2, s3, s4, s5, s6, s7, s11, s12, s14, s15, s16, s17, s18, s1)
        #     #print s1, s2, s3, s4, s5
        #     try:
        #         cur_PROD.execute(sql_string)
        #         cur_PROD.execute("commit")
        #     except Exception as inst:
        #         print "NO Update"

        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        cur_PROD = conn_PROD.cursor()
        # conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        # cur_PROD = conn_PROD.cursor()
        print ("PROD migration neweb_contract_contract_line")
        print ('')
        #
        # cur_PROD.execute("select max(id) from neweb_contract_contract_line")
        # prodcontractlineid = cur_PROD.fetchone()
        # myprodcontraclineid = int(prodcontractlineid[0])
        # projno=[]
        #projno.append('SVC0612-040')
        #projno.append('SVC0612-059')
        #projno.append('SVC0612-067')
        # projno.append('SVC0606-035')
        # projno.append('SVC0612-063')
        # projno.append('SVC0612-036')
        # projno.append('SVC0701-014')
        # projno.append('SVC0701-010')
        # projno.append('SVC0701-015')
        # projno.append('SVC0701-013')
        # projno.append('SVC0701-007')
        # projno.append('SVC0612-074')
        # projno.append('SVC0701-035')
        # projno.append('SVC0701-041')
        # projno.append('SVC0701-025')
        # projno.append('SVC0701-042')
        # projno.append('SVC0701-009')
        # projno.append('SVC0612-065')
        # projno.append('SVC0612-063')
        # projno.append('SVC0701-028')
        # projno.append('SVC0612-075')
        # projno.append('SVC0701-016')
        # projno.append('SVC0701-019')
        # projno.append('SVC0612-042')
        # projno.append('SVC0701-032')
        # projno.append('SVC0611-019')
        # projno.append('SVC0701-024')
        # projno.append('SVC0701-039')
        # projno.append('SVC0701-018')
        # projno.append('SVC0701-043')
        # projno.append('SVC0701-038')
        # projno.append('SVC0701-045')
        # projno.append('SVC0512-057')
        # projno.append('SVC0701-049')
        # projno.append('SVC0701-046')
        # projno.append('SVC0701-051')
        # projno.append('SVC0701-052')
        # projno.append('SVC0701-040')
        # projno.append('SVC0612-076')
        # projno.append('SVC0701-055')
        # projno.append('SVC0701-060')
        # projno.append('SVC0612-031')
        # projno.append('SVC0612-047')
        # projno.append('SVC0611-014')
        # projno.append('SVC0701-061')
        # projno.append('SVC0612-071')
        # projno.append('SVC0412-071')
        # projno.append('SVC0503-025')
        # projno.append('SVC0601-003')
        # projno.append('SVC0612-071')
        # projno.append('SVC0507-035')
        # projno.append('SVC0602-047')
        # projno.append('SVC0605-011')
        # projno.append('SVC0602-012')
        # projno.append('SVC0609-024')
        # projno.append('SVC0608-053')
        # projno.append('SVC0606-029')
        # projno.append('SVC0702-002')
        # projno.append('SVC0702-006')
        # projno.append('SVC0701-064')
        # projno.append('SVC0702-014')
        # projno.append('SVC0612-051')
        # projno.append('SVC0508-052')
        # projno.append('SVC0702-016')



        cur_neweb.execute("select max(id) from neweb_contract_contract_line")
        mymaxid=cur_neweb.fetchone()

        for rec in self:
            # for rec in projno:
           cur_neweb.execute("select id from neweb_contract_contract where project_no='%s'" % rec )
           print ("%s" % rec)
           mycontractlineid = cur_neweb.fetchone()
           cur_neweb.execute("select id from neweb_contract_contract_line where contract_id=%d" % mycontractlineid[0])
           print ("%s" % mycontractlineid[0])
           myrec = cur_neweb.fetchall()
           for contractline_rec in myrec:
              cur_neweb.execute("select id,contract_id,sequence,machine_serial_no,special_warn,x_locked,prod,special_warn_days from neweb_contract_contract_line where id = %d" % contractline_rec[0])
              myrec1=cur_neweb.fetchall()
              for line in myrec1:
                  s1=line[0]
                  s2=line[1]
                  s3=line[2]
                  s4=line[3]
                  s5=line[4]
                  s6=line[5]
                  s7=line[6]
                  s8=line[7]
                  #print "%s" %
                  try:
                     cur_PROD.execute("""insert into neweb_contract_contract_line(id,sequence,machine_serial_no,special_warn,x_locked,prod) values ('%s','%s','%s','%s','%s','%s')""" % (s1,s3,s4,s5,s6,s7))
                  except Exception as inst:
                     print ("fail:")
                  cur_PROD.execute("commit")
           for contractline_rec in myrec:
               cur_neweb.execute("select id,special_warn_date,maintain_partner,memo,prod_sla,special_warn_days,contract_id from neweb_contract_contract_line where id = %d" % contractline_rec[0])
               myrec1 = cur_neweb.fetchall()
               for line in myrec1:
                   s1 = line[0]
                   s2 = line[1]
                   s3 = line[2]
                   s4 = line[3]
                   s5 = line[4]
                   s6 = line[5]
                   s7 = line[6]
                   #print "update %s %s %s %s %s" % (s1, s2, s3, s4, s5)
                   if s2:
                       try:
                           cur_PROD.execute("update neweb_contract_contract_line set special_warn_date='%s' where id='%s'" % (s2, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: special_warn_date")
                   if s3:
                       try:
                           cur_PROD.execute(
                               "update neweb_contract_contract_line set maintain_partner='%s' where id='%s'" % (s3, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: maintain_partner")
                   if s4:
                       try:
                           cur_PROD.execute(
                               "update neweb_contract_contract_line set memo='%s' where id='%s'" % (s4, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: memo")
                   if s5:
                       try:
                           cur_PROD.execute(
                               "update neweb_contract_contract_line set prod_sla='%s' where id='%s'" % (s5, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: prod_sla")
                   if s6:
                       try:
                           cur_PROD.execute(
                               "update neweb_contract_contract_line set special_warn_days='%s' where id='%s'" % (
                               s6, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: special_warn_days")
                   if s7:
                       try:
                           cur_PROD.execute(
                               "update neweb_contract_contract_line set contract_id='%s' where id='%s'" % (s7, s1))
                           cur_PROD.execute("commit")
                       except Exception as inst:
                           print ("NO Update: contract_id")

        mymaxid1=int(mymaxid[0])+1
        cur_PROD.execute("alter sequence neweb_contract_contract_line_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")



        print ("Neweb_contract_contract_line complete")


    def updatemaindate(self):
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        cur_PROD = conn_PROD.cursor()

        cur_PROD.execute("select id,sla,maintenance_start_date,maintenance_end_date from neweb_contract_contract")
        myrec1 = cur_PROD.fetchall()
        for line in myrec1:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            print (s1, s2, s3, s4)
            # if s2:
            #     cur_PROD.execute(
            #         "update neweb_contract_contract_line set prod_sla='%s' where contract_id='%s'" % (s2, s1))
            #     cur_PROD.execute("commit")
            if s3 and s4:
                cur_PROD.execute(
                    "update neweb_contract_contract_line set contract_start_date='%s',contract_end_date='%s' where contract_id='%s'" % (
                    s3, s4, s1))
                cur_PROD.execute("commit")
        print ("Neweb_contract sla,main_start_date,main_end_date update complete")
        cur_PROD.execute("select migration_contract_line()")
        cur_PROD.execute("commit")



    def serviceadd_migration(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (self.SOURCE_IP,self.DB_NAME,self.USER_NAME,self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        #conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB 正式環境更新 Inspection_method")
        print ('')

        cur_neweb.execute("select id,inspection_method from neweb_contract_contract")
        myinspection = cur_neweb.fetchall()
        for line in myinspection:
            s1 = line[0]
            s2 = line[1]
            print ("%s %s" % (s1,s2))
            if s2:
               cur_PROD.execute("""update neweb_contract_contract set inspection_method='%s' where id=%d """ % (s2,s1))
               cur_PROD.execute("commit")


        print ("Inspection_method update complete")
        print ("")
        cur_PROD.execute("""delete from neweb_base_value_added_service_neweb_contract_contract_rel""")
        cur_PROD.execute("commit")
        cur_neweb.execute("""select * from neweb_base_value_added_service_neweb_contract_contract_rel""")
        myserviceadd = cur_neweb.fetchall()
        for line in myserviceadd:
            s1 = line[0]
            s2 = line[1]
            print ("%s %s" % (s1,s2))
            try:
               cur_PROD.execute("""insert into neweb_base_value_added_service_neweb_contract_contract_rel VALUES (%d,%d)""" % (s1,s2))
               cur_PROD.execute("commit")
            except Exception as inst:
               print ("No insert service added")


        print ("Service Added insert Compete")
        cur_PROD.close()
        cur_neweb.close()


    def calendar_migration(self):
        conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
        self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        conn_neweb = psycopg2.connect(conn1_string)
        cur_neweb = conn_neweb.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        # conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        cur_PROD = conn_PROD.cursor()
        print ("NEWEB calendar event migration")
        print ('')




        # print "Calendar Event Migration"
        # print ""
        # cur_neweb.execute("select max(id) from calendar_event")
        # maxid=cur_neweb.fetchone()
        # cur_neweb.execute("""select id,name,allday,create_date,display_start,recurrency,start_datetime,write_uid,month_by,rrule,
        #     duration,final_date,create_uid,user_id,tu,day,start,state,th,start_date,fr,stop_date,stop,stop_datetime,write_date,
        #     active,description,'1',count,end_type,we,mo,interval,su,recurrent_id,sa,show_as,oe_update_date from calendar_event
        #     where create_date >= '2018-01-01' """)
        #
        # mycalendar = cur_neweb.fetchall()
        # for line in mycalendar:
        #     s1 = line[0]
        #     s2 = ''+ line[1]
        #     s3 = line[2]
        #     s4 = line[3]
        #     s5 = line[4]
        #     s6 = line[5]
        #     s7 = line[6]      # start_date have null 1
        #     s8 = line[7]      # write_uid
        #     s9 = line[8]
        #     s10 = line[9]      # rrule have null   2
        #     s11 = line[10]
        #     s12 = line[11]
        #     s13 = line[12]    # create_uid
        #     s14 = line[13]
        #     s15 = line[14]
        #     s16 = line[15]     # day have null 3
        #     s17 = line[16]
        #     s18 = line[17]
        #     s19 = line[18]
        #     s20 = line[19]     # start_date have null 4
        #     s21 = line[20]
        #     s22 = line[21]     # stop_date have null  5
        #     s23 = line[22]
        #     s24 = line[23]     # stop_datetime have null  6
        #     s25 = line[24]
        #     s26 = line[25]
        #     s27 = line[26]     # description have null  7
        #     s28 = line[27]     # '1'
        #     s29 = line[28]
        #     s30 = line[29]
        #     s31 = line[30]
        #     s32 = line[31]
        #     s33 = line[32]
        #     s34 = line[33]
        #     s35 = line[34]     # recurrent_id have null   8
        #     s36 = line[35]
        #     s37 = line[36]
        #     s38 = line[37]
        #
        #     # print "%s %s" % (s1, s2)
        #     try:
        #         cur_PROD.execute("""insert into calendar_event (id,name,allday,create_date,display_start,recurrency,month_by,
        #             tu,start,state,th,fr,stop,write_date,active,count,end_type,we,mo,interval,su,sa,
        #             show_as,oe_update_date) values (%s,'%s',%s,'%s','%s',%s,'%s',%s,'%s','%s',%s,%s,'%s','%s',%s,%d,'%s',%s,%s,%s,%s,%s,'%s','%s')""" % (
        #             s1,s2,s3,s4,s5,s6,s9,s15,s17,s18,s19,s21,s23,s25,s26,s29,s30,s31,s32,s33,s34,s36,s37,s38))
        #         cur_PROD.execute("commit")
        #     except Exception as inst:
        #         print "No insert Calendar event:"
        #
        #
        # for line1 in mycalendar:
        #     s1 = line1[0]
        #     s2 = line1[1]
        #     s3 = line1[2]
        #     s4 = line1[3]
        #     s5 = line1[4]
        #     s6 = line1[5]
        #     s7 = line1[6]      # start_datetime have null 1
        #     s8 = line1[7]
        #     s9 = line1[8]
        #     s10 = line1[9]      # rrule have null   2
        #     s11 = line1[10]
        #     s12 = line1[11]
        #     s13 = line1[12]
        #     s14 = line1[13]
        #     s15 = line1[14]
        #     s16 = line1[15]     # day have null 3
        #     s17 = line1[16]
        #     s18 = line1[17]
        #     s19 = line1[18]
        #     s20 = line1[19]     # start_date have null 4
        #     s21 = line1[20]
        #     s22 = line1[21]     # stop_date have null  5
        #     s23 = line1[22]
        #     s24 = line1[23]     # stop_datetime have null  6
        #     s25 = line1[24]
        #     s26 = line1[25]
        #     s27 = line1[26]     # description have null  7
        #     s28 = line1[27]     # '1'
        #     s29 = line1[28]
        #     s30 = line1[29]
        #     s31 = line1[30]
        #     s32 = line1[31]
        #     s33 = line1[32]
        #     s34 = line1[33]
        #     s35 = line1[34]     # recurrent_id have null   8
        #     s36 = line1[35]
        #     s37 = line1[36]
        #     s38 = line1[37]
        #     if not s7:
        #        try:
        #            cur_PROD.execute("""update calendar_event set start_datetime='%s' where id=%s""" % (s7,s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update start_datetime:"
        #     if not s10:
        #        try:
        #            cur_PROD.execute("""update calendar_event set rrule='%s' where id=%s""" % (s10, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update rrule:"
        #     if not s16:
        #        try:
        #            cur_PROD.execute("""update calendar_event set day=%s where id=%s""" % (s16, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update day:"
        #     if not s20:
        #        try:
        #            cur_PROD.execute("""update calendar_event set start_date='%s' where id=%s""" % (s20, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update start_date:"
        #     if not s22:
        #        try:
        #            cur_PROD.execute("""update calendar_event set stop_date='%s' where id=%s""" % (s22, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update stop_date:"
        #     if not s24:
        #        try:
        #            cur_PROD.execute("""update calendar_event set stop_datetime='%s' where id=%s""" % (s24, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update stop_datetime:"
        #     if not s27:
        #        try:
        #            cur_PROD.execute("""update calendar_event set description='%s' where id=%s""" % (s27, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update description:"
        #     if not s35:
        #        try:
        #            cur_PROD.execute("""update calendar_event set recurrent_id=%s where id=%s""" % (s35, s1))
        #            cur_PROD.execute("commit")
        #        except Exception as inst:
        #            print "No update recurrent_id:"
        #     try:
        #        cur_PROD.execute("""update calendar_event set duration='%s' where id=%s""" % (s11,s1))
        #        cur_PROD.execute("commit")
        #     except Exception as inst:
        #        print "No update duration:"
        #     try:
        #        cur_PROD.execute("""update calendar_event set user_id=%s where id=%s""" % (s14, s1))
        #        cur_PROD.execute("commit")
        #     except Exception as inst:
        #        print "No update user_id:"
        #
        #     try:
        #        cur_PROD.execute("""update calendar_event set write_uid=%s where id=%s""" % (s8, s1))
        #        cur_PROD.execute("commit")
        #     except Exception as inst:
        #        print "No update write_uid"
        #
        #     try:
        #        cur_PROD.execute("""update calendar_event set create_uid=%s where id=%s""" % (s13, s1))
        #        cur_PROD.execute("commit")
        #     except Exception as inst:
        #        print "No update creatre_uid"
        #
        #
        # mymaxid1 = int(maxid[0]) + 1
        # cur_PROD.execute("""alter sequence calendar_event_id_seq restart with %d""" % mymaxid1)
        # cur_PROD.execute("commit")



        print ("Calendar Attendee Migration")
        print ("")
        cur_neweb.execute("select max(id) from calendar_attendee")
        maxid = cur_neweb.fetchone()
        cur_neweb.execute("""select id,create_uid,create_date,cn,access_token,event_id,state,email,
                                write_date,write_uid,partner_id,availability,google_internal_event_id,
                                oe_synchro_date from calendar_attendee where create_date >= '2018-01-01' """)

        myattendee = cur_neweb.fetchall()
        for line in myattendee:
            s1 = line[0]
            s2 = line[1]    # create_uid
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]   # write_uid
            s11 = line[10]
            s12 = line[11]
            s13 = line[12]
            s14 = line[13]

            print ("%s %s" % (s1, s4))
            try:
                cur_PROD.execute("""insert into calendar_attendee (id,create_date,common_name,
                      access_token,event_id,state,email,write_date)
                       values (%s,'%s','%s','%s',%s,'%s','%s','%s')""" % (s1, s3, s4, s5, s6, s7,s8,s9))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No insert calendar addtenee")

        for line1 in myattendee:
            s1 = line1[0]
            s2 = line1[1]
            s3 = line1[2]
            s4 = line1[3]
            s5 = line1[4]
            s6 = line1[5]
            s7 = line1[6]
            s8 = line1[7]
            s9 = line1[8]
            s10 = line1[9]
            s11 = line1[10]
            s12 = line1[11]
            s13 = line1[12]
            s14 = line1[13]

            if not s11:
                try:
                    cur_PROD.execute("""update calendar_attendee set partner_id=%s where id=%s""" % (s11, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update partner_id:")


            if not s12:
                try:
                    cur_PROD.execute("""update calendar_attendee set availability=%s where id=%s""" % (s12, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update availability:")
            if not s13:
                try:
                    cur_PROD.execute("""update calendar_attendee set google_internal_event_id='%s' where id=%s""" % (s13, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update google_internal_event_id:")
            if not s14:
                try:
                    cur_PROD.execute("""update calendar_attendee set oe_synchro_date='%s' where id=%s""" % (s14, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update oe_synchro_date:")

            if not s2:
                try:
                    cur_PROD.execute("""update calendar_attendee set create_uid=%s where id=%s""" % (s2, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update create_uid")
            if not s10:
                try:
                    cur_PROD.execute("""update calendar_attendee set write_uid=%s where id=%s""" % (s10, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No update write_uid")


        mymaxid1 = int(maxid[0]) + 1
        cur_PROD.execute("alter sequence calendar_attendee_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")


        print ("Calendar Alarm Migration")
        print ("")
        cur_neweb.execute("select max(id) from calendar_alarm")
        maxid = cur_neweb.fetchone()
        cur_neweb.execute("""select id,create_uid,create_date,name,interval,write_uid,duration_minutes,write_date,duration,type
                           from calendar_alarm where id >= 7 """)

        myalarm = cur_neweb.fetchall()
        for line in myalarm:
            s1 = line[0]
            s2 = line[1]
            s3 = line[2]
            s4 = line[3]
            s5 = line[4]
            s6 = line[5]
            s7 = line[6]
            s8 = line[7]
            s9 = line[8]
            s10 = line[9]

            print ("%s %s" % (s1, s4))
            try:
                cur_PROD.execute("""insert into calendar_alarm (id,create_date,name,
                                      interval,duration_minutes,write_date,duration,type)
                                       values (%s,%s,'%s',%s,%s,%s,%s,%s)""" % (
                s1, s3, s4, s5, s7, s8, s9, s10))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No insert calendar alarm")

        mymaxid1 = int(maxid[0]) + 1
        cur_PROD.execute("alter sequence calendar_alarm_id_seq restart with %d" % mymaxid1)
        cur_PROD.execute("commit")

        print ("insert calendar_alarm_calendar_event_rel")
        print ("")

        cur_PROD.execute("select max(calendar_event_id) from calendar_alarm_calendar_event_rel")
        mymaxeventid = cur_PROD.fetchone()
        try:
            mymaxeventid1=int(mymaxeventid[0])
        except Exception as inst:
            mymaxeventid1 = 0

        cur_neweb.execute("""select calendar_event_id,calendar_alarm_id from calendar_alarm_calendar_event_rel
                    where calendar_event_id > %d """ % mymaxeventid1)
        mycal_alarm_rel = cur_neweb.fetchall()
        for line in mycal_alarm_rel:
            s1 = line[0]
            s2 = line[1]
            try:
                cur_PROD.execute("""insert into calendar_alarm_calendar_event_rel(calendar_event_id,calendar_alarm_id)
                                values (%d,%d)""" % (s1,s2))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No insert calendar_alarm_calendar_event_rel")

        print ("insert calendar_event_res_partner_rel")
        print ("")

        cur_PROD.execute("select max(calendar_event_id) from calendar_event_res_partner_rel")
        mymaxeventid = cur_PROD.fetchone()
        try:
            mymaxeventid1=int(mymaxeventid[0])
        except Exception as inst:
            mymaxeventid1 = 0
        cur_neweb.execute("""select calendar_event_id,res_partner_id from calendar_event_res_partner_rel
                            where calendar_event_id > %d """ % mymaxeventid1)
        mycal_event_rel = cur_neweb.fetchall()
        for line in mycal_event_rel:
            s1 = line[0]
            s2 = line[1]
            try:
                cur_PROD.execute("""insert into calendar_event_res_partner_rel(calendar_event_id,res_partner_id)
                                        values (%d,%d)""" % (s1, s2))
                cur_PROD.execute("commit")
            except Exception as inst:
                print ("No insert calendar_event_res_partner_rel")

        #
        #
        # print "insert mail.followers"
        # print ""
        #
        # cur_neweb.execute("""select id,partner_id,channel_id,res_model,res_id from mail_followers where res_model='calendar.event'""")
        # mymailfollower = cur_neweb.fetchall()
        # for line in mymailfollower:
        #     s1 = line[0]
        #     s2 = line[1]    # partner_id have null
        #     s3 = line[2]    # channel_id is null
        #     s4 = line[3]
        #     s5 = line[4]
        #     if not s2:
        #        try:
        #            cur_PROD.execute("""insert into mail.followers(id,res_model,res_id)
        #               values(%s,'%s',%s) """ % (s1,s4,s5))
        #        except Exception as inst:
        #            print "No Insert Mail followers"
        #     else:
        #        try:
        #            cur_PROD.execute("""insert into mail.followers(id,partner_id,res_model,res_id)
        #                                  values(%s,%s,'%s',%s) """ % (s1,s2 ,s4, s5))
        #        except Exception as inst:
        #            print "No Insert Mail followers"
        #
        # cur_PROD.execute("commit")
        # cur_PROD.execute("select max(id) from mail.followers")
        # mymaxid = cur_PROD.fetchone()[0]
        # cur_PROD.execute("alter sequence mail_followers_id_seq restart with %d" % mymaxid)
        #
        # cur_neweb.execute(""" select id,create_date,write_date,write_uid,create_uid,parent_id,subtype_id,
        #                     res_id,message_id,body,record_name,no_auto_thread,date,model,reply_to,author_id,
        #                     message_type,email_from,subject from mail_message where model='calendar.event' and
        #                     create_date >= '2017-01-01' """)
        # mymailmessage = cur_neweb.fetchall()
        # for line in mymailmessage:
        #     s1 = line[0]
        #     s2 = line[1]
        #     s3 = line[2]
        #     s4 = line[3]
        #     s5 = line[4]
        #     s6 = line[5]    # parent_id have null
        #     s7 = line[6]
        #     s8 = line[7]
        #     s9 = line[8]
        #     s10 = line[9]   # body have null
        #     s11 = line[10]
        #     s12 = line[11]
        #     s13 = line[12]
        #     s14 = line[13]
        #     s15 = line[14]
        #     s16 = line[15]
        #     s17 = line[16]
        #     s18 = line[17]
        #     s19 = line[18]   # subject have null
        #     try:
        #         cur_PROD.execute("""insert into mail_message(id,create_date,write_date,write_uid,create_uid,
        #                          subtype_id,res_id,message_id,record_name,no_auto_thread,date,model,replay_to,
        #                          author_id,message_type,email_from) values (%s,%s,%s,%s,%s,%s,%s,'%s','%s',%s,%s,'%s',
        #                          '%s',%s,'%s','%s')""" % (s1,s2,s3,s4,s5,s7,s8,s9,s11,s12,s13,s14,s15,s16,s17,s18))
        #         cur_PROD.execute("commit")
        #     except Exception as inst:
        #         print "No Inert mail message"
        #     if s6:
        #        try:
        #            cur_PROD.execute("""update mail_message set parent_id=%s where id=%s""" % (s6,s1))
        #        except Exception as inst:
        #            print "No update parent_id"
        #     if s10:
        #        try:
        #            cur_PROD.execute("""update mail_message set body='%s' where id=%s""" % (s10, s1))
        #        except Exception as inst:
        #            print "No update body"
        #     if s19:
        #         try:
        #             cur_PROD.execute("""update mail_message set subject='%s' where id=%s""" % (s19, s1))
        #         except Exception as inst:
        #             print "No update subject"
        # cur_PROD.execute("""select max(id) from mail_message""")
        # mymaxid = cur_PROD.fetchone()[0]
        # cur_PROD.execute("alter sequence mail_message_id_seq restart with %d" % mymaxid)
        # cur_PROD.execute("commit")
        #
        # print "Calendar Migration Completed"
        # cur_PROD.close()
        # cur_neweb.close()

    def repair_carecalldate(self):
        # conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (
        # self.SOURCE_IP, self.DB_NAME, self.USER_NAME, self.PASSWORD)
        # conn_neweb = psycopg2.connect(conn1_string)
        # cur_neweb = conn_neweb.cursor()
        conn2_string = "host='192.168.1.222' dbname='PROD' user='odoo' password='odoo'"
        conn_PROD = psycopg2.connect(conn2_string)
        # conn_PROD = psycopg2.connect(database='PROD', user='odoo')
        cur_PROD = conn_PROD.cursor()
        # print "NEWEB 正式環境calendar event migration"
        # print ''
        cur_PROD.execute("select distinct repair_id from neweb_repair_repair_care_call_log ")
        myrec = cur_PROD.fetchall()
        for line in myrec:
            s1 = line[0]
            cur_PROD.execute("select get_carecalldate(%d)" % s1)
            cur_PROD.execute("commit")
        print ("Care Call Date Update Complete")



