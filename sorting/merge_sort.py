# merge sortting https://en.wikipedia.org/wiki/Merge_sort

import os
import time




def merge(left, right):
    # merging two parts
    sorted_list = []
    left_idx = right_idx = 0

    left_len, right_len = len(left), len(right)

    while (left_idx < left_len) and (right_idx < right_len):
        if left[left_idx] <= right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

    # merging together
    sorted_list = sorted_list + left[left_idx:] + right[right_idx:]

    return sorted_list




def merge_sort(list_nums):

    if len(list_nums) <= 1:
        return list_nums


    mid = len(list_nums) // 2

    left = merge_sort(list_nums[:mid])
    right = merge_sort(list_nums[mid:])

    return merge(left, right)



if __name__=='__main__':
    # Verify it works
    random_list_of_nums = [120, 45, 68, 250, 176]

    print('Before sorting\n')
    print(random_list_of_nums)

    sorted_list = merge_sort(random_list_of_nums)

    print('After sorting\n')
    print(sorted_list)

