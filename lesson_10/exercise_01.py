"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.
"""
from math import pi


class Circle:

    def __init__(self, rad: int|float):
        self.rad = rad

    def circumference(self):
        return 2 * pi * self.rad

    def area_of_a_circle(self):
        return pi * self.rad ** 2


cir_1 = Circle(10)
print(f'{cir_1.circumference()=}, {cir_1.area_of_a_circle()=}')
