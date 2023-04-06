# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationbase4wizard(models.TransientModel):
    _name = "neweb_migration.base4_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def warehouse_orderpoint(self):
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
            print("正式環境導入(26).stock_warehouse_orderpoint")
            print("")
            cur_neweb.execute("select max(id) from stock_warehouse_orderpoint")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("""select id,lead_type,location_id,name,product_id,product_max_qty,product_min_qty,qty_multiple,warehouse_id,company_id from stock_warehouse_orderpoint""")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from stock_warehouse_orderpoint")
            # cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
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
                cur_PROD.execute("select count(*) from product_product where id=%d" % s5)
                mycount = cur_PROD.fetchone()

                if int(mycount[0]) >= 1:
                    print("%s" % mycount)
                    print("%s %s %s %s %s %s %s %s %s %s" % (s1, s2, s3, s4, s5, s6, s7, s8, s9, s10))
                    cur_PROD.execute(
                        """insert into stock_warehouse_orderpoint(id,lead_type,location_id,name,product_id,product_max_qty,product_min_qty,qty_multiple,warehouse_id,company_id) VALUES (%s,'%s',%s,'%s',%s,%f,%f,%f,%s,%s)""" % (
                        s1, s2, s3, s4, s5, s6, s7, s8, s9, s10))

                    cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (26, 'stock.warehouse_orderpoint', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence stock_warehouse_orderpoint_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute(
                "select id,company_id,write_uid,active,write_date,lead_days from stock_warehouse_orderpoint")
            myrec1 = cur_neweb.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]
                # try:
                #     cur_PROD.execute("update stock_warehouse_orderpoint set company_id='%s' where id='%s'" % (s2,s1))
                #     cur_PROD.execute("commit")
                # except Exception as inst:
                #     print "No update stock_warehouse_orderpoint => company_id"
                try:
                    cur_PROD.execute("update stock_warehouse_orderpoint set write_uid='%s' where id='%s'" % (s3, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No update stock_warehouse_orderpoint => write_uid")
                try:
                    cur_PROD.execute("update stock_warehouse_orderpoint set active='%s' where id='%s'" % (s4, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No update stock_warehouse_orderpoint => active")
                try:
                    cur_PROD.execute("update stock_warehouse_orderpoint set write_date='%s' where id='%s'" % (s5, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No update stock_warehouse_orderpoint => write_date")
                try:
                    cur_PROD.execute("update stock_warehouse_orderpoint set lead_days='%s' where id='%s'" % (s6, s1))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No update stock_warehouse_orderpoint => lead_days")
            print("NEWEB 正式環竟導入 stock_warehouse_orderpoint 完成")
            print("")

    def stock_location(self):
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
            print("正式環境導入(27).stock_location")
            print("")
            cur_neweb.execute("select max(id) from stock_location")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("""select id,name,usage,active from stock_location""")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from procurement_rule")
            cur_PROD.execute("delete from stock_warehouse")
            cur_PROD.execute("delete from stock_location")
            cur_PROD.execute("delete from stock_location_route")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                cur_PROD.execute(
                    "insert into stock_location(id,name,usage,active) values (%s,'%s','%s',%s)" % (s1, s2, s3, s4))
                cur_PROD.execute("commit")
                print("%s %s %s %s" % (s1, s2, s3, s4))
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (27, 'stock.location', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence stock_location_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute(
                "select id,complete_name,parent_left,parent_right,location_id,scrap_location from stock_location")
            myrec1 = cur_neweb.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]
                if s2:
                    cur_PROD.execute("update stock_location set complete_name='%s' where id='%s'" % (s2, s1))
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
            cur_neweb.execute(
                "select id,name,sequence,warehouse_selectable,company_id,product_selectable,product_categ_selectable,active from stock_location_route")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]
                s7 = line[6]
                s8 = line[7]
                cur_PROD.execute("""insert into stock_location_route(id,name,sequence,warehouse_selectable,company_id,product_selectable,product_categ_selectable,active) values 
                          (%s,'%s',%s,%s,%s,%s,%s,%s)""" % (s1, s2, s3, s4, s5, s6, s7, s8))
                cur_PROD.execute("commit")
                print("%s %s %s %s" % (s1, s2, s3, s4))
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (28, 'stock.location_route', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence stock_location_route_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("select id,sale_selectable from stock_location_route")
            myrec1 = cur_neweb.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                if s2:
                    cur_PROD.execute("update stock_location_route set sale_selectable='%s' where id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
            print("NEWEB 正式環竟導入 stock_location 完成")
            print("")

    def stock_warehouse(self):
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
            print("正式環境導入(29).ir_sequence")
            print("")
            cur_neweb.execute("select max(id) from ir_sequence")
            mymaxid = cur_neweb.fetchone()
            cur_PROD.execute("select max(id) from ir_sequence")
            mynewebmaxid = cur_PROD.fetchone()
            myintmaxid = int(mynewebmaxid[0])
            cur_neweb.execute("select id,implementation,name,number_increment,number_next,padding from ir_sequence")
            myrec1 = cur_neweb.fetchall()

            cur_PROD.execute("delete from account_journal")
            cur_PROD.execute("delete from procurement_rule")
            cur_PROD.execute("delete from stock_warehouse")
            # cur_PROD.execute("delete from procurement_rule")
            cur_PROD.execute("delete from stock_picking_type")
            # cur_PROD.execute("delete from account_journal")
            cur_PROD.execute("delete from ir_sequence")

            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
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
                    print("%s %s %s %s" % (s1, s2, s3, s4))
                except Exception as inst:
                    print("Insert fail")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (29, 'ir.sequence', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence ir_sequence_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("正式環境導入 ir_sequence 完成")
            print("")

            print("正式環境導入(30).stock_picking_type")
            print("")
            cur_neweb.execute("select max(id) from stock_picking_type")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,code,name,sequence_id from stock_picking_type")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                try:
                    cur_PROD.execute("""insert into stock_picking_type(id,code,name,sequence_id) values (%s,'%s','%s',%s)""" % (s1, s2, s3, s4))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("Insert fail")
                print("%s %s %s %s" % (s1, s2, s3, s4))
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (30, 'stock.picking_type', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence stock_picking_type_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("""select id,sequence,color,use_create_lots,default_location_dest_id,show_entire_packs,use_existing_lots,
                   warehouse_id,active,return_picking_type_id,default_location_src_id from stock_picking_type""")
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
                if s2:
                    try:
                        cur_PROD.execute("""update stock_picking_type set sequence=%d where id=%d """ % (s2, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type  sequence OK!")
                    except Exception as inst:
                        print("update sequence fail")
                if s3:
                    try:
                        cur_PROD.execute("""update stock_picking_type set color=%d where id=%d """ % (s3, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type color OK!")
                    except Exception as inst:
                        print("update color fail")
                if s4:
                    try:
                        cur_PROD.execute("""update stock_picking_type set use_create_lots=%s where id=%d """ % (s4, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type use_create_lots OK!")
                    except Exception as inst:
                        print("update use_create_lots fail")
                if s5:
                    try:
                        cur_PROD.execute(
                            """update stock_picking_type set default_location_dest_id=%d where id=%d """ % (s5, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type default_location_dest_id OK!")
                    except Exception as inst:
                        print("update fail")
                if s6:
                    try:
                        cur_PROD.execute("""update stock_picking_type set show_entire_packs=%s where id=%d """ % (s6, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type show_entire_packs OK!")
                    except Exception as inst:
                        print("update show_entire_packs fail")
                if s7:
                    try:
                        cur_PROD.execute("""update stock_picking_type set use_existing_lots=%s where id=%d """ % (s7, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type use_existing_type OK!")
                    except Exception as inst:
                        print("update use_existing_type fail")
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
                        print("UPDATE stock_picking_type active OK!")
                    except Exception as inst:
                        print("update active fail")
                if s10:
                    try:
                        cur_PROD.execute(
                            """update stock_picking_type set return_picking_type_id=%d where id=%d """ % (s10, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type return_picking_type_id OK!")
                    except Exception as inst:
                        print("update return_picking_type_id fail")
                if s11:
                    try:
                        cur_PROD.execute(
                            """update stock_picking_type set default_location_src_id=%d where id=%d """ % (s11, s1))
                        cur_PROD.execute("commit")
                        print("UPDATE stock_picking_type default_location_src_id OK!")
                    except Exception as inst:
                        print("update default_location_src_id fail")

            print("")
            print("正式環境導入 stock_picking_type 完成")
            print("")

            print("正式環境導入(31)stock_warehouse")
            print("")
            cur_neweb.execute("select max(id) from stock_warehouse")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute(
                """select id,code,company_id,delivery_steps,lot_stock_id,name,reception_steps,view_location_id,pick_type_id from stock_warehouse""")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
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
                              (%s,'%s',%s,'%s',%s,'%s','%s',%s,TRUE,%s)""" % (s1, s2, s3, s4, s5, s6, s7, s8, s9))
                cur_PROD.execute("commit")
                print("%s %s %s %s" % (s1, s2, s3, s4))
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (31, 'stock.warehouse', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence stock_warehouse_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("NEWEB 正式環境導入stock_warehouse 完成")
            print("")

            print("正式環境導入(32).procurement_rule")
            print("")
            cur_neweb.execute("select max(id) from procurement_rule")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,action,name,picking_type_id,procure_method from procurement_rule")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                cur_PROD.execute("""insert into procurement_rule(id,action,name,picking_type_id,procure_method) VALUES 
                        (%s,'%s','%s',%s,'%s')""" % (s1, s2, s3, s4, s5))
                cur_PROD.execute("commit")
                print("%s %s %s %s" % (s1, s2, s3, s4))
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (32, 'procurement_rule', num, num, 'neweb_base'))
            cur_PROD.execute("""commit""")
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
                        cur_PROD.execute("""update stock_picking_type set warehouse_id=%d where id=%d""" % (s2, s1))
                        cur_PROD.execute("commit")
                        print("Update stock_picking_type warehouse_id OK!")
                    except Exception as inst:
                        print("Update stock_picking_type warehouse_id OK!")

    def neweb_to_prod(self):
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
                    cur_PROD.execute("update hr_department set parent_id=%s  where id=%s" % (s2, s1))
                if s3:
                    cur_PROD.execute("update hr_department set active=%s  where id=%s" % (s3, s1))
                if s4:
                    cur_PROD.execute("update hr_department set name='%s'  where id=%s" % (s4, s1))
                cur_PROD.execute("commit")

            mymaxid1 = int(mynewebmaxid[0]) + 1
            cur_PROD.execute("alter sequence hr_department_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            print("HR_DEPARTMENT UPDATE")
            print("")
            print("")

            cur_PROD.execute("select max(id) from hr_job")
            mymaxid = cur_PROD.fetchone()
            cur_PROD.execute("select id,name,state from hr_job")
            myrec = cur_PROD.fetchall()
            for line in myrec:
                s1 = line[0]
                s2 = line[1]

                cur_PROD.execute("select count(*) from hr_job where id=%s" % s1)
                mycount = cur_PROD.fetchone()
                if int(mycount[0]) == 0:
                    cur_PROD.execute("insert into hr_job (id,name,state) values (%s,'%s','recruit')" % (s1, s2))
                else:
                    cur_PROD.execute("update hr_job set name='%s' where id=%s" % (s2, s1))
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence hr_job_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            print("HR_JOB UPDATE")
            print("")
            print("")

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
                    cur_PROD.execute(
                        "insert into resource_resource (id,name,resource_type,time_efficiency) values (%s,'%s','user',1)" % (
                        s1, s2))
                    cur_PROD.execute("commit")
                else:
                    cur_PROD.execute("update resource_resource set name='%s' where id=%s" % (s2, s1))
                    cur_PROD.execute("commit")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence resource_resource_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            print("RESOURCE_RESOURCE UPDATE")
            print("")
            print("")

            cur_PROD.execute("select max(id) from hr_employee")
            mymaxid = cur_PROD.fetchone()
            cur_PROD.execute(
                "select id,job_id,coach_id,parent_id,resource_id,department_id,work_email,work_location,employee_num from hr_employee")
            myrec = cur_PROD.fetchall()
            for line in myrec:
                s1 = line[0]
                s2 = line[4]
                cur_PROD.execute("select count(*) from hr_employee where id=%d " % s1)
                mycount = cur_PROD.fetchone()
                if int(mycount[0]) == 0:
                    sql_string2 = """insert into hr_employee(id,resource_id) values (%s,%s)""" % (s1, s2)
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

                # print u"%s %s %s %s %s" % (s1,s2,s3,s4,s5)
                # cur_PROD.execute("select count(*) from hr_employee where id=%d " % s1)
                # mycount = cur_PROD.fetchone()
                # if int(mycount[0]) == 0 :
                #     sql_string2 = """insert into hr_employee(id) values ('%s')""" % (s1)
                #     cur_PROD.execute(sql_string2)
                if s2:
                    cur_PROD.execute("update hr_employee set job_id='%s'  where id='%s'" % (s2, s1))
                if s3:
                    cur_PROD.execute("update hr_employee set coach_id='%s'  where id='%s'" % (s3, s1))
                if s4:
                    cur_PROD.execute("update hr_employee set parent_id='%s'  where id='%s'" % (s4, s1))
                if s5:
                    try:
                        cur_PROD.execute("update hr_employee set resource_id='%s'  where id='%s'" % (s5, s1))
                    except Exception as inst:
                        print("NO UPDATE ")
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
            print("HR_EMPLOYEE UPDATE")
            print("")



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
                # print u"%s %s %s %s %s" % (s1,s2,s3,s4,s5)
                cur_PROD.execute("select count(*) from res_partner where id=%s" % s1)
                mycount = cur_PROD.fetchone()
                if int(mycount[0]) == 0:
                    cur_PROD.execute(
                        "insert into res_partner(id,name,invoice_warn,notify_email,sale_warn,picking_warn,purchase_warn) values (%s,'%s','no-message','always','no-message','no-message','no-message')" % (
                        s1, s2))
                if s3:
                    cur_PROD.execute("update res_partner set employee=%s where id=%s" % (s3, s1))
                if s4:
                    cur_PROD.execute("update res_partner set street='%s' where id=%s" % (s4, s1))
                if s5:
                    cur_PROD.execute("update res_partner set display_name='%s' where id=%s" % (s5, s1))
                if s6:
                    cur_PROD.execute("update res_partner set email='%s' where id=%s" % (s6, s1))
                if s7:
                    cur_PROD.execute("update res_partner set lang='%s' where id=%s" % (s7, s1))
                if s8:
                    cur_PROD.execute("update res_partner set tz='%s' where id=%s" % (s8, s1))
                if s9:
                    cur_PROD.execute("update res_partner set vat='%s' where id=%s" % (s9, s1))
                cur_PROD.execute("commit")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence res_partner_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("RES_PARTNER UPDATE")
            print("")

            cur_PROD.execute("select max(id) from res_users")
            mymaxid = cur_PROD.fetchone()
            cur_PROD.execute("select id,partner_id,login from res_users")
            myrec = cur_PROD.fetchall()
            for line in myrec:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                # print u"%s %s %s" % (s1,s2,s3)
                cur_PROD.execute("select count(*) from res_users where id=%s" % s1)
                mycount = cur_PROD.fetchone()
                if int(mycount[0]) == 0:
                    try:
                        cur_PROD.execute(
                            "insert into res_users(id,partner_id,login,company_id) values (%s,%s,'%s','1')" % (s1, s2, s3))
                    except Exception as inst:
                        print("NO UPDATE:")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence res_users_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            print("RES_USERS UPDATE")
            print("")


            cur_PROD.execute("delete from res_groups_users_rel")
            cur_PROD.execute("commit")
            cur_PROD.execute("select gid,uid from res_groups_users_rel")
            myrec = cur_PROD.fetchall()
            for line in myrec:
                s1 = line[0]
                s2 = line[1]
                try:
                    cur_PROD.execute("insert into res_groups_users_rel(gid,uid) values (%s,%s)" % (s1, s2))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("NO INSERT :")

            print("RES_GROUPS_USERS_REL UPDATE")
            print("")


    def setsladisabled(self):
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
            print("PROD SLA OLD DATA SET DISABLED")
            print("")
            cur_PROD.execute("update neweb_base.sla set disabled=TRUE ;")
            cur_PROD.execute("commit")

            print("PROD SLA DISABLED OLD DATA")
            print("")


            ############# 合約異動轉資料

    def contract_newupdate_migration(self):
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
            cur_PROD.execute("select max(id) from product_template")
            myprodmaxid = cur_PROD.fetchone()
            print("NEWEB 正式環境導入 neweb_base_maintenance_category")
            print('')

            print("正式環境導入product_template")
            print('')
            cur_neweb.execute("select max(id) from product_template")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute(
                "select id,categ_id,name,type,uom_id,uom_po_id from product_template where id > %d" % int(myprodmaxid[0]))
            myrec1 = cur_neweb.fetchall()

            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]

                print(s1, s2, s3, s4, s5, s6)
                cur_PROD.execute("""insert into product_template (id,categ_id,name,type,
                          uom_id,uom_po_id,purchase_line_warn,sale_line_warn,tracking,track_service,invoice_policy,purchase_method) VALUES
                         ('%s','%s','%s','%s','%s','%s','no-message','no-message','none','manual','order','receive')""" % (
                    s1, s2, s3, s4, s5, s6))
                cur_PROD.execute("commit")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence product_template_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("""select id,sale_ok,active,sale_delay,purchase_ok,serial,serial_num,maintenance_category_id,
                          specification,is_maintenance_target,brand,model from product_template where id > %d""" % int(
                myprodmaxid[0]))
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
                print(s1, s2, s3, s4, s5, s6, s7)
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
                        print("Specification NO update")
                if s10:
                    cur_PROD.execute("update product_template set is_maintenance_target='%s' where id='%s'" % (s10, s1))
                    cur_PROD.execute("commit")
                if s11:
                    cur_PROD.execute("update product_template set brand='%s' where id='%s'" % (s11, s1))
                    cur_PROD.execute("commit")
                if s12:
                    cur_PROD.execute("update product_template set model='%s' where id='%s'" % (s12, s1))
                    cur_PROD.execute("commit")
            print("product template update OK!")

            print("正式環境導入product_product")
            print('')

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
                print(s1, s2, s3)
                cur_PROD.execute(
                    "insert into product_product(id,product_tmpl_id,active) values ('%s','%s','%s')" % (s1, s2, s3))
                cur_PROD.execute("commit")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence product_product_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            cur_neweb.execute(
                "select id,default_code,name_template from product_product where id > %d" % int(myprodmaxid[0]))
            myrec1 = cur_neweb.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                print(s1, s2, s3)
                if s2:
                    try:
                        cur_PROD.execute("update product_product set default_code='%s' where id='%s'" % (s2, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("default_code no update")
                if s3:
                    try:
                        cur_PROD.execute("update product_product set name_template='%s' where id='%s'" % (s3, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("name_template no update")
            cur_PROD.execute("select migration_prod_temp()")
            cur_PROD.execute("commit")
            print("PRODUCT_PRODUCT update OK!")

            print("PROD 異動資料導入環境 ")




            cur_PROD.execute("select max(id) from res_partner")
            mymaxid = cur_PROD.fetchone()
            cur_neweb.execute("select max(id) from res_partner")
            mynewmaxid = cur_neweb.fetchone()
            cur_neweb.execute(
                "select name,email,lang,tz,supplier,is_company,customer,id from res_partner where id > %d" % int(
                    mymaxid[0]))
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
                print(s1, s2, s3, s4, s5, s6, s7)
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
                    print("NO Insert")
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
                print(s1, s2, s3, s4, s5)
                try:
                    cur_PROD.execute(sql_string)
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("NO Update")


            print("PROD 合約異動資料導入 neweb_contract_contract")
            print('')
            cur_PROD.execute("select max(id) from neweb_contract_contract")  # 目前PROD環境最大ID
            prodmaxid = cur_PROD.fetchone()
            myprodmaxid = int(prodmaxid[0])
            cur_neweb.execute("select max(id) from neweb_contract_contract")
            mymaxid = cur_neweb.fetchone()

            sql_string = """select id,daily_maintain_hour_end,daily_maintain_hour_start,is_maintenance_contract,
            inspection_warn,warranty_warn,customer_name,is_outsourcing_service,need_recovery_rehearsal,num_of_contract_lines,
            state,name,is_rental_contract,site_check,deployment,weekly_maintain_day,project_no,is_locked,project,site_check_upload,
            maintenance_warn,sla from neweb_contract_contract where id > %d""" % myprodmaxid
            cur_neweb.execute(sql_string)
            myrec1 = cur_neweb.fetchall()
            # cur_PROD.execute("delete from neweb_contract_contract")
            # cur_PROD.execute("commit")
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
                print(s1, s2, s3, s4, s5, s6, s7, s8)
                sql_string = """insert into neweb_contract_contract (id,daily_maintain_hour_end,daily_maintain_hour_start,
                is_maintenance_contract,inspection_warn,warranty_warn,is_outsourcing_service,need_recovery_rehearsal,
                num_of_contract_lines,state,name,is_rental_contract,site_check,deployment,weekly_maintain_day,project_no,
                is_locked,project,site_check_upload,maintenance_warn) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                '%s','%s','%s','%s','%s','%s','%s','%s','%s')""" \
                             % (s1, s2, s3, s4, s5, s6, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21)
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence neweb_contract_contract_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            sql_string = """select id,ae,contract_memo,warranty_end_date,cur_inspection_date,penalties,sales,recovery_rehearsal_status,
            recovery_rehearsal_datetime,maintenance_warn_days,end_customer,inspection_warn_days,maintenance_start_date,clinch_date,
            maintenance_end_date,sales_dept,warranty_start_date,recovery_rehearsal_description,inspection_date,tx_price,warranty_warn_days,
            ae_dept,contact_person,sla,customer_name from neweb_contract_contract where id > %d""" % myprodmaxid
            cur_neweb.execute(sql_string)
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
                print("Update %s %s %s %s" % (s2, s3, s4, s5))
                if s2:
                    cur_PROD.execute("update neweb_contract_contract set ae='%s' where id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
                if s3:
                    cur_PROD.execute("update neweb_contract_contract set contract_memo='%s' where id='%s'" % (s3, s1))
                    cur_PROD.execute("commit")
                if s4:
                    cur_PROD.execute("update neweb_contract_contract set warranty_end_date='%s' where id='%s'" % (s4, s1))
                    cur_PROD.execute("commit")
                if s5:
                    cur_PROD.execute("update neweb_contract_contract set cur_inspection_date='%s' where id='%s'" % (s5, s1))
                    cur_PROD.execute("commit")
                if s6:
                    cur_PROD.execute("update neweb_contract_contract set penalties='%s' where id='%s'" % (s6, s1))
                    cur_PROD.execute("commit")
                if s7:
                    cur_PROD.execute("update neweb_contract_contract set sales='%s' where id='%s'" % (s7, s1))
                    cur_PROD.execute("commit")
                if s8:
                    cur_PROD.execute(
                        "update neweb_contract_contract set recovery_rehearsal_status='%s' where id='%s'" % (s8, s1))
                    cur_PROD.execute("commit")
                if s9:
                    cur_PROD.execute(
                        "update neweb_contract_contract set recovery_rehearsal_datetime='%s' where id='%s'" % (s9, s1))
                    cur_PROD.execute("commit")
                if s10:
                    cur_PROD.execute(
                        "update neweb_contract_contract set maintenance_warn_days='%s' where id='%s'" % (s10, s1))
                    cur_PROD.execute("commit")
                if s11:
                    try:
                        cur_PROD.execute("update neweb_contract_contract set end_customer='%s' where id='%s'" % (s11, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: end_customer")

                if s12:
                    cur_PROD.execute(
                        "update neweb_contract_contract set inspection_warn_days='%s' where id='%s'" % (s12, s1))
                    cur_PROD.execute("commit")
                if s13:
                    cur_PROD.execute(
                        "update neweb_contract_contract set maintenance_start_date='%s' where id='%s'" % (s13, s1))
                    cur_PROD.execute("commit")
                if s14:
                    cur_PROD.execute("update neweb_contract_contract set clinch_date='%s' where id='%s'" % (s14, s1))
                    cur_PROD.execute("commit")
                if s15:
                    cur_PROD.execute(
                        "update neweb_contract_contract set maintenance_end_date='%s' where id='%s'" % (s15, s1))
                    cur_PROD.execute("commit")
                if s16:
                    cur_PROD.execute("update neweb_contract_contract set sales_dept='%s' where id='%s'" % (s16, s1))
                    cur_PROD.execute("commit")
                if s17:
                    cur_PROD.execute(
                        "update neweb_contract_contract set warranty_start_date='%s' where id='%s'" % (s17, s1))
                    cur_PROD.execute("commit")
                if s18:
                    cur_PROD.execute(
                        "update neweb_contract_contract set recovery_rehearsal_description='%s' where id='%s'" % (s18, s1))
                    cur_PROD.execute("commit")
                if s19:
                    cur_PROD.execute("update neweb_contract_contract set inspection_date='%s' where id='%s'" % (s19, s1))
                    cur_PROD.execute("commit")
                if s20:
                    cur_PROD.execute("update neweb_contract_contract set tx_price='%s' where id='%s'" % (s20, s1))
                    cur_PROD.execute("commit")
                if s21:
                    cur_PROD.execute("update neweb_contract_contract set warranty_warn_days='%s' where id='%s'" % (s21, s1))
                    cur_PROD.execute("commit")
                if s22:
                    cur_PROD.execute("update neweb_contract_contract set ae_dept='%s' where id='%s'" % (s22, s1))
                    cur_PROD.execute("commit")
                if s23:
                    cur_PROD.execute("update neweb_contract_contract set contact_person='%s' where id='%s'" % (s23, s1))
                    cur_PROD.execute("commit")
                if s24:
                    cur_PROD.execute("update neweb_contract_contract set sla='%s' where id='%s'" % (s24, s1))
                    cur_PROD.execute("commit")
                if s25:
                    try:
                        cur_PROD.execute("update neweb_contract_contract set customer_name='%s' where id='%s'" % (s25, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: customer_name")
                cur_PROD.execute(
                    "update neweb_contract_contract set daily_maintain_hour_start='16' where daily_maintain_hour_start='None'")
                cur_PROD.execute(
                    "update neweb_contract_contract set daily_maintain_hour_end='38' where daily_maintain_hour_end='None'")
                cur_PROD.execute(
                    "update neweb_contract_contract set weekly_maintain_day='1' where weekly_maintain_day='None'")
                cur_PROD.execute("commit")
                cur_PROD.execute("select migration_contract_ae();")
                cur_PROD.execute("commit")



    def serviceadd_migration(self):
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
            print("正式環境更新 Inspection_method")
            print('')

            cur_neweb.execute("select id,inspection_method from neweb_contract_contract")
            myinspection = cur_neweb.fetchall()
            for line in myinspection:
                s1 = line[0]
                s2 = line[1]
                print("%s %s" % (s1, s2))
                if s2:
                    cur_PROD.execute(
                        """update neweb_contract_contract set inspection_method='%s' where id=%d """ % (s2, s1))
                    cur_PROD.execute("commit")

            print("Inspection_method update complete")
            print("")
            cur_PROD.execute("""delete from neweb_base_value_added_service_neweb_contract_contract_rel""")
            cur_PROD.execute("commit")
            cur_neweb.execute("""select * from neweb_base_value_added_service_neweb_contract_contract_rel""")
            myserviceadd = cur_neweb.fetchall()
            for line in myserviceadd:
                s1 = line[0]
                s2 = line[1]
                print("%s %s" % (s1, s2))
                try:
                    cur_PROD.execute(
                        """insert into neweb_base_value_added_service_neweb_contract_contract_rel VALUES (%d,%d)""" % (
                        s1, s2))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No insert service added")

            print("Service Added insert Compete")
            cur_PROD.close()
            cur_neweb.close()

    def calendar_migration(self):
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
            print("NEWEB calendar event migration")
            print('')


            print("Calendar Attendee Migration")
            print("")
            cur_neweb.execute("select max(id) from calendar_attendee")
            maxid = cur_neweb.fetchone()
            cur_neweb.execute("""select id,create_uid,create_date,cn,access_token,event_id,state,email,
                                    write_date,write_uid,partner_id,availability,google_internal_event_id,
                                    oe_synchro_date from calendar_attendee where create_date >= '2018-01-01' """)

            myattendee = cur_neweb.fetchall()
            for line in myattendee:
                s1 = line[0]
                s2 = line[1]  # create_uid
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]
                s7 = line[6]
                s8 = line[7]
                s9 = line[8]
                s10 = line[9]  # write_uid
                s11 = line[10]
                s12 = line[11]
                s13 = line[12]
                s14 = line[13]

                print("%s %s" % (s1, s4))
                try:
                    cur_PROD.execute("""insert into calendar_attendee (id,create_date,common_name,
                          access_token,event_id,state,email,write_date)
                           values (%s,'%s','%s','%s',%s,'%s','%s','%s')""" % (s1, s3, s4, s5, s6, s7, s8, s9))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No insert calendar addtenee")

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
                        print("No update partner_id:")

                if not s12:
                    try:
                        cur_PROD.execute("""update calendar_attendee set availability=%s where id=%s""" % (s12, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("No update availability:")
                if not s13:
                    try:
                        cur_PROD.execute(
                            """update calendar_attendee set google_internal_event_id='%s' where id=%s""" % (s13, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("No update google_internal_event_id:")
                if not s14:
                    try:
                        cur_PROD.execute("""update calendar_attendee set oe_synchro_date='%s' where id=%s""" % (s14, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("No update oe_synchro_date:")

                if not s2:
                    try:
                        cur_PROD.execute("""update calendar_attendee set create_uid=%s where id=%s""" % (s2, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("No update create_uid")
                if not s10:
                    try:
                        cur_PROD.execute("""update calendar_attendee set write_uid=%s where id=%s""" % (s10, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("No update write_uid")

            mymaxid1 = int(maxid[0]) + 1
            cur_PROD.execute("alter sequence calendar_attendee_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("Calendar Alarm Migration")
            print("")
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

                print("%s %s" % (s1, s4))
                try:
                    cur_PROD.execute("""insert into calendar_alarm (id,create_date,name,
                                          interval,duration_minutes,write_date,duration,type)
                                           values (%s,%s,'%s',%s,%s,%s,%s,%s)""" % (
                        s1, s3, s4, s5, s7, s8, s9, s10))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No insert calendar alarm")

            mymaxid1 = int(maxid[0]) + 1
            cur_PROD.execute("alter sequence calendar_alarm_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("insert calendar_alarm_calendar_event_rel")
            print("")

            cur_PROD.execute("select max(calendar_event_id) from calendar_alarm_calendar_event_rel")
            mymaxeventid = cur_PROD.fetchone()
            try:
                mymaxeventid1 = int(mymaxeventid[0])
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
                                    values (%d,%d)""" % (s1, s2))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print("No insert calendar_alarm_calendar_event_rel")

            print("insert calendar_event_res_partner_rel")
            print("")

            cur_PROD.execute("select max(calendar_event_id) from calendar_event_res_partner_rel")
            mymaxeventid = cur_PROD.fetchone()
            try:
                mymaxeventid1 = int(mymaxeventid[0])
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
                    print("No insert calendar_event_res_partner_rel")



    def repair_carecalldate(self):
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
            # print u"NEWEB 正式環境calendar event migration"
            # print ''
            cur_PROD.execute("select distinct repair_id from neweb_repair_repair_care_call_log ")
            myrec = cur_PROD.fetchall()
            for line in myrec:
                s1 = line[0]
                cur_PROD.execute("select get_carecalldate(%d)" % s1)
                cur_PROD.execute("commit")
            print("Care Call Date Update Complete")





