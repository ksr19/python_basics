user_input = input("Введите строку из слов, разделенных пробелами: ")
print("Преобразованный вывод: ")
for ind, word in enumerate(user_input.split(), 1):
    print(ind, word[:10])
