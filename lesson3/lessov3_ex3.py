#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3,):
    try:
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'
print(my_func(1, 2, 3))
