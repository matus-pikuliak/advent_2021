from itertools import product
from statistics import median
import re

l, r = '([{<', ')]}>'
wrong = set(map(''.join, set(product(l, r)) - set(zip(l, r))))

p1, p2 = 0, set()
for line in open('input').read().splitlines():
    while len(line) > len(line := re.sub(r'\[\]|\(\)|<>|{}', '', line)): pass
    try:
        bracket = line[min(line.index(w) for w in r if w in line)]
        p1 += [3, 57, 1197, 25137][r.index(bracket)]
    except ValueError:
        p2.add(sum((l.index(c) + 1) * 5 ** i for i, c in enumerate(line)))

print(p1, median(p2))
