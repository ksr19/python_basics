time = int(input("Пожалуйста, введите время в секундах: "))
if time < 0:
    print("Вводимая величина должна быть неотрицательной")
else:
    hours = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 3600 % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
