# -*- coding: utf-8 -*-
# Author : Peter Wu

from odoo import models,fields,api, _

class newebstockininherit4(models.Model):
    _inherit = "stock.quant"

    @api.model
    def _get_quants_action(self, domain=None, extend=False):
        """ Returns an action to open quant view.
        Depending of the context (user have right to be inventory mode or not),
        the list view will be editable or readonly.

        :param domain: List for the domain, empty by default.
        :param extend: If True, enables form, graph and pivot views. False by default.
        """
        self._quant_tasks()
        ctx = dict(self.env.context or {})
        ctx.pop('group_by', None)
        action = {
            'name': _('Update Quantity'),
            'view_type': 'tree',
            'view_mode': 'list',
            'res_model': 'stock.quant',
            'type': 'ir.actions.act_window',
            'context': ctx,
            'domain': domain or [],
            'help': """
                    <p class="o_view_nocontent_empty_folder">No Stock On Hand</p>
                    <p>This analysis gives you an overview of the current stock
                    level of your products.</p>
                    """
        }

        if self._is_inventory_mode():
            action['view_id'] = self.env.ref('stock.view_stock_quant_tree_editable').id
            # fixme: erase the following condition when it'll be possible to create a new record
            # from a empty grouped editable list without go through the form view.
            if not self.search_count([
                ('company_id', '=', self.env.company.id),
                ('location_id.usage', 'in', ['internal', 'transit'])
            ]):
                action['context'].update({
                    'search_default_productgroup': 0,
                    'search_default_locationgroup': 1
                })
        else:
            action['view_id'] = self.env.ref('stock.view_stock_quant_tree').id
            # Enables form view in readonly list
            action.update({
                'view_mode': 'tree,form',
                'views': [
                    (action['view_id'], 'list'),
                    (self.env.ref('stock.view_stock_quant_form').id, 'form'),
                ],
            })
        if extend:
            action.update({
                'view_mode': 'tree,form,pivot,graph',
                'views': [
                    (action['view_id'], 'list'),
                    (self.env.ref('stock.view_stock_quant_form').id, 'form'),
                    (self.env.ref('stock.view_stock_quant_pivot').id, 'pivot'),
                    (self.env.ref('stock.stock_quant_view_graph').id, 'graph'),
                ],
            })
        return action


class newebstockinproduct(models.Model):
    _inherit = "product.product"

    def action_open_quants(self):
        domain = [('product_id', 'in', self.ids)]
        hide_location = not self.user_has_groups('stock.group_stock_multi_locations')
        hide_lot = all([product.tracking == 'none' for product in self])
        self = self.with_context(hide_location=hide_location, hide_lot=hide_lot)

        # If user have rights to write on quant, we define the view as editable.
        if self.user_has_groups('stock.group_stock_manager'):
            self = self.with_context(inventory_mode=True)
            # Set default location id if multilocations is inactive
            if not self.user_has_groups('stock.group_stock_multi_locations'):
                user_company = self.env.company
                warehouse = self.env['stock.warehouse'].search(
                    [('company_id', '=', user_company.id)], limit=1
                )
                if warehouse:
                    self = self.with_context(default_location_id=warehouse.lot_stock_id.id)
        # Set default product id if quants concern only one product
        if len(self) == 1:
            self = self.with_context(
                default_product_id=self.id,
                single_product=True
            )
        else:
            self = self.with_context(product_tmpl_id=self.product_tmpl_id.id)
        ctx = dict(self.env.context)
        ctx.update({'no_at_date': True, 'search_default_on_hand': True,'search_default_locationgroup':True})
        return self.env['stock.quant'].with_context(ctx)._get_quants_action(domain)
