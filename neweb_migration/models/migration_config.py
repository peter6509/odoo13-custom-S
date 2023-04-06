# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError

class NEWEBMigration(models.Model):
    _name = "neweb_migration.config"
    _description = "資料庫昇級配置主檔"

    SOURCE_IP = fields.Char(string="來源端IP",default='192.168.1.221')
    DB_NAME = fields.Char(string="來源端資料庫",default='PROD')
    USER_NAME = fields.Char(string="資料庫帳號",default='odoo')
    PASSWORD = fields.Char(string="帳號密碼",default='odoo')
    migration_line = fields.One2many('neweb_migration.config_line','migration_id',string="明細")

    @api.model
    def create(self, vals):
        mycount = self.env['neweb_migration.config'].search_count([])
        if mycount > 0 :
            raise UserError("只能存在一筆記錄！")
        res = super(NEWEBMigration, self).create(vals)
        return res


class NEWEBMigrationline(models.Model):
    _name = "neweb_migration.config_line"
    _description = "資料庫昇級明細數據"
    _order = "seq_id"

    migration_id = fields.Many2one('neweb_migration.config',ondelete='cascade')
    seq_id = fields.Integer(string="序號")
    migration_table = fields.Char(string="TABLE名稱")
    migration_model = fields.Char(string="Model名称")
    source_record = fields.Integer(string="來源TABLE筆數",default=0)
    target_record = fields.Integer(string="目的TABLE筆數",default=0)

