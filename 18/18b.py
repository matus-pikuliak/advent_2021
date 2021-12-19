from functools import reduce
from itertools import permutations


def read_line(s):
    x = []
    d = 0
    for c in s:
        d += {'[': 1, ']': -1}.get(c, 0)
        if c.isdigit():
            x.append(int(c) + 1j * d)
    return x


def explode(x):
    try:
        idx = next(i for i, val in enumerate(x) if val.imag == 5)
        a, b = x[idx].real, x[idx+1].real
        if idx - 1 >= 0:
            x[idx - 1] += a
        if idx + 2 < len(x):
            x[idx + 2] += b
        x.pop(idx + 1)
        x[idx] = 4j
        return True
    except StopIteration:
        return False


def split(x):
    try:
        idx = next(i for i, val in enumerate(x) if val.real >= 10)
        val, dep = x[idx].real, x[idx].imag
        x[idx] = val // 2 + 1j * (dep + 1)
        x.insert(idx + 1, val - val // 2 + 1j * (dep + 1))
        return True
    except StopIteration:
        return False


def add(a, b):
    x = [v + 1j for v in a] + [v + 1j for v in b]
    while True:
        if explode(x): continue
        if split(x): continue
        break
    return x


def magnitude(x):
    for d in range(4, 0, -1):
        while True:
            try:
                idx = next(i for i, val in enumerate(x) if val.imag == d)
                x[idx] = 3 * x[idx].real + 2 * x[idx + 1].real + 1j * (d - 1)
                x.pop(idx + 1)
            except StopIteration:
                break
    return int(x[0].real)


nums = list(map(read_line, open('input')))

# Part 1
print(magnitude(reduce(add, nums)))

# Part 2
print(max(
    magnitude(add(a, b))
    for a, b in permutations(nums, 2)
))
