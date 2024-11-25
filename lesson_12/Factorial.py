"""
Задание №1.
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
Задание №2.
Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""
import os
import json


class Factorial:

    def __init__(self, num_of_values: int, name: str):
        self.num_of_values = num_of_values
        self._history = []
        self.name = name + '.json'

    @staticmethod
    def _factorial(number: int) -> int:
        fact_res = 1
        if number in (0, 1):
            return fact_res
        for i in range(2, number + 1):
            fact_res *= i
        return fact_res

    def show_history(self):
        print('----------')
        print(f'Для {self} вывожу {len(self._history)} значений(ие):')
        for i in self._history:
            print(f'Значение = {i[0]} -> результат {i[1]}')
        print('----------\n')

    def __call__(self, fuct_number: int) -> int:
        fact_res = self._factorial(fuct_number)
        if not self._history:
            self._history.append((str(fuct_number), fact_res))
        elif len(self._history) < self.num_of_values:
            self._history.append((str(fuct_number), fact_res))
        else:
            self._history.append((str(fuct_number), fact_res))
            del self._history[0]
        return fact_res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dict_val = {}
        if len(self._history) == self.num_of_values:
            for i in self._history:
                dict_val[str(i[0])] = i[1]
            with open(self.name, 'w', encoding='UTF-8') as file:
                json.dump(dict_val, file)
        else:
            if os.path.exists(self.name) and os.stat(self.name).st_size != 0:
                with open(self.name, 'r', encoding='UTF-8') as json_file:
                    dict_val = json.load(json_file)
            list_val = []
            dict_val2 = {}
            for i in dict_val.items():
                list_val.append(i)
            for i in self._history:
                list_val.append((i[0], i[1]))
            if len(list_val) < self.num_of_values:
                for i in list_val[-len(list_val):]:
                    dict_val2.update({i[0]: i[1]})
            else:
                for i in list_val[-self.num_of_values:]:
                    dict_val2.update({i[0]: i[1]})
            with open(self.name, 'w', encoding='UTF-8') as file:
                json.dump(dict_val2, file)


if __name__ == '__main__':
    with Factorial(3, 'var_1') as var_1:
        var_1(10)
