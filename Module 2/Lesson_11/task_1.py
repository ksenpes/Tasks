
def sum_sales_with_for(prices):
    summ = 0

    for price in prices:
        summ += price
    print(*prices, sep='+', end=f'={summ}\n')


prices = [100, 200, 300]    #введите ваши данные
sum_sales_with_for(prices)