def track_low_stock_with_for(products, porog):
    for product, kol in products.items():
        if kol < porog:
            print(f'{product} - {kol}')


print('Низкий запас:')
track_low_stock_with_for({'apples': 50, 'bananas': 10, 'cherries': 3}, 15)  #введите ваши данные