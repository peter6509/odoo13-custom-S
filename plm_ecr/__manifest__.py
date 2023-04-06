# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).


{
    'name': 'ECR Order for PLM',
    'version': '12.0.1',
    'summary': 'For Company employee use ECR order trigger ECO',
    'description': 'Employee can create ECR Order to Engineer Check..generate to ECO Order',
    'category': 'Tools',
    'author': 'JasonWu(jaronemo@msn.com)',
    'license': 'GPL-3',
    'depends': ['mrp_plm', 'report_py3o'],
    'data': ['security/ir.model.access.csv',
             'data/plm_ecr_sequence.xml',
             'data/reminder_email_template.xml',
             'views/plm_ecr_reason.xml',
             'views/plm_ecr.xml',
             'report/plm_ecr_report.xml'],
    'installable': True,
    'auto_install': False,
}