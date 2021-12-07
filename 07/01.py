crabs = list(map(int, open('input').read().split(',')))

# Part 1
print(min(
    sum(abs(c - i) for c in crabs)
    for i in range(max(crabs))
))

# Part 2
print(min(
    sum((d := abs(c - i)) * (d + 1) // 2 for c in crabs)
    for i in range(max(crabs))
))
