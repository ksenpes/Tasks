def calculate_discount(price, pos):
    discount = 0
    if pos >= 20:
        discount = 0.2 * price
    elif pos >= 10:
        discount = 0.1 * price
    return int(price - discount)


price = int(input('Цена: '))
pos = int(input('Посещений: '))        
print('Итоговая цена: ', calculate_discount(price, pos))