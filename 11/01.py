from itertools import product, count

x = {
    i + 1j*j: num
    for i, line in enumerate(open('input'))
    for j, num in enumerate(map(int, line.strip()))
}
c = 0


def explode(octo, x):
    x[octo] = 0
    c = 1
    for i, j in product([1, 0, -1], repeat=2):
        if (n := octo + i + 1j * j) in x:
            x[n] += 1 * (x[n] > 0)
            c += x[n] > 9 and explode(n, x)
    return c


def step(x, c):
    for octo in x:
        x[octo] += 1
    while (octo := next((o for o, val in x.items() if val > 9), None)) is not None:
        c += explode(octo, x)
    return x, c


for i in count():
    x, c = step(x, c)

    if i == 99:
        print('part 1:', c)

    if not any(x.values()):
        print('part 2:', i + 1)
        break
