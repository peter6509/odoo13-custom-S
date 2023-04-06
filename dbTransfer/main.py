# -*- coding: utf-8 -*-
import os
import importlib
import configparser as cfp
from globalVars import GlobalVars

__globals = globals()
__globals['module'] = {}
config = cfp.ConfigParser()
gv = GlobalVars()
db = {
    'resource': {
        'dbname': 'NEWEB',
        'host': 'localhost',
        'port': '5432',
        'user': 'odoo',
        'password': 'odoo',
    },
    'target': {
        'dbname': 'NEWEB13',
        'host': 'localhost',
        'port': '5433',
        'user': 'postgres',
        'password': 'odoo',
    }
}


def load_config():
    print('config.conf')
    path = 'config.conf'
    if os.path.exists(path):
        config.read(path)
        sections = config.sections()

        for k in db:
            if k not in sections:
                print(f'config.conf havn\'t "{k}" section')
                exit(0)
            else:
                v = db[k]
                section = config[k]
                for i in v.keys():
                    db[k][i] = section.get(i) if section.get(i) else input(f'Input {k} {i}:')

    else:
        print('Not config.conf on folder')
        exit(0)


def load_modules():
    """ dynamic load ./models/*.py"""
    model_path = 'models'
    if not os.path.exists(model_path):
        print('folder "models" not exist!')
        exit(0)

    models = os.listdir(model_path)

    for m in filter(lambda x: True if '.py' in x else False, models):
        mod_name = m[:-3]  # remove ".py"
        mod = __globals[mod_name] = importlib.import_module(f'models.{mod_name}', package=__name__)
        __globals['module'][mod.name] = mod


def link_db():
    for k in db:
        v = db[k]
        for i in v:
            config_value = v[i]
            if not config_value:
                config_value = input(f'Input {k} {i}:')
                db[k][i] = config_value

        connect_info = " ".join([f'{i}={db[k][i]}' for i in db[k]])
        db[k]['connection'] = connect_info

    gv.setOrUpdateVar(db)


def menu():
    keys = __globals['module'].keys()
    symbol = '='
    title = f'{symbol * 10} Menu {symbol * 10}'
    print(title)
    for i, k in enumerate(keys, start=1):
        print(f"{i}. {k}")
    print(symbol * len(title))
    print('If you want to exit, input "exit" or "bye"')

    while True:
        choose = input('Select: ')

        if choose in ['bye', 'exit']:
            gv.clearAllVars()
            print('See ya!')
            exit(0)

        try:
            choose = int(choose)
        except:
            print('Expect int, but got str! please choose again.')
            continue

        if choose > len(keys) or choose < 1:
            print('Select number haven\'t model! Please choose again.')
        else:
            key = list(keys)[choose - 1]
            print(f'Your select module {key}')
            __globals['module'][key].run()


if '__main__' == __name__:
    load_config()
    load_modules()
    link_db()
    menu()
