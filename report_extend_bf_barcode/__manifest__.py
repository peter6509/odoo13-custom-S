# -*- coding: utf-8 -*-

{
    'name': 'Dinamic Barcode All models',
    'description': 'Dinamic Generate Barcode All models',
    'summary': 'Dinamic Barcode All models, professional report, simple report designer, ideal for contracts, report barcode.',
    'category': 'All',
    'version': '1.0',
    'website': 'http://www.buildfish.com/',
    "license": "AGPL-3",
    'author': 'BuildFish',
    'depends': [
        'report_extend_bf',
        "sale_management",
        'stock',
        'purchase',
    ],
    'data': [
        'data/templates.xml',
        'report.xml',
        'views/barcode_template_views.xml',
        'views/barcode_views.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
    ],
    'live_test_url': 'https://youtu.be/bzlLr1tEiA0',
    'price': 10.00,
    'currency': 'EUR',
    'images': ['static/description/banner.png'],
    'application': True,
}
