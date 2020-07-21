def fact(n):
    factorial = 1
    for j in range(1, n + 1):
        factorial = factorial * j
        yield factorial


try:
    n = int(input("Введите целое положительное число: "))
    if n < 1:
        print("Необходимо ввести целое положительное число!")
    else:
        for i, el in enumerate(fact(n), 1):
            print(f"Факториал числа {i} - {el}")
except ValueError:
    print("Необходимо ввести целое положительное число!")
