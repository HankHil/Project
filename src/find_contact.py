import json

from utils import data_read


def find_contact(numbers):
    try:
        data = json.loads(data_read())
        print({x: y for x, y in data.items() if numbers.strip('"') in y})
    except json.decoder.JSONDecodeError:
        print('Справочник пуст, нечего искать.')
    except AttributeError:
        print('Вы забыли указать телефон или его часть')
