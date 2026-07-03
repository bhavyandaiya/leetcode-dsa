nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1]
n = len(nums)


def func(nums):
    ctr = 0
    max_ctr = 0

    for i in range(0, n):
        if nums[i] == 1:
            ctr += 1
        else:
            max_ctr = max(max_ctr, ctr)
            ctr = 0

    return max_ctr

print(func(nums))
        