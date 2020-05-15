"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

# a
f = open('text.txt')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i: стрелов
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i, len(i), 'симв.', word, 'сл.')

print(line, 'стр.')
f.close()

# b
f = open('file_task_02.txt', 'r+')
f.truncate()
str_list = ['День\n', 'Ночь\n', 'Чиж и Ко - "Фантом"\n', 'Я бегу по вызженной земле, гермошлем захлопнув на ходу\n']
f.writelines(str_list)

f = open('file_task_02.txt')
line_count = 0
for line in f:
    line_count += 1

    flag = 0
    word = 0
    for j in line:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(line, word, 'сл.')

print("Количество строк в файле: ", line_count)
f.close()