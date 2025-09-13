import json

from utils import data_read, data_write


def delete_contact(info):
    try:
        contacts = json.loads(data_read())
        contacts.pop(info.strip('"'))

        data_write(contacts)

    except json.decoder.JSONDecodeError:
        print('Справочник пуст, нечего удалять.')
    except AttributeError:
        print('Не указан контакт для удаления.')
    except KeyError:
        print('Такого контакта в справочнике нет.')
