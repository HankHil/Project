import json

from utils import data_read, data_write


def merge_contact(book) -> None:
    try:
        file_content = json.loads(data_read())

        with open(book, 'r') as c:
            copy_content = c.read()
        if all([x not in y for x in copy_content for y in file_content]):
            file_content.update(json.loads(copy_content))
            data_write(file_content)
        else:
            print('Дубликаты не допускаются')

    except FileNotFoundError:
        print('Файл не найден')
    except json.decoder.JSONDecodeError:
        print('Файл не подходит')
