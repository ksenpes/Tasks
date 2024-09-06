t = list(map(int, input('Введите список: ').split(', ')))
k, n, m = t[1], t[0], t[-1]
print('Числа подсписка: ', ', '.join(map(str, t[n:m:k])))