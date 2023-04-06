# -*- coding: utf-8 -*-
{
    'name': "acme_finereports",

    'summary': """
         正璽 FineReport TEST """,

    'description': """
         正璽 FineReport TEST

    """,

    'author': "Peter",
    'website': "https://www.alldo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ACME',
    'version': '0.13',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    # always loaded
    'data': [
        # 'security/report_security.xml',
        # 'security/ir.model.access.csv',
        # 'wizard/routing_inspection_report_wizard_view.xml',
        # 'wizard/production_summary_report_wizard_view.xml',
        # 'wizard/pcr_stock_report_wizard_view.xml',
        # 'wizard/pcr_process_line_report_wizard_view.xml',
        # 'views/zimo_reports.xml',
        # 'views/mrp_routing_view.xml',
        # 'views/pcr_process_line_report_view.xml',

        # 'views/production_summary_report_view.xml',
        # 'views/pcr_stock_report_view.xml',
        # 'views/routing_inspection_report_view.xml',
        'wizard/acme_last10_shipping_wizard.xml',
        'wizard/acme_last10_prod_wizard.xml',
        'wizard/acme_last10_qc_wizard.xml',
        'views/acme_finereport_menu.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable':True, #是否启用安装,通常固定为True
    'auto_install':False,#建库时是否自动安装
    'application':True,#是否为应用程序
}