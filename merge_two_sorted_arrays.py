def merge_try_1(nums1, m, nums2, n):
    i = 0
    j = 0
    merged_array = []

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            merged_array.append(nums1[i])
            i += 1
        elif nums1[i] > nums2[j]:
            merged_array.append(nums2[j])
            j += 1
        else:
            merged_array.append(nums1[i])
            merged_array.append(nums2[j])
            i+=1
            j+=1

    if i < m:
        merged_array.append()

    if j < n:
        merged_array.append()

    nums1 = merged_array

    return nums1

def merge_try_2(nums1, m, nums2, n):
    i = 0
    j = 0

    while i < m and j < n:

        if nums1[i] <= nums2[j]:
            i += 1
        else:
            nums1.insert(i, nums2[j])
            j += 1
            m += 1

    if j < n:
        nums1 += nums2[j: n]

    return nums1




