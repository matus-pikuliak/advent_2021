chardef = [(8, False), (6, True), (8, True), (7, True), (4, False), (9, True), (7, False)]


def chars2digit(chars):
    return next(
        i for i, digit in enumerate(['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'])
        if set(chars) == set(digit)
    )


def code_value(hint, code):
    four_word = next(word for word in hint.split() if len(word) == 4)
    return sum(
        10 ** (3 - i) * chars2digit([
            'abcdefg'[chardef.index((hint.count(c), c in four_word))]
            for c in word
        ])
        for i, word in enumerate(code.split())
    )

print(sum(
    code_value(*line.split('|'))
    for line in open('input')
))



