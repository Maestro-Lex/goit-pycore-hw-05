'''
Модуль, який містить всі наші методи для бота
'''
from colorama import Fore


def parse_input(user_input: str) -> list:
    '''
    Парсер команд
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() # Робимо введення команд нечутливим до регистру
    return cmd, *args

def help():
    '''
    Функція-помічник з інформацію про наявні команди
    '''
    return \
f"{Fore.LIGHTYELLOW_EX}    > {'help':10}{Fore.RESET}- show commands description\n\
{Fore.LIGHTYELLOW_EX}    > {'add':10}{Fore.RESET}- add contact (name, phone number)\n\
{Fore.LIGHTYELLOW_EX}    > {'change':10}{Fore.RESET}- change phone namber of the contact (name, phone number)\n\
{Fore.LIGHTYELLOW_EX}    > {'phone':10}{Fore.RESET}- show the phone namber of the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'del':10}{Fore.RESET}- remove the contact (name)\n\
{Fore.LIGHTYELLOW_EX}    > {'all':10}{Fore.RESET}- show the contact list\n\
{Fore.LIGHTYELLOW_EX}    > {'close':10}{Fore.RESET}- close the Bot\n\
{Fore.LIGHTYELLOW_EX}    > {'exit':10}{Fore.RESET}- close the Bot"

def input_error(func):
    '''
    Функція-декоратор для обробки помилок команд.
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)        
        except ValueError:
            return f"{Fore.LIGHTRED_EX}Give me name and phone please.{Fore.RESET}"            
        except KeyError:
            return f"{Fore.LIGHTRED_EX}There is no such user!{Fore.RESET}"     
        except IndexError:
            return f"{Fore.LIGHTRED_EX}Enter user name.{Fore.RESET}"
    return inner

@input_error
def add_contact(args: list, contacts: dict) -> str:
    '''
    Команда додання імені та номеру до списку контактів 
    '''
    name, phone = args
    contacts[name.capitalize().strip(",")] = phone
    return f"{Fore.LIGHTGREEN_EX}Contact added.{Fore.RESET}"

@input_error
def change_contact(args: list, contacts: dict) -> str:
    '''
    Команда зміни номеру телефону за ім'ям контакту, у разі його наявності 
    '''
    name, phone = args
    if name.capitalize().strip(",") in contacts.keys():
        contacts[name.capitalize().strip(",")] = phone
        return f"{Fore.LIGHTGREEN_EX}Contact updated.{Fore.RESET}"
    else:
        raise KeyError

@input_error
def show_phone(args: list, contacts: dict) -> str:
    '''
    Команда, що виводить номер телефону за ім'ям контакту, у разі його наявності
    '''
    return contacts[args[0].capitalize()]

@input_error
def remove_contact(args: list, contacts: dict) -> str:
    '''
    Команда, що видаляє контакт за ім'ям користувача, у разі його наявності
    '''
    contacts.pop(args[0].capitalize())
    return f"{Fore.LIGHTGREEN_EX}Contact deleted.{Fore.RESET}"

def show_all(contacts: dict) -> str:
    '''
    Команда виводу всього списку контактів із сортуванням за ім'ям користувача у вигляді таблиці
    '''
    contacts_list_str = f"|{'name':^15}|{'phone number':^17}|\n-----------------------------------\n"   
    for key, value in sorted(contacts.items()):
        contacts_list_str += f"|{key:<15}|{value:>17}|\n"
    if not contacts:
        return f"{Fore.LIGHTRED_EX}Contact list is empty!{Fore.RESET}"
    return contacts_list_str