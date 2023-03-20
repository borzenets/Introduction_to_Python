import view
import model


patch = 'DB.csv'
phone_book = []


def start():
    while True:
        menu_choice = view.show_menu()
        date = model.file_db(patch, 'r')
        phone_book = model.pars_lines_csv_to_dict_in_list(date)
        match menu_choice:
            case 1:
                view.show_contacts(phone_book, 'Телефонная книга пуста')
            case 2:
                pass
            case 3:
                new_contact = view.add_contact()
                phone_book = model.add_remove_change_contact(phone_book, data=new_contact)
                line_p_book = model.pars_dict_in_list_to_lines_csv(phone_book)
                model.file_db(patch, 'w', line_p_book)
                view.show_message(f'Контакт {new_contact["name"]} добавлен')
            case 4:
                pass
            case 5:
                view.show_contacts(phone_book, 'Ошибка')
                index = view.remove_contact()
                message = model.add_remove_change_contact(phone_book, index=index)
                line_p_book = model.pars_dict_in_list_to_lines_csv(phone_book)
                model.file_db(patch, 'w', line_p_book)
                view.show_message(message)


