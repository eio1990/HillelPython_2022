# Дан словарь, создать новый словарь при помощи конструкции генератор словаря,
# поменяв местами ключ и значение.

dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

new_dict = {items[1]: items[0] for items in dict.items()}
print(new_dict)

