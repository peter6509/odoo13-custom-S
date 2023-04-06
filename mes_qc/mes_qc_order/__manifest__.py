# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)
{
    'name': 'MES FQC ORDER',
    'version': '13.0.1.0',
    'summary': 'For Manufacture Flow Quality Control',
    'description': 'Manufacture Flow Quality Control Order with Report Use',
    'category': 'Tools',
    'author': 'Jason Wu(jaronemo@msn.com)',
    'depends': ['base', 'mixmes_qc_config'],
    'data': ['data/mes_qc_order_seq.xml',
             'views/mes_qc_order.xml'],
    'installable': True,
    'auto_install': False,
}