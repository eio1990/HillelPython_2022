# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

digit = int(input('N = '))
k = 0
l = 1

for l in range(1, digit+1):
   if l%3 == 0:
        l += 1
        continue
    else:
        k = l ** 3 + k
        l += 1

while l < digit+1:
    if l % 3 == 0:
        l += 1
        continue
    else:
        k = l ** 3 + k
        l += 1

print(k)
