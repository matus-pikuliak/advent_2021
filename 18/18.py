from copy import deepcopy
from functools import reduce
from itertools import permutations


def add_left(x, val):
    if isinstance(x, int): return x + val
    return [add_left(x[0], val), x[1]]


def add_right(x, val):
    if isinstance(x, int): return x + val
    return [x[0], add_right(x[1], val)]


def explode(x, d):
    if isinstance(x, list):
        if d == 3:
            if isinstance(x[0], list):
                a, b = x[0]
                x[0] = 0
                x[1] = add_left(x[1], b)
                return True, a, 0
            elif isinstance(x[1], list):
                a, b = x[1]
                x[0] = add_right(x[0], a)
                x[1] = 0
                return True, 0, b
        else:
            v, l, r = explode(x[0], d + 1)
            if v and r:
                x[1] = add_left(x[1], r)
                return v, 0, 0
            if v:
                return v, l, r
            v, l, r = explode(x[1], d + 1)
            if v and l:
                x[0] = add_right(x[0], l)
                return v, 0, 0
            return v, l, r
    return False, 0, 0


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, x - x // 2]
        else:
            return False, x
    else:
        v, x[0] = split(x[0])
        if not v:
            v, x[1] = split(x[1])
        return v, x


def add(a, b):
    x = [deepcopy(a), deepcopy(b)]
    while True:
        if explode(x, 0)[0]: continue
        if split(x)[0]: continue
        break
    return x


def magnitude(x):
    if isinstance(x, int): return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


nums = list(map(eval, open('input')))

# Part 1
print(magnitude(reduce(add, nums)))

# Part 2
print(max(
    magnitude(add(a, b))
    for a, b in permutations(nums, 2)
))
