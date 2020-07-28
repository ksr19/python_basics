from random import random

with open("text_5.txt", "w+", encoding='utf-8') as f:
    for i in range(int(random() * (50 - 1) + 1)):
        print(round(random() * 100, 4), end=' ', file=f)
    f.seek(0)
    print(f"Сумма чисел в файле {sum(map(float, f.read().split())):.4f}")
