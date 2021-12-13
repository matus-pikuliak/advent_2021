points, folds = open('input').read().split('\n\n')
points = list(
    list(map(int, line.split(',')))
    for line in points.split()
)

for i, fold in enumerate(folds.split('\n')):
    dim, num = fold.split('=')
    dim = dim[-1] == 'y'
    num = int(num)
    for p in points:
        p[dim] -= 2 * (p[dim] - num) * (p[dim] > num)
    if not i:
        print(len(set(map(tuple, points))))

points = set(map(tuple, points))
for i in range(10):
    for j in range(100):
        print('#' if (j, i) in points else ' ', end='')
    print()

