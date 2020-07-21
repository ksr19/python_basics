input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
modified_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
print("Исходный список:", input_list)
print("Новый список:", modified_list)
