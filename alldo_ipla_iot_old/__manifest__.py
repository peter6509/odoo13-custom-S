# -*- coding: utf-8 -*-
# Author : Peter Wu


{
    'name': u"ALLDO For IPLA IOT 工單管理模組",
    'version': '13.0',
    'summary': "ALLDO For IPLA IOT 工單管理模組",

    'description': """ALLDO For IPLA IOT 工單管理模組.... """,
    'author': "ALLDO Technology,Peter Wu",
    'category': 'Work Order',
    'depends': ['purchase','sale','product','stock', 'maintenance','sh_message','hr'],
    'data': [
             'security/ipla_iot_security.xml',
             'security/ir.model.access.csv',
             'views/ipla_iot_workorder.xml',
             'views/ipla_electronic_scale.xml',
             'views/ipla_equipment_feed.xml',
             'views/ipla_iot_bells.xml',
             'views/ipla_iot_company_stockloc.xml',
             'views/ipla_iot_empinfo.xml',
             'views/ipla_iot_employee.xml',
             'views/ipla_iot_equipstatusinfo.xml',
             'views/ipla_iot_excel_download.xml',
             'views/ipla_iot_equipperformance.xml',
             'views/ipla_iot_main_status.xml',
             'views/ipla_iot_manperformance.xml',
             'views/ipla_iot_outsuborder.xml',
             'views/ipla_iot_processing_view.xml',
             'views/ipla_iot_prodstock.xml',
             'views/ipla_iot_replaceline_list.xml',
             'views/ipla_iot_server.xml',
             'views/ipla_iot_stockmove_list.xml',
             'views/ipla_iot_workorder_performance.xml',
             'views/ipla_maintenance_inherit.xml',
             'views/ipla_maintenance_inherit1.xml',
             'views/ipla_product_template_inherit.xml',
             'views/stock_picking_inherit.xml',
             'wizards/emp_attendance_export_wizard.xml',
             'wizards/iot_init_pickle_wizard.xml',
             'wizards/iot_mo_action_wizard.xml',
             'wizards/iot_mo_start_wizard.xml',
             'wizards/iot_restart_wizard.xml',
             'wizards/iot_shutdown_wizard.xml',
             'wizards/ipla_iot_dbclear_wizard.xml',
             'wizards/ipla_iot_deployment_wizard.xml',
             'wizards/ipla_iot_empbarcode_wizard.xml',
             'wizards/ipla_iot_mixsearch.xml',
             'wizards/ipla_iot_mixsearch_replaceline.xml',
             'wizards/ipla_iot_mo_add.xml',
             'wizards/ipla_iot_ngreturn_excel_wizard.xml',
             'wizards/ipla_iot_ngreturn_report_wizard.xml',
             'wizards/ipla_iot_open_workorder.xml',
             'wizards/ipla_iot_prodstock_wizard.xml',
             'wizards/ipla_iot_replaceline_wizard.xml',
             'wizards/ipla_iot_shipping_excel_wizard.xml',
             'wizards/ipla_iot_stockmove_mixsearch.xml',
             'wizards/ipla_iot_wkorder_processing_wizard.xml',
             'wizards/ipla_iot_workorder_performance_wizard.xml',
             'wizards/ipla_outsourcing_in_wizard.xml',
             'wizards/ipla_outsourcing_out_wizard.xml',
             'wizards/outsourcing_inout_wizard.xml',
             'wizards/ipla_iot_po_stockin.xml',
             'reports/alldo_ipla_iot_empbarcode_report.xml',
             'reports/alldo_ipla_iot_equipstatusbarcode_report.xml',
             'reports/alldo_ipla_iot_ngreturn_report.xml',
             'reports/alldo_ipla_iot_outsourcing_report.xml',
             'reports/alldo_ipla_iot_report.xml',
             'reports/alldo_ipla_iot_shipping_report.xml',
             'reports/alldo_ipla_iot_wkorder_report.xml',
             'reports/alldo_ipla_iot_wkorder_report1.xml',
             'reports/alldo_ipla_iot_report.xml',
             'views/ipla_iot_menu.xml',
    ],
    'installable': True,
    'application': True,

}
