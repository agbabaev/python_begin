#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

text = input('Введите текст')
#text = 'national geographic'
#text = 'environmental protection'
#print(len(text))
words = text.split()
for el, word in enumerate(words):
    print('пункт', el+1, ' >>> слово -', word[:10])
