# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

str1 = input('Введите 1ю строку: ')
str2 = input('Введите 2ю строку: ')
str3 = input('Введите 3ю строку: ')
str4 = input('Введите 4ю строку: ')

with open('text.txt', 'w') as f:
    f.write(str1)
    f.write('\n')
    f.write(str2)

with open('text.txt', 'a') as f:
    f.write('\n')
    f.write(str3)
    f.write('\n')
    f.write(str4)




