# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationbase2wizard(models.TransientModel):
    _name = "neweb_migration.base2_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def product_migration(self):
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
            print ("正式環境導入(10).neweb_base_maintenance_category")
            print ('')
            cur_neweb.execute("select max(id) from neweb_base_maintenance_category")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,name,product_attr,disabled from neweb_base_maintenance_category")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_repair_repair_part")
            cur_PROD.execute("commit")
            cur_PROD.execute("delete from neweb_base_problem_solution")
            cur_PROD.execute("commit")
            cur_PROD.execute("delete from neweb_base_problem")
            cur_PROD.execute("commit")
            cur_PROD.execute("delete from neweb_base_maintenance_category")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                s4=line[3]
                print (s1,s2,s3,s4)
                try :
                    cur_PROD.execute("insert into neweb_base_maintenance_category(id,name,product_attr,disabled) values ('%s','%s','%s',%s)" %
                                      (s1, s2, s3, s4))
                    cur_PROD.execute("commit")
                except Exception as inst:
                    print (" default_code no update")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (10, 'neweb_base.maintenance_category', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_base_maintenance_category_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")


            print ("正式環境導入(11).product_template")
            print ('')
            cur_neweb.execute("select max(id) from product_template")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,categ_id,name,type,uom_id,uom_po_id from product_template where id > 2")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from stock_move")
            cur_PROD.execute("commit")
            cur_PROD.execute("delete from stock_inventory_line")
            cur_PROD.execute("commit")
            cur_PROD.execute("delete from product_template where id > 2")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                s4=line[3]
                s5=line[4]
                s6=line[5]

                print (s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into product_template (id,categ_id,name,type,
                   uom_id,uom_po_id,purchase_line_warn,sale_line_warn,tracking,track_service,invoice_policy,purchase_method) VALUES
                  ('%s','%s','%s','%s','%s','%s','no-message','no-message','none','manual','order','receive')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (11, 'product.template', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence product_template_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("""select id,sale_ok,active,sale_delay,purchase_ok,serial,serial_num,maintenance_category_id,
                   specification,is_maintenance_target,brand,model from product_template where id > 2""")
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
                print (s1,s2,s3,s4,s5,s6,s7)
                if s2:
                   cur_PROD.execute("update product_template set sale_ok='%s' where id='%s'" % (s2,s1))
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

            print ("正式環境導入(12).product_product")
            print ('')

            cur_neweb.execute("select max(id) from product_product")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,product_tmpl_id,active from product_product where id > 2")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from product_product where id > 2")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                print (s1,s2,s3)
                cur_PROD.execute("insert into product_product(id,product_tmpl_id,active) values ('%s','%s','%s')" % (s1,s2,s3))
                cur_PROD.execute("commit")

            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (12, 'product.product', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence product_product_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            cur_neweb.execute("select id,default_code,name_template from product_product where id>2")
            myrec1=cur_neweb.fetchall()
            for line in myrec1:
                s1=line[0]
                s2=line[1]
                s3=line[2]
                print (s1,s2,s3)
                if s2:
                   try:
                      cur_PROD.execute("update product_product set default_code='%s' where id='%s'" % (s2,s1))
                      cur_PROD.execute("commit")
                   except Exception as inst:
                      print (" default_code no update")
                if s3:
                   try:
                      cur_PROD.execute("update product_product set name_template='%s' where id='%s'" %(s3,s1))
                      cur_PROD.execute("commit")
                   except Exception as inst:
                      print ("name_template no update")
            cur_PROD.execute("select migration_prod_temp()")
            cur_PROD.execute("commit")
            print ("PRODUCT_PRODUCT update OK!")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'PRODUCT Migration ok！'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }
        else:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'PASSCODE 錯誤！'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }

    def contract_migration(self):
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
            print ("正式環境導入(13).neweb_contract_contract")
            print ('')
            cur_neweb.execute("select max(id) from neweb_contract_contract")
            mymaxid = cur_neweb.fetchone()
            sql_string="""select id,daily_maintain_hour_end,daily_maintain_hour_start,is_maintenance_contract,
            inspection_warn,warranty_warn,customer_name,is_outsourcing_service,need_recovery_rehearsal,num_of_contract_lines,
            state,name,is_rental_contract,site_check,deployment,weekly_maintain_day,project_no,is_locked,project,site_check_upload,
            maintenance_warn,sla from neweb_contract_contract"""
            cur_neweb.execute(sql_string)
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_contract_contract")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
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
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (13, 'neweb_contract.contract', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_contract_contract_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            sql_string="""select id,ae,contract_memo,warranty_end_date,cur_inspection_date,penalties,sales,recovery_rehearsal_status,
            recovery_rehearsal_datetime,maintenance_warn_days,end_customer,inspection_warn_days,maintenance_start_date,clinch_date,
            maintenance_end_date,sales_dept,warranty_start_date,recovery_rehearsal_description,inspection_date,tx_price,warranty_warn_days,
            ae_dept,contact_person,sla,customer_name from neweb_contract_contract"""
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

                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = 'neweb_contract.contract migration ok'
                return {
                    'name': '系統通知訊息',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context,
                }
        else:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'PASSCODE 錯誤！'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }


    def contract_line_migration(self):
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
            print("正式環境導入(14).neweb_contract_contract_line")
            print('')

            cur_neweb.execute("select max(id) from neweb_contract_contract_line")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute(
                "select id,contract_id,sequence,machine_serial_no,special_warn,x_locked,prod,special_warn_days from neweb_contract_contract_line")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_contract_contract_line")
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
                s7 = line[6]
                s8 = line[7]
                print(s1, s2, s3, s4, s5, s6, s7, s8)
                cur_PROD.execute("""insert into neweb_contract_contract_line(id,sequence,machine_serial_no,special_warn,x_locked,prod)
                                     values ('%s','%s','%s','%s','%s','%s')""" % (s1, s3, s4, s5, s6, s7))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (14, 'neweb_contract.contract_line', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence neweb_contract_contract_line_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute(
                "select id,special_warn_date,maintain_partner,memo,prod_sla,special_warn_days,contract_id from neweb_contract_contract_line")
            myrec1 = cur_neweb.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                s5 = line[4]
                s6 = line[5]
                s7 = line[6]
                print("update %s %s %s %s %s" % (s1, s2, s3, s4, s5))
                if s2:
                    try:
                        cur_PROD.execute(
                            "update neweb_contract_contract_line set special_warn_date='%s' where id='%s'" % (s2, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: special_warn_date")
                if s3:
                    try:
                        cur_PROD.execute(
                            "update neweb_contract_contract_line set maintain_partner='%s' where id='%s'" % (s3, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: maintain_partner")
                if s4:
                    try:
                        cur_PROD.execute("update neweb_contract_contract_line set memo='%s' where id='%s'" % (s4, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: memo")
                if s5:
                    try:
                        cur_PROD.execute("update neweb_contract_contract_line set prod_sla='%s' where id='%s'" % (s5, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: prod_sla")
                if s6:
                    try:
                        cur_PROD.execute(
                            "update neweb_contract_contract_line set special_warn_days='%s' where id='%s'" % (s6, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: special_warn_days")
                if s7:
                    try:
                        cur_PROD.execute(
                            "update neweb_contract_contract_line set contract_id='%s' where id='%s'" % (s7, s1))
                        cur_PROD.execute("commit")
                    except Exception as inst:
                        print("NO Update: contract_id")

            print("Neweb_contract_contract_line complete")

            cur_PROD.execute("select id,sla,maintenance_start_date,maintenance_end_date from neweb_contract_contract")
            myrec1 = cur_PROD.fetchall()
            for line in myrec1:
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                print(s1, s2, s3, s4)
                if s2:
                    cur_PROD.execute(
                        "update neweb_contract_contract_line set prod_sla='%s' where contract_id='%s'" % (s2, s1))
                    cur_PROD.execute("commit")
                if s3 and s4:
                    cur_PROD.execute(
                        "update neweb_contract_contract_line set contract_start_date='%s',contract_end_date='%s' where contract_id='%s'" % (
                        s3, s4, s1))
                    cur_PROD.execute("commit")
            print("Neweb_contract sla,main_start_date,main_end_date update complete")
            cur_PROD.execute("select migration_contract_line()")
            cur_PROD.execute("commit")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_contract.contract_line migration ok'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }
        else:
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'PASSCODE 錯誤！'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context,
            }
