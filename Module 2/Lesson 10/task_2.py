def color(hour):
    if hour >= 6 and hour < 18:
        return "Светлый"
    else:
        return "Темный"

hour = int(input('Текущее время: '))
print("Цвет фона:", color(hour))