gamma = sum(
    2 ** (11 - i)
    for i, col in enumerate(zip(*open('input')))
    if sum(map(int, col)) > len(col) / 2
)
print(gamma * (gamma ^ (2 ** 12 - 1)))