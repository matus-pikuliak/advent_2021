points, folds = open('input').read().split('\n\n')
points = set(
    tuple(line.split(','))
    for line in points.split()
)

for i, fold in enumerate(folds.split('\n')):
    dim = fold.split('=')[0][-1]
    num = int(fold.split('=')[1])
    for p in set(points):
        val, imag = {
            'y': (p.imag, 1j),
            'x': (p.real, 1)
        }[dim]
        if val > num:
            points.add(p - imag * 2 * (val - num))
            points.remove(p)
    if not i:
        print(len(points))

for i in range(10):
    for j in range(100):
        print('#' if j + 1j * i in points else ' ', end='')
    print()

