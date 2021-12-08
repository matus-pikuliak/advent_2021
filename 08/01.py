print(sum(
    len(word) in {2, 3, 4, 7}
    for line in open('input')
    for word in line.split('|')[1].split()
))