"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку. При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов list-архивы также являются свойствами экземпляра
"""


class Archive:
    """ Класс с сохранением истории свойств в списке archive """
    archive = []

    def __init__(self, num: int, string: str):
        self.num = num
        self.string = string
        self.archive = Archive.archive.copy()
        Archive.archive.append(self)

    def __repr__(self):
        return f'Archive({self.num}, {self.string})'

    def __str__(self):
        return f'Это экземпляр класса Archive с числом {self.num} и строкой {self.string}'


p1 = Archive(1, 'a')
p2 = Archive(2, 'b')
p3 = Archive(3, 'c')

print(p1)
print(p2.archive)
print(p3.archive)
