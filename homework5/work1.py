# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число, а значение - сколько раз оно встречается).
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.


from random import randint
lst = []

for i in range(50):
    lst.append(randint(1, 10))
print('Список чисел: ', lst)


def analysis(sequence: list) -> dict:
    dct = {}
    for i in sequence:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    return dct




result = analysis(lst)

for item in result:
    print("'%d':%d" %(item, result[item]))