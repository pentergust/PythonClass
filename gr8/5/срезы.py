a = [1,2,3,4,5,6,7,8,9,10]
b = 'Привет я некоторая строка для экспериментов'

print(a[:4]) # [:n] выводит от начала до 4ого
print(a[4:]) # [n:] от n до конца
print(a[4:7]) # [n:m] от n до m элементы
print(a[1:7:2]) # [n:m:s] от n до m с шагом s

print(b[:4]) # [:n] выводит от начала до 4ого
print(b[4:]) # [n:] от n до конца
print(b[4:7]) # [n:m] от n до m элементы
print(b[1:14:2]) # [n:m:s] от n до m с шагом s

stroka = b[3:17]
print(stroka)

