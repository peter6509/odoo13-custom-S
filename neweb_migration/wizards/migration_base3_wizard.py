# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationbase3wizard(models.TransientModel):
    _name = "neweb_migration.base3_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def repair_migration(self):
        if self.passcode == '!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print ("NEWEB 正式環境導入(15).neweb_base_problem")
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
            num =0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                s4=line[3]

                print (s1,s2,s3,s4)
                cur_PROD.execute("""insert into neweb_base_problem(id,description,maintenance_category_id,name) VALUES
                  ('%s','%s','%s','%s')""" % (s1,s2,s3,s4))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (15, 'neweb_base.problem', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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
            print ("NEWEB 正式環境導入(16).neweb_base_problem_solution")
            print ("")
            cur_neweb.execute("select max(id) from neweb_base_problem_solution")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,name,problem_id from neweb_base_problem_solution")
            # cur_PROD.execute("delete from neweb_base_problem_solution")
            # cur_PROD.execute("commit")
            myrec1=cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]

                print (s1,s2,s3)
                cur_PROD.execute("""insert into neweb_base_problem_solution(id,name,problem_id) VALUES
                     ('%s','%s','%s')""" % (s1,s2,s3))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (16, 'neweb_base.problem_solution', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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



            print ("NEWEB 正式環境導入(17).neweb_repair_repair")
            print ('')

            cur_neweb.execute("select max(id) from neweb_repair_repair")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,contact_user,customer_id,name,repair_datetime from neweb_repair_repair")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_repair_repair")
            cur_PROD.execute("commit")
            i=0
            num = 0
            for line in myrec1:
                num = num +1
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
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (17, 'neweb_repair.repair', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 正式環境導入 (18).neweb_repair_repair_care_call_log")
            print ("")

            cur_neweb.execute("select max(id) from neweb_repair_repair_care_call_log")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id from neweb_repair_repair_care_call_log")
            # cur_PROD.execute("delete from neweb_repair_repair_care_call_log")
            # cur_PROD.execute("commit")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]

                print (s1)
                cur_PROD.execute("insert into neweb_repair_repair_care_call_log(id) values ('%s')" % (s1))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (18, 'neweb_repair.repair_care_call_log', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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


            print ("NEWEB 導入正式環境(19).neweb_repair_repair_work_log")
            print ("")
            cur_neweb.execute("select max(id) from neweb_repair_repair_work_log")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id from neweb_repair_repair_work_log")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num +1
                s1 = line[0]

                print (s1)
                cur_PROD.execute("insert into neweb_repair_repair_work_log(id) values ('%s')" % (s1))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (19, 'neweb_repair.repair_work_log', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 導入正式環境(20).neweb_repair_questionnaire")
            print ("")
            cur_neweb.execute("select max(id) from neweb_repair_questionnaire")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,name from neweb_repair_questionnaire")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_repair_questionnaire")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]

                print (s1,s2)
                cur_PROD.execute("insert into neweb_repair_questionnaire(id,name) values ('%s','%s')" % (s1,s2))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (20, 'neweb_repair.questionnaire', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 導入正式環境(21).neweb_repair_question")
            print ("")
            cur_neweb.execute("select max(id) from neweb_repair_question")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,name from neweb_repair_question")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_repair_question")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]

                print (s1,s2)
                cur_PROD.execute("insert into neweb_repair_question(id,name) values ('%s','%s')" % (s1,s2))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (21, 'neweb_repair.question', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_repair_question_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("select id,questionnaire_id,disabled,write_date,write_uid,create_date,create_uid from neweb_repair_question")
            myrec1=cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
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

            print ("NEWEB 導入正式環境(22).neweb_repair_repair_questionnaire")
            print ("")
            cur_neweb.execute("select max(id) from neweb_repair_repair_questionnaire")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id from neweb_repair_repair_questionnaire")
            # cur_PROD.execute("delete from neweb_repair_repair_questionnaire")
            # cur_PROD.execute("commit")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]

                print (s1)
                cur_PROD.execute("insert into neweb_repair_repair_questionnaire(id) values ('%s')" % (s1))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (22, 'neweb_repair.repair_questionnaire', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 正式環境導入(23).neweb_repair_repair_line")
            print ('')

            cur_neweb.execute("select max(id) from neweb_repair_repair_line")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id from neweb_repair_repair_line")
            cur_PROD.execute("delete from neweb_repair_repair_line")
            cur_PROD.execute("commit")
            myrec1=cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]

                print (s1)
                cur_PROD.execute("insert into neweb_repair_repair_line (id) values ('%s')" % (s1))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (23, 'neweb_repair.repair_line', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 正式導入(24).NEWEB_REPAIR_REPAIR_PART ")
            print ("")

            cur_neweb.execute("select max(id) from neweb_repair_repair_part")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,prod from neweb_repair_repair_part")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_repair_repair_part")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]

                print (s1,s2)
                try:
                    cur_PROD.execute("""insert into neweb_repair_repair_part(id,prod) values
                               ('%s','%s')""" % (s1,s2))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print ("No inert")

            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (24, 'neweb_repair.repair_part', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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

            print ("NEWEB 正式導入(25).NEWEB_BASE_PRODUCT_LINK ")
            print ("")

            cur_neweb.execute("select max(id) from neweb_base_product_link")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,prod from neweb_base_product_link")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_base_product_link")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]

                print (s1,s2)
                cur_PROD.execute("""insert into neweb_base_product_link(id,prod) values
                   ('%s','%s')""" % (s1,s2))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (25, 'neweb_base.product_link', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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