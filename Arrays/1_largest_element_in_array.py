
arr = [3, 2, 1, 5, 2, 9, 1, 14, 12]
n = len(arr)

# brute-force
# sort first, then return last-element

# def func(arr):
#     arr.sort()
#     return arr[n-1]

# TC:
# sorting: O(N logN)
# SC: O(1)

##########

# optimal
# assume first element as the largest, compare and convert


def func(arr):
    largest = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

# TC:
# we'll just traverse through the array ONCE: O(N)
# SC: O(1)

print(func(arr))