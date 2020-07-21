input_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_list = [el for el in input_list if input_list.count(el) == 1]
print("Исходный список:", input_list)
print("Список с уникальными элементами:", unique_list)
