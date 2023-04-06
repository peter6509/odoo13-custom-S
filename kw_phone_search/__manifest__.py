{
    'name': 'Advanced contact search by name email and phone',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '13.0.0.0.1',

    'depends': [
        'phone_validation', 'kw_mixin', 'kw_phone',
    ],
    'data': [
        'views/partner_view.xml',
        'views/res_config_settings_view.xml',
    ],
    'installable': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'live_test_url': 'https://kw-phone.demo13.kitworks.systems',
}
