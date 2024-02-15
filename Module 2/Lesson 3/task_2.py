n = int(input('Введите количество сотрудников '))
n2 = int(round(n/2))
n3 = int(n - n2)
a = [str(input('Введите имя: ')) for i in range(n2)]
b = [str(input('Введите имя: ')) for i in range(n3)]
print("В чётные дни работают: ", ", ".join(a))
print(n2, n3)
print("В нечётные дни работают: ", ", ".join(b))