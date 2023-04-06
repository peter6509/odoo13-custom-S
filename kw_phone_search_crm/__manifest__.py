{
    'name': 'Advanced crm search by name email and phone',

    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '13.0.0.0.1',

    'depends': [
        'crm',
        'kw_phone_search',
    ],

    'data': [
        'views/views.xml',
    ],
    'installable': True,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'live_test_url': 'https://kw-phone.demo13.kitworks.systems',
}
