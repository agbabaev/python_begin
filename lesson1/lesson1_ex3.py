#3. Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

num = input('Введите число от 1 до 9!')
print('Ваше число =', num)

user_sum = (int(num) + int(num + num) + int(num + num + num))

print(user_sum)

print('or')

print(f"{num} + {num + num} + {num + num + num} = {user_sum}")