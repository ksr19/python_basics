class Cell:
    def __init__(self, name, nucleus):
        self.name = name
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell('+'.join([self.name, other.name]), self.nucleus + other.nucleus)

    def __sub__(self, other):
        return Cell('-'.join([self.name, other.name]),
                    self.nucleus - other.nucleus) if self.nucleus > other.nucleus else "Операция не определена."

    def __mul__(self, other):
        return Cell('*'.join([self.name, other.name]), self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell('/'.join([self.name, other.name]),
                    self.nucleus // other.nucleus) if self.nucleus // other.nucleus > 0 else "Операция не определена."

    def __str__(self):
        return f"Количество ячеек в клетке {self.name}: {self.nucleus}."

    @property
    def nucleus(self):
        return self.__nucleus

    @nucleus.setter
    def nucleus(self, nucleus):
        if type(nucleus) == str or nucleus < 1:
            raise ParameterError
        elif type(nucleus) == float:
            self.__nucleus = int(round(nucleus, 0))
        else:
            self.__nucleus = int(nucleus)

    def make_order(self, row_length):
        print(
            f"\nПредставление клетки {self.name}. Ячеек в клетке {self.nucleus}. Количество ячеек в ряду {row_length}:")
        obj = IterObj(self.nucleus, row_length)
        for el in obj:
            print(el, end='')


class Iterator:
    def __init__(self, finish, length, start=0):
        self.finish = finish
        self.length = length
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= self.finish:
            return "*" if self.i % self.length != 0 else "*\n"
        else:
            raise StopIteration


class IterObj:
    def __init__(self, finish, length, start=0):
        self.finish = finish
        self.length = length
        self.start = start

    def __iter__(self):
        return Iterator(self.finish, self.length, self.start)


class ParameterError(Exception):
    pass


try:
    cell1 = Cell("Cell1", 21.7)
    print(cell1)
    cell2 = Cell("Cell2", 12.8)
    print(cell2)
    print(f"Сложение клеток -- {cell1 + cell2}")
    print(f"Вычитание клеток -- {cell1 - cell2}")
    print(f"Умножение клеток -- {cell1 * cell2}")
    print(f"Деление клеток -- {cell1 / cell2}")
    cell1.make_order(8)
    cell1.make_order(4)
    cell2.make_order(8)
    cell2.make_order(4)
    (cell1 + cell2).make_order(8)
    (cell1 * cell2).make_order(50)
except ParameterError:
    print("Произошла ошибка! Число ячеек должно быть положительным целым числом!")
