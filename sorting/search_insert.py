def binary_search(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, x, low, mid-1)

        else:
            return binary_search(array, x, mid + 1, high)

    else:
        return low


def search_insert(nums, target):
    return binary_search(nums, target, 0, len(nums) - 1)