from functools import reduce

print("Произведение четных чисел от 100 до 1000:",
      reduce((lambda a, b: a * b), [_ for _ in range(100, 1001) if _ % 2 == 0]))
