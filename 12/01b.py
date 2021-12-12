from collections import defaultdict

n = defaultdict(lambda: set())

for line in open('input'):
    x, y = line.strip().split('-')
    n[x].add(y)
    n[y].add(x)

small = {node for node in n if node.islower() and node not in {'start', 'end'}}


def make_num(last, visited, double, part2):
    if last == 'start':
        return 0
    if last == 'end':
        return 1
    if last.islower():
        if last not in visited:
            return num(last, visited | {last}, double, part2)
        elif part2 and not double:
            return num(last, small, small, part2)
        else:
            return 0
    return num(last, visited, double, part2)


def num(last, smalls, double, part2=False):
    return sum(
        make_num(node, smalls, double, part2)
        for node in n[last]
    )


print(num('start', set(), None, False))
print(num('start', set(), None, True))
