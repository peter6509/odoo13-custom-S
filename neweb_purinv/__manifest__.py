# -*- coding: utf-8 -*-
# Author : Peter Wu

{

    'name': '<10>.NEWEB 請款申請作業',
    'license': 'LGPL-3',
    'version': '13.0',
    'category': 'Invoice management',
    'sequence': 13,
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    'depends': ['base', 'sale', 'neweb_project', 'purchase', 'hr'],
    'description': '<10>.NEWEB 請款申請作業',
    'summary': '<10>.NEWEB 請款申請作業',
    'data': ['security/ir.model.access.csv',
             'security/neweb_purinv_security.xml',
             'data/ir_sequence_data.xml',
             # 'wizards/neweb_pur_uninv_select.xml',
             'wizards/neweb_pur_uninv_wizard.xml',
             'views/neweb_pur_invoice.xml',
             'views/neweb_pur_invoice_inherit.xml',
            ],
    'installable': True,
    'application': True,
}
