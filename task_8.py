"""
Задача 8:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def power(a, b):
    if b == 1:
        return a
    return a * power(a, b - 1)


def start_app():
    a = get_int_from_user('Введите основание степени: ')
    b = get_int_from_user('Введите показатель степени: ')
    if a is not None and b is not None:
        print(f'Результат a в степени b {power(a, b)}')
    else:
        print('Что-то пошло не так, попробуйте еще раз')


if __name__ == "__main__":
    start_app()
