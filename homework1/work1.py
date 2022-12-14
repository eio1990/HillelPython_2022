# 1. Создать 3 переменные с одинаковыми данными (и одинаковым типом) и с одинаковыми идентификаторами
# (не присваивая значения переменных друг другу)
# 2. Создать 2 переменные с одинаковыми данными (и одинаковым типом) и с разными идентификаторами
# 3. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались
# одинаковые данные (и одинаковым типом), а у 2-х последних стали одинаковые идентификаторы
# и остались одинаковые данные.

# * добиться нужного результата необходимо только приведением типов данных к нужному


x1 = 17
x2 = 17
x3 = 17
print("Проверка условия: ")
print('x1=x2: ', x1 == x2)
print('x2=x3: ', x2 == x3)
print('x1 в ячейке памяти x2: ', x1 is x2)
print('x2 в ячейке памяти x3: ', x2 is x3)
print('-'*100)
print("Меняем типы так, чтобы у x1,x2,x3 стали разные идентификаторы, но при этом остались "
      "одинаковые данные (и одинаковым типом)...")
x1 = float(x1)
x2 = float(x2)
x3 = float(x3)
print('x1=x2: ', x1 == x2)
print('x2=x3: ', x2 == x3)
print('x1 в ячейке памяти x2: ', x1 is x2) # проверка в одной ли ячейке памяти данные
print('x2 в ячейке памяти x3: ', x2 is x3)
print('Одинаковый ли тип: ', type(x1) == type(x2) == type(x3))
print('-'*100)
y1 = [23]
y2 = [23]
print("Проверка условия: ")
print('y1=y2: ', y1 == y2)
print('y1 в ячейке памяти y2: ', y1 is y2)
print(type(y1), type(y2))
print('-'*100)
print("Меняем типы так, чтобы у y1,y2 стали одинаковые идентификаторы, но при этом остались "
      "одинаковые данные (и одинаковым типом)...")
print('-'*100)
y1 = bool(y1)
y2 = bool(y2)
print('y1=y2: ', y1 == y2)
print('y1 в ячейке памяти y2: ', y1 is y2)
print('Одинаковый ли тип: ', type(y1) == type(y2))


