from collections import Counter, defaultdict

poly = list(next(open('input')).strip())
r = dict(
    line.strip().split(' -> ')
    for line in open('input')
    if '->' in line
)

for i in (10, 40):
    c = Counter(p1+p2 for p1, p2 in zip(poly, poly[1:]))

    for _ in range(i):
        n = defaultdict(lambda: 0)
        for k, v in c.items():
            n[k[0]+r[k]] += v
            n[r[k]+k[1]] += v
        c = n

    chars = [
        (sum(v * k.count(ch) for k, v in c.items()) + 1) // 2
        for ch in set(r.values())
    ]
    print(max(chars) - min(chars))
