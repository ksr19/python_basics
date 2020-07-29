class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print(f"Запуск отрисовки. {self.title}.")


class Pen(Stationery):
    def draw(self):
        print(f"Начало отрисовки. Инструмент {self.title}.")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка начинается. Инструмент {self.title}.")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка... Инструмент {self.title}.")


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
