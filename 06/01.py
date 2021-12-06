for days in (80, 256):
    gen = [open('input').read().count(str(i)) for i in range(9)]
    for _ in range(days):
        gen = [gen[(i + 1) % 9] for i in range(9)]
        gen[6] += gen[8]
    print(sum(gen))
