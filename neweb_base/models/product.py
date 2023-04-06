# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _


class ProductTemplate(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'
	_description = "Product Template"
	_defaults = {
		'sale_ok': 0,
		'purchase_ok': 0,
	}

	maintenance_category_id = fields.Many2one('neweb_base.maintenance_category', ondelete='cascade', string="Maintenance Category")
	is_maintenance_target = fields.Boolean(string='Is Maintenance Target')
	brand = fields.Char(string='Brand')
	serial = fields.Char(string='Machine Serial')
	model = fields.Char(string='Machine Model')
	serial_num = fields.Char(string='Serial Number')
	specification = fields.Text(string='Specification')

	prod_ids = fields.One2many('neweb_base.product_link', 'prod_tmp_id', string="Products")

	@api.onchange('serial', 'model', 'brand')
	def _serial_model_model_onchange(self):
		name_composite = []
		if self.brand:
			name_composite.append(self.brand)
		if self.serial:
			name_composite.append(self.serial)
		if self.model:
			name_composite.append(self.model)

		self.name = " ".join(name_composite)

	# @api.one
	@api.depends('name', 'default_code')
	def _compute_display_name(self):
		for rec in self:
			if rec.default_code:
				rec.display_name = "%s [%s]" % (rec.name, rec.default_code)
			# Add parts to name
			if rec.is_maintenance_target:
				parts = ", ".join([(p.prod.name + ' x ' + str(p.quantity)) for p in rec.prod_ids])
				if parts != '':
					if rec.display_name:
						rec.display_name += ('【%s】' % parts)
					else:
						rec.display_name = ('【%s】' % parts)


class ProductProduct(models.Model):
	_name = 'product.product'
	_inherit = 'product.product'
	_description = "Product"

	# def name_get(self, cr, user, ids, context=None):
	# 	if context is None:
	# 		context = {}
	# 	if isinstance(ids, (int, long)):
	# 		ids = [ids]
	# 	if not len(ids):
	# 		return []
    #
	# 	def _name_get(d):
	# 		name = d.get('name','')
	# 		code = context.get('display_default_code', True) and d.get('default_code', False) or False
	# 		if code:
	# 			# name = '[%s] %s' % (code,name)
	# 			name = '%s [%s]' % (name,code)
	# 		# Add parts to name
	# 		if product.product_tmpl_id.is_maintenance_target:
	# 			parts = ", ".join([(p.prod.name + ' x ' + str(p.quantity)) for p in product.product_tmpl_id.prod_ids])
	# 			if parts != '':
	# 				name += ('【%s】' % parts)
	# 		return d['id'], name
    #
	# 	partner_id = context.get('partner_id', False)
	# 	if partner_id:
	# 		partner_ids = [partner_id, self.pool['res.partner'].browse(cr, user, partner_id, context=context).commercial_partner_id.id]
	# 	else:
	# 		partner_ids = []
    #
	# 	# all user don't have access to seller and partner
	# 	# check access and use superuser
	# 	self.check_access_rights(cr, user, "read")
	# 	self.check_access_rule(cr, user, ids, "read", context=context)
    #
	# 	result = []
	# 	for product in self.browse(cr, user, ids, context=context).sudo():
	# 		variant = ", ".join([v.name for v in product.attribute_value_ids])
	# 		name = variant and "%s (%s)" % (product.name, variant) or product.name
	# 		sellers = []
	# 		if partner_ids:
	# 			if variant:
	# 				sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and (x.product_id == product)]
	# 			if not sellers:
	# 				sellers = [x for x in product.seller_ids if (x.name.id in partner_ids) and not x.product_id]
	# 		if sellers:
	# 			for s in sellers:
	# 				seller_variant = s.product_name and (
	# 					variant and "%s (%s)" % (s.product_name, variant) or s.product_name
	# 					) or False
	# 				mydict = {
	# 						  'id': product.id,
	# 						  'name': seller_variant or name,
	# 						  'default_code': s.product_code or product.default_code,
	# 						  }
	# 				result.append(_name_get(mydict))
	# 		else:
	# 			mydict = {
	# 					  'id': product.id,
	# 					  'name': name,
	# 					  'default_code': product.default_code,
	# 					  }
	# 			result.append(_name_get(mydict))
	# 	return result


class ProductProductLink(models.Model):
	_name = 'neweb_base.product_link'
	_description = "Product Links"
	_defaults = {
		'quantity': 1,
	}

	name = fields.Char(string = "parts",compute="_compute_name")
	prod = fields.Many2one('product.product', ondelete='cascade', string="Product Child", required=True)
	quantity = fields.Integer(string="Quantity")

	prod_tmp_id = fields.Many2one('product.template', ondelete='cascade', string="Product Parent")

	# @api.one
	def _compute_name(self):
		self.name = self.prod.name + ' x ' + str(self.quantity)
