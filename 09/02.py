import math
from collections import Counter

nums = {
    i + 1j * j: num
    for i, line in enumerate(open('input').read().splitlines())
    for j, num in enumerate(map(int, line))
}


def find_min(ad):
    return next(
        (
            find_min(ad + d)
            for d in (1, -1, 1j, -1j)
            if nums.get(ad + d, math.inf) < nums[ad]
        ),
        ad
    )


c = Counter(find_min(ad) for ad in nums if nums[ad] < 9).most_common(3)
print(c[0][1] * c[1][1] * c[2][1])
