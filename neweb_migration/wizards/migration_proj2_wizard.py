# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationproj2wizard(models.TransientModel):
    _name = "neweb_migration.project2_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def project12_migration(self):
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
            print("正式環境導入(12).neweb_transationtype")
            print('')
            cur_neweb.execute("select max(id) from neweb_transationtype")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_transationtype")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_transationtype")
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
                cur_PROD.execute("""insert into neweb_transationtype(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (12,'neweb.transationtype',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_transationtype_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_transationtype Migration OK！'
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


    def project13_migration(self):
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
            print("正式環境導入(13).neweb_contacttype")
            print('')
            cur_neweb.execute("select max(id) from neweb_contacttype")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_contacttype")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_contacttype")
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
                cur_PROD.execute("""insert into neweb_contacttype(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (13,'neweb.contacttype',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_contacttype_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_contacttype Migration OK！'
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

    def project14_migration(self):
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
            print("正式環境導入(14).neweb_prodbrand")
            print('')
            cur_neweb.execute("select max(id) from neweb_prodbrand")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_prodbrand")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_prodbrand")
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
                cur_PROD.execute("""insert into neweb_prodbrand(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (14,'neweb.prodbrand',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_prodbrand_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb.prodbrand Migration OK！'
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

    def project15_migration(self):
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
            print("正式環境導入(15).neweb.proj_select")
            print('')
            cur_neweb.execute("select max(id) from neweb_proj_select")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_proj_select")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_proj_select")
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
                cur_PROD.execute("""insert into neweb_proj_select(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (15,'neweb.proj_select',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_proj_select_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_proj_select Migration OK！'
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

    def project19_migration(self):
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
            print("正式環境導入(19).neweb_prodset")
            print('')
            cur_neweb.execute("select max(id) from neweb_prodset")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_prodset")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_prodset")
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
                cur_PROD.execute("""insert into neweb_prodset(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (19,'neweb.prodset',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_prodset_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_prodset Migration OK！'
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

    def project20_migration(self):
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
            print("正式環境導入(20).neweb_projmaintype")
            print('')
            cur_neweb.execute("select max(id) from neweb_projmaintype")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_projmaintype")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_projmaintype")
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
                cur_PROD.execute("""insert into neweb_projmaintype(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (20,'neweb.projmaintype',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_projmaintype_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_projmaintype Migration OK！'
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

    def project21_migration(self):
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
            print("正式環境導入(21).neweb_engmaintype")
            print('')
            cur_neweb.execute("select max(id) from neweb_engmaintype")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_engmaintype")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_engmaintype")
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
                cur_PROD.execute("""insert into neweb_engmaintype(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (21,'neweb.engmaintype',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_engmaintype_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_engmaintype Migration OK！'
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