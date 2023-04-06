# -*- coding: utf-8 -*-
# Author : Peter Wu


import psycopg2
import os.path
import os
import time
import pickle


class IOT_UTIL:

    # def mes_wakeonlan(macaddr):
    #     from wakeonlan import send_magic_packet
    #     send_magic_packet(macaddr)

    # def mes_mostart_check():
    #     if os.path.exists('/home/pi/mes_action/mes_mo_action.pickle'):
    #         with open('/home/pi/mes_action/mes_mo_action.pickle', 'rb') as mo_action:
    #             now_no_no = pickle.load(mo_action)
    #         mo_action.close()
    #         return now_no_no['mo_no']
    #     else:
    #         return ''

    def wip_reboot(node_ip):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(node_ip, 22, 'root', '!99999ibm')
        ssh.get_transport().open_session().exec_command("kill -9 $(ps -ef|grep acme_client.py|grep -v grep|awk '{print $2}')")
        # ssh.get_transport().open_session().exec_command("mv /home/pi/mes_action/action.bak /home/pi/mes_action/mes_action.pickle")
        stdin, stdout, stderr = ssh.exec_command("shutdown -r now")
        ssh.close()

    def wip_shutdown(node_ip):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(node_ip, 22, 'root', '!99999ibm')
        stdin, stdout, stderr = ssh.exec_command("shutdown -h now")
        ssh.close()

    def iot_push_file(node_ip, localpath, remotepath):  ## 傳檔到終端點
        import paramiko
        t = paramiko.Transport((node_ip, 22))
        t.connect(username='pi', password='pi')
        sftp = paramiko.SFTPClient.from_transport(t)
        if os.path.exists(localpath):
            try:
                # sftp.stat(remotepath)
                sftp.put(localpath, remotepath)
            except Exception as inst:
                print('Push NO OK')
        else:
            print('Local No such File')
        t.close()

    def iot_get_file(node_ip, remotepath, localpath):  ## 從終端點抓檔
        import paramiko

        t = paramiko.Transport((node_ip, 22))
        t.connect(username='pi', password='pi')
        sftp = paramiko.SFTPClient.from_transport(t)
        try:
            # sftp.stat(remotepath)
            sftp.get(remotepath, localpath)
        except Exception as inst:
            print('Get No Ok')

        t.close()

    def check_iot(self,myip):
        response = os.system("ping -c 1 " + myip)
        if response == 0:
            return True
        else:
            return False
        # else:
        #     return {'warning': {'title': '警告通知', 'message': _('未設定參數檔,請確認!')}}
            # tk.messagebox.showinfo(message="未設定參數檔,請確認")
            # return False

    def check_modata(self,mo_no):  ## 與Odoo Server確認此工單

            import psycopg2
            SOURCE_IP = '192.168.1.10'
            DB_NAME = 'acme'
            USER_NAME = 'odoo'
            PASSWORD = '!99999ibm'

            mes_string = "host='%s' dbname='%s' user='%s' password='%s' port='5432'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
            try:
                mes_conn = psycopg2.connect(mes_string)
                mes_cur = mes_conn.cursor()
                mes_cur.execute("select checkdbinfo()")
                myrec = mes_cur.fetchone()[0]
                if myrec == True:
                    print("成功")
                else:
                    print("失敗")
            except ValueError:
                print('失敗')



    # def check_mostate(mo_no):
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         response = os.system("ping -c 1 " + SOURCE_IP)
    #         if response != 0:
    #             return {'warning': {'title': '警告通知', 'message': _('DB Server不存在,請確認!')}}
    #             # tk.messagebox.showinfo(title="警告", message="DB Server不存在,請確認")
    #             # return
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         mes_cur.execute("select getmostate('%s')" % mo_no)
    #         mymesrec = mes_cur.fetchone()
    #         if mymesrec[0] == 'OK':  # OK
    #             return "1"
    #         if mymesrec[0] == 'NO':  # NO OK
    #             return "2"
    #     else:
    #         return {'warning': {'title': '警告通知', 'message': _('尚未做系統參數配置,無法繼續!')}}
    #         # tk.messagebox.showerror(message=u'尚未做系統參數配置,無法繼續')

    # def getsmbpath(mo_no):
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         try:
    #             mes_cur.execute("select getsmbpath('%s')" % mo_no)
    #             mysmbpath = mes_cur.fetchone()
    #         except ValueError:
    #             print("No SMB Path INFO")
    #         if mysmbpath:
    #             return mysmbpath[0]
    #     else:
    #         return {'warning': {'title': '警告通知', 'message': _('尚未做系統參數配置,無法繼續!')}}
    #         # tk.messagebox.showerror(message=u'尚未做系統參數配置,無法繼續')

    # def mo_process_write(mo_no):  ## write 目前 SOP 排程序列
    #     my_sop_process = list()
    #     if os.path.exists('/home/pi/mes_action/mes_sop_process.pickle'):
    #         with open('/home/pi/mes_action/mes_sop_process.pickle', 'rb') as sop_process:
    #             my_sop_process = pickle.load(sop_process)
    #         sop_process.close()
    #     if mo_no not in my_sop_process:
    #         my_sop_process.append({'mo_no': mo_no})
    #         with open('/home/pi/mes_action/mes_sop_process.pickle', 'wb') as sop_process:
    #             pickle.dump(my_sop_process, sop_process, protocol=pickle.HIGHEST_PROTOCOL)
    #         sop_process.close()
    #     else:
    #         return {'warning': {'title': '警告通知', 'message': _('此工單已在序列中了!')}}
    #         # tk.messagebox.showinfo(title=u'INFO', message=u'此工單已在序列中了')
    #
    # def check_assing_mo_data(mo_no, sopseqid):
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         mes_cur.execute("select distinct product_id from mrp_production where name='%s'" % mo_no)
    #         myprodid = mes_cur.fetchone()[0]
    #         mymoprodid = int(myprodid)
    #         mes_cur.execute("select id,cnt_prod_pic from mes_sop_sop where prodname=%d " % mymoprodid)
    #         messop = mes_cur.fetchone()
    #         if messop:
    #             messopid = int(messop[0])
    #             cntprodpic = messop[1]
    #             mes_cur.execute(
    #                 "select workshop_type from mes_sop_sop_workshop where sop_lines_id=%d  and sop_sequence_id='%s'" % (
    #                 messopid, sopseqid))
    #             mymessop1_rec = mes_cur.fetchone()
    #             if not mymessop1_rec or mymessop1_rec[0] != '1':
    #                 raise ValueError("此工站序號錯誤,請確認..")
    #                 # return {'warning': {'title': '警告通知', 'message': _('此工站序號錯誤,請確認..')}}
    #                 # # tk.messagebox.showinfo(title=u'訊息', message=u'此工站序號錯誤,請確認..')
    #                 # return False
    #             else:
    #                 return True
    #         else:
    #             return False
    #     else:
    #         return False
    #
    # def assign_sop_data(mo_no, sopseqid):
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         mes_cur.execute("select distinct product_id from mrp_production where name='%s'" % mo_no)
    #         myprodid = mes_cur.fetchone()[0]
    #         mymoprodid = int(myprodid)
    #         mes_cur.execute("select id,cnt_prod_pic,wip_name from mes_sop_sop where prodname=%d " % mymoprodid)
    #         messop = mes_cur.fetchone()
    #         if messop:
    #             messopid = int(messop[0])
    #             cntprodpic = messop[1]
    #             wipname = messop[2]
    #             mes_cur.execute(
    #                 "select sop_sequence_id,sop_workshop_name,sop_workshop_ip,workshop_type,sop_file_type,sop_file_name,remote_file_name,smb_file_name,sop_delay_time,sop_active from mes_sop_sop_workshop where sop_lines_id=%d  and sop_sequence_id='%s'" % (
    #                 messopid, sopseqid))
    #             mymessop_rec = mes_cur.fetchall()
    #             if mymessop_rec:
    #                 sop_array = []
    #                 for rec in mymessop_rec:
    #                     # try:
    #                     mes_cur.execute("select getwipip(%s,%s)" % (wipname, rec[0]))
    #                     myip = mes_cur.fetchone()
    #                     # except ValueError:
    #                     #    print("No Node IP")
    #                     # try:try
    #                     mes_cur.execute("select getwipmac(%s,%s)" % (wipname, rec[0]))
    #                     mymac = mes_cur.fetchone()
    #                     # except ValueError:
    #                     #    print("No Node MAC")
    #                     if not rec[5]:
    #                         mysopfilename = 'xx'
    #                     else:
    #                         mysopfilename = rec[5]
    #                     if not rec[0]:
    #                         mysopseqid = 0
    #                     else:
    #                         mysopseqid = rec[0]
    #                     if not rec[1]:
    #                         mysopwhname = 'xx'
    #                     else:
    #                         mysopwhname = rec[1]
    #                     if not myip[0]:
    #                         mysopip = 'xx'
    #                     else:
    #                         mysopip = myip[0]
    #                     if not rec[3]:
    #                         mywhtype = '1'
    #                     else:
    #                         mywhtype = rec[3]
    #                     if not rec[4]:
    #                         mysopfiletype = '2'
    #                     else:
    #                         mysopfiletype = rec[4]
    #                     if not rec[6]:
    #                         myrfname = 'xx'
    #                     else:
    #                         myrfname = rec[6]
    #                     if not rec[7]:
    #                         mysmbfname = 'xx'
    #                     else:
    #                         mysmbfname = rec[7]
    #                     if not rec[8]:
    #                         mysopdtime = 20
    #                     else:
    #                         mysopdtime = rec[8]
    #                     if not rec[9]:
    #                         mysopactive = '0'
    #                     else:
    #                         mysopactive = rec[9]
    #                     if not mymac[0]:
    #                         mynodemac = 'xx'
    #                     else:
    #                         mynodemac = mymac[0]
    #                     sop_array.append({'sop_sequence_id': mysopseqid,
    #                                       'sop_workshop_name': mysopwhname,
    #                                       'sop_workshop_ip': mysopip,
    #                                       'workshop_type': mywhtype,
    #                                       'sop_file_type': mysopfiletype,
    #                                       'sop_file_name': mysopfilename,
    #                                       'remote_file_name': myrfname,
    #                                       'smb_file_name': mysmbfname,
    #                                       'cnt_prod_pic': cntprodpic,
    #                                       'sop_delay_time': mysopdtime,
    #                                       'sop_active': mysopactive,
    #                                       'sop_workshop_mac': mynodemac, })
    #                 with open('/home/pi/mes_action/mes_single_sopinfo.pickle', 'wb') as sop_info:
    #                     pickle.dump(sop_array, sop_info)
    #                 sop_info.close()
    #             else:
    #                 return {'warning': {'title': '警告通知', 'message': _('查無此工站資訊,請確認!')}}
    #                 # tk.messagebox.showinfo(title="警告", message="查無此工站資訊,請確認")
    #         try:
    #             mes_cur.execute("select completed_qty,mo_closed from mes_sop_mo_status where name='%s'" % mo_no)
    #             mescnt_rec = mes_cur.fetchone()
    #         except ValueError:
    #             print("No MO Statue INFO")
    #         if mescnt_rec:
    #             mycompleteqty = mescnt_rec[0]
    #             mymoclosed = mescnt_rec[1]
    #         else:
    #             mycompleteqty = 0
    #             mymoclosed = 'N'
    #         try:
    #             mes_cur.execute("select getmoprodno('%s')" % mo_no)
    #             myprodno = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No PROD No")
    #         try:
    #             mes_cur.execute("select getmoprodname('%s')" % mo_no)
    #             myprodname = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No  PROD Name")
    #         try:
    #             mes_cur.execute("select getmoprodqty('%s')" % mo_no)
    #             myprodqty = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No Prod Qty")
    #         try:
    #             mes_cur.execute("select getmoprodmodel('%s')" % mo_no)
    #             mymodelno1 = mes_cur.fetchone()[0]
    #         except Exception as inst:
    #             mymodelno1 = 'None'
    #             print("No PROD Model")
    #         if not myprodno[0]:
    #             myprodno1 = 'xx'
    #         else:
    #             myprodno1 = myprodno[0]
    #         if not myprodname[0]:
    #             myprodname1 = 'xx'
    #         else:
    #             myprodname1 = myprodname[0]
    #         if not myprodqty[0]:
    #             myprodqty1 = 0
    #         else:
    #             myprodqty1 = myprodqty[0]
    #         moactioninfo = []
    #         moactioninfo.append({'mo_no': mo_no,
    #                              'product_no': myprodno1,
    #                              'machine_type': myprodname1,
    #                              'product_qty': myprodqty1,
    #                              'completed_qty': mycompleteqty,
    #                              'model_no': mymodelno1,
    #                              })
    #         with open('/home/pi/mes_action/mes_single_moinfo.pickle', 'wb') as mes_cntinfo:
    #             pickle.dump(moactioninfo, mes_cntinfo, protocol=pickle.HIGHEST_PROTOCOL)
    #         mes_cntinfo.close()
    #
    # def get_mo_info(mo_no):  ## from odoo server 抓取工單資訊
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         mes_cur.execute("select distinct product_id from mrp_production where name='%s'" % mo_no)
    #         myprodid = mes_cur.fetchone()[0]
    #         mymoprodid = int(myprodid)
    #         mes_cur.execute("select id,cnt_prod_pic,wip_name from mes_sop_sop where prodname=%d " % mymoprodid)
    #         messop = mes_cur.fetchone()
    #         if messop:
    #             messopid = int(messop[0])
    #             cntprodpic = messop[1]
    #             wipname = messop[2]
    #             mes_cur.execute(
    #                 "select sop_sequence_id,sop_workshop_name,sop_workshop_ip,workshop_type,sop_file_type,sop_file_name,remote_file_name,smb_file_name,sop_delay_time,sop_active from mes_sop_sop_workshop where sop_lines_id=%d  order by sop_sequence_id" % messopid)
    #             mymessop_rec = mes_cur.fetchall()
    #             if mymessop_rec:
    #                 sop_array = []
    #                 for rec in mymessop_rec:
    #                     try:
    #                         mes_cur.execute("select getwipip(%s,%s)" % (wipname, rec[0]))
    #                         myip = mes_cur.fetchone()
    #                     except Exception as inst:
    #                         print("No Node IP")
    #                     try:
    #                         mes_cur.execute("select getwipmac(%s,%s)" % (wipname, rec[0]))
    #                         mymac = mes_cur.fetchone()
    #                     except Exception as inst:
    #                         print("No Node MAC")
    #
    #                     if not rec[5]:
    #                         mysopfilename = 'xx'
    #                     else:
    #                         mysopfilename = rec[5]
    #                     if not rec[0]:
    #                         mysopseqid = 0
    #                     else:
    #                         mysopseqid = rec[0]
    #                     if not rec[1]:
    #                         mysopwhname = 'xx'
    #                     else:
    #                         mysopwhname = str(rec[1])
    #                     if not myip[0]:
    #                         mysopip = 'xx'
    #                     else:
    #                         mysopip = myip[0]
    #                     if not rec[3]:
    #                         mywhtype = '1'
    #                     else:
    #                         mywhtype = rec[3]
    #                     if not rec[4]:
    #                         mysopfiletype = '2'
    #                     else:
    #                         mysopfiletype = rec[4]
    #                     if not rec[6]:
    #                         myrfname = 'xx'
    #                     else:
    #                         myrfname = rec[6]
    #                     if not rec[7]:
    #                         mysmbfname = 'xx'
    #                     else:
    #                         mysmbfname = rec[7]
    #                     if not rec[8]:
    #                         mysopdtime = 20
    #                     else:
    #                         mysopdtime = rec[8]
    #                     if not rec[9]:
    #                         mysopactive = '0'
    #                     else:
    #                         mysopactive = rec[9]
    #                     if not mymac[0]:
    #                         mynodemac = 'xx'
    #                     else:
    #                         mynodemac = mymac[0]
    #                     sop_array.append({'sop_sequence_id': mysopseqid,
    #                                       'sop_workshop_name': mysopwhname,
    #                                       'sop_workshop_ip': mysopip,
    #                                       'workshop_type': mywhtype,
    #                                       'sop_file_type': mysopfiletype,
    #                                       'sop_file_name': mysopfilename,
    #                                       'remote_file_name': myrfname,
    #                                       'smb_file_name': mysmbfname,
    #                                       'cnt_prod_pic': cntprodpic,
    #                                       'sop_delay_time': mysopdtime,
    #                                       'sop_active': mysopactive,
    #                                       'sop_workshop_mac': mynodemac, })
    #
    #                 with open('/home/pi/mes_action/mes_sopinfo.pickle', 'wb') as sop_info:
    #                     pickle.dump(sop_array, sop_info)
    #                 sop_info.close()
    #         mes_cur.execute("select completed_qty,mo_closed from mes_sop_mo_status where name='%s'" % mo_no)
    #         mescnt_rec = mes_cur.fetchone()
    #         if mescnt_rec:
    #             mycompleteqty = mescnt_rec[0]
    #             mymoclosed = mescnt_rec[1]
    #         else:
    #             mycompleteqty = 0
    #             mymoclosed = 'N'
    #         try:
    #             mes_cur.execute("select getmoprodno('%s')" % mo_no)
    #             myprodno = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No PROD No")
    #         try:
    #             mes_cur.execute("select getmoprodname('%s')" % mo_no)
    #             myprodname = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No PROD Name")
    #         try:
    #             mes_cur.execute("select getmoprodqty('%s')" % mo_no)
    #             myprodqty = mes_cur.fetchone()
    #         except Exception as inst:
    #             print("No PROD Qty")
    #         try:
    #             mes_cur.execute("select getmoprodmodel('%s')" % mo_no)
    #             mymodelno1 = mes_cur.fetchone()[0]
    #         except Exception as inst:
    #             mymodelno1 = 'None'
    #             print("No PROD Model")
    #
    #         if not myprodno[0]:
    #             myprodno1 = 'xx'
    #         else:
    #             myprodno1 = myprodno[0]
    #         if not myprodname[0]:
    #             myprodname1 = 'xx'
    #         else:
    #             myprodname1 = myprodname[0]
    #         if not myprodqty[0]:
    #             myprodqty1 = 0
    #         else:
    #             myprodqty1 = myprodqty[0]
    #         moactioninfo = []
    #         moactioninfo.append({'mo_no': mo_no,
    #                              'product_no': myprodno1,
    #                              'machine_type': myprodname1,
    #                              'product_qty': myprodqty1,
    #                              'completed_qty': mycompleteqty,
    #                              'model_no': mymodelno1,
    #                              })
    #         with open('/home/pi/mes_action/mes_moinfo.pickle', 'wb') as mes_cntinfo:
    #             pickle.dump(moactioninfo, mes_cntinfo, protocol=pickle.HIGHEST_PROTOCOL)
    #         mes_cntinfo.close()
    #
    #
    #     else:
    #         return {'warning': {'title': '警告通知', 'message': _('尚未做系統參數配置,無法繼續!')}}
    #         # tk.messagebox.showerror(message=u'尚未做系統參數配置,無法繼續')
    #
    # def Ping(hostname):
    #     # hostname = "google.com"  # example
    #     response = os.system("ping -c 1 " + hostname)
    #
    #     # and then check the response...
    #     if response == 0:
    #         return True
    #     else:
    #         return False
    #
    # def complete_mo_status(mo_no, moclosed):  ## update Odoo Server mes_assembly.mo_status 工單狀態
    #     if os.path.exists('/home/pi/mes_config/mes_config.pickle'):
    #         with open('/home/pi/mes_config/mes_config.pickle', 'rb') as config_file:
    #             config_dict = pickle.load(config_file)
    #         config_file.close()
    #         SOURCE_IP = config_dict['mes_server_ip']
    #         DB_NAME = config_dict['mes_db_name']
    #         USER_NAME = config_dict['mes_db_username']
    #         PASSWORD = config_dict['mes_db_password']
    #         mes_string = "host='%s' dbname='%s' user='%s' password='%s'" % (SOURCE_IP, DB_NAME, USER_NAME, PASSWORD)
    #         mes_conn = psycopg2.connect(mes_string)
    #         mes_cur = mes_conn.cursor()
    #         moweight_dict = []
    #
    #         if os.path.exists('/home/pi/mes_weight/mes_cnt.pickle'):
    #             with open('/home/pi/mes_weight/mes_cnt.pickle', 'rb') as mes_weight:
    #                 moweight_dict = pickle.load(mes_weight)
    #             mes_weight.close()
    #             # except Exception as inst:
    #             #    print("MES WEIGHT FILE HAVE PROBLEM")
    #             # print(moweight_dict)
    #         if os.path.exists('/home/pi/mes_cnt/mes_cnt.pickle'):
    #             with open('/home/pi/mes_cnt/mes_cnt.pickle', 'rb') as mes_cnt:
    #                 mocnt_dict = pickle.load(mes_cnt)
    #             mes_cnt.close()
    #             if len(mocnt_dict) > 0:
    #                 completeqty = 0
    #                 i = 0
    #                 for item in mocnt_dict:
    #                     mono = mocnt_dict[i]['mo_no']
    #                     mocdate = mocnt_dict[i]['m_date']
    #                     moctime = mocnt_dict[i]['m_time']
    #                     if moweight_dict:
    #                         try:
    #                             if moweight_dict[i]['product_weight']:
    #                                 moweight = moweight_dict[i]['product_weight']
    #                             else:
    #                                 moweight = '0.0'
    #                         except Exception as inst:
    #                             print("No Weight record")
    #                             moweight = '0.0'
    #                     else:
    #                         moweight = '0.0'
    #                     completeqty += 1
    #                     mes_cur.execute(
    #                         "select insert_mo_data('%s','%s','%s','%s')" % (mono, mocdate, moctime, moweight))
    #                     mes_cur.execute("commit")
    #                     i += 1
    #                 mes_cur.execute("select update_mes_mo_status('%s',%d,'%s')" % (mo_no, completeqty, moclosed))
    #                 mes_cur.execute("commit")
    #         if os.path.exists('/home/pi/mes_cnt/mes_cnt.pickle'):
    #             mocntfile = '/home/pi/mes_cnt/mes_cnt.pickle'
    #             os.remove(mocntfile)
    #         if os.path.exists('/home/pi/mes_weight/mes_cnt.pickle'):
    #             moweightfile = '/home/pi/mes_weight/mes_cnt.pickle'
    #             os.remove(moweightfile)
    #         lbarray = []
    #         if os.path.exists('/home/pi/mes_action/mes_sop_process.pickle'):
    #             with open('/home/pi/mes_action/mes_sop_process.pickle', 'rb') as sop_process:
    #                 sop_lists = pickle.load(sop_process)
    #             sop_process.close()
    #             if sop_lists:
    #                 for item in sop_lists:
    #                     lbarray.append(item)
    #             if len(lbarray) > 0 and moclosed == 'Y':
    #                 lbarray.remove(mo_no)
    #             with open('/home/pi/mes_action/mes_sop_process.pickle', 'wb') as sop_process:
    #                 pickle.dump(lbarray, sop_process, protocol=pickle.HIGHEST_PROTOCOL)
    #             sop_process.close()
    #
    #     else:
    #         return {'warning': {'title': '警告通知', 'message': _('尚未做系統參數配置,無法繼續!')}}
    #         # tk.messagebox.showerror(message=u'尚未做系統參數配置,無法繼續')
    #
    # def rm_cnt_file(rm_ip, rm_file):
    #     import paramiko
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh.connect(rm_ip, 22, 'pi', '!999ibm')
    #     stdin, stdout, stderr = ssh.exec_command("rm -Rf '%s'" % rm_file)
    #     ssh.close()
    #
    # def rm_remote_file(rm_ip, rm_file):
    #     import paramiko
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh.connect(rm_ip, 22, 'pi', '!999ibm')
    #     stdin, stdout, stderr = ssh.exec_command("rm -Rf '%s'" % rm_file)
    #     ssh.close()
    #
    # def mes_init_proc():
    #     try:
    #         os.remove('/home/pi/mes_action/mes_action.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_mo_action.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_moinfo.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_sopinfo.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_single_moinfo.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_single_sopinfo.pickle')
    #     except Exception as inst:
    #         A = 1
    #     try:
    #         os.remove('/home/pi/mes_action/mes_sop_process.pickle')
    #     except Exception as inst:
    #         A = 1