a, b, c = input(), input(), input()
# 2 5 8
MAX_LEN = max(len(a), len(b), len(c))
MIN_LEN = min(len(a), len(b), len(c))
SUM_LEN = len(a) + len(b) + len(c)
if MAX_LEN == SUM_LEN - MIN_LEN - MAX_LEN + (SUM_LEN - MIN_LEN - MAX_LEN) - MIN_LEN:
    print('YES')
else:
    print('NO')
