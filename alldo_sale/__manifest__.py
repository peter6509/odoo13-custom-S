# -*- coding: utf-8 -*-
# Author: Peter Wu

{
    'name': u'<1>.AllDo銷售變更模組',
    'license': 'LGPL-3',
    'version': '13.0',
    'category': 'Sale Order management',
    "website": "http://www.alldo.com.tw",
    "author": "AllDo Technology",
    'depends': ['base','sale'],
     'data': [
              'security/ir.model.access.csv',
              'views/alldo_sale_inherit.xml',
              'views/alldo_sale_inherit1.xml',
              'data/alldo_data.xml',

             ],
    'application': True,
    'installable': True,
    'description': u'<1>.AllDo 銷售管理模組',
    'summary': u'<1>.AllDo 銷售管理模組',
}
