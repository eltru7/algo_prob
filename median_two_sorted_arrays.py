import math
from merge_two_sorted_arrays import merge_try_2

def find_median_sorted_arrays(nums1, nums2):

    merged_array = merge_try_2(nums1, len(nums1), nums2, len(nums2))
    median = 0
    index = 0

    length = len(merged_array)

    if length == 1:
        return merged_array[0]

    if length % 2 == 0:
        index = math.ceil(length / 2) - 1
        median = (merged_array[index] + merged_array[index + 1]) / 2
    else:
        index = math.ceil(length / 2) - 1
        median = merged_array[index]

    return median
