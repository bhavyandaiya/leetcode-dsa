# leetcode 268: find missing num in nums[]

nums = [1, 2, 3, 4, 0]
n = len(nums)

# brute force approach
# def func(nums):
#     n = len(nums)
#     for i in range(n + 1):
#         if i not in nums:
#             return i

# # better approach
# def func(nums):
#     hash_map = {}
#     for i in range(0, n+1):
#         hash_map[i] = 0
#     for num in nums:
#         hash_map[num] += 1
#     for k, v in hash_map.items():
#         if v==0:
#             return k

# optimal solution
def func(nums):
    return int(n*(n+1)/2 - sum(nums))

print(func(nums))