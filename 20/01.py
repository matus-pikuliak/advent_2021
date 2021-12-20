code = next(open('input'))

points = set(
    i + 1j * j
    for i, line in enumerate(open('input').readlines()[2:])
    for j, c in enumerate(line.strip())
    if c == '#'
)

for step in range(50):
    points = set(
        i + 1j * j
        for i in range(-100+step, 200-step)
        for j in range(-100+step, 200-step)
        if code[
            int(''.join(
                str(int(p in points))
                for p in [i + 1j * j + d for d in [-1-1j, -1, -1+1j, -1j, 0, 1j, 1-1j, 1, 1+1j]]),
            2)
        ] == '#'
    )

    if step in {1, 49}:
        print(len(points))