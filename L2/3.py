month_number = 0
while month_number < 1 or month_number > 12:
    month_number = int(input("Введите номер месяца: "))
seasons_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
for _ in seasons_dict.keys():
    if month_number in seasons_dict.get(_):
        print(f"Месяц с номером {month_number} - это {_}.")
        break
