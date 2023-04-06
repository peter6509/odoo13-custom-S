# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationproj3wizard(models.TransientModel):
    _name = "neweb_migration.project3_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def project22_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(22).neweb_projbranch")
            print('')
            cur_neweb.execute("select max(id) from neweb_projbranch")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_projbranch")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_projbranch")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_projbranch(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (22,'neweb.projbranch',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_projbranch_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_projbranch Migration OK！'
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


    def project23_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(23).neweb_costtype")
            print('')
            cur_neweb.execute("select max(id) from neweb_costtype")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_costtype")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_costtype")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_costtype(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (23,'neweb.costtype',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_costtype_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_costtype Migration OK！'
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

    def project27_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(27).neweb_warranty_service_rule")
            print('')
            cur_neweb.execute("select max(id) from neweb_warranty_service_rule")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_warranty_service_rule")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_warranty_service_rule")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_warranty_service_ruled(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (27,'neweb.warranty_service_rule',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_warranty_service_rule_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_warranty_service_rule Migration OK！'
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

    def project28_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(28).neweb_payment_term_rule")
            print('')
            cur_neweb.execute("select max(id) from neweb_payment_term_rule")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_payment_term_rule")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_payment_term_rule")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_payment_term_rule(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (28,'neweb.payment_term_rule',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_payment_term_rule_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_payment_term_rule Migration OK！'
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

    def project29_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(29).neweb_main_service_rule")
            print('')
            cur_neweb.execute("select max(id) from neweb_main_service_rule")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_main_service_rule")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_main_service_rule")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_main_service_rule(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (29,'neweb.main_service_rule',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_main_service_rule_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_main_service_rule Migration OK！'
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

    def project30_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(30).neweb_routine_maintenance")
            print('')
            cur_neweb.execute("select max(id) from neweb_routine_maintenance")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_routine_maintenance")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_routine_maintenance")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_routine_maintenance(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (30,'neweb.routine_maintenance',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_routine_maintenance_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_routine_maintenance Migration OK！'
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

    def project33_migration(self):
        if self.passcode=='!99999ibm':
            myrec = self.env['neweb_migration.config'].search([])
            SOURCE_IP = myrec.SOURCE_IP
            DB_NAME = myrec.DB_NAME
            USER_NAME = myrec.USER_NAME
            PASSWORD = myrec.PASSWORD
            conn1_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP,DB_NAME,USER_NAME,PASSWORD)
            conn_neweb = psycopg2.connect(conn1_string)
            cur_neweb = conn_neweb.cursor()
            conn_PROD = psycopg2.connect(database='PROD', user='odoo')
            cur_PROD = conn_PROD.cursor()
            print("正式環境導入(33).neweb_salenocheck")
            print('')
            cur_neweb.execute("select max(id) from neweb_salenocheck")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_salenocheck")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_salenocheck")
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
                print(s1,s2,s3,s4,s5,s6)
                cur_PROD.execute("""insert into neweb_salenocheck(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (33,'neweb.salenocheck',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_salenocheck_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_salenocheck Migration OK！'
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