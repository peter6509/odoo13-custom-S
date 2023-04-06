# -*- coding: utf-8 -*-
{
	'name': u'<5.1>.NEWEB 合約管理模組',
	'version': '13.0',
	'summary': "Contract Management",
	'sequence': 7,
	'description': """
Neweb Contract
==============
Specially designed Contract Management Module for Neweb.""",
    "website": "http://www.lansir.com.tw",
    "author": "ALLDO Technology",
    'category': 'CONTRACT MANAGEMENT',
    'version': '0.1',
    'depends': ['base', 'neweb_base'],

    # always loaded
    'data': [
        # 'security/contract_security.xml',
        'security/ir.model.access.csv',
        'views/contract.xml',
        'views/contract_line.xml',
        'data/contract_mail_template.xml',
        'data/contract_ir_cron.xml',
        'data/contract_sequence.xml',
        # 'views/contract_workflow.xml',
        # 'report/contract_report_view.xml', # 要改
        'wizards/neweb_contract_wizard.xml',
        'wizards/neweb_contractline_wizard.xml',
        'views/contract_inherit.xml',
        'views/contract_security_inherit.xml',
        # 'views/contract_search.xml',  # 不需要了
        # 'security/neweb_contract_is_closed_domainforce.xml',
        'views/contract_excel_deonload.xml',
        'wizards/neweb_excel_export_wizard.xml',
        'security/contract_exceldownload_security.xml',
        'wizards/neweb_maincontract_export_wizard.xml',
        'wizards/neweb_modeltype1_import_wizard.xml',
        'views/contract_hd_line.xml',
        'views/contract_cpu_line.xml',
        'views/contract_ram_line.xml',
        'views/contract_expand_card_line.xml',
        'views/contract_power_line.xml',

    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo.xml',
    # ],
    'description' : u'<5.1>.NEWEB 合約管理模組',
    'summary': u'<5.1>.NEWEB 合約管理模組',
    'installable': True,
    'application': True,

}
