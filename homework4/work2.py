# Сделать программу в виде функций в которой нужно будет угадывать число.


import random
guess = random.randint(1, 50)
name = input('Привет игрок, представься пожалуйста. \n' )
print(f'Очень приятно, {name}, что ты к нам заглянул!')
print('-' * 50)
print(f'{name}, тебе предстоит проверить свою удачу и отгадать число от 1 до 50')
print('-' * 50)

def guess_func():
    x = 0
    tries = 7
    print(f'Да начнется УГАДАЙКА! У тебя {tries} попыток!')
    while tries > 0:
        x = int(input('Введи преполагаемое число: '))
        if guess > x:
            tries = tries - 1
            print(f'Загаданное число больше {x}. Осталось {tries} попыток.')
            print('-' * 50)
        elif guess < x:
            tries = tries - 1
            print(f'Загаданное число меньше {x}. Осталось {tries} попыток.')
            print('-' * 50)
        elif guess == x:
            print(f'Поздравляю, {name}! Тебе сопутсвует удача! Загаданное число - {x}, заходи еще.')
            break

guess_func()

