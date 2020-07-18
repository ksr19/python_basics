try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    print(f"Отношение двух чисел: {round((lambda a, b: a / b)(a, b), 2)}")
except ValueError:
    print("Необходимо ввести число!")
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
