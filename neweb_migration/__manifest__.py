# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': '<99>.NEWEB V10-V13 Migration模組',
    'license': 'LGPL-3',
    'version': '13.0',
    'category': 'Project management',
    'sequence': 99,
    "website": "http://www.lansir.com.tw",
    "author": "ALLDO Technology",
    'depends': ['neweb_base','neweb_contract','neweb_project','neweb_purchase','neweb_stockin'],
    'data': [ 'security/ir.model.access.csv',
              # 'views/migration_config.xml',
              # 'wizards/migration_base1_wizard.xml',
              # 'wizards/migration_base2_wizard.xml',
              # 'wizards/migration_base3_wizard.xml',
              # 'wizards/migration_proj1_wizard.xml',
              # 'wizards/migration_proj2_wizard.xml',
              # 'wizards/migration_proj3_wizard.xml',
              # 'wizards/migration_base4_wizard.xml',
              'views/migration_contractline.xml',
              'views/migration_menu.xml',
             ],

    'application': True,
    'installable': True,
    'description': '<99>.NEWEB V10-V13 Migration模組',
    'summary': '<99>.NEWEB V10-V13 Migration模組',
}