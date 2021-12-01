nums = list(map(int, open('input')))

# Part 1
print(sum(
    a > b
    for a, b in zip(nums[1:], nums)
))

# Part 2
print(sum(
    a > b
    for a, b in zip(nums[3:], nums)
))