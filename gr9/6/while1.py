#Вводятся числа пока не будет введено отрицальное. Выведите числа(каждый тип отдельно) которые делятся только на 2,только на 3, 
# и только на 2 и 3
a = 0
na2 = []
na3 = []
na6 = []
while a >= 0: # будет работать пока истино заданное условие
    a = int(input('Введите число:'))
    if a>10:
        continue
    if a % 6 == 0:
        na6.append(a)
    elif a % 2 == 0:
        na2.append(a)
    elif a % 3 == 0:
        na3.append(a)
print(f'Числа которые делятся на 2: {na2}')
print(f'Числа которые делятся на 3: {na3}')
print(f'Числа которые делятся на 6: {na6}')