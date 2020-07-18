userNameString = input("Пожалуйста, введите свое имя: ")
userSurnameString = input("Пожалуйста, введите свою фамилию: ")
userIntNumber = int(input("Пожалуйста, введите целое число: "))
userFloatNumber = float(input("Пожалуйста, введите вещественное число: "))
if userFloatNumber > userIntNumber:
    print(f"Уважаемый {userNameString} {userSurnameString}, число {userFloatNumber} больше числа {userIntNumber}.")
elif userFloatNumber == userIntNumber:
    print(f"Уважаемый {userNameString} {userSurnameString}, числа равны.")
else:
    print(f"Уважаемый {userNameString} {userSurnameString}, число {userIntNumber} больше числа {userFloatNumber}.")
