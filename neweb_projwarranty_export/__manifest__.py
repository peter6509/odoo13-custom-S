# -*- coding: utf-8 -*-
# Author : Peter Wu

{
	'name': u'<1.5>.NEWEB成本分析產出保固表格',
	'version': '13.0',
	'summary': "NEWEB Project For Warranty Export",
	'sequence': 12,
	'description': """
Neweb Contract
==============
Neweb Project For Warranty Export Module.""",
    "website": "http://www.odootw.com.tw",
    "author": "AllDo Technology",
    'category': 'Invoicing',
    'version': '10',
    'depends': ['base', 'neweb_project','neweb_invoice'],
    'data': [ 'security/ir.model.access.csv',
              'views/neweb_projwarranty_export_download.xml',
              'wizards/neweb_projwarranty_export_wizards.xml',
              'views/neweb_projwarranty_menu.xml',


    ],

    'description' : '<1.5>.NEWEB成本分析產出保固表格',
    'summary': '<1.5>.NEWEB成本分析產出保固表格',
    'installable': True,
    'application': True,

}