# -*- coding: utf-8 -*-
# Author : Peter Wu

{
    'name': 'Openacademy',
    'version': '12',
    'sequence': 200,
    'category': 'Student Academy Score system',
    'website': 'https://www.alldo.com.tw',
    'summary': 'Student Academy Score system',
    'description': """
     學生成績系統
""",
    'depends': ['sale'

                ],
    'data': [
        'security/ir.model.access.csv',
        'security/openacademy_security_rule.xml',
        # 'security/openacademy_security_rule1.xml',
        # 'security/openacademy_score_rule.xml',
        'views/openacademy_teacher.xml',
        'views/openacademy_class.xml',
        'views/openacademy_student.xml',
        'views/openacademy_score.xml',
        'views/openacademy_course.xml',
        'views/openacademy_student_inherit.xml',
        'views/openacademy_student_inherit1.xml',
        # 'wizards/openacademy_student_search_wizard.xml',
        'views/openacademy_class_inherit.xml',
        'views/openacademy_student_inherit2.xml',
        'views/openacademy_score_inherit.xml',
        'views/openacademy_score_inherit1.xml',
        'views/openacademy_respartner_inherit.xml',
        # 'views/openacademy_download_file.xml',
        # 'wizards/openacademy_student_export.xml',
        'data/openacademy_course_list.xml',
        # 'wizards/openacademy_score_import_wizard.xml',
        # 'reports/openacademy_studentclass_report.xml',
        # 'reports/openacademy_report.xml',

        'views/openacademy_menu.xml',

    ],

    'installable': True,
    'application': True,
}
