#Ребята собрались в поход. Для каждого ребёнка есть требование. Ребята решили разделить обязанности сбора 
# и каждый собирал что-то от себя для всех. Нужно проверить правильно ли ребята собрались в поход.

trebovanie = {
    "Вода": 3,
    "Консервы": 4,
    "Макароны": 0.5,
    "Палатка": 1,
    "Снеки": 0.3,
    "Спички": 1
}
deti = {'Дарья': {'Вода': 6.0, 'Консервы': 99.0, 'Макароны': 6.0, 'Палатка': 6.0, 'Снеки': 6.0, 'Спички': 6.0}, 
        'Александр': {'Вода': 6.0, 'Консервы': 1.0, 'Макароны': 0.0, 'Палатка': 0.0, 'Снеки': 0.0, 'Спички': 0.0}}
print(deti)
for i in trebovanie.keys():
    if trebovanie[i]*2 > deti['Дарья'][i] + deti['Александр'][i]:
        print('Никуда они так не пойдут! Остановить!')
        break
else:
    print("Дети к походу готовы")
    
