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
