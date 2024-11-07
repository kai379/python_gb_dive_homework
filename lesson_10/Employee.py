"""
Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
"""
from People import People


class Employee(People):

    def __init__(self, id_employee: str, *args, **kwargs):
        if len(id_employee) == 6:
            self.id_employee = int(id_employee)
        elif len(id_employee) < 6:
            self.id_employee = int(id_employee.zfill(6))
        self.access_lvl = sum(list(map(int, str(self.id_employee)))) % 7
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    emp_01 = Employee('211113', 'FIO', 65)
    print(emp_01.access_lvl)


