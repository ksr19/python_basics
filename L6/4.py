class Car:
    is_police = False

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        dir_dict = {'r': 'направо', 'l': 'налево'}
        print(f"Машина повернула {dir_dict[direction]}.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):
    max_speed = 60

    def show_speed(self):
        if self.speed > TownCar.max_speed:
            print(f"Максимально разрешенная скорость - {TownCar.max_speed} км/ч. "
                  f"Текущая скорость - {self.speed} км/ч. Пожалуйста, снизьте скорость!")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class SportCar(Car):
    pass


class WorkCar(Car):
    max_speed = 40

    def show_speed(self):
        if self.speed > WorkCar.max_speed:
            print(f"Максимально разрешенная скорость - {WorkCar.max_speed} км/ч. "
                  f"Текущая скорость - {self.speed} км/ч. Пожалуйста, снизьте скорость!")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class PoliceCar(Car):
    is_police = True


car1 = SportCar(200, 'white', 'Audi')
car2 = TownCar(70, 'silver', 'Volkswagen')
car3 = TownCar(50, 'blue', 'Lada')
car4 = WorkCar(50, 'orange', 'Mini')
car5 = WorkCar(39, 'yellow', 'Subaru')
car6 = PoliceCar(90, 'white', 'Ford')
cars = [car1, car2, car3, car4, car5, car6]
for car in cars:
    print(f"Модель машины - {car.name}. Цвет - {car.color}. Является полицейской - {car.is_police}.")
    car.go()
    car.show_speed()
    car.turn('r')
    car.stop()
