# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': u'<1.4>.NEWEB 成本分析/合約 整合模組',
    'license': 'LGPL-3',
    'version': '13.0',
    'category': 'Project ＆ contract management',
    'sequence': 9,
    "website": "http://www.lansir.com.tw",
    "author": "LANSIR Technology",
    'depends': ['base', 'neweb_project','neweb_contract'],
    'data': ['wizards/neweb_project_analysis_wizard.xml',
             'views/neweb_project_revenue_cost.xml',
             'security/ir.model.access.csv',
             'views/neweb_project_revenue_search.xml',
             'views/neweb_stock_move_inherit.xml',
             'reports/revenue_analysis_report.xml',
             'reports/cost_analysis_report.xml',
             'security/neweb_project_contract_menu_security.xml',
             ],
    'application': True,
    'installable': True,
    'description': '<1.4>.NEWEB 成本分析/合約 整合模組',
    'summary': '<1.4>.NEWEB 成本分析/合約 整合模組'
}