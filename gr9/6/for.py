# Задаётся трёхзначное число. Определите какое минимальное число, будет в двоичной системе иметь ровно 5 единиц. 
schet = 0
for i in range(100,1000):
    schet += 1
    a = bin(i)[2:]
    if a.count('1') == 3:
        print(f'Число которое в двоичном содержет 3 единиц будет {i}')
        print(f'В двоином виде оно такое: {a}')
        break
print(f'Цикл завершён и всё хорошо. Пройдено {schet} этапов')