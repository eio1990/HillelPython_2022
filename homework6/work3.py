# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()

from datetime import datetime
import time
def decorator(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f'Время выполнения функции {func}: {end - start} секунд')
    return wrapper

@decorator
def func1():
    print('Производится запуск функции func1')
    sum = 17 + 24
    print(f'Произведено вычесление суммы, 17 + 24 = {sum}')

@decorator
def func2():
    print('Производится запуск функции func2')
    sum = 17 * 24
    print(f'Произведено вычесление произведения, 17 * 24 = {sum}')


func1()
func2()