import json

from utils import data_read


def list_contact(info):
    try:
        if info != None:
            print(json.loads(data_read())[info.strip('"')])
        else:
            print(json.loads(data_read()))

    except json.decoder.JSONDecodeError:
        print('Справочник пуст, нечего показать.')
