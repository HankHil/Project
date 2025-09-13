import json

from utils import data_read, data_write


def add_contact(info):
    try:
        contacts = json.loads(data_read())
    except json.JSONDecodeError:
        contacts = {}
    finally:
        if '"' in info:
            info = info.split('" ')
        else:
            info = info.split(' ')
        contacts[info[0].strip('"')] = info[1].strip('"')

        data_write(contacts)
