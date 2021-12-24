al, bl, cl = list(), list(), list()

for i, line in enumerate(open('input')):
    words = line.split()
    if i % 18 == 4:
        al.append(int(words[2]))
    if i % 18 == 5:
        bl.append(int(words[2]))
    if i % 18 == 15:
        cl.append(int(words[2]))


def valid(num):
    gen = map(int, str(num))
    z = 0
    ws = []

    for a, b, c in zip(al, bl, cl):
        if a == 1:
            w = next(gen)
        else:
            w = (z % 26) + b
        if w > 9 or w < 1:
            return
        ws.append(w)
        d = z % 26 + b != w
        z = z // a * ((25 * d) + 1) + (w + c) * d

    if z == 0:
        return ''.join(map(str, ws))


# Part 1
for num in range(9999999, 0, -1):
    if x := valid(num):
        print(x)
        break

# Part 2
for num in range(1111111, 9999999):
    if x := valid(num):
        print(x)
        break
