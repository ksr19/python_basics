a = 0
b = 0
increment = 0.1
days = 1
while a <= 0:
    a = float(input("Введите сколько километров пробежал спортсмен в первый день тренировок: "))
while b <= 0:
    b = float(input("Введите цель спортсмена в километрах: "))
while a < b:
    a *= (increment + 1)
    days += 1
print(f"Дней для достижения цели спортсменом: {days}")
