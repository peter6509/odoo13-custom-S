# -*- coding: utf-8 -*-
# Author : Peter Wu

{
	'name': u'<96>.NEWEB Finereport',
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
    'data': ['security/neweb_bi_security.xml',
              'views/neweb_finereport_menu.xml',
    ],

    'description' : '<96>.NEWEB Finereport',
    'summary': '<96>.NEWEB Finereport',
    'installable': True,
    'application': True,}
