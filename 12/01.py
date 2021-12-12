from collections import defaultdict

n = defaultdict(lambda: set())

for line in open('input'):
    x, y = line.strip().split('-')
    n[x].add(y)
    n[y].add(x)

small = {node for node in n if node.islower() and node not in {'start', 'end'}}


def num(path, part2=False):
    if path[-1] == 'end':
        return 1

    return sum(
        num(path + [node], part2)
        for node in n[path[-1]]
        if (
            not node.islower() or
            node not in path or
            part2 and node in small and max(path.count(sm) for sm in small) == 1
        )
    )


print(num(['start']))
print(num(['start'], part2=True))
