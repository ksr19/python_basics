class DivisionError(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise DivisionError("Делить на ноль нельзя!")
    else:
        print(f"Результат деления: {a / b:.4f}")
except ValueError:
    print("Необходимо ввести числа!")
except DivisionError as err:
    print(err)
