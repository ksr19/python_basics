try:
    with open("text_3.txt", "r", encoding='utf-8') as f:
        employee_list = []
        earnings_list = []
        for line in f:
            earnings_list.append(float(line.split()[1]))
            if float(line.split()[1]) < 20000:
                employee_list.append(line.split()[0])

    print("Список сотрудников с зарплатой менее 20000:", employee_list)
    print(f"Средний доход сотрудников: {sum(earnings_list) / len(earnings_list):.2f}")
except IOError:
    print("Отсутствует файл 'text_3.txt'")
