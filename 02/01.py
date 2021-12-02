final = sum(
    {'f': 1j, 'd': 1, 'u': -1}[l[0]] * int(l[-2])
    for l in open('input')
)

print(int(final.imag * final.real))
