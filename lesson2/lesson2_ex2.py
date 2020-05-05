"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

#my_list = list(input("Введите значения для списка"))
my_list = [2, 6.4, False, 'Hello']
for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]
print(my_list)

my_list = [2, 6.4, False, 'Hello']
j = 0
for el in range(int(len(my_list)/2)):
  my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
  j += 2
print(my_list)

my_list = [2, 6.4, False, 'Hello']
for j, el in enumerate(my_list):
    if j % 2 != 0:
        my_list[j], my_list[j - 1] = my_list[j - 1], el
print(my_list)
