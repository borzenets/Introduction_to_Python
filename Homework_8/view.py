def show_menu() -> int:
    while True:
        user_input = input('МЕНЮ:'
                           '\n1 - Показать все контакты'
                           '\n2 - Поиск контактов'
                           '\n3 - Добавить новый контакт'
                           '\n4 - Изменить контакт'
                           '\n5 - Удалить контакт'
                           '\nВведите номер пункта меню: ')

        if user_input.isdigit() and 0 < int(user_input) <= 5:
            return int(user_input)
        else:
            print('Введите число от 1 до 5')


def show_contacts(contacts: list, message: str) -> None:
    if not contacts:
        print(message)
    else:
        for i, contact in enumerate(contacts, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f' {contact.get("phone"):<20} '
                  f' {contact.get("comment"):<20} ')


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите коментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def show_message(message: str) -> None:
    print('-' * (len(message) + 2))
    print(' ' + message)
    print('-' * (len(message) + 2))


def remove_contact() -> int:
    while True:
        user_input = input('Введите номер контакта для удаления: ')
        if user_input.isdigit() and 0 < int(user_input):
            return int(user_input) - 1


def get_search_string() -> str:
    return input('Введите строку для поиска: ')


def edit_contact():
    index = int(input('Введите номер контакта для изменения: '))
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите коментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}, index - 1
