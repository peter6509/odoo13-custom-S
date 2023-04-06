# -*- coding: utf-8 -*-
{
	'name': u"<4.2>.NEWEB 報修管理模組",
	'version': '1.0',
	'summary': "Repair",
	'sequence': 6,
	'description': """
Neweb Repair
==============
Specially designed Repair Module for Neweb.""",
    "website": "http://www.odootw.com",
    "author": "ALLDO Technology",

	'category': 'Uncategorized',
	'version': '0.1',

	# any module necessary for this one to work correctly
	'depends': ['base', 'neweb_base', 'neweb_contract'],

	# always loaded
	'data': [
		'security/ir.model.access.csv',
		'security/repair_security.xml',
		'data/repair_mail_template.xml',
		'data/repair_sequence.xml',
		'data/repair_questionnaire_data.xml',
		'views/questionnaire.xml',
		'views/repair.xml',
		'views/contract_view.xml',
		# 'views/repair_workflow.xml',  # 要修改
		'report/repair_report_view.xml', # 要修改
		'print/repair_print_report.xml', # 要修改
		'print/repair_print_template.xml',
		'print/repair_work_template.xml',
		'views/repair_parts_categ.xml',
		'views/repair_search.xml',
		'views/repair_inherit.xml',
		'wizards/tracking_parts_wizard.xml',
		'wizards/change_parts_wizard.xml',
		'views/repair_member.xml',
		'views/repair_inherit1.xml',
		'views/neweb_repeatcall_excel_download.xml',
		'wizards/neweb_repair_repeat_wizard.xml',
		'views/repair_inherit2.xml',
		'wizards/neweb_care_call_report.xml',
	],
	# # only loaded in demonstration mode
	# 'demo': [
	# 	'demo.xml',
	# ],
	'description': u"<4.2>.NEWEB 報修管理模組",
	'summary' : u"<4.2>.NEWEB 報修管理模組",
	'installable': True,
	'application': True,
}
