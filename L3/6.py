def int_func(user_input):
    input_list = list(user_input)
    for i in range(0, len(input_list)):
        if ord(input_list[i]) == 32 or 97 <= ord(input_list[i]) <= 122:
            if i == 0 or ord(input_list[i - 1]) == 32:
                input_list[i] = input_list[i].title()
        else:
            return "Допустимо использование только маленьких латинских букв!"
    return "".join(input_list)


user_input = input("Введите строку слов, состоящих из маленьких латинских букв: ")
print(int_func(user_input))
