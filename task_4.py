"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def get_sum_elements(num, current_value = 1, sum_elements = 0):
    sum_elements += current_value
    current_value /= -2
    num -= 1
    if num == 0:
        return sum_elements
    return get_sum_elements(num, current_value, sum_elements)


def start_app():
    n = get_int_from_user('Введите число элементов: ')
    if n is not None:  # 0 Даёт False, но это число
        result = get_sum_elements(n)
        print(f'Сумма {n} элементов это {result}')
    else:
        print('Неверный ввод')

if __name__ == "__main__":
    start_app()
