"""
Задание №1.
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""


class Factorial:

    def __init__(self, num_of_values: int):
        self.num_of_values = num_of_values
        self._history = []

    def _factorial(self, number: int) -> int:
        fact_res = 1
        if self.num_of_values in (0, 1):
            return fact_res
        for i in range(2, number + 1):
            fact_res *= number
        return fact_res

    def show_history(self):
        print('----------')
        print(f'Для {self} вывожу {len(self._history)} значений(ие): \n')
        for i in self._history:
            print(f'Значение {i[0]} - результат {i[1]}')
        print('----------')

    def __call__(self, number: int) -> int:
        fact_res = self._factorial(number)
        if not self._history:
            self._history.append((number, fact_res))
        elif len(self._history) < self.num_of_values:
            self._history.append((number, fact_res))
        else:
            self._history.append((number, fact_res))
            del self._history[0]
        return fact_res


if __name__ == '__main__':
    var_1 = Factorial(3)
    var_1(3)
    var_1.show_history()
    var_1(4)
    var_1.show_history()
    var_1(5)
    var_1.show_history()
    var_1(6)
    var_1.show_history()
    var_1(7)
    var_1.show_history()
