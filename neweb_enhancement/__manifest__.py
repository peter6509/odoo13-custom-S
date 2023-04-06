# -*- coding: utf-8 -*-
# Author : Peter Wu

# -*- coding: utf-8 -*-
{
	'name': u'<1.3>.NEWEB Enhancement Function',
	'version': '13.0',
	'summary': "Neweb Enhancement Function",
	'sequence': 2,
	'description': """
Neweb Enhancement Function
==============
Specially Function Module for Neweb.""",
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','neweb_project'],

    # always loaded
    'data': ['security/ir.model.access.csv',
             'views/neweb_security_download.xml',
             'wizards/neweb_security_export.xml',
             'wizards/neweb_migration_dept.xml',
             'views/neweb_sale_purchase_account_setting.xml',
             'views/neweb_hr_job_postype.xml',
             'wizards/user_conflict_group_wizard.xml',

    ],

    'description' : u'<1.3>.NEWEB Enhancement Function',
    'summary': u'<1.3>.NEWEB Enhancement Function',
    'installable': True,
    'application': True,

}
