from time import sleep


class TrafficLight:
    __color = 'red'

    def running(self):
        while True:
            print(f"\033[30m\033[41m{self.__color}")
            sleep(7)
            self.__color = 'yellow'
            print(f"\033[30m\033[43m{self.__color}")
            sleep(2)
            self.__color = 'green'
            print(f"\033[30m\033[42m{self.__color}")
            sleep(7)
            self.__color = 'yellow'
            print(f"\033[30m\033[43m{self.__color}")
            sleep(2)
            self.__color = 'red'


tl = TrafficLight()
tl.running()
