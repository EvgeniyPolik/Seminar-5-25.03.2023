"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def get_count_digits(num, even_count = 0, noteven_count = 0):
    if num % 2 == 0:
        even_count += 1
    else:
        noteven_count += 1
    num //= 10
    if num == 0:
        return even_count, noteven_count
    else:
        return get_count_digits(num, even_count, noteven_count)


def start_app():
    n = get_int_from_user('Введите ваше число: ')
    if n is not None:  # 0 Даёт False, но это четное число
        result = get_count_digits(n)
        print(f'В числе {n}, число четных цифр: {result[0]}, а не четных: {result[1]}')
    else:
        print('Неверный ввод')

if __name__ == "__main__":
    start_app()
