from math import prod
from operator import gt, lt, eq

packet = ''.join(
    bin(int(char, 16))[2:].zfill(4)
    for char in open('input').read()
)


def b2i(start, end):
    return int(packet[start:end], 2)


def process(p):
    vs_sum = b2i(p, p+3)
    type_id = b2i(p+3, p+6)
    p += 6
    if type_id == 4:
        val = 0
        while True:
            val = val * 16 + b2i(p+1, p+5)
            p += 5
            if packet[p - 5] == '0':
                break
    else:
        vals = []
        i = int(packet[p])
        p += 1
        if i:
            num = b2i(p, p+11)
            p += 11
            for _ in range(num):
                p, vs, val = process(p)
                vals.append(val)
                vs_sum += vs
        else:
            num = b2i(p, p+15) + p + 15
            p += 15
            while p < num:
                p, vs, val = process(p)
                vals.append(val)
                vs_sum += vs

        if type_id < 4:
            val = {0: sum, 1: prod, 2: min, 3: max}[type_id](vals)
        else:
            val = {5: gt, 6: lt, 7: eq}[type_id](*vals)

    return p, vs_sum, val


# _, part1, part2
print(process(0))
