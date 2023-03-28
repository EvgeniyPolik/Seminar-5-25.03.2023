"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def get_int_from_user(message):
    try:
        n = int(input(message))
    except ValueError:
        return
    else:
        return n


def magic_coub(n, count_trys=1):
    yes_no = {False: 'больше', True: 'меньше'}
    if count_trys > 10:
        print(f'Число не угадано! Загаданное число {n}')
        return
    user_choose = get_int_from_user(f'Попытка № {count_trys}, введите Ваше число: ')
    if user_choose is not None:
        if user_choose == n:
            print(f'Ура, вы угадали загаданное число {n}')
        else:
            print(f'Не верно! Ваше число {yes_no[n > user_choose]} загаданного!')
            magic_coub(n, count_trys + 1)
    else:
        print('Неверный ввод')
        magic_coub(n, count_trys)


def start_app():
    n = random.randint(0, 100)
    magic_coub(n)


if __name__ == "__main__":
    start_app()
