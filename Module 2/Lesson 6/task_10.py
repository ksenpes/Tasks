import statistics as st
t = list(map(int, input('Введите цены: ').split(', ')))
print('Средняя цена товара: ', st.mean(t))