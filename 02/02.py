dep, hor, aim = 0, 0, 0

for line in open('input'):
    c, i = line[0], int(line[-2])
    if c == 'f':
        hor += i
        dep += i * aim
    else:
        aim += i * {'d': 1, 'u': -1}[c]

print(dep * hor)