t = input('Введите товары: ').split(', ')
print('Позиции для перестановки: ')
a = int(input())
b = int(input())
t[a-1], t[b-1] = t[b-1], t[a-1]
print('На полке: ', (', ').join(t))