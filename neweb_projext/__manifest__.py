# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': u'<1.2>.NEWEB 專案管理擴充模組',
    'license': 'LGPL-3',
    'version': '13.0',
     'sequence': 2,
    'category': 'Project EXT management',
    "website": "http://www.odootw.com",
    "author": "ALLDO Technology",
    'depends': ['base','neweb_project'],
    'data': ['security/ir.model.access.csv',
             'security/neweb_saleorder_download_security.xml',
             'security/neweb_partner_export_security.xml',
             'security/res_partner_security.xml',
             'views/neweb_sale_inherit4.xml',     # 要重寫
             'views/neweb_project_inherit.xml',     # 臨時mark
             'views/neweb_project_inherit1.xml',    # 臨時mark
             'views/neweb_project_inherit5.xml',    # 臨時mark
             'views/neweb_project_inherit6.xml',    # 臨時mark
             'views/neweb_project_inherit7.xml',    # 臨時mark
             'views/neweb_partner_menu.xml',
             # 'views/neweb_sale_inherit5.xml',   # 要重寫
             # 'security/neweb_projext_menu_security.xml',
             'security/neweb_engassign_security.xml',
             'views/neweb_partner_inherit.xml',   # 要重寫
             'views/neweb_project_inherit8.xml',    # 臨時mark
             'wizards/goto_project_wizard.xml',
             'views/neweb_project_inherit9.xml',     # 臨時mark
             'wizards/neweb_sale_import_inherit_wizard.xml',
             'views/neweb_project_inherit10.xml',  # 要重寫
             'views/neweb_project_inherit11.xml',     # 臨時mark
             'wizards/neweb_project_import_wizard.xml',
             'views/neweb_project_inherit12.xml',   # 臨時mark
             'views/neweb_project_inherit13.xml',   # 要重寫
             # 'views/neweb_project_inherit14.xml',   # 要重寫
             'data/neweb_cost_dept_data.xml',
             'data/neweb_birthday_data.xml',
             'views/neweb_cost_dept.xml',
             'views/neweb_project_inherit15.xml',   # 要重寫
             'views/neweb_partner_inherit1.xml',
             'views/neweb_partner_export_download.xml',
             'wizards/neweb_partner_export_wizard.xml',
             'views/neweb_project_inherit16.xml',     # 臨時mark
             'wizards/partner_change_sale_wizard.xml',
             'views/neweb_sale_inherit6.xml',       # 要重寫
             'views/neweb_project_inherit17.xml',     # 臨時mark
             # 'views/neweb_res_partner_inherit.xml',
             'views/neweb_sale_inherit7.xml',
             'views/neweb_assign_inherit.xml',
             'wizards/neweb_partner_export_wizard1.xml',
             'wizards/neweb_partner_export_wizard2.xml',
             'views/neweb_res_partner_inherit2.xml',
             'views/neweb_open_account_day1.xml',
             'data/neweb_open_account_day.xml',
             'views/neweb_sale_inherit8.xml',
             'views/neweb_project_inherit18.xml',
             'wizards/custom_credit_wizard.xml',
             'security/neweb_openaccountday1_rule.xml',
             'security/neweb_project_acceptanced_rule.xml',
             'views/neweb_project_inherit19.xml',
              'views/repair_support_maillist.xml',
             ],
    'application': True,
    'installable': True,
    'description': u'<1.2>.NEWEB 專案管理擴充模組',
    'summary': u'<1.2>.NEWEB 專案管理擴充模組',
}
