# "Ветеренарная клиника" - программа должна уметь: 1) добавить питомца и информацию о нём(имя питомца, ФИ хозяина, возраст питомца)
# 2) Выводить на экран список питомцев
# 3) Выписывать питомца(удалять из списка)
# 4) Завершать программу
spisok = [['Котик', 'НеКотик', '2'], ['Собачка', 'НеСобачка', '3'], ['Черепаха', 'НеЧерепаха', '4'], ['Хлеб', 'Игорь', '12']] # Основной список с информацией
while True:
    komanda = int(input('1) Добавить 2) Вывести 3) Выписать 4) Завершить(введите номер команды): '))
    if komanda == 4:
        break
    elif komanda == 1:
        b = []
        b.append(input('Введите имя питомца: '))
        b.append(input('Введите имя хозяина: '))
        b.append(input('Введите возраст питомца: '))
        spisok.append(b)
    elif komanda == 2:
        print(spisok)
    elif komanda == 3:
        schet = -1
        zapros = input('Кого выписать: ')
        for i in spisok:
            schet += 1
            if zapros in i:
                spisok.pop(schet)
                break
print('Программа завершена')