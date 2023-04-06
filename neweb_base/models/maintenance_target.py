# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)


class MaintenanceTarget(models.Model):
    _name = 'neweb_base.maintenance_target'
    _inherits = {'product.product': 'prod'}
    _description = "Maintenance Target"
    _sql_constraints = [('prod_machine_serial_no_uniq', 'unique(prod, machine_serial_no)', 'Product + Machine Serial No must be unique!!')]

    prod = fields.Many2one('product.product', ondelete='cascade', string="Maintenance Target", domain=[('is_maintenance_target', '=', True)], required=True)

    machine_serial_no = fields.Char(string='Machine Serial No', required=True)
    memo = fields.Text(string='Remark')

    # category_id = fields.Many2one('neweb_base.maintenance_category', ondelete='cascade', string="Maintenance Category", required=True)
    maintenance_category_id = fields.Char(related="prod.maintenance_category_id.name", string="Maintenance Category")

    # @api.one
    # @api.depends('prod')
    # def _get_prod_category(self):
    #     for rec in self:
    #         rec.category_id = rec.prod.maintenance_category_id.name

    def _is_maintenance_target(self, vals):
        # _logger.info("test flag.... %s" % vals.get('prod'))
        prod_id = vals.get('prod')
        prod_obj = self.env['product.product'].search([('id', '=', prod_id)])
        # _logger.info("test obj name : %s" % prod_obj.name)
        # _logger.info("test obj....%s" % prod_obj.is_maintenance_target)
        return prod_obj.is_maintenance_target

    @api.model
    def create(self, vals):
        # _logger.info("create:.... %s" % vals)
        if not self._is_maintenance_target(vals):
            raise ValidationError(_('The Product must be Maintenance target.'))
        return super(MaintenanceTarget, self).create(vals)

    # @api.multi
    def write(self, vals):
        # _logger.info("update:.... %s" % vals)
        if vals.get('prod'):
            if not self._is_maintenance_target(vals):
                raise ValidationError(_('The Product must be Maintenance target.'))
        return super(MaintenanceTarget, self).write(vals)
