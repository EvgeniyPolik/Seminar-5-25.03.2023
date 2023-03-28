"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def get_sum_elements(num, sum_elements=0):
    if num == 0:
        return sum_elements
    return num + get_sum_elements(num - 1)


def start_app():
    yes_no = {False: 'не равно', True: 'равно'}
    n = get_int_from_user('Введите число элементов: ')
    if n is not None:  # 0 Даёт False, но это число
        result_recurcive = get_sum_elements(n)
        result_analitcs = (n * (n + 1)) / 2
        print(f'Сумма {n} элементов полученная рекурсивно: {result_recurcive}, что '
              f'{yes_no[result_analitcs == result_recurcive]} вычисленному {result_analitcs}')
    else:
        print('Неверный ввод')


if __name__ == "__main__":
    start_app()
