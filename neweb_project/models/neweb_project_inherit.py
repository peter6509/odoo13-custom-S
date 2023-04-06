# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api
from odoo.exceptions import UserError


class warrantyservicerule(models.Model):
    _name = "neweb.warranty_service_rule"
    _description = '成本分析保固服務條款基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="保固服務條款")
    active = fields.Boolean(string="生效",default=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("未輸入 保固服務條款 請確認！")
        myname = self.name
        mycount = self.env['neweb.warranty_service_rule'].search_count([('name','=',myname)])
        if mycount > 0:
            raise UserError("輸入值已重複,請確認！")
        res = super(warrantyservicerule,self).create(vals)
        return res


class newebpaymentterm(models.Model):
    _name = "neweb.payment_term_rule"
    _description = '成本分析分期付款基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="分期付款條款")
    active = fields.Boolean(string="生效",default=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("未輸入 分期付款條款 請確認！")
        myname = self.name
        mycount = self.env['neweb.payment_term_rule'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise UserError("輸入值已重複,請確認！")
        res = super(newebpaymentterm, self).create(vals)
        return res

class mainservicerule(models.Model):
    _name = "neweb.main_service_rule"
    _description = '成本分析維護服務條款基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="維護服務條款")
    active = fields.Boolean(string="生效",default=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("未輸入 維護服務條款 請確認！")
        myname = self.name
        mycount = self.env['neweb.main_service_rule'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise UserError("輸入值已重複,請確認！")
        res = super(mainservicerule, self).create(vals)
        return res


class routinemaintenance(models.Model):
    _name = "neweb.routine_maintenance"
    _description = '成本分析定期維護條款基礎配置'
    _order = "sequence,id"

    name = fields.Char(string="定期維護條款")
    active =fields.Boolean(string="生效",default=True)
    sequence = fields.Integer(string="SEQ", default=20)

    @api.model
    def create(self, vals):
        if 'name' in vals and not vals['name']:
            raise UserError("未輸入 定期維護條款 請確認！")
        myname = self.name
        mycount = self.env['neweb.routine_maintenance'].search_count([('name', '=', myname)])
        if mycount > 0:
            raise UserError("輸入值已重複,請確認！")
        res = super(routinemaintenance, self).create(vals)
        return res



class newebprojectinherit(models.Model):
    _inherit = "sale.order"
    _description = '銷售主檔'

    payment_term_new = fields.Many2one('neweb.payment_term_rule',string="分期付款期數")
    warranty_service_rule_new = fields.Many2one('neweb.warranty_service_rule',string="保固服務條款")
    main_service_rule_new = fields.Many2one('neweb.main_service_rule',string="維護服務條款")
    routine_maintenance_new = fields.Many2one('neweb.routine_maintenance',string="定期維護條款")

