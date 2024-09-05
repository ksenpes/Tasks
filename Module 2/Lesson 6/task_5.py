t = list(map(int, input('Введите цены: ').split(', ')))
t_max = max(t)
i_max = t.index(t_max)
t_min = min(t)
i_min = t.index(t_min)
t[i_min] = t_max
t[i_max] = t_min
t = str(t)
print('Новые цены:', ''.join(t))