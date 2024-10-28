"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def func(num):
    for elem in range(2, num):
        if num % elem == 0:
            return False
    return True


def my_gen(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if func(num):
            count += 1
            yield num


print(*my_gen(5))
