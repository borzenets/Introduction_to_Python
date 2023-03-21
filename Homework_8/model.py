def file_db(patch_file, flag, date=None):
    with open(patch_file, flag, encoding='UTF-8') as file:
        match flag:
            case 'r':
                return file.readlines()
            case 'w':
                file.write(date)
                return 'Изменения сохранены'
            case 'a':
                file.write(date)
                return 'Данные добавлены'
            case _:
                return 'Неправильный flag режима работы с файлом'


def pars_lines_csv_to_dict_in_list(data: str):
    pb = []
    for index, contact in enumerate(data):
        contact = {
            'name': contact.split(';')[0].strip(),
            'phone': contact.split(';')[1].strip(),
            'comment': contact.split(';')[2].strip()
        }
        pb.append(contact)
    return pb


def pars_dict_in_list_to_lines_csv(data: list[dict]) -> str:
    lines_csv = []
    for contact in data:
        lines_csv.append(';'.join(contact.values()))

    lines_csv = '\n'.join(lines_csv)
    return lines_csv


def add_remove_change_contact(p_book: list[dict], data=None, index=None) -> list[dict] or str:
    if str(index) and data:
        data['name'] = p_book[index]['name'] if not bool(data['name']) else data['name']
        data['phone'] = p_book[index]['phone'] if not bool(data['phone']) else data['phone']
        data['comment'] = p_book[index]['comment'] if not bool(data['comment']) else data['comment']
        p_book.pop(index)
        p_book.insert(index, data)
        return p_book
    elif not index and data:
        p_book.append(data)
        return p_book
    else:
        return 'Контакт ' + p_book.pop(index)['name'] + ' удален'


def search(search_str: str, p_book: list[dict]) -> list[dict]:
    result_list = []
    for contact in p_book:
        if search_str.lower() in ';'.join(contact.values()).lower():
            result_list.append(contact)
    return result_list
