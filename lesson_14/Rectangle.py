"""
Задание №5.
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем длину и ширину.
При вычитании не допускайте отрицательных значений.
"""
from functools import total_ordering


@total_ordering
class Rectangle:

    def __init__(self, side_a: int | float, side_b: int | float | None = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def perimeter(self) -> int | float:
        return 2 * (self.side_a + self.side_b)

    def area(self) -> int | float:
        return self.side_a * self.side_b

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)

    def __sub__(self, other):
        pass

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()

    def __str__(self):
        return f'Это экз река {self.side_a} - {self.side_b}'


rec_1 = Rectangle(10, 20)
rec_2 = Rectangle(5, 9)
print(rec_1 > rec_2)
print(rec_1 < rec_2)
print(rec_1 == rec_2)
