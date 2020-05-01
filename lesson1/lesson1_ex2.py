#2. Пользователь вводит время в секундах.
#Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. #
# Используйте форматирование строк.

num_seconds = int(input('Введите любое количество секунд'))
print('Ваше число равно =', num_seconds)
hours = num_seconds // 3600
minutes = (num_seconds % 3600) // 60
seconds = (num_seconds % 3600) % 60
time_format1 = (f"{hours}:{minutes}:{seconds}")
time_format2 = (f"hours: {hours}, minutes: {minutes}, seconds: {seconds}.")

print(time_format1)
print('or')
print(time_format2)