# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
import psycopg2,sys
from odoo.exceptions import  UserError

class migrationbasewizard(models.TransientModel):
    _name = "neweb_migration.base_wizard"

    passcode = fields.Char(string="PASSCODE",required=True)

    def sla_migration(self):
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
            print("正式環境導入(1).neweb_base.sla")
            print('')
            cur_neweb.execute("select max(id) from neweb_base_sla")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,disabled,maintenance_time,name,onsite_time,response_time from neweb_base_sla")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_base_sla")
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
                cur_PROD.execute("""insert into neweb_base_sla(id,disabled,maintenance_time,name,onsite_time,response_time)
                     values ('%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (1,'neweb_base.sla',num,num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 =  int(mymaxid[0])+1
            cur_PROD.execute("alter sequence neweb_base_sla_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_base.sla Migration OK！'
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

    def value_add_service_migration(self):
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
            print("正式環境導入(2).neweb_base.value_added_service")
            print('')
            cur_neweb.execute("select max(id) from neweb_base_value_added_service")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,name,disabled,content from neweb_base_value_added_service")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from neweb_base_value_added_service")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                s3 = line[2]
                s4 = line[3]
                print(s1, s2, s3, s4)
                sql_string = """insert into neweb_base_value_added_service(id,name,disabled,content)
                               values ('%s','%s','%s','%s')""" % (s1, s2, s3, s4)
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (2, 'neweb_base.value_added_service', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence neweb_base_value_added_service_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'neweb_base.value_added_service migration ok'
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

    def hr_department_migration(self):
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
            print("正式環境導入(3).HR_DEPARTMENT")
            print('')
            cur_neweb.execute("select max(id) from hr_department")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,name,parent_id from hr_department")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from hr_department")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                print(s1, s2)
                sql_string = """insert into hr_department(id,name,active)
                                    values ('%s','%s','1')""" % (s1, s2)
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            for line in myrec1:
                s1=line[0]
                s2=line[2]
                if s2:
                   cur_PROD.execute("update hr_department set parent_id='%s' where id='%s'" %(s2,s1))
                   cur_PROD.execute("commit")

            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (3, 'hr.department', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0])+1
            cur_PROD.execute("alter sequence hr_department_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'hr.department migration ok'
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

    def res_partner_migration(self):
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
            print("正式環境導入(4).RES_PARTNER_TITLE")
            print('')
            cur_PROD.execute("delete from res_partner_title where id > 6")
            cur_PROD.execute("commit")
            cur_neweb.execute("select max(id) from res_partner_title")
            mymaxid=cur_neweb.fetchone()
            cur_neweb.execute("select id,name,shortcut from res_partner_title where id > 6")
            myrec1=cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                if not s3:
                   s3='-'
                cur_PROD.execute("insert into res_partner_title(id,name,shortcut) values ('%s','%s','%s')" % (s1,s2,s3) )
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (4, 'res.partner.title', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0])+1
            cur_PROD.execute("alter sequence res_partner_title_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print("正式環境導入res.partner")
            print('')
            # cur_PROD.execute("delete from res_partner where id > 6")
            # cur_PROD.execute("commit")
            cur_neweb.execute("select max(id) from res_partner")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select name,email,lang,tz,supplier,is_company,customer,id from res_partner where id > 6")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                 num = num + 1
                 s1 = line[0]
                 s2 = line[1]
                 if not s2:
                    s2 = '-'
                 s3 = line[2]
                 if not s3:
                    s3='zh_TW'
                 s4 = line[3]
                 if not s4 :
                    s4 = 'Asia/Taipei'
                 s5 = line[4]
                 s6 = line[5]
                 s7 = line[6]
                 s8 = line[7]
                 print (s1,s2,s3,s4,s5,s6,s7)
                 if s5 and s6 and s7 :
                    sql_string="insert into res_partner(name,email,lang,tz,active,supplier,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                            "values ('%s',%s,'%s','%s','1','%s','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (s1,s2,s3,s4,s5,s6,s7,s1,s8)
                 elif s5 and s6 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s5, s6, s1,s8)
                 elif s5 and s7 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s5, s7, s1,s8)
                 elif s6 and s7 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s6, s7, s1,s8)
                 elif s5 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,supplier,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s5, s1,s8)
                 elif s6 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,is_company,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s6, s1,s8)
                 elif s7 :
                    sql_string = "insert into res_partner(name,email,lang,tz,active,customer,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','%s','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s7, s1,s8)
                 else:
                    sql_string = "insert into res_partner(name,email,lang,tz,active,notify_email,invoice_warn,sale_warn,picking_warn,purchase_warn,display_name,id) " \
                                  "values ('%s','%s','%s','%s','1','always','no-message','no-message','no-message','no-message','%s','%s')" % (
                                  s1, s2, s3, s4, s1,s8)
                 try :
                    cur_PROD.execute(sql_string)
                    cur_PROD.execute("commit")
                 except Exception as inst:
                     print("NO Insert")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (5, 'res.partner', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0])+1
            cur_PROD.execute("alter sequence res_partner_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_PROD.execute("update res_partner set company_id='1'")
            cur_PROD.execute("commit")

            cur_neweb.execute("""select id,street,zip,function,phone,mobile,fax,title,
                                         parent_id,use_parent_address,vat,commercial_partner_id,
                                         company_type,color,comment,website,type,employee
                                        from res_partner where id >6""")
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

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'res.partner migration ok!'
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
                'context': context,}

    def res_users_migration(self):
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
            # print "NEWEB 正式環境導入 MAIL_ALIAS"
            # print ''
            # cur_neweb.execute("select max(id) from mail_alias")
            # mymaxid = cur_neweb.fetchone()
            # cur_neweb.execute("select id,alias_model_id from mail_alias where id > 1")
            # myrec1 = cur_neweb.fetchall()
            # cur_PROD.execute("delete from mail_alias where id > 1")
            # cur_PROD.execute("commit")
            # for line in myrec1:
            #     s1=line[0]
            #     s2=line[1]
            #     print s1,s2
            #     cur_PROD.execute("""insert into mail_alias(id,alias_contact,alias_defaults,alias_model_id)
            #           values ('%s','everyone','{}','%s')""" % (s1,s2))
            #     cur_PROD.execute("commit")
            # mymaxid1 = int(mymaxid[0])+1
            # cur_PROD.execute("alter sequence mail_alias_id_seq restart with %d" % mymaxid1)
            # cur_PROD.execute("commit")

            print("正式環境導入(6).RES_USERS")
            print ('')
            cur_neweb.execute("select max(id) from res_users")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,active,login,partner_id,alias_id,google_calendar_cal_id,google_calendar_rtoken,google_calendar_token from res_users where id > 10")
            myrec1 = cur_neweb.fetchall()
            cur_PROD.execute("delete from res_users where id > 10")
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
                if not s6:
                   s6='-'
                s7=line[6]
                if not s7:
                   s7='-'
                s8=line[7]
                if not s8:
                   s8='-'
                print (s1,s2,s3,s4,s5,s6,s7,s8)
                # if not s5:
                sql_string="""insert into res_users(id,active,login,partner_id,google_calendar_cal_id,google_calendar_rtoken,google_calendar_token,company_id)
                    values ('%s','%s','%s','%s','%s','%s','%s','1')""" % (s1,s2,s3,s4,s6,s7,s8)
                # else:
                #    sql_string = """insert into res_users(id,active,login,partner_id,alias_id,google_calendar_cal_id,google_calendar_rtoken,google_calendar_token,company_id)
                #     values ('%s','%s','%s','%s','%s','%s','%s','%s','1')""" % (s1, s2, s3, s4,s5, s6, s7, s8)

                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (6, 'res.users', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0])+1
            cur_PROD.execute("alter sequence res_users_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_PROD.execute("update res_users set password='!999ibm',password_crypt='HASH' where id > 10")
            cur_PROD.execute("commit")
            cur_neweb.execute("select id,user_id from res_partner")
            myrec1=cur_neweb.fetchall()
            for line in myrec1:
                s1=line[0]
                s2=line[1]
                if s2:
                   cur_PROD.execute("update res_partner set user_id='%s' where id='%s'" % (s2,s1))
                   cur_PROD.execute("commit")
            cur_PROD.execute("delete from resource_resource")
            cur_PROD.execute("commit")
            cur_neweb.execute("select max(id) from resource_resource")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,time_efficiency,user_id,name,company_id,active,resource_type from resource_resource")
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
                if s3:
                   cur_PROD.execute("""insert into resource_resource (id,time_efficiency,user_id,name,
                                     company_id,active,resource_type) values('%s','%s','%s','%s','%s','%s','%s') """ %
                                     (s1,s2,s3,s4,s5,s6,s7))
                   cur_PROD.execute("commit")
                else:
                   cur_PROD.execute("""insert into resource_resource (id,time_efficiency,name,
                                                     company_id,active,resource_type) values('%s','%s','%s','%s','%s','%s') """ %
                                      (s1, s2, s4, s5, s6, s7))
                   cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (7, 'resource.resource', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1 = int(mymaxid[0]) + 1
            cur_PROD.execute("alter sequence resource_resource_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            view = self.env.ref('sh_message.sh_message_wizard')
            view_id = view and view.id or False
            context = dict(self._context or {})
            context['message'] = 'res.users migration ok!'
            return {
                'name': '系統通知訊息',
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sh.message.wizard',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'context': context, }
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
                'context': context, }

    def hr_employee_migration(self):
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
            # print ("正式環境導入resource.resource")
            # print ('')

            # cur_neweb.execute("select max(id) from resource_resource")
            # mymaxid = cur_neweb.fetchone()
            # cur_neweb.execute("select id,name,resource_type,time_efficiency,active from resource_resource")
            # myrec1=cur_neweb.fetchall()
            # cur_PROD.execute("delete from resource_resource")
            # cur_PROD.execute("commit")
            # for line in myrec1:
            #     s1=line[0]
            #     s2=line[1]
            #     s3=line[2]
            #     s4=line[3]
            #     s5=line[4]
            #     print s1,s2,s3,s4,s5
            #     sql_string="""insert into resource_resource(id,name,resource_type,time_efficiency,active) VALUES
            #           ('%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5)
            #     cur_PROD.execute(sql_string)
            #     cur_PROD.execute("commit")
            # mymaxid1 = int(mymaxid[0])+1
            # cur_PROD.execute("alter sequence resource_resource_id_seq restart with %d" % mymaxid1)
            # cur_PROD.execute("commit")

            print ("正式環境導入(8).hr.job")
            print ('')
            cur_neweb.execute("select max(id) from hr_job")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("select id,description,name,expected_employees,state,no_of_recruitment,no_of_employee,department_id from hr_job")
            myrec1=cur_neweb.fetchall()
            cur_PROD.execute("delete from hr_job")
            cur_PROD.execute("commit")
            num = 0
            for line in myrec1:
                num = num + 1
                s1 = line[0]
                s2 = line[1]
                if not s2:
                   s2='-'
                s3 = line[2]
                s4 = line[3]
                if not s4:
                   s4=0
                s5 = line[4]
                s6 = line[5]
                if not s6:
                   s6=0
                s7 = line[6]
                if not s7:
                   s7=0
                s8 = line[7]
                print (s1,s2,s3,s4,s5,s6,s7,s8)
                if not s8:
                   sql_string="""insert into hr_job(id,description,name,expected_employees,state,no_of_recruitment,no_of_employee) VALUES
                       ('%s','%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6,s7)
                else:
                   sql_string = """insert into hr_job(id,description,name,expected_employees,state,no_of_recruitment,no_of_employee) VALUES
                                       ('%s','%s','%s','%s','%s','%s','%s')""" % (s1, s2, s3, s4, s5, s6, s7)
                cur_PROD.execute(sql_string)
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (8, 'hr.job', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence hr_job_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")

            print ("正式環境導入(9).hr.employee")
            print ('')

            cur_neweb.execute("select max(id) from hr_employee")
            mymaxid = cur_neweb.fetchone()
            cur_neweb.execute("""select id,resource_id,work_phone,mobile_phone,work_email,work_location,gender,employee_num from hr_employee""")
            cur_PROD.execute("delete from hr_employee")
            cur_PROD.execute("commit")
            myrec1 = cur_neweb.fetchall()
            num = 0
            for line in myrec1:
                num = num + 1
                s1=line[0]
                s2=line[1]
                s3=line[2]
                if not s3:
                   s3='-'
                s4=line[3]
                if not s4:
                   s4='-'
                s5=line[4]
                if not s5:
                   s5='-'
                s6=line[5]
                if not s6:
                   s6='-'
                s7=line[6]
                if not s7:
                   s7='-'
                s8=line[7]
                if not s8:
                   s8='-'
                print (s1,s2,s3,s4,s5,s6,s7,s8)
                cur_PROD.execute("""insert into hr_employee (id,resource_id,
                          work_phone,mobile_phone,work_email,work_location,gender,employee_num) values
                    ('%s','%s','%s','%s','%s','%s','%s','%s')""" % (s1,s2,s3,s4,s5,s6,s7,s8))
                cur_PROD.execute("commit")
            cur_PROD.execute("""select genmigrationdata(%d,'%s',%d,%d,'%s')""" % (9, 'hr.employee', num, num,'neweb_base'))
            cur_PROD.execute("""commit""")
            mymaxid1=int(mymaxid[0])+1
            cur_PROD.execute("alter sequence hr_employee_id_seq restart with %d" % mymaxid1)
            cur_PROD.execute("commit")
            cur_neweb.execute("select id,address_id,coach_id,job_id,country_id,parent_id,department_id from hr_employee")
            myrec1=cur_neweb.fetchall()
            for line in myrec1:
                s1=line[0]
                s2=line[1]
                s3=line[2]
                s4=line[3]
                s5=line[4]
                s6=line[5]
                s7=line[6]

                if s2:
                   cur_PROD.execute("update hr_employee set address_id='%s' where id='%s'" % (s2,s1))
                   cur_PROD.execute("commit")
                if s3:
                   cur_PROD.execute("update hr_employee set coach_id='%s' where id='%s'" %(s3,s1))
                   cur_PROD.execute("commit")
                if s4:
                    cur_PROD.execute("update hr_employee set job_id='%s' where id='%s'" % (s4, s1))
                    cur_PROD.execute("commit")
                if s5:
                    cur_PROD.execute("update hr_employee set country_id='%s' where id='%s'" % (s5, s1))
                    cur_PROD.execute("commit")
                if s6:
                    cur_PROD.execute("update hr_employee set parent_id='%s' where id='%s'" % (s6, s1))
                    cur_PROD.execute("commit")
                if s7:
                    try:
                       cur_PROD.execute("update hr_employee set department_id='%s' where id='%s'" % (s7, s1))
                       cur_PROD.execute("commit")
                    except Exception as inst:
                       print ("Department_id NO Update")
                # if s8:
                #     try:
                #        cur_PROD.execute("update hr_employee set image='%s' where id='%s'" % (s8, s1))
                #        cur_PROD.execute("commit")
                #     except Exception as inst:
                #        print "Department_id NO Update"
                cur_PROD.execute("update hr_employee set gender=null where gender='-'")
                cur_PROD.execute("commit")
                print ("hr_employee update OK!")

                view = self.env.ref('sh_message.sh_message_wizard')
                view_id = view and view.id or False
                context = dict(self._context or {})
                context['message'] = 'hr.employee migration ok'
                return {
                    'name': '系統通知訊息',
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'sh.message.wizard',
                    'views': [(view.id, 'form')],
                    'view_id': view.id,
                    'target': 'new',
                    'context': context, }
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
                'context': context, }
