from collections import Counter


def find(most):
    rows = open('input').readlines()
    for i in range(12):
        c = Counter(r[i] for r in rows)
        rows = [
            r for r in rows
            if (r[i] == '1') != (c['1'] >= c['0']) ^ most
        ]
        if len(rows) == 1:
            return rows[0]


print(int(find(True), 2) * int(find(False), 2))

