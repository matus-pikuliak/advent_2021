from functools import cache

@cache
def c(s, d):
    if d == 0: return open('input').read().count(str(s))
    return c((s + 1) % 9, d - 1) + c(0, d-1) * (s == 6)


for days in (80, 256):
    print(sum(c(i, days) for i in range(9)))

