import json


def data_read():
    with open('data.json', 'r', encoding='utf-8') as f:
        return f.read()


def data_write(contacts):
    with open('data.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(contacts))


def parse_command(line: str) -> tuple:
    command_name = line.split(maxsplit=1)[0]
    command_param = line.split(maxsplit=1)[1:]
    if command_param.count(' ') > 2:
        print(f'''Неправильный формат ввода контакта
        Введите контакт используя \"''')
        parse_command(input())
    elif command_param == []:
        command_param = [None]
    return command_name, command_param[0]
