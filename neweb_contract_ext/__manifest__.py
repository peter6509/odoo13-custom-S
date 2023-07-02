# -*- coding: utf-8 -*-
# Author : Peter Wu

# -*- coding: utf-8 -*-
{
	'name': u'<5.2>.NEWEB 合約管理擴充模組',
	'version': '13.0',
	'summary': "Contract EXT Management",
	'sequence': 8,
	'description': """
Neweb Contract
==============
Specially designed Contract EXT Management Module for Neweb.""",
    "website": "http://www.lansir.com.tw",
    "author": "ALLDO Technology",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'neweb_base','neweb_project','neweb_contract'],

    # always loaded
    'data': ['security/ir.model.access.csv',
             'data/contract_mail_template1.xml',
             'views/neweb_contract_contract_inherit.xml',
             'views/neweb_contract_contract_inherit1.xml',
             'views/neweb_contract_contract_inherit2.xml',
             'views/neweb_contract_contract_inherit3.xml',

             'views/neweb_contract_contract_inherit4.xml',
             'views/neweb_contract_contract_inherit5.xml',
             'views/neweb_contract_contract_inherit6.xml',
             'wizards/neweb_contract_inherit_wizard.xml',
             'wizards/neweb_contract_inherit_wizard.xml',
             'views/neweb_contract_contract_inherit7.xml',
             'views/neweb_contract_selline.xml',
    ],

    'description' : u'<5.2>.NEWEB 合約管理擴充模組',
    'summary': u'<5.2>.NEWEB 合約管理擴充模組',
    'installable': True,
    'application': True,

}
