def func(tasks):
    max_tasks = max(tasks.values())
    sotr = [employee for employee, tasks in tasks.items() if tasks == max_tasks]
    if len(sotr) == len(tasks):
        return ", ".join(sotr)
    else:
        return sotr[0]

tasks = {"Анна": 5, "Боб": 7, "Сьюзан": 9}
print("Самый ответственный:", func(tasks))