# -*- coding: utf-8 -*-
# Author : Peter Wu

{
	'name': u"<6>.NEWEB 業務業績分析模組",
	'version': '13.0',
	'summary': "Sale Analysis",
	'sequence': 9,
	'description': """
Neweb Sale Analysis Module
==============
Specially designed Repair Module for Neweb.""",
    "website": "http://www.odootw.com",
    "author": "ALLDO Technology",

	'category': 'Uncategorized',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base', 'neweb_base', 'sale'],

	# always loaded
	'data': [
		     'security/ir.model.access.csv',
		     'security/neweb_expense_security.xml',
		     'security/neweb_travel_security.xml',
		     'views/crm_team_menu.xml',
			 'views/crm_team_targetgp.xml',
			 # 'data/ir_sequence_data.xml',
		     'data/neweb_op_program_data.xml',
		     'data/neweb_expense_flow_message.xml',
		     'data/neweb_travel_flow_message.xml',
		     'views/neweb_expense_report.xml',
		     'views/neweb_official_doc.xml',
		     'wizards/sale_analysis_wizard.xml',
		     'views/crm_team_saleanalysis.xml',
		     'data/neweb_expense_data.xml',
		     'views/neweb_expenseitem_config.xml',
		     'views/neweb_expenseevent_config.xml',
		     'views/neweb_expensedoc_config.xml',
             'views/neweb_travel_report.xml',
		     'views/neweb_travel_report_inherit.xml',
		     'views/neweb_sale_analysis_excel_download.xml',
		     'views/neweb_op_program.xml',
		     'views/neweb_group_member.xml',
		     'views/neweb_pith_doc.xml',
	],
	# # only loaded in demonstration mode
	# 'demo': [
	# 	'demo.xml',
	# ],
	'description': u"<6>.NEWEB 業務業績分析模組",
	'summary' : u"<6>.NEWEB 業務業績分析模組",
	'installable': True,
	'application': True,
}
