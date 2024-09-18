def func(money):
    if money < 1000:
        return "Google"
    elif 1000 <= money <= 5000:
        return "Facebook"
    else:
        return "Instagram"

money = int(input('Бюджет: '))
print(func(money))