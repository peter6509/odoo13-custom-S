# -*- coding: utf-8 -*-
{
    'name': "huaguang_reports",

    'summary': """
         子墨报表--华光 """,

    'description': """
         子墨报表模块,用来展示报表应用.

    """,

    'author': "浙江子墨信息科技有限公司",
    'website': "https://www.zimo2018.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'zimo',
    'version': '0.14',

    # any module necessary for this one to work correctly
    'depends': ['base', 'zimo_pcr', 'mrp', 'rfid_huaguang'],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    # always loaded
    'data': [
        'security/report_security.xml',
        'security/ir.model.access.csv',
        'wizard/routing_inspection_report_wizard_view.xml',
        'wizard/production_summary_report_wizard_view.xml',
        'wizard/pcr_stock_report_wizard_view.xml',
        # 'wizard/pcr_process_line_report_wizard_view.xml',
        'views/zimo_reports.xml',
        # 'views/mrp_routing_view.xml',
        # 'views/pcr_process_line_report_view.xml',

        'views/production_summary_report_view.xml',
        'views/pcr_stock_report_view.xml',
        'views/routing_inspection_report_view.xml',
        'views/actions.xml',
        'views/menus.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable':True, #是否启用安装,通常固定为True
    'auto_install':False,#建库时是否自动安装
    'application':True,#是否为应用程序
}