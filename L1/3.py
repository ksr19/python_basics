n = input("Пожалуйста, введите неотрицательное число: ")
if int(n) < 0:
    print("Введенное число должно быть неотрицательным")
else:
    sum_n = int(n) + int(n + n) + int(n + n + n)
    print(f"Сумма чисел {n}, {n + n} и {n + n + n} равна {sum_n}")
