# -*- coding: utf-8 -*-
# Author: Peter Wu

{
    'name': u'<1.1>.NEWEB 銷售/專案管理模組',
    'license': 'LGPL-3',
    'version': '13.0',
     'sequence': 1,
    'category': 'Project management',
    "website": "http://www.odootw.com",
    "author": "ALLDO Technology",
    'depends': ['base','sale','purchase','hr'],
    'data': [
             'security/neweb_security.xml',
             'security/ir.model.access.csv',
             # 'security/res_partner_security.xml',
             'views/respartner_inherit.xml',
             'wizards/neweb_balance_check.xml',
             'wizards/neweb_import_wizard.xml',
             'views/neweb_project.xml',
             'wizards/neweb_projitem_select.xml',
             'views/neweb_assign.xml',
             'views/neweb_prodset_config.xml',
             'views/neweb_buscate_config.xml',
             'views/neweb_projmaintype_config.xml',
             'views/neweb_engmaintype_config.xml',
             'views/neweb_contacttype_config.xml',
             'wizards/neweb_assign_wizard.xml',
             'data/neweb_project_data.xml',
             'views/neweb_projbranch_config.xml',
             'views/neweb_gencode_config.xml',
             'views/neweb_costtype_config.xml',
             'views/neweb_prodbrand_config.xml',
             'wizards/neweb_engassignwork_wizard.xml',
             'wizards/neweb_engcomplete_wizard.xml',
             # 'views/neweb_project_inherit.xml',    # 移除
             'views/neweb_transationtype_config.xml',
             'views/neweb_assservicemode_config.xml',
             'views/neweb_assservicetype_config.xml',
             'views/neweb_stockmove_menu.xml',
             'wizards/neweb_saletoproj_wizard.xml',
             'wizards/neweb_sale_import_wizard.xml',
             'views/neweb_sale_inherit.xml',      # 要重寫
             'views/neweb_sale_categ.xml',
             'data/neweb_assign_emailtemplate.xml',
             'wizards/neweb_projsaleitem_export.xml',
             'views/neweb_project_search.xml',
             'security/neweb_project_menu_security.xml', # 要重寫
              'security/neweb_engassign_security.xml',
              'security/neweb_project_security.xml',   # 要重寫
              'data/neweb_project_approve_mail.xml',
              'data/neweb_project_reject_mail.xml',
              'data/neweb_eng_assign_approve_mail.xml',
              'data/neweb_eng_assign_reject_mail.xml',
              'data/sale_order_data.xml',
              'views/neweb_quotationinclude_config.xml',
              'views/neweb_callserviceresponse_config.xml',
              'wizards/partner_import_wizard.xml',
              'views/neweb_paymentterm_config.xml',
              'views/warranty_service_rule_config.xml',
              'views/main_service_rule_config.xml',
              'views/routine_main_rule_config.xml',
              'views/neweb_sale_order_inherit.xml',  # 要重寫
              'views/neweb_project_inherit1.xml',  #mark
              # 'views/respartner_inherit1.xml',  # 移除
              'views/neweb_sale_inherit1.xml',  # 要重寫
              'views/neweb_assign_inherit.xml',
              'views/neweb_sale_inherit2.xml',   # 要重寫
              'views/neweb_import_download.xml',
              'views/neweb_sale_inherit3.xml',   # 要重寫
              'views/respartner_inherit2.xml',
              'views/neweb_assign1.xml',
              'views/neweb_assign_inherit.xml',
              'views/neweb_assign_inherit1.xml',
              # 'views/neweb_project_inherit2.xml', # prod_revenue readonly  # 移除
              'views/neweb_export_download.xml',
              'views/neweb_sitem_modeltype1.xml',

             ],
    'application': True,
    'installable': True,
    'description': u'<1.1>.NEWEB 銷售/專案管理模組',
    'summary': u'<1.1>.NEWEB 銷售/專案管理模組',
}
