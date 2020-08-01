from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def fabric(self):
        pass

    def __add__(self, other):
        return self.fabric + other.fabric


class Coat(Clothes):
    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 42:
            self.__v = 42
        elif v > 60:
            self.__v = 60
        else:
            self.__v = v

    @property
    def fabric(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1.2:
            self.__h = 1.2
        elif h > 2.5:
            self.__h = 2.5
        else:
            self.__h = h

    @property
    def fabric(self):
        return self.h * 2 + 0.3


c = Coat(52)
s = Suit(1.75)

print(f"Ткани потребуется на пальто: {c.fabric:.2f} метров.")
print(f"Ткани потребуется на костюм: {s.fabric:.2f} метров.")
print(f"Итого ткани потребуется: {c + s:.2f} метров.")
