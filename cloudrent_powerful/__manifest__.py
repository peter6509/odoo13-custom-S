# -*- coding: utf-8 -*-
##############################################################################
{
    "name": "CloudRent Workflow",
    "version": "13",
    'license': 'OPL-1',
    "website": "http://www.odootw.com",
    "depends": ["base","web", "calendar"],
    "author": "<Jon alangwansui@qq.com>",
    "category": "Tools",
    "description": """
       CloudRent Workflow Tool.
    """,
    "data": [
        'secureity/ir.model.access.csv',
        'views/wkf.xml',
        'wizard/wizard_wkf.xml',
    ],

    'demo':[
        'demo/wkf.base.csv',
        'demo/wkf.node.csv',
        'demo/wkf.trans.csv',
    ],
    #'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'active': True,
    'price': 150,
    'currency': 'EUR',
    'auto_install': True,
    'images': [
        'static/description/theme.jpg',
    ],

}
