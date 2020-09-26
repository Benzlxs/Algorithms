# merge sortting https://en.wikipedia.org/wiki/Quicksort
# time complexity is O(nlog(n))

import os
import time


def partition(nums, low, high):
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(list_nums):

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(list_nums, 0, len(list_nums)-1)


if __name__=='__main__':
    # Verify it works
    random_list_of_nums = [120, 45, 68, 250, 176]

    print('Before sorting\n')
    print(random_list_of_nums)

    quick_sort(random_list_of_nums)

    print('After sorting\n')
    print(random_list_of_nums)

