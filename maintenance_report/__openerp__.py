# -*- coding: utf-8 -*-
# Author: Peter Wu

{
    'name': u'生產設備維修履歷報告',
    'license': 'LGPL-3',
    'version': '1.0',
    'category': 'Manufacturing',
    'author': 'Peter Wu',
    'depends': ['mrp_maintenance', 'stock'],
    'data': ['security/mreport_security.xml',
             'wizard/msearch_wizard.xml',
             'wizard/mreport_wizard.xml',
             'wizard/mmonth_wizard.xml',
             'wizard/mproduct_wizard.xml',
             'report/report.xml',
             'report/mreport_template.xml',
             'report/mmonth_template.xml',
             'report/mproduct_template.xml',
             'security/ir.model.access.csv',
             'views/mreport_pivot.xml',
             'views/maintenance_menu.xml',
             'views/main_kanban_inherit.xml',
             'views/main_month_pivot.xml',
             'wizard/mmonth_pivot.xml',
             'views/main_team_group.xml',
             'security/maintenance_team.xml',
             'views/main_equipment_inherit.xml',
             'wizard/super_main_mod.xml',
             'views/main_request_inherit.xml',
             'views/main_his_pivot.xml',
             'wizard/mainhis_pivot_wizard.xml',
             ],
    # 'css':['static/src/css/base.css'],
    'application': True,
    'installable': True,
    'summary': u'生產設備維修履歷查詢',
}