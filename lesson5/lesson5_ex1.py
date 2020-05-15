"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""
# a

fname = input('Файл: ')
f = open(fname,'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()

# b

f = open('file_task_01.txt', 'w')
print("Введите данные в файл: ")
while True:
    text = input()
    f.write(text + '\n')
    if text == "":
        break
f.close()