# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': "CloudRent 租屋住戶管理模組",
    'version': '13.0',
    'summary': "CloudRent 租屋住戶管理模組",
    'description': """CloudRent 租屋住戶管理模組(住戶日用電度數記錄/租戶儲值收款記錄/費用對帳記錄Line租戶)""",
    'author': "ALLDO Technology CO.,LTD.",
    'category': 'CloudRent HouseHold Manager',
    'depends': ['sh_message'],
    'data': [ 'data/cloudrent_payment_item.xml',
              'data/cloudrent_payment_month.xml',
              'data/cloudrent_equip_part.xml',
              'data/cloudrent_repair_sequence.xml',
              'data/cloudrent_equip_part.xml',
              'security/cloudrent_security.xml',
              'security/cloudrent_security1.xml',
              'security/line_notify_group.xml',
              'security/ir.model.access.csv',
              'security/cloudrent_household_rule.xml',
              'views/cloudrent_household_member.xml',
              'views/cloudrent_household_house.xml',
              'views/cloudrent_household_line.xml',
              'views/cloudrent_household_config.xml',
              'views/cloudrent_household_bill_line.xml',
              'views/cloudrent_household_bill_line_his.xml',
              'wizards/line_notify_send.xml',
              'wizards/mon_amount_report_wizard.xml',
               'reports/cloudrent_bill_templates.xml',
              'reports/mmonth_template.xml',
              'reports/cloudrent_bill_reports.xml',
              'wizards/cloudrent_household_payment.xml',
              'wizards/cloudrent_month_report_wizard.xml',
              'wizards/cloudrent_maintennance_report_wizard.xml',
              'reports/maintenance_template.xml',
              'wizards/cloudrent_start_scale_wizard.xml',
              'wizards/cloudrent_member_line_wizard.xml',
              'wizards/cloudrent_household_previous_balance_wizard.xml',
              'wizards/cloudrent_household_mixsearch.xml',
              'views/cloudrent_emeter_mixsearch_line.xml',
              'views/cloudrent_excel_download.xml',
              'views/cloudrent_member_payment.xml',
              'wizards/cloudrent_contract_wizard.xml',
              'views/cloudrent_emeterhub.xml',
              'wizards/cloudrent_memberout_wizard.xml',
              'wizards/cloudrent_escaletot_wizard.xml',
              'wizards/cloudrent_memberin_wizard.xml',
              'views/cloudrent_household_landlord.xml',
              # 'views/cloudrent_household_member_history.xml',
              'views/cloudrent_equip_part.xml',
              'wizards/cloudrent_repair_grant_wizard.xml',
              'views/cloudrent_menu.xml',
              'views/cloudrent_landlord_menu.xml',
              ],
    'installable': True,
    'application': True,

}
