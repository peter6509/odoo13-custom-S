# -*- coding: utf-8 -*-

{
    'name': 'add fields in Lead/Opportunity tree view',
    'version': '1.0',
    'category': 'Sale',
    'author': 'Teknovative Solution',
    'summary': 'add fields in Lead/Opportunity tree view',
    'website': 'http://www.teknovatesolutions.com/',
    'images': [],
    'depends': ['crm','contacts'],
    'data': [
        'view/crm_lead_tree.xml',
        'view/res_partner_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

