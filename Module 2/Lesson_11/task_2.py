def count_specific_items_with_while(a, b):
    count = 0
    i = 0
    while i < len(a):
        if a[i] == b:
            count += 1
        i += 1
    return count


a = ['fruit', 'toy', 'fruit', 'toy']     #введите ваши данные
print(f"'{a}'")
b = 'toy'
print(f"'{b}'")
print(f"Количество '{b}': {count_specific_items_with_while(a, b)}")