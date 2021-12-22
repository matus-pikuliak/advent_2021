import re
from functools import partial

lights = list()


def add(coord):
    for l in lights:
        if overlap(l, coord):
            for part in minus(coord, l):
                add(part)
            return
    lights.append(coord)


def remove(coord):
    overlapping = list(filter(partial(overlap, coord), lights))
    for l in overlapping:
        lights.remove(l)
        lights.extend(minus(l, coord))


def overlap(l1, l2):
    def overlap_1d(x1, x2, y1, y2):
        return x2 >= y1 and x1 <= y2

    return overlap_1d(l1[0], l1[1], l2[0], l2[1]) and overlap_1d(l1[2], l1[3], l2[2], l2[3]) and overlap_1d(l1[4], l1[5], l2[4], l2[5])


def minus(l1, l2):
    l1 = list(l1)
    l2 = list(l2)
    if l1[0] < l2[0]:
        yield l1[0], l2[0]-1, l1[2], l1[3], l1[4], l1[5]
        l1[0] = l2[0]
    if l1[1] > l2[1]:
        yield l2[1]+1, l1[1], l1[2], l1[3], l1[4], l1[5]
        l1[1] = l2[1]
    if l1[2] < l2[2]:
        yield l1[0], l1[1], l1[2], l2[2]-1, l1[4], l1[5]
        l1[2] = l2[2]
    if l1[3] > l2[3]:
        yield l1[0], l1[1], l2[3]+1, l1[3], l1[4], l1[5]
        l1[3] = l2[3]
    if l1[4] < l2[4]:
        yield l1[0], l1[1], l1[2], l1[3], l1[4], l2[4]-1
        l1[4] = l2[4]
    if l1[5] > l2[5]:
        yield l1[0], l1[1], l1[2], l1[3], l2[5]+1, l1[5]


for line in open('input'):
    nums = list(map(int, re.findall(r'[-\d]+', line)))
    nums = (
        min(nums[0:2]), max(nums[0:2]),
        min(nums[2:4]), max(nums[2:4]),
        min(nums[4:6]), max(nums[4:6]),
    )
    if line.startswith('on'):
        add(nums)
    else:
        remove(nums)

print(sum(
    (l[1] - l[0] + 1) * (l[3] - l[2] + 1) * (l[5] - l[4] + 1)
    for l in lights
))



