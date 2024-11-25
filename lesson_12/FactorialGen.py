"""
Задание №3.
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactorialGen:

    def __init__(self, *args):
        self.start, self.step = 1, 1
        if len(args) == 1:
            self.stop = args[0] + 1
        elif len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
        else:
            self.start, self.stop, self.step, *_ = args

    @staticmethod
    def _factorial(number: int) -> int:
        if number in (0, 1):
            return 1
        fact_res = 1
        for i in range(2, number + 1):
            fact_res *= i
        return fact_res

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.stop:
            raise StopIteration
        for fact_return in range(self.start, self.stop):
            self.result = self._factorial(fact_return)
            self.start += self.step
            return self.result


gen_fact = FactorialGen(2, 10, 2)

for i in gen_fact:
    print(i)
