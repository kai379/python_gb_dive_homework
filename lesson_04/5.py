name = ['Al', 'Ev', 'Nik']
proc = ['10', '11', '50']
zp = [10_000, 50_000, 3_000_000]

res = dict([(i[0], i[1] * int(i[2])) for i in zip(name, zp, proc)])
print(res)
