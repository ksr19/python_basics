class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i." if self.b >= 0 else f"{self.a} - {abs(self.b)}i."

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


first_number = ComplexNumber(4, 5)
second_number = ComplexNumber(-2, -3)
print(f"Первое комплексное число: {first_number}")
print(f"Второе комплексное число: {second_number}")
print(f"Сумма двух чисел: {first_number + second_number}")
print(f"Произведение двух чисел: {first_number * second_number}")
