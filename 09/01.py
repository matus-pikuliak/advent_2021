import math

nums = {
    i + 1j * j: num + 1
    for i, line in enumerate(open('input').read().splitlines())
    for j, num in enumerate(map(int, line))
}

print(sum(
    nums[ad]
    for ad in nums
    if all(nums.get(ad + d, math.inf) > nums[ad] for d in (1, -1, 1j, -1j))
))
