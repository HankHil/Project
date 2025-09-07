def parse_command(line: str) -> tuple:
    command_name = line.split(maxsplit=1)[0]
    command_param = line.split(maxsplit=1)[1:]
    if command_param.count(' ') > 2:
        print(f'''Неправильный формат ввода контакта
        Введите контакт используя \"''')
        parse_command(input())
    elif command_param == []:
        command_param = [None]
    # if '"' in command_param[0]:
    #     name, phone = command_param[0].split('" ')
    # else:
    #     name, phone = command_param[0].split()
    #name, phone = command_param[0], command_param[1]
    return command_name, command_param[0]

assert (parse_command('add ivan_ivanov 123-1345-2323-2') ==
        ('add', 'ivan_ivanov 123-1345-2323-2'))
assert (parse_command('add "Иванов Иван Иванович" "+9 1223 222 22 22"') ==
        ('add', '"Иванов Иван Иванович" "+9 1223 222 22 22"'))


