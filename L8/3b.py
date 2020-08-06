class OnlyNumbersException(Exception):
    def __init__(self, text):
        self.text = text


numbers_list = []
while True:
    new_element = input("Введите число для добавления в список. Введите 'stop' для прекращения ввода: ")
    if new_element == "stop":
        break
    else:
        try:
            if new_element.isnumeric():
                numbers_list.append(int(new_element))
                print("Число добавлено!")
            else:
                raise OnlyNumbersException("Необходимо ввести одно число или 'stop' для прекращения ввода!")
        except OnlyNumbersException as err:
            print(err)
print("Сформированный список:", numbers_list)
