# -*- coding: utf-8 -*-
{
	'name': u"<4.1>.Neweb 合約/報修基礎模組",
	'version': '2.0',
	'summary': "Neweb Customization Base",
	'sequence': 5,
	'description': """
Neweb Base
==========
Base Module for Neweb Customization.""",
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
	'category': 'Uncategorized',
	'depends': ['base', 'sale', 'purchase', 'hr', 'product', 'stock','neweb_project','google_calendar'],
	'data': [
		# 'views/neweb_base.xml',
		#'security/base_security.xml',
		'security/ir.model.access.csv',
		# 'views/web_custom_style.xml',
		'views.xml',
		'templates.xml',
		# 'views/customer_category.xml',
		'views/neweb_base_menuitem.xml',
		'views/hr_view.xml',
		'views/res_partner_view.xml',
		'views/qa.xml',
		'views/sla.xml',
		'views/value_added_service.xml',
		'views/maintenance_category.xml',
		# 'views/maintenance_target.xml',
		# 'views/regular_inspection_type.xml',
		# 'views/product_view.xml',
		'views/sla_inherit.xml',
		'wizards/custom_credit_wizard.xml',
		'wizards/custom_credit_import_wizard.xml',
	],
	'demo': [
		'demo.xml',
	],
	'qweb': [
		"static/src/xml/*.xml",
	],
	'description': u'<4.1>.Neweb 合約/報修基礎模組',
	'summary': u'<4.1>.Neweb 合約/報修基礎模組',
	'installable': True,
	'application': True,

}
