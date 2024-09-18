
def func_max_price(price):
    if len(price) == 1:
        return price[0]
    else:
        max_price = func_max_price(price[1:])
        if price[0] > max_price:
            return price[0]
        else:
            return max_price

price = [15, 7, 10] #введите ваши данные
print('Список цен: ', price)
print('Максимальный ценник: ', func_max_price(price))