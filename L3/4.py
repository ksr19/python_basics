def my_func(x, y):
    """Возведение числа x в отрицательную степень y.

    :param x:  действительное положительное число
    :param y:  целое отрицательное число
    :return:
    """
    if x <= 0:
        print("Основание степени должно быть положительным!")
    else:
        if y >= 0:
            print("Степень должна быть отрицательной!")
        else:
            power_result = 1
            for i in range(y, 0):
                power_result = power_result / x
            print(f"Число {x} в степени {y}: {round(power_result, 4)}.")


try:
    x = float(input("Введите действительное положительное число: "))
    y = int(input("Введите целое отрицательное число: "))
    my_func(x, y)
except ValueError:
    print("Необходимо вводить числа!")
