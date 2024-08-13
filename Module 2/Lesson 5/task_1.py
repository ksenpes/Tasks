company = str(input("Введите название компании: "))
n = len(company) // 2
print(company[n:] + company[:n])