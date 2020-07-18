revenue = -1
cost = -1
while revenue < 0:
    revenue = float(input("Пожалуйста, введите выручку фирмы. Величина должна быть неотрицательной: "))
while cost < 0:
    cost = float(input("Пожалуйста, введите издержки фирмы. Величина должна быть неотрицательной: "))
if cost > revenue:
    print(f"Фирма убыточна. Величина убытка {cost - revenue}.")
elif revenue > cost:
    print(f"Фирма прибыльна. Величина прибыли {revenue - cost}.")
    print("Рентабельность фирмы составляет %.2f." % ((revenue - cost) / revenue))
    employee = 0
    while employee <= 0:
        employee = int(input("Пожалуйста, введите количество работников. Величина должна быть положительной: "))
    print("Прибыль фирмы в расчете на сотрудника составляет %.2f." % ((revenue - cost) / employee))
else:
    print("Издержки фирмы равны выручке.")
