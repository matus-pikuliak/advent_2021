from itertools import chain

lines = open('input').read().splitlines()

o = {int(n): i for i, n in enumerate(lines[0].split(','))}
boards_ver = [
    [list(map(int, l.split())) for l in b]
    for b in zip(*[lines[i::6] for i in range(2, 7)])
]
boards_hor = [list(zip(*b)) for b in boards_ver]


def calculate(board):
    steps = min(max(o[num] for num in row) for row in board)
    score = sum(num for num in chain(*board) if o[num] > steps)
    score *= next(k for k, v in o.items() if v == steps)
    return steps, score


# Part 1
print(min(map(calculate, boards_ver + boards_hor)))

# Part 2
print(max(
    min(calculate(b1), calculate(b2))
    for b1, b2
    in zip(boards_ver, boards_hor)
))