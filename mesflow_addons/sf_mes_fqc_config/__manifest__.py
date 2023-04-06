# _*_ coding: utf-8 _*_

{
    'name': u'FQC質檢配置',
    'license': 'LGPL-3',
    'version': '13.0.1',
    'category': 'MES ASSEMBLY LINE',
    'depends': ['mes_assembly','report_py3o'],
    'data': [
        'security/ir.model.access.csv',
        'views/inspection_qc_config.xml',
        'views/inspection_fqc_order.xml',
        'views/mes_mo_menu.xml',
        'report/mes_fqc_report.xml',

             ],

    'application': True,
    'installable': True,
    'description': u'FQC質檢配置',
    'summary': u'FQC質檢配置',
}