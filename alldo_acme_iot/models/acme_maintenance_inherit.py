# -*- coding: utf-8 -*-
# Author : Peter Wu

import json,logging,re
from odoo import models,fields,api, _
from odoo.exceptions import UserError
from lxml import etree


class alldomaintenanceinherit(models.Model):
    _inherit = "maintenance.equipment"
    _order = "sequence,id"

    iot_ip = fields.Char(string="IOT TCP/IP 位址")
    iot_uuid = fields.Char(string="IOT UUID")
    iot_mac = fields.Char(string="IOT MAC Address")
    iot_status = fields.Selection([('1', '架模'),('2','開工'), ('3', '烘模'), ('4','停止')], default='4', string="IOT狀態")
    iot_owner = fields.Many2one('hr.employee', string="擔當者1")
    iot_owner1 = fields.Many2one('hr.employee', string="擔當者2")
    iot_start_datetime = fields.Datetime(string="啟動時間")
    iot_data_line = fields.One2many('alldo_acme_iot.equipment_iot_data','iot_id',string="IOT履歷明細",copy=False)
    iot_status_line = fields.One2many('alldo_acme_iot.equipment_iot_status', 'iot_id', string="IOT狀態明細", copy=False)
    outofforder_line = fields.One2many('alldo_acme_iot.equipment_outofforder_status', 'iot_id', string="設備異常記錄", copy=False)
    scale_line = fields.One2many('alldo_acme_iot.electronic_scale','equipment_no', string="磅秤投料記錄", copy=False)
    equipment_no = fields.Char(string="機台編號",required=True)
    equipment_type = fields.Selection([('1','鑄件'),('2','熔爐'),('3','加工機')],string="設備型態")
    mo_no = fields.Many2one('alldo_acme_iot.workorder',string="目前在線工單")
    start_duration = fields.Float(digits=(10, 1), string="今日開工總工時(分鐘)", default=0.0)
    stop_duration = fields.Float(digits=(10, 1), string="今日暫停總工時(分鐘)", default=0.0)
    sequence = fields.Integer(string="SEQ",default=20)
    iot_item = fields.Integer(string="主控劃面序列")
    image = fields.Binary('教學說明')
    image_filename = fields.Char("Image Filename")
    today_prodnum = fields.Float(string="今日生產量")
    maintenance_line = fields.One2many('alldo_acme_iot.equipment_maintenance_data','equip_id',string="機台設備維護記錄",copy=False)

    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False, context=None):
    #     if context is None:
    #         context = {}
    #     res = super(alldomaintenanceinherit, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
    #     _main_arch_lst = """
    #      <page string="機台維護保養記錄" name="Main_line" >
    #         <field name="maintenance_line" widget="one2many" nolabel="1">
    #             <tree >
    #                  <field name="main_date"/>
    #                  <field name="partner_id" options="{'no_create':true,'no_create_edit':true}"/>
    #                  <field name="main_desc"/>
    #                  <field name="main_memo"/>
    #                  <field name="main_attach" widget="binary"/>
    #             </tree>
    #         </field>
    #     </page>
    #       """
    #     doc = etree.XML(res['arch'])
    #     if view_type == 'form':
    #         main_node = doc.xpath("//page[@string='Maintenance']")
    #         if main_node and len(main_node) > 0 :
    #             main_page = etree.XML(_main_arch_lst)
    #             main_node.addnext(main_page)
    #     res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res

    def run_updatetodaynum(self):
        self.env.cr.execute("""select updatetodaynum()""")
        self.env.cr.execute("""commit""")


    def run_iot_restart(self):
        import paramiko
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.iot_ip, 22, 'root', '!99999ibm')
        ssh.get_transport().open_session().exec_command(
            "kill -9 $(ps -ef|grep mes_client.py|grep -v grep|awk '{print $2}')")
        ssh.get_transport().open_session().exec_command(
            "mv /home/pi/mes_action/action.bak /home/pi/mes_action/mes_action.pickle")
        stdin, stdout, stderr = ssh.exec_command("shutdown -r now")
        ssh.close()
        view = self.env.ref('sh_message.sh_message_wizard')
        view_id = view and view.id or False
        context = dict(self._context or {})
        context['message']='IOT已重啟動作！'
        return {
            'name':'訊息通知',
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'sh.message.wizard',
            'views':[(view.id,'form')],
            'view_id':view.id,
            'target':'new',
            'context':context,
            }


class alldoacmeiotequipmentiotdata(models.Model):
    _name = "alldo_acme_iot.equipment_iot_data"
    _description = "IOT機台狀態履歷"
    _order = "id desc"

    iot_id = fields.Many2one('maintenance.equipment', ondelete='cascade')
    iot_uuid = fields.Char(string="IOT UUID")
    iot_datetime = fields.Datetime(string="時間")
    # iot_status = fields.Selection([('1', '啟動'), ('2', '暫停'), ('3', '停止')], default='3', string="IOT狀態")
    iot_owner = fields.Many2one('hr.employee', string="擔當者1")
    iot_owner1 = fields.Many2one('hr.employee', string="擔當者2")
    iot_workorder = fields.Many2one('alldo_acme_iot.workorder',string="工單號碼")
    iot_num = fields.Float(digits=(5,1),string="數量")
    iot_serial = fields.Char(string="IOT 流水號")



class alldoacmeiotequipmentiotstatus(models.Model):
    _name = "alldo_acme_iot.equipment_iot_status"

    iot_id = fields.Many2one('maintenance.equipment', ondelete='cascade')
    iot_datetime = fields.Datetime(string="時間")
    iot_workorder = fields.Many2one('alldo_acme_iot.workorder', string="工單號碼")
    iot_status = fields.Selection([('1', '開工'), ('2', '暫停'), ('3', '停止')], default='3', string="IOT狀態")



class alldoamceiotmaintenancedata(models.Model):
    _name = "alldo_acme_iot.equipment_maintenance_data"
    _description = "機台設備維護記錄"
    _order = "main_date desc"

    equip_id = fields.Many2one('maintenance.equipment',ondelete='cascade')
    main_date = fields.Date(string="維護日期")
    partner_id = fields.Many2one('res.partner',string="維護廠商")
    main_desc = fields.Char(string="維護明細")
    main_memo = fields.Text(string="MEMO")
    main_attach = fields.Binary(string="維護文件夾檔",attachment=False)

