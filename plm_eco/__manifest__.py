# -*- coding: utf-8 -*-
# Author: Jason Wu (jaronemo@msn.com)
{
    'name': 'ECO Order',
    'version': '12.0.1',
    'summary': 'For PLM Module add some functions',
    'description': 'For PLM use some functions',
    'category': 'Tools',
    'author': 'Jason Wu(jaronemo@msn.com)',
    'depends': ['mrp_plm', 'report_py3o', ],
    'data': [
        'data/plm_eco_reason_data.xml',
        'data/reminder_email_template.xml',
        'data/reminder_scheduler.xml',
        'security/plm_eco_security.xml',
        'security/ir.model.access.csv',
        'views/mrp_eco_product_list.xml',
        'views/mrp_eco.xml',
        'views/plm_eco_reason.xml',
        'views/mrp_bom.xml',
        'report/plm_eco_report.xml',
        'wizard/approve_change_wizard.xml'
    ],
    'installable': True,
    'auto_install': False,
}
