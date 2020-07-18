num = int(input("Пожалуйста, введите целое положительное число: "))
maxDigit = 0
while num > 0:
    if num % 10 > maxDigit:
        maxDigit = num % 10
        if maxDigit == 9:
            break
    num = num // 10
print(f"Максимальная цифра введенного числа: {maxDigit}")
