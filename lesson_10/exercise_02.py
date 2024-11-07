"""
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""


class Rectangle:

    def __init__(self, side_a: int | float, side_b: int | float | None = None):
        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b

    def perimeter_of_a_rectangle(self) -> int | float:
        return 2 * (self.side_a + self.side_b)

    def area_of_a_rectangle(self) -> int | float:
        return self.side_a * self.side_b


rec_1 = Rectangle(10, 2)
rec_2 = Rectangle(20, None)
print(f'{rec_1.perimeter_of_a_rectangle()}, {rec_2.area_of_a_rectangle()}')
print(f'{rec_2.perimeter_of_a_rectangle()}, {rec_2.area_of_a_rectangle()}')
