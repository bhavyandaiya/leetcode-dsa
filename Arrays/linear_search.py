nums = [5, 23, 64, 2, 6, 7, 43, 6, 7, 43, 3, 10]
n = len(nums)
target = 6

def func(nums, target):
    for i in range(0, n):
        if nums[i] == target:
            return i
    else: 
        return -1


print(func(nums, target))