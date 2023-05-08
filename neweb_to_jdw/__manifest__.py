# -*- coding: utf-8 -*-
# Author : Peter Wu

{
	'name': u'<97>.NEWEB Odoo to 筋斗雲匯出精靈',
	'version': '13.0',
	'summary': "Odoo export CSV For JDW",
	'sequence': 100,
	'description': """
Neweb Contract
==============
Employee Timesheet management Module for Neweb.""",
    "website": "http://www.odootw.com.tw",
    "author": "AllDo Technology",
    'category': 'Uncategorized',
    'version': '10',
    'depends': ['base','sh_message'],
    'data': ['security/ir.model.access.csv',
             'view/jdw_download.xml',
             'wizards/neweb_custom_export_wizard.xml',
             'wizards/neweb_dev_export_wizard.xml',
             'wizards/neweb_contract_export_wizard.xml',
             'wizards/neweb_contractline_export_wizard.xml',
             'view/jdw_menu.xml',
    ],

    'description' : '<97>.NEWEB Odoo to 筋斗雲匯出精靈',
    'summary': '<97>.NEWEB Odoo to 筋斗雲匯出精靈',
    'installable': True,
    'application': True,}

