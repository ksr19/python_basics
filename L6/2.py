class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, road_height, asphalt_sqm_weight):
        return round(self._length * self._width * asphalt_sqm_weight * road_height / 1000, 2)


try:
    test_road = Road(5000, 20)
    road_height = float(input("Введите толщину дорожного полотна в см: "))
    asphalt_sqm_weight = float(input("Введите массу в кг асфальта для покрытия 1 кв.м. дороги асфальтом толщиной "
                                     "в 1 см : "))
    print(f"Масса асфальта для покрытия дорожного полотна длиной {test_road._length} метров "
          f"и шириной {test_road._width} метров: {test_road.asphalt_weight(road_height, asphalt_sqm_weight)} тонн.")
except ValueError:
    print("Вводимые параметры должны быть числовыми!")
