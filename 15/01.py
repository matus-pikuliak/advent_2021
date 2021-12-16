import heapq
import math

dimx = len(next(open('input')).strip())
dimy = dimx

for repeat in {1, 5}:
    cave = dict()

    for i, line in enumerate(open('input')):
        for j, num in enumerate(map(int, line.strip())):
            for a in range(repeat):
                for b in range(repeat):
                    c = num + a + b
                    c -= 9 * (c > 9)
                    cave[i + (a * dimx) + (j + (b * dimy)) * 1j] = c

    heapq.heapify(b := [(0, 0, 0)])
    c = {0: 0}
    end = max(n.real for n in cave) + 1j * max(n.imag for n in cave)

    while end not in c:
        val, a1, a2 = heapq.heappop(b)
        x = a1 + 1j * a2
        if c[x] == val:
            for n in (x + d for d in (-1, 1, -1j, 1j)):
                if n in cave and c.get(n, math.inf) > c[x] + cave[n]:
                    c[n] = c[x] + cave[n]
                    heapq.heappush(b, (c[n], n.real, n.imag))

    print(c[end])