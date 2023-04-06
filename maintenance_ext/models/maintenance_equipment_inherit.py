# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class MaintenanceEquipmentInherit(models.Model):
    _inherit = "maintenance.equipment"

    @api.depends('check_list_line')
    def _get_list(self):
        num=0
        for rec in self.check_list_line:
            num = num + 1
        if num > 0:
           self.have_list=True
        else:
           self.have_list=False

    @api.depends('check_list_line1')
    def _get_list1(self):
        num = 0
        for rec in self.check_list_line1:
            num = num + 1
        if num > 0:
            self.have_list1 = True
        else:
            self.have_list1 = False

    check_list_line = fields.One2many('maintenance.equipment_check_list','equip_id',copy=False)
    enable_check_list = fields.Boolean(string="啟用每日巡檢清單",default=False)
    check_list_line1 = fields.One2many('maintenance.equipment_check_list1','equip_id',copy=False)
    enable_check_list1 = fields.Boolean(string="啟用額定維修清單", default=False)
    have_list = fields.Boolean(string="有每日巡檢清單",compute=_get_list)
    have_list1 = fields.Boolean(string="有額定定保清單", compute=_get_list1)
    main_type = fields.Selection([('1','依設定日期'),('2','依生產機台碼錶')],string="定保觸發模式",default='1')
    equip_last_value = fields.Float(digits=(12,5),string="上次定保碼錶值")
    equip_next_value = fields.Float(digits=(12,5),string="下次定保碼錶值")
    equip_now_value = fields.Float(digits=(12,5),string="目前碼錶值")
    ref_equipname = fields.Char(string="參考來源")
    ref_equipname1 = fields.Char(string="參考來源")

    def copy_template_list(self):
        self.env.cr.execute("""select gentempchecklist(%d,'%s')""" % (self.id,self.ref_equipname))
        self.env.cr.execute("""commit""")

    def copy_template_list1(self):
        self.env.cr.execute("""select gentempchecklist1(%d,'%s')""" % (self.id,self.ref_equipname1))
        self.env.cr.execute("""commit""")


class MaintenanceEquipmentCheckList(models.Model):
    _name = "maintenance.equipment_check_list"
    _description = "設備每日巡檢清單"

    equip_id = fields.Many2one('maintenance.equipment',ondelete='cascade')
    check_item = fields.Char(string="巡檢項目名稱")
    check_active = fields.Boolean(string="生效?",default=True)
    check_value = fields.Selection([('1','OK/NG'),('2','輸入檢測數據')],string="檢測模式",default='1')
    h_value = fields.Float(digits=(12,5),string="上限值")
    l_value = fields.Float(digits=(12,5),string="下限值")


class MaintenanceEquipmentCheckList1(models.Model):
    _name = "maintenance.equipment_check_list1"
    _description = "設備額定定保清單"

    equip_id = fields.Many2one('maintenance.equipment',ondelete='cascade')
    check_item = fields.Char(string="定檢項目名稱")
    check_active = fields.Boolean(string="生效?",default=True)


