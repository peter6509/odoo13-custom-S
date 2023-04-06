# -*- coding: utf-8 -*-
# Author : Peter Wu

# -*- coding: utf-8 -*-
{
	'name': u'<9>.NEWEB 樞鈕分析',
	'version': '13.0',
	'summary': "Neweb Pivot Management",
	'sequence': 12,
	'description': """
Neweb Pivot Analysis
==============
Specially designed repair pivot/project pivot/contract pivot Management Module for Neweb.""",
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'neweb_base','neweb_project','neweb_contract','neweb_repair'],

    # always loaded
    'data': ['security/ir.model.access.csv',
             # 'data/neweb_pivot_data.xml',
             'views/neweb_pivot_menu.xml',
             'views/neweb_pivot_repair.xml',
             'views/neweb_pivot_project.xml',
             'views/neweb_pivot_project1.xml',
             'security/neweb_pivot_security.xml',

    ],

    'description' : '<9>.NEWEB 樞鈕分析模組',
    'summary': '<9>.NEWEB 樞鈕分析模組',
    'installable': True,
    'application': True,

}
