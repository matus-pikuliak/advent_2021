from itertools import product

points = []
for line in open('input'):
    if line.strip():
        if line.startswith('--'):
            points.append(set())
        else:
            points[-1].add(tuple(map(int, line.split(','))))

seed = [list('xyz'), list('zxy'), list('yzx')]
rotations = []
for s in seed:
    for _ in range(4):
        rotations.append(s)
        rotations.append([f'-{s[0]}'.replace('--', ''), s[1], f'-{s[2]}'.replace('--', '')])
        s = [f'{s[1]}'.replace('--', ''), f'-{s[0]}'.replace('--', ''), s[2]]

sw = {
    'x': lambda p: p[0],
    '-x': lambda p: -p[0],
    'y': lambda p: p[1],
    '-y': lambda p: -p[1],
    'z': lambda p: p[2],
    '-z': lambda p: -p[2],
}

done = [points[0]]
done_ids = {0}
done_p = -1
scanners = []

while len(done_ids) != len(points):
    done_p += 1

    for f in range(len(points)):
        if f in done_ids:
            continue
        for r in rotations:
            rotated = [tuple(sw[r[i]](p) for i in range(3)) for p in points[f]]
            for p1, p2 in product(done[done_p], rotated[-11:]):
                pts = set(
                    tuple(p1[i] - p2[i] + p3[i] for i in range(3))
                    for p3 in rotated
                )
                if len(pts & done[done_p]) >= 12:
                    print(f, r, tuple(p1[i] - p2[i] for i in range(3)))
                    scanners.append(tuple(p1[i] - p2[i] for i in range(3)))
                    done.append(pts)
                    done_ids.add(f)
                    break
            else: continue
            break

# Part 1
print(len(set.union(*done)))

# Part 2
print(max(
    sum(abs(s1[i] - s2[i]) for i in range(3))
    for s1, s2 in product(list(set(scanners)), repeat=2)
))
