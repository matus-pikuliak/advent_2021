from itertools import permutations

digits = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}


def code_word(word, code):
    return ''.join(sorted('abcdefg'[code.index(c)] for c in word))


def line_value(words):
    for code in permutations('abcdefg'):
        if all(code_word(word, code) in digits for word in words):
            return sum(
                10 ** (3 - i) * digits[code_word(word, code)]
                for i, word in enumerate(words[-4:])
            )

print(sum(
    line_value(line.replace('|', '').split())
    for line in open('input')
))
