# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationprojwizard(models.TransientModel):
    _name = "neweb_migration.project_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    # def proj1_migration(self):
    #     self.env.cr.execute("""select dblink_connect('NEWEB','hostaddr=localhost port=5432 dbname=NEWEB user=postgres password=postgres')""")
    #     self.env.cr.execute("""select dblink_exec('NEWEB','BEGIN')""")
    #     self.env.cr.execute(""" select dblink_exec('')""")
    #     if self.passcode=='!99999ibm':
    #         view = self.env.ref('sh_message.sh_message_wizard')
    #         view_id = view and view.id or False
    #         context = dict(self._context or {})
    #         context['message'] = 'neweb.setup_desc_item Migration OK！'
    #         return {
    #             'name': '系統通知訊息',
    #             'type': 'ir.actions.act_window',
    #             'view_type': 'form',
    #             'view_mode': 'form',
    #             'res_model': 'sh.message.wizard',
    #             'views': [(view.id, 'form')],
    #             'view_id': view.id,
    #             'target': 'new',
    #             'context': context,
    #         }
    #     else:
    #     view = self.env.ref('sh_message.sh_message_wizard')
    #     view_id = view and view.id or False
    #     context = dict(self._context or {})
    #     context['message'] = 'PASSCODE 錯誤！'
    #     return {
    #         'name': '系統通知訊息',
    #         'type': 'ir.actions.act_window',
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'sh.message.wizard',
    #         'views': [(view.id, 'form')],
    #         'view_id': view.id,
    #         'target': 'new',
    #         'context': context,
    #     }



    def project1_migration(self):
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
            print("正式環境導入<1>.neweb_setup_desc_item")
            print('')
            cur_neweb.execute("select max(id) from neweb_setup_desc_item")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_setup_desc_item")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_setup_desc_item")
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
                cur_PROD.execute("""insert into neweb_setup_desc_item(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (1,'neweb.setup_desc_item',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_setup_desc_item_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb.setup_desc_item Migration OK！'
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


    def project2_migration(self):
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
            print("正式環境導入<2>.neweb_setup_attach")
            print('')
            cur_neweb.execute("select max(id) from neweb_setup_attach")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_setup_attach")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_setup_attach")
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
                cur_PROD.execute("""insert into neweb_setup_attach(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (2,'neweb.setup_attach',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_setup_attach_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb.setup_attach Migration OK！'
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

    def project3_migration(self):
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
            print("正式環境導入<3>.neweb_ass_service_mode")
            print('')
            cur_neweb.execute("select max(id) from neweb_ass_service_mode")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_ass_service_mode")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_ass_service_mode")
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
                cur_PROD.execute("""insert into neweb_ass_service_mode(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (3,'neweb.ass_service_mode',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_ass_service_mode_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb.ass_service_mode Migration OK！'
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

    def project8_migration(self):
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
            print("正式環境導入<8>.neweb_export_excel_download")
            print('')
            cur_neweb.execute("select max(id) from neweb_export_excel_download")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_export_excel_download")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_export_excel_download")
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
                cur_PROD.execute("""insert into neweb_export_excel_download(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (8,'neweb.export_excel_download',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_export_excel_download_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_export_excel_download Migration OK！'
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

    def project9_migration(self):
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
            print("正式環境導入<9>.neweb_import_excel_download")
            print('')
            cur_neweb.execute("select max(id) from neweb_import_excel_download")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select * from neweb_import_excel_download")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_import_excel_download")
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
                cur_PROD.execute("""insert into neweb_import_excel_download(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (9,'neweb.import_excel_download',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_import_excel_download_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_import_excel_download Migration OK！'
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

    def project10_migration(self):
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
            print("正式環境導入<10>.neweb_proj_gencode")
            print('')
            cur_neweb.execute("select max(id) from neweb_proj_gencode")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select *  from neweb_proj_gencode")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_proj_gencode")
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
                cur_PROD.execute("""insert into neweb_proj_gencode(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (10,'neweb.proj_gencode',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_proj_gencode_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_neweb_proj_gencode Migration OK！'
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
    def project11_migration(self):
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
            print("正式環境導入<11>.neweb_buscate")
            print('')
            cur_neweb.execute("select max(id) from neweb_buscate")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select  * from neweb_buscate")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_buscate")
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
                cur_PROD.execute("""insert into neweb_buscate(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (11,'neweb.buscate',num,num,'neweb_project'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_buscate_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_buscate Migration OK！'
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