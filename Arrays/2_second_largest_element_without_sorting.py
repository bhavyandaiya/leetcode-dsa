arr = [1, 2, 4, 7, 7, 5]
n = len(arr)

# # brute-force
# # sort -> largest = arr[n-1], second largest = element smaller than largest (not equivalent allowed, hence this approach)

# def func(arr):
#     arr.sort()
#     largest = arr[n-1]
#     for i in range(n-2, 0, -1):
#         if arr[i] != largest:
#             second_largest = arr[i]
#             break
#     return second_largest

# print(func(arr))

# # TC: 
# # sorting: O(N logN)
# # for loop: O(N)

# optimal solution
# first pass (same as q1)

