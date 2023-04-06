# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': '維護保養EXT',
    'license': 'LGPL-3',
    'version': '13.0',
     'sequence': 1,
    'category': 'maintenance repair',
    "website": "",
    "author": "ALLDO Technology",
    'depends': ['maintenance'],
    'data': ['security/maintenance_security.xml',
             'security/ir.model.access.csv',
             'views/maintenance_equipment_inherit.xml',
             'views/maintenance_request_inherit.xml',

             ],
    'application': True,
    'installable': True,
    'description': '維護保養EXT',
    'summary': '維護保養EXT',
}

