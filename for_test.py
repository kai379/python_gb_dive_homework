tuple1 = (1, 2, 3, [1, 2, 3, 4])
print(tuple1)
tuple1[3][0] = 99
print(tuple1)
# hash(tuple1)
set_1 = {tuple1[2]: tuple1[0]}
print(set_1)
