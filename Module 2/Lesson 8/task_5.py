mag_1 = set(input('Первый магазин: ').split(', '))
mag_2 = set(input('Второй магазин: ').split(', '))

ex_mag_1 = mag_1.difference(mag_2)
ex_mag_2 = mag_2.difference(mag_1)

print('Только в первом магазине:', ', '.join(ex_mag_1))
print('Только в втором магазине:', ', '.join(ex_mag_2))