# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _
from odoo.exceptions import UserError, RedirectWarning


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
    iot_data_line = fields.One2many('alldo_ipla_iot.equipment_iot_data','iot_id',string="IOT履歷明細",copy=False)
    iot_status_line = fields.One2many('alldo_ipla_iot.equipment_iot_status', 'iot_id', string="IOT狀態明細", copy=False)
    outofforder_line = fields.One2many('alldo_ipla_iot.equipment_outofforder_status', 'iot_id', string="設備異常記錄", copy=False)
    scale_line = fields.One2many('alldo_ipla_iot.electronic_scale','equipment_no', string="磅秤投料記錄", copy=False)
    equipment_no = fields.Char(string="機台編號",required=True)
    equipment_type = fields.Selection([('1','成型機'),('2','加工機')],string="設備型態")
    mo_no = fields.Many2one('alldo_ipla_iot.workorder',string="目前在線工單")
    start_duration = fields.Float(digits=(10, 1), string="今日開工總工時(分鐘)", default=0.0)
    stop_duration = fields.Float(digits=(10, 1), string="今日暫停總工時(分鐘)", default=0.0)
    sequence = fields.Integer(string="SEQ",default=20)
    iot_item = fields.Integer(string="主控劃面序列")
    image = fields.Binary('教學說明')
    image_filename = fields.Char("Image Filename")
    today_prodnum = fields.Float(string="今日生產量")

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


class alldoiplaiotequipmentiotdata(models.Model):
    _name = "alldo_ipla_iot.equipment_iot_data"
    _description = "IOT機台狀態履歷"
    _order = "id desc"

    iot_id = fields.Many2one('maintenance.equipment', ondelete='cascade')
    iot_uuid = fields.Char(string="IOT UUID")
    iot_datetime = fields.Datetime(string="時間")
    # iot_status = fields.Selection([('1', '啟動'), ('2', '暫停'), ('3', '停止')], default='3', string="IOT狀態")
    iot_owner = fields.Many2one('hr.employee', string="擔當者1")
    iot_owner1 = fields.Many2one('hr.employee', string="擔當者2")
    iot_workorder = fields.Many2one('alldo_ipla_iot.workorder',string="工單號碼")
    iot_num = fields.Float(digits=(5,1),string="數量")
    iot_serial = fields.Char(string="IOT 流水號")



class alldoiplaiotequipmentiotstatus(models.Model):
    _name = "alldo_ipla_iot.equipment_iot_status"

    iot_id = fields.Many2one('maintenance.equipment', ondelete='cascade')
    iot_datetime = fields.Datetime(string="時間")
    iot_workorder = fields.Many2one('alldo_ipla_iot.workorder', string="工單號碼")
    iot_status = fields.Selection([('1', '開工'), ('2', '暫停'), ('3', '停止')], default='3', string="IOT狀態")

