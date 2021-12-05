from collections import Counter
from itertools import chain

lines = [
    list(map(int, line.replace(' -> ', ',').split(',')))
    for line in open('input')
]


def points(line):
    a, b, c, d = line
    steps = abs(a - c) or abs(b - d)
    dx = (2 * (a < c) - 1) * (a != c)
    dy = (2 * (b < d) - 1) * (b != d)
    return [
        (a + i * dx, b + i * dy)
        for i in range(steps + 1)
    ]

# Part 1
counts = Counter(chain.from_iterable(
    points(line)
    for line in lines
    if line[0] == line[2] or line[1] == line[3]
))
print(sum(v > 1 for v in counts.values()))

# Part 2
counts = Counter(chain.from_iterable(map(points, lines)))
print(sum(v > 1 for v in counts.values()))
