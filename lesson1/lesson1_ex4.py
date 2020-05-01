# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input('Введите число из нескольких цифр!'))
current_max = 0
num = user_num
while num > 0:
    digit = num % 10
    if digit > current_max:
        current_max = digit
        if current_max == 9:
            break
    num = num // 10
print(current_max)

