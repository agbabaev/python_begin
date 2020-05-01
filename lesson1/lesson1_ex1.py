# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

num = int(input('Введите число!'))
print(num)

while True:
    fractional_number = input('Введите дробное число через точку!\nОтвет пользователя -> ')
    # это вариант решения за рамками темы урока.
    # try:
    #     fractional_number = float(fractional_number)
    #     print(f'Вы ввели {fractional_number}, который является {type(fractional_number)}!')
    #     break
    # except:
    #     print('Это не число!')
    #     continue
    if '.' in fractional_number:
        error = False
        for i in fractional_number:
            if i == '.':
                None
            elif i.isdigit():
                None
            else:
                error = True
                break
        if error:
            print('Вы ввели не float, попробуйте еще!')
            continue
        print("Вы ввели дробное число равное", float(fractional_number))
        break
    else:
        print('Вы ввели не float, попробуйте еще!')

text = input('Введите свое имя!')  # str по умолчанию!
print('Добро пожаловать,', text, '!')


