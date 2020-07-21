from sys import argv

try:
    script_name, work_hours, hourly_rate, bonus = argv
    salary = float(work_hours) * float(hourly_rate) + float(bonus)
    print("Выработка в часах:", work_hours)
    print("Ставка в час:", hourly_rate)
    print("Премия:", bonus)
    print("Итоговая заработная плата сотрудника:", salary)
except ValueError:
    print("Необходимо вводить числовые значения")
