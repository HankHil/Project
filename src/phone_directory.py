from add_contact import add_contact
from delete_contact import delete_contact
from find_contact import find_contact
from list_contact import list_contact
from merge_contact import merge_contact
from utils import parse_command

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
            delete_contact(command_param)
        elif command_name == "find":
            find_contact(command_param)
        elif command_name == "merge":
            merge_contact(command_param)
        else:
            print("Unknown command")
        print(
            f"Command name = {command_name}, command_param = {command_param}")
