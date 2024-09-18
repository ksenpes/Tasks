def calculate_discount(price, i = 0, discount = 0) -> int:
    if i == len(price):
        return price
    new_price = price[i] - discount
    discount = 0.1 * price[i]
    price[i] = int(new_price)
    return calculate_discount(price, i+1, discount)

price = [1000, 2000, 3000]     #введите ваши данные
print(price)
print(calculate_discount(price))