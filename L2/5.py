my_list = [7, 5, 3, 3, 2]
user_number = 0
while user_number < 1:
    user_number = int(input("Введите натуральное число: "))
index = 0
while index < len(my_list) and user_number <= my_list[index]:
    index += 1
if index < len(my_list):
    my_list.insert(index, float(user_number))
else:
    my_list.append(float(user_number))
print("Результат рейтинга: ", my_list)
