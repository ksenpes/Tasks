def func(c: int, p: int, pr: int):
    soot = c / p

    if soot < 0.01 and pr >= p:
        return "Недооцененная"
    elif 0.01 <= soot < 0.05:
        return "Низкая"
    elif 0.05 < soot <= 0.1 and pr > c:
        return "Средняя"
    elif soot > 0.1:
        return "Высокая"
    else:
        return "Неопределенная"

c, p, pr = 50, 10000, 150000 #введите ваши данные
print ('Клики, Показы, Просмотры: ', c,',', p,',', pr)
print(func(c, p, pr))