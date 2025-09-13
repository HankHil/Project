import json

from utils import data_read


def list_contact(name):
    try:
        if name:
            print(json.loads(data_read())[name.strip('"')])
        else:
            print(json.loads(data_read()))

    except json.decoder.JSONDecodeError:
        print('Справочник пуст, нечего показать.')
    except KeyError:
        print('Такого контакта нет в справочнике.')
