from itertools import product
from statistics import median

l, r = '([{<', ')]}>'
wrong = set(map(''.join, set(product(l, r)) - set(zip(l, r))))

p1, p2 = 0, set()
for line in open('input').read().splitlines():
    while len(line) > len(line := line.replace('<>', '').replace('[]', '').replace('{}', '').replace('()', '')): pass
    try:
        bracket = line[min(line.index(w) for w in wrong if w in line) + 1]
        p1 += dict(zip(r, [3, 57, 1197, 25137]))[bracket]
    except ValueError:
        p2.add(sum((l.index(c) + 1) * 5 ** i for i, c in enumerate(line)))

print(p1, median(p2))
