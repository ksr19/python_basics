with open("text_1.txt", "w") as f:
    while True:
        input_string = input("Введите информацию для добавления в файл (пустая строка для прекращения ввода): ")
        if input_string:
            f.write(input_string + "\n")
        else:
            break
