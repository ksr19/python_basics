user_list = list(input("Введите произвольный текст: "))
print("Исходный список: ", user_list)
for index in range(len(user_list) // 2):
    user_list[2 * index], user_list[2 * index + 1] = user_list[2 * index + 1], user_list[2 * index]
print("Отредактированный список: ", user_list)
