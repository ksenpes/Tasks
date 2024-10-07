def convert_units_with_while(a, met):
    i = 0
    while i < len(a):
        if met == 'meters':
            converted_value = a[i] * 3.28084
            print(f"{a[i]} meter(s) = {converted_value} foot(feet)")
            i += 1

a = [1, 2]   #введите ваши данные
met = 'meters'  #введите ваши данные
convert_units_with_while(a, met)