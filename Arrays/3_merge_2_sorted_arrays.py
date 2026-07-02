nums1 = [1, 1, 1, 2, 4, 6, 7]
nums2 = [1, 1, 2, 4, 5, 7, 8, 9, 10]

def func(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i = nums1[0]
    j = nums2[0]
    merged = []
    while i < n and j < m:
        if (nums1[i] <= nums2[j]):
            if len(merged) == 0 or merged[-1] != nums1[i]:      # first if to check if merged is empty, second if if merged has 1 or more elemetns
                merged.append(nums1[i])
            i+=1 
        else:
            if len(merged) == 0 or merged[-1] != nums2[j]:
                merged.append(nums2[j])
            j+=1
    
    # now if either i or j exhausts, we want to simply check merged and append
    while i < n:
        if len(merged) == 0 or merged[-1] != nums1[i]:      # first if to check if merged is empty, second if if merged has 1 or more elemetns
            merged.append(nums1[i])
        i+=1

    while j < m:
        if len(merged) == 0 or merged[-1] != nums2[j]:
            merged.append(nums2[j])
        j+=1        

    return merged

print(func(nums1, nums2))


# TC: O(n+m)    -> len of both arrays
# SC: O(1)      -> nothing being stored