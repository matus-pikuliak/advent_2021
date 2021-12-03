rows = open('input').readlines()


def c(pref):
    return sum(r.startswith(pref) for r in rows)


def find(most):
    code = ''
    while c(code) > 1:
        code += {most: '1', not most: '0'}[c(code + '1') >= c(code + '0')]
    final = next(r for r in rows if r.startswith(code))
    return int(final, 2)


print(find(True) * find(False))
