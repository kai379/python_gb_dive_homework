# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input())
n_after_hex = hex(num)
values_hex = '0123456789ABCDEF'
n_hex = ''
HEX = 16
while num > 0:
    n_hex = values_hex[num % 16] + n_hex
    num //= 16

print(f'Шестнадцатеричное представление числа: {n_hex}')
print(f'Проверка результата: {n_after_hex}')