from itertools import chain

lines = open('input').read().splitlines()

o = lines[0].split(',')
boards = [
    [l.split() for l in b]
    for b in zip(*[lines[i::6] for i in range(2, 7)])
]


def score(board):
    return min(score_rows(board), score_rows(list(zip(*board))))


def score_rows(board):
    steps = min(max(o.index(num) for num in row) for row in board)
    score = sum(int(num) for num in chain(*board) if o.index(num) > steps) * int(o[steps])
    return steps, score


# Part 1
print(min(map(score, boards)))

# Part 2
print(max(map(score, boards)))
