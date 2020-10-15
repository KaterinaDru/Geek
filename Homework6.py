# Задание 1
import time


class TrafficLight:

    def __init__(self):
        self.__color = ['красный', 'желтый', 'зеленый']

    @property
    def running(self):
        for i in self.__color:
            yield i


t = TrafficLight()
for i in t.running:
    if i == 'красный':
        print(i)
        time.sleep(7)
    elif i == 'желтый':
        print(i)
        time.sleep(2)
    else:
        print(i)
        time.sleep(5)


# Задание 4

class Car:
    def __init__(self):
        self.speed: int = 70
        self.color: str = ''
        self.name: str = ''
        self.is_police: bool = True

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self, speed):
        print(f'Скорость автомобиля {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость')
        else:
            print(f'Скорость автомобиля {self.speed}')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')
        else:
            print(f'Скорость автомобиля {self.speed}')


main_car = Car()
town_car = TownCar()
work_car = WorkCar()

main_car.go()
town_car.go()
town_car.show_speed()
work_car.show_speed()
main_car.turn('направо')


# Задание 2


class Road:
    _mass = 25
    _thickness = 1

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def formula(self):
        print(self._length * self._width * self._mass * self._thickness)


road_1 = Road(1, 2)
road_1.formula()


