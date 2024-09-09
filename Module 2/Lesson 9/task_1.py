def calculate_discount(price: list, sale):
    return(sum(price) * (sale / 100))

price = list(map(int, input('Введите цены и скидку: ').split(', ')))
print('Сумма скидки: ', calculate_discount(price[:-1], price[-1]))