# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class MaintenanceCategory(models.Model):
    _name = 'neweb_base.maintenance_category'
    _description = "維護類別基礎配置"
    _sql_constraints = [('name_uniq', 'unique(name)', 'Maintenance Category must be unique!!')]

    name = fields.Char(string='Maintenance Category', required=True, translate=True)
    # TODO Product Type No
    product_type_ids = fields.One2many('neweb_base.product_type', 'maintenance_category_id', string="Product Type", required=False)
    product_attr = fields.Selection([('Hardware', 'Hardware'), ('Software', 'Software')], string='Product Attribute', required=True)
    maintenance_item_ids = fields.One2many('neweb_base.maintenance_item', 'maintenance_category_id', string="Maintenance Item", required=False)

    disabled = fields.Boolean(string='Disabled')
    memo = fields.Text(string='Remark')

    # problem_id = fields.Many2one('neweb_base.problem', ondelete='cascade', string="Problem Name", required=True)


class ProductType(models.Model):
    _name = 'neweb_base.product_type'
    _description = "Product Type Number"

    name = fields.Char(string='Product Type Number', required=True, translate=True)
    maintenance_category_id = fields.Many2one('neweb_base.maintenance_category', ondelete='cascade', string="Maintenance Category")


class MaintenanceItem(models.Model):
    _name = 'neweb_base.maintenance_item'
    _description = "維護項目基礎配置"

    name = fields.Char(string='Maintenance Item', required=True, translate=True)
    maintenance_category_id = fields.Many2one('neweb_base.maintenance_category', ondelete='cascade', string="Maintenance Category")
