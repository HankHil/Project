from utils import parse_command
import json

#обработать ошибку отсутствия ключа

def add_contact(info):
    with open('data.json', 'r') as f:
        file_content = f.read()
        if file_content == '':
            contacts = {}
        else:
            contacts = json.loads(file_content)
        if '"' in info:
            info = info.split('" ')
        else:
            info = info.split(' ')
        contacts[info[0].strip('"')] = info[1].strip('"')
        with open('data.json', 'w') as f:
            f.write(json.dumps(contacts))

def delite_contact(info):
    with open('data.json', 'r') as f:
        file_content = f.read()
        if file_content == '':
            return print('Справочник пуст, нечего удалять.')
        else:
            contacts = json.loads(file_content)
        contacts.pop(info.strip('"'))
        with open('data.json', 'w') as f:
            f.write(json.dumps(contacts))


def list_contact(info):
    with open('data.json', 'r') as f:
        file_content = f.read()
        if file_content == '':
            return print('Справочник пуст, нечего показать.')
        elif info != None:
            print(json.loads(file_content)[info.strip('"')])
        else:
            print(json.loads(file_content))


def find_contact(info):
    with open('data.json', 'r') as f:
        file_content = f.read()
        if file_content == '':
            return print('Справочник пуст, нечего искать.')
        elif info != None:
            data = json.loads(file_content)
            print({x:y for x, y in data.items() if info.strip('"') in y})
        else:
            print('Вы забыли указать телефон или его часть')


def merge_contact(info):
    with open('data.json', 'r') as o:
        original_content = json.loads(o.read())
        with open(info, 'r') as c:
            copy_content = c.read()
            if copy_content == '':
                return print('Нечего копировать')
            else:
                original_content.update(json.loads(copy_content))
                with open('data.json', 'w') as f:
                    f.write(json.dumps(original_content))

if __name__ == "__main__":

    cmd_name: str = ''
    while cmd_name != "exit":
        cmd_name = input("Enter command: ")
        if cmd_name == "exit":
            print('Работа завершена')
            break

        command_name, command_param = parse_command(cmd_name)
        if command_name == "list":
            list_contact(command_param)
        elif command_name == "add":
            add_contact(command_param)
        elif command_name == "delete":
            delite_contact(command_param)
        elif command_name == "find":
            find_contact(command_param)
        elif command_name == "merge":
            merge_contact(command_param)
        else:
            print("Unknown command")
        print(
            f"Command name = {command_name}, command_param = {command_param}")




