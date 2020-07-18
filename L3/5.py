def add_values(input_list):
    input_sum = 0
    for element in input_list:
        if element.upper() == 'Q':
            break
        else:
            try:
                input_sum += float(element)
            except ValueError:
                pass
    return input_sum


total_sum = 0
while True:
    user_input = input("Введите числа, разделенные пробелом. Для завершения взаимодействия напишите 'q': ").split()
    total_sum += add_values(user_input)
    if 'q' in user_input or 'Q' in user_input:
        break
    else:
        print(f"Сумма введенных чисел на текущий момент: {total_sum}.")
print(f"Сумма введенных чисел на момент завершения: {total_sum}.")
