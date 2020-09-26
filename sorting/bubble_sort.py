# merge sortting https://en.wikipedia.org/wiki/Bubble_sort
# time complexity is O(n^2)

import os
import time




def bubble_sort(list_nums):
    swapped = True
    while swapped:
        swapped=False
        for i in range(len(list_nums)-1):
            if list_nums[i] > list_nums[i+1]:
                # swap
                list_nums[i], list_nums[i+1] = list_nums[i+1], list_nums[i]
                # set the flag to loop again
                swapped = True
    return list_nums



if __name__=='__main__':
    # Verify it works
    random_list_of_nums = [120, 45, 68, 250, 176]

    print('Before sorting\n')
    print(random_list_of_nums)

    sorted_list = bubble_sort(random_list_of_nums)

    print('After sorting\n')
    print(sorted_list)

