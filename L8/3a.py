import re


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
            regex = re.compile("\-?\d+\.?\d*")
            if new_element not in re.findall(regex, new_element):
                raise OnlyNumbersException("Необходимо ввести одно число или 'stop' для прекращения ввода!")
            else:
                numbers_list.append(float(new_element)) if "." in new_element else numbers_list.append(int(new_element))
                print("Число добавлено!")
        except OnlyNumbersException as err:
            print(err)
print("Сформированный список:", numbers_list)
