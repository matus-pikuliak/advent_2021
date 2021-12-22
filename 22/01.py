import re

on = set()
for line in open('input'):
    nums = list(map(int, re.findall(r'[-\d]+', line)))
    nums = (
        min(nums[0:2]), max(nums[0:2]),
        min(nums[2:4]), max(nums[2:4]),
        min(nums[4:6]), max(nums[4:6]),
    )
    if any(abs(i) > 50 for i in nums):
        break
    lights = set(
        (x, y, z)
        for x in range(nums[0], nums[1]+1)
        for y in range(nums[2], nums[3]+1)
        for z in range(nums[4], nums[5]+1)
    )
    if line.startswith('on'):
        on |= lights
    else:
        on -= lights
    print(len(on))
