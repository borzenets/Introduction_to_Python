# Задача 34

vowel_letters_rus = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
text = input('Введите стихотворенье Винни-Пуха: ')
print(text)
text_list = text.lower().split()


def count_letters(string: str, letters: list) -> int:
    return len([letter for letter in string if letter in letters])


for index, phrase in enumerate(text_list):
    if index == 0:
        count = count_letters(phrase, vowel_letters_rus)
    elif count == count_letters(phrase, vowel_letters_rus):
        continue
    else:
        print('Пам парам')
        break
else:
    print('Парам пам-пам')
