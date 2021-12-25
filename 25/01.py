from itertools import count

r = set()
d = set()

for i, line in enumerate(open('input').read().splitlines()):
    for j, c in enumerate(line):
        if c == 'v':
            d.add(i + 1j * j)
        if c == '>':
            r.add(i + 1j * j)


def right(p):
    if p.imag == j:
        return p.real
    return p + 1j


def down(p):
    if p.real == i:
        return p.imag * 1j
    return p + 1


for step in count(1):
    rd = r | d
    mvr = set(p for p in r if right(p) not in rd)
    r = r - mvr | set(map(right, mvr))

    rd = r | d
    mvd = set(p for p in d if down(p) not in rd)
    d = d - mvd | set(map(down, mvd))

    if not mvr and not mvd:
        break

print(step)
