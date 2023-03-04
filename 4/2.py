# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.

# user_string = input('Введите несколько слов разделенных пробелом: ')

user_string = 'а где тут руль спросил гагарин ' \
              'деревня буркнул королёв ' \
              'ещё спроси а где тут вожжи ' \
              'ещё поехали скажи '

#  Мое решение
count_words = dict()

user_string_list = user_string.lower().split()
user_string_list = [item.strip(',.;:_?!*()-@!#$%^&+= ') for item in user_string_list]

for word in user_string_list:
    count_words[word] = count_words.get(word, 0) + 1

print(f'В тексте всего {sum(count_words.values())} слов, {len(count_words)} неповторяющихся слов.')

#  Решение преподавателя

print(len(set(user_string.split())))
