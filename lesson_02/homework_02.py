# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

frac1 = "1/2"
num1, den1 = frac1.split("/")
print(num1, den1)
frac2 = "1/3"
num2, den2 = frac2.split("/")
print(num2, den2)
sum_of_num = Fraction(frac1) + Fraction(frac2)
prod_of_num = Fraction(frac1) * Fraction(frac2)
print(f'Сумма дробей: {Fraction(int(num1), int(den1)) + Fraction(int(num2), int(den2))}')
print(f'Произведение дробей: {Fraction(int(num1), int(den1)) * Fraction(int(num2), int(den2))}')
print(f'Сумма дробей: {sum_of_num}')
print(f'Произведение дробей: {prod_of_num}')
