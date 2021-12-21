from itertools import cycle, count

gen = cycle(range(1, 101))
p = [6, 9]
s = [0, 0]
num = 0
pl = 1

for i in count():
    pl = 1 - pl
    p[pl] = (p[pl] + sum(next(gen) for _ in range(3))) % 10
    s[pl] += p[pl] + 1
    if s[pl] >= 1000:
        break

print((i + 1) * min(s) * 3)
